# Pixel art craft: why some pixel art reads as crafted and some as cheap

`pixel-art-direction.md` fixes the constraints (canvas, palette size, frame counts). This file is
the theory behind the pixels themselves: what experienced pixel artists look at, the named defects
players notice even when they cannot name them, and how to check each one with the bundled scripts
(`scripts/pixel_audit.py`, `scripts/palette_ramp.py`).

Pixel art is defined less by low resolution than by **intent**: every pixel is placed on purpose,
and the artist stays in control at the level of the single pixel [D23], [D25]. Viewers read that
intent from consistency: one grid, deliberate clusters, a controlled palette and a single light
source. Most "cheap-looking" pixel art breaks one of these on a short list of named defects
(section 14).

## 1. The grid is the medium

- **One pixel size everywhere.** Mixed pixel sizes ("mixels") come from scaling a sprite, mixing
  asset packs, rotating or anti-aliased text. They break the illusion faster than any drawing
  mistake. Only a background layer may differ, and even then it uses one size throughout.
- **Integer scaling, whole-pixel positions.** Scale the whole frame by 2, 3, 4… with nearest
  neighbour. Draw sprites and the camera at whole art pixels. Fractional positions or scales make
  pixels change width as things move.
- **Presentation:** share art at 2–4× in PNG or GIF, never JPEG; compression smears pixels [D23],
  [D25]. Store screenshots should be integer multiples too.
- **Resolution sets the style.** Celeste is commonly reported at 320×180 and Hyper Light Drifter
  at 480×270 (community-sourced figures [D35]). 480×270 reads less retro unless characters are
  large; 320×180 leaves room for little detail.

## 2. Clusters, not pixels

A **cluster** is a group of touching pixels of one colour. It is the real unit of decision: the
shape of each cluster, and how it meets its neighbours, decides the look [D23], [D25].

- Simple angular clusters give a clean, sharp look; varied organic clusters give a natural one.
  Pick one per game.
- A **lone pixel** that belongs to no cluster reads as noise and exposes the grid. Keep single
  pixels for deliberate jobs: eyes on small sprites, specular highlights, stars, bubbles [D23].
- **Chunky pixel rule:** avoid 1-px-thick limbs and branches on anything that needs volume. They
  cannot be shaded, so they look flat and flimsy [D18].
- **Less is more.** Implied detail lets the viewer fill in the rest. Overworked sprites lose
  their charm, so stop polishing when the read is clear [D18], [D25].

## 3. Lines

- A straight line at any angle other than 0°, 45° or 90° is a staircase. Keep its steps
  consistent (1:1, 2:1, 3:1…). A step of a different length is a **jaggy**.
- In curves, step lengths should grow or shrink steadily (1-2-3-4, never 1-3-1) [D18], [D23].
  Some jaggies are unavoidable; keep them where they describe form.
- A **double** is an extra pixel at a corner that thickens a 1-px line. Remove it.
- Isometric art uses 2:1 lines (about 26.6°), not true 30°, because 30° steps unevenly [D25].

## 4. Banding

**Banding** happens when neighbouring clusters start and end at the same x or y. The eye then
sees the grid instead of the form [D23], [D24]. It shows up as:

- an outline with a shading band that hugs it at the same length;
- parallel bands of equal width ("staircase banding");
- anti-aliasing segments that line up with the line they soften.

The fix is to vary cluster lengths, offset where they end, and shade from the light rather than
from the outline.

## 5. Light, form and projection

- **Pick the light source first**, usually above and from a top corner, and keep it for every
  sprite and tile [D25].
- **Shade forms, not outlines.** Simplify objects into volumes: a treetop is a few spheres, a nest
  is a bowl [D18]. Shading in rings from the outline inward ignores the light. This is **pillow
  shading**, and it makes objects soft and blurry [D18], [D23]. A frontal light is fine; what
  matters is that shading follows the form [D23].
- **Quick checks** [D18]:
  - Squint: a few large clusters of light and dark should still read.
  - Desaturate: the shading must work in greyscale.
  - Flip horizontally: proportion and shading errors jump out.
