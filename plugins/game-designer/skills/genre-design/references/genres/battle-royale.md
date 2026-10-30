# Battle royale

Many players (often 50–150) drop into a shrinking map, loot gear and fight until one player
or squad remains.

> **Sourcing note:** few primary designer talks were retrieved. Guidance combines general
> competitive-design principles with secondary coverage of well-known features (contextual
> ping). Validate with playtests.

## Core loop
Drop (choose a landing spot) → loot quickly → rotate with the zone → fight or avoid →
heal and reloot → final circles → win or spectate, then requeue.

## Signature mechanics
- A shrinking safe zone (circle) as the pacing engine.
- Random loot distribution and rarity tiers.
- Landing choice as the first strategic decision (hot drop vs. quiet).
- Squad play: revives, respawn beacons, **contextual pings**. Apex Legends' ping system let
  random teammates coordinate without voice; it was tested with voice chat off.
- Third-partying and positional play.

## Pacing shape
Hot-drop peak → looting valley → rotation tension → sporadic fights → final circles (rising
climax). Most players die early, so the *average* curve is front-loaded. Fast requeue and a
rewarding early game matter.

## Progression model
Account levels, battle passes, cosmetics, ranked tiers. In-match gear progression resets
every game.

## Balancing levers
- Circle timing, damage, and the number of players alive per phase.
- Loot density and rarity by area (hot zones vs. edges).
- TTK (long TTK allows third-party escapes; short TTK rewards first shot).
- Mobility tools vs. the circle.
- Matchmaking skill bands.

## Failure modes
- **Dead time:** long looting or travel with no decisions or encounters.
- **Early-death frustration:** most players lose within minutes. Make early matches fun and
  requeue instant.
- **Loot RNG deciding fights.**
- **Unclear spaces:** sound and sightlines can't be read at range.
- **Cheating and performance** at a 100-player scale.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| PUBG | Established the core formula: drop, loot, circle |
| Fortnite | Building adds expressive mobility and defense; constant live events refresh the map |
| Apex Legends | Hero abilities plus contextual ping make squad play with strangers work |

## Design questions
1. What does the player decide in the first 60 seconds?
2. How long is the longest stretch without an encounter or decision?
3. What does a player who dies in minute 3 get from the match?
4. How do teammates communicate without voice?

## Sources
- [B32] Apex Legends ping system coverage (secondary).
- [B7] Sirlin: viable options. · [A22] *Game Analytics*: session and death telemetry.
- Full bibliography: `research/SOURCES.md` in the repository.
