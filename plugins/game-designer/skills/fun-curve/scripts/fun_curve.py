#!/usr/bin/env python3
"""Plot and diagnose an interest curve (fun curve) from a beat list.

Input  : CSV with columns time,intensity[,type][,label] or JSON (a list of beats,
         or {"title": ..., "unit": ..., "beats": [...]}). Time may be a number or
         "mm:ss" / "hh:mm:ss". Intensity is felt engagement/tension on 0-10.
Output : <stem>_report.md   diagnostics, metrics, beat table, ASCII curve
         <stem>_report.json  same data, machine-readable
         <stem>_resampled.csv  evenly resampled curve for spreadsheets
         <stem>_curve.png     chart (only if matplotlib is installed)

Standard library only; matplotlib is optional and the script degrades to
text/CSV output without it.

Example:
  python3 fun_curve.py ../examples/roguelite-20min-run.csv --out ./out --reference
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from dataclasses import asdict, dataclass

SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2, "info": 3}
SEVERITY_PENALTY = {"high": 15, "medium": 8, "low": 3, "info": 0}

# Reference palette (validated categorical order; see README "Charts").
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
          "#e87ba4", "#008300", "#6250d6", "#e34948"]
MARKERS = ["o", "s", "^", "D", "v", "p", "h", "<"]
STATUS = {"good": "#0ca30c", "warning": "#fab219", "critical": "#d03b3b"}

# Schell-style reference shape: hook, dip, rising peaks, climax, resolution.
REFERENCE_SHAPE = [(0.0, 0.30), (0.05, 0.75), (0.12, 0.35), (0.28, 0.55), (0.36, 0.40),
                   (0.52, 0.70), (0.60, 0.50), (0.78, 0.85), (0.88, 1.00), (1.0, 0.45)]


@dataclass
class Beat:
    time: float
    intensity: float
    type: str = ""
    label: str = ""
    new: bool = False      # introduces something new: a rule, enemy, place or open question


# Beat types that put a fresh question in front of the player (curiosity supply).
CURIOSITY_TYPES = {"reveal", "discovery", "twist", "mystery", "new", "unlock", "surprise", "question"}


@dataclass
class Finding:
    code: str
    severity: str
    message: str
    suggestion: str = ""
    start: float | None = None
    end: float | None = None


# ---------------------------------------------------------------- input ---

def parse_time(raw: str | float) -> float:
    """Accept 12, 12.5, '12:30' (mm:ss) or '1:02:30' (hh:mm:ss) -> minutes-or-units."""
    if isinstance(raw, (int, float)):
        return float(raw)
    text = str(raw).strip()
    if ":" not in text:
        return float(text)
    parts = [float(p) for p in text.split(":")]
    if len(parts) == 2:
        return parts[0] + parts[1] / 60.0
    if len(parts) == 3:
        return parts[0] * 60.0 + parts[1] + parts[2] / 60.0
    raise ValueError(f"unrecognised time value: {raw!r}")


def _pick(row: dict, *names: str, default: str = "") -> str:
    lowered = {k.strip().lower(): v for k, v in row.items() if k}
    for name in names:
        if name in lowered and lowered[name] not in (None, ""):
            return str(lowered[name]).strip()
    return default


def load_beats(path: str) -> tuple[list[Beat], dict]:
    meta: dict = {}
    with open(path, encoding="utf-8-sig") as fh:
        text = fh.read()
    if path.lower().endswith(".json"):
        data = json.loads(text)
        if isinstance(data, dict):
            meta = {k: v for k, v in data.items() if k != "beats"}
            data = data.get("beats", [])
        rows = [{str(k).lower(): v for k, v in item.items()} for item in data]
    else:
        lines = []
        for ln in text.splitlines():
            stripped = ln.strip()
            if stripped.startswith("#"):
                key, _, value = stripped.lstrip("#").partition(":")
                if key.strip().lower() in ("title", "unit") and value.strip():
                    meta[key.strip().lower()] = value.strip()
            elif stripped:
                lines.append(ln)
        rows = list(csv.DictReader(lines))
    beats = []
    for i, row in enumerate(rows, start=1):
        t_raw = _pick(row, "time", "t", "minute", "min", "start")
        v_raw = _pick(row, "intensity", "interest", "tension", "value", "level")
        if t_raw == "" or v_raw == "":
            raise ValueError(f"row {i}: needs 'time' and 'intensity' columns")
        value = float(v_raw)
        if not 0 <= value <= 10:
            print(f"warning: row {i} intensity {value} clamped to 0-10", file=sys.stderr)
            value = min(10.0, max(0.0, value))
        flag = _pick(row, "new", "novel", "question").strip().lower()
        beats.append(Beat(parse_time(t_raw), value,
                          _pick(row, "type", "kind", "category").lower(),
                          _pick(row, "label", "name", "note", "description"),
                          flag not in ("", "0", "no", "n", "false", "-")))
    beats.sort(key=lambda b: b.time)
    if len(beats) < 3:
        raise ValueError("need at least 3 beats to analyse a curve")
    if beats[-1].time <= beats[0].time:
        raise ValueError("beats must span a positive duration")
    return beats, meta


# ------------------------------------------------------------- analysis ---

def resample(beats: list[Beat], points: int = 400) -> list[tuple[float, float]]:
    t0, t1 = beats[0].time, beats[-1].time
    out, j = [], 0
    for k in range(points + 1):
        t = t0 + (t1 - t0) * k / points
        while j < len(beats) - 2 and beats[j + 1].time < t:
            j += 1
        a, b = beats[j], beats[j + 1]
        span = b.time - a.time
        frac = 0.0 if span <= 0 else min(1.0, max(0.0, (t - a.time) / span))
        out.append((t, a.intensity + (b.intensity - a.intensity) * frac))
    return out


def find_peaks(beats: list[Beat], peak_min: float) -> list[int]:
    peaks = []
    for i, b in enumerate(beats):
        if b.intensity < peak_min:
            continue
        left_ok = i == 0 or b.intensity >= beats[i - 1].intensity
        right_ok = i == len(beats) - 1 or b.intensity > beats[i + 1].intensity
        if left_ok and right_ok:
            peaks.append(i)
    return peaks


def segments(curve, predicate) -> list[tuple[float, float]]:
    """Contiguous [start, end] time ranges of the resampled curve where predicate(v)."""
    out, start = [], None
    for t, v in curve:
        if predicate(v):
            start = t if start is None else start
        elif start is not None:
            out.append((start, prev_t))
            start = None
        prev_t = t
    if start is not None:
        out.append((start, curve[-1][0]))
    return out


def slope(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    den = sum((x - mx) ** 2 for x in xs)
    return 0.0 if den == 0 else sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den


def analyse(beats: list[Beat], cfg: argparse.Namespace) -> dict:
    t0, t1 = beats[0].time, beats[-1].time
    dur = t1 - t0
    curve = resample(beats)
    values = [v for _, v in curve]
    findings: list[Finding] = []
    fmt = lambda t: f"{t:.1f}"  # noqa: E731

    # 1. Hook
    hook_end = t0 + cfg.hook_window * dur
    hook_beats = [b for b in beats if b.time <= hook_end]
    hook_peak = max((b.intensity for b in hook_beats), default=0.0)
    if hook_peak < cfg.hook_min:
        findings.append(Finding(
            "MISSING_HOOK", "high",
            f"No beat reaches {cfg.hook_min:g}/10 in the first {cfg.hook_window:.0%} of the experience "
            f"(best is {hook_peak:g}). Players decide early whether to keep going.",
            "Open with a short, legible high-interest moment (a promise of the core fantasy, a "
            "striking reveal, or a quick win), then dip to teach.", t0, hook_end))

    # 2. Flat zones
    min_len = cfg.flat_min * dur
    i = 0
    while i < len(curve):
        lo = hi = curve[i][1]
        j = i
        while j + 1 < len(curve):
            v = curve[j + 1][1]
            if max(hi, v) - min(lo, v) > cfg.flat_tolerance:
                break
            lo, hi, j = min(lo, v), max(hi, v), j + 1
        length = curve[j][0] - curve[i][0]
        if length >= min_len:
            level = sum(values[i:j + 1]) / (j - i + 1)
            if level < 4:
                sev, why = "high", "low and flat: boredom and quit risk"
            elif level >= 7:
                sev, why = "medium", "high and flat: numbness and fatigue risk"
            else:
                sev, why = "medium", "flat: interest stops moving"
            findings.append(Finding(
                "FLAT_ZONE", sev,
                f"{fmt(curve[i][0])}-{fmt(curve[j][0])}: intensity stays within "
                f"±{cfg.flat_tolerance / 2:g} around {level:.1f} for {length:.1f} units ({why}).",
                "Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, "
                "a reward, or a deliberate rest that sets up the next rise.", curve[i][0], curve[j][0]))
            i = j + 1
        else:
            i += 1

    # 3. Peaks, climax, relief
    peaks = find_peaks(beats, cfg.peak_min)
    climax_idx = max(range(len(beats)), key=lambda k: (beats[k].intensity, beats[k].time))
    climax = beats[climax_idx]
    climax_pos = (climax.time - t0) / dur
    window = cfg.relief_window * dur
    for p in peaks:
        pb = beats[p]
        if p == climax_idx or pb.time + window > t1:
            continue
        after = [v for t, v in curve if pb.time < t <= pb.time + window]
        if after and min(after) > pb.intensity - cfg.relief_drop:
            findings.append(Finding(
                "NO_RELIEF", "medium",
                f"Peak at {fmt(pb.time)} ({pb.intensity:g}{', ' + pb.label if pb.label else ''}) is not "
                f"followed by a drop of {cfg.relief_drop:g}+ within {window:.1f} units.",
                "After a peak, give a release beat (safe room, loot, story, shop, short traversal) "
                "so the next peak lands harder.", pb.time, pb.time + window))
    for s, e in segments(curve, lambda v: v >= cfg.high):
        if e - s > cfg.sustain_max * dur:
            findings.append(Finding(
                "SUSTAINED_PEAK", "medium",
                f"{fmt(s)}-{fmt(e)}: intensity stays at or above {cfg.high:g} for {e - s:.1f} units "
                f"({(e - s) / dur:.0%} of the run).",
                "Break the plateau into two peaks with a short release between them, or vary the "
                "kind of intensity (spatial, cognitive, emotional).", s, e))

    if climax_pos < cfg.climax_min:
        findings.append(Finding(
            "EARLY_CLIMAX", "high",
            f"The strongest moment ({climax.intensity:g}{', ' + climax.label if climax.label else ''}) "
            f"happens at {climax_pos:.0%} of the experience; later beats never top it.",
            f"Move or build a climax into the last {1 - cfg.climax_min:.0%}, or reduce the early peak "
            "so the ending is the highest point.", climax.time, climax.time))
    elif climax_idx == len(beats) - 1:
        findings.append(Finding(
            "NO_RESOLUTION", "low",
            "The experience ends on its climax with no resolution beat.",
            "Add a short denouement (reward, results screen with meaning, story button) unless "
            "ending on the peak is intentional, as in an arcade loop.", climax.time, climax.time))
    elif t1 - climax.time > 0.2 * dur:
        findings.append(Finding(
            "LONG_TAIL", "low",
            f"{(t1 - climax.time) / dur:.0%} of the run comes after the climax.",
            "Shorten the post-climax tail or give it its own small arc.", climax.time, t1))

    # 4. Escalation of peaks after the hook
    mid_peaks = [beats[p] for p in peaks if beats[p].time > hook_end]
    if len(mid_peaks) >= 3:
        s = slope([b.time for b in mid_peaks], [b.intensity for b in mid_peaks]) * dur
        if s <= 0:
            findings.append(Finding(
                "NO_ESCALATION", "medium",
                f"Peaks after the hook don't rise (trend {s:+.1f} points across the run).",
                "Make each major peak a little stronger or more complex than the last: sawtooth "
                "upward, resetting lower after each release.", mid_peaks[0].time, mid_peaks[-1].time))

    # 5. Variety of beat types
    typed = [b for b in beats if b.type]
    if typed:
        run_start = 0
        for k in range(1, len(beats) + 1):
            if k == len(beats) or beats[k].type != beats[run_start].type:
                run = beats[run_start:k]
                span = run[-1].time - run[0].time
                if run[0].type and (len(run) >= cfg.max_run or span >= 0.25 * dur):
                    findings.append(Finding(
                        "MONOTONY", "medium" if span >= 0.25 * dur else "low",
                        f"{len(run)} consecutive '{run[0].type}' beats from {fmt(run[0].time)} to "
                        f"{fmt(run[-1].time)}.",
                        "Interleave a different activity or change the rules of the repeated one.",
                        run[0].time, run[-1].time))
                run_start = k
        counts: dict[str, int] = {}
        for b in typed:
            counts[b.type] = counts.get(b.type, 0) + 1
        top, top_n = max(counts.items(), key=lambda kv: kv[1])
        if len(typed) >= 8 and top_n / len(typed) > 0.5:
            findings.append(Finding(
                "LOW_VARIETY", "low",
                f"'{top}' makes up {top_n / len(typed):.0%} of beats.",
                "Check that the dominant activity has internal variety (enemy mixes, rule twists)."))

    # 6. Load balance
    high_share = sum(v >= cfg.high for v in values) / len(values)
    low_share = sum(v <= cfg.low for v in values) / len(values)
    if high_share > cfg.high_share:
        findings.append(Finding(
            "FATIGUE_RISK", "medium",
            f"{high_share:.0%} of the time is at intensity {cfg.high:g}+.",
            "Peaks need valleys; lower some mid-run beats so the high ones stay special."))
    if low_share > cfg.low_share:
        findings.append(Finding(
            "DOWNTIME_RISK", "medium",
            f"{low_share:.0%} of the time is at intensity {cfg.low:g} or below.",
            "Shorten low stretches or give them a purpose (anticipation, planning, curiosity)."))

    # 7. Curiosity supply: fun is uncertainty resolved faster than expected, so new questions
    #    must keep arriving. Only checked when the beat list marks them (types or a `new` column).
    fresh = [b.time for b in beats if b.new or b.type in CURIOSITY_TYPES]
    if len(fresh) >= 2:
        stop = climax.time if climax.time > fresh[-1] else fresh[-1]   # nothing new is needed after the climax
        marks = [t0] + fresh + [stop]
        gap, gs, ge = max((marks[k + 1] - marks[k], marks[k], marks[k + 1]) for k in range(len(marks) - 1))
        if gap > cfg.curiosity_gap * dur:
            findings.append(Finding(
                "CURIOSITY_GAP", "medium" if gap > 0.4 * dur else "low",
                f"Nothing new arrives between {fmt(gs)} and {fmt(ge)} ({gap / dur:.0%} of the run): no fresh "
                "question for the player to resolve.",
                "Introduce a rule twist, enemy, place or story question in that stretch, or plant a visible "
                "unexplained thing earlier that pays off there.", gs, ge))

    # 8. Data density
    gaps = [(beats[k + 1].time - beats[k].time, beats[k].time, beats[k + 1].time)
            for k in range(len(beats) - 1)]
    gap, gs, ge = max(gaps)
    if gap > cfg.sparse_gap * dur:
        findings.append(Finding(
            "SPARSE_DATA", "info",
            f"No beats between {fmt(gs)} and {fmt(ge)} ({gap / dur:.0%} of the run); the curve "
            "there is interpolated.", "Add the beats that happen in that stretch.", gs, ge))

    findings.sort(key=lambda f: (SEVERITY_ORDER[f.severity], f.start if f.start is not None else 0))
    score = max(0, 100 - sum(SEVERITY_PENALTY[f.severity] for f in findings))
    metrics = {
        "duration": round(dur, 2),
        "beats": len(beats),
        "curiosity_beats": len(fresh),
        "mean_intensity": round(sum(values) / len(values), 2),
        "peak_count": len(peaks),
        "climax_time": climax.time,
        "climax_position": round(climax_pos, 3),
        "climax_intensity": climax.intensity,
        "hook_peak": hook_peak,
        "share_high": round(high_share, 3),
        "share_low": round(low_share, 3),
        "pacing_score": score,
    }
    return {"metrics": metrics, "findings": findings, "curve": curve,
            "peaks": peaks, "climax_idx": climax_idx, "hook_end": hook_end}


# --------------------------------------------------------------- output ---

def ascii_chart(curve, beats, width: int = 64, height: int = 10) -> str:
    t0, t1 = curve[0][0], curve[-1][0]
    grid = [[" "] * width for _ in range(height + 1)]
    for col in range(width):
        t = t0 + (t1 - t0) * col / (width - 1)
        v = min(curve, key=lambda tv: abs(tv[0] - t))[1]
        grid[height - round(v / 10 * height)][col] = "·"
    for b in beats:
        col = round((b.time - t0) / (t1 - t0) * (width - 1))
        grid[height - round(b.intensity / 10 * height)][col] = "o"
    rows = [f"{10 - r * 10 // height:>3} |" + "".join(line) for r, line in enumerate(grid)]
    rows.append("    +" + "-" * width)
    rows.append(f"     {t0:<10.1f}{'':{width - 20}}{t1:>10.1f}")
    return "\n".join(rows)


def write_reports(beats, result, meta, out_dir, stem, unit, chart_path):
    m, findings = result["metrics"], result["findings"]
    title = meta.get("title") or stem
    lines = [f"# Interest curve report: {title}", ""]
    lines += ["| Metric | Value |", "|---|---|",
              f"| Duration | {m['duration']} {unit} |",
              f"| Beats | {m['beats']} |",
              f"| Mean intensity | {m['mean_intensity']} / 10 |",
              f"| Peaks (≥ threshold) | {m['peak_count']} |",
              f"| Climax | {m['climax_intensity']:g} at {m['climax_time']:g} {unit} "
              f"({m['climax_position']:.0%} through) |",
              f"| Hook strength | {m['hook_peak']:g} / 10 |",
              f"| Time at high intensity | {m['share_high']:.0%} |",
              f"| Time at low intensity | {m['share_low']:.0%} |",
              f"| Pacing health (heuristic) | {m['pacing_score']} / 100 |", ""]
    if chart_path:
        lines += [f"![Interest curve]({os.path.basename(chart_path)})", ""]
    lines += ["## Findings", ""]
    if not findings:
        lines += ["No pacing problems detected by the heuristics. Validate with playtests.", ""]
    for f in findings:
        span = ""
        if f.start is not None:
            span = (f" ({f.start:.1f}-{f.end:.1f} {unit})" if f.end not in (None, f.start)
                    else f" (at {f.start:.1f} {unit})")
        lines += [f"- **[{f.severity.upper()}] {f.code}**{span}: {f.message}",
                  f"  - Fix: {f.suggestion}" if f.suggestion else ""]
    lines += ["", "## Curve (text view)", "", "```", ascii_chart(result["curve"], beats), "```", "",
              "## Beats", "", f"| Time ({unit}) | Intensity | Type | Label |", "|---|---|---|---|"]
    lines += [f"| {b.time:g} | {b.intensity:g} | {b.type} | {b.label} |" for b in beats]
    lines += ["", "_Heuristic diagnostics. Thresholds are configurable; confirm with playtest "
              "data (quit points, session length, observed affect)._", ""]
    md_path = os.path.join(out_dir, f"{stem}_report.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(ln for ln in lines if ln is not None))
    json_path = os.path.join(out_dir, f"{stem}_report.json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({"title": title, "unit": unit, "metrics": m,
                   "findings": [asdict(f) for f in findings],
                   "beats": [asdict(b) for b in beats]}, fh, indent=2, ensure_ascii=False)
    csv_path = os.path.join(out_dir, f"{stem}_resampled.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow([f"time_{unit}", "intensity"])
        writer.writerows((round(t, 3), round(v, 3)) for t, v in result["curve"])
    return md_path, json_path, csv_path


def setup_fonts(plt) -> None:
    """Use an installed UI sans plus CJK fallbacks so non-English labels render."""
    import logging
    from matplotlib import font_manager
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
    available = {f.name for f in font_manager.fontManager.ttflist}
    latin = [f for f in ("Helvetica Neue", "Helvetica", "Arial", "Segoe UI", "DejaVu Sans")
             if f in available][:1]
    cjk = [f for f in ("Apple SD Gothic Neo", "AppleGothic", "Malgun Gothic", "Noto Sans CJK KR",
                       "Hiragino Sans", "Yu Gothic", "Noto Sans CJK JP", "PingFang SC",
                       "Microsoft YaHei", "Noto Sans CJK SC") if f in available]
    plt.rcParams.update({"font.family": (latin or ["DejaVu Sans"]) + cjk, "font.size": 10,
                         "axes.unicode_minus": False})


def plot(beats, result, meta, path, unit, show_reference: bool, label_all: bool) -> bool:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import Patch
        from matplotlib.lines import Line2D
    except ImportError:
        return False

    setup_fonts(plt)
    curve, m = result["curve"], result["metrics"]
    t0, t1 = curve[0][0], curve[-1][0]
    fig, ax = plt.subplots(figsize=(11, 5.2), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    # Diagnostic washes (status colors, always named in the legend).
    ax.axvspan(t0, result["hook_end"], color=STATUS["good"], alpha=0.08, lw=0)
    for f in result["findings"]:
        if f.start is None or f.end is None or f.end <= f.start:
            continue
        if f.code in ("FLAT_ZONE", "MONOTONY"):
            ax.axvspan(f.start, f.end, color=STATUS["warning"], alpha=0.16, lw=0)
        elif f.code in ("NO_RELIEF", "SUSTAINED_PEAK"):
            ax.axvspan(f.start, f.end, color=STATUS["critical"], alpha=0.10, lw=0)

    if show_reference:
        scale = max(b.intensity for b in beats)
        ax.plot([t0 + x * (t1 - t0) for x, _ in REFERENCE_SHAPE],
                [y * scale for _, y in REFERENCE_SHAPE],
                color=MUTED, lw=1.5, ls=(0, (4, 3)), zorder=2)

    ax.plot([t for t, _ in curve], [v for _, v in curve], color=INK_2, lw=2,
            solid_capstyle="round", solid_joinstyle="round", zorder=3)

    types = []
    for b in beats:
        key = b.type or "beat"
        if key not in types:
            types.append(key)
    if len(types) > len(SERIES):  # fold extra types into "other" instead of cycling hues
        keep = types[:len(SERIES) - 1]
        types = keep + ["other"]
    style = {t: (SERIES[i], MARKERS[i]) for i, t in enumerate(types)}
    for t in types:
        pts = [b for b in beats if (b.type or "beat") == t or (t == "other" and (b.type or "beat") not in style)]
        if not pts:
            continue
        color, marker = style[t]
        ax.scatter([b.time for b in pts], [b.intensity for b in pts], s=64, c=color, marker=marker,
                   edgecolors=SURFACE, linewidths=2, zorder=4)

    climax = beats[result["climax_idx"]]
    ax.scatter([climax.time], [climax.intensity], s=260, facecolors="none",
               edgecolors=INK, linewidths=1.5, zorder=5)
    label_idx = set(range(len(beats))) if label_all else set(result["peaks"]) | {0, result["climax_idx"]}
    for k in sorted(label_idx):
        b = beats[k]
        if not b.label:
            continue
        pos = (b.time - t0) / (t1 - t0)
        ha = "left" if pos < 0.06 else "right" if pos > 0.94 else "center"
        ax.annotate(b.label, (b.time, b.intensity), xytext=(0, 10), textcoords="offset points",
                    ha=ha, va="bottom", fontsize=8, color=INK_2, zorder=6)

    ax.set_xlim(t0 - 0.01 * (t1 - t0), t1 + 0.01 * (t1 - t0))
    ax.set_ylim(0, 11.2)
    ax.set_yticks(range(0, 11, 2))
    ax.set_xlabel(f"Time ({unit})", color=INK_2)
    ax.set_ylabel("Intensity / interest (0-10)", color=INK_2)
    ax.grid(axis="y", color=GRID, lw=1)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(BASELINE)
    ax.tick_params(colors=MUTED, length=0)
    title = meta.get("title") or "Interest curve"
    ax.set_title(title, loc="left", color=INK, fontsize=13, fontweight="semibold", pad=26)
    ax.text(0, 1.03, f"Pacing health {m['pacing_score']}/100 · climax at {m['climax_position']:.0%} · "
            f"{len(result['findings'])} finding(s)", transform=ax.transAxes, color=INK_2, fontsize=9)

    handles = [Line2D([], [], marker=style[t][1], color=style[t][0], ls="", markersize=8,
                      markeredgecolor=SURFACE, label=t) for t in types]
    handles += [Patch(color=STATUS["good"], alpha=0.25, label="hook window"),
                Patch(color=STATUS["warning"], alpha=0.35, label="flat / monotony"),
                Patch(color=STATUS["critical"], alpha=0.25, label="no relief / sustained peak"),
                Line2D([], [], marker="o", color=INK, ls="", markersize=11, markerfacecolor="none",
                       label="climax")]
    if show_reference:
        handles.append(Line2D([], [], color=MUTED, lw=1.5, ls=(0, (4, 3)), label="reference shape"))
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.01, 1.0), frameon=False,
              fontsize=8.5, labelcolor=INK_2)
    fig.tight_layout()
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("beats", help="CSV or JSON beat list")
    ap.add_argument("--out", help="output directory (default: next to the input file)")
    ap.add_argument("--title", help="chart/report title")
    ap.add_argument("--unit", default=None, help="time unit label, e.g. min, s, sessions (default: min)")
    ap.add_argument("--format", default="png", choices=["png", "svg"], help="chart format")
    ap.add_argument("--reference", action="store_true", help="overlay a reference interest-curve shape")
    ap.add_argument("--label-all", action="store_true", help="label every beat, not just peaks")
    ap.add_argument("--no-plot", action="store_true", help="skip the chart even if matplotlib exists")
    g = ap.add_argument_group("thresholds")
    g.add_argument("--hook-window", type=float, default=0.10, help="fraction of duration for the hook")
    g.add_argument("--hook-min", type=float, default=6.0, help="minimum intensity of a hook")
    g.add_argument("--flat-tolerance", type=float, default=1.0, help="max range inside a flat zone")
    g.add_argument("--flat-min", type=float, default=0.12, help="min flat-zone length (fraction)")
    g.add_argument("--peak-min", type=float, default=7.0, help="minimum intensity of a peak")
    g.add_argument("--relief-window", type=float, default=0.12, help="window after a peak (fraction)")
    g.add_argument("--relief-drop", type=float, default=2.5, help="required drop after a peak")
    g.add_argument("--climax-min", type=float, default=0.70, help="earliest acceptable climax (fraction)")
    g.add_argument("--high", type=float, default=8.0, help="high-intensity threshold")
    g.add_argument("--low", type=float, default=3.0, help="low-intensity threshold")
    g.add_argument("--high-share", type=float, default=0.35, help="max share of time at high")
    g.add_argument("--low-share", type=float, default=0.40, help="max share of time at low")
    g.add_argument("--sustain-max", type=float, default=0.15, help="max continuous high stretch (fraction)")
    g.add_argument("--max-run", type=int, default=4, help="max consecutive beats of one type")
    g.add_argument("--sparse-gap", type=float, default=0.15, help="flag gaps longer than this fraction")
    g.add_argument("--curiosity-gap", type=float, default=0.30, help="max stretch with nothing new (fraction)")
    args = ap.parse_args(argv)

    try:
        beats, meta = load_beats(args.beats)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.title:
        meta["title"] = args.title
    meta.setdefault("title", os.path.splitext(os.path.basename(args.beats))[0])
    unit = args.unit or meta.get("unit") or "min"
    out_dir = args.out or os.path.dirname(os.path.abspath(args.beats))
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(args.beats))[0]

    result = analyse(beats, args)
    chart_path = None
    if not args.no_plot:
        candidate = os.path.join(out_dir, f"{stem}_curve.{args.format}")
        if plot(beats, result, meta, candidate, unit, args.reference, args.label_all):
            chart_path = candidate
        else:
            print("note: matplotlib not installed; wrote text/CSV outputs only "
                  "(pip install matplotlib for charts)", file=sys.stderr)
    md, js, cs = write_reports(beats, result, meta, out_dir, stem, unit, chart_path)

    m = result["metrics"]
    print(f"Pacing health {m['pacing_score']}/100 | climax {m['climax_intensity']:g} at "
          f"{m['climax_position']:.0%} | {len(result['findings'])} finding(s)")
    for f in result["findings"]:
        print(f"  [{f.severity.upper():6}] {f.code}: {f.message}")
    print(ascii_chart(result["curve"], beats))
    for p in filter(None, [chart_path, md, js, cs]):
        print(f"wrote {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
