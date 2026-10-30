# Horror

Covers survival horror (limited resources, a vulnerable protagonist), psychological horror,
stalker or chase horror, action horror and co-op horror.

## Core loop
Explore under threat → perceive signs of danger (sound, shadow, environmental story) → decide
(hide, run, fight, wait) → survive or fail → brief relief → dread builds again.

## Signature mechanics
- Vulnerability: limited ammo or no weapons, weak combat, scarce saves.
- A stalker or director AI that controls threat presence over time.
- Sound design as information and dread (footsteps, breathing, silence).
- Limited vision: darkness, a flashlight battery, fog. These work only with other cues.
- Safe rooms and save points as valleys.

## Pacing shape
Mostly **dread** (anticipation), with **short** spikes of terror, then relief. Long
high-intensity stretches (endless chases) numb fear. Alien: Isolation's director has the alien
retreat after menace peaks. Left 4 Dead's Director guarantees relaxation after peaks.
Valleys aren't safe. They're *quiet tension*.

## Progression model
Story and mystery progression (what happened here?), map and key progression (survival
horror), modest resource upgrades. Too much power growth turns horror into action.

## Balancing levers
- Threat frequency and proximity (a menace meter, director cooldowns).
- Resource scarcity: ammo, healing, battery, saves.
- Player power vs. threat power.
- Information: how much the player sees and hears of the threat.
- Fail cost: how much progress a death costs. Fear needs stakes; frustration kills fear.

## Failure modes
- **Jump-scare dependence:** cheap spikes without dread become predictable.
- **Overexposed monster:** familiarity removes fear. Keep the threat partly unseen.
- **Sustained chases** that turn fear into annoyance.
- **Punitive deaths:** replaying long sections turns horror into a chore.
- **Atmosphere with no meaning.** Fog or darkness alone isn't scary. Grip stresses using lore,
  music and odd sightings to steer the imagination, and leaving gaps for players to fill.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Alien: Isolation | A director plus a senses-driven alien creates unscripted ebb and flow; the player is deliberately underpowered |
| Amnesia: The Dark Descent | No combat; the player fills gaps with their imagination; simple controls leave room for paranoia |
| Resident Evil (classic / remakes) | Resource scarcity turns every encounter into a decision about whether to fight or avoid |
| Left 4 Dead | Intensity-driven pacing with guaranteed relief; co-op turns fear into People Fun |

## Talks and postmortems
- Hope, GDC 2015 on Alien: Isolation (focus on survival, not killing).
- Thompson, *The Perfect Organism: The AI of Alien: Isolation* (secondary analysis).
- Grip (Frictional Games) interviews on leaving gaps, vulnerability and thematic monsters.
- Booth, *The AI Systems of Left 4 Dead* (2009).

## Design questions
1. What does the player *imagine* the threat can do, and how do you protect that mystery?
2. How long are the terror spikes, and what guarantees relief after each?
3. What does the player lose on death, and does that loss raise fear or frustration?
4. Which cue (audio, visual, story) tells the player danger is close, and is it learnable?

## Sources
- [A27] Thompson (2017, secondary). · [A28] Hope (2015, recap).
- [B18] Grip interviews (secondary). · [A4] Booth (2009).
- Worked fix of a horror chapter's pacing: `skills/fun-curve/examples/horror-fix-walkthrough.md` (in this plugin).
- Full bibliography: `research/SOURCES.md` in the repository.
