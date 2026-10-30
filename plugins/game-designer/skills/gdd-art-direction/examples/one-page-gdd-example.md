# Lanternfall — one-page design            Owner: solo dev  Updated: 2026-10-30  Status: draft

## In one sentence
You are the last lantern spirit sinking through a drowned city, and every spark you carry is
both your life and your weapon.

| Genre | Platform / input | Session | Audience | Stage | Team / timeline |
|---|---|---|---|---|---|
| Action roguelite | PC; gamepad + KB/M | 20-min runs | Players of short-run action roguelites who like readable combat | Concept → greybox | Solo designer-programmer + contract art and audio, 12 months |

## Target aesthetics (ranked)
1. Challenge  2. Discovery  3. Fantasy

## Pillars
| Pillar | Test question | Rejects (example) |
|---|---|---|
| Light is the only resource | Does this spend, risk or create light? | A separate mana bar |
| Every room is a readable puzzle-fight | Can a player tell within 2 s what each enemy will do? | Random, untelegraphed attacks |
| The deep remembers | Does a run leave something behind in the city above? | Meta progression that is only stat bonuses |

## Core loops
```
[moment]  dash / strike / flare ──► enemy flinch + light burst ──► light orbs ──► spend or keep
              ▲                                                                    │
              └──────────────────────────── light level changes reach and damage ◄┘
[session] district path → 4-6 rooms → shrine boon → mid-boss → district 2 → keeper → bank light
[meta]    banked light relights the city above → new lanterns, NPC stories, opt-in "darker" depths
```

## Key features
- **Light meter** = health + ammo + currency. *Light is the only resource.*
- **Telegraphed enemy wind-ups** (0.4 s, unique sound plus a glow). *Readable puzzle-fight.*
- **Shrine boons** ("pick 1 of 3") that modify how light is spent. *Readable puzzle-fight.*
- **Relighting the city above** (hub). *The deep remembers.*
- **Darker depths** (opt-in heat levels). *Challenge, for mastery.*

## Pacing sketch
Run: hook (ambush) by 0:30 · mid-boss at about 43% · final keeper in the last 10% · run
summary with relight animation. See `fun-curve/examples/roguelite-20min-run.csv`.

## Progression and economy
Progression: horizontal unlocks (lanterns, boons) plus opt-in difficulty; stat bonuses capped
at +10%. Currency: light (in run) → banked light (meta), one direction only.
Monetization: premium, no microtransactions. (The ethics check passes trivially.)

## Visual and audio target
- Visual pillar: *light tells you everything.* Light is the brightest value on screen, enemies
  stay dark until lit, and no decorative glow competes with pickups.
- References: a dark watercolor city (take: muted, desaturated background values); bioluminescent
  sea life (take: shape of light trails); stained glass (take: color only where light passes).
- Audio pillar: *hear the danger before you see it.* Enemy wind-up sounds sit above the music.

## Reference games (lesson, not feature)
- Hades: story advances on death, so failure is progress.
- Into the Breach: telegraphed intent makes every turn fair.
- Dead Cells: run variety from a small set of well-tuned rooms.

## Scope check (from `asset-list-example.csv`)
| | Hours |
|---|---|
| Raw estimate, all assets and features | 1,494 |
| With integration ×1.3 and +25% buffer | about 2,430 |
| Solo capacity, 12 months (27 focused h/week, 10% off) | about 1,264 (80% = 1,011) |

**Over by about 2×.** Decision: contract the art (733 raw h) and audio (174 raw h). Solo dev
work is then 587 raw h, or **about 954 h** with factors, which fits under 1,011. Also **defer
District 2's new enemies and tileset to a post-launch update**. That brings dev work to about
832 h (comfortable) and contract art to 591 raw h. **Budget needed:** contract art and audio
(about 765 raw h after deferral).

## Risks and cheapest tests
1. Light-as-health feels stingy (hoarding). Test: greybox 3 rooms; pass if players spend
   ≥ 40% of the light they pick up.
2. Contract art arrives late or off-style. Test: commission one enemy plus one tileset chunk
   from the style guide first; pass if it needs ≤ 1 revision.
3. "Roguelite with a twist" is crowded. Test: a 30 s capsule GIF on two channels; pass if it
   gets more saves and replies than the last three posts.

## Open questions
- Run length on Steam Deck: 20 min, or shorter districts? (Options: 20 / 15; recommendation: 20
  with mid-run save; decide by vertical slice.)
- Localization at launch: EN only, or EN/KO/JA? (Recommendation: EN + KO + JA text, since the
  pipeline exists; decide by alpha.)
