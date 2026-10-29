# Cost curve: Starter set cost curve

![Cost curve](card-set_fit.png)

Fit on 20 items: R² = 0.811, RMSE = 0.76 cost. Flag threshold ±1.14.

## Value of each attribute (in cost units)

| Attribute | Cost per point |
|---|---|
| (intercept) | -0.322 |
| attack | +0.588 |
| health | +0.398 |
| draw | +1.195 |
| taunt | +0.639 |
| charge | +0.778 |

_The intercept is the baseline cost every item pays (e.g. the card itself). A negative weight usually marks a drawback; if a 'positive' attribute fits negative, it is overvalued in the current set or confounded with another column._

## Outliers

- **Comet Scout** costs 2, fair ≈ 4.2 (+2.2): undercosted (too strong); raise its cost or trim its stats.
- **Glass Tyrant** costs 3, fair ≈ 4.8 (+1.8): undercosted (too strong); raise its cost or trim its stats.
- **Rust Golem** costs 5, fair ≈ 3.3 (-1.7): overcosted (too weak); lower its cost or add value.

## All items

| Item | Cost | Fair | Residual | Verdict |
|---|---|---|---|---|
| Comet Scout | 2 | 4.21 | +2.21 | undercosted (too strong) |
| Glass Tyrant | 3 | 4.79 | +1.79 | undercosted (too strong) |
| Lantern Moth | 2 | 2.26 | +0.26 | on curve |
| Moss Sprite | 1 | 1.25 | +0.25 | on curve |
| Sky Herald | 5 | 5.21 | +0.21 | on curve |
| Iron Warden | 3 | 3.08 | +0.08 | on curve |
| Ash Sentinel | 4 | 4.07 | +0.07 | on curve |
| Ember Pup | 1 | 1.06 | +0.06 | on curve |
| Tide Squire | 2 | 2.05 | +0.05 | on curve |
| Bramble Ogre | 4 | 4.02 | +0.02 | on curve |
| Dune Racer | 3 | 3.01 | +0.01 | on curve |
| Granite Colossus | 6 | 5.99 | -0.01 | on curve |
| Storm Lancer | 5 | 4.99 | -0.01 | on curve |
| Reef Hydra | 7 | 6.97 | -0.03 | on curve |
| Tiny Tactician | 2 | 1.86 | -0.14 | on curve |
| Thorn Bastion | 6 | 5.85 | -0.15 | on curve |
| Marsh Witch | 3 | 2.84 | -0.16 | on curve |
| Archive Owl | 4 | 3.83 | -0.17 | on curve |
| Quill Imp | 1 | 0.66 | -0.34 | on curve |
| Rust Golem | 5 | 3.27 | -1.73 | overcosted (too weak) |

_A linear cost curve misses synergies, conditional text and metagame context. Use it to find suspects, then playtest._