- **Projection.** Never mix viewpoints in one scene (top-down 3/4, side view, isometric). Depth
  comes mostly from light falling differently on planes where they meet [D25].
- **Cast shadows set the air:** hard and crisp for clear air, soft for haze [D25].

## 6. Anti-aliasing and outlines

**Anti-aliasing (AA)** places in-between pixels so a jagged edge reads smooth. It works through
**perceived value** (lightness), not hue [D24].

- The longer the segment, the longer the AA run.
- For a long transition, use a few AA colours in runs of different lengths rather than many
  single pixels.
- Choose AA colours by value. A different hue of similar value often looks better than the
  muddy average of two colours [D24].

| Mistake | What happens | Rule |
|---|---|---|
| Outer AA on game sprites | It fringes on any other background | Never AA against an unknown background; semi-transparent pixels only for effects [D18], [D24] |
| Too much AA | The line blurs | Use only what smooths the step [D23] |
| Too little AA | Single pixels only blunt the step | Lengthen the AA runs [D23] |
| AA on tiny sprites | It reads as noise | Ask whether it is needed; often the answer is no [D24] |

**Outline policy** (choose one per layer):

- **Black outline:** a cartoony look, and segments inner forms harshly.
- **Coloured outline:** the darkest colour of the adjacent ramp.
- **Selective outline (sel-out):** the outline lightens where light hits and drops out toward
  negative space [D18]. It is really AA applied to the outline, so it is safest when the
  background is known [D23], [D24].

Celeste's artist favours outer outlines because they separate sprites from any background [D17].
A **broken inner line** can show a soft fold without spending a colour [D24].

## 7. Colour

| Rule | Practice |
|---|---|
| Ramps per material | 3–5 colours for game sprites, more in big master palettes. Brightness rises steadily; saturation peaks mid-ramp and falls toward the bright end, because bright plus saturated burns the eyes [D25], [D23] |
| Hue shift | Lights turn warmer (toward yellow), shadows cooler (toward blue or violet). Ramps without it ("straight ramps") look flat and are hard to harmonise. About 20° per step is one practitioner's upper bound [D25], [D23] |
| Even value steps | Space lightness evenly in a perceptual space (OKLab L), not in HSB, where equal steps do not look equal [D30], [D25] |
| Shared colours | The darkest and lightest colours often serve every ramp, and neutral mid-tones bridge ramps. Fewer colours mean cohesion and control [D23] |
| Every colour has a job | Too-similar colours blend into mush. Merge them or push them apart [D18] |
| Avoid naive colour | Leaves are not pure green and rocks are not pure grey; reflected light mixes hues [D18] |
| Value range | Use darks, mid-tones and highlights. Perceived value depends on the neighbours, and a darker pixel makes a line look thicker [D23] |
| Start from a published palette | 16 and 32 colours are common sizes [D18]. The template uses Sweetie 16 [D36] |
| Colour cycling | Rotate palette entries to animate water, fire or time of day, with no new frames [D33] |

`palette_ramp.py ramp` builds a ramp with these rules. `palette_ramp.py check` flags straight
ramps, uneven value steps, near-duplicates, eye-burning colours and gaps in the value scale.

## 8. Dithering

Dithering blends two colours without adding a third, or adds texture [D18], [D23].

- **Patterns:** the 50% checkerboard is calmest. 25/75 patterns show more. Interlaced dithering
  joins two dithered regions. Random dithering is single-pixel noise; avoid it.
- **CRTs blurred dither into a solid colour; LCDs do not.** Patterns now stay visible, so use
  less [D23], [D33].
- **Lower-contrast pairs dither more softly.** If dither covers half a sprite, add a colour
  instead [D23].
- **Where it belongs:** large areas (skies) and rough materials, not small characters [D18].

## 9. Texture

- Reduce the material to a few abstract key clusters. Repeat them with varied spacing [D25].
- Balance detail across the area.
- Leave empty stretches so the texture is implied. Busy next to busy tires the eye; negative
  space rests it [D25].
