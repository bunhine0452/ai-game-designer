#!/usr/bin/env python3
"""game-design-charts: a tiny MCP server (stdio, Python standard library only).

Tools
  interest_curve  diagnose a pacing curve (hook, peaks, lulls, flat stretches, climax)
  gacha_odds      exact chance of getting a featured unit (rate, 50/50, hard pity, spark)

Each tool returns a text summary plus structuredContent. Hosts that support MCP Apps
(extension io.modelcontextprotocol/ui, e.g. the Claude desktop app) also render an interactive
chart from the ui:// resource linked in the tool's _meta. Other hosts show the text.
No network access, no files written.
"""
from __future__ import annotations

import json
import math
import os
import sys

VERSION = "1.0.0"
UI_MIME = "text/html;profile=mcp-app"
HERE = os.path.dirname(os.path.abspath(__file__))
VIEWS = {"ui://game-design-charts/interest-curve": "interest_curve.html", "ui://game-design-charts/gacha-odds": "gacha_odds.html"}


# ---------------------------------------------------------------------------------------------
# Interest curve diagnosis (mirrors the rules in views/interest_curve.html)
# ---------------------------------------------------------------------------------------------
def diagnose_curve(beats: list[dict]) -> dict:
    pts = sorted(({"t": float(b["t"]), "intensity": max(0.0, min(10.0, float(b["intensity"]))), "label": str(b.get("label", ""))} for b in beats), key=lambda b: b["t"])
    if len(pts) < 3:
        raise ValueError("give at least 3 beats")
    t0, t1 = pts[0]["t"], pts[-1]["t"]
    span = (t1 - t0) or 1.0
    ys = [p["intensity"] for p in pts]
    peak_i = max(range(len(ys)), key=lambda i: ys[i])
    issues = []
    hook = next((p for p in pts if p["intensity"] >= 6), None)
    hook_at = (hook["t"] - t0) / span if hook else None
    if hook is None or hook_at > 0.15:
        issues.append({"kind": "LATE_HOOK", "text": "No strong beat (6+) in the first 15% of the session." if hook is None else f"First strong beat arrives at {hook_at:.0%} of the session; aim for the first 10–15%."})
    peak_pos = (pts[peak_i]["t"] - t0) / span
    if peak_pos < 0.6:
        issues.append({"kind": "EARLY_PEAK", "text": f"The highest point is at {peak_pos:.0%}; later beats can't top it, so the end may feel flat."})
    run_start, longest = None, (0.0, None, None)
    for p in pts:
        if p["intensity"] <= 3:
            run_start = p["t"] if run_start is None else run_start
            if p["t"] - run_start > longest[0]:
                longest = (p["t"] - run_start, run_start, p["t"])
        else:
            run_start = None
    if longest[0] / span > 0.2:
        issues.append({"kind": "LONG_LULL", "text": f"Intensity stays at 3 or below from {longest[1]:g} to {longest[2]:g} ({longest[0] / span:.0%} of the session)."})
    flat_start, flat = 0, (0.0, None, None)
    for i in range(1, len(pts)):
        if abs(ys[i] - ys[i - 1]) >= 1.0:
            flat_start = i
        dur = pts[i]["t"] - pts[flat_start]["t"]
        if dur > flat[0]:
            flat = (dur, pts[flat_start]["t"], pts[i]["t"])
    if flat[0] / span > 0.25:
        issues.append({"kind": "FLAT_STRETCH", "text": f"Almost no change from {flat[1]:g} to {flat[2]:g} ({flat[0] / span:.0%} of the session). Add a spike or a rest."})
    peaks = sum(1 for i in range(1, len(ys) - 1) if ys[i] > ys[i - 1] and ys[i] >= ys[i + 1])
    if len(pts) >= 6 and peaks < 2:
        issues.append({"kind": "NO_RHYTHM", "text": "Fewer than 2 peaks: tension needs release-and-rise cycles (a sawtooth)."})
    if peak_i == len(pts) - 1 and len(pts) >= 5:
        issues.append({"kind": "NO_RESOLUTION", "text": "The session ends on its peak with no wind-down. Add a short release beat after the climax."})
    mean = sum(ys) / len(ys)
    sd = math.sqrt(sum((y - mean) ** 2 for y in ys) / len(ys))
    if sd < 1.2:
        issues.append({"kind": "MONOTONE", "text": f"Intensity barely varies (standard deviation {sd:.1f}). Contrast drives interest."})
    return {"beats": pts, "duration": span, "peak": {"t": pts[peak_i]["t"], "intensity": ys[peak_i], "position": peak_pos},
            "hook_position": hook_at, "peaks": peaks, "mean": round(mean, 2), "sd": round(sd, 2), "issues": issues}


