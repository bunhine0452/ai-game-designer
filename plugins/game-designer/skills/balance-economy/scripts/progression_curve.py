#!/usr/bin/env python3
"""Generate and compare XP / level progression tables.

Curve families (XP needed to go from level L to L+1):
  linear    first + step * (L - 1)                (step defaults to first)
  poly      first * ((L + offset) / (1 + offset)) ** exponent
  exp       first * growth ** (L - 1)
  logistic  first + (cap - first) / (1 + e^(-k (L - m)))   S-curve with a soft cap
  all       every family with the same first level and the same total XP

--total keeps --first fixed and solves the family's shape parameter (step,
exponent, growth or cap ratio) so the table sums to the target. That answers
"level 1 takes 100 XP and the cap takes 2M XP in total: what exponent?"

Optional income model (--xp-per-hour) converts XP into play time per level, which
is what players actually feel.

Outputs: <name>.csv (or one CSV per curve with --curve all), <name>_report.md and
<name>.png when matplotlib is available. Standard library only otherwise.

Examples:
  python3 progression_curve.py --curve poly --levels 50 --first 100 --exponent 2.2 \
      --xp-per-hour 900 --income-growth 1.06 --name rpg_xp --out ./out
  python3 progression_curve.py --curve all --levels 60 --total 2000000 --name compare
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import sys

SURFACE, INK, INK_2, MUTED, GRID, BASELINE = ("#fcfcfb", "#0b0b0b", "#52514e",
                                              "#898781", "#e1e0d9", "#c3c2b7")
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
FAMILIES = ["linear", "poly", "exp", "logistic"]


def xp_per_level(family: str, levels: int, a: argparse.Namespace) -> list[float]:
    """XP to advance from level L to L+1, for L = 1 .. levels-1."""
    out = []
    k = a.steepness / levels
    m = a.midpoint * levels
    cap = a.cap_ratio * a.first
    for lvl in range(1, levels):
        if family == "linear":
            out.append(a.first + (a.step if a.step is not None else a.first) * (lvl - 1))
        elif family == "poly":
            out.append(a.first * ((lvl + a.offset) / (1 + a.offset)) ** a.exponent)
        elif family == "exp":
            out.append(a.first * a.growth ** (lvl - 1))
        elif family == "logistic":
            raw = a.first + (cap - a.first) / (1 + math.exp(-k * (lvl - m)))
            base = a.first + (cap - a.first) / (1 + math.exp(-k * (1 - m)))
            out.append(raw * a.first / base)  # anchor level 1->2 at `first`
        else:
            raise ValueError(family)
    return out


SHAPE_PARAM = {"linear": ("step", 0.0, 1e9), "poly": ("exponent", 0.0, 8.0),
               "exp": ("growth", 1.0, 2.0), "logistic": ("cap_ratio", 1.0, 1e5)}


def solve_shape(family: str, levels: int, a: argparse.Namespace, target: float) -> argparse.Namespace:
    """Bisect the family's shape parameter so total XP matches target (first stays fixed)."""
    name, lo, hi = SHAPE_PARAM[family]
    trial = argparse.Namespace(**vars(a))

    def total(value: float) -> float:
        setattr(trial, name, value)
        return sum(xp_per_level(family, levels, trial))

    t_lo, t_hi = total(lo), total(hi)
    if not t_lo <= target <= t_hi:
        raise ValueError(f"{family}: total {target:,.0f} is outside the reachable range "
                         f"{t_lo:,.0f} to {t_hi:,.0f} for the first-level value {a.first:g} (for logistic, raise the steepness)")
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if total(mid) < target else (lo, mid)
    setattr(trial, name, (lo + hi) / 2)
    return trial


def build_table(xp: list[float], a: argparse.Namespace) -> list[dict]:
    rows, cum_xp, cum_h = [], 0.0, 0.0
    for i, need in enumerate(xp):
        lvl = i + 1
        row = {"level": lvl, "xp_to_next": round(need), "cumulative_xp": round(cum_xp),
               "growth_ratio": round(need / xp[i - 1], 4) if i else ""}
        if a.xp_per_hour:
            income = a.xp_per_hour * a.income_growth ** (lvl - 1)
            hours = need / income
            row.update({"xp_per_hour": round(income, 1), "hours_this_level": round(hours, 3),
                        "cumulative_hours": round(cum_h, 2)})
            cum_h += hours
        rows.append(row)
        cum_xp += need
    final = {"level": len(xp) + 1, "xp_to_next": "", "cumulative_xp": round(cum_xp), "growth_ratio": ""}
    if a.xp_per_hour:
        final.update({"xp_per_hour": "", "hours_this_level": "", "cumulative_hours": round(cum_h, 2)})
    rows.append(final)
    return rows


