#!/usr/bin/env python3
"""Turn a playtest event log into a funnel, difficulty and drop-off report.

  python3 playtest_report.py examples/playtest-log.csv --out ./out
  python3 playtest_report.py log.csv --levels "Docks,Market,Bell Tower" --out ./out

Input CSV columns: player, t, event, level, value (header required; lines starting with #
are skipped). `t` is seconds since the player's session started.

  event          level              value
  session_start  -                  -
  level_start    level id           -
  level_complete level id           -
  death          level id           -
  hint           level id           -          (help asked for or given)
  quit           level id or -      -          (the player stopped playing)
  rating         question id        1-7        (post-session questionnaire answer)

Outputs (in --out): <stem>_report.md, <stem>_levels.csv, <stem>_ratings.csv and, when
matplotlib is installed, <stem>_funnel.png. Flags: DROP_OFF, DIFFICULTY_SPIKE, SLOW_LEVEL,
QUIT_CLUSTER, LOW_RATING, HINT_HEAVY. Standard library only (matplotlib optional); no network.
"""
from __future__ import annotations

import argparse
import csv
import os
import statistics as st
import sys
from collections import defaultdict


def load(path: str) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        lines = [ln for ln in f if ln.strip() and not ln.lstrip().startswith("#")]
    rows = list(csv.DictReader(lines))
    need = {"player", "t", "event"}
    if not rows or not need <= set(rows[0]):
        raise SystemExit(f"error: the CSV needs at least the columns {sorted(need)}")
    for r in rows:
        r["t"] = float(r["t"] or 0)
        r["level"] = (r.get("level") or "").strip()
        r["event"] = r["event"].strip()
    return sorted(rows, key=lambda r: (r["player"], r["t"]))


def median(xs):
    return st.median(xs) if xs else 0.0


def analyze(rows: list[dict], order: list[str] | None):
    players = sorted({r["player"] for r in rows})
    seen_levels = []
    for r in rows:
        if r["event"] in ("level_start", "level_complete", "death", "hint") and r["level"] and r["level"] not in seen_levels:
            seen_levels.append(r["level"])
    levels = order or seen_levels
    reached, completed = defaultdict(set), defaultdict(set)
    deaths, hints, times, quits = defaultdict(int), defaultdict(int), defaultdict(list), defaultdict(int)
    start_t = {}
    for r in rows:
        p, e, lv = r["player"], r["event"], r["level"]
        if e == "level_start":
            reached[lv].add(p); start_t.setdefault((p, lv), r["t"])
        elif e == "level_complete":
            completed[lv].add(p); reached[lv].add(p)
            if (p, lv) in start_t:
                times[lv].append(r["t"] - start_t[(p, lv)])
        elif e == "death":
            deaths[lv] += 1
        elif e == "hint":
            hints[lv] += 1
        elif e == "quit":
            quits[lv or "(no level)"] += 1
    ratings = defaultdict(list)
    for r in rows:
        if r["event"] == "rating" and r.get("value", "").strip():
            ratings[r["level"] or "overall"].append(float(r["value"]))
    table = []
    for i, lv in enumerate(levels):
        n_reach, n_done = len(reached[lv]), len(completed[lv])
        table.append({"level": lv, "reached": n_reach, "completed": n_done,
                      "completion_rate": n_done / n_reach if n_reach else 0.0,
                      "deaths": deaths[lv], "deaths_per_player": deaths[lv] / n_reach if n_reach else 0.0,
                      "hints": hints[lv], "median_time_s": median(times[lv]), "quits_here": quits.get(lv, 0)})
    return players, table, quits, ratings


