# Idle and incremental

Games where numbers grow, often while the player is away: clickers, idle tycoons,
incremental games with unfolding systems, and idle RPGs.

## Core loop
Earn currency (click or wait) → buy generators or upgrades → production rises → reach the
next milestone → unlock a new system → eventually **prestige** (reset for a permanent
multiplier) → progress faster through the same curve.

## Signature mechanics
- Generators with **exponential cost growth**. Pecorella's model: next cost =
  base × rate^owned, with rates typically 1.07–1.15.
- Production growing linearly with count, times multipliers (milestones, upgrades).
- Prestige resets with permanent multipliers.
- Offline progress, so returning feels like a reward.
- **Layered unfolding:** new mechanics revealed over time (Universal Paperclips, Cookie
  Clicker).

## Pacing shape
Fast early unlocks (seconds to minutes) → growth slows as exponential costs overtake
production → a **prestige moment** resets with a multiplier → the curve repeats faster. Each
prestige layer is a nested interest curve. The whole game is a series of slowdowns and
breakthroughs.

## Progression model
Exponential numbers on a log scale. Players feel progress through **multipliers and new
systems**, not through absolute numbers. Notation (K, M, B, scientific) becomes part of the
UI design.

## Balancing levers
- Cost growth rate per generator vs. production growth; the time to the next purchase.
- Milestone multipliers (e.g. ×2 at 25, 50, 100 owned).
- Prestige formula: currency earned on reset vs. lifetime earnings (often a root function).
- Offline earning rate and cap.
- Time-to-next-unlock targets per phase (use `progression_curve.py --curve exp`).

## Failure modes
- **The wall:** time to the next purchase stretches to hours with nothing new to do.
- **Prestige that doesn't feel faster:** the multiplier is too small.
- **No new decisions:** it's only "buy the cheapest". Add branching upgrades and layers.
- **Monetized waiting** (speed-ups) that leans on impatience. Disclose and keep it fair.
- **Number blindness:** big numbers without context. Show rates, time-to-goal and milestones.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Cookie Clicker | The genre template: a clear loop, milestone upgrades, humorous unfolding |
| AdVenture Capitalist | Clean generator math; managers automate clicking; prestige via angel investors |
| Universal Paperclips | Each phase reveals a new system and theme; the layers tell a story |
| Melvor Idle / idle RPGs | Idle mechanics wrapped around RPG skill progression for players short on time |

## Talks and postmortems
- Pecorella, *The Math of Idle Games*, Parts I–III (Kongregate), and *Quest for Progress*
  (GDC Europe 2016).

## Design questions
1. What is the target time-to-next-purchase in each phase, and when does the first wall hit?
2. How much faster is the second prestige run than the first? (Players expect a clear jump.)
3. What new system is revealed every N hours?
4. What does a returning player see first, and does it feel like a gift?

## Sources
- [B24] Pecorella (2016). https://www.gamedeveloper.com/design/the-math-of-idle-games-part-i
- [C2] Schreiber & Romero: exponential curves.
- Full bibliography: `research/SOURCES.md` in the repository.
