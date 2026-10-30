# Action and platformer

Covers 2D/3D platformers, precision platformers, character action (combo-driven melee) and
action-adventure combat.

## Core loop
Read the space or the enemy → commit to a move (jump, dash, strike) → instant feedback
(landing, hit reaction) → small reward (progress, combo, collectible) → the next obstacle
comes a little harder.

## Signature mechanics
- Tight movement: jump arcs, air control, dash, wall-jump.
- Forgiveness windows: coyote time, jump buffering, corner correction.
- Enemy tells and hit reactions: anticipation, active frames, recovery.
- Checkpoints and fast retry (precision games).
- Combo systems, cancels and style ranks (character action).

## Pacing shape
Short levels follow **introduce → develop → twist → conclude** (kishōtenketsu): teach one
idea safely, test it harder, combine or invert it, then drop it. Worlds escalate in a
sawtooth, with a boss or gauntlet at the end of each world. Precision platformers alternate
hard screens with breather screens.

## Progression model
Mostly **skill progression** (the player improves), sometimes with ability unlocks (new
movement verbs) and collectible-gated optional content. Character action adds move-list
unlocks and upgrades. These should widen expression, not just add damage.

## Balancing levers
- Gap widths and platform timings, relative to jump distance and timing windows.
- Enemy density, tell length and recovery frames.
- Checkpoint spacing (time lost per failure).
- Collectible placement (risk off the main path for optional reward).
- Assist options (game speed, invincibility) kept separate from the designed difficulty.

## Failure modes
- **Floaty or laggy controls:** input latency, long acceleration, no buffering.
- **Unfair deaths:** off-screen hazards, unreadable tells, leaps of faith.
- **Long run-backs** after death, so the punishment outweighs the lesson.
- **Mechanic soup:** too many ideas at once and none developed.
- **Difficulty spikes without teaching:** the skill being tested was never introduced.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Celeste | Very hard screens feel fair through invisible forgiveness and instant respawn; optional strawberries let skilled players opt into more risk |
| Super Mario 3D Land/World | Each level is a self-contained arc for one idea, so there's constant novelty with low teaching cost |
| Hollow Knight | Combat and movement share a small verb set, so mastery carries over everywhere |
| Devil May Cry series | Style ranking rewards variety over repetition and pulls players toward expressive play |

## Talks and postmortems
- Thorson, *Celeste & Forgiveness* (2020): the forgiveness techniques, explained by the designer.
- Kishōtenketsu in 3D Mario level design (designer interview and analysis).
- Swink, *Game Feel* (book): tuning movement feel.

## Design questions
1. What single verb is fun with no goals, enemies or rewards?
2. How long from death to playing again? (Target: under 2 s for precision games.)
3. Which new idea does each level introduce, and where does it get twisted?
4. What does an expert do that a novice can't, and is it visible?

## Sources
- [A13] Thorson (2020). https://maddymakesgames.com/articles/celeste_and_forgiveness/
- [A29] Kishōtenketsu / Hayashida (secondary).
- [A11] Swink (2008), *Game Feel*. · [A12] Jonasson & Purho (2012), *Juice it or lose it*.
- Full bibliography: `research/SOURCES.md` in the repository.
