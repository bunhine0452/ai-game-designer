# Playtest analysis

## From raw notes to findings

1. **Atomize.** Split notes into single observations: `participant, time, observation,
   quote (optional)`. Keep what happened separate from what you think it means.
2. **Cluster.** Group observations that share a cause into one issue. Name it by the
   player-facing problem ("doesn't notice the cooldown"), not by a solution.
3. **Count.** Report frequency as **n of N** participants. One strong reaction can matter,
   but label it as an isolated case.
4. **Rate** with the severity rubric (impact × reach × confidence).
5. **Interpret** with principles: trace aesthetic → dynamic → mechanic (MDA). For pacing,
   build the observed curve (`fun-curve/references/measuring-fun.md`).
6. **Recommend** specific changes, each with a *verify by* metric for the next round.
7. **Triangulate** with telemetry where possible: quit points, deaths, time per segment, funnels.

## Reading what players say

| Players say | Usually reliable for | Usually unreliable for |
|---|---|---|
| "This was boring / confusing / frustrating" | *That* something is wrong, and roughly where | *What* the fix is |
| "Add feature X" | A hint at an unmet need | The right solution |
| "It was fine" | Little. Probe with specific moments | — |
| Body language, idle time, retries | Engagement, frustration, persistence | Reasons (ask afterwards) |

Ask about specific moments ("What were you trying to do when…?"). Avoid leading questions
("Did you like the boss?" → "What do you remember about the boss?").

## Method fit

- **RITE:** when a problem's cause and fix are obvious (UI, tutorial text), fix it before the
  next participant and confirm.
- **Comparative tests:** for balance or pacing variants, use A/B builds with the same task
  and compare metrics.
- **Repeated sessions:** for retention and mastery questions, have the same players return over
  days. The first-session reaction isn't enough.

## Finding template

```
F-03 · "Players miss the light-bank prompt at the end of a run" · 6 of 8 · P1
Observations: P2 (19:40) left the summary screen without banking; P5: "where did my light go?"
Interpretation: the bank action sits in a low-contrast corner during a celebratory animation
(readability; feedback hierarchy)
Recommendation: auto-bank by default, show a "+120 light banked" counter animating into the city icon
Verify by: next round, ≥ 7/8 can say how much light they banked
```

## Sources
- [A20] Ambinder (2009), *Valve's Approach to Playtesting*. · [A19] RITE.
- [A21] Drachen, Mirza-Babaei & Nacke (eds., 2018), *Games User Research*.
- [A22] *Game Analytics* (2013). · [A5] MDA.
- Full bibliography: `research/SOURCES.md` in the repository.