def curve_text(d: dict, title: str) -> str:
    lines = [f"Interest curve: {title}" if title else "Interest curve",
             f"{len(d['beats'])} beats over {d['duration']:g} time units; peak {d['peak']['intensity']:g} at {d['peak']['t']:g} ({d['peak']['position']:.0%}); {d['peaks']} local peaks; mean {d['mean']}, sd {d['sd']}."]
    lines += [f"- {i['kind']}: {i['text']}" for i in d["issues"]] or ["- No structural issues found. Check the curve against real playtest data."]
    return "\n".join(lines)


# ---------------------------------------------------------------------------------------------
# Gacha odds: exact distribution of pulls until the featured unit (mirrors views/gacha_odds.html)
# ---------------------------------------------------------------------------------------------
def gacha_cdf(rate: float, share: float, guarantee: bool, hard_pity: int | None, spark: int | None,
              since: int = 0, guaranteed: bool = False, spark_points: int = 0, max_pulls: int = 2000) -> list[float]:
    if not 0 < rate <= 1 or not 0 < share <= 1:
        raise ValueError("rate and featured_share must be in (0, 1]")
    states = {(since, guaranteed): 1.0}       # (pulls since last top-rarity, guaranteed flag) -> probability still waiting
    got, cdf = 0.0, []
    for k in range(1, max_pulls + 1):
        if spark and spark_points + k >= spark:
            got += sum(states.values()); cdf.append(min(1.0, got)); break
        nxt = {}
        for (s, g), pr in states.items():
            p_top = 1.0 if hard_pity and s + 1 >= hard_pity else rate
            p_feat = 1.0 if g else share
            got += pr * p_top * p_feat
            if p_feat < 1:
                key = (0, guarantee)                  # lost the 50/50: next top is guaranteed when the banner says so
                nxt[key] = nxt.get(key, 0.0) + pr * p_top * (1 - p_feat)
            key = (s + 1, g)
            if p_top < 1:
                nxt[key] = nxt.get(key, 0.0) + pr * (1 - p_top)
        states = {k2: v for k2, v in nxt.items() if v > 1e-15}
        cdf.append(min(1.0, got))
        if not states:
            break
    return cdf


def gacha_summary(cdf: list[float], budget: int) -> dict:
    mean = sum((c - (cdf[i - 1] if i else 0.0)) * (i + 1) for i, c in enumerate(cdf))
    tail = 1.0 - cdf[-1]
    q = lambda p: next((i + 1 for i, c in enumerate(cdf) if c >= p), None)
    worst = len(cdf) if tail < 1e-9 else None
    return {"mean": round(mean, 2), "consolidated_rate": round(1 / mean, 5) if mean else None, "median": q(0.5), "p90": q(0.9),
            "p99": q(0.99), "worst_case": worst, "budget": budget, "chance_within_budget": round(cdf[min(budget, len(cdf)) - 1], 4) if budget else 0.0,
            "truncated": tail >= 1e-9}


def gacha_text(args: dict, s: dict) -> str:
    rules = [f"top rate {args['rate']:.2%}", f"featured share {args['featured_share']:.0%}"]
    if args.get("guarantee_after_loss"): rules.append("guarantee after a lost 50/50")
    if args.get("hard_pity"): rules.append(f"hard pity at {args['hard_pity']}")
    if args.get("spark"): rules.append(f"spark/exchange at {args['spark']}")
    out = [f"Featured unit odds ({', '.join(rules)}):",
           f"- Mean {s['mean']} pulls (consolidated rate {s['consolidated_rate']:.2%}); median {s['median']}, 90th percentile {s['p90']}, 99th percentile {s['p99']}.",
           f"- Worst case: {s['worst_case']} pulls." if s["worst_case"] else "- No ceiling: some players never get it (NO_CEILING). Add a hard pity or a spark exchange."]
    if s["budget"]:
        out.append(f"- With {s['budget']} pulls: {s['chance_within_budget']:.1%} chance.")
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# MCP plumbing
# ---------------------------------------------------------------------------------------------
TOOLS = [
    {"name": "interest_curve", "title": "Interest curve",
     "description": "Diagnose a game session's pacing from beats (time, intensity 0-10, optional label): late hook, early peak, long lulls, flat stretches, missing rhythm or resolution. Renders an editable chart in hosts that support MCP Apps.",
     "inputSchema": {"type": "object", "required": ["beats"], "properties": {
         "title": {"type": "string"},
         "beats": {"type": "array", "minItems": 3, "items": {"type": "object", "required": ["t", "intensity"], "properties": {
             "t": {"type": "number", "description": "time (minutes or seconds; be consistent)"},
             "intensity": {"type": "number", "minimum": 0, "maximum": 10}, "label": {"type": "string"}}}}}},
     "_meta": {"ui": {"resourceUri": "ui://game-design-charts/interest-curve", "visibility": ["model", "app"]}, "ui/resourceUri": "ui://game-design-charts/interest-curve"}},
    {"name": "gacha_odds", "title": "Gacha odds",
     "description": "Exact distribution of pulls needed to get a featured unit, given the top-rarity rate, featured share (50/50), guarantee after a lost 50/50, hard pity and spark exchange, plus the chance within a pull budget. Renders an interactive CDF chart in hosts that support MCP Apps.",
     "inputSchema": {"type": "object", "required": ["rate"], "properties": {
         "rate": {"type": "number", "description": "top-rarity rate per pull, e.g. 0.03"},
         "featured_share": {"type": "number", "default": 0.5}, "guarantee_after_loss": {"type": "boolean", "default": True},
         "hard_pity": {"type": ["integer", "null"], "description": "top rarity guaranteed on this pull since the last one"},
         "spark": {"type": ["integer", "null"], "description": "pulls after which the featured unit can be exchanged"},
         "budget_pulls": {"type": "integer", "default": 0},
         "pulls_since_top": {"type": "integer", "default": 0}, "guaranteed": {"type": "boolean", "default": False},
         "spark_points": {"type": "integer", "default": 0}}},
     "_meta": {"ui": {"resourceUri": "ui://game-design-charts/gacha-odds", "visibility": ["model", "app"]}, "ui/resourceUri": "ui://game-design-charts/gacha-odds"}},
]


