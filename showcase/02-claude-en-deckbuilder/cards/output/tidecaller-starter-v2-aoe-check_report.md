# Cost curve: tidecaller-starter-v2-aoe-check

Fit on 24 items: R² = 0.952, RMSE = 0.18 cost. Flag threshold ±0.50.

## Value of each attribute (in cost units)

| Attribute | Cost per point |
|---|---|
| (intercept) | -0.294 |
| damage | +0.161 |
| aoe_damage | +0.253 |
| block | +0.193 |
| draw | +0.488 |
| tide | +0.178 |
| drench | +0.393 |
| exhaust | -0.588 |

_The intercept is the baseline cost every item pays (e.g. the card itself). A negative weight usually marks a drawback; if a 'positive' attribute fits negative, it is overvalued in the current set or confounded with another column._

## Outliers

None beyond the threshold. The set sits on one curve.

## All items

| Item | Cost | Fair | Residual | Verdict |
|---|---|---|---|---|
| Rogue Wave | 2 | 2.31 | +0.31 | on curve |
| Tidal Wave | 3 | 3.27 | +0.27 | on curve |
| Riptide | 1 | 1.24 | +0.24 | on curve |
| Mist Veil | 1 | 1.23 | +0.23 | on curve |
| Breakwater | 2 | 2.20 | +0.20 | on curve |
| Saltspray | 0 | 0.17 | +0.17 | on curve |
| Neap Tide | 0 | 0.14 | +0.14 | on curve |
| Brine Lash | 1 | 1.08 | +0.08 | on curve |
| Spindrift | 1 | 1.07 | +0.07 | on curve |
| Kelp Snare | 1 | 1.05 | +0.05 | on curve |
| Ebb and Flow | 1 | 1.04 | +0.04 | on curve |
| Undertow | 1 | 1.02 | +0.02 | on curve |
| Maelstrom | 3 | 2.98 | -0.02 | on curve |
| Moonpull | 2 | 1.97 | -0.03 | on curve |
| Abyssal Call | 3 | 2.94 | -0.06 | on curve |
| Deep Current | 2 | 1.91 | -0.09 | on curve |
| Spring Tide | 1 | 0.91 | -0.09 | on curve |
| Splash | 1 | 0.85 | -0.15 | on curve |
| Brace | 1 | 0.85 | -0.15 | on curve |
| Crest Breaker | 2 | 1.81 | -0.19 | on curve |
| Whirlpool | 2 | 1.79 | -0.21 | on curve |
| Still Water | 2 | 1.78 | -0.22 | on curve |
| Drowned Bell | 2 | 1.71 | -0.29 | on curve |
| Swell | 2 | 1.67 | -0.33 | on curve |

_A linear cost curve misses synergies, conditional text and metagame context. Use it to find suspects, then playtest._
