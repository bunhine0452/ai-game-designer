# Cost curve: Tidecaller starter pool v1: cost curve

![Cost curve](tidecaller-starter-v1_fit.png)

Fit on 24 items: R² = 0.712, RMSE = 0.49 cost. Flag threshold ±0.74.

## Value of each attribute (in cost units)

| Attribute | Cost per point |
|---|---|
| (intercept) | -0.276 |
| damage | +0.195 |
| block | +0.225 |
| draw | +0.574 |
| tide | -0.036 |
| drench | +0.156 |
| aoe | +1.087 |
| exhaust | -0.155 |

_The intercept is the baseline cost every item pays (e.g. the card itself). A negative weight usually marks a drawback; if a 'positive' attribute fits negative, it is overvalued in the current set or confounded with another column._

## Outliers

- **Rogue Wave** costs 1, fair ≈ 2.4 (+1.4): undercosted (too strong); raise its cost or trim its stats.
- **Still Water** costs 2, fair ≈ 0.8 (-1.2): overcosted (too weak); lower its cost or add value.

## All items

| Item | Cost | Fair | Residual | Verdict |
|---|---|---|---|---|
| Rogue Wave | 1 | 2.38 | +1.38 | undercosted (too strong) |
| Spring Tide | 0 | 0.73 | +0.73 | on curve |
| Spindrift | 1 | 1.52 | +0.52 | on curve |
| Breakwater | 2 | 2.39 | +0.39 | on curve |
| Maelstrom | 3 | 3.36 | +0.36 | on curve |
| Saltspray | 0 | 0.27 | +0.27 | on curve |
| Mist Veil | 1 | 1.26 | +0.26 | on curve |
| Whirlpool | 2 | 2.10 | +0.10 | on curve |
| Deep Current | 2 | 2.06 | +0.06 | on curve |
| Tidal Wave | 3 | 3.04 | +0.04 | on curve |
| Undertow | 1 | 1.04 | +0.04 | on curve |
| Neap Tide | 0 | 0.03 | +0.03 | on curve |
| Crest Breaker | 2 | 2.03 | +0.03 | on curve |
| Riptide | 1 | 1.01 | +0.01 | on curve |
| Splash | 1 | 0.86 | -0.14 | on curve |
| Brine Lash | 1 | 0.82 | -0.18 | on curve |
| Brace | 1 | 0.81 | -0.19 | on curve |
| Ebb and Flow | 1 | 0.80 | -0.20 | on curve |
| Abyssal Call | 3 | 2.77 | -0.23 | on curve |
| Kelp Snare | 1 | 0.74 | -0.26 | on curve |
| Swell | 2 | 1.60 | -0.40 | on curve |
| Moonpull | 2 | 1.40 | -0.60 | on curve |
| Drowned Bell | 3 | 2.34 | -0.66 | on curve |
| Still Water | 2 | 0.81 | -1.19 | overcosted (too weak) |

_A linear cost curve misses synergies, conditional text and metagame context. Use it to find suspects, then playtest._
