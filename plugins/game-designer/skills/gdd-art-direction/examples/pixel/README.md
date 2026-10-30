# Pixel audit and repair: a worked example

The input imitates AI-generated "pixel art". We took a 160×90 piece of *Dot Gardener* (one of the
showcase games) and degraded it the way image models and careless resizing do: bicubic
enlargement to 912×513 (5.7× per pixel), then JPEG at quality 70. The result has soft edges,
thousands of colours and no clean grid.

## Commands

```bash
python3 ../../scripts/pixel_audit.py audit ai-like-input.jpg            > audit-before.txt
python3 ../../scripts/pixel_audit.py fix ai-like-input.jpg -o fixed.png --palette palette.hex --upscale 4
python3 ../../scripts/pixel_audit.py audit fixed.png --palette palette.hex > audit-after.txt
python3 ../../scripts/palette_ramp.py check palette.hex \
  --ramps "#1a1726 #3a3a52 #5f6378 #8b93a1 #c3c8c9 | #24372f #3d5a45 #5f7d58 #8ea36f | #3b2a26 #6b4a3a #9a7050 #c9a27a | #1f3b5a #3c6e8f #74a9be" \
  --png palette-ramps.png > palette-check.txt
python3 ../../scripts/palette_ramp.py ramp --base "#3f8f5a" --png ramp-green.png > ramp-green.txt
```

## What happened

| Step | Result |
|---|---|
| Audit of the input | **FAIL**. The grid was found at 5.69 px per art pixel (160×90 cells), but 47% of pixels disagree with their cell and there are 5,641 colours. Flags: AI_OR_RESAMPLED, TOO_MANY_COLORS, NOISE_PIXELS. |
| Fix | 160×90 art, 25 palette colours, 88 low-contrast stray pixels removed. **93.3%** of art pixels match the original. |
| Audit of the result | Clean 4× grid, no mixels, no stray colours. One warning remains, LOW_VALUE_RANGE: this stone-heavy crop really is mid-grey, so a designer should decide whether that is intended. |
| Palette check | The game's four ramps (stone, moss, soil, water) rise in even steps (0.12–0.19 OKLab L). Each shifts hue by 8–28° from dark to light. No flags. |
| Ramp | A five-step green ramp around `#3f8f5a`: even lightness, shadows toward teal, lights toward yellow, saturation peaking at the base colour. |

The remaining 7% are mostly thin details (single-pixel flowers, one-pixel mortar lines) that the
blur erased. The repair restores the grid and palette; a person still repaints those details.

## Files

- `ai-like-input.jpg`: the degraded input.
- `fixed.png`: the repaired art, shown at 4×.
- `palette.hex`: the original colours.
- `audit-before.txt`, `audit-after.txt`, `fix-log.txt`: the reports.
- `palette-check.txt` and `palette-ramps.png`: the palette check and its ramp sheet.
- `ramp-green.txt` and `ramp-green.png`: the generated ramp.
