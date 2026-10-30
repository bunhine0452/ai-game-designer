# 3D and pixel prototypes

Both keep the single-file contract (`?test=1`, `?shot=1`, logic separate from rendering).
Start from `assets/template-3d.html` or `assets/template-pixel.html`.

## Pixel prototypes

**Render pipeline.** Draw everything into a small offscreen canvas at the internal
resolution (for example 320×180). Then copy it to the visible canvas, scaled by the largest
**integer** that fits, with `imageSmoothingEnabled = false` and CSS `image-rendering: pixelated`.
Letterbox the rest. Never draw sprites directly at fractional scales.

**Positions.** Simulate in sub-pixel floats if you like, but draw at `Math.round(x)`. Snap the
camera the same way, so sprites and tiles never shimmer against each other.

**Sprites without files.** Store sprites as rows of palette letters and decode each once into an
offscreen canvas **at native size**: one sprite pixel is one buffer pixel. Baking a sprite at 2×
into a 1× buffer creates mixels.

```js
const PAL = { k: "#1a1c2c", r: "#b13e53", o: "#ef7d57", y: "#ffcd75" };   // '.' = transparent
const COIN = ["..kkkk..", ".kyyyyk.", "kyyyyyok", ".kooook.", "..kkkk.."];   // light top-left, shade bottom-right
```

Keep one palette for the whole game, organised as ramps (see `gdd-art-direction` →
`references/pixel-art-craft.md`). Apply the drawing rules there: clusters instead of single-pixel
speckle, one light direction, an outline policy, no outer anti-aliasing.

**Text.** Use a tiny bitmap font drawn from the same kind of strings (the template has a 3×5
font). `fillText` anti-aliases, even at small sizes, and leaks colours that are not in the
palette. A pixel webfont must be thresholded to palette colours before it touches the buffer.

**The pixel contract test.** In `?test=1`, draw a representative frame (text, effects, a
fractional position), read the buffer with `getImageData`, and assert that every pixel is a
palette colour with full alpha. This one check catches anti-aliased text, smoothing, rotation,
alpha fades and sub-pixel drawing. Then audit the `?shot=1` screenshot:

```bash
python3 ../gdd-art-direction/scripts/pixel_audit.py audit screenshots/my-game.png --palette palette.hex
```

**Feel at low resolution.** Screen shake moves in whole pixels. Use flash frames with a
reserved color for hits, and short freeze frames (2–4 ticks) for impact. Particles are single
pixels or 2×2 squares.

## 3D prototypes (three.js)

**Library.** Load a **pinned** three.js build through an import map, for example version
0.160.0 from jsDelivr: `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js`.
Never load an unpinned "latest" URL. Note the network dependency in the report.

**Keep the simulation testable.** Game state (positions, velocities, collectibles, timers)
lives in plain objects updated by `step(dt)`. three.js meshes only **mirror** that state in
`sync()`. Tests and bots call `step()` without touching WebGL.

**Physics you can trust.** Use a fixed timestep (for example 1/120 s, accumulated) for
movement and collisions. Simple shapes (spheres, capsules, axis-aligned boxes, height
functions) cover most prototypes. Write a test for every collision rule.

**Camera.** Damped follow with look-ahead, a minimum distance, and occlusion handling (pull the
camera in, or fade blocking meshes). See `gdd-art-direction` → `references/3d-art-direction.md`.

**Look on a budget.** Flat or toon materials (`MeshToonMaterial`, `MeshLambertMaterial`), fog
matched to the sky color, one directional light plus hemisphere light, and a few shadow
casters. Vertex colors or tiny gradient textures beat large textures. Merge or instance
repeated props.

**Headless tests and screenshots.** Headless Chrome renders WebGL through a software
rasterizer. `scripts/check.py` passes the flags for it. If WebGL is unavailable, the page must
still run its `?test=1` logic tests and show a clear message instead of a blank screen.

**Performance check.** Log draw calls (`renderer.info.render.calls`) and triangles in
`?test=1`. Assert they stay under the budget written in the style guide.

## Sources
- [D16] Azzi, *Pixel Logic*; [D17] Medeiros (Saint11) tutorials; [D20] Haigh-Hutchinson, *Real-Time Cameras*.
- [D23] Pixel Joint, *The Pixel Art Tutorial*; [D25] Schlitter (SLYNYRD), *Pixelblog*; [D36] Sweetie 16 palette (GrafxKid).
- [A11] Swink, *Game Feel*; [A12] Jonasson & Purho, *Juice it or lose it*.
- Full bibliography: `research/SOURCES.md` in the repository.
