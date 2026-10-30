# Cost curve: Curva de Coste - 12 Guardianes del Jardín

Fit on 12 items: R² = 0.212, RMSE = 50.46 cost. Flag threshold ±75.68.

## Value of each attribute (in cost units)

| Attribute | Cost per point |
|---|---|
| (intercept) | +68.401 |
| dps | +1.342 |
| range | +7.498 |
| aoe_radius | +21.223 |
| slow_pct | +1.293 |

_The intercept is the baseline cost every item pays (e.g. the card itself). A negative weight usually marks a drawback; if a 'positive' attribute fits negative, it is overvalued in the current set or confounded with another column._

## Outliers

- **Orquídea Real** costs 310, fair ≈ 167.0 (-143.0): overcosted (too weak); lower its cost or add value.
- **Mazorca Cañonera** costs 140, fair ≈ 218.4 (+78.4): undercosted (too strong); raise its cost or trim its stats.

## All items

| Item | Cost | Fair | Residual | Verdict |
|---|---|---|---|---|
| Mazorca Cañonera | 140 | 218.40 | +78.40 | undercosted (too strong) |
| Girasol Radiante | 95 | 126.45 | +31.45 | on curve |
| Brote Guisante | 110 | 120.42 | +10.42 | on curve |
| Lirio Glacial | 185 | 189.45 | +4.45 | on curve |
| Cactus Espinoso | 150 | 146.70 | -3.30 | on curve |
| Planta Carnívora | 175 | 166.88 | -8.12 | on curve |
| Diente de León Céfiro | 190 | 173.59 | -16.41 | on curve |
| Sauce Protector | 245 | 228.56 | -16.44 | on curve |
| Seta Esporífera | 190 | 169.36 | -20.64 | on curve |
| Rosa Francotiradora | 205 | 176.74 | -28.26 | on curve |
| Calabaza Bomba | 230 | 198.47 | -31.53 | on curve |
| Orquídea Real | 310 | 167.00 | -143.00 | overcosted (too weak) |

_A linear cost curve misses synergies, conditional text and metagame context. Use it to find suspects, then playtest._
