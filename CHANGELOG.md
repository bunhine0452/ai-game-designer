# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

## [1.10.0] - 2026-10-31

### Added
- **Pixel art craft** (gdd-art-direction): `references/pixel-art-craft.md`, the theory behind pixel
  art that reads as crafted. It covers clusters and noise, line steps and jaggies, banding and
  pillow shading, light, form and projection, anti-aliasing and sel-out, hue-shifted ramps with
  even perceptual steps, dithering, texture, tiles and autotiling, animation (key poses, holds,
  sub-pixel), production at scale, and AI-generated pixel art, plus a 12-item defect checklist
  ordered by visibility (sources D23–D36).
- **`pixel_audit.py`** (gdd-art-direction):
  - `audit` finds the scale of a sprite, an integer-scaled screenshot or an upscaled AI image,
    and follows grids that drift. It flags MIXELS, NON_INTEGER_SCALE, AI_OR_RESAMPLED,
    OFF_PALETTE, TOO_MANY_COLORS, SIMILAR_COLORS, NOISE_PIXELS, LOW_VALUE_RANGE, EYEBURN,
    MELTS_INTO_BG and SOFT_ALPHA, each with a fix.
  - `fix` turns AI-made "pixel art" into a native-size PNG on a real grid and palette. On game
    art degraded on purpose it recovered 96% of pixels (nearest 4× + JPEG), 93% (bicubic 5.7× +
    JPEG) and about 80% (bilinear 3.3× + JPEG, with `--size`).
  - Standard library only; Pillow speeds up reading and adds JPEG.
- **`palette_ramp.py`** (gdd-art-direction):
  - `ramp` builds hue-shifted ramps in OKLCh: even lightness, warm lights, cool shadows,
    saturation peaking mid-ramp.
  - `check` flags straight ramps, uneven value steps, near-duplicates, eye-burning colours and
    value gaps.
  - Exports `.gpl`, `.hex` and swatch PNGs.
- `examples/pixel/`: an AI-like image audited and repaired (93% of pixels recovered), with a
  palette check and a generated ramp.

### Changed
- **Pixel template** (playable-prototype): sprites are now drawn at native size (the old 2× bake
  produced mixels). Text uses a 3×5 bitmap font instead of anti-aliased `fillText`. The palette
  is organised as Sweetie 16 ramps. A new **pixel contract** self-test asserts that a drawn frame
  holds palette colours only, and the hero must stand out from the floor in greyscale.
- `pixel-art-direction.md`: projection, outline, anti-aliasing and dithering policies, and a
  checks section for screenshots and AI-generated assets.
- **Dot Gardener:** random single-pixel speckle on wall tops, floors and rubble is replaced by
  small clusters lit from the top-left, with empty stone between them. The bloom's stone colour
  is pushed apart from the base one so the change reads (the audit flagged the pair as
  near-identical). A pixel-contract frame test was added (14 self-tests).

## [1.9.0] - 2026-10-30

### Added
- **Fun hypothesis** (game-design): the design brief now states what players will want to find
  out, how often it resolves, what makes it felt and for whom, and the next step is the smallest
  toy with keep / pivot / kill thresholds written before anyone plays. `frameworks.md` has the
  template and the loop.
- **The common thread** (fun-curve): `what-makes-it-fun.md` opens with the unifying account
  (uncertainty resolved faster than expected, times the sensory, social and meaning layers).
- **Anti-fun screen** (playable-prototype): a standard set of bot checks for every prototype's
  `?test=1`: beatable, not trivial, no dominant option, outcome in doubt, decisions and questions
  keep coming. `template.html` demonstrates two of them.
- **Free-choice play and A/B comparisons** (design-review): `free_play` and `prefer` events;
  `playtest_report.py` reports both, with an exact sign test for two-way comparisons, and flags
  `LOW_FREE_PLAY`.
- **Curiosity gaps** (fun-curve): an optional `new` column and curiosity beat types;
  `fun_curve.py` flags `CURIOSITY_GAP` when nothing new arrives for over 30% of the run before
  the climax (`--curiosity-gap`). Beat lists without these markers report as before.