def diagnose(name: str, rows: list[dict], a: argparse.Namespace) -> list[str]:
    body = rows[:-1]
    total = rows[-1]["cumulative_xp"]
    notes = []
    half = next(r["level"] for r in rows if r["cumulative_xp"] >= total / 2)
    notes.append(f"Half of all XP is earned after level {half} of {a.levels} "
                 f"({half / a.levels:.0%} of the level range): "
                 + ("back-loaded; the late game carries most of the grind." if half / a.levels > 0.8
                    else "front-loaded; late levels arrive quickly." if half / a.levels < 0.5
                    else "balanced spread."))
    if a.xp_per_hour:
        hours = [r["hours_this_level"] for r in body]
        total_h = rows[-1]["cumulative_hours"]
        notes.append(f"Time to max level: {total_h:.1f} h. Per level: {min(hours) * 60:.0f} min "
                     f"(fastest) to {max(hours) * 60:.0f} min (slowest).")
        jumps = [(body[i]["level"], hours[i] / hours[i - 1]) for i in range(1, len(hours))
                 if hours[i - 1] > 0 and hours[i] >= 0.25 and hours[i] / hours[i - 1] > a.jump_flag]
        if jumps:
            lv, ratio = max(jumps, key=lambda j: j[1])
            notes.append(f"WARNING: time-per-level jumps x{ratio:.2f} at level {lv}; players feel a wall. "
                         "Smooth the curve or add a new XP source there.")
        if hours[-1] / max(hours[0], 1e-9) > a.wall_ratio:
            notes.append(f"WARNING: last level takes {hours[-1] / hours[0]:.0f}x longer than the first. "
                         "Fine for an endgame grind; risky if the cap is the story's end.")
        if hours[0] * 60 > 30:
            notes.append("WARNING: the first level takes over 30 minutes; early levels should come fast "
                         "to teach the loop and reward the first session.")
    return notes


