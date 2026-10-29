# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

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