- Do not let key clusters touch and merge into blobs; corner contact is fine [D25].
- Orphan pixels are acceptable only when they clearly belong to a larger texture [D25].

## 10. Tiles

- **Size:** 16×16 is the common choice, and larger than 32×32 is rarely worth the labour; 8×8
  works and reads chunky [D25].
- **Hide the repeat:** spread visual weight evenly so no feature repeats as a pattern. Let
  clusters cross tile edges to hide seams. Mix flat tiles, variants and props. Mirror tiles to
  save time. Always preview the tile repeated at 1× [D25].
- **Transitions:** a 16-tile set handles edges (4 neighbours) or, with the dual-grid method,
  corners. The 47-tile "blob" set covers every 8-neighbour shape; diagonals matter only when both
  adjacent edges are filled. Animated tiles can cycle frames inside one index [D27].
- **Isometric tiles:** 2:1 lines, even dimensions, cuboids first [D25].

## 11. Animation

- **Key poses first.** The extremes must read on their own; in-betweens are optional [D25].
- **Energy over smoothness.** Too many frames drain energy. A three-pose run (stride, pass,
  stride) can beat eight frames. When you cut frames, lengthen the holds: eight poses at 80 ms
  carry about the same motion as four at 160 ms [D25].
- **Block in flat colours first,** one body part at a time, and add detail only once the motion
  works [D25].
- **Quadrupeds:** the back leg follows the opposite front leg by a step, and both pairs travel
  the same distance, or the body stretches like an accordion [D25].
- **Respect clusters in every frame.** A stray pixel flickers in a loop [D25].
- **Sub-pixel animation** is animated anti-aliasing. To move something less than a pixel, shift
  the colours (light, shadow, edge blend) instead of the pixels. It needs enough shades and
  suits small sprites and details [D24], [D26].
- **Smear frames** stretch a fast motion into one streak frame; use them sparingly [D17].
- **Tiny sprites** move at least one pixel per frame. Split bigger characters into layered parts
  you can move separately [D25].

## 12. Production at scale

- **Dead Cells** modelled characters in 3D and converted the animations to pixel art with an
  in-house tool. That gave consistency without hand-drawing every retake [D34]. A 3D-to-pixel
  pipeline still needs pixel rules on its output: no AA, palette mapping, snapped positions.
- **Authenticity versus comfort.** Shovel Knight mostly kept the NES palette, adding a few
  colours. It broke any hardware limit that hurt play, for example with layered parallax. The
  aim was the remembered game, not the hardware [D32].

## 13. AI-generated "pixel art"

**Typical defects** [D31]:

- The cells drift in size and position, with no single grid.
- Mixels.
- Hundreds of colours.
- Soft gradients and blur, and chaotic dither.
- Semi-transparent edges.
- Letter-like blobs instead of text.

None of these proves AI on its own; beginners make the same mistakes.

**Repair pipeline** (`pixel_audit.py fix`, after [D31]):

1. Find the period from the spacing between edges.
2. Follow the grid where it drifts.
3. Take the dominant colour of each cell's inner area.
4. Make alpha fully on or off.
5. Map colours to the palette, or merge near-duplicates.
6. Remove low-contrast stray pixels.

Then fix lines, AA and light by hand; the tool restores the grid, not intent. On real game art
degraded on purpose, it recovered:

| Degradation | Recovered |
|---|---|
| Nearest-neighbour 4× + JPEG 60 | 96% of art pixels |
| Bicubic 5.7× + JPEG 70 | 93% |
| Bilinear 3.3× + JPEG 80 | About 80%, only when told the art size (`--size`) |

Heavy blur on small cells is a limit. Give `--size WxH` when you know the art size.

**Research context:**

- Making pixel art from images is a joint choice of a small palette and a mapping. Expert pixel
  artists preferred the jointly optimised results to naive downsampling [D29].
- The reverse direction (vectorising pixel art) works because pixel art is a deliberate
  abstraction, not a blurry photo [D28].

## 14. Defect checklist (most visible first)

