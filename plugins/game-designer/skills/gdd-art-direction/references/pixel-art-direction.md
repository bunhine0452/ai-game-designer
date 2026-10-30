# Pixel art direction

Pixel art is a set of constraints chosen on purpose: a fixed grid, a small palette and few
frames. Decide the constraints first and write them down. Most "it looks off" problems come
from breaking them by accident (mixed pixel sizes, rotated sprites, smooth scaling).

This file covers the decisions. The craft behind them (clusters, lines, banding, light and form,
anti-aliasing, ramps, dithering, texture, tiles, animation, AI-generated art) and a defect
checklist are in `pixel-art-craft.md`. The checks run with `scripts/pixel_audit.py` and
`scripts/palette_ramp.py` (section 8).

## 1. Lock the canvas

| Decision | Options | Rule of thumb |
|---|---|---|
| Internal resolution | 320×180, 384×216, 480×270, 640×360 | Pick one that **integer-scales** to 1920×1080 (×6, ×5, ×4, ×3). Render to that buffer, then scale it up with nearest-neighbour. |
| Tile size | 8, 16, 24, 32 px | 16 px suits most top-down and platformer games. Smaller tiles mean more readable rooms but less character detail. |
| Character size | 16–48 px tall | Decide how much face and silhouette you need. A 16 px hero reads by pose; 32 px and up can show expression. |
| Pixel density | One size for everything | Never mix pixel sizes: no 2× sprites beside 1× tiles, no smooth-scaled UI. |
| Camera | Pixel-snapped | Snap the camera and sprites to whole pixels of the internal buffer. Sub-pixel movement shimmers. |
| Projection | Side view, top-down 3/4, isometric (2:1 lines) | One projection per scene; never mix viewpoints. |
| Outline policy | None, dark, coloured, selective (sel-out) | One policy per layer. Outer outlines keep sprites readable on any background. |
| Anti-aliasing | None, inner only | Never outer AA on game sprites: the background is unknown. |
| Dithering | None, 50% checker on large areas | Skies and rough materials only; add a colour instead of dithering half a sprite. |

Write these in the style guide as **hard rules** with a one-line reason each.

## 2. Palette

- **Start small:** 16–32 colors for the whole game, organized as **ramps** (dark → light) per
  material: skin, foliage, stone, water, metal, UI. Published palettes (for example on Lospec)
  are good starting points; adjust them to your pillars.
- **Hue-shift the ramps:** shadows drift toward cool or purple, highlights toward warm or
  yellow. That reads livelier than plain darker and lighter versions of one hue. Build ramps
  with `palette_ramp.py ramp --base "#hex"` (even perceptual steps, at most about 20° of hue per
  step) and check a finished palette with `palette_ramp.py check`.
- **Reserve colors for gameplay:** danger, pickup and interactable each get a hue that
  decoration never uses (the readability rule in `art-direction.md`).
- **Check value first:** grayscale a screenshot. The player, hazards and the goal must
  separate by brightness alone. This also covers most color-vision deficiencies.
- **Backgrounds recede:** lower contrast and saturation than the play layer, and fewer details
  per tile.

## 3. Drawing rules that keep it clean

- **Clean lines:** avoid doubles (2 px where 1 px would do), jaggies (uneven steps in a curve)
  and orphan pixels. Curves step as 1-2-3-4 or 4-3-2-1, not 1-3-1.
- **Outlines:** pick a policy. No outline, dark outline, or selective outline ("selout":
  outline colored by the adjacent fill, lighter toward the light). Use the same policy for
  everything at the same layer.
- **Anti-aliasing by hand,** only on large curves and only inside the sprite, never against an
  unknown background.
- **Dithering** is a texture tool (sky gradients, rough stone), not a way to fake extra colors
  everywhere. Keep it off characters at small sizes.
- **Light from one direction,** consistent across sprites and tiles (usually top-left).
- **Silhouette test:** fill each sprite black. Every enemy type and every pickup must be
  recognizable from the shape alone.

