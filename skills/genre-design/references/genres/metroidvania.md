# Metroidvania

A connected, non-linear world explored by gaining abilities that open previously blocked
paths. Often mixed with action-platformer combat and RPG stats.

## Core loop
Explore → hit a barrier you can't pass yet (remember it) → find an ability or key item →
backtrack, with the new ability changing how known spaces work → open new areas → repeat.

## Signature mechanics
- **Ability gating:** movement abilities (double jump, dash, grapple, wall cling) double as
  keys. *Gate ordering* is the sequence in which they unlock regions.
- Interconnected map with shortcuts, fast travel and save rooms.
- A map screen as a core UI (markers, uncovered rooms, item icons).
- Secrets: breakable walls, hidden rooms, optional bosses.
- Sequence breaking: skilled players skipping gates, sometimes on purpose.

## Pacing shape
Large-scale arcs from ability to ability: each new ability is a peak, followed by an
exploration "re-read" of old areas (a valley of discovery), then a boss. The middle risks
sagging when backtracking turns into chores. Late game, the world opens up, with more
freedom and higher stakes.

## Progression model
Ability progression (new verbs) is primary. Stat upgrades (health, damage) and collectibles
are secondary. The ideal: every ability changes **both** traversal and combat.

## Balancing levers
- Distance between gates and the abilities that open them (memory load).
- Backtracking cost: fast-travel density, shortcuts opened on return.
- Map information: how much is auto-marked vs. left for the player to remember.
- Optional-content difficulty vs. reward.
- Combat difficulty per region, given that the player may arrive in different orders.

## Failure modes
- **Lost and frustrated:** no hint of where to go next, and no memorable landmarks.
- **Backtracking as busywork:** returning to old areas with nothing new to do.
- **Abilities that only open doors** and add nothing to combat or movement.
- **Soft-locks and dead ends** with no reward.
- **Scope:** a hand-made, interconnected world is content-heavy and hard to change late.

Research on backtracking prototypes suggests that returning feels like *reinterpreting*
familiar space, not retracing it, when the function of the new ability is clear,
environmental cues are consistent, and the main route stays understandable.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Super Metroid | Environmental storytelling and visible but unreachable items create curiosity without text |
| Hollow Knight | Buying maps from a cartographer and needing a quill turns navigation into a game; a huge world held together by landmarks |
| Ori and the Blind Forest | Movement abilities chain into flowing traversal, so backtracking feels like a victory lap |
| Gato Roboto | Familiar abilities with a twist (rockets on a cooldown instead of ammo) keep a small scope fresh |

## Talks and postmortems
- Backtracking and multi-mode abilities: Chalmers MSc thesis (2026).
- Gato Roboto designer Q&A (Game Developer).
- *Note:* primary GDC talks on Hollow Knight and Ori weren't retrieved in this research pass
  (they're mostly behind GDC Vault logins), so guidance here rests on design principles and
  secondary analysis.

## Design questions
1. For each ability: what does it change in traversal, combat and old areas?
2. Where are the landmarks a player will remember a blocked path by?
3. What new reward is waiting the second time through each region?
4. Can the critical path be explained in one sentence per act?

## Sources
- [B43] Chalmers thesis and Gato Roboto Q&A (secondary).
- [A1] Schell: interest curves and curiosity.
- Full bibliography: `research/SOURCES.md` in the repository.
