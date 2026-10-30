# Scope estimation and asset lists

## Why scope kills indie games

Unfinished games teach less than finished small ones. Derek Yu, in interviews about
finishing, advises starting very small and releasing on time rather than polishing forever.
Scope problems come from content counts multiplying (characters × animations × variants),
features with hidden dependencies (save systems, localization, accessibility, platform
certification), and underestimating iteration.

## Content inventory (asset list)

List every asset family with counts and estimates. Use `templates/asset-list.csv`:

`id, category, name, description, pillar, priority, count, unit_hours, total_hours, owner, status, notes`

- **category:** character, enemy, environment, prop, VFX, UI, audio-sfx, audio-music, VO,
  animation, narrative, level, code-feature.
- **priority (MoSCoW):** `must` (core loop), `should` (core experience), `could`
  (polish/extra), `wont` (explicitly cut).
- **unit_hours:** hours per unit for the team's actual skill level. Measure one before you
  estimate many.
- **total_hours** = count × unit_hours.

## Estimation method

1. **Build one of each** asset family in the vertical slice and time it, including
   iteration and implementation.
2. **Multiply** by counts. Add an **integration factor** (×1.2–1.5) for importing, hookup and
   bug fixing.
3. **Add buffers:** +25–50% for unknowns in pre-production; +15–25% once production is stable.
4. **Compare with capacity:** team members × productive hours per week (≈ 25–30 h of focused work
   in a 40-hour week) × weeks.
5. **Cut by priority** until estimated hours ≤ 80% of capacity (keep slack for polish, bugs,
   marketing and certification).

## Hidden scope checklist

- [ ] Save/load and data migration
- [ ] Settings, input remapping, accessibility options
- [ ] Localization (text expansion, fonts, RTL), plus VO if any
- [ ] Platform requirements and certification (console), store pages, ratings
- [ ] Tutorials and onboarding
- [ ] Analytics and crash reporting
- [ ] Multiplayer: netcode, matchmaking, moderation, servers
- [ ] Marketing assets: trailers, capsule art, screenshots, press kit

## Genre appetite (rough guide)

| Appetite | Genres | Scope advice for small teams |
|---|---|---|
| Content-hungry | RPG, metroidvania, narrative, MMO | Small world, deep reactivity; reuse assets |
| Systems-hungry | Strategy, sim, roguelike, sandbox | Fewer assets, more design iteration; procedural content |
| Polish-hungry | Action, platformer, rhythm, fighting | Few levels or characters at very high quality |
| Live-ops-hungry | F2P, MMO, battle royale | Plan the content cadence before launch; it's a commitment |

## Sources
- [D4] Yu, interview on finishing games (secondary).
- [D3] Fullerton (2018), *Game Design Workshop*: production and prototyping.
- [D1] Librande (2010): documents scoped to the decision.
- Full bibliography: `research/SOURCES.md` in the repository.
