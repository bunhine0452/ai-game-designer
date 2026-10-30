---
name: playable-prototype
description: Turns game design documents into playable, testable browser prototypes. Produces a single-file HTML5 game whose numbers come straight from the design (cards, stats, curves, economy), with procedural placeholder art and sound, built-in self-tests (?test=1) including bots that play it start to finish, and automatic screenshots. Use when the user wants to prototype, greybox or make a design playable, build a vertical slice, turn a paper prototype into a digital one, test a core loop, share a playable demo, or build a quick game from a GDD, one-pager, beat list, card list or economy model. Includes pixel-art and 3D (three.js) templates. Hands production art and engine work to asset or engine tools. Also triggers on 프로토타입, 플레이 가능하게, 그레이박스, 데모 게임 만들기, 빠르게 만들어 보기; プロトタイプ, 遊べる試作, グレーボックス, デモ版; 原型, 可玩原型, 灰盒, 做个试玩版; prototipo jugable, demo jugable.
argument-hint: "[design document path or one-pager]"
license: MIT
compatibility: Any agent that reads SKILL.md folders. Scripts need Python 3; check.py also needs a local Chrome, Chromium or Edge.
metadata:
  author: bunhine0452
  version: "1.6.0"
  repository: https://github.com/bunhine0452/ai-game-designer
---

# Playable prototype

Turn a design into something people can play in five minutes, and prove that it matches the
design. The goal is not a finished game. It's the **cheapest playable test of the design's
riskiest assumption**, built so the numbers can be trusted and the result can be shared as a link.

**Language (required):**
- Answer in the language of the user's latest message.
- In a non-English answer, write **every** technical term the first time it appears as the
  localized term plus the English term in parentheses, e.g. `그레이박스 (Greybox)`,
  `자체 테스트 (Self-test)`, `プロトタイプ (Prototype)`, `原型 (Prototype)`. After that, use the
  localized term alone.
- Standard terms are in `references/glossary.md` if bundled, or `../game-design/references/glossary.md`.
- Game UI text follows the design's language. Offer an English toggle when the audience is broader.

## Workflow

1. **Find the design inputs.** Collect the documents: the brief or one-pager (pillars, core
   loop, risks), beat lists, card, unit or tower tables, economy configs, progression tables.
   If there are none, run the `game-design` workflow first (a provisional brief is enough).
2. **Pick the scope from the design itself.** Build the test the design names as its riskiest
   assumption (e.g. "a 2-week greybox: 6×6 field, 3 monsters, 3 days"). Cut everything else.
   One core loop, one session's worth of content, a clear end state. See `references/design-to-code.md`.
3. **Copy numbers verbatim, with provenance.** Put tables in the code as data, with a comment
   naming the source file and version ("cards: tidecaller-starter-v3.csv"). Never "improve" a
   number silently. If a value is missing, choose one, mark it `// placeholder`, and list it in
   your answer.
4. **Start from the template.** Copy `assets/template.html` (or `template-pixel.html` /
   `template-3d.html`; see `references/3d-and-pixel-prototypes.md`). It already has the contract: a
   single state object, a seeded RNG, logic separate from UI, change-only DOM updates, and the
   `?test=1` / `?shot=1` hooks. Structure rules: `references/prototype-structure.md`.
5. **Make the pillars visible.** Every pillar becomes a mechanic or UI element you can point
   to (e.g. "no failure, only detours": crops pause instead of dying; "transparent odds": the
   odds table is always on screen). Run the `design-review` ethics checks on any monetization
   in the prototype. Use free currency only, and don't simulate real-money purchases.
6. **Write the self-tests with the game,** not after it:
   - *fidelity*: formulas and tables equal the design numbers (e.g. "chapter 1 = 41.4 min");
   - *rules*: invariants of the core loop (crest at 10 resets to 5; prune refunds 80%);
   - *bots*: a simple policy plays the whole session to an end state, many seeds, no errors;
   - *balance probes*: report the bot's outcome (win rate, resources left) as information.
   Details and pitfalls: `references/testing-and-bots.md`.
