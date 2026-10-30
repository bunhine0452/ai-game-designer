# Combat math: damage, defense, TTK, DPS budgets

## Start from time-to-kill (TTK)

Decide how long a fight should take, then derive the numbers:

```
TTK ≈ effective_HP / effective_DPS
effective_DPS = damage_per_hit × hit_rate × accuracy × (1 + crit_chance × (crit_mult − 1)) × damage_multiplier
```

For shooters with magazines, include reloads:

```
shots_to_kill = ceil(HP / damage_per_shot_after_falloff)
TTK = (shots_to_kill − 1) / fire_rate      (+ reload time if shots_to_kill > magazine)
```

| Genre | Typical TTK target (design choice, not a rule) |
|---|---|
| Tactical shooter | very short (first accurate shot wins) |
| Arena / hero shooter | moderate (time to react and reposition) |
| ARPG trash mobs vs. bosses | under a second vs. tens of seconds to minutes |
| Fighting game round | tens of seconds |
| MOBA team fight | several seconds of burst plus sustained damage |

Short TTK rewards positioning and first shots. Long TTK rewards tracking, ability use and the
ability to respond.

## Defense formulas

| Formula | Damage taken | Properties |
|---|---|---|
| Subtractive | `max(min_dmg, dmg − armor)` | Simple; armor dominates small hits; needs a minimum-damage floor |
| Percentage (capped) | `dmg × (1 − min(cap, armor%))` | Easy to read; caps stop immunity |
| Hyperbolic (diminishing) | `dmg × K / (K + armor)` | Every point of armor adds the same % of *effective HP*: `EHP = HP × (1 + armor/K)`. Linear EHP growth, no immunity |
| Ratio (attack/defense) | `dmg × atk / (atk + def)` | Self-scaling across levels; common in JRPGs |

The hyperbolic form is popular because the marginal value of armor is constant in EHP terms,
so it never hits a cliff.

**Effective HP (EHP):** the raw damage needed to kill a target, counting mitigation. Compare
builds in EHP and effective DPS, not raw stats.

## DPS budgets

Give each role or unit a **power budget** and spend it across attributes:

1. Pick a baseline unit (budget = 100).
2. Assign value rates (1 DPS = x points, 1 EHP = y points, range, mobility, utility).
3. Each unit's attributes should sum to its budget (± a tolerance).
4. Fit the rates from data with `cost_curve.py` (treat "budget" as cost) and look for
   outliers.

Role trade-offs: high DPS ↔ low EHP (glass cannon), high EHP ↔ low DPS (tank), utility costs
damage (support). Without trade-offs, one role dominates.

## Scaling with level

- If player damage and enemy HP grow at the same rate, TTK stays constant and progression
  feels flat. Let the player's power outgrow content a little after each upgrade, then
  introduce stronger enemies (a sawtooth).
- Exponential stat growth needs exponential enemy scaling, which leads to number bloat. Prefer
  modest growth plus new mechanics (enemy behaviors, resistances).
- Separate **numbers that scale** (damage, HP) from **numbers that shouldn't** (cooldowns,
  movement speed, timing windows), which keep the feel consistent.

## Randomness in combat

- Damage variance (±10%) adds texture. Large variance makes outcomes feel arbitrary.
- Crit and dodge are output randomness. Cap them, or use pseudo-random distributions so streaks
  are less likely (some games raise the chance after each miss).
- Show hit chances honestly. If you quietly favor the player, keep it consistent, and expect
  players to notice the mismatch eventually.

## Worked mini-example

Target: a normal enemy dies in about 3 hits from a level-10 sword. Sword damage 40, crit 10% at
×2.0. Enemy HP 110, armor 20 (hyperbolic K = 100 → takes 100/120 = 83%).
Damage per hit = 40 × 0.83 × (1 + 0.1 × 1.0) = 36.7, so 110 / 36.7 ≈ 3 hits. ✓
At one attack per 0.6 s, TTK ≈ 1.2 s (the third hit lands at 1.2 s).

## Sources
- [C2] Schreiber & Romero (2021), *Game Balance*: damage formulas, TTK, scaling.
- [C1] Schreiber (2010), *Game Balance Concepts*.
- [B6] Griesemer (2010): how a 0.2 s change to time between shots reshaped Halo 3's sniper balance.
- [B5] Loudy & Campbell (2018): resource-from-combat design in DOOM.
- Full bibliography: `research/SOURCES.md` in the repository.