- `research/FUN_DEEP_DIVE.md`: why fun is hard to design, predict and measure (sources A48–A68).

## [1.8.0] - 2026-10-30

### Added
- **What makes it fun** (fun-curve): `references/what-makes-it-fun.md` collects experiments and
  large datasets on enjoyment: enjoyable challenge, outcome uncertainty and suspense, curiosity
  and uncertain success, the optimal juice dose, need satisfaction *and* frustration (BANGS),
  motivation quality vs. hours played, the mixed evidence on hidden difficulty adjustment,
  social play, meaningful choice and meaning. Each comes with an evidence-strength rating and
  design rules.
- **Fun diagnosis** (design-review): `references/fun-diagnosis.md` scores eight fun drivers
  separately, finds the bottleneck and writes fixes as testable predictions.
- **Playtest kit:** `outcome` (final margin) and `explore` (optional action) events, and three
  questionnaire items (`curious`, `challenge`, reversed `pressure`). `playtest_report.py` adds a
  fun-driver table and the flags `ONE_SIDED`, `LOW_CURIOSITY` and `PRESSURE`. Logs without the
  new events report exactly as before.
- **Ethics:** "Engagement is not fun", based on the Oxford telemetry study.
- Sources A32–A47. Items checked only at the abstract level or through secondary coverage are
  marked and listed under research gaps.

## [1.7.0] - 2026-10-30

### Added
- **Pixel art and 3D art direction** (gdd-art-direction): `pixel-art-direction.md` (integer-scaled
  canvas, palette ramps and reserved colours, clean lines and outlines, animation frames and timing,
  tiles and bitmap fonts, scope math) and `3d-art-direction.md` (finishable styles, polygon,
  texel and draw-call budgets, player metrics, camera rules, landmarks and wayfinding, colour
  scripts). Sources D16–D22.
- **Pixel and 3D prototypes** (playable-prototype): `template-pixel.html` (320×180 integer
  pipeline, palette sprites, a BFS bot), `template-3d.html` (pinned three.js, fixed-step
  simulation separate from rendering, a draw-call budget test) and
  `references/3d-and-pixel-prototypes.md`. `check.py` now enables SwiftShader so WebGL renders
  in headless Chrome.
- **Showcase sessions 07 and 08**: a 3D gliding delivery game (Korean) and a pixel-art garden
  puzzle (Japanese), both real Claude Code runs with the plugin.
- **Two games built from them**: *Kite Post* (three.js; its autopilot flies all eight deliveries
  inside their target times) and *Dot Gardener* (pixel art; a breadth-first solver proves every
  room, that every seed is needed, and both endings of the last room).

## [1.6.0] - 2026-10-30

### Added
- **Workflow commands** (Claude Code): `/game-designer:new-game`, `balance-check`, `ship-check`
  and `prototype` chain the skills into common workflows.
- **Subagents:** `design-critic` (independent review) and `economy-auditor` (runs the
  simulators and reports exact numbers).
- **`export_engine.py`** (balance-economy): turns a final design table into Godot (Resource and
  loader), Unity (Serializable row and ScriptableObject), Unreal (USTRUCT and DataTable CSV) or
  typed JSON, with provenance. Adds `references/engine-handoff.md`.
- **Playtest kit** (design-review): `playtest_report.py` (funnel, difficulty spikes, drop-off,
  quit clusters, questionnaire means), `references/playtest-kit.md` and an example log.
- **`game-design-charts`**, an optional marketplace plugin: a standard-library MCP server
  (`interest_curve`, `gacha_odds`) that renders interactive charts in hosts that support MCP
  Apps and returns exact text everywhere.
- Agent Skills `license`, `compatibility` and `metadata` fields, plus `argument-hint`, on every
  skill.
- The README reports the with/without-plugin ablation over 21 cases: mean score 0.984 vs 0.778.

