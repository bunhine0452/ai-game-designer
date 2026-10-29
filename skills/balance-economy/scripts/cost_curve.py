#!/usr/bin/env python3
"""Fit a cost curve to cards / units / items and flag the outliers.

Model: cost ~ intercept + sum(weight_i * attribute_i), fitted by least squares.
Each weight is "how much one point of that attribute is worth in cost". The fitted
"fair cost" of each item is compared with its actual cost:
  residual = fair - actual > 0   -> item is undercosted (too strong for its cost)
  residual = fair - actual < 0   -> item is overcosted  (too weak for its cost)

Input CSV: a name column, a cost column, then numeric attribute columns
(booleans as 0/1). Non-numeric extra columns are ignored.

Outputs: <stem>_fit.csv, <stem>_report.md, and <stem>_fit.png with matplotlib.

Examples:
  python3 cost_curve.py ../examples/card-set.csv --out ./out
  python3 cost_curve.py units.csv --cost-col gold --name-col unit --robust
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import sys

SURFACE, INK, INK_2, MUTED, GRID, BASELINE = ("#fcfcfb", "#0b0b0b", "#52514e",
                                              "#898781", "#e1e0d9", "#c3c2b7")
SERIES = ["#2a78d6", "#eb6834", "#1baf7a"]


def load(path: str, name_col: str, cost_col: str, exclude_cols: set[str]):
    with open(path, encoding="utf-8-sig") as fh:
        rows = [r for r in csv.DictReader(ln for ln in fh if ln.strip() and not ln.lstrip().startswith("#"))]
    if not rows:
        raise ValueError("no rows")
    cols = [c for c in rows[0].keys() if c not in (name_col, cost_col) and c not in exclude_cols]

    def numeric(col: str) -> bool:
        for r in rows:
            v = (r.get(col) or "").strip()
            if v == "":
                continue
            try:
                float(v)
            except ValueError:
                return v.lower() in ("true", "false", "yes", "no")
        return True

    attrs = [c for c in cols if numeric(c)]
    to_num = lambda v: 1.0 if str(v).strip().lower() in ("true", "yes") else 0.0 if str(v).strip().lower() in (  # noqa: E731
        "false", "no", "") else float(v)
    items = []
    for r in rows:
        if name_col not in r or cost_col not in r:
            raise ValueError(f"CSV needs '{name_col}' and '{cost_col}' columns")
        items.append({"name": r[name_col], "cost": float(r[cost_col]),
                      "x": [to_num(r.get(c, "")) for c in attrs]})
    return items, attrs


def solve(a: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[piv][col]) < 1e-12:
            raise ValueError("singular system: an attribute is constant or duplicated; drop it")
        m[col], m[piv] = m[piv], m[col]
        for r in range(n):
            if r != col:
                f = m[r][col] / m[col][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [m[i][n] / m[i][i] for i in range(n)]


def fit(items, n_attr: int, intercept: bool, ridge: float) -> list[float]:
    design = [([1.0] if intercept else []) + it["x"] for it in items]
    k = len(design[0])
    xtx = [[sum(row[i] * row[j] for row in design) + (ridge if i == j and (i > 0 or not intercept) else 0.0)
            for j in range(k)] for i in range(k)]
    xty = [sum(row[i] * it["cost"] for row, it in zip(design, items)) for i in range(k)]
    return solve(xtx, xty)


def predict(coef: list[float], x: list[float], intercept: bool) -> float:
    return (coef[0] if intercept else 0.0) + sum(w * v for w, v in zip(coef[1:] if intercept else coef, x))


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


def plot(results, path: str, title: str) -> bool:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
    except ImportError:
        return False
    setup_fonts(plt)
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    lo = min(min(r["cost"], r["fair"]) for r in results) - 0.5
    hi = max(max(r["cost"], r["fair"]) for r in results) + 0.5
    ax.plot([lo, hi], [lo, hi], color=MUTED, lw=1.5, ls=(0, (4, 3)))
    groups = {"on curve": (SERIES[0], "o"), "undercosted (too strong)": (SERIES[1], "^"),
              "overcosted (too weak)": (SERIES[2], "s")}
    for label, (color, marker) in groups.items():
        pts = [r for r in results if r["verdict"] == label]
        ax.scatter([r["cost"] for r in pts], [r["fair"] for r in pts], s=70, c=color, marker=marker,
                   edgecolors=SURFACE, linewidths=2, zorder=3)
        for r in pts if label != "on curve" else []:
            ax.annotate(r["name"], (r["cost"], r["fair"]), xytext=(6, 4), textcoords="offset points",
                        fontsize=8.5, color=INK_2)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_xlabel("Actual cost", color=INK_2)
    ax.set_ylabel("Fair cost from the fitted curve", color=INK_2)
    ax.grid(color=GRID, lw=1)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(BASELINE)
    ax.tick_params(colors=MUTED, length=0)
    ax.set_title(title, loc="left", color=INK, fontsize=13, fontweight="semibold")
    handles = [Line2D([], [], marker=m, color=c, ls="", markersize=8, markeredgecolor=SURFACE, label=l)
               for l, (c, m) in groups.items()]
    handles.append(Line2D([], [], color=MUTED, lw=1.5, ls=(0, (4, 3)), label="fair = actual"))
    ax.legend(handles=handles, frameon=False, fontsize=8.5, labelcolor=INK_2, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", help="items CSV")
    ap.add_argument("--name-col", default="name")
    ap.add_argument("--cost-col", default="cost")
    ap.add_argument("--ignore", default="", help="comma-separated columns to ignore")
    ap.add_argument("--no-intercept", action="store_true", help="force the curve through zero")
    ap.add_argument("--ridge", type=float, default=1e-6, help="L2 regularisation for small sets")
    ap.add_argument("--robust", action="store_true", help="refit without |z|>2 outliers, then judge all")
    ap.add_argument("--threshold", type=float, help="flag |residual| above this (default 1.5 x RMSE, min 0.5)")
    ap.add_argument("--title", help="chart title")
    ap.add_argument("--out", help="output directory (default: next to the CSV)")
    ap.add_argument("--no-plot", action="store_true")
    a = ap.parse_args(argv)
    try:
        items, attrs = load(a.csv, a.name_col, a.cost_col, {c.strip() for c in a.ignore.split(",") if c.strip()})
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    intercept = not a.no_intercept
    if len(items) <= len(attrs) + int(intercept):
        print(f"error: {len(items)} items cannot fit {len(attrs)} attributes; add items or drop columns",
              file=sys.stderr)
        return 2
    try:
        coef = fit(items, len(attrs), intercept, a.ridge)
        if a.robust:
            res = [it["cost"] - predict(coef, it["x"], intercept) for it in items]
            sd = math.sqrt(sum(r * r for r in res) / len(res)) or 1.0
            core = [it for it, r in zip(items, res) if abs(r) / sd <= 2]
            if len(core) > len(attrs) + int(intercept):
                coef = fit(core, len(attrs), intercept, a.ridge)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    results = []
    for it in items:
        fair = predict(coef, it["x"], intercept)
        results.append({"name": it["name"], "cost": it["cost"], "fair": fair, "residual": fair - it["cost"]})
    rmse = math.sqrt(sum(r["residual"] ** 2 for r in results) / len(results))
    mean_cost = sum(r["cost"] for r in results) / len(results)
    ss_tot = sum((r["cost"] - mean_cost) ** 2 for r in results) or 1.0
    r2 = 1 - sum(r["residual"] ** 2 for r in results) / ss_tot
    threshold = a.threshold if a.threshold is not None else max(0.5, 1.5 * rmse)
    for r in results:
        r["verdict"] = ("undercosted (too strong)" if r["residual"] > threshold else
                        "overcosted (too weak)" if r["residual"] < -threshold else "on curve")

    out_dir = a.out or os.path.dirname(os.path.abspath(a.csv))
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(a.csv))[0]
    with open(os.path.join(out_dir, f"{stem}_fit.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "cost", "fair_cost", "residual", "verdict"])
        for r in sorted(results, key=lambda r: -r["residual"]):
            w.writerow([r["name"], r["cost"], round(r["fair"], 2), round(r["residual"], 2), r["verdict"]])

    weights = list(zip((["(intercept)"] if intercept else []) + attrs, coef))
    lines = [f"# Cost curve: {a.title or stem}", ""]
    chart = os.path.join(out_dir, f"{stem}_fit.png")
    if not a.no_plot and plot(results, chart, a.title or f"Cost curve: {stem}"):
        lines += [f"![Cost curve]({os.path.basename(chart)})", ""]
    elif not a.no_plot:
        print("note: matplotlib not installed; wrote CSV/Markdown only", file=sys.stderr)
    lines += [f"Fit on {len(items)} items: R² = {r2:.3f}, RMSE = {rmse:.2f} cost. "
              f"Flag threshold ±{threshold:.2f}.", "", "## Value of each attribute (in cost units)", "",
              "| Attribute | Cost per point |", "|---|---|"]
    lines += [f"| {n} | {w:+.3f} |" for n, w in weights]
    if intercept:
        lines += ["", "_The intercept is the baseline cost every item pays (e.g. the card itself). A "
                  "negative weight usually marks a drawback; if a 'positive' attribute fits negative, "
                  "it is overvalued in the current set or confounded with another column._"]
    flagged = sorted((r for r in results if r["verdict"] != "on curve"), key=lambda r: -abs(r["residual"]))
    lines += ["", "## Outliers", ""]
    if not flagged:
        lines.append("None beyond the threshold. The set sits on one curve.")
    for r in flagged:
        direction = "raise its cost or trim its stats" if r["residual"] > 0 else "lower its cost or add value"
        lines.append(f"- **{r['name']}** costs {r['cost']:g}, fair ≈ {r['fair']:.1f} "
                     f"({r['residual']:+.1f}): {r['verdict']}; {direction}.")
    lines += ["", "## All items", "", "| Item | Cost | Fair | Residual | Verdict |", "|---|---|---|---|---|"]
    lines += [f"| {r['name']} | {r['cost']:g} | {r['fair']:.2f} | {r['residual']:+.2f} | {r['verdict']} |"
              for r in sorted(results, key=lambda r: -r["residual"])]
    lines += ["", "_A linear cost curve misses synergies, conditional text and metagame context. Use it "
              "to find suspects, then playtest._", ""]
    md = os.path.join(out_dir, f"{stem}_report.md")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"R² {r2:.3f}, RMSE {rmse:.2f}; weights: " + ", ".join(f"{n} {w:+.2f}" for n, w in weights))
    for r in flagged:
        print(f"  {r['verdict']:26} {r['name']}: cost {r['cost']:g}, fair {r['fair']:.2f}")
    print(f"wrote {md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
