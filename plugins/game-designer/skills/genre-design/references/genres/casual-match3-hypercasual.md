# Casual, hypercasual and match-3

- **Casual:** low barrier, short sessions, broad audience (puzzle, word, solitaire,
  merge, decorate).
- **Hypercasual:** a single mechanic understood in seconds, ad-monetized, marketing-tested
  early.
- **Match-3 / saga:** level-based tile matching with goals, boosters, obstacles and meta
  layers (decoration, story).

## Core loop
- **Match-3:** start a level (goal, move limit) → match tiles → cascades and specials → meet
  the goal or run out of moves → stars and rewards → the next level on the map.
- **Hypercasual:** tap or swipe → an instant result → score or level → repeat (seconds).

## Signature mechanics
- Match-3: special tiles (line, bomb, color), **blockers** (obstacles that raise difficulty),
  move limits, boosters, lives or energy, map progression, meta decoration.
- Hypercasual: one-touch input, a satisfying physics or visual hook, very short levels.

## Pacing shape
Across levels, not within one. King's talks describe pacing difficulty across sequences
(an industry analysis found about one hard level in five, with the first hard level often
around level 10). Meta layers add longer arcs (renovation rooms, story chapters). Hypercasual
pacing: seconds-long loops with level-to-level novelty.

## Progression model
Level map progression, star collection, meta decoration, events. Hypercasual: level counter
and unlockable skins.

## Balancing levers
- Level difficulty: blocker types and density, move count, goal size, color count.
- Difficulty sequencing: hard and easy alternation, gate levels.
- King: a very hard level converted well but caused the most churn, and A/B tests showed an
  easier version kept players longer. Look at the effects on the whole progression.
- Booster economy and lives regeneration.
- Hypercasual go/no-go metrics. Voodoo's published targets moved from about 55% D1 / 22% D7 /
  CPI under $0.25 to about 45% D1 / 13% D7 / $0.20 CPI (2020), alongside playtime and
  marketability signals.

## Failure modes
- **Monetization-shaped difficulty:** levels tuned to sell boosters rather than to be fun.
  Players feel it.
- **Churn walls** at hard levels (A/B test easier variants).
- **Sameness:** new levels that reuse old ideas without new blockers or goals.
- **Ad fatigue** (hypercasual): ad frequency that drives uninstalls.
- **Fake-ad mismatch:** marketing a game that doesn't exist (deceptive, and it hurts retention).

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Candy Crush Saga | Huge level library with data-driven pacing; blockers create variety from one mechanic |
| Royal Match | Fast animations and a clear meta (castle renovation) |
| Two Dots | Minimalist visuals and a calm tone made match-style puzzles feel premium |
| Hypercasual hits (e.g. Helix Jump-style) | One verb, instant feedback, and a satisfying physics hook |

## Talks and postmortems
- King: *Blockers: Analyzing Difficulty Drivers in Candy Crush Games*; long-term difficulty
  tuning; level design pillars (difficulty, rhythm, flow, hooks).
- Voodoo: published hypercasual KPI targets and testing process.

## Design questions
1. What makes level N different from level N−1: a new blocker, goal or constraint?
2. Where are the hard levels, and what does churn look like right after them?
3. Is any level tuned to sell boosters rather than to challenge?
4. (Hypercasual) Does the hook read in a 3-second video with no sound?

## Sources
- [B25] King talks and coverage (secondary). · [B26] Voodoo (publisher blog and interview).
- [A26] GameAnalytics benchmarks.
- [A15] Zagal et al. (2013): dark patterns to avoid in monetized casual games.
- Full bibliography: `research/SOURCES.md` in the repository.
