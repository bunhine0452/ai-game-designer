# Cost curve: Tidecaller starter pool v3 (final): cost curve

![Cost curve](tidecaller-starter-v3_fit.png)

Fit on 24 items: R² = 0.960, RMSE = 0.16 cost. Flag threshold ±0.50.

## Value of each attribute (in cost units)

| Attribute | Cost per point |
|---|---|
| (intercept) | -0.306 |
| damage | +0.169 |
| aoe_damage | +0.255 |
| block | +0.193 |
| draw | +0.482 |
| tide | +0.185 |
| drench | +0.356 |
| exhaust | -0.594 |

_The intercept is the baseline cost every item pays (e.g. the card itself). A negative weight usually marks a drawback; if a 'positive' attribute fits negative, it is overvalued in the current set or confounded with another column._

## Outliers

None beyond the threshold. The set sits on one curve.

## All items

| Item | Cost | Fair | Residual | Verdict |
|---|---|---|---|---|
| Tidal Wave | 3 | 3.31 | +0.31 | on curve |
| Riptide | 1 | 1.25 | +0.25 | on curve |
| Mist Veil | 1 | 1.23 | +0.23 | on curve |
| Breakwater | 2 | 2.19 | +0.19 | on curve |
| Saltspray | 0 | 0.15 | +0.15 | on curve |
| Neap Tide | 0 | 0.14 | +0.14 | on curve |
| Rogue Wave | 2 | 2.09 | +0.09 | on curve |
| Spindrift | 1 | 1.08 | +0.08 | on curve |
| Brine Lash | 1 | 1.08 | +0.08 | on curve |
| Maelstrom | 3 | 3.04 | +0.04 | on curve |
| Undertow | 1 | 1.04 | +0.04 | on curve |
| Ebb and Flow | 1 | 1.03 | +0.03 | on curve |
| Kelp Snare | 1 | 1.01 | +0.01 | on curve |
| Moonpull | 2 | 1.98 | -0.02 | on curve |
| Abyssal Call | 3 | 2.95 | -0.05 | on curve |
| Spring Tide | 1 | 0.92 | -0.08 | on curve |
| Crest Breaker | 2 | 1.91 | -0.09 | on curve |
| Deep Current | 2 | 1.90 | -0.10 | on curve |
| Splash | 1 | 0.89 | -0.11 | on curve |
| Brace | 1 | 0.84 | -0.16 | on curve |
| Still Water | 2 | 1.79 | -0.21 | on curve |
| Whirlpool | 2 | 1.76 | -0.24 | on curve |
| Swell | 2 | 1.75 | -0.25 | on curve |
| Drowned Bell | 2 | 1.68 | -0.32 | on curve |

_A linear cost curve misses synergies, conditional text and metagame context. Use it to find suspects, then playtest._
