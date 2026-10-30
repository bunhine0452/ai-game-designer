#!/usr/bin/env python3
"""Render the ai-game-designer banner ("Measured Wonder", see banner-philosophy.md).

  python3 docs/design/make_banner.py --fonts <dir with Instrument Serif/Sans + Geist Mono TTFs>

Writes docs/images/banner.png (2560x1280, README) and docs/images/social-preview.png
(1280x640, GitHub social preview, < 1 MB). Fonts: Instrument Serif, Instrument Sans and
Geist Mono (SIL Open Font License, Google Fonts). Needs numpy + matplotlib.

Hidden in plain sight: the gold line is an interest curve (hook, rising peaks, climax,
resolution), the diagonal band is a flow channel, the 26 ticks are the genre playbooks, the
six markers are the six skills, and the 121 faint traces are the bibliography's 121 sources.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

INK, IVORY, SLATE, GOLD = "#0d121d", "#ede6d6", "#5f6b80", "#f0b44c"
W, H = 2560, 1280
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def curve(t):
    """Smooth interest curve: hook, dip, three rising peaks, climax, resolution."""
    keys = np.array([[0.00, .30], [.06, .74], [.14, .37], [.30, .56], [.39, .43], [.55, .71],
                     [.64, .54], [.80, .87], [.89, 1.0], [1.0, .46]])
    xs = np.linspace(0, 1, 2001)
    ys = np.interp(xs, keys[:, 0], keys[:, 1])
    k = np.exp(-np.linspace(-3, 3, 121) ** 2)             # gaussian smoothing kernel
    ys = np.convolve(np.pad(ys, 60, mode="edge"), k / k.sum(), mode="valid")
    return np.interp(t, xs, ys)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", required=True)
    a = ap.parse_args()
    f = lambda name: FontProperties(fname=os.path.join(a.fonts, name))  # noqa: E731
    serif, italic = f("InstrumentSerif-Regular.ttf"), f("InstrumentSerif-Italic.ttf")
    sans, mono = f("InstrumentSans-Regular.ttf"), f("GeistMono-Regular.ttf")
    pt = lambda px: px * 72 / 100                                        # noqa: E731  px -> pt at dpi 100

    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    fig.patch.set_facecolor(INK); ax.set_facecolor(INK)
    rng = np.random.default_rng(121)

    # Plate geometry
    X0, X1, Y0, Y1 = 1190, 2420, 270, 1010
    px = lambda t: X0 + t * (X1 - X0)                                    # noqa: E731
    py = lambda v: Y1 - v / 1.12 * (Y1 - Y0)                             # noqa: E731

    # Dot lattice (the ruled paper of the plate)
    gx, gy = np.meshgrid(np.arange(X0, X1 + 1, 41), np.arange(Y0, Y1 + 1, 39))
    ax.scatter(gx, gy, s=1.1, color=SLATE, alpha=.35, linewidths=0)

    # Flow channel: a soft diagonal band
    t = np.linspace(0, 1, 400)
    lo, hi = .16 + .62 * t, .40 + .62 * t
    ax.fill_between(px(t), py(np.minimum(lo, 1.1)), py(np.minimum(hi, 1.1)), color=GOLD, alpha=.045, linewidth=0)
    for edge in (lo, hi):
        ax.plot(px(t), py(np.minimum(edge, 1.1)), color=SLATE, lw=.6, alpha=.55, dashes=(2, 5))

    # 121 faint traces: the evidence
    for _ in range(121):
        shift, amp = rng.normal(0, .012), rng.normal(1, .06)
        wob = sum(rng.normal(0, .016) * np.sin(2 * np.pi * (k + 1) * t + rng.uniform(0, 6.28)) for k in range(3))
        ax.plot(px(t), py(np.clip(curve(np.clip(t + shift, 0, 1)) * amp + wob, 0, 1.1)), color=IVORY, lw=.55, alpha=.075)

    # The one line that matters
    ys = curve(t)
    for w, al in ((16, .035), (9, .06), (5, .12)):
        ax.plot(px(t), py(ys), color=GOLD, lw=w, alpha=al, solid_capstyle="round")
    ax.plot(px(t), py(ys), color=GOLD, lw=2.6, solid_capstyle="round")

    # Six markers on the line
    marks = [(.06, "hook"), (.30, ""), (.55, ""), (.80, ""), (.89, "climax"), (.985, "")]
    for tm, label in marks:
        x, y = px(tm), py(curve(tm))
        if label == "climax":
            for r, al in ((46, .18), (30, .35)):
                ax.add_patch(plt.Circle((x, y), r, fill=False, ec=GOLD, lw=.9, alpha=al))
            ax.add_patch(plt.Circle((x, y), 9, color=GOLD, zorder=5))
        else:
            ax.add_patch(plt.Circle((x, y), 8, fc=INK, ec=IVORY, lw=1.4, zorder=5))
        if label:
            ax.text(x, y - 62, label.upper(), fontproperties=mono, fontsize=pt(17), color=IVORY, alpha=.7,
                    ha="center", va="bottom")

    # Axes and 26 ticks
    ax.plot([X0, X0], [Y0 - 10, Y1], color=SLATE, lw=.8); ax.plot([X0, X1 + 10], [Y1, Y1], color=SLATE, lw=.8)
    for i in range(26):
        x = X0 + (i + .5) * (X1 - X0) / 26
        ax.plot([x, x], [Y1, Y1 + (16 if i % 5 == 0 else 9)], color=SLATE, lw=.8)
    for v in (0, .25, .5, .75, 1.0):
        ax.plot([X0 - 9, X0], [py(v), py(v)], color=SLATE, lw=.8)
    ax.text(X0 - 26, Y0 - 10, "INTEREST", fontproperties=mono, fontsize=pt(16), color=SLATE, rotation=90, ha="right", va="top")
    ax.text(X1 + 10, Y1 + 44, "TIME", fontproperties=mono, fontsize=pt(16), color=SLATE, ha="right", va="top")
    ax.text(X0, Y1 + 82, "FIG. 1   INTEREST OVER TIME   ·   N = 121", fontproperties=mono, fontsize=pt(17), color=SLATE, ha="left", va="top")

    # Typography column
    L = 140
    ax.text(L, 300, "PLATE 01   ·   LUDOMETRY", fontproperties=mono, fontsize=pt(20), color=GOLD, ha="left", va="baseline")
    ax.plot([L, L + 70], [338, 338], color=GOLD, lw=1.2)
    ax.text(L - 6, 560, "ai-game", fontproperties=serif, fontsize=pt(176), color=IVORY, ha="left", va="baseline")
    ax.text(L - 6, 720, "designer", fontproperties=italic, fontsize=pt(176), color=IVORY, ha="left", va="baseline")
    ax.text(L, 830, "Research-backed game design skills", fontproperties=sans, fontsize=pt(42), color=IVORY, alpha=.92, ha="left", va="baseline")
    ax.text(L, 888, "for any AI agent.", fontproperties=sans, fontsize=pt(42), color=IVORY, alpha=.92, ha="left", va="baseline")
    ax.text(L, 1010, "PACING  ·  GENRES  ·  BALANCE  ·  DOCUMENTS  ·  REVIEW  ·  PROTOTYPES", fontproperties=mono, fontsize=pt(19.5), color=SLATE, ha="left", va="baseline")

    # Paper grain
    grain = rng.normal(0, 1, (H // 2, W // 2))
    ax.imshow(grain, cmap="gray", extent=(0, W, H, 0), alpha=.035, interpolation="bilinear", zorder=10)

    # Safety check: nothing may run off the canvas or into the plate
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for txt in ax.texts:
        bb = txt.get_window_extent(r)
        assert bb.x0 >= 60 and bb.x1 <= W - 60 and bb.y0 >= 40 and bb.y1 <= H - 40, (txt.get_text(), bb)
        if txt.get_position()[0] < 1000:
            assert bb.x1 < X0 - 90, ("text column overlaps plate", txt.get_text(), bb.x1)

    out = os.path.join(ROOT, "docs", "images")
    master = os.path.join(out, ".banner-master.png")
    fig.savefig(master, facecolor=INK)
    plt.close(fig)
    from PIL import Image                      # Pillow ships with matplotlib
    img = Image.open(master).convert("RGB")
    img.resize((2000, 1000), Image.LANCZOS).save(os.path.join(out, "banner.png"), optimize=True)
    img.resize((1280, 640), Image.LANCZOS).save(os.path.join(out, "social-preview.png"), optimize=True)
    os.remove(master)
    for n in ("banner.png", "social-preview.png"):
        p = os.path.join(out, n)
        print(n, os.path.getsize(p) // 1024, "KB")


if __name__ == "__main__":
    main()
