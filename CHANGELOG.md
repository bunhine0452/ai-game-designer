# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

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
