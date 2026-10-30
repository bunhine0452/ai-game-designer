# Prototype structure (single-file HTML)

## Layout of the file

```
<head>  meta viewport · title · <style> with CSS variables for the palette
<body>  header (title + link to the design doc) · canvas and/or DOM panels · <pre id="selftest" hidden>
<script>
  1. data (tables copied from the design, with provenance comments)
  2. seeded RNG (mulberry32) · helpers
  3. state: one object S, created by fresh()
  4. rules: pure-ish functions that change S (no DOM access)
  5. rendering: draw() for canvas, ui() for DOM, both read S only
  6. input: event handlers call rules, then render
  7. selftest() and the ?test=1 / ?shot=1 entry points
  8. requestAnimationFrame loop
```

## Rules that saved the showcase prototypes

1. **One state object.** `let S = fresh();` holds everything. Tests reset with `S = fresh()`,
   and saves are `JSON.stringify(S)`.
2. **Logic never touches the DOM.** Rules record what should happen next
   (`S.pending = "reward" | "rest" | "win" | "loss"`), and the UI shows it. In the first
   Tidecaller draft, the fight logic opened the reward dialog directly, which crashed the
   headless bot. Recording a `pending` state fixed it.
3. **Rebuild DOM only when it changes.** `ui()` often runs every frame. Replacing a button
   list 60 times a second eats clicks, because the element under the mouse is gone by mouseup.
   Use:
   ```js
   const setHTML = (el, html) => { if (el._html !== html) { el._html = html; el.innerHTML = html; } };
   ```
4. **Seeded randomness.** Route every random call through `rng()`. Tests and `?shot=1`
   set `rng = seeded(N)` for repeatable runs.
5. **Event-precise time.** For economies, advance time to the exact moment something becomes
   affordable. Don't sample per frame. Offline settlement then equals online play (and you can
   test that).
6. **No browser dialogs.** `alert`/`confirm`/`prompt` block automation and feel cheap. Use an
   in-page overlay.
7. **Storage is optional.** Wrap `localStorage` in try/catch. Private windows and previews
   may throw.
8. **Canvas images from SVG need `xmlns`.** Inline SVG in HTML works without it, but a
   `data:image/svg+xml` image fails to draw silently. In Monster Farm the monsters were
   invisible until it was added.
9. **Scale canvas text for its display size.** A 960-px canvas shown at 670 px shrinks text
   by 30%. Size canvas fonts for the displayed size.

10. **Rules emit events; the presentation plays them back.** Rule functions push events
    (`hit`, `crest`, `draw`, `kill`) and return at once. The UI drains the queue with
    `await`ed delays, updating a separate view model from each event's payload. Bots run the
    same rules with events switched off. Split multi-actor phases into steps
    (`beginEnemyPhase`, `enemyAct(e)`, `finish`) so the screen can show each actor in turn.
11. **Keep a handle on what is on screen.** Rules often clear state at the end
    (`G.fight = null`). The last blow still has to animate, so keep a `SHOWN` reference
    for the duration of the playback.
12. **Previews run the real rules on a copy.** `structuredClone(state)`, stub the RNG, play,
    read the outcome, and restore. Then test that every preview equals the real result.

## Input and layout

- Keyboard plus pointer for every action. Touch: `touch-action: manipulation` on the canvas.
- Map pointer coordinates through `getBoundingClientRect()` and the canvas size, so the
  page works at any width.
- Prefer a fixed 1280×720 stage scaled with `transform: scale(k)` to fit the window. The
  composition then holds on every screen. Use body-colored bands for the letterbox and a
  "turn your phone sideways" hint for portrait phones.

## Sources

- Lessons from building the six prototypes in the repository's `games/` folder.
- [A11] Swink, game feel (responsiveness); [D7]/[D8] accessibility guidelines. Full
  bibliography: `research/SOURCES.md`.
