#!/usr/bin/env python3
"""Audit pixel art for the defects players notice, and repair AI-generated "pixel art".

  python3 pixel_audit.py audit sprite.png [--palette pal.hex] [--max-colors 32] [--bg "#1a1c2c"] [--json]
  python3 pixel_audit.py fix fake.png -o clean.png [--palette pal.hex | --colors 16] [--scale 8]
                         [--upscale 4] [--transparent-bg] [--keep-orphans]
  python3 pixel_audit.py selftest

`audit` reads art at native size, integer-scaled screenshots (it finds the scale), and upscaled
AI images (it follows a drifting grid). It reports the grid, colours, stray pixels, value range
and edges, then lists flags with fixes. `fix` samples one colour per detected cell, binarizes
alpha, maps colours to a palette (or merges near-duplicates), removes low-contrast stray pixels and
writes a clean PNG at native size. Flags are explained in references/pixel-art-craft.md
("Audit flags"). Python 3 standard library only; Pillow, if installed, speeds up reading and adds
JPEG/WebP input.
"""
import argparse
import json
import math
import os
import random
import sys
from array import array
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixelkit import (alpha, dist, hexcol, hsv, load_palette, nearest, oklab, pack, read_image,  # noqa: E402
                      unpack, write_png)

TOL = 64            # colour jumps smaller than this (sum of RGBA channel differences) are treated as noise
SIMILAR = 0.03      # OKLab distance under which two colours are hard to tell apart
MERGE = 0.05        # fix: colours closer than this are merged (AI noise; too close to carry separate jobs)
NOISE_DIST = 0.10   # a stray pixel this close to its surroundings reads as noise, not as an accent


# ---------- grid detection ----------
def _jump(u, v):
    return (abs((u & 255) - (v & 255)) + abs(((u >> 8) & 255) - ((v >> 8) & 255))
            + abs(((u >> 16) & 255) - ((v >> 16) & 255)) + abs(((u >> 24) & 255) - ((v >> 24) & 255)))


def _spread(n, k):
    return range(n) if n <= k else sorted({int(i * (n - 1) / (k - 1)) for i in range(k)})


def _runs(found, runs, radius=1):
    """Merge edges within `radius` px (a blurred border makes several), keeping the strongest, then count the gaps."""
    kept = []
    for pos, d in found:
        if kept and pos - kept[-1][0] <= radius:
            if d > kept[-1][1]:
                kept[-1] = (pos, d)
        else:
            kept.append((pos, d))
    for (p0, _), (p1, _) in zip(kept, kept[1:]):
        runs[p1 - p0] += 1


def edges(w, h, px, tol=TOL, lines=512):
    """Edge strength per column and per row, plus the edges found on each sampled line."""
    xp, yp, xf, yf = [0] * w, [0] * h, [], []
    for y in _spread(h, lines):
        row, found = px[y * w:(y + 1) * w], []
        for x in range(1, w):
            u, v = row[x - 1], row[x]
            if u != v:
                d = _jump(u, v)
                if d > tol:
                    xp[x] += d
                    found.append((x, d))
        xf.append(found)
    for x in _spread(w, lines):
        prev, found = px[x], []
        for y in range(1, h):
            v = px[y * w + x]
            if v != prev:
                d = _jump(prev, v)
                if d > tol:
                    yp[y] += d
                    found.append((y, d))
            prev = v
        yf.append(found)
    return xp, yp, xf, yf


def run_hist(found_lines, radius=1):
    runs = Counter()
    for found in found_lines:
        _runs(found, runs, radius)
    return runs


def comb_period(runs, n, pmin=2.0):
    """Pixel period from run lengths: gaps between edges are whole multiples of the art-pixel size.

    hits(p) is the share of runs within max(0.5, 0.12p) px of a multiple of p; a run shorter than
    half of p cannot sit between two cell borders and counts as a miss. Divisors of the true period
    hit as often, so the largest period near the best share wins; mean cos(2*pi*run/p) breaks ties."""
    maxp = max(2.0, min(128.0, n / 3))
    items = [(r, c) for r, c in runs.items() if r <= 4 * maxp]
    tot = sum(c for _, c in items)
    if tot < 8 or maxp <= pmin:
        return None, 0.0
    cos, tau = math.cos, 2 * math.pi

    def hits(p):
        tol = max(0.5, 0.12 * p)
        return sum(c for r, c in items if r >= 0.5 * p and abs(r - p * round(r / p)) <= tol) / tot

    def fine(p):
        return sum(c * (cos(tau * r / p) if r >= 0.5 * p else -1.0) for r, c in items) / tot

    grid = [round(pmin + 0.05 * i, 2) for i in range(int((maxp - pmin) / 0.05) + 1)]   # below 2 px every run fits
    scores = [(p, hits(p)) for p in grid]
    best = max(s for _, s in scores)
    if best < 0.45:
        return None, best
    p0 = max(p for p, s in scores if s >= 0.9 * best)
    win = [p for p, s in scores if p0 * 0.85 <= p <= p0 * 1.1 and s >= 0.9 * best]
    p = max(win, key=lambda q: (fine(q), -abs(q - round(q))))
    for q in [round(p + d / 200, 3) for d in range(-10, 11)]:   # refine to 0.005 px
        if fine(q) > fine(p) + 1e-9:
            p = q
    if abs(p - round(p)) < 0.03 and fine(round(p)) >= fine(p) - 0.02:
        p = float(round(p))
    return p, hits(p)


