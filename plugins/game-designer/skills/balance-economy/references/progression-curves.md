# Progression curves

## Think in time, not XP

What a player feels is **time per level** (or sessions per upgrade):

```
time_per_level(L) = xp_needed(L) / xp_income_per_hour(L)
```

Income usually grows too (better zones, gear, multipliers), so the shape of the XP table
alone tells you little. Model both. `progression_curve.py --xp-per-hour --income-growth`
does this.

## Curve families

| Family | XP to next level | Feel | Use when | Watch out for |
|---|---|---|---|---|
| Linear | `a + b·(L−1)` | Steady, predictable; each level a little longer | Short games, skill-capped progressions, battle passes | Late levels feel no different; low long-term pull |
| Polynomial (power) | `a·((L+c)/(1+c))^p`, p ≈ 1.5–3 | Fast early, steadily longer | Most RPG XP tables | Very high ratios at low L when c = 0 (use an offset c) |
| Exponential | `a·g^(L−1)`, g ≈ 1.05–1.25 | Each level a fixed % harder; explodes late | Idle games and prestige loops (with exponential income); soft caps | Needs exponential rewards or it becomes a wall |
| Logistic (S-curve) | `a + (cap−a)/(1+e^(−k(L−m)))` | Slow start, fast middle, plateau | Mastery tracks with a natural ceiling; soft level caps | Plateau can feel like no progress; use it with other goals |
| Piecewise | different formulas per bracket | Designed eras (leveling, then endgame) | Live games: a fast leveling phase, then horizontal progression | Visible discontinuities: smooth the joins |

Choosing:
1. **Fix the anchor:** time for level 1→2 (usually 2–10 minutes; the first session should
   give several levels).
2. **Fix the total:** hours to the cap (genre-dependent: a 10–15 h action RPG, a 40–80 h JRPG,
   hundreds of hours for an MMO at launch).
3. **Pick the shape** by how the late game should feel. Then solve the shape parameter for the
   total (`--total` does this while keeping the anchor).

## Diagnostics to check

- **Half-XP level:** the level at which half of all XP has been earned. Above 80% of the
  levels means the grind is back-loaded, so the late game carries most of the time.
- **Time-per-level walls:** a jump of more than ~1.6× from one level to the next, on levels
  that take meaningful time.
- **Last/first ratio:** how much longer the last level takes than the first. Very high
  ratios are fine for an endgame grind, but risky if the cap marks the story's end.
- **Content pacing:** does content (zones, quests, abilities) arrive at the same rate as
  levels? Levels without new content feel empty.

## XP sources

- **Primary loop XP** (kills, quests) should cover most leveling.
- **Catch-up XP** (rested XP, first-win-of-day bonuses, bonuses for under-leveled players) helps
  returning and casual players without punishing absence.
- **Avoid obligation framing:** bonuses for showing up are fine; *penalties* for not
  showing up (decay, loss) are a dark pattern (*playing by appointment*).

## Worked example (from `examples/rpg-xp-table.md`)

Poly curve: exponent 2.2, offset 5, 300 XP for level 1→2, income 3,000 XP/h growing 5% per
level. Result: 654,915 XP to level 50, about 44 h. Level 1 takes 6 min and the slowest level
75 min. The half-XP level is 40 (80%). The curve rises then flattens (income growth catches up
late), which suits a story RPG whose ending sits near the cap.

## Sources
- [C1] Schreiber (2010), *Game Balance Concepts*. https://gamebalanceconcepts.wordpress.com/
- [C2] Schreiber & Romero (2021), *Game Balance*, CRC Press.
- [B24] Pecorella (2016), *The Math of Idle Games*: exponential cost vs. linear production.
- [A15] Zagal et al. (2013): playing by appointment as a dark pattern.
- Full bibliography: `research/SOURCES.md` in the repository.
