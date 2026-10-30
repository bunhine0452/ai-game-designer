# Tidecaller: genre brief

**Concept:** a roguelike deckbuilder for PC where every card is a tide spell. Team of three.

**Core genre:** roguelike deckbuilder. The moment-to-moment loop is turn-based card combat.
**Wrapper:** roguelite run structure. Each run is fight → card reward → remove or upgrade → choose a path. Between runs, meta unlocks.

## The core system (used across all three deliverables)

| Term | Rule |
|---|---|
| **Tide gauge** | Shared 0–10 gauge; starts each combat at 5 |
| **Surge N / Ebb N** | Raise / lower the tide by N. **Every card does one or the other** |
| **Crest** | Tide reaches 10: deal 8 damage to ALL enemies, reset to 5 |
| **Slack Water** | Tide reaches 0: gain 8 block, draw 1, reset to 5 |
| **Drench N** | The target's next N hits taken deal +3 |
| **Enemy tide intent** | Enemies telegraph their own Surge or Ebb on the same gauge |

## Design pillars

1. **Read the water.** Everything after the draw is visible and deterministic, including what enemies will do to the tide.
2. **Rise and break.** Every turn is about building toward a Crest or a Slack Water and choosing when to spend it.
3. **Every card is water.** One spell grammar (Surge or Ebb), with no attack, skill or power split.

## Expectations to honor

| # | Convention | Why players expect it | Concrete move for Tidecaller |
|---|---|---|---|
| 1 | **Telegraphed enemy intent** | Slay the Spire made the turn a readable puzzle. Hidden intent feels unfair in this genre | Show damage intent **and tide intent** ("Surge 3"). Hovering a card previews where the gauge lands after play, after the enemy's move |
| 2 | **Pick 1 of 3 card rewards, with Skip** | Small decks are the strategy, and skipping is a skill | 3 offers after each fight, Skip always allowed. Rare odds rise in Act 2 so the deck can come online mid-run (see `03-interest-curve.md`) |
| 3 | **Deck thinning and upgrades** | Removing basics is how a build gets sharper | Removal at every shop with a rising price. Upgrade or heal at rest sites |
| 4 | **Branching map with visible node types** | Route planning is the between-fights strategy | 3 acts of about 8 nodes each, 2–3 path options. Fight, elite, event, shop, rest and boss icons visible ahead of time |
| 5 | **Fast restart; meta unlocks widen options instead of adding power** | Death has to feel like a lesson. Raw meta power stops skill from mattering | Under 10 s from the death screen to the first turn. Unlocks add cards and relics to the pool (24 → ~80), never +HP or +damage |

Turn economy follows the genre default (3 energy, draw 5, 10-card starter deck), so veterans read it immediately.

## Conventions to break

| # | Genre default | Tidecaller's break | Pillar | Cost and how to pay it |
|---|---|---|---|---|
| 1 | Player resources are private | **One shared tide gauge.** Enemies push it too, and you can bait an enemy's Surge into your own Crest | Read the water | Teaching time. Introduce enemy tide intent in the second fight (2.5 min), never in the tutorial popup. *Test:* do players hold a card because of the enemy's tide intent? |
| 2 | Card types (attack / skill / power) carry identity | **Direction carries identity.** Every card Surges or Ebbs; nothing is neutral | Every card is water | Sameness risk (failure mode 6). Pay it with 3 archetypes that win differently: **Crest** (Surge burst AoE), **Slack** (Ebb control and block), **Current** (draw and tide manipulation) |
| 3 | Runs last 45–90 min | **30-minute runs**: three ~10-minute acts | Rise and break | The deck may not come online before the end. Pay it with removal at the first shop, Act 2 rares, and a rest before the mid-run peak. This also suits a small team: less content is needed per run |

## Pacing shape

- **Combat (3–6 turns):** turns 1–2 build the gauge, mid-combat a Crest or Slack swing, then the kill. Enemy tide intent creates the tension, because they may push the gauge away from your plan.
- **Run (30 min):** hook within 1 min, a sawtooth that rises per act, the deck-comes-online peak at ~50%, and the final boss in the last 10%. Plotted and diagnosed in `03-interest-curve.md`.
- **Whole game:** early runs end in Act 1–2, first wins come after several hours, then difficulty tiers ("Spring Tide" levels) stretch the curve. Several hours is a rule of thumb, not a target from data.

## Progression model and the levers that matter most

Three layers: (1) in-run deck and relics, (2) player knowledge across runs, which should be the main source of win rate, and (3) meta unlocks that widen the pool.

| Lever | Current value | Where it's modelled |
|---|---|---|
| Value of 1 tide point | 0.19 energy (fitted) | `02-cost-curve-analysis.md` |
| Crest vs Slack payoff | Both ≈ 2.0 energy for ≈ 0.95 energy of tide, so they're symmetric | `02-cost-curve-analysis.md` |
| Enemy tide-intent frequency | Act 1: rare; Act 2: every fight; bosses: seize the gauge | `run/tidecaller-run-v2.csv` |
| Offers per reward / removal price | 3 offers, removal at every shop | Telemetry after first build |
| Card pool size | 24 starter → ~80 at 1.0 | Scope, see failure mode 11 |