7. **Make it look and feel like a game, not a dashboard.** Clear the presentation bar in
   `references/assets-and-feel.md` before you call it done. Then add art and sound that respect the art direction: Procedural SVG/canvas
   shapes following the style guide's shape language and palette; WebAudio tones for key
   events; captions for every sound cue. See `references/assets-and-feel.md`. For production
   art, hand off to asset tools (e.g. an image or canvas-design skill, an engine plugin).
8. **Verify, screenshot, share.**
   ```bash
   python3 scripts/check.py path/to/games/        # every game: self-tests + screenshot
   python3 scripts/check.py my-game/index.html --no-shot
   ```
   It runs headless Chrome with a throwaway profile, reads `<pre id="selftest">`, and saves
   `screenshots/<name>.png` from the `?shot=1` state. Look at every screenshot before
   reporting. If the user wants a link, GitHub Pages serves the files as-is (add `.nojekyll`).
9. **Report:** what was built and the assumption it tests, the source of each number,
   placeholders, test results (with the bot outcomes), the screenshot, how to play, and the
   next playtest question with a pass criterion.

## Output contract (every prototype)

- One `index.html`, no build step, no external scripts (fonts optional). Works at phone width.
- Header line linking the design document it implements.
- `?test=1` writes JSON `{game, pass, results:[{name, pass, info}]}` into `<pre id="selftest">`
  and sets `document.title` to `SELFTEST PASS|FAIL`.
- `?shot=1` builds a deterministic, representative mid-game state for the screenshot.
- Optional storage wrapped in try/catch; the game works without it.
- Screen-first layout: a fixed 16:9 stage scaled to fit the window, with the play space as the
  hero. No sidebar of stat text. Numbers live on the units, cards and diegetic gauges.
- Accessibility: keyboard and pointer input, captions for audio cues, a reduce-flashing option
  when anything flashes, readable text sizes, no color-only signals.

## Principles

- **Fidelity over flourish.** A prototype that quietly changes the design's numbers tests
  nothing. Show the numbers, cite them, test them.
- **The bot is your first playtester.** If a scripted player can't finish, a human won't. If
  it wins easily with no thought, the challenge is missing.
- **Decouple logic from the screen.** Game rules record outcomes (`pending = "reward"`), and
  the UI decides how to show them. That one rule makes bots and tests possible.
- **Original work only.** Prototype the user's design. Use reference games as lessons, never
  as assets, names or layouts to copy.
- **Fidelity is the floor, not the bar.** Correct numbers in a stat-dump UI still read as
  "terrible" to players. Ship one polished loop rather than six greyboxes.
- **Playtest in a real browser.** Click through every screen with the mouse before you report.
  Headless tests and screenshots miss hover, timing and end-of-fight bugs.
- **Small and finished beats big and broken.** End the session cleanly (a win, a summary,
  "the demo ends here") so testers can say what they felt.

## References

- `references/design-to-code.md`: from documents to scope and data; genre starter patterns.
- `references/prototype-structure.md`: single-file architecture, state, rendering, input.
- `references/testing-and-bots.md`: self-test categories, bot design, real pitfalls found.
- `references/assets-and-feel.md`: procedural art, WebAudio, juice, captions, hand-off.
- `assets/template.html`: starter file with the full contract. `template-pixel.html` (integer-scaled
  pixel pipeline, palette sprites, BFS bot) and `template-3d.html` (pinned three.js, fixed-step
  simulation separate from rendering, draw-call budget test).
- `references/3d-and-pixel-prototypes.md`: pixel rendering pipeline and feel; three.js setup, physics, camera and headless WebGL tests.
- `scripts/check.py`: headless self-test runner and screenshotter.
- `examples/README.md`: six live prototypes built with this workflow, and what each demonstrates.