def best_phase(prof, p):
    n, step = len(prof), (1.0 if p == int(p) else 0.25)
    best, ph = (-1, 0.0), 0.0
    while ph < p:
        s, last, pos = 0, -1, ph
        while pos < n - 0.5:
            i = int(round(pos))
            if i != last and 0 < i < n:
                s += prof[i]
                last = i
            pos += p
        if s > best[0]:
            best = (s, ph)
        ph += step
    return best[1]


def walk(prof, n, p, phase):
    """Boundaries that follow the grid even when it drifts.

    Starts at the strongest edge near the rigid grid (the most reliable line), then steps by p in
    both directions, snapping each predicted line to the strongest edge within about a third of a
    cell. Flat stretches keep the predicted spacing."""
    r = max(1, int(round(p * 0.35)))
    cands = [i for i in range(1, n) if prof[i] > 0 and abs(((i - phase + p / 2) % p) - p / 2) <= r]
    anchor = max(cands, key=lambda i: prof[i]) if cands else int(round(phase)) or int(round(p))

    def step(start, sign):
        out, pos = [], start
        while True:
            pos += sign * p
            c = int(round(pos))
            if not (0 < c < n):
                return out
            lo, hi = max(1, c - r), min(n - 1, c + r)
            b = max(range(lo, hi + 1), key=lambda i: prof[i])
            if prof[b] <= 0:
                b = c
            if out and sign * (b - out[-1]) <= 0 or sign * (b - start) <= 0:
                b = c
            out.append(b)
            pos = b

    inner = sorted(set(step(anchor, -1) + [anchor] + step(anchor, 1)))
    out = [0] + [b for b in inner if 0 < b < n] + [n]
    if len(out) > 2 and out[1] - out[0] < p / 2:      # drop slivers: letterbox or cropped partial cells
        out.pop(1)
    if len(out) > 2 and out[-1] - out[-2] < p / 2:
        out.pop(-2)
    return out


def rigid(n, p, phase):
    """Evenly spaced boundaries (constant resampling factor), slivers at the ends dropped."""
    out, k = [0], 0
    while True:
        b = int(round(phase + k * p))
        k += 1
        if b >= n:
            break
        if b > out[-1]:
            out.append(b)
    out.append(n)
    if len(out) > 2 and out[1] - out[0] < p / 2:
        out.pop(1)
    if len(out) > 2 and out[-1] - out[-2] < p / 2:
        out.pop(-2)
    return out


def _grid(xp, yp, sx, sy, follow=True):
    line = walk if follow else rigid
    xb = line(xp, len(xp), sx, best_phase(xp, sx)) if follow else rigid(len(xp), sx, best_phase(xp, sx))
    yb = line(yp, len(yp), sy, best_phase(yp, sy)) if follow else rigid(len(yp), sy, best_phase(yp, sy))
    tot = (sum(xp) + sum(yp)) or 1
    near = (lambda prof, b: prof[b]) if follow else (lambda prof, b: max(prof[max(1, b - 1):b + 2]))
    return xb, yb, (sum(near(xp, b) for b in xb[1:-1]) + sum(near(yp, b) for b in yb[1:-1])) / tot


def _tune(prof, p):
    """Fine-tune a resampling factor: the rigid grid that catches the most edge energy within +-3%."""
    best = (-1.0, p, 0.0)
    for k in range(-30, 31):
        q = p * (1 + k / 1000)
        ph = best_phase(prof, q)
        s = sum(max(prof[max(1, b - 1):b + 2]) for b in rigid(len(prof), q, ph)[1:-1])
        if s > best[0]:
            best = (s, q, ph)
    return best[1]


