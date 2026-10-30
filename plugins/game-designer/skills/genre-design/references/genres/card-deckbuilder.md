# Card games and deckbuilders

Covers collectible and trading card games (CCG/TCG, digital and physical), living card
games, roguelike deckbuilders (build the deck during a run), and tabletop-style
deckbuilders (Dominion-like markets).

## Core loop
- **CCG:** collect cards → build a deck → play a match (draw, spend resources, play cards,
  answer the opponent) → rewards → refine the deck.
- **Roguelike deckbuilder:** fight → choose a card reward (or skip) → remove or upgrade cards →
  path choice → fight harder enemies.

## Signature mechanics
- A resource curve (mana or energy per turn) and card **cost curves**.
- Card advantage, tempo and value as the core strategic tensions.
- Keywords that compress rules text (taunt, charge, exhaust).
- Synergy archetypes (aggro, control, combo, ramp).
- Deck thinning and removal (roguelike deckbuilders).
- Telegraphed enemy intent (Slay the Spire) turns combat into a readable puzzle.

## Pacing shape
Match: early turns develop → mid-game tempo swings → late game bombs or combos (the
climax). Roguelike deckbuilder run: act sawtooth with elites and bosses; a deck "comes
online" mid-run, which is a strong peak. Live CCGs pace the meta with expansions.

## Progression model
CCG: collection growth (watch pay-to-win), ranked ladders, cosmetic collection. Roguelike
deckbuilder: within-run deck growth, plus meta unlocks (new cards and characters).
Ascension levels give long-term challenge.

## Balancing levers
- **Cost curve:** value per resource point, including a baseline cost for the card itself.
  Fit it with `balance-economy/scripts/cost_curve.py` to find off-curve cards.
- Rarity distribution and its effect on power (watch rarity = power).
- Draw rate, hand size, resource ramp.
- Counterplay density: how many answers exist to each threat type.
- Win-rate and pick-rate metrics per card (Slay the Spire balanced with early-access metrics
  and community feedback).

## Failure modes
- **Dominant deck or card** (no viable options): the ladder collapses into mirror matches.
- **Pay-to-win collection gaps** in CCGs.
- **Too much output randomness** (coin flips deciding matches) vs. input randomness (draws,
  which players plan around).
- **Rules-text bloat** and complexity creep across expansions.
- **Unfun interaction**, such as long uninteractive opponent turns or land-screw-style
  resource failure.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Magic: The Gathering | The original resource-and-color system gives deep deckbuilding; decades of public design writing |
| Hearthstone | Simplified the CCG (automatic mana, no instant-speed interaction) to reach a broad audience |
| Slay the Spire | Telegraphed intent plus a small deck makes each choice weigh a lot; skipping cards is a strategy |
| Dominion | A shared market removed collecting; deckbuilding became the game |
| Balatro | Poker hands as a familiar grammar with escalating multipliers; easy to read, deep to break |

## Talks and postmortems
- Rosewater, *Ten Things Every Game Needs* (Making Magic) and *Twenty Years, Twenty Lessons*
  (GDC 2016).
- Dodds, *Hearthstone: Making a Game for Everyone* (GDC 2014 recap).
- Giovannetti, *Slay the Spire: Metrics Driven Design and Balance* (GDC 2019).
- Schreiber, *Game Balance Concepts*: cost curves and transitive balance.

## Design questions
1. What is the value of one resource point, and which cards sit off that curve on purpose?
2. Which archetypes exist, and what beats each?
3. Where does randomness enter: before decisions (draws) or after (coin flips)?
4. How long is a typical opponent turn, and what is the player doing meanwhile?

## Sources
- [B22] Rosewater (2011; GDC 2016). · [B23] Dodds (2014, recap). · [B2] Giovannetti (2019).
- [C1] Schreiber (2010). · [C2] Schreiber & Romero (2021). · [C6] Engelstein & Shalev: randomness.
- Full bibliography: `research/SOURCES.md` in the repository.
