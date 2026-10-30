# Cost curve: Curva de Coste Rebalanceada - 12 Guardianes

Fit on 12 items: R² = 0.999, RMSE = 1.50 cost. Flag threshold ±2.25.

## Value of each attribute (in cost units)

| Attribute | Cost per point |
|---|---|
| (intercept) | +17.553 |
| dps | +2.074 |
| range | +15.029 |
| aoe_radius | +34.915 |
| slow_pct | +1.262 |

_The intercept is the baseline cost every item pays (e.g. the card itself). A negative weight usually marks a drawback; if a 'positive' attribute fits negative, it is overvalued in the current set or confounded with another column._

## Outliers

- **Cactus Espinoso** costs 150, fair ≈ 152.3 (+2.3): undercosted (too strong); raise its cost or trim its stats.
- **Seta Esporífera** costs 190, fair ≈ 187.7 (-2.3): overcosted (too weak); lower its cost or add value.
- **Calabaza Bomba** costs 230, fair ≈ 232.3 (+2.3): undercosted (too strong); raise its cost or trim its stats.

## All items

| Item | Cost | Fair | Residual | Verdict |
|---|---|---|---|---|
| Cactus Espinoso | 150 | 152.35 | +2.35 | undercosted (too strong) |
| Calabaza Bomba | 230 | 232.27 | +2.27 | undercosted (too strong) |
| Diente de León Céfiro | 190 | 192.09 | +2.09 | on curve |
| Girasol Radiante | 95 | 95.75 | +0.75 | on curve |
| Lirio Glacial | 185 | 185.07 | +0.07 | on curve |
| Planta Carnívora | 175 | 174.93 | -0.07 | on curve |
| Sauce Protector | 245 | 244.56 | -0.44 | on curve |
| Mazorca Cañonera | 270 | 269.10 | -0.90 | on curve |
| Orquídea Real | 170 | 168.96 | -1.04 | on curve |
| Rosa Francotiradora | 205 | 203.93 | -1.07 | on curve |
| Brote Guisante | 110 | 108.28 | -1.72 | on curve |
| Seta Esporífera | 190 | 187.72 | -2.28 | overcosted (too weak) |

_A linear cost curve misses synergies, conditional text and metagame context. Use it to find suspects, then playtest._
