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

**Sprites without files.** Store sprites as strings of palette indices and decode them once
into offscreen canvases:

```js
const PAL = ["", "#1a1c2c", "#5d275d", "#b13e53", "#ef7d57", "#ffcd75"];   // index 0 = transparent
const HERO = ["..11..", ".1551.", "155551", ".1441.", "..11.."];              // '.' or '0' = transparent
```

Keep one palette for the whole game, and check the art against the style guide (ramps,
reserved colors).

**Text.** Use a tiny bitmap font drawn from the same kind of strings, or a pixel webfont at
integer sizes only.

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
- [A11] Swink, *Game Feel*; [A12] Jonasson & Purho, *Juice it or lose it*.
- Full bibliography: `research/SOURCES.md` in the repository.
