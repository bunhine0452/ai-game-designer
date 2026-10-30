# Tower defense

Place defenses along or around enemy paths to stop waves. Variants: fixed paths, mazing
(players build the path), lane defense (Plants vs. Zombies), hero-plus-towers, and
TD-roguelite hybrids.

## Core loop
Preview the wave → spend resources on towers or upgrades → watch the wave resolve (with
optional active abilities) → earn resources → adapt placement → harder wave.

## Signature mechanics
- Tower archetypes: single-target DPS, area damage, slow or control, support or buff,
  economy.
- Enemy archetypes that counter tower types: armored, fast, flying, swarm, splitting,
  shielded, boss.
- Placement constraints (grid, path, slots).
- Upgrade paths and branching specializations.
- An interest or economy mechanic (saving vs. spending).

## Pacing shape
Within a level: early waves teach → mid waves force adaptation (new enemy type) → the final
wave or boss is the climax. Planning phases are valleys and waves are peaks. Across the
campaign: a new tower or enemy every level or two, with challenge modes after.

## Progression model
New towers and enemies (horizontal) plus meta upgrades (vertical; keep them modest).
Plants vs. Zombies is a model for teaching: one new plant or zombie at a time, each level a
lesson, aimed at players who'd never played a strategy game.

## Balancing levers
- Cost curves: tower cost vs. DPS, range and utility (use `cost_curve.py`).
- Enemy HP and speed scaling per wave; spawn density.
- Resource income per kill and per wave; interest rates.
- Counter strength: how much armor reduces non-piercing damage.
- Leak tolerance (lives).

## Failure modes
- **Dominant tower or placement:** one setup clears everything.
- **Passive watching:** waves take long and offer no decisions during them. Add active
  abilities, speed-up, or mid-wave choices.
- **Unreadable failure:** the player doesn't know why enemies leaked.
- **Information overload** from too many towers at once.
- **Late-game unit spam** that hurts performance and readability.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Plants vs. Zombies | Deep teaching: each level adds one element, so non-gamers master a strategy game |
| Bloons TD series | Branching upgrade paths with distinct identities give many viable builds |
| Kingdom Rush | Hero units and active abilities keep players engaged during waves |
| Defense Grid | Mazing plus readable enemy pathing makes placement a spatial puzzle |

## Talks and postmortems
- Fan, *How I Got My Mom to Play Through Plants vs. Zombies* (GDC 2012): 10 techniques for
  teaching mechanics.
- Schreiber, *Game Balance Concepts*: cost curves for units and towers.

## Design questions
1. What does the player decide *during* a wave?
2. Which enemy type counters which tower, and is it previewed before the wave?
3. Is saving resources ever better than spending? When?
4. How many distinct winning setups exist on each map?

## Sources
- [B14] Fan (2012). https://gdconf.com/news/gdc_2012_reveals_plants_vs_zom
- [C1] Schreiber (2010). · [C2] Schreiber & Romero (2021).
- Full bibliography: `research/SOURCES.md` in the repository.
