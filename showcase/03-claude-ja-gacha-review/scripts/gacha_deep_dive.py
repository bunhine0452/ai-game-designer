#!/usr/bin/env python3
"""Banner-level gacha deep dive for 星喚びの島 (complements economy_sim.py).

economy_sim.py models one gacha currency and one SSR pity counter that never resets.
This script reads the same JSON and adds what a Japanese-market pickup banner needs:

- pickup (featured) share of SSR hits, with or without a guarantee after losing (すり抜け)
- spark exchange (天井/交換) after N pulls, and whether the SSR pity counter and the spark
  points carry over to the next banner or are lost when it ends
- free vs paid premium currency (無償/有償石) and which one is consumed first
- real-money (JPY) cost per featured SSR at the standard pack rate

Extra config keys (economy_sim.py ignores them):
  "banner": {"days": 14, "pickup_share": 0.5, "guarantee_after_loss": true, "spark": 120,
             "carry_pity": true, "carry_spark": true, "consume": "free_first",
             "yen_per_paid_stone": 1.667}
  archetypes[].banner_interest   chance a player wants a given banner (others are skipped)
  archetypes[].copies_wanted     featured copies chased per wanted banner (default 1)
  archetypes[].purchases[].paid  paid part of "amount"; the rest is a free bonus

Candidates file (optional): [{"name": "...", "gacha": {...}, "banner": {...}}, ...]; each
entry overrides the first config's "gacha"/"banner" keys (a "pity" of null removes pity).

Usage:
  python3 gacha_deep_dive.py config/v1.json config/v2.json --candidates c.json --out out/deep_dive
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import os
import random
import sys

COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#8e5bd6", "#52514e"]


def pull_probability(k: int, base: float, pity: dict | None) -> float:
    """Chance that pull k (1-based, since the last SSR) is an SSR. Same rule as economy_sim.py."""
    if not pity:
        return base
    if pity.get("hard") and k >= pity["hard"]:
        return 1.0
    start = pity.get("soft_start")
    if start and k >= start:
        return min(1.0, base + pity.get("soft_step", 0.0) * (k - start + 1))
    return base


def featured_distribution(base, pity, share, guarantee, spark, limit=5000):
    """Exact P(first featured SSR on pull n) for a fresh account. Rows: (n, mass, cdf, spark_mass)."""
    states = {(0, False): 1.0}  # (pulls since last SSR, guaranteed next SSR) -> prob. still waiting
    rows, cdf = [], 0.0
    for n in range(1, limit + 1):
        nxt, mass = {}, 0.0
        for (k, g), pr in states.items():
            p = pull_probability(k + 1, base, pity)
            win = 1.0 if g else share
            mass += pr * p * win
            if p * (1 - win) > 0:
                key = (0, guarantee)
                nxt[key] = nxt.get(key, 0.0) + pr * p * (1 - win)
            if p < 1:
                nxt[(k + 1, g)] = nxt.get((k + 1, g), 0.0) + pr * (1 - p)
        spark_mass = 0.0
        if spark and n == spark:
            spark_mass = sum(nxt.values())
            nxt = {}
        cdf += mass + spark_mass
        rows.append((n, mass + spark_mass, cdf, spark_mass))
        states = nxt
        if sum(states.values()) < 1e-9:
            break
    return rows


def quantile(rows, q):
    return next((n for n, _, c, _ in rows if c >= q - 1e-12), rows[-1][0])


def exact_stats(cfg):
    g, b = cfg["gacha"], cfg["banner"]
    pity = g.get("pity")
    base = g["rates"][pity["item"] if pity else next(iter(g["rates"]))]
    ssr_rows = featured_distribution(base, pity, 1.0, False, None)
    rows = featured_distribution(base, pity, b.get("pickup_share", 1.0),
                                 b.get("guarantee_after_loss", False), b.get("spark"))
    mean = sum(n * m for n, m, _, _ in rows)
    yen = g["cost"] * b.get("yen_per_paid_stone", 0.0)
    return {"rows": rows, "base": base, "ssr_mean": sum(n * m for n, m, _, _ in ssr_rows),
            "mean": mean, "p50": quantile(rows, 0.5), "p90": quantile(rows, 0.9),
            "p99": quantile(rows, 0.99), "max": rows[-1][0], "via_spark": sum(r[3] for r in rows),
            "yen_per_pull": yen}


def simulate(cfg):
    rng = random.Random(cfg.get("seed", 1))
    g, b = cfg["gacha"], cfg["banner"]
    cur, cost, pity = g["currency"], g["cost"], g.get("pity")
    base = g["rates"][pity["item"] if pity else next(iter(g["rates"]))]
    share, guarantee = b.get("pickup_share", 1.0), b.get("guarantee_after_loss", False)
    spark, days, free_first = b.get("spark"), int(b.get("days", 14)), b.get("consume", "free_first") == "free_first"
    faucets = [f for f in cfg.get("faucets", []) if f["currency"] == cur]
    archetypes = cfg["archetypes"]
    total_share = sum(a.get("share", 1.0) for a in archetypes)

    players = []
    for _ in range(int(cfg.get("players", 1000))):
        r, acc, arch = rng.random() * total_share, 0.0, archetypes[-1]
        for a in archetypes:
            acc += a.get("share", 1.0)
            if r <= acc:
                arch = a
                break
        players.append({"arch": arch, "free": float(cfg["currencies"][cur].get("start", 0)), "paid": 0.0,
                        "yen": 0.0, "played": 0, "since": 0, "guar": False, "spark": 0, "pulls": 0, "ssr": 0,
                        "feat": 0, "via_spark": 0, "lost_pity": 0, "lost_spark": 0, "spent_free": 0.0,
                        "spent_paid": 0.0, "want": False, "got": 0, "wanted": 0, "won": 0})

    for day in range(1, int(cfg.get("sessions", 90)) + 1):
        new_banner = (day - 1) % days == 0
        for pl in players:
            a = pl["arch"]
            if new_banner:
                if day > 1:
                    if not b.get("carry_pity", False):
                        pl["lost_pity"] += pl["since"] if pity else 0  # a flat rate has no memory to lose
                        pl["since"], pl["guar"] = 0, False
                    if not b.get("carry_spark", False):
                        pl["lost_spark"] += pl["spark"]
                        pl["spark"] = 0
                pl["want"], pl["got"] = rng.random() < a.get("banner_interest", 1.0), 0
                pl["wanted"] += pl["want"]
            if rng.random() > a.get("play_prob", 1.0):
                continue
            pl["played"] += 1
            for pur in a.get("purchases", []):
                if pur["currency"] == cur and day % int(pur.get("every", 1)) == 0:
                    paid = pur.get("paid", pur["amount"])
                    pl["paid"] += paid
                    pl["free"] += pur["amount"] - paid
                    pl["yen"] += pur.get("price", 0.0)
            for f in faucets:
                if rng.random() > f.get("prob", 1.0):
                    continue
                amount = max(0.0, rng.gauss(f["mean"], f.get("sd", 0.0)))
                pl["free"] += amount * a.get("income_mult", 1.0) * (1 + f.get("growth", 0.0)) ** (pl["played"] - 1)
            while pl["want"] and pl["got"] < a.get("copies_wanted", 1) and pl["free"] + pl["paid"] >= cost:
                first, second = ("free", "paid") if free_first else ("paid", "free")
                take = min(pl[first], cost)
                pl[first] -= take
                pl[second] -= cost - take
                pl["spent_" + first] += take
                pl["spent_" + second] += cost - take
                pl["pulls"] += 1
                pl["since"] += 1
                pl["spark"] += 1
                featured = False
                if rng.random() < pull_probability(pl["since"], base, pity):
                    pl["ssr"] += 1
                    pl["since"] = 0
                    if pl["guar"] or rng.random() < share:
                        featured, pl["guar"] = True, False
                    else:
                        pl["guar"] = guarantee
                if not featured and spark and pl["spark"] >= spark:
                    featured = True
                    pl["spark"] -= spark
                    pl["via_spark"] += 1
                if featured:
                    pl["feat"] += 1
                    pl["got"] += 1
                    pl["won"] += pl["got"] == 1
    return players


def summarise(cfg, players):
    yen_per_stone = cfg["banner"].get("yen_per_paid_stone", 0.0)
    by_arch = {}
    for pl in players:
        by_arch.setdefault(pl["arch"]["name"], []).append(pl)
    out = []
    for a in cfg["archetypes"]:
        pls = by_arch.get(a["name"], [])
        if not pls:
            continue
        n = len(pls)
        feat = sum(p["feat"] for p in pls)
        yen = sum(p["yen"] for p in pls)
        out.append({"archetype": a["name"], "players": n, "avg_yen": yen / n,
                    "avg_pulls": sum(p["pulls"] for p in pls) / n, "avg_featured": feat / n,
                    "share_any_featured": sum(p["feat"] > 0 for p in pls) / n,
                    "banner_win_rate": sum(p["won"] for p in pls) / max(1, sum(p["wanted"] for p in pls)),
                    "spark_share": sum(p["via_spark"] for p in pls) / feat if feat else 0.0,
                    "avg_lost_pity": sum(p["lost_pity"] for p in pls) / n,
                    "avg_lost_spark": sum(p["lost_spark"] for p in pls) / n,
                    "yen_per_featured": yen / feat if feat and yen else 0.0,
                    "end_free": sum(p["free"] for p in pls) / n, "end_paid": sum(p["paid"] for p in pls) / n})
    unused_paid_yen = sum(p["paid"] for p in players) * yen_per_stone
    return out, {"unused_paid_yen_per_1000": unused_paid_yen / len(players) * 1000,
                 "paid_share_of_spend": sum(p["spent_paid"] for p in players)
                 / max(1.0, sum(p["spent_paid"] + p["spent_free"] for p in players))}


def plot(scenarios, out_dir):
    try:
        import logging
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib import font_manager
    except ImportError:
        return None
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
    available = {f.name for f in font_manager.fontManager.ttflist}
    jp = [f for f in ("Hiragino Sans", "YuGothic", "Noto Sans CJK JP", "Yu Gothic", "Meiryo") if f in available]
    plt.rcParams.update({"font.family": jp[:1] + ["DejaVu Sans"], "font.size": 10})
    groups = {}  # scenarios with identical gacha math share one line
    for sc in scenarios:
        key = (round(sc["exact"]["mean"], 6), sc["exact"]["max"], sc["exact"]["p50"])
        groups.setdefault(key, []).append(sc)
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=150)
    for i, scs in enumerate(groups.values()):
        rows, e = scs[0]["exact"]["rows"], scs[0]["exact"]
        ax.plot([r[0] for r in rows], [r[2] for r in rows], color=COLORS[i % len(COLORS)], lw=2,
                label=f"{' = '.join(s['name'] for s in scs)}（平均 {e['mean']:.0f} 連・最大 {e['max']} 連）")
    ax.axhline(0.9, color="#c3c2b7", lw=1, ls="--")
    ax.set_xlim(0, max(min(sc["exact"]["max"], 400) for sc in scenarios) + 10)
    ax.set_ylim(0, 1.03)
    ax.set_title("狙いのピックアップSSRを1体得るまでの累積確率（初期状態から・厳密計算）", loc="left")
    ax.set_xlabel("ガチャ回数（連）")
    ax.set_ylabel("累積確率")
    ax.grid(axis="y", color="#e1e0d9")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=8.5, loc="lower right")
    fig.tight_layout()
    path = os.path.join(out_dir, "featured_cdf.png")
    fig.savefig(path)
    plt.close(fig)
    return path


def scenario_from(cfg, name, override=None):
    c = copy.deepcopy(cfg)
    for key in ("gacha", "banner"):
        for k, v in (override or {}).get(key, {}).items():
            if v is None:
                c[key].pop(k, None)
            else:
                c[key][k] = v
    return {"name": name, "cfg": c}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("configs", nargs="+", help="economy JSON configs with gacha + banner blocks")
    ap.add_argument("--candidates", help="JSON list of gacha/banner overrides applied to the first config")
    ap.add_argument("--out", default="out/deep_dive")
    a = ap.parse_args(argv)
    scenarios = []
    try:
        for path in a.configs:
            with open(path, encoding="utf-8") as fh:
                scenarios.append(scenario_from(json.load(fh), os.path.splitext(os.path.basename(path))[0]))
        if a.candidates:
            with open(a.candidates, encoding="utf-8") as fh:
                scenarios += [scenario_from(scenarios[0]["cfg"], c["name"], c) for c in json.load(fh)]
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    os.makedirs(a.out, exist_ok=True)

    for sc in scenarios:
        sc["exact"] = exact_stats(sc["cfg"])
        sc["arch"], sc["totals"] = summarise(sc["cfg"], simulate(sc["cfg"]))
        with open(os.path.join(a.out, f"{sc['name']}_featured_pity.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["pull_n", "p_first_featured_at_n", "cdf", "of_which_spark"])
            w.writerows((n, round(m, 8), round(c, 6), round(s, 8)) for n, m, c, s in sc["exact"]["rows"])
        with open(os.path.join(a.out, f"{sc['name']}_archetypes.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(sc["arch"][0].keys()))
            w.writeheader()
            w.writerows({k: round(v, 4) if isinstance(v, float) else v for k, v in r.items()} for r in sc["arch"])

    chart = plot(scenarios, a.out)
    lines = ["# Gacha deep dive: featured SSR, spark, carry-over, paid/free stones", "",
             "Exact math from a fresh account; simulation uses each config's players, sessions and seed.", ""]
    if chart:
        lines += [f"![featured CDF]({os.path.basename(chart)})", ""]
    lines += ["## Scenarios (exact)", "",
              "| Scenario | SSR base | Pulls/SSR | Featured mean | p50 | p90 | p99 | Max | Via spark | "
              "JPY mean | JPY p90 | JPY max |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for sc in scenarios:
        e = sc["exact"]
        y = e["yen_per_pull"]
        lines.append(f"| {sc['name']} | {e['base']:.2%} | {e['ssr_mean']:.1f} | {e['mean']:.1f} | {e['p50']} | "
                     f"{e['p90']} | {e['p99']} | {e['max']} | {e['via_spark']:.1%} | {e['mean'] * y:,.0f} | "
                     f"{e['p90'] * y:,.0f} | {e['max'] * y:,.0f} |")
    lines += ["", "## Scenarios (simulated banner outcomes)", "",
              "| Scenario | Archetype | Avg JPY | Avg pulls | Avg featured | Win rate on wanted banners | "
              "Via spark | Lost pity / player | Lost spark pts / player | JPY per featured | End free | End paid |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for sc in scenarios:
        for r in sc["arch"]:
            lines.append(f"| {sc['name']} | {r['archetype']} | {r['avg_yen']:,.0f} | {r['avg_pulls']:.1f} | "
                         f"{r['avg_featured']:.2f} | {r['banner_win_rate']:.0%} | {r['spark_share']:.0%} | "
                         f"{r['avg_lost_pity']:.1f} | {r['avg_lost_spark']:.1f} | {r['yen_per_featured']:,.0f} | "
                         f"{r['end_free']:,.0f} | {r['end_paid']:,.0f} |")
    lines += ["", "## Paid stones (有償石)", "", "| Scenario | Consume order | Paid share of gacha spend | "
              "Unused paid balance per 1,000 players (JPY) |", "|---|---|---|---|"]
    for sc in scenarios:
        t = sc["totals"]
        lines.append(f"| {sc['name']} | {sc['cfg']['banner'].get('consume', 'free_first')} | "
                     f"{t['paid_share_of_spend']:.1%} | {t['unused_paid_yen_per_1000']:,.0f} |")
    lines += ["", "_A model, not a forecast: replace archetype shares and behaviour with telemetry._", ""]
    with open(os.path.join(a.out, "deep_dive_report.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