### Notes
- Submitted to the Claude plugin directory. One automated policy hold remains for reviewer
  confirmation: a heuristic reads the word "pass" (as in "ethics pass") as a credential.

## [1.5.0] - 2026-10-30

### Changed
- **The plugin now lives in `plugins/game-designer/`.** The folder holds the skills, the
  research, the evals, and the manifests for Claude Code, Codex, Antigravity and Gemini CLI. The
  repo root keeps the marketplaces, docs, games and showcase. Installs are now lean (about 150
  files instead of the whole repo), and the Claude plugin directory scans only the plugin.
- Both marketplaces (`.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`)
  point at the new folder, so the install commands are unchanged. Antigravity and Gemini CLI now
  install from `./ai-game-designer/plugins/game-designer`.
- Example charts moved to `docs/images/examples/`, and the walkthroughs link to them. The
  scripts still write charts to `examples/output/`, but those files are git-ignored.
- `tools/install.py` and `tools/package.py` read from the new folder. The plugin zip now
  contains only the plugin.

### Added
- A listing README for the plugin folder, with example prompts and a disclosure of what the
  plugin runs.

## [1.4.1] - 2026-10-30

### Added
- `PRIVACY.md` and a "What it runs, sends, and fetches" section in both READMEs, plus
  `displayName`, `documentationUrl`, `supportUrl` and `privacyPolicyUrl` in the plugin
  manifest, for the Claude plugin directory listing.

## [1.4.0] - 2026-10-30

### Changed
- **All six games rebuilt to the Tidecaller bar.** Each now has an illustrated scene as the
  hero, animation and feedback, synthesized sound, and title, play and end screens, with the
  design numbers and rules unchanged:
  - **Garden Guardians:** painted garden and plants, animated pests, projectiles, pollen
    threads, and a hover preview of range and pollination.
  - **Stardust Mine:** five painted planets, multiplying rigs, ore streaming to an orbiting
    hauler, warp transitions, and English/中文.
  - **Hoshiyobi Island:** an aurora shrine, sixteen individually drawn creatures, plain
    flip-card reveals, and English/日本語.
  - **Monster Farm:** a cozy farm with four animated monsters, day light, letter-style reports,
    and Korean/English.
  - **Low Tide:** dynamic lighting in a camera-followed lighthouse, spatial audio, a minimap, and
    touch controls.
- Self-tests grew from 66 to 81 across the six games, with render, translation and preview checks.

## [1.3.1] - 2026-10-30

### Changed
- **Tidecaller rebuilt** to a real demo standard. It now has an illustrated moonlit sea and a
  diegetic tide pole whose water line is the gauge, illustrated enemies with idle, hit and death
  animations, and a painted vignette on each of the 24 cards. Hovering a card previews the
  damage and where the water lands. Big moments get a crest wave, slack ripples and an eclipse
  for the boss. It adds synthesized sound and title, route, reward, rest and end screens, plus
  coach tips and keyboard play. Rules and numbers are unchanged. There are 16 self-tests,
  including a check that the preview matches the real play in 240 of 240 random states.
- `playable-prototype` skill: adds a presentation bar (screen-first stage, diegetic gauges,
  illustrated units and cards, previews, feedback, a loop of screens, real-browser playtests)
  and the event-playback architecture, after the first builds passed every test but looked
  like dashboards.

### Fixed
- Tidecaller: an enemy defeated by a Crest mid-turn no longer acts later in the same
  enemy phase.

## [1.3.0] - 2026-10-30

### Added
- Seventh skill, **`playable-prototype`**: turns design documents into single-file browser
  prototypes. Numbers are copied verbatim with provenance, logic is decoupled from the UI, and
  every prototype has `?test=1` self-tests (fidelity, rules, bots, balance probes) and a
  `?shot=1` screenshot state. It ships a starter template, a cross-platform headless-Chrome runner
  (`scripts/check.py`) and the six live games as examples. It distills what worked, and the
  bugs we hit, while building `games/`.
- Router route, eval cases (EN/KO/JA) and README rows for the new skill.

