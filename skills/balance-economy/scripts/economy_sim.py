#!/usr/bin/env python3
"""Monte Carlo simulation of a game economy: faucets, sinks, purchases and gacha.

Simulates N players over S sessions from a JSON config, then reports balance
percentiles per currency, faucet/sink flow, inequality (Gini), archetype results
and, for gacha, the exact pity distribution next to the simulated one.

Config (JSON):
{
  "title": "...", "players": 1000, "sessions": 60, "seed": 7,
  "currencies": {"gold": {"start": 0}, "gems": {"start": 0}},
  "archetypes": [
    {"name": "casual", "share": 0.6, "play_prob": 0.6, "income_mult": 0.8},
    {"name": "spender", "share": 0.05, "play_prob": 0.95, "income_mult": 1.0,
     "purchases": [{"currency": "gems", "amount": 980, "every": 7, "price": 14.99}]}
  ],
  "faucets": [{"name": "quests", "currency": "gold", "mean": 400, "sd": 120,
               "growth": 0.03, "prob": 1.0}],
  "sinks": [
    {"name": "upgrade", "currency": "gold", "kind": "buy", "cost": 800,
     "cost_growth": 0.12, "max_per_session": 2, "reserve": 0},
    {"name": "repairs", "currency": "gold", "kind": "fixed", "amount": 60},
    {"name": "trade tax", "currency": "gold", "kind": "percent", "rate": 0.05}
  ],
  "gacha": {"name": "banner", "currency": "gems", "cost": 160,
            "max_pulls_per_session": 10, "reserve": 0,
            "rates": {"SSR": 0.006, "SR": 0.051},
            "pity": {"item": "SSR", "hard": 90, "soft_start": 74, "soft_step": 0.06}}
}
  faucet.growth  per played session (compounding); faucet.prob = chance per session
  sink kinds     fixed (flat drain), percent (share of this session's income in that
                 currency), buy (repeatable purchase whose cost grows per purchase)

Outputs: <name>_sessions.csv, <name>_players.csv, <name>_pity.csv (if gacha),
<name>_report.md, and <name>_economy.png / <name>_pity.png with matplotlib.

Example:
  python3 economy_sim.py ../examples/f2p-economy.json --out ./out
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys

SURFACE, INK, INK_2, MUTED, GRID, BASELINE = ("#fcfcfb", "#0b0b0b", "#52514e",
                                              "#898781", "#e1e0d9", "#c3c2b7")
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]


# ------------------------------------------------------------ gacha math ---

def pull_probability(k: int, base: float, pity: dict | None) -> float:
    """Chance that pull number k (1-based, since the last hit) is a hit."""
    if not pity:
        return base
    if pity.get("hard") and k >= pity["hard"]:
        return 1.0
    start = pity.get("soft_start")
    if start and k >= start:
        return min(1.0, base + pity.get("soft_step", 0.0) * (k - start + 1))
    return base


def pity_distribution(base: float, pity: dict | None, limit: int = 2000) -> list[tuple[int, float, float, float]]:
    """Exact (k, p_k, P(first hit at k), CDF) until the CDF reaches ~1."""
    rows, survive, cdf = [], 1.0, 0.0
    for k in range(1, limit + 1):
        p = pull_probability(k, base, pity)
        mass = survive * p
        cdf += mass
        survive *= 1 - p
        rows.append((k, p, mass, cdf))
        if survive < 1e-9:
            break
    return rows


def quantile_from_cdf(rows, q: float) -> int:
    return next((k for k, _, _, cdf in rows if cdf >= q), rows[-1][0])


# ------------------------------------------------------------ simulation ---

def percentile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = min(len(sorted_vals) - 1, max(0, round(q * (len(sorted_vals) - 1))))
    return sorted_vals[idx]


def gini(values: list[float]) -> float:
    vals = sorted(max(0.0, v) for v in values)
    n, total = len(vals), sum(vals)
    if n == 0 or total == 0:
        return 0.0
    weighted = sum((i + 1) * v for i, v in enumerate(vals))
    return (2 * weighted) / (n * total) - (n + 1) / n


def simulate(cfg: dict) -> dict:
    rng = random.Random(cfg.get("seed", 1))
    currencies = list(cfg["currencies"].keys())
    n_players, n_sessions = int(cfg.get("players", 1000)), int(cfg.get("sessions", 30))
    archetypes = cfg.get("archetypes") or [{"name": "player", "share": 1.0}]
    total_share = sum(a.get("share", 1.0) for a in archetypes)
    gacha = cfg.get("gacha")

    players = []
    for i in range(n_players):
        r, acc, arch = rng.random() * total_share, 0.0, archetypes[-1]
        for a in archetypes:
            acc += a.get("share", 1.0)
            if r <= acc:
                arch = a
                break
        players.append({"arch": arch, "bal": {c: float(cfg["currencies"][c].get("start", 0)) for c in currencies},
                        "played": 0, "buys": {}, "pulls": 0, "hits": 0, "since_hit": 0,
                        "spend": 0.0, "hit_pulls": [], "items": {}})

    per_session = []
    for s in range(1, n_sessions + 1):
        inflow = {c: 0.0 for c in currencies}
        outflow = {c: 0.0 for c in currencies}
        bought = 0
        for pl in players:
            arch = pl["arch"]
            if rng.random() > arch.get("play_prob", 1.0):
                continue
            pl["played"] += 1
            earned = {c: 0.0 for c in currencies}
            for pur in arch.get("purchases", []):
                if s % int(pur.get("every", 1)) == 0:
                    pl["bal"][pur["currency"]] += pur["amount"]
                    inflow[pur["currency"]] += pur["amount"]
                    pl["spend"] += pur.get("price", 0.0)
            for f in cfg.get("faucets", []):
                if rng.random() > f.get("prob", 1.0):
                    continue
                amount = max(0.0, rng.gauss(f["mean"], f.get("sd", 0.0)))
                amount *= arch.get("income_mult", 1.0) * (1 + f.get("growth", 0.0)) ** (pl["played"] - 1)
                pl["bal"][f["currency"]] += amount
                earned[f["currency"]] += amount
                inflow[f["currency"]] += amount
            for sk in cfg.get("sinks", []):
                cur, kind = sk["currency"], sk.get("kind", "fixed")
                if kind == "fixed":
                    paid = min(pl["bal"][cur], sk["amount"])
                elif kind == "percent":
                    paid = min(pl["bal"][cur], earned[cur] * sk["rate"])
                elif kind == "buy":
                    paid, count = 0.0, 0
                    level = pl["buys"].get(sk["name"], 0)
                    while count < sk.get("max_per_session", 1):
                        price = sk["cost"] * (1 + sk.get("cost_growth", 0.0)) ** level
                        if pl["bal"][cur] - price < sk.get("reserve", 0):
                            break
                        pl["bal"][cur] -= price
                        paid += price
                        level += 1
                        count += 1
                    pl["buys"][sk["name"]] = level
                    bought += count
                    outflow[cur] += paid
                    continue
                else:
                    raise ValueError(f"unknown sink kind: {kind}")
                pl["bal"][cur] -= paid
                outflow[cur] += paid
            if gacha:
                cur, cost = gacha["currency"], gacha["cost"]
                pity = gacha.get("pity")
                hit_item = pity["item"] if pity else next(iter(gacha["rates"]))
                base = gacha["rates"][hit_item]
                others = [(k, v) for k, v in gacha["rates"].items() if k != hit_item]
                pulls = 0
                while (pulls < gacha.get("max_pulls_per_session", 10)
                       and pl["bal"][cur] - cost >= gacha.get("reserve", 0)):
                    pl["bal"][cur] -= cost
                    outflow[cur] += cost
                    pulls += 1
                    pl["pulls"] += 1
                    pl["since_hit"] += 1
                    p = pull_probability(pl["since_hit"], base, pity)
                    roll = rng.random()
                    if roll < p:
                        pl["hits"] += 1
                        pl["hit_pulls"].append(pl["since_hit"])
                        pl["since_hit"] = 0
                        item = hit_item
                    else:
                        item, acc = "common", p
                        for name, rate in others:
                            acc += rate
                            if roll < acc:
                                item = name
                                break
                    pl["items"][item] = pl["items"].get(item, 0) + 1
        row = {"session": s, "inflow": inflow, "outflow": outflow, "buys": bought, "stats": {}}
        for c in currencies:
            vals = sorted(pl["bal"][c] for pl in players)
            row["stats"][c] = {"mean": sum(vals) / len(vals), "p10": percentile(vals, 0.1),
                               "p50": percentile(vals, 0.5), "p90": percentile(vals, 0.9)}
        per_session.append(row)
    return {"players": players, "sessions": per_session, "currencies": currencies}


# --------------------------------------------------------------- analysis ---

def analyse(cfg: dict, sim: dict) -> tuple[list[str], list[str], dict | None]:
    findings, summary = [], []
    sessions, currencies = sim["sessions"], sim["currencies"]
    third = max(1, len(sessions) // 3)
    late = sessions[-third:]
    for c in currencies:
        total_in = sum(r["inflow"][c] for r in sessions)
        total_out = sum(r["outflow"][c] for r in sessions)
        late_in = sum(r["inflow"][c] for r in late)
        late_out = sum(r["outflow"][c] for r in late)
        ratio = late_in / late_out if late_out else float("inf")
        p50_start, p50_end = late[0]["stats"][c]["p50"], late[-1]["stats"][c]["p50"]
        per_session_income = late_in / len(late) / max(1, len(sim["players"]))
        g = gini([pl["bal"][c] for pl in sim["players"]])
        summary.append(f"| {c} | {total_in:,.0f} | {total_out:,.0f} | "
                       f"{(total_in / total_out if total_out else float('inf')):.2f} | {ratio:.2f} | "
                       f"{sessions[-1]['stats'][c]['p50']:,.0f} | {g:.2f} |")
        growth = (p50_end - p50_start) / max(1, len(late) - 1)
        if ratio > 1.25 and growth > 0:
            sev = "HIGH" if ratio > 1.5 else "MEDIUM"
            findings.append(f"**[{sev}] INFLATION ({c})**: in the last third, faucets exceed sinks {ratio:.2f}:1 "
                            f"and the median balance keeps rising (~{growth:,.0f}/session; about "
                            f"{p50_end / max(per_session_income, 1e-9):.1f} sessions of income hoarded). Prices "
                            f"tied to {c} lose meaning. Fix: add sinks that scale with progression "
                            f"(consumables, upgrades, trade taxes) or slow late faucets.")
        elif late_out == 0 and late_in > 0:
            findings.append(f"**[HIGH] NO_SINK ({c})**: nothing drains {c} in the last third.")
        if g > 0.6:
            findings.append(f"**[MEDIUM] INEQUALITY ({c})**: Gini {g:.2f} at the end. Fine for single-player; "
                            "in shared economies it prices newcomers out. Consider catch-up faucets or "
                            "progressive sinks.")
    for sk in cfg.get("sinks", []):
        if sk.get("kind") != "buy":
            continue
        levels = sorted(pl["buys"].get(sk["name"], 0) for pl in sim["players"])
        med = percentile(levels, 0.5)
        if med == 0:
            findings.append(f"**[HIGH] STARVATION ({sk['name']})**: the median player never affords it. "
                            "Lower the base cost or raise early income.")
        elif med < len(sessions) / 15:
            findings.append(f"**[MEDIUM] SLOW_SINK ({sk['name']})**: median player bought it {med:.0f} times in "
                            f"{len(sessions)} sessions; progress through it may feel stalled.")

    pity_info = None
    gacha = cfg.get("gacha")
    if gacha:
        pity = gacha.get("pity")
        hit_item = pity["item"] if pity else next(iter(gacha["rates"]))
        base = gacha["rates"][hit_item]
        rows = pity_distribution(base, pity)
        expected = sum(k * mass for k, _, mass, _ in rows)
        total_pulls = sum(pl["pulls"] for pl in sim["players"])
        total_hits = sum(pl["hits"] for pl in sim["players"])
        pity_info = {"rows": rows, "expected": expected, "item": hit_item, "base": base,
                     "p50": quantile_from_cdf(rows, 0.5), "p90": quantile_from_cdf(rows, 0.9),
                     "p99": quantile_from_cdf(rows, 0.99), "max": rows[-1][0] if pity and pity.get("hard") else None,
                     "realised": total_hits / total_pulls if total_pulls else None, "hits": total_hits,
                     "zero_share": sum(pl["hits"] == 0 for pl in sim["players"]) / len(sim["players"])}
        if pity_info["zero_share"] > 0.5:
            findings.append(f"**[MEDIUM] RARE_FOR_MOST**: {pity_info['zero_share']:.0%} of simulated players never "
                            f"obtain a {hit_item} in {len(sessions)} sessions. If the {hit_item} is needed to "
                            "progress, this is a paywall; if it is cosmetic or a side-grade, say so in the UI.")
        if not pity or not pity.get("hard"):
            findings.append(f"**[HIGH] NO_HARD_PITY**: {hit_item} has no guaranteed ceiling; the unluckiest 1% need "
                            f"{pity_info['p99']} pulls. Add a hard pity and disclose it (several jurisdictions "
                            "require probability disclosure; see references/randomness-and-loot.md).")
        consolidated = 1 / expected
        if consolidated > 1.5 * base:
            findings.append(f"**[INFO] DISCLOSURE**: headline rate {base:.2%} vs consolidated rate "
                            f"{consolidated:.2%} once pity is counted. Disclose both, plus the pity terms.")
        spenders = [pl for pl in sim["players"] if pl["spend"] > 0]
        if spenders and pity and pity.get("hard"):
            per_dollar = [pur["amount"] / pur["price"] for a in cfg.get("archetypes", [])
                          for pur in a.get("purchases", []) if pur.get("currency") == gacha["currency"]
                          and pur.get("price")]
            if per_dollar:
                worst = pity["hard"] * gacha["cost"] / max(per_dollar)
                avg = expected * gacha["cost"] / max(per_dollar)
                pity_info["money"] = (avg, worst)
                summary.append(f"\nReal-money cost of one {hit_item} at the best pack rate: "
                               f"~{avg:,.2f} on average, {worst:,.2f} at hard pity.")
    return findings, summary, pity_info


# ---------------------------------------------------------------- output ---

def setup_fonts(plt) -> None:
    import logging
    from matplotlib import font_manager
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
    available = {f.name for f in font_manager.fontManager.ttflist}
    latin = [f for f in ("Helvetica Neue", "Helvetica", "Arial", "Segoe UI", "DejaVu Sans")
             if f in available][:1]
    cjk = [f for f in ("Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans CJK KR", "Hiragino Sans",
                       "Yu Gothic", "PingFang SC", "Microsoft YaHei") if f in available]
    plt.rcParams.update({"font.family": (latin or ["DejaVu Sans"]) + cjk, "font.size": 10})


def style_axis(ax, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_facecolor(SURFACE)
    ax.set_title(title, loc="left", color=INK, fontsize=11, fontweight="semibold")
    ax.set_xlabel(xlabel, color=INK_2)
    ax.set_ylabel(ylabel, color=INK_2)
    ax.grid(axis="y", color=GRID, lw=1)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(BASELINE)
    ax.tick_params(colors=MUTED, length=0)


def plot(cfg, sim, pity_info, out_dir, name) -> list[str]:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
    except ImportError:
        return []
    setup_fonts(plt)
    compact = FuncFormatter(lambda v, _: f"{v / 1e6:g}M" if abs(v) >= 1e6 else f"{v / 1e3:g}K"
                            if abs(v) >= 1e3 else f"{v:g}")
    paths, sessions, currencies = [], sim["sessions"], sim["currencies"]
    xs = [r["session"] for r in sessions]
    fig, axes = plt.subplots(2, len(currencies), figsize=(5.6 * len(currencies), 7.4), dpi=150, squeeze=False)
    fig.patch.set_facecolor(SURFACE)
    for j, c in enumerate(currencies):
        ax = axes[0][j]
        style_axis(ax, f"{c}: balance per player", "Session", c)
        ax.fill_between(xs, [r["stats"][c]["p10"] for r in sessions], [r["stats"][c]["p90"] for r in sessions],
                        color=SERIES[0], alpha=0.12, lw=0, label="p10-p90")
        ax.plot(xs, [r["stats"][c]["p50"] for r in sessions], color=SERIES[0], lw=2, label="median")
        ax.yaxis.set_major_formatter(compact)
        ax.legend(frameon=False, fontsize=8.5, labelcolor=INK_2, loc="upper left")
        ax2 = axes[1][j]
        style_axis(ax2, f"{c}: total flow per session", "Session", c)
        ax2.plot(xs, [r["inflow"][c] for r in sessions], color=SERIES[0], lw=2, label="faucets (in)")
        ax2.plot(xs, [r["outflow"][c] for r in sessions], color=SERIES[1], lw=2, label="sinks (out)")
        ax2.yaxis.set_major_formatter(compact)
        ax2.legend(frameon=False, fontsize=8.5, labelcolor=INK_2, loc="upper left")
    fig.suptitle(cfg.get("title", name), x=0.01, ha="left", color=INK, fontsize=13, fontweight="semibold")
    fig.tight_layout()
    path = os.path.join(out_dir, f"{name}_economy.png")
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)
    paths.append(path)

    if pity_info:
        rows = pity_info["rows"]
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), dpi=150)
        fig.patch.set_facecolor(SURFACE)
        style_axis(a1, f"Chance the first {pity_info['item']} lands on pull k", "Pull k", "Probability")
        a1.bar([k for k, *_ in rows], [m for _, _, m, _ in rows], width=0.8, color=SERIES[0], lw=0)
        style_axis(a2, "Cumulative chance of at least one", "Pulls", "Probability")
        a2.plot([k for k, *_ in rows], [c for *_, c in rows], color=SERIES[0], lw=2)
        for q, label in ((0.5, "p50"), (0.9, "p90")):
            k = quantile_from_cdf(rows, q)
            a2.scatter([k], [q], s=64, color=SERIES[0], edgecolors=SURFACE, linewidths=2, zorder=3)
            a2.annotate(f"{label}: {k} pulls", (k, q), xytext=(-8, 6), textcoords="offset points",
                        ha="right", fontsize=8.5, color=INK_2)
        a2.set_ylim(0, 1.05)
        fig.suptitle(f"{cfg['gacha'].get('name', 'Gacha')}: exact pity distribution "
                     f"(mean {pity_info['expected']:.1f} pulls)", x=0.01, ha="left", color=INK,
                     fontsize=13, fontweight="semibold")
        fig.tight_layout()
        path = os.path.join(out_dir, f"{name}_pity.png")
        fig.savefig(path, facecolor=SURFACE)
        plt.close(fig)
        paths.append(path)
    return paths


def write_outputs(cfg, sim, findings, summary, pity_info, out_dir, name, charts) -> str:
    currencies = sim["currencies"]
    with open(os.path.join(out_dir, f"{name}_sessions.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["session", "currency", "mean", "p10", "p50", "p90", "inflow", "outflow", "net", "buys"])
        for r in sim["sessions"]:
            for c in currencies:
                st = r["stats"][c]
                w.writerow([r["session"], c, round(st["mean"], 2), round(st["p10"], 2), round(st["p50"], 2),
                            round(st["p90"], 2), round(r["inflow"][c], 2), round(r["outflow"][c], 2),
                            round(r["inflow"][c] - r["outflow"][c], 2), r["buys"]])
    with open(os.path.join(out_dir, f"{name}_players.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["player", "archetype", "sessions_played"] + [f"balance_{c}" for c in currencies]
                   + ["upgrades", "pulls", "hits", "spend"])
        for i, pl in enumerate(sim["players"]):
            w.writerow([i, pl["arch"]["name"], pl["played"]] + [round(pl["bal"][c], 1) for c in currencies]
                       + [sum(pl["buys"].values()), pl["pulls"], pl["hits"], round(pl["spend"], 2)])
    if pity_info:
        with open(os.path.join(out_dir, f"{name}_pity.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["pull_k", "p_hit_on_k", "p_first_hit_at_k", "cdf"])
            w.writerows((k, round(p, 6), round(m, 8), round(c, 6)) for k, p, m, c in pity_info["rows"])

    lines = [f"# Economy simulation: {cfg.get('title', name)}", "",
             f"{len(sim['players']):,} players × {len(sim['sessions'])} sessions, seed {cfg.get('seed', 1)}.", ""]
    lines += [f"![{os.path.basename(p)}]({os.path.basename(p)})" for p in charts] + [""]
    lines += ["## Findings", ""] + ([f"- {f}" for f in findings] or ["- No structural problems detected."]) + [""]
    lines += ["## Currency flow", "",
              "| Currency | Total in | Total out | In/Out | In/Out (last third) | Median end balance | Gini |",
              "|---|---|---|---|---|---|---|"] + summary + [""]
    lines += ["## Archetypes", "", "| Archetype | Players | Avg sessions | Avg upgrades | Avg pulls | Avg hits | "
              "Share with ≥1 hit | Avg spend |", "|---|---|---|---|---|---|---|---|"]
    by_arch: dict[str, list] = {}
    for pl in sim["players"]:
        by_arch.setdefault(pl["arch"]["name"], []).append(pl)
    for arch, pls in by_arch.items():
        n = len(pls)
        lines.append(f"| {arch} | {n} | {sum(p['played'] for p in pls) / n:.1f} | "
                     f"{sum(sum(p['buys'].values()) for p in pls) / n:.1f} | {sum(p['pulls'] for p in pls) / n:.1f} | "
                     f"{sum(p['hits'] for p in pls) / n:.2f} | {sum(p['hits'] > 0 for p in pls) / n:.0%} | "
                     f"{sum(p['spend'] for p in pls) / n:.2f} |")
    if pity_info:
        pi = pity_info
        lines += ["", f"## Gacha: {pi['item']}", "",
                  f"- Base rate {pi['base']:.2%}; expected pulls per {pi['item']} **{pi['expected']:.1f}** "
                  f"(consolidated rate **{1 / pi['expected']:.2%}**).",
                  f"- Pulls needed: median {pi['p50']}, 90% of players by {pi['p90']}, 99% by {pi['p99']}"
                  + (f", guaranteed by {pi['max']}." if pi["max"] else " (no guarantee)."),
                  f"- Realised hit rate in the simulation: {pi['realised']:.2%} per pull ({pi['hits']} hits). "
                  "It sits below the consolidated rate when most players stop before reaching soft pity."
                  if pi["realised"] is not None else "- No pulls happened; raise income or sessions.",
                  f"- Players who never obtained one: {pi['zero_share']:.0%}."]
        if "money" in pi:
            lines.append(f"- Real money per {pi['item']}: ~{pi['money'][0]:.2f} average, "
                         f"{pi['money'][1]:.2f} worst case (hard pity).")
    lines += ["", "_A model, not a forecast: validate archetype assumptions against telemetry._", ""]
    path = os.path.join(out_dir, f"{name}_report.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config", help="economy JSON config")
    ap.add_argument("--out", help="output directory (default: next to the config)")
    ap.add_argument("--players", type=int, help="override player count")
    ap.add_argument("--sessions", type=int, help="override session count")
    ap.add_argument("--seed", type=int, help="override random seed")
    ap.add_argument("--no-plot", action="store_true")
    a = ap.parse_args(argv)
    try:
        with open(a.config, encoding="utf-8") as fh:
            cfg = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    for key in ("players", "sessions", "seed"):
        if getattr(a, key) is not None:
            cfg[key] = getattr(a, key)
    if not cfg.get("currencies"):
        print("error: config needs at least one currency", file=sys.stderr)
        return 2
    out_dir = a.out or os.path.dirname(os.path.abspath(a.config))
    os.makedirs(out_dir, exist_ok=True)
    name = os.path.splitext(os.path.basename(a.config))[0]
    try:
        sim = simulate(cfg)
    except (KeyError, ValueError) as exc:
        print(f"error: bad config: {exc}", file=sys.stderr)
        return 2
    findings, summary, pity_info = analyse(cfg, sim)
    charts = [] if a.no_plot else plot(cfg, sim, pity_info, out_dir, name)
    if not charts and not a.no_plot:
        print("note: matplotlib not installed; wrote CSV/Markdown only", file=sys.stderr)
    report = write_outputs(cfg, sim, findings, summary, pity_info, out_dir, name, charts)
    print("\n".join(f"- {f}" for f in findings) or "No structural problems detected.")
    if pity_info:
        print(f"Gacha: expected {pity_info['expected']:.1f} pulls per {pity_info['item']} "
              f"(p50 {pity_info['p50']}, p90 {pity_info['p90']}, p99 {pity_info['p99']})")
    for p in charts + [report]:
        print(f"wrote {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
