# Pacing models

## Tension and release

Intensity only reads by contrast. A run of peaks with no release flattens into numbness, and
a run of valleys with no tension turns into boredom. The basic unit of pacing is a **cycle**:
build-up → peak → release → (anticipation) → next build-up.

## Left 4 Dead's AI Director

Valve's Director models each survivor's "emotional intensity". Intensity rises when the
player takes damage, and rises more from enemies close by. It decays slowly over time. The
Director then runs a population cycle:

| Phase | What the Director does |
|---|---|
| Build up | Spawn normal threats while intensity rises |
| Sustain peak | Keep the pressure briefly once intensity crosses a threshold |
| Peak fade | Stop adding threats; let the current ones resolve |
| Relax | Hold back major threats for a while so players can recover and move on |

The lessons generalize. (1) Measure intensity from player state, not from the level script.
(2) **Guarantee** a release after every peak. (3) Use procedural placement of enemies and
items so experienced players can't memorise the pacing.

## Alien: Isolation's menace

A director AI always knows where the player is and steers the alien toward them. The alien
itself must hunt using its own senses, so it never "cheats". A menace measure rises while the
alien is near or perceived (heard, seen). Past a threshold, the alien withdraws into the
vents for a while. This creates ebb and flow without a script. Pair it with the design
choice to make the player underpowered: the core decision becomes "stay or go?".
(Mechanism details come from secondary analysis of the game.)

## Kishōtenketsu (introduce, develop, twist, conclude)

Nintendo's 3D Mario levels are often described as a four-part arc. **Introduce** a mechanic
safely, **develop** it with harder uses, **twist** it (combine or invert it), then
**conclude** and drop it. The level is short and self-contained, and the next level uses a
new idea. It's a strong model for puzzle and platformer levels and for tutorial sequences in
any genre.

## Sawtooth escalation

Each segment ramps up and ends harder than it started. The next segment resets lower, but
above the previous valley. The result is relief inside each segment while the trend line
still climbs. It matches the rising peaks of an interest curve and keeps difficulty inside a
flow channel that moves up as the player's skill grows.

## Session-length design

- **Design the natural session as a complete mini-arc** (one run, one match, one day in the
  game, one level), with a hook, a peak and a reason to start the next one.
- **End sessions on a high or with a hook.** End-of-session rewards and previews of the next
  goal invite a return. Don't punish leaving: no lost progress, no decaying resources.
- **Make the length match the context.** Mobile play happens in short, interruptible slots,
  so loops of 30 s to 3 min with reliable save points work best. PC and console players
  accept 20–90 minute arcs.
- **First session:** first-day retention is low across mobile. In 2024 benchmark data,
  median D1 was in the low 20s % and top-quartile D1 about 27%. The first 5–10 minutes
  therefore carry outsized weight: hook early, teach fast, reward a first success.

## Typical shapes by genre and scale

Use these as targets to compare against, not rules.

| Genre and scale | Hook | Body | Climax | Notes |
|---|---|---|---|---|
| Roguelite run (15–40 min) | Within 1–2 min (first fight, first boon) | Sawtooth per biome; shop and rest valleys | Final boss in last 10% | Mid-boss around 40–50%; variety from builds |
| Action / platformer level (3–10 min) | First 30 s | Kishōtenketsu; 2–3 rising peaks | Last 15% | Checkpoints before peaks |
| Shooter campaign mission (15–30 min) | Opening set piece | Combat arenas with traversal valleys | Final arena or set piece | Vary combat spaces (open/tight) |
| Horror chapter (20–60 min) | Early unease, not a jump scare | Long dread build; short spikes | Late chase or confrontation | Valleys are *tense quiet*, not safe |
| Puzzle chapter (10–30 min) | A clear, quick early win | Introduce → combine → twist | Hardest "aha" in last 20% | Breathers after hard puzzles |
| Strategy match (20–90 min) | Early meaningful choice | Expansion plateau → skirmishes | Decisive battle | Fight the "solved mid-game" plateau |
| Competitive match (10–40 min) | First contact quickly | Skirmish waves | Final objective / final circle | Comeback potential keeps late peaks |
| Narrative game chapter (30–90 min) | Character or mystery hook | Revelations as peaks | Emotional climax | Choices as peaks; let quiet scenes breathe |
| Idle / incremental (days) | Fast first unlocks (seconds) | Slowing growth → prestige | Prestige moments | Each prestige restarts the curve faster |
| Match-3 sequence (10–20 levels) | Easy wins first | About 1 hard level in 5 | Hard "gate" levels | Pace difficulty across levels |
| Whole game (10–60 h) | First hour delivers the fantasy | New mechanic or place every 1–3 h | Final act | Watch the hour-8 "middle sag" |

## Sources

- [A4] Booth (2009), *The AI Systems of Left 4 Dead*. https://cdn.fastly.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf
- [A27] Thompson (2017), *The Perfect Organism: The AI of Alien: Isolation* (secondary). · [A28] Hope, GDC 2015 recap.
- [A29] Kishōtenketsu in 3D Mario level design (designer interview and analysis, secondary).
- [A1] Schell, interest curves. · [A3] Chen (2007), flow channel.
- [A26] GameAnalytics (2025), *Mobile Gaming Benchmarks*.
- [B25] King match-3 difficulty pacing talks. · [B24] Pecorella, idle-game math.
- Full bibliography: `research/SOURCES.md` in the repository.