## 4. Animation

| Action | Frames | Notes |
|---|---|---|
| Idle | 2–6 | A breathing bob of 1 px is enough at small sizes |
| Walk / run | 4–8 | Strong contact poses. Keep the head's vertical travel to 1–2 px |
| Attack | 3–6 | Anticipation (hold 2–3 ticks) → active frame (1–2 ticks) → recovery; add a smear frame |
| Hit / death | 2–4 | Flash a reserved color for 1–2 frames, then knockback |

- Animate on **ticks** (for example 1 tick = 1/60 s, a frame holds 4–8 ticks) and vary the
  holds. Even timing looks mechanical.
- Squash and stretch, smears and secondary motion (hair, scarf) work at pixel scale too, but
  keep the volume constant.
- Particles are pixels as well: square, palette-locked, and snapped to the grid.

## 5. Tiles, UI and text

- Build tiles as a **set** (inner, edges, corners, transitions) and test them for seams and
  repetition by painting a large area. Break up repetition with 2–3 variants and props.
- Use a **bitmap font** drawn on the same grid (for example 5×7 or 6×8 for body text) or a
  pixel font rendered at integer sizes only. Never use a smooth font scaled by a non-integer.
- UI frames use the palette's darkest ramp and one accent. Keep text contrast at 4.5:1 or
  higher, and offer a larger-text option.

## 6. Scope math

Count the art: unique sprites × animations × frames, plus tiles × variants. At 16 px, a
practiced artist might finish a handful of animated frames per hour; at 32–48 px, far fewer.
Put this count into the asset list (`scope-and-assets.md`) before promising content.

## 7. Style guide block (copy into the style guide)

```
Canvas: 384×216, ×5 to 1920×1080, nearest-neighbour, pixel-snapped camera
Projection: top-down 3/4 · Tiles: 16 px · Hero: 24 px tall · Enemies: 16–32 px
Palette: 24 colors in 6 ramps (+2 reserved: danger #e43b44, pickup #feae34)
Outlines: selout on characters, none on tiles · Light: top-left · AA: inner only
Dithering: 50% checker on skies and rough stone only
Animation: 12 ticks/s base; hero walk 6 frames, attack 5 (smear on frame 3)
Font: 6×8 bitmap, integer scaling only
Checks: pixel_audit.py PASS on every screenshot; palette_ramp.py check on the palette
Never: rotated sprites, mixed pixel sizes, smooth scaling, unreserved red, JPEG
```

## 8. Checks and AI-generated assets

- **Every screenshot:** `python3 scripts/pixel_audit.py audit shot.png --palette palette.hex`.
  It finds the scale and reports mixels, off-palette colours, noise, near-duplicate colours,
  value range and eye-burning colours, each with a fix. A prototype's own `?test=1` should also
  assert that a drawn frame holds palette colours only (the pixel template does).
- **Sprites on a known background:** add `--bg "#hex"` to catch sprites whose edges melt into
  it.
- **AI-generated "pixel art":** never use it as is. Run
  `pixel_audit.py fix ai.png -o clean.png --palette palette.hex`, giving `--size WxH` when you
  know the art size. Then repaint lines, anti-aliasing and light by hand, and audit again. See
  `pixel-art-craft.md` §13 for what the repair can and cannot recover.

## Sources
- [D16] Azzi, M. (2017; revised 2022). *Pixel Logic: A Guide to Pixel Art*.
- [D17] Medeiros, P. (Saint11). Pixel art tutorials (animated GIF series).
- [D18] Yu, D. *Pixel Art Tutorial* and *Common Mistakes* (derekyu.com).
- [D23] Pixel Joint, *The Pixel Art Tutorial*; [D25] Schlitter (SLYNYRD), *Pixelblog*; [D30] Ottosson, OKLab; [D31] AI pixel-art repair tools.
- [D5] Readability and silhouettes (TF2); [D11] color-vision deficiency; [D12] WCAG contrast.
- Full bibliography: `research/SOURCES.md` in the repository.
