# Measuring fun

A predicted curve is a hypothesis. Playtests and telemetry test it. Valve frames it the
same way: a design is a hypothesis and a playtest is an experiment.

## Playtest methods

| Method | Best for | How | Pitfalls |
|---|---|---|---|
| Direct observation | Confusion, emotion, where players look | Watch silently; note time stamps of confusion, delight, frustration | Observer influence; don't help |
| Think-aloud | Players' mental models | Ask players to narrate what they think and intend | Slows play; less natural intensity |
| Post-session interview | Memorable moments, reasons | Open questions: "What do you remember? Where did you want to stop?" | Memory favors the peak and the end |
| RITE (Rapid Iterative Testing and Evaluation) | Fast UI/UX and tutorial fixes | Fix a clear problem after even one participant; confirm with the next | Only for problems with an obvious cause |
| Moment-by-moment self-report | Observed intensity curve | After play, the player draws their interest over a timeline or rates video segments | Retrospective bias; pair with telemetry |
| Biometrics (heart rate, skin conductance) | Arousal peaks | Sync with gameplay video | Arousal isn't enjoyment; expensive |

**Sample sizes:** 5–8 players per round find most usability problems. Pacing and difficulty
need more (15–30+), because variance between players is the point. Recruit the target
audience, not friends and developers.

## Questionnaires

- **PXI (Player Experience Inventory)**: measures functional consequences (audiovisual appeal,
  challenge, ease of control, clarity of goals, progress feedback) and psychosocial ones
  (mastery, curiosity, immersion, autonomy, meaning). Validated across five studies.
  A short miniPXI exists. *Recommended default.*
- **PENS**: autonomy, competence, relatedness, presence and intuitive controls. Free for
  academic use; commercial use needs permission.
- **GEQ**: very widely used, but a 2018 systematic review found inconsistent use and didn't
  confirm its proposed factor structure. Use it with caution and don't compare scores across
  studies.

Ask a few questions right after the segment you care about rather than one long survey at
the end.

## Telemetry signals

| Signal | What it suggests | Turn it into beats |
|---|---|---|
| Quit location and time (last event before session end) | Where interest fell below "keep going" | Clusters of quits mark low beats or walls |
| Deaths / failures per segment | Difficulty peaks and spikes | High deaths plus high retries = hard fun; high deaths plus quits = wall |
| Time per segment vs. intended | Confusion or grind | Much longer than intended = a flat zone or getting lost |
| Retries before success | Persistence | Falling retries over time = learning (good) |
| Input rate, idle time, pauses | Engagement or boredom | Long idles in non-menu play = disengagement |
| Optional content uptake | Curiosity, autonomy | Low uptake = the option isn't attractive or visible |
| Session length and frequency | Fit with context | Compare to the target session length |
| D1 / D7 / D30 retention | Longer-term interest | Compare cohorts before and after a change |
| Funnel completion (tutorial, first boss, chapter 2) | Where the curve loses people | Plot the funnel next to the interest curve |

**Benchmarks:** mobile retention is low across the board. 2024 benchmark data put median D1
in the low 20s % and top-quartile D1 around 27%. Compare against your own earlier cohorts and
the closest genre, not a global average.

## Mapping observations to an observed curve

1. Split the experience into the same segments as the predicted beat list.
2. For each segment, set observed intensity from player-reported intensity (if collected),
   adjusted by behavioral evidence: −2 for idle or quits clustered there, +1 for voluntary
   retries or optional uptake.
3. Plot observed and predicted together (run `fun_curve.py` on each and compare charts).
4. Large gaps are the problems. Rank them by how many players they affect.

## Ethics of measurement

Tell playtesters what is recorded. Get consent for video and biometrics. Anonymize
telemetry. Don't optimize a metric (session length, spend) against player well-being.
`design-review` covers dark patterns.

## Sources

- [A20] Ambinder (2009), *Valve's Approach to Playtesting*. https://cdn.fastly.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf
- [A19] Medlock et al. (2002), RITE method (summary: https://measuringu.com/rite-method/).
- [A21] Drachen, Mirza-Babaei & Nacke (eds., 2018), *Games User Research*.
- [A22] Seif El-Nasr, Drachen & Canossa (eds., 2013), *Game Analytics*.
- [A25] Vanden Abeele et al. (2020), PXI. · [A23] IJsselsteijn et al. (2013), GEQ. · [A24] Law, Brühlmann & Mekler (2018), GEQ review.
- [A9] Ryan, Rigby & Przybylski (2006), PENS origin.
- [A26] GameAnalytics (2025), *Mobile Gaming Benchmarks*.
- Full bibliography: `research/SOURCES.md` in the repository.