def write_csv(path: str, rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


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


def plot(tables: dict[str, list[dict]], path: str, title: str, has_time: bool) -> bool:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
    except ImportError:
        return False
    setup_fonts(plt)
    panels = 2 if has_time else 1
    fig, axes = plt.subplots(1, panels, figsize=(6.2 * panels, 4.6), dpi=150, squeeze=False)
    fig.patch.set_facecolor(SURFACE)
    compact = FuncFormatter(lambda v, _: f"{v / 1e6:g}M" if v >= 1e6 else f"{v / 1e3:g}K" if v >= 1e3 else f"{v:g}")
    ax = axes[0][0]
    style_axis(ax, "XP to next level", "Level", "XP")
    ax.yaxis.set_major_formatter(compact)
    for i, (name, rows) in enumerate(tables.items()):
        body = rows[:-1]
        ax.plot([r["level"] for r in body], [r["xp_to_next"] for r in body], color=SERIES[i % 4], lw=2,
                solid_capstyle="round", label=name)
    if has_time:
        ax2 = axes[0][1]
        style_axis(ax2, "Play time per level", "Level", "Minutes")
        for i, (name, rows) in enumerate(tables.items()):
            body = rows[:-1]
            ax2.plot([r["level"] for r in body], [r["hours_this_level"] * 60 for r in body],
                     color=SERIES[i % 4], lw=2, solid_capstyle="round", label=name)
    if len(tables) > 1:
        axes[0][0].legend(frameon=False, fontsize=8.5, labelcolor=INK_2, loc="upper left")
    fig.suptitle(title, x=0.01, ha="left", color=INK, fontsize=13, fontweight="semibold")
    fig.tight_layout()
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--curve", default="poly", choices=FAMILIES + ["all"])
    ap.add_argument("--levels", type=int, default=50, help="max level (table covers 1..levels)")
    ap.add_argument("--first", type=float, default=100, help="XP for level 1 -> 2")
    ap.add_argument("--total", type=float, help="rescale so total XP to max level equals this")
    ap.add_argument("--step", type=float, help="linear: XP added per level (default = first)")
    ap.add_argument("--exponent", type=float, default=2.0, help="poly exponent")
    ap.add_argument("--offset", type=float, default=0.0,
                    help="poly: shifts L so early ratios are gentler (e.g. 5)")
    ap.add_argument("--growth", type=float, default=1.10, help="exp growth per level")
    ap.add_argument("--midpoint", type=float, default=0.5, help="logistic midpoint (fraction of levels)")
    ap.add_argument("--steepness", type=float, default=10.0, help="logistic steepness")
    ap.add_argument("--cap-ratio", type=float, default=40.0, help="logistic plateau as a multiple of first")
    ap.add_argument("--xp-per-hour", type=float, help="XP income per hour at level 1")
    ap.add_argument("--income-growth", type=float, default=1.0, help="income multiplier per level")
    ap.add_argument("--jump-flag", type=float, default=1.6, help="flag level-to-level time jumps above this")
    ap.add_argument("--wall-ratio", type=float, default=40.0, help="flag last/first time-per-level ratio")
    ap.add_argument("--name", default="progression", help="output file stem")
    ap.add_argument("--title", help="chart title")
    ap.add_argument("--out", default=".", help="output directory")
    ap.add_argument("--no-plot", action="store_true")
    a = ap.parse_args(argv)
    if a.levels < 3:
        print("error: --levels must be at least 3", file=sys.stderr)
        return 2
    os.makedirs(a.out, exist_ok=True)

    families = FAMILIES if a.curve == "all" else [a.curve]
    target = a.total
    if a.curve == "all" and target is None:
        target = sum(xp_per_level("poly", a.levels, a))  # compare shapes at equal total XP
    tables, report = {}, [f"# Progression report: {a.title or a.name}", ""]
    for fam in families:
        params = a
        if target:
            try:
                params = solve_shape(fam, a.levels, a, target)
            except ValueError as exc:
                if a.curve != "all":
                    print(f"error: {exc}", file=sys.stderr)
                    return 2
                print(f"warning: skipped {exc}", file=sys.stderr)  # compare the families that can
                report += [f"## {fam} (skipped)", "", f"- {exc}", ""]
                continue
        xp = xp_per_level(fam, a.levels, params)
        rows = build_table(xp, a)
        tables[fam] = rows
        stem = a.name if len(families) == 1 else f"{a.name}_{fam}"
        write_csv(os.path.join(a.out, f"{stem}.csv"), rows)
        pname = SHAPE_PARAM[fam][0]
        shape = f"{pname} = {getattr(params, pname) if getattr(params, pname) is not None else a.first:.4g}"
        report += [f"## {fam} ({shape}{', solved for total' if target else ''})", "",
                   f"- Total XP to level {a.levels}: {rows[-1]['cumulative_xp']:,}",
                   f"- XP for level 1→2: {rows[0]['xp_to_next']:,}; for {a.levels - 1}→{a.levels}: "
                   f"{rows[-2]['xp_to_next']:,}"]
        report += [f"- {n}" for n in diagnose(fam, rows, a)] + [f"- Table: `{stem}.csv`", ""]

    if not tables:
        print("error: no curve family can reach the target total", file=sys.stderr)
        return 2
    sample = tables[next(iter(tables))]
    cols = [c for c in sample[0].keys()]
    report += [f"## Sample rows ({next(iter(tables))})", "", "| " + " | ".join(cols) + " |",
               "|" + "---|" * len(cols)]
    picks = sorted({0, 1, 2, 4, 9, len(sample) // 2, len(sample) - 2, len(sample) - 1})
    report += ["| " + " | ".join(str(sample[i][c]) for c in cols) + " |" for i in picks if i < len(sample)]
    report += ["", "_Read XP together with income: players feel time per level, not XP._", ""]

    chart = os.path.join(a.out, f"{a.name}.png")
    if not a.no_plot and plot(tables, chart, a.title or a.name, bool(a.xp_per_hour)):
        report.insert(2, f"![Progression]({os.path.basename(chart)})\n")
        print(f"wrote {chart}")
    elif not a.no_plot:
        print("note: matplotlib not installed; wrote CSV/Markdown only", file=sys.stderr)
    md = os.path.join(a.out, f"{a.name}_report.md")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(report))
    print("\n".join(line for line in report if line.startswith("- ") or line.startswith("## ")))
    print(f"wrote {md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