def detect_grid(w, h, px, scale=None, tol=TOL, size=None):
    """Find the art-pixel grid. Pass 1 looks for crisp cells; pass 2 tolerates smooth scaling.

    scale forces the screen-pixels-per-art-pixel factor; size=(W, H) gives the art size directly
    (the most reliable option for heavily blurred images)."""
    native = {"scale": 1.0, "xb": list(range(w + 1)), "yb": list(range(h + 1)), "share": 1.0, "comb": 0.0, "blurred": False}
    xp, yp, xf, yf = edges(w, h, px, tol)
    blurred = False
    if size:
        sx, sy = w / size[0], h / size[1]
        xb = [int(round(i * sx)) for i in range(size[0] + 1)]
        yb = [int(round(j * sy)) for j in range(size[1] + 1)]
        return {"scale": round((sx + sy) / 2, 3), "sx": sx, "sy": sy, "xb": xb, "yb": yb, "share": 1.0, "comb": 1.0, "blurred": False}
    if scale:
        sx = sy = float(scale)
        cx = cy = 1.0
        xb, yb, share = _grid(xp, yp, sx, sy, follow=False)
    else:
        sx, cx = comb_period(run_hist(xf), w)
        sy, cy = comb_period(run_hist(yf), h)
        ok = bool(sx and sy)
        if ok:
            xb, yb, share = _grid(xp, yp, sx, sy)
            ok = share >= 0.9 or (min(sx, sy) >= 3 and share >= 0.35)
        if not ok and len(set(px[::max(1, len(px) // 200000)])) <= 256:
            return native   # few colours: crisp native art, not a smooth upscale
        if not ok:
            # pass 2: smooth scaling (thousands of in-between colours) spreads each border over a few
            # pixels; merge edges within a radius smaller than half a cell, look again, and lay a rigid
            # grid (a constant resampling factor)
            best = None
            for t2 in (24, 40, 64):   # JPEG noise and soft borders call for different thresholds
                xp2, yp2, xf2, yf2 = edges(w, h, px, t2)
                for radius in (2, 3, 4):
                    pmin = 2 * radius + 0.5   # merging must stay under half a cell
                    bx, hx = comb_period(run_hist(xf2, radius), w, pmin)
                    by, hy = comb_period(run_hist(yf2, radius), h, pmin)
                    if bx and by and (best is None or min(hx, hy) > best[0]):
                        best = (min(hx, hy), bx, by, xp2, yp2)
            if best is None:
                return native
            _, sx, sy, xp2, yp2 = best
            sx, sy = _tune(xp2, sx), _tune(yp2, sy)
            cx = cy = best[0]
            xp, yp, blurred = xp2, yp2, True
            xb, yb, share = _grid(xp, yp, sx, sy, follow=False)
            if share < 0.25:
                return native
    s = round((sx + sy) / 2, 2) if abs(sx - sy) <= 0.25 else round(max(sx, sy), 2)
    return {"scale": s, "sx": sx, "sy": sy, "xb": xb, "yb": yb, "share": round(share, 3),
            "comb": round(min(cx, cy), 3), "blurred": blurred}


# ---------- sampling ----------
def sample(w, h, px, xb, yb):
    """One colour per cell: the dominant 5-bit bucket of the cell's inner area, averaged.

    Returns (aw, ah, art, cell_noise, mixed) where cell_noise is the share of inner pixels that
    disagree with their cell (smooth scaling, JPEG, AI noise) and mixed lists the (i, j) cells whose
    full area holds more than one exact colour (mixels on an otherwise clean image)."""
    out, off, tot, mixed = array("I"), 0, 0, []
    for j in range(len(yb) - 1):
        y0, y1 = yb[j], yb[j + 1]
        my = (y1 - y0) // 5 if y1 - y0 >= 4 else 0
        for i in range(len(xb) - 1):
            x0, x1 = xb[i], xb[i + 1]
            mx = (x1 - x0) // 5 if x1 - x0 >= 4 else 0
            cnt = Counter()
            for y in range(y0 + my, y1 - my):
                cnt.update(px[y * w + x0 + mx:y * w + x1 - mx])
            buckets = {}
            for v, c in cnt.items():
                buckets.setdefault(v & 0xF8F8F8F8, []).append((v, c))
            win = max(buckets.values(), key=lambda b: sum(c for _, c in b))
            n = sum(c for _, c in win)
            if len(win) == 1:
                out.append(win[0][0])
            else:
                acc = [0, 0, 0, 0]
                for v, c in win:
                    for ch, val in enumerate(unpack(v)):
                        acc[ch] += val * c
                out.append(pack(*(int(round(a / n)) for a in acc)))
            cells = sum(cnt.values())
            off += cells - n
            tot += cells
            first = px[y0 * w + x0]
            if len(cnt) > 1 or any(v != first for y in (y0, y1 - 1) for v in px[y * w + x0:y * w + x1]) \
                    or any(px[y * w + x] != first for y in range(y0, y1) for x in (x0, x1 - 1)):
                mixed.append((i, j))
    return len(xb) - 1, len(yb) - 1, out, (off / tot if tot else 0.0), mixed


# ---------- analysis ----------
def _neighbours(aw, ah, x, y):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (dx or dy) and 0 <= x + dx < aw and 0 <= y + dy < ah:
                yield x + dx, y + dy


def orphans(aw, ah, art):
    """Opaque pixels with no 8-neighbour of the same colour. Returns (noise, accents) lists of (x, y, colour, neighbour colour)."""
    noise, accent = [], []
    for y in range(ah):
        for x in range(aw):
            v = art[y * aw + x]
            if alpha(v) < 128:
                continue
            nb = [art[ny * aw + nx] for nx, ny in _neighbours(aw, ah, x, y)]
            if any(u == v for u in nb):
                continue
            opaque = [u for u in nb if alpha(u) >= 128]
            if not opaque:
                continue
            maj = Counter(opaque).most_common(1)[0][0]
            (noise if dist(v, maj) < NOISE_DIST else accent).append((x, y, v, maj))
    return noise, accent


def similar_pairs(colors):
    cols = list(colors)
    if len(cols) > 256:
        return None
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            d = dist(cols[i], cols[j])
            if d < SIMILAR:
                pairs.append((d, cols[i], cols[j]))
    return sorted(pairs)


def mixel_region(aw, ah, mixed):
    """Where mixed cells cluster: the 4x4 region (in art pixels) with the highest share of them."""
    if not mixed:
        return None
    reg = Counter((4 * i // aw, 4 * j // ah) for i, j in mixed)
    k, n = reg.most_common(1)[0]
    cells = max(1, (aw // 4) * (ah // 4))
    return {"x": [k[0] * aw // 4, (k[0] + 1) * aw // 4], "y": [k[1] * ah // 4, (k[1] + 1) * ah // 4],
            "share": round(min(1.0, n / cells), 2)}


def analyse(path, palette=None, max_colors=32, bg=None, scale=None, size=None):
    w, h, px = read_image(path)
    g = detect_grid(w, h, px, scale, size=size)
    if g["scale"] > 1:
        aw, ah, art, cell_noise, mixed = sample(w, h, px, g["xb"], g["yb"])
    else:
        aw, ah, art, cell_noise, mixed = w, h, px, 0.0, []
    widths = Counter(g["xb"][i + 1] - g["xb"][i] for i in range(len(g["xb"]) - 1))
    heights = Counter(g["yb"][i + 1] - g["yb"][i] for i in range(len(g["yb"]) - 1))
    off, worst = len(mixed) / max(1, aw * ah), mixel_region(aw, ah, mixed)
    soft = sum(1 for v in art if 0 < alpha(v) < 255)
    opaque = [v | 0xFF000000 for v in art if alpha(v) >= 128]
    counts = Counter(opaque)
    n_op = max(1, len(opaque))
    noise, accent = orphans(aw, ah, art)
    Ls = sorted(oklab(v)[0] for v in opaque) or [0.0]
    lo, hi = Ls[int(0.05 * (len(Ls) - 1))], Ls[int(0.95 * (len(Ls) - 1))]
    burn = sum(c for v, c in counts.items() if hsv(v)[0] >= 0.9 and hsv(v)[1] >= 0.9)
    pairs = similar_pairs(counts)
    rep = {"file": path, "image": [w, h], "scale": g["scale"], "art": [aw, ah], "grid_on_share": g["share"],
           "cell_widths": dict(sorted(widths.items())), "cell_heights": dict(sorted(heights.items())),
           "cell_noise": round(cell_noise, 3), "mixed_cells": round(off, 3), "mixed_region": worst,
           "colors": len(counts), "top_colors": [[hexcol(v), c] for v, c in counts.most_common(12)],
           "soft_alpha_pixels": soft, "noise_pixels": len(noise), "accent_pixels": len(accent),
           "noise_examples": [[x, y, hexcol(v), hexcol(m)] for x, y, v, m in noise[:6]],
           "value_range": round(hi - lo, 3), "value_lo_hi": [round(lo, 3), round(hi, 3)],
           "eyeburn_share": round(burn / n_op, 3),
           "similar_pairs": None if pairs is None else [[hexcol(a), hexcol(b), round(d, 3)] for d, a, b in pairs[:8]]}
    flags = []

    def flag(code, sev, msg, fix):
        flags.append({"code": code, "severity": sev, "message": msg, "fix": fix})

    noisy = cell_noise > 0.08
    if g["scale"] > 1 and not noisy and (len(widths) > 1 or len(heights) > 1):
        spread = sorted(set(widths) | set(heights))
        flag("NON_INTEGER_SCALE", "fail", f"pixel cells are {spread} screen px wide: the art was scaled by a non-integer factor",
             "Scale by whole numbers only (nearest neighbour), or let the engine letterbox to the largest integer scale.")
    if g["scale"] > 1 and noisy:
        flag("AI_OR_RESAMPLED", "fail", f"cells are not flat ({cell_noise:.0%} of pixels disagree with their cell; widths {sorted(widths)}): "
             "smooth scaling, JPEG compression or AI generation", "Run `pixel_audit.py fix` to snap to the grid, then repaint the details by hand.")
    if g["scale"] > 1 and not noisy and off > 0.01:
        where = f" (mostly art x {worst['x']}, y {worst['y']})" if worst else ""
        flag("MIXELS", "fail", f"{off:.1%} of art pixels hold more than one screen colour{where}: pixels of another size, "
             "rotated or smooth-scaled parts, anti-aliased text, or sprites off the pixel grid",
             "Draw everything at one pixel size, never rotate or scale sprites by non-integers, and snap positions to whole art pixels.")
    if soft > 0.01 * n_op:
        flag("SOFT_ALPHA", "warn", f"{soft} semi-transparent pixels: outer anti-aliasing fringes on other backgrounds",
             "Make every pixel fully opaque or fully transparent; anti-alias only inside the sprite.")
    if palette:
        pset = {p & 0xFFFFFF for p in palette}
        offp = [v for v in counts if v & 0xFFFFFF not in pset]
        if offp:
            flag("OFF_PALETTE", "fail", f"{len(offp)} colours are not in the palette, e.g. {', '.join(hexcol(v) for v in offp[:5])}",
                 "Map them to the nearest palette colour (`fix --palette`), and check fonts and scaled images for anti-aliasing.")
        rep["off_palette"] = [hexcol(v) for v in offp[:20]]
    if len(counts) > max_colors:
        flag("TOO_MANY_COLORS", "fail" if len(counts) > 4 * max_colors else "warn",
             f"{len(counts)} colours (budget {max_colors})", "Reduce to ramps per material; merge near-duplicates (`fix --colors N`).")
    if pairs:
        flag("SIMILAR_COLORS", "warn", f"{len(pairs)} colour pairs are almost identical, e.g. {hexcol(pairs[0][1])} / {hexcol(pairs[0][2])}",
             "Give every colour its own job: merge the pair or push it apart in value.")
    if pairs is None:
        flag("SIMILAR_COLORS", "warn", "more than 256 colours: too many to check pairwise", "Quantize first (`fix`).")
    if len(noise) >= 3 and len(noise) > 0.015 * n_op:
        ex = ", ".join(f"({x},{y})" for x, y, _, _ in noise[:5])
        flag("NOISE_PIXELS", "warn", f"{len(noise)} stray single pixels that barely differ from their surroundings, e.g. at {ex}",
             "Join them to a cluster or remove them; single pixels should be deliberate (eyes, highlights, stars).")
    if hi - lo < 0.40:
        flag("LOW_VALUE_RANGE", "warn", f"values span only {hi - lo:.2f} of the lightness scale (5th-95th percentile)",
             "Spread darks and lights further; check the image in greyscale.")
    if burn / n_op > 0.15:
        flag("EYEBURN", "warn", f"{burn / n_op:.0%} of pixels use colours near full saturation and full brightness",
             "Pull saturation down as colours get brighter; keep the most saturated colours for small accents.")
    if bg is not None:
        edge_px = [art[y * aw + x] for y in range(ah) for x in range(aw) if alpha(art[y * aw + x]) >= 128
                   and any(alpha(art[ny * aw + nx]) < 128 for nx, ny in _neighbours(aw, ah, x, y) if nx == x or ny == y)]
        if edge_px:
            Lb = oklab(bg)[0]
            melt = sum(1 for v in edge_px if abs(oklab(v)[0] - Lb) < 0.12) / len(edge_px)
            rep["edge_melt_share"] = round(melt, 3)
            if melt > 0.35:
                flag("MELTS_INTO_BG", "warn", f"{melt:.0%} of the sprite's edge pixels are close in value to {hexcol(bg)}",
                     "Add a darker (or lighter) outline, or change the background value; check the silhouette.")
    rep["flags"] = flags
    rep["verdict"] = "FAIL" if any(f["severity"] == "fail" for f in flags) else ("WARN" if flags else "PASS")
    return rep, (aw, ah, art)


def print_report(rep):
    print(f"# Pixel audit: {os.path.basename(rep['file'])}  ->  {rep['verdict']}\n")
    w, h = rep["image"]
    aw, ah = rep["art"]
    if rep["scale"] > 1:
        print(f"- Grid: {w}x{h} image = {aw}x{ah} art pixels at scale {rep['scale']} "
              f"(cell widths {rep['cell_widths']}, heights {rep['cell_heights']})")
        print(f"- Grid fit: {rep['grid_on_share']:.0%} of edge energy on grid lines; cell noise {rep['cell_noise']:.1%}; "
              f"mixed cells {rep['mixed_cells']:.1%}")
    else:
        print(f"- Grid: native size {w}x{h} (no upscaling found)")
    print(f"- Colours: {rep['colors']} (top: {', '.join(f'{c} x{n}' for c, n in rep['top_colors'][:6])})")
    print(f"- Values: lightness {rep['value_lo_hi'][0]:.2f}-{rep['value_lo_hi'][1]:.2f} (range {rep['value_range']:.2f}); "
          f"eyeburn share {rep['eyeburn_share']:.0%}")
    print(f"- Single pixels: {rep['noise_pixels']} low-contrast (noise), {rep['accent_pixels']} high-contrast (accents: eyes, highlights, stars)")
    if rep.get("edge_melt_share") is not None:
        print(f"- Edge vs background: {rep['edge_melt_share']:.0%} of edge pixels close in value")
    print()
    if not rep["flags"]:
        print("No flags. Still review by eye: line flow (jaggies, doubles), banding, pillow shading, light direction.")
    for f in rep["flags"]:
        print(f"[{f['severity'].upper()}] {f['code']}: {f['message']}\n       fix: {f['fix']}")


# ---------- fix ----------
def median_cut(counts, n):
    boxes = [list(counts.items())]
    while len(boxes) < n:
        best, axis, spread = None, 0, 0.0
        for bi, box in enumerate(boxes):
            if len(box) < 2:
                continue
            labs = [oklab(v) for v, _ in box]
            for ax in range(3):
                vals = [l[ax] for l in labs]
                s = (max(vals) - min(vals)) * (1.0 if ax == 0 else 0.8)
                s *= sum(c for _, c in box) ** 0.5
                if s > spread:
                    best, axis, spread = bi, ax, s
        if best is None:
            break
        box = sorted(boxes.pop(best), key=lambda vc: oklab(vc[0])[axis])
        half, acc, cut = sum(c for _, c in box) / 2, 0, 1
        for i, (_, c) in enumerate(box):
            acc += c
            if acc >= half:
                cut = min(max(1, i + 1), len(box) - 1)
                break
        boxes += [box[:cut], box[cut:]]
    return [max(b, key=lambda vc: vc[1])[0] for b in boxes]


def merge_similar(counts, thr=SIMILAR):
    reps = []
    for v, _ in counts.most_common():
        if not any(dist(v, r) < thr for r in reps):
            reps.append(v)
    return reps


def fix(path, out, palette=None, colors=None, scale=None, upscale=1, transparent_bg=False, keep_orphans=False, max_colors=32,
        merge=MERGE, size=None):
    w, h, px = read_image(path)
    g = detect_grid(w, h, px, scale, size=size)
    if g["scale"] > 1:
        aw, ah, art, _, _ = sample(w, h, px, g["xb"], g["yb"])
    else:
        aw, ah, art = w, h, array("I", px)
    art = array("I", [(v | 0xFF000000) if alpha(v) >= 128 else 0 for v in art])
    before = len({v for v in art if v})
    if transparent_bg:
        border = [art[i] for i in range(aw)] + [art[(ah - 1) * aw + i] for i in range(aw)] + \
                 [art[j * aw] for j in range(ah)] + [art[j * aw + aw - 1] for j in range(ah)]
        bgc, n = Counter(v for v in border if v).most_common(1)[0] if any(border) else (0, 0)
        if bgc and n >= 0.4 * len(border):
            stack = [(x, y) for y in range(ah) for x in range(aw) if (x in (0, aw - 1) or y in (0, ah - 1))]
            seen = set()
            while stack:
                x, y = stack.pop()
                if (x, y) in seen or not (0 <= x < aw and 0 <= y < ah):
                    continue
                seen.add((x, y))
                v = art[y * aw + x]
                if v and dist(v, bgc) < 0.06:
                    art[y * aw + x] = 0
                    stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    counts = Counter(v for v in art if v)
    if palette:
        reps = [p | 0xFF000000 for p in palette]
    elif colors:
        reps = median_cut(counts, colors)
    else:
        reps = merge_similar(counts, merge)
        if len(reps) > max_colors:
            reps = median_cut(Counter({r: counts.get(r, 1) for r in reps}), max_colors)
    lut = {v: nearest(v, reps) for v in counts}
    art = array("I", [lut[v] if v else 0 for v in art])
    removed = 0
    if not keep_orphans:
        noise, _ = orphans(aw, ah, art)
        for x, y, _, maj in noise:
            art[y * aw + x] = maj
            removed += 1
    write_png(out, aw, ah, art, max(1, int(upscale)))
    after = len({v for v in art if v})
    return {"scale": g["scale"], "art": [aw, ah], "colors_before": before, "colors_after": after,
            "noise_removed": removed, "out": out}


# ---------- self-test ----------
def _synth(aw, ah, pal, rng, transparent=False):
    art = array("I", [0 if transparent else pal[0]] * (aw * ah))
    for _ in range(aw * ah // 6):
        x, y = rng.randrange(aw), rng.randrange(ah)
        rw, rh, c = rng.randint(1, 4), rng.randint(1, 4), rng.choice(pal[1:])
        for j in range(y, min(ah, y + rh)):
            for i in range(x, min(aw, x + rw)):
                art[j * aw + i] = c
    return art


def _resample(aw, ah, art, sizes_x, sizes_y, rng, noise=0, blur=False):
    xs, ys = [0], [0]
    for i in range(aw):
        xs.append(xs[-1] + sizes_x[i % len(sizes_x)] if isinstance(sizes_x, list) else xs[-1] + rng.choice(sizes_x))
    for j in range(ah):
        ys.append(ys[-1] + sizes_y[j % len(sizes_y)] if isinstance(sizes_y, list) else ys[-1] + rng.choice(sizes_y))
    w, h = xs[-1], ys[-1]
    px = array("I", [0] * (w * h))
    for j in range(ah):
        for i in range(aw):
            v = art[j * aw + i]
            for y in range(ys[j], ys[j + 1]):
                for x in range(xs[i], xs[i + 1]):
                    if noise:
                        r, g, b, a = unpack(v)
                        r, g, b = (min(255, max(0, c + rng.randint(-noise, noise))) for c in (r, g, b))
                        px[y * w + x] = pack(r, g, b, a)
                    else:
                        px[y * w + x] = v
    if blur:   # the first column of each cell becomes a mix of its two neighbours
        for i in range(1, aw):
            x = xs[i]
            for y in range(h):
                a, b = unpack(px[y * w + x - 1]), unpack(px[y * w + x + 1 if x + 1 < w else x])
                px[y * w + x] = pack(*((p + q) // 2 for p, q in zip(a, b)))
    return w, h, px


def selftest():
    import tempfile
    rng = random.Random(7)
    pal = [pack(26, 28, 44), pack(93, 39, 93), pack(177, 62, 83), pack(239, 125, 87), pack(255, 205, 117),
           pack(56, 183, 100), pack(59, 93, 201), pack(244, 244, 244)]
    res = []

    def ok(name, cond, info=""):
        res.append((name, bool(cond), info))

    tmp = tempfile.mkdtemp()
    p = os.path.join(tmp, "a.png")
    # 1. PNG round trip through the pure decoder (and Pillow's filtered PNGs when available)
    art = _synth(24, 16, pal, rng, transparent=True)
    write_png(p, 24, 16, art)
    _, _, back = read_image(p, pure=True)
    ok("PNG write/read round trip (pure decoder)", list(back) == list(art))
    try:
        from PIL import Image
        im = Image.new("RGBA", (24, 16))
        im.putdata([unpack(v) for v in art])
        im.save(p, optimize=True)
        _, _, back = read_image(p, pure=True)
        ok("pure decoder reads Pillow's filtered PNGs", list(back) == list(art))
        im.convert("RGB").quantize(colors=8).save(p)   # palette PNG
        _, _, back = read_image(p, pure=True)
        ok("pure decoder reads palette PNGs", len(back) == 24 * 16)
    except ImportError:
        ok("Pillow not installed: filtered-PNG check skipped", True)
    # 2. clean integer upscale: exact scale, exact art, no flags
    art = _synth(40, 24, pal, rng)
    w, h, px = _resample(40, 24, art, [4], [4], rng)
    write_png(p, w, h, px)
    rep, (aw, ah, a2) = analyse(p)
    ok("clean 4x screenshot: scale 4 found", rep["scale"] == 4, rep["scale"])
    ok("clean 4x screenshot: art recovered exactly", (aw, ah) == (40, 24) and list(a2) == list(art), (aw, ah))
    ok("clean 4x screenshot: no grid flags", not any(f["code"] in ("MIXELS", "NON_INTEGER_SCALE", "AI_OR_RESAMPLED") for f in rep["flags"]),
       [f["code"] for f in rep["flags"]])
    # 3. native art stays native
    write_png(p, 40, 24, art)
    rep, _ = analyse(p)
    ok("native-size art: scale 1", rep["scale"] == 1, rep["scale"])
    # 4. non-integer scale (2.5x: cells of 2 and 3 px) is flagged
    w, h, px = _resample(40, 24, art, [2, 3], [2, 3], rng)
    write_png(p, w, h, px)
    rep, _ = analyse(p)
    ok("2.5x scaling flagged NON_INTEGER_SCALE", any(f["code"] == "NON_INTEGER_SCALE" for f in rep["flags"]), [f["code"] for f in rep["flags"]])
    # 5. mixels: a 4x screenshot with one sprite drawn at half the pixel size (2 screen px per pixel)
    w, h, px = _resample(40, 24, art, [4], [4], rng)
    small = _synth(20, 12, pal, rng)
    for j in range(12):
        for i in range(20):
            for y in range(32 + 2 * j, 34 + 2 * j):
                for x in range(40 + 2 * i, 42 + 2 * i):
                    px[y * w + x] = small[j * 20 + i]
    write_png(p, w, h, px)
    rep, _ = analyse(p)
    ok("half-size sprite in a 4x screenshot flagged MIXELS", rep["scale"] == 4 and any(f["code"] == "MIXELS" for f in rep["flags"]),
       (rep["scale"], [f["code"] for f in rep["flags"]]))
    # 6. AI-like: drifting 6-7 px cells, colour noise and blurred cell borders
    art = _synth(32, 24, pal, rng)
    w, h, px = _resample(32, 24, art, (6, 7), (6, 7), rng, noise=10, blur=True)
    write_png(p, w, h, px)
    rep, _ = analyse(p)
    ok("AI-like image flagged", rep["verdict"] == "FAIL" and any(f["code"] in ("AI_OR_RESAMPLED", "TOO_MANY_COLORS") for f in rep["flags"]),
       [f["code"] for f in rep["flags"]])
    q = os.path.join(tmp, "fixed.png")
    r = fix(p, q, palette=pal)
    _, _, a3 = read_image(q)
    same = sum(1 for u, v in zip(a3, art) if u == v | 0xFF000000) / len(art) if r["art"] == [32, 24] else 0
    ok("fix with the palette recovers the art (>= 97% of pixels)", same >= 0.97, f"{r['art']} {same:.1%}")
    r = fix(p, q)
    _, _, a4 = read_image(q)
    same = sum(1 for u, v in zip(a4, art) if nearest(u, pal) == v) / len(art) if r["art"] == [32, 24] else 0
    ok("fix without a palette merges the noise (<= 12 colours, >= 95% match)", r["colors_after"] <= 12 and same >= 0.95,
       f"{r['colors_before']} -> {r['colors_after']} colours, {same:.1%}")
    # 7. stray pixels: a near-colour speck is noise, a bright eye is an accent
    art = array("I", [pal[5]] * (16 * 16))
    art[5 * 16 + 5] = pack(60, 178, 104)       # almost the same green
    art[10 * 16 + 10] = pal[7]                 # white highlight
    write_png(p, 16, 16, art)
    rep, _ = analyse(p)
    ok("near-colour speck counted as noise, bright pixel as accent", rep["noise_pixels"] == 1 and rep["accent_pixels"] == 1,
       (rep["noise_pixels"], rep["accent_pixels"]))
    ok("near-duplicate colours flagged SIMILAR_COLORS", any(f["code"] == "SIMILAR_COLORS" for f in rep["flags"]))
    fails = [r for r in res if not r[1]]
    for name, passed, info in res:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}" + (f"  ({info})" if info != "" else ""))
    print(f"\n{len(res) - len(fails)}/{len(res)} checks passed")
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("audit", help="report grid, colours, stray pixels and values, with flags and fixes")
    a.add_argument("image")
    a.add_argument("--palette", help="'#hex,#hex', a .hex/.gpl file or a palette PNG")
    a.add_argument("--max-colors", type=int, default=32)
    a.add_argument("--bg", help="background colour the sprite will sit on, e.g. '#1a1c2c'")
    a.add_argument("--scale", type=float, help="force the screen-pixels-per-art-pixel scale")
    a.add_argument("--size", help="the art size in pixels, e.g. 64x64 (most reliable for blurry images)")
    a.add_argument("--art", help="also save the detected art-resolution image here")
    a.add_argument("--json", action="store_true")
    f = sub.add_parser("fix", help="snap to the grid, quantize, clean stray pixels, write a native-size PNG")
    f.add_argument("image")
    f.add_argument("-o", "--out", required=True)
    f.add_argument("--palette")
    f.add_argument("--colors", type=int, help="reduce to this many colours (median cut in OKLab)")
    f.add_argument("--max-colors", type=int, default=32)
    f.add_argument("--scale", type=float, help="force the screen-pixels-per-art-pixel scale")
    f.add_argument("--size", help="the art size in pixels, e.g. 64x64 (most reliable for blurry images)")
    f.add_argument("--upscale", type=int, default=1, help="also enlarge the result by this integer (nearest neighbour)")
    f.add_argument("--transparent-bg", action="store_true", help="flood-fill the border colour to transparent")
    f.add_argument("--keep-orphans", action="store_true", help="do not remove low-contrast stray pixels")
    f.add_argument("--merge", type=float, default=MERGE, help=f"merge colours closer than this OKLab distance (default {MERGE})")
    sub.add_parser("selftest", help="run the built-in checks")
    args = ap.parse_args()
    if args.cmd == "selftest":
        return selftest()
    pal = load_palette(args.palette) if args.palette else None
    size = tuple(int(v) for v in args.size.lower().split("x")) if getattr(args, "size", None) else None
    if args.cmd == "audit":
        from pixelkit import parse_hex
        rep, (aw, ah, art) = analyse(args.image, pal, args.max_colors, parse_hex(args.bg) if args.bg else None, args.scale, size)
        if args.art:
            write_png(args.art, aw, ah, art)
        if args.json:
            print(json.dumps(rep, indent=1))
        else:
            print_report(rep)
        return 1 if rep["verdict"] == "FAIL" else 0
    r = fix(args.image, args.out, pal, args.colors, args.scale, args.upscale, args.transparent_bg, args.keep_orphans, args.max_colors,
            args.merge, size)
    print(f"scale {r['scale']} -> art {r['art'][0]}x{r['art'][1]}; colours {r['colors_before']} -> {r['colors_after']}; "
          f"stray pixels removed {r['noise_removed']}; wrote {r['out']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
