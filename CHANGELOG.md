# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

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
