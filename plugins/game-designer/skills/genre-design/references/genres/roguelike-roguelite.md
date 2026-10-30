# Roguelike and roguelite

**Roguelike** in the traditional sense (the Berlin Interpretation, 2008) has high-value
factors such as procedural generation, permadeath, turn-based grid play, resource management
and exploration. **Roguelite** keeps permadeath and runs but adds persistent meta progression
and usually real-time action. Also covers roguelike deckbuilders and "bullet heaven"
auto-shooters.

## Core loop
Start a run → take on procedurally assembled challenges → pick from random rewards
(boons, cards, items) to build a strategy → die or win → carry meta progress → start a new run.

## Signature mechanics
- Procedural rooms and maps, with designer-made chunks assembled at random.
- **Build crafting** from random offers ("pick 1 of 3"): synergy discovery.
- Permadeath plus fast restart.
- Meta progression: unlocks, permanent upgrades, narrative progress.
- Self-imposed difficulty tiers (heat, ascension) for long-term mastery.

## Pacing shape
Run: hook within 1–2 minutes → sawtooth per act or biome → mid-boss → shops and rests as
valleys → final boss in the last 10%. Meta arc: early runs end fast, wins arrive after hours,
and difficulty tiers extend the curve.

## Progression model
Three layers. (1) **Within the run:** build power. (2) **Across runs:** player knowledge,
which is the main one. (3) **Meta unlocks:** these should widen options (new items,
characters) more than add raw power, or skill stops mattering. Hades shows narrative meta
progression: the story advances *because* you died.

## Balancing levers
- Offer weights and rarity per act; pity for key build pieces.
- Synergy caps (stopping infinite combos from breaking the run, or allowing them as a
  late-run treat).
- Damage and HP scaling per act; elite frequency.
- Shop prices vs. currency income per act.
- Meta power budget: how much easier the game gets from unlocks alone.
- Slay the Spire's team used metrics from early-access runs (card pick and win rates) with
  community feedback, and warned that metrics mislead without context.

## Failure modes
- **Run sameness:** too few meaningful offers; one obvious build.
- **Snowball or doom loop:** early luck decides the run (too much output randomness).
- **Meta grind replacing skill:** players must grind unlocks before they can win.
- **Slow restart** after death.
- **Long runs with no checkpoint** in a genre that expects short sessions (watch run length
  on mobile).

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Spelunky | Systemic interactions (shopkeepers, physics, enemies) make each run a story; mastery is all knowledge |
| Slay the Spire | Input randomness (cards drawn, enemy intent shown) followed by deterministic play makes every turn a fair puzzle |
| Hades | Narrative progresses on death, so failure feels like progress; boons from gods make build identity readable |
| Vampire Survivors | Removes aiming and inputs so the build *is* the game; a cheap, highly readable power fantasy |
| Dead Cells | Action-platformer feel plus roguelite structure; permanent unlocks widen options |

## Talks and postmortems
- Berlin Interpretation (2008).
- Giovannetti, *Slay the Spire: Metrics Driven Design and Balance* (GDC 2019).
- Kasavin & Korb, *The Dialogue of Hades* (GDC 2021); Kasavin on narrative roguelikes (GDC Podcast).
- Yu, *Spelunky* (Boss Fight Books, 2016).

## Design questions
1. How many distinct builds can a player find in 10 runs? In 100?
2. Is randomness mostly *input* (offers, maps) or *output* (hit rolls)? Input randomness
   supports strategy.
3. What does a death teach, and how quickly is the player back in?
4. What share of win rate comes from meta unlocks vs. player skill?

## Sources
- [B1] Berlin Interpretation. http://www.roguebasin.com/index.php/Berlin_Interpretation
- [B2] Giovannetti (2019). https://www.gdcvault.com/play/1025731/
- [B3] Kasavin & Korb (2021). · [B4] Yu (2016), *Spelunky*.
- [B40] Vampire Survivors genre coverage (secondary).
- [C6] Engelstein & Shalev: input vs. output randomness.
- Full bibliography: `research/SOURCES.md` in the repository.