| # | Defect | What players see | Check | Fix |
|---|---|---|---|---|
| 1 | Mixels, non-integer scale, sprites off the grid | Shimmer, a "cheap" look | `pixel_audit` MIXELS, NON_INTEGER_SCALE | One pixel size, integer scale, whole-pixel positions |
| 2 | AA leaks (browser fonts, smoothing, rotation, alpha blends) | Soft edges, stray colours | AI_OR_RESAMPLED, OFF_PALETTE, SOFT_ALPHA; in-game palette-only frame test | Bitmap fonts, smoothing off, no rotation |
| 3 | Too many or too similar colours | Mud, no clear forms | TOO_MANY_COLORS, SIMILAR_COLORS; `palette_ramp check` | Ramps per material; merge near-duplicates |
| 4 | Random speckle and orphans | Grit, unfinished | NOISE_PIXELS; the accent count | Key clusters plus empty space |
| 5 | Low value range, sprite melts into the background | Unreadable | LOW_VALUE_RANGE, MELTS_INTO_BG (`--bg`); greyscale | Spread values; outline |
| 6 | Bright and saturated together | Eye strain | EYEBURN | Desaturate as colours brighten |
| 7 | Straight ramps, uneven steps | Flat, lifeless colour | STRAIGHT_RAMP, UNEVEN_STEPS | Hue shift; even OKLab steps |
| 8 | Jaggies and doubles | Wobbly lines | By eye at 1× | Even step patterns |
| 9 | Banding and pillow shading | Flat, blurry forms | By eye; squint test | Shade from the light; offset cluster ends |
| 10 | Over-dithering | A noisy field | By eye | Add a colour; dither large areas only |
| 11 | Overworked detail | Stiff, airless | By eye | Remove pixels; imply detail |
| 12 | Mechanical animation | Lifeless motion | Frame-timing review | Key poses, varied holds, sub-pixel AA |

## 15. Audit flags

`pixel_audit.py audit` finds the scale of a screenshot or AI image and analyses one colour per art
pixel.

- **MIXELS** (fail): more than 1% of art pixels hold several screen colours on an otherwise clean
  image. The report says where.
- **NON_INTEGER_SCALE** (fail): flat cells of uneven width.
- **AI_OR_RESAMPLED** (fail): more than 8% of pixels inside cells disagree with their cell.
- **OFF_PALETTE** (fail, with `--palette`).
- **TOO_MANY_COLORS** (warn above the budget; fail above four times the budget).
- **SIMILAR_COLORS:** pairs closer than 0.03 OKLab.
- **NOISE_PIXELS:** low-contrast single pixels over 1.5% of the art.
- **LOW_VALUE_RANGE:** 5th–95th percentile lightness span under 0.40.
- **EYEBURN:** more than 15% of pixels near full saturation and brightness.
- **MELTS_INTO_BG:** more than 35% of edge pixels close in value to `--bg`.
- **SOFT_ALPHA:** semi-transparent pixels.

Lines, banding, pillow shading and light direction still need eyes; the report says so.

## Sources
- [D17] Medeiros (Saint11), tutorials and readability notes. · [D18] Yu, *Pixel Art Tutorial* and *Common Mistakes*.
- [D23] Pixel Joint, "The Pixel Art Tutorial". · [D24] Pixel Parmesan (2020), anti-aliasing fundamentals.
- [D25] Schlitter (SLYNYRD), Pixelblog 1, 2, 3, 5, 6, 8, 20, 25, 26, 41, 47. · [D26] 2D Will Never Die, sub-pixel animation.
- [D27] Red Blob Games, autotiling. · [D28] Kopf & Lischinski (2011). · [D29] Gerstner et al. (2012).
- [D30] Ottosson (2020), OKLab. · [D31] unfake and Sprite Fusion Pixel Snapper (AI pixel-art repair tools).
- [D32] D'Angelo (2014), "Breaking the NES". · [D33] Ferrari (GDC 2016); colour cycling. · [D34] Vasseur (2018), Dead Cells pipeline.
- [D35] Reported internal resolutions (community figures). · [D36] Sweetie 16 palette (GrafxKid, Lospec).
- Full bibliography: `research/SOURCES.md` in the repository.
