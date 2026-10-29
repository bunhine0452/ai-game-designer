# Worked example: finding off-curve cards

**Set:** 20 fictional creature cards with `cost, attack, health, draw, taunt, charge`. The set
was built on a hidden rule (cost ≈ (attack + health)/2 − 0.5 + draw + taunt/2 + charge) and
three cards were planted off-curve.

```bash
python3 scripts/cost_curve.py examples/card-set.csv --robust --title "Starter set cost curve" --out examples/output
```

![Cost curve](output/card-set_fit.png)

## Fitted value of each attribute (cost units)

| Attribute | Fitted | Hidden rule |
|---|---|---|
| intercept | −0.32 | −0.5 |
| attack | +0.59 | +0.5 |
| health | +0.40 | +0.5 |
| draw | +1.20 | +1.0 |
| taunt | +0.64 | +0.5 |
| charge | +0.78 | +1.0 |

The fit recovers the rule closely from just 20 integer-costed cards. The gaps come from
rounding costs to whole numbers.

## Outliers found

| Card | Cost | Fair | Verdict | Suggested change |
|---|---|---|---|---|
| Comet Scout | 2 | 4.2 | Undercosted (too strong) | Cost 4, or drop charge or draw |
| Glass Tyrant | 3 | 4.8 | Undercosted (too strong) | Cost 5, or 6/4 → 4/3 |
| Rust Golem | 5 | 3.3 | Overcosted (too weak) | Cost 3, or add a meaningful effect |

**Why `--robust`:** without it, the outliers bend the curve and the fit misses Comet Scout
(it finds only 2 of 3). The robust mode fits, drops points with |z| > 2, refits, then judges
every card against the clean curve.

## Limits
A linear curve doesn't price synergy, conditional text or the metagame. Use these flags as
suspects for playtesting, then check pick and win rates once the cards are live.