def call_tool(name: str, args: dict) -> dict:
    if name == "interest_curve":
        d = diagnose_curve(args.get("beats") or [])
        d["title"] = args.get("title", "")
        return {"content": [{"type": "text", "text": curve_text(d, d["title"])}], "structuredContent": d}
    if name == "gacha_odds":
        a = {"rate": float(args["rate"]), "featured_share": float(args.get("featured_share", 0.5)),
             "guarantee_after_loss": bool(args.get("guarantee_after_loss", True)), "hard_pity": args.get("hard_pity"),
             "spark": args.get("spark"), "budget_pulls": int(args.get("budget_pulls") or 0)}
        cdf = gacha_cdf(a["rate"], a["featured_share"], a["guarantee_after_loss"], a["hard_pity"], a["spark"],
                        int(args.get("pulls_since_top") or 0), bool(args.get("guaranteed")), int(args.get("spark_points") or 0))
        s = gacha_summary(cdf, a["budget_pulls"])
        step = max(1, len(cdf) // 400)
        return {"content": [{"type": "text", "text": gacha_text(a, s)}],
                "structuredContent": {"params": a, "summary": s, "cdf": [round(c, 6) for c in cdf[::step]], "cdf_step": step}}
    raise KeyError(name)


def handle(msg: dict) -> dict | None:
    method, mid, params = msg.get("method"), msg.get("id"), msg.get("params") or {}
    if mid is None:                       # notification
        return None
    ok = lambda result: {"jsonrpc": "2.0", "id": mid, "result": result}
    err = lambda code, text: {"jsonrpc": "2.0", "id": mid, "error": {"code": code, "message": text}}
    try:
        if method == "initialize":
            return ok({"protocolVersion": params.get("protocolVersion", "2025-06-18"),
                       "capabilities": {"tools": {"listChanged": False}, "resources": {"listChanged": False},
                                        "extensions": {"io.modelcontextprotocol/ui": {}}},
                       "serverInfo": {"name": "game-design-charts", "version": VERSION}})
        if method == "ping":
            return ok({})
        if method == "tools/list":
            return ok({"tools": TOOLS})
        if method == "tools/call":
            try:
                return ok(call_tool(params.get("name"), params.get("arguments") or {}))
            except KeyError as e:
                return err(-32602, f"unknown tool {e}")
            except (ValueError, TypeError) as e:
                return ok({"content": [{"type": "text", "text": f"Invalid input: {e}"}], "isError": True})
        if method == "resources/list":
            return ok({"resources": [{"uri": u, "name": f, "mimeType": UI_MIME, "description": "Interactive chart view (MCP Apps)"} for u, f in VIEWS.items()]})
        if method == "resources/read":
            uri = params.get("uri")
            if uri not in VIEWS:
                return err(-32602, f"unknown resource {uri}")
            html = open(os.path.join(HERE, "views", VIEWS[uri]), encoding="utf-8").read()
            return ok({"contents": [{"uri": uri, "mimeType": UI_MIME, "text": html, "_meta": {"ui": {"prefersBorder": True}}}]})
        return err(-32601, f"method not found: {method}")
    except Exception as e:   # never crash the server on one bad request
        return err(-32603, f"internal error: {e}")


def main() -> int:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}) + "\n"); sys.stdout.flush()
            continue
        for m in (msg if isinstance(msg, list) else [msg]):
            res = handle(m)
            if res is not None:
                sys.stdout.write(json.dumps(res, ensure_ascii=False) + "\n"); sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
