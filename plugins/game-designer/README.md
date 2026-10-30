# AI Game Designer

Research-backed game design skills for every genre. Seven skills work like a senior game
designer at your side, and they answer in your language (Korean, Japanese, Chinese, Spanish,
English and more), with the English term in parentheses the first time a concept appears.

| Skill | What it does |
|---|---|
| `game-design` | Entry point. Turns an idea into a design brief: player fantasy, pillars, core loops, MDA analysis, risks. Routes to the other skills. |
| `fun-curve` | Plots and diagnoses interest curves and pacing (flow, difficulty, tension and release, onboarding, game feel), with the evidence on what players actually enjoy. |
| `genre-design` | 26 genre playbooks with conventions to honor and to break, plus hybrid-genre design. |
| `balance-economy` | XP and progression curves, combat math, cost curves, faucets and sinks, drop rates, and exact gacha and pity math, with simulators. |
| `gdd-art-direction` | One-page designs, GDDs, feature specs, asset lists, art and audio direction, accessibility checklists. |
| `design-review` | Structured critiques of concepts, specs, builds and playtest notes, a fun diagnosis across eight drivers, and an ethics pass for dark patterns. |
| `playable-prototype` | Turns design documents into single-file browser prototypes with self-tests, bots and screenshots. |

## Commands (Claude Code)

`/game-designer:new-game <idea>`, `/game-designer:balance-check <file>`,
`/game-designer:ship-check <doc>` and `/game-designer:prototype <doc>` chain the skills into
common workflows. The `design-critic` and `economy-auditor` subagents give an independent review
and exact simulator numbers.

## Try it

- "I have an idea for a cozy farming game where monsters change the land. Make it a design brief."
- "Here are my horror level beats with intensities. Plot the interest curve and tell me where it sags."
- "Design a gacha banner with a pity system, then calculate the exact cost to get the featured unit."
- "Review my monetization plan and flag any dark patterns."
- "Turn this one-pager into a playable browser prototype with tests."

## What it runs, sends, and fetches

- **Skills** are Markdown instructions. They don't execute anything by themselves.
- **Python scripts** in `skills/*/scripts/` run only when you or your agent call them. They use
  the Python standard library (matplotlib is optional, for charts), read only the files you pass,
  write to the output folder you choose, and make **no network requests**.
- **`skills/playable-prototype/scripts/check.py`** starts your locally installed Chrome, Chromium
  or Edge in headless mode with a throwaway profile, to run a prototype's self-tests and take a
  screenshot, then deletes the profile.
- **No hooks, no MCP servers, no telemetry, no data collection.** See [PRIVACY.md](PRIVACY.md).

## Learn more

Sources for every reference are in `research/`. The full documentation, six real sessions in
four languages, and six playable games built with these skills are on GitHub:
https://github.com/bunhine0452/ai-game-designer

Support and bug reports: https://github.com/bunhine0452/ai-game-designer/issues ·
License: MIT
