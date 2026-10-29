# Severity rubric

## Levels

| Level | Definition | Examples |
|---|---|---|
| **P0 (blocker)** | Breaks the core experience for most players, *or* creates legal or ethical exposure | Core verb not fun; progression soft-lock; undisclosed paid odds; paid random items targeted at minors |
| **P1 (major)** | Substantially harms a target aesthetic or pillar for many players | Dominant strategy; a wall in the first hour; unreadable threats; inflation |
| **P2 (moderate)** | Noticeable friction or a missed opportunity, for some players or some of the time | A flat mid-level stretch; a weak reward moment; a missing accessibility option |
| **P3 (polish)** | Minor or cosmetic | Inconsistent icon; small timing tweak |

## Prioritization score

```
priority = impact (1-3) × reach (1-3) × confidence (0.5 / 0.75 / 1.0)
then sort by priority, breaking ties by lower cost (S < M < L)
```

- **Impact:** 3 = blocks or severely harms the target experience; 2 = clearly reduces it;
  1 = minor.
- **Reach:** 3 = most players; 2 = a significant segment (new players, a platform, one
  archetype); 1 = edge cases.
- **Confidence:** 1.0 = observed in playtests or data; 0.75 = strong principle plus
  material evidence; 0.5 = hypothesis.
- **Cost:** S = hours to a day; M = days to a week; L = weeks or more, or a redesign.

Ethics and legal issues are P0 regardless of score.

**Quick wins** are P1/P2 issues with cost S. List them separately so the team can act today.

## Writing a good issue

| Field | Good | Bad |
|---|---|---|
| Issue | "Players don't notice the dash cooldown" | "Dash is bad" |
| Evidence | "5/8 testers dashed into spikes during cooldown; 3 said 'it didn't work'" | "It feels off" |
| Why | "Feedback isn't readable: no cooldown indicator (game feel)" | "Players hate it" |
| Fix | "Add a 2-frame flash plus a sound when dash recharges; dim the character outline during cooldown" | "Improve feedback" |
| Verify | "Next playtest: fewer than 2/8 testers dash during cooldown" | — |

## Sources
- [A20] Ambinder (2009): playtests as experiments. · [A19] RITE method.
- [A21] *Games User Research* (2018): severity and frequency in usability findings.
- Full bibliography: `research/SOURCES.md` in the repository.
