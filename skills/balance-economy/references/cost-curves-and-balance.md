# Cost curves, transitive and intransitive balance

## Transitive balance: cost curves

In a transitive system, higher cost buys more power along a **cost curve**. Schreiber's
method:

1. Pick a resource unit (mana, gold, supply).
2. Estimate the value of each attribute in that unit (1 attack = 0.5, draw a card = 1.0…).
3. Include an **intercept**: a baseline every item pays (e.g. the card slot itself). It is
   often negative in card games, because the card is a cost you spend.
4. Sum each item's attribute values to get its "fair cost" and compare with its actual cost.
5. Items far above the curve are **undercosted** (too strong); far below, **overcosted** (too
   weak).

`cost_curve.py` fits the attribute values by least squares, so you don't have to guess them.
Run it with `--robust` so outliers don't drag the curve.

### Reading the fitted weights
- A weight is the cost of one point of an attribute. Check that it makes sense (positive for
  benefits, negative for drawbacks).
- A **negative weight on a benefit** usually means the attribute is confounded with another
  column or overvalued in the current set. Add items that vary it independently.
- **R²** shows how much of the cost the linear model explains. Low R² means costs follow
  rules the model doesn't see: synergies, conditional effects, or inconsistent design.

### Limits
Linear cost curves miss synergy (two cards worth more together), conditional text, tempo,
scarcity (unique effects) and the metagame. Use them to find suspects, then playtest and check
win and pick rates.

### Non-linear curves
Many games make high-cost items pay **more** per point of power (late-game bombs, since big
effects are harder to answer), or give a discount per point (to encourage expensive plays).
Fit separate curves per cost band, or add a `cost²` column, if the residuals curve.

## Intransitive balance: counters

In intransitive systems, A beats B, B beats C, and C beats A (rock-paper-scissors). Model it as
a **payoff matrix** and find the expected optimal mix:

| | Rock | Paper | Scissors |
|---|---|---|---|
| Rock | 0 | −1 | +1 |
| Paper | +1 | 0 | −1 |
| Scissors | −1 | +1 | 0 |

With symmetric payoffs, the optimal mix is equal thirds. If one counter wins by more (e.g.
Rock beats Scissors by +2), the equilibrium shifts: Rock is used *less* and Paper *more*,
because players expect Rock. Solve small matrices by hand or in a spreadsheet. In live
games, check whether observed pick rates match the expected mix.

Uses: unit-type triangles (cavalry > archers > infantry > cavalry), fighting-game options
(strike / throw / block), element wheels, hero counters.

## Competitive balance goals (Sirlin)

1. **Viable options:** many choices are worth making. Count the options that appear in
   winning play at the top level.
2. **Fairness:** players of equal skill have about equal win chances despite different
   picks. Each faction or character should be able to win in expert hands.
3. **No dominant strategy:** the worst outcome. One option above all removes every other
   choice. More customization often reduces viable options, so test the combinations.

Johnson's warning: players will find the optimal strategy even if it drains the fun ("water
finds a crack"), so make sure the optimal path is also enjoyable.

## Balance for whom?

Competitive games usually balance for top players (where dominance is clearest) and watch
the median skill band separately. Something can be oppressive for novices (hard to answer)
while weak at the top. Track win and pick rates by skill tier.

## Sources
- [C1] Schreiber (2010), *Game Balance Concepts* (cost curves, transitive and intransitive). https://gamebalanceconcepts.wordpress.com/
- [C2] Schreiber & Romero (2021). · [C3] Schreiber (2016), GDC.
- [B7] Sirlin, *Balancing Multiplayer Games*, Parts 1–3. · [B11] Johnson (2011).
- [B2] Giovannetti (2019): metrics-driven card balance.
- Full bibliography: `research/SOURCES.md` in the repository.
