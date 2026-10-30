# Core design frameworks

Working notes on the frameworks the router uses. Everything here is paraphrased; see the
Sources section.

## MDA: Mechanics, Dynamics, Aesthetics

- **Mechanics**: rules, data and algorithms, i.e. what the designer writes down.
- **Dynamics**: behaviour at run time when players interact with the mechanics over time
  (bluffing, kiting, rushing, hoarding).
- **Aesthetics**: emotional responses the player has (tension, wonder, pride).

The designer controls only mechanics directly. Players experience aesthetics first and work
backwards. So debug in this order:

1. Name the missing or unwanted aesthetic ("the fights feel samey").
2. Find the dynamic that should produce it ("players use the same opener every fight").
3. Find the mechanic that allows or rewards that dynamic ("the opener is strictly best
   against every enemy type").
4. Change the mechanic and predict the new dynamic before building it.

### The eight aesthetics (MDA taxonomy)

| Aesthetic | Player feels | Typical mechanics | Example question |
|---|---|---|---|
| Sensation | Sensory pleasure | Juice, audio, haptics, spectacle | Does pressing the button feel good with no context? |
| Fantasy | Make-believe | Role, setting, power fantasy | What does the player get to *be*? |
| Narrative | Drama | Plot, characters, branching | What will the player retell afterwards? |
| Challenge | Obstacle course | Skill tests, puzzles, mastery curves | What gets better with practice? |
| Fellowship | Social framework | Co-op, guilds, trading, chat | What can players do *for* each other? |
| Discovery | Uncharted territory | Exploration, secrets, emergent systems | What is unknown at hour 1 and known at hour 10? |
| Expression | Self-discovery | Building, customization, play styles | What can two players do differently? |
| Submission | Pastime | Low-stakes loops, routine, ambience | Can it be played half-attentively and still feel nice? |

Lazzaro's four keys cross-check the list from observed emotion: **Hard Fun** (challenge
and *fiero*), **Easy Fun** (curiosity, novelty), **People Fun** (social emotions), and
**Serious Fun** (play that changes the player or their world). Her studies found that
well-liked games tend to deliver several keys and that players move between them in one
session.

## Design pillars

A pillar is a short phrase plus a **test question**. Use pillars to decide what to build,
cut or protect.

- 3–5 pillars. Fewer is too vague to guide anything; more and they stop being priorities.
- Each pillar maps to at least one target aesthetic.
- Each pillar should reject at least one plausible feature. If it rejects nothing, rewrite it.
- Phrase pillars as experiences, not features: "Every room is a tactical puzzle", not
  "Grid-based combat".

Template:

```
Pillar: <experience phrase>
Serves: <aesthetic(s)>
Test: <yes/no question a feature must pass>
Rejects (example): <a feature this pillar would cut>
```

Studios report building early prototypes around pillars and the emotions they target. For
example, Subnautica set pillars before prototyping, and Hi-Fi Rush defined its mechanics
through core pillars that fed a positive feedback loop.

## Loops and arcs

Cook models play as **loops**: the player acts, the game gives feedback, and the player
updates their mental model and acts again. Loops repeat at different time scales. **Arcs**
are one-shot experiences (a story beat, a reveal) that don't repeat the same way.

### Three loop layers

| Layer | Time scale | Write it as | Failure mode |
|---|---|---|---|
| Moment-to-moment | 1–30 s | verb → feedback → micro-reward | Inputs feel unresponsive; feedback is unclear |
| Session | 5–60 min | goal → challenge → reward → choice → new goal | No reason to start "one more" |
| Meta | days–months | progression, collection, mastery, status | Grind with no new decisions; pure number-go-up |

Checks:
- Each lower loop **feeds** the one above (fights earn resources, resources unlock choices,
  choices change future fights).
- The reward of each loop **changes the next iteration** (new options, new knowledge). It
  shouldn't just add a number.
- The core verb is fun before rewards are added. Prototype it with no progression.

### Skill atoms (skill chains)

Break a mechanic into the smallest learnable unit: *action → simulation → feedback →
updated model*. Chain atoms into a skill tree ("jump" → "jump over gap" → "wall-jump chain").
This shows what must be taught first, where players get stuck, and which atoms are never
used after the tutorial (cut or deepen them).

## Interesting decisions

Meier's definition: a game is a series of interesting decisions. A decision is interesting
when:

1. **No option dominates**, so each one wins in some situation.
2. **The trade-off is readable**: the player can predict consequences well enough to reason.
3. **It matters**: the outcome changes later options or results.
4. **It's personal**: play style, risk appetite or situation decides it, not a solved answer.

Red flags: an always-best choice (dominant strategy), a coin flip with no information, a
choice whose effect is invisible, or one that is overturned before it matters. Johnson
warns that players will find and use the optimal strategy even if it drains the fun ("water
finds a crack"). Design so the optimal path is also the enjoyable one.

## Fun as learning

Koster frames fun as the pleasure of learning patterns. Once a player has fully learned a
system's patterns, boredom follows. Depth comes from systems that keep producing new
patterns (opponents, procedural content, combinatorics, social play). Practical test: list
what a player is still learning at hours 1, 5, 20 and 100. An empty row predicts churn there.

## Worked example: tightening a vague concept

> "A cozy farming game with monsters."

| Step | Result |
|---|---|
| Target aesthetics | Submission (primary), Discovery, Expression |
| Fantasy | Tend a valley where tamed monsters reshape the land |
| Pillars | *Every monster changes the farm* (test: does this monster alter terrain, crops or routes?) · *No fail states, only detours* (test: can a mistake end progress? if yes, redesign) · *Discover by noticing* (test: is this learnable by watching the world, without a tooltip?) |
| Moment loop | Pet / feed / guide monster → visible terrain change → small harvest |
| Session loop | Pick a plot goal → combine monster abilities → harvest → unlock a seed or monster → new goal |
| Meta loop | Valley restoration map, monster codex, seasonal festivals |
| Rejected by pillars | Combat arenas (no fail states), stamina timers that end the day early (punishes rather than detours) |

## Fun hypothesis and keep/kill thresholds

No document can show that a game will be fun: the effect emerges in play, pooled design rules
transfer poorly between games, and even strong studios cancel most projects. Treat fun as a
hypothesis and test it with the smallest playable toy.

The best current account of fun is **uncertainty resolved faster than expected**: players enjoy
having something in doubt and resolving it at a good rate. On top of that sit the sensory layer
(feel, music, effects), other people, and meaning. Write the hypothesis in those terms:

```
Open question:   what will players want to find out? (where the exit is, which build wins,
                 who survives the last lap, what the mural means)
Rate:            how often a question resolves, and how often a new one arrives
Felt as:         what makes each resolution land (feel, sound, a reveal, a number popping)
For whom:        the audience and kind of fun (hard, easy, people, serious)
Keep if:         a behavioural threshold, e.g. 4 of 6 testers keep playing 5+ min after
                 "you can stop now", and A beats B in 8 of 12 comparisons
Kill if:         the floor below which you stop, e.g. fewer than 2 of 6 keep playing
```

**Loop:** hypothesis → smallest toy (core verb plus one source of uncertainty, no content) →
bot screen for anti-fun (`playable-prototype` → testing-and-bots, "anti-fun screen") → 5-8
outsiders (free-choice play, an A/B comparison, observer notes; `design-review` → playtest kit) →
keep, pivot or kill against the thresholds you wrote first → only then build content.

Write the thresholds before the test. Thresholds chosen after seeing the data always pass.

## Sources
- [A48]–[A68] the fun deep dive (`research/FUN_DEEP_DIVE.md`): why fun is hard, uncertainty resolution, measuring and studio practice.

- [A5] Hunicke, LeBlanc & Zubek (2004), *MDA: A Formal Approach to Game Design and Game Research*. https://users.cs.northwestern.edu/~hunicke/MDA.pdf
- [A6] Lazzaro (2004), *Why We Play Games: Four Keys to More Emotion Without Story*.
- [A16] Cook (2007), *The Chemistry of Game Design*. https://lostgarden.com/2007/07/19/the-chemistry-of-game-design/
- [A17] Cook (2012), *Loops and Arcs*. https://lostgarden.com/2012/04/30/loops-and-arcs
- [A18] Meier (2012), *Interesting Decisions*, GDC.
- [B11] Johnson (2011), *Water Finds a Crack*. https://designer-notes.com/game-developer-column-17-water-finds-a-crack
- [A10] Koster (2004/2013), *A Theory of Fun for Game Design*.
- [B16] Cleveland (2019), *The Design of Subnautica*, GDC. · [B27] Johanas (2024), *Developing Hi-Fi RUSH Backwards*, GDC.
- Full bibliography: `research/SOURCES.md` in the repository.