### Changed
- `games/tools/check.py` moved to `skills/playable-prototype/scripts/check.py` and was
  generalized (any folder or HTML file; finds Chrome, Chromium or Edge on macOS, Linux or Windows).

## [1.2.0] - 2026-10-30

### Added
- `games/`: six original, playable browser prototypes built from the showcase design documents:
  Monster Farm, Tidecaller, Hoshiyobi Island, Low Tide, Garden Guardians and Stardust Mine. Each is
  a single HTML file with procedural art (and sound in Low Tide), uses the design docs' numbers,
  and ships self-tests (`?test=1`) including bots that play it start to finish. There is an
  arcade gallery at `games/index.html`, served by GitHub Pages.
- `games/tools/check.py`: runs every game's self-tests and captures screenshots with headless
  Chrome, using a throwaway profile.
- New visual identity, "Measured Wonder": `docs/design/banner-philosophy.md`, a reproducible
  `docs/design/make_banner.py`, a new README banner and a 1280×640 social preview image.

## [1.1.0] - 2026-10-30

### Changed
- Renamed the repository to **ai-game-designer** (was `claude-game-designer`). GitHub redirects
  the old URL. The Claude Code marketplace is now `ai-game-designer`, so install with
  `/plugin install game-designer@ai-game-designer`.
- Skill text is agent-neutral. The icon moved to `assets/icon.png`.

### Added
- **Works beyond Claude.** Native packages for OpenAI Codex (root `plugin.json` in the Agent
  Plugins format, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`), Gemini CLI
  (`gemini-extension.json`) and Antigravity (validated with `agy plugin validate`).
- `install.sh` / `tools/install.py`: install the skills into `.agents/skills` (shared path read
  by Codex, Gemini CLI and Antigravity) or into Claude Code, Codex, Gemini CLI, Cursor, Copilot
  or OpenCode directories, at project or user scope, by copy or symlink.
- `AGENTS.md`: instructions for any agent working in the repo or using the skills without native
  support.
- `showcase/`: outputs from six real sessions run in parallel across Claude Code, Codex and
  Antigravity in five languages.
- `economy_sim.py`: optional `featured` (rate-up share, with a guarantee after a lost 50/50) and
  `spark` (the featured item is guaranteed within N pulls) gacha settings. It computes the exact
  featured-item distribution, checked against a 100k-run Monte Carlo, and the featured CDF appears
  on the pity chart. Found in real use (showcase session 03).

### Fixed
- `NO_HARD_PITY` became `NO_CEILING`, which counts a spark or a 50/50 guarantee as a ceiling.
  This removes a false warning on spark-based designs.
- `progression_curve.py --curve all` skips a family that can't reach the target total, with a
  note in the report, instead of aborting the whole comparison.

## [1.0.0] - 2026-10-30

### Added
- Six skills: `game-design` (router), `fun-curve`, `genre-design`, `balance-economy`,
  `gdd-art-direction`, `design-review`.
- 26 genre playbooks plus a hybrid-genre method.
- Scripts (Python 3 stdlib, optional matplotlib):
  - `fun_curve.py`: interest-curve plotting and pacing diagnostics.
  - `progression_curve.py`: XP tables for linear, polynomial, exponential and logistic curves,
    with shape solving and play-time conversion.
  - `economy_sim.py`: Monte Carlo faucet/sink/gacha simulation with exact pity distributions.
  - `cost_curve.py`: least-squares cost curves with robust outlier detection.
- Worked examples: a roguelite run, a horror pacing fix, an RPG XP table, an F2P economy fix,
  a card cost curve, a design brief, a hybrid genre brief, a one-page GDD with a scope check,
  and a monetization review.
- Multilingual behavior and a 130+ term glossary (EN, KO, JA, ZH-Hans, ES).
- Research notes and a 120+ entry bibliography with trust levels.
- Claude Code marketplace manifest, a packaged `.plugin`, and per-skill zips for the Claude app.
- 18 multilingual trigger evals for `claude plugin eval`.
