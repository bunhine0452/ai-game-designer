# Contributing

Thanks for helping make game design knowledge more accessible. Contributions of every size are
welcome.

## Good first contributions

- **Glossary fixes** by native speakers (`skills/game-design/references/glossary.md`), or a
  new language column.
- **Better sources** for weakly sourced areas (racing, battle royale, party games,
  metroidvania, puzzle). Primary sources are preferred: talks, postmortems, papers, designer
  blogs.
- **New worked examples** (a beat list, an economy config, a review), with the script outputs.
- **Genre playbook improvements**, following the fixed section template.

## Rules

1. **Cite everything.** Add new sources to `research/SOURCES.md` with an ID and a trust level
   (P/S/L), and reference that ID in the file's `## Sources` section.
2. **Paraphrase.** Don't copy text verbatim from copyrighted books, talks or articles. Short
   quotes need attribution and must be necessary.
3. **Keep skills lean.** A `SKILL.md` body stays under about 2,000 words; deep knowledge goes in
   `references/`. Descriptions stay under 1,024 characters and include trigger phrases in
   several languages.
4. **Scripts:** Python 3 standard library only, with matplotlib optional. They must still
   produce text or CSV output without matplotlib, and run against the bundled examples.
5. **Originality:** examples use original, fictional games. Don't add clones of existing games.
6. **Ethics:** guidance must never help design manipulative monetization. Healthy
   alternatives are always welcome.

## Before opening a pull request

```bash
claude plugin validate .                     # Claude Code manifests and skills
agy plugin validate . && gemini extensions validate .   # other agents, if installed
python3 skills/fun-curve/scripts/fun_curve.py skills/fun-curve/examples/roguelite-20min-run.csv --out /tmp/fc
python3 skills/balance-economy/scripts/economy_sim.py skills/balance-economy/examples/f2p-economy.json --out /tmp/eco
python3 skills/playable-prototype/scripts/check.py games/   # game self-tests + screenshots
python3 tools/package.py                     # builds dist/ (plugin + per-skill zips)
claude plugin eval . --runs 1                # optional: multilingual trigger evals
```

Use conventional commits: `feat(scope): …`, `fix(scope): …`, `docs(scope): …`.

## Code of conduct

Be kind, assume good intent, and critique ideas rather than people.