## Failure-mode checklist

| # | Failure mode | Status | Why | Design move or test |
|---|---|---|---|---|
| 1 | **Dominant card or deck / solved gauge** | **At risk** | There's one resource axis. A max-tide-movement deck can chain Crests every turn. Draft v1 already had a free tide engine (Spring Tide at 0 cost) | Keep `tide` priced (it now fits at +0.19 per point). Consider Crest damage falling within one turn (8 → 6 → 4); that's a rule of thumb to test. Track pick and win rate per card |
| 2 | Pay-to-win collection | Not at risk | Premium PC with no card sales | If you add DLC, sell characters and cosmetics, never stronger cards |
| 3 | Output randomness decides fights | Not at risk | All card numbers are fixed and intent is visible. Randomness comes only from draws, offers and the map (input randomness) | Rule: no ranged rolls like "deal 4–10" and no random tide shifts. Keep this rule as the pool grows |
| 4 | Rules-text bloat | **At risk (moderate)** | The starter pool already uses 5 keywords (Surge, Ebb, Crest, Slack, Drench) plus enemy tide intent | Cap launch at 6 keywords, keep card text to 2 lines or fewer, and put the explanation in the gauge preview rather than the text |
| 5 | Unfun interaction ("tide screw", long enemy turns) | **At risk** | An enemy Ebb can wipe out a Crest you planned, which feels like land screw | Every enemy tide move is telegraphed a turn ahead. No hidden tide changes. An enemy's tide moves cap at 3 per turn outside bosses. Enemy turns animate in under 3 s |
| 6 | **Run sameness** | **At risk (highest)** | "Every card is a tide spell" means one visual and mechanical grammar, and 24 cards share 2 verbs | 3 archetypes with distinct win conditions, plus relics that change gauge rules (a 0–14 gauge, double Crest, Slack also deals damage). *Test:* a playtester finds ≥ 3 distinct builds in 10 runs |
| 7 | Snowball or doom loop | **At risk (moderate)** | Crest AoE plus Drench snowballs once online. A 30-min run leaves little time to recover from a bad Act 1 | Tune Act 1 fights for the basic deck, put one rest per act, and make elites optional |
| 8 | Meta grind replacing skill | Not at risk | Unlocks widen the pool and don't add stats | Meta power budget: zero raw stats |
| 9 | Slow restart | At risk (small) | Draft run v1 had a 1-minute intro | Moved the story to the death screen. Target under 10 s from death to first turn |
| 10 | Long runs with no checkpoint | Not at risk | 30 min on PC | Still suspend-save at every node |
| 11 | **Scope vs. team size** | **At risk** | Deckbuilders are systems-hungry. Genre leaders ship roughly 70+ cards per character plus relics and dozens of enemies | One character at 1.0: about 80 cards, about 30 relics, about 25 enemies, 3 act bosses and 1 final boss. Cards stay data-driven (the CSV in `cards/` is already pipeline-ready), and you re-run the cost curve on every pool change |
| 12 | Theme readability (24 water cards look alike) | **At risk** | One theme, one palette | Silhouette and shape code by direction (Surge: rising crest frame; Ebb: falling, deep frame), not color alone, for accessibility. Hand off to `gdd-art-direction` |

## Reference games and the lesson to take

| Game | Lesson (not a feature to copy) |
|---|---|
| Slay the Spire | Telegraphed intent plus a small deck makes each turn a fair puzzle, and its team balanced with pick and win metrics read in context. *Apply:* show tide intent with an exact gauge preview, and log pick and win rates from the first build |
| Balatro | One familiar grammar with escalating payoffs is easy to read and deep to break. *Apply:* Surge and Ebb can carry the whole game if Crest payoffs escalate (relics, chains) |
| Hades | Story that moves forward on death makes failure feel like progress. *Apply:* the lighthouse keeper's story plays on the death screen, which also frees up the first minute of each run |
| Into the Breach | Fully telegraphed enemy actions that you can redirect make a small game deep. *Apply:* baiting an enemy's Surge into your Crest is Tidecaller's version of pushing an enemy into its own attack |

## Evidence note

The Slay the Spire metrics practice comes from a GDC talk (Giovannetti, *Metrics Driven Design and Balance*, 2019). Run-length ranges,
the keyword cap, the restart target and the Crest falloff are rules of thumb from general practice, not published studies.

## Next steps

- Card numbers: `02-cost-curve-analysis.md` (done).
- Pacing: `03-interest-curve.md` (done).
- Not yet done: a one-page GDD and an art direction pass on card readability (`gdd-art-direction`), and a critique once a prototype exists (`design-review`).
