#!/usr/bin/env python3
"""Build hue-shifted colour ramps and check pixel-art palettes.

  python3 palette_ramp.py ramp --base "#3f8f5a" [--steps 5] [--shift 12] [--light-hue 95] [--shadow-hue 285]
                          [--png ramp.png] [--gpl ramp.gpl] [--hex ramp.hex]
  python3 palette_ramp.py check PALETTE [--ramps "#a #b #c | #d #e"] [--png sheet.png] [--json]
  python3 palette_ramp.py selftest

`ramp` works in OKLCh (Ottosson 2020), where equal lightness steps look equal: lightness is spaced
evenly from dark to light around the base colour, highlights turn toward a warm light hue and
shadows toward a cool shadow hue (at most --shift degrees per step), and chroma falls off toward
the ends so highlights never burn. `check` reports value range, near-duplicates, eye-burning
colours, gaps in the value scale and, per ramp (given or guessed), step evenness, hue shift and
where saturation peaks. PALETTE is '#hex,#hex', a .hex/.txt/.gpl file or a palette PNG.
See references/pixel-art-craft.md ("Colour"). Python 3 standard library only.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixelkit import (dist, from_oklch, hexcol, hsv, hue_delta, load_palette, oklch, pack, parse_hex,  # noqa: E402
                      write_png)

LIGHT_HUE, SHADOW_HUE = 95.0, 285.0   # OKLCh hues: warm yellow light, blue-violet shade


def toward(h, target, amount):
    d = hue_delta(h, target)
    return (h + max(-amount, min(amount, d))) % 360


def make_ramp(base, steps=5, shift=12.0, light_hue=LIGHT_HUE, shadow_hue=SHADOW_HUE, lmin=0.24, lmax=0.93):
    """Return the ramp dark -> light as packed colours, with the base colour kept as one step."""
    L0, C0, h0 = oklch(base)
    L0 = min(max(L0, lmin + 0.02), lmax - 0.02)
    dark = int(round((steps - 1) * (L0 - lmin) / (lmax - lmin)))
    dark = min(max(dark, 1 if steps > 2 else 0), steps - 2 if steps > 2 else steps - 1)
    light = steps - 1 - dark
    out = []
    for k in range(dark, 0, -1):            # shadows: cooler, a little less chroma, never muddy
        t = k / dark
        out.append(from_oklch(L0 - (L0 - lmin) * t, C0 * (1 - 0.35 * t ** 1.5), toward(h0, shadow_hue, shift * k)))
    out.append(base)
    for k in range(1, light + 1):            # lights: warmer and clearly less saturated
        t = k / light
        out.append(from_oklch(L0 + (lmax - L0) * t, C0 * (1 - 0.6 * t ** 1.3), toward(h0, light_hue, shift * k)))
    return out


def ramp_stats(ramp):
    lch = [oklch(c) for c in ramp]
    dl = [b[0] - a[0] for a, b in zip(lch, lch[1:])]
    dh = [hue_delta(a[2], b[2]) for a, b in zip(lch, lch[1:]) if a[1] > 0.03 and b[1] > 0.03]
    peak = max(range(len(lch)), key=lambda i: lch[i][1])
    flags = []
    if any(d <= 0 for d in dl):
        flags.append(("NOT_MONOTONIC", "lightness does not rise at every step"))
    pos = [d for d in dl if d > 0]
    if len(pos) >= 2 and max(pos) / min(pos) > 2.5:
        flags.append(("UNEVEN_STEPS", f"value steps range {min(pos):.2f}-{max(pos):.2f}: some neighbours blur together, others jump"))
    if len(ramp) >= 3 and dh and abs(sum(dh)) < 4 and sum(abs(x) for x in dh) < 6:
        flags.append(("STRAIGHT_RAMP", "no hue shift: only lightness changes (reads flat and harmonises poorly)"))
    if len(ramp) >= 3 and peak == len(ramp) - 1 and lch[-1][0] > 0.75:
        flags.append(("BRIGHT_END_SATURATED", "the lightest colour is the most saturated: highlights will burn"))
    return {"colors": [hexcol(c) for c in ramp], "L": [round(x[0], 3) for x in lch], "C": [round(x[1], 3) for x in lch],
            "h": [round(x[2], 1) for x in lch], "value_steps": [round(d, 3) for d in dl],
            "hue_shift_total": round(sum(dh), 1), "chroma_peak_index": peak, "flags": flags}


def guess_ramps(pal):
    """Chain colours from light to dark when hue, chroma and value fit a ramp. A heuristic; pass --ramps to be exact."""
    cols = sorted(pal, key=lambda c: -oklch(c)[0])
    chains = []
    for c in cols:
        L, C, h = oklch(c)
        best, cost = None, 9.0
        for ch in chains:
            Lt, Ct, ht = oklch(ch[-1])
            dL = Lt - L
            if not 0.04 <= dL <= 0.32:
                continue
            if (C < 0.03) != (Ct < 0.03) or abs(C - Ct) > 0.12:
                continue   # greys chain with greys, colours with colours of similar strength
            dh = 0 if C < 0.03 else abs(hue_delta(ht, h))
            if dh > 55:
                continue
            k = dh / 55 + abs(C - Ct) / 0.12 + abs(dL - 0.13) / 0.13
            if k < cost:
                best, cost = ch, k
        if best is not None:
            best.append(c)
        else:
            chains.append([c])
    return [list(reversed(ch)) for ch in chains if len(ch) >= 3]


def check(pal, ramps=None):
    lch = {c: oklch(c) for c in pal}
    Ls = sorted(v[0] for v in lch.values())
    gaps = sorted(((b - a), a, b) for a, b in zip(Ls, Ls[1:]))
    pairs = sorted((dist(a, b), a, b) for i, a in enumerate(pal) for b in pal[i + 1:] if dist(a, b) < 0.03)
    burn = [c for c in pal if hsv(c)[0] >= 0.9 and hsv(c)[1] >= 0.9]
    greys = [c for c in pal if lch[c][1] < 0.03]
    guessed = ramps is None
    ramps = ramps if ramps is not None else guess_ramps(pal)
    rep = {"count": len(pal), "value_range": [round(Ls[0], 3), round(Ls[-1], 3)],
           "largest_value_gap": [round(gaps[-1][0], 3), round(gaps[-1][1], 3), round(gaps[-1][2], 3)] if gaps else None,
           "near_duplicates": [[hexcol(a), hexcol(b), round(d, 3)] for d, a, b in pairs],
           "eyeburn": [hexcol(c) for c in burn], "greys": [hexcol(c) for c in greys],
           "ramps_guessed": guessed, "ramps": [ramp_stats(r) for r in ramps]}
    flags = []
    if Ls[-1] - Ls[0] < 0.6:
        flags.append(("NARROW_VALUES", f"lightness only spans {Ls[0]:.2f}-{Ls[-1]:.2f}: add a deeper dark or a brighter light"))
    if gaps and gaps[-1][0] > 0.22:
        flags.append(("VALUE_GAP", f"no colours between lightness {gaps[-1][1]:.2f} and {gaps[-1][2]:.2f}"))
    if pairs:
        flags.append(("NEAR_DUPLICATES", f"{len(pairs)} pairs closer than 0.03 OKLab: merge them or give each its own job"))
    if burn:
        flags.append(("EYEBURN", f"{len(burn)} colours near full saturation and brightness: {', '.join(hexcol(c) for c in burn[:4])}"))
    rep["flags"] = flags
    return rep


def swatches(rows, path, cell=16):
    rows = [r for r in rows if r]
    w = max(len(r) for r in rows) * cell
    h = len(rows) * cell
    px = [0] * (w * h)
    for j, row in enumerate(rows):
        for i, c in enumerate(row):
            for y in range(j * cell, (j + 1) * cell):
                for x in range(i * cell, (i + 1) * cell):
                    px[y * w + x] = c | 0xFF000000
    write_png(path, w, h, px)


def write_gpl(path, cols, name):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"GIMP Palette\nName: {name}\nColumns: {len(cols)}\n#\n")
        for c in cols:
            r, g, b = (c & 255, (c >> 8) & 255, (c >> 16) & 255)
            f.write(f"{r:3d} {g:3d} {b:3d}\t{hexcol(c)}\n")


def print_check(rep):
    print(f"# Palette check: {rep['count']} colours, lightness {rep['value_range'][0]:.2f}-{rep['value_range'][1]:.2f}\n")
    if rep["largest_value_gap"]:
        g = rep["largest_value_gap"]
        print(f"- Largest value gap: {g[0]:.2f} (between L {g[1]:.2f} and {g[2]:.2f})")
    print(f"- Greys/neutrals: {len(rep['greys'])}; eye-burning colours: {len(rep['eyeburn'])}; near-duplicate pairs: {len(rep['near_duplicates'])}")
    print(f"\n## Ramps ({'guessed: pass --ramps to be exact' if rep['ramps_guessed'] else 'as given'})\n")
    for r in rep["ramps"]:
        print(f"- {' '.join(r['colors'])}")
        print(f"  value steps {', '.join(f'{d:.2f}' for d in r['value_steps'])}; hue shift {r['hue_shift_total']:+.0f} deg dark->light; "
              f"chroma peaks at step {r['chroma_peak_index'] + 1}/{len(r['colors'])}")
        for code, msg in r["flags"]:
            print(f"  [WARN] {code}: {msg}")
    print()
    for code, msg in rep["flags"]:
        print(f"[WARN] {code}: {msg}")
    if not rep["flags"] and not any(r["flags"] for r in rep["ramps"]):
        print("No flags.")


def selftest():
    res = []

    def ok(name, cond, info=""):
        res.append((name, bool(cond), info))

    for base in ("#3f8f5a", "#b13e53", "#3b5dc9", "#c9a27a"):
        r = make_ramp(parse_hex(base), 5)
        st = ramp_stats(r)
        ok(f"ramp from {base}: 5 colours, base kept", len(r) == 5 and parse_hex(base) in r, st["colors"])
        ok(f"ramp from {base}: lightness rises evenly", not any(c in ("NOT_MONOTONIC", "UNEVEN_STEPS") for c, _ in st["flags"]), st["value_steps"])
        Lh = [oklch(c) for c in r]
        ok(f"ramp from {base}: highlight hue moves toward the light hue",
           abs(hue_delta(Lh[-1][2], LIGHT_HUE)) < abs(hue_delta(oklch(parse_hex(base))[2], LIGHT_HUE)) + 0.5, [round(x[2]) for x in Lh])
        ok(f"ramp from {base}: no eye-burning highlight", not any(hsv(c)[0] >= 0.9 and hsv(c)[1] >= 0.9 for c in r[-2:]))
    straight = [pack(0, int(v * 0.6), 0) for v in (60, 110, 160, 210, 255)]
    st = ramp_stats(straight)
    ok("a pure value ramp of one hue is flagged STRAIGHT_RAMP", any(c == "STRAIGHT_RAMP" for c, _ in st["flags"]), st["h"])
    rep = check([parse_hex(x) for x in ("#000000", "#00ff00", "#101010", "#121212", "#ffffff")])
    codes = [c for c, _ in rep["flags"]]
    ok("check flags eyeburn and near-duplicates", "EYEBURN" in codes and "NEAR_DUPLICATES" in codes, codes)
    sweetie = load_palette("#1a1c2c,#5d275d,#b13e53,#ef7d57,#ffcd75,#a7f070,#38b764,#257179,#29366f,#3b5dc9,#41a6f6,#73eff7,#f4f4f4,#94b0c2,#566c86,#333c57")
    rep = check(sweetie)
    ok("Sweetie 16: ramps are found and the palette has a wide value range", len(rep["ramps"]) >= 3 and rep["value_range"][1] - rep["value_range"][0] > 0.7,
       [r["colors"] for r in rep["ramps"]])
    import tempfile
    d = tempfile.mkdtemp()
    write_gpl(os.path.join(d, "s.gpl"), sweetie, "sweetie")
    ok("GIMP .gpl export loads back", load_palette(os.path.join(d, "s.gpl")) == sweetie)
    swatches([sweetie], os.path.join(d, "s.png"))
    ok("palette PNG loads back", sorted(load_palette(os.path.join(d, "s.png"))) == sorted(c | 0xFF000000 for c in sweetie))
    for name, passed, info in res:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}" + (f"  ({info})" if info != "" and not passed else ""))
    fails = sum(1 for r in res if not r[1])
    print(f"\n{len(res) - fails}/{len(res)} checks passed")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("ramp", help="build a hue-shifted ramp around a base colour")
    r.add_argument("--base", required=True, help="the mid colour, e.g. '#3f8f5a'")
    r.add_argument("--steps", type=int, default=5)
    r.add_argument("--shift", type=float, default=12.0, help="max hue shift per step in degrees (practitioners stay at or under about 20)")
    r.add_argument("--light-hue", type=float, default=LIGHT_HUE, help="OKLCh hue highlights turn toward (95 = warm yellow)")
    r.add_argument("--shadow-hue", type=float, default=SHADOW_HUE, help="OKLCh hue shadows turn toward (285 = blue-violet)")
    r.add_argument("--lmin", type=float, default=0.24)
    r.add_argument("--lmax", type=float, default=0.93)
    r.add_argument("--png")
    r.add_argument("--gpl")
    r.add_argument("--hex")
    r.add_argument("--json", action="store_true")
    c = sub.add_parser("check", help="check a palette and its ramps")
    c.add_argument("palette")
    c.add_argument("--ramps", help="ramps dark->light, colours separated by spaces, ramps by '|'")
    c.add_argument("--png", help="write a swatch sheet (one row per ramp)")
    c.add_argument("--json", action="store_true")
    sub.add_parser("selftest")
    args = ap.parse_args()
    if args.cmd == "selftest":
        return selftest()
    if args.cmd == "ramp":
        if not 2 <= args.steps <= 12:
            ap.error("--steps must be 2-12")
        ramp = make_ramp(parse_hex(args.base), args.steps, min(args.shift, 30.0), args.light_hue, args.shadow_hue, args.lmin, args.lmax)
        st = ramp_stats(ramp)
        if args.png:
            swatches([ramp], args.png)
        if args.gpl:
            write_gpl(args.gpl, ramp, f"ramp {args.base}")
        if args.hex:
            with open(args.hex, "w") as f:
                f.write("\n".join(hexcol(x).lstrip("#") for x in ramp) + "\n")
        if args.json:
            print(json.dumps(st, indent=1))
            return 0
        print(" ".join(st["colors"]))
        print("L  " + " ".join(f"{x:.2f}" for x in st["L"]))
        print("C  " + " ".join(f"{x:.3f}" for x in st["C"]))
        print("h  " + " ".join(f"{x:.0f}" for x in st["h"]))
        for code, msg in st["flags"]:
            print(f"[WARN] {code}: {msg}")
        return 0
    pal = load_palette(args.palette)
    ramps = None
    if args.ramps:
        ramps = [[parse_hex(x) for x in part.split()] for part in args.ramps.split("|") if part.strip()]
    rep = check(pal, ramps)
    if args.png:
        used = {c for r in (ramps or guess_ramps(pal)) for c in r}
        swatches((ramps or guess_ramps(pal)) + [[c for c in pal if c not in used]], args.png)
    if args.json:
        print(json.dumps(rep, indent=1))
    else:
        print_check(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
