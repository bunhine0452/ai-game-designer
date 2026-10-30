# AGENTS.md

Guidance for AI coding agents (Codex, Copilot, Cursor, Antigravity, Gemini CLI, Claude Code
and others) working **in this repository** or **with these skills**.

## What this repo is

Six Agent Skills for game design in `skills/<name>/SKILL.md` (the open SKILL.md format):

| Skill | Use it for |
|---|---|
| `game-design` | Entry point: design briefs, pillars, core loops, MDA; routes to the others |
| `fun-curve` | Interest curves, pacing, flow, difficulty, game feel |
| `genre-design` | 26 genre playbooks and hybrid-genre design |
| `balance-economy` | XP curves, combat math, cost curves, economies, drop rates, gacha and pity |
| `gdd-art-direction` | One-page designs, GDDs, feature specs, asset lists, art and audio direction, accessibility |
| `design-review` | Critiques of concepts, specs, builds and playtest notes, with a dark-pattern ethics pass |

## Using the skills from an agent without native skill support

1. Read the `description` in each `skills/*/SKILL.md` frontmatter and pick the skill that
   matches the user's request (start with `game-design` if unsure).
2. Read that `SKILL.md` fully and follow its workflow. Open files in its `references/` only
   when the workflow points to them.
3. Run the bundled scripts with Python 3 instead of estimating numbers:
   `skills/fun-curve/scripts/fun_curve.py`, `skills/balance-economy/scripts/progression_curve.py`,
   `economy_sim.py`, `cost_curve.py` (each has `--help`).
4. Answer in the user's language. In non-English answers, write each technical term on
   first use as `localized (English)`. See `skills/game-design/references/glossary.md`.

## Installing into an agent

```bash
./install.sh                                   # ./.agents/skills (read by Codex, Gemini CLI, Antigravity...)
./install.sh --agent claude --scope user       # ~/.claude/skills
./install.sh --list-agents                     # all known targets
```

Native packages also exist: `.claude-plugin/` (Claude Code), root `plugin.json` plus
`.codex-plugin/` and `.agents/plugins/marketplace.json` (Codex), `gemini-extension.json`
(Gemini CLI). Antigravity can install the repo as a plugin directly.

## Working on this repo

- Keep each `SKILL.md` body under about 2,000 words; put depth in `references/`. Descriptions
  stay under 1,024 characters.
- Every reference file ends with `## Sources` citing IDs from `research/SOURCES.md`.
  Paraphrase; never copy copyrighted text verbatim.
- Scripts use the Python 3 standard library, with matplotlib optional. Without matplotlib
  they must still write text and CSV output.
- Examples use original, fictional games. Never add clones of existing games.
- Before committing: `claude plugin validate .` (or your agent's validator), run the scripts on
  `skills/*/examples/`, and `python3 tools/package.py`.
- Commit style: `<type>(<scope>): <description>` (feat, fix, docs, test, chore, refactor).