def flags(players, table, quits, ratings) -> list[str]:
    out, n = [], len(players)
    for prev, cur in zip(table, table[1:]):
        if prev["reached"] and (prev["reached"] - cur["reached"]) / prev["reached"] > 0.25:
            out.append(f"DROP_OFF: {prev['reached']} reached {prev['level']} but only {cur['reached']} reached {cur['level']} "
                       f"({(prev['reached'] - cur['reached']) / prev['reached']:.0%} lost).")
    dpp = [t["deaths_per_player"] for t in table if t["reached"]]
    base = median(dpp)
    for t in table:
        if t["reached"] and t["deaths_per_player"] >= max(2.0, 2 * base) and base >= 0:
            out.append(f"DIFFICULTY_SPIKE: {t['level']} averages {t['deaths_per_player']:.1f} deaths per player (median across levels {base:.1f}).")
    mt = [t["median_time_s"] for t in table if t["median_time_s"]]
    base_t = median(mt)
    for t in table:
        if base_t and t["median_time_s"] > 2 * base_t:
            out.append(f"SLOW_LEVEL: {t['level']} takes {t['median_time_s'] / 60:.1f} min (median), over twice the typical {base_t / 60:.1f} min.")
    total_q = sum(quits.values())
    for lv, q in quits.items():
        if total_q >= 3 and q >= 2 and q / total_q >= 0.25:
            out.append(f"QUIT_CLUSTER: {q} of {total_q} quits happened in {lv}.")
    for t in table:
        if t["reached"] and t["hints"] / t["reached"] >= 1.0:
            out.append(f"HINT_HEAVY: {t['level']} needed {t['hints']} hints for {t['reached']} players.")
    for q, vals in ratings.items():
        if len(vals) >= 3 and st.mean(vals) < 4.0:
            out.append(f"LOW_RATING: '{q}' averages {st.mean(vals):.1f} / 7 (n={len(vals)}).")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("log", help="event log CSV")
    ap.add_argument("--levels", help="comma-separated level order (default: order of first appearance)")
    ap.add_argument("--out", default="playtest-out")
    a = ap.parse_args()
    rows = load(a.log)
    players, table, quits, ratings = analyze(rows, [s.strip() for s in a.levels.split(",")] if a.levels else None)
    fl = flags(players, table, quits, ratings)
    os.makedirs(a.out, exist_ok=True)
    stem = os.path.splitext(os.path.basename(a.log))[0]
    with open(os.path.join(a.out, f"{stem}_levels.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(table[0]) if table else ["level"]); w.writeheader(); w.writerows(table)
    with open(os.path.join(a.out, f"{stem}_ratings.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["question", "n", "mean", "min", "max"])
        for q, v in sorted(ratings.items()):
            w.writerow([q, len(v), f"{st.mean(v):.2f}", min(v), max(v)])
    n = len(players)
    md = [f"# Playtest report: {stem}", "", f"- Players: **{n}**",
          f"- Finished the last level: **{table[-1]['completed'] if table else 0} of {n}**", "",
          "## Funnel and difficulty", "", "| Level | Reached | Completed | Completion | Deaths / player | Hints | Median time | Quits here |",
          "|---|---|---|---|---|---|---|---|"]
    for t in table:
        md.append(f"| {t['level']} | {t['reached']} of {n} | {t['completed']} | {t['completion_rate']:.0%} | {t['deaths_per_player']:.1f} | "
                  f"{t['hints']} | {t['median_time_s'] / 60:.1f} min | {t['quits_here']} |")
    if ratings:
        md += ["", "## Questionnaire (1–7)", "", "| Question | n | Mean | Range |", "|---|---|---|---|"]
        md += [f"| {q} | {len(v)} | {st.mean(v):.1f} | {min(v):g}–{max(v):g} |" for q, v in sorted(ratings.items())]
    md += ["", "## Flags", ""] + ([f"- {x}" for x in fl] or ["- None. Check the qualitative notes before calling it done."])
    md += ["", "Numbers show *where* players struggled, not *why*. Pair each flag with observer notes",
           "(see `references/playtest-kit.md`) before deciding on a fix, and re-test the fix."]
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 4.2))
        xs = range(len(table))
        ax.bar(xs, [t["reached"] for t in table], color="#9fb7c9", label="reached")
        ax.bar(xs, [t["completed"] for t in table], color="#3b6e8f", label="completed")
        ax2 = ax.twinx(); ax2.plot(xs, [t["deaths_per_player"] for t in table], color="#d1495b", marker="o", label="deaths / player")
        ax.set_xticks(list(xs)); ax.set_xticklabels([t["level"] for t in table], rotation=20, ha="right")
        ax.set_ylabel("players"); ax2.set_ylabel("deaths per player"); ax.set_title(f"Playtest funnel: {stem} (n={n})")
        h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1 + h2, l1 + l2, loc="upper right", fontsize=8)
        fig.tight_layout(); png = os.path.join(a.out, f"{stem}_funnel.png"); fig.savefig(png, dpi=130); plt.close(fig)
        md.insert(4, f"![Funnel]({os.path.basename(png)})\n")
    except ImportError:
        pass
    with open(os.path.join(a.out, f"{stem}_report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    sys.exit(main())
