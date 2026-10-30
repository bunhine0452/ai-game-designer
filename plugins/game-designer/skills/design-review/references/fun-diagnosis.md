# Fun diagnosis

Use this when the question is "is it fun?" or "why isn't it fun?". Don't answer with one
verdict. Score each **driver** separately, find the weakest one, and fix that first. The evidence
behind each driver is in `fun-curve` → `references/what-makes-it-fun.md`.

## 1. Score the drivers

For each driver, write **strong / weak / unknown** with the evidence (an observation, a number,
a quote). "Unknown" is an honest answer and turns into a playtest question.

| Driver | Ask | Weak when you see | Smallest fixes to try |
|---|---|---|---|
| **Challenge** | Is the next obstacle slightly above the player's skill, and does failing feel fair? | Sighs and autopilot play (too easy); "that's cheap" and quitting at one spot (unfair) | Re-order to a sawtooth; telegraph earlier; move checkpoints; add an optional harder goal |
| **Outcome uncertainty** | Is the result in doubt until late? | Most contests decided early; players stop trying once ahead or behind | Late swings, a harder final phase, closer matchmaking, visible comeback options |
| **Curiosity** | What will the player want to find out in the next five minutes? | No questions asked aloud; nobody tries optional things; play time short even when ratings are fine | Reveal a new rule or combination on a rhythm; graded results; leave visible unexplained things |
| **Feedback** | Does every action confirm itself and show its outcome and size? | "Did that hit?"; mashing; or players missing events in the effects | Add legible feedback first, then emphasis; scale effects to the outcome; cut noise |
| **Autonomy** | Do players choose what to do and how? | One dominant strategy; "I had to"; skipping text to get back control | Add viable options; make goals self-chosen; remove forced sequences |
| **Competence** | Can players see themselves improving? | Blame on luck or the game; no visible mastery curve | Show improvement (times, ranks, unlocks by skill); make loss causes readable |
| **Relatedness** | Is there someone to play with, against or for? (if the design is social) | Silence in co-op; newcomers stranded; toxicity | Shared goals, emotes, spectating, protective matchmaking |
| **Meaning** | Will anything stay with the player afterwards? | Nothing named in "what do you remember most?" | A quiet beat after a peak; a character or place to care about; a choice with a felt consequence |

Rate the **frustration** side of the three needs separately from satisfaction. A feature can
satisfy competence (a fair boss) and frustrate autonomy (you must grind to reach it).

## 2. Find the bottleneck

- The weakest driver that the design pillars care about is the bottleneck. A cozy game can
  ignore outcome uncertainty; a competitive one can't.
- Check the interest curve (`fun-curve`) at the same time. A driver can be strong overall and
  missing at the moment players quit.
- Engagement numbers alone don't diagnose fun. Long sessions with a high `pressure` score mean
  players feel they have to play, which is a warning, not a win.

## 3. Write findings as predictions

Each finding names the driver, the evidence and a testable fix:

```
[P1] Outcome uncertainty is weak in arena fights. 7 of 10 logged fights ended with the
player above 80% health (one-sided). Fix: the last wave spawns from both sides.
Prediction: one-sided outcomes drop below 40%, and the "challenge" rating rises above 5.
```

Use the severity rubric (`severity-rubric.md`) as usual. A bottleneck driver usually rates P1:
it limits everything else.

## 4. Measure in the next playtest

- Log `outcome` events (final margin) and `explore` events (optional actions) as described in
  `playtest-kit.md`. `scripts/playtest_report.py` reports one-sided outcomes and exploration per
  level and flags `ONE_SIDED`, `LOW_CURIOSITY` and `PRESSURE`.
- Add the `curious`, `challenge` and `pressure` items to the questionnaire.
- For results you want to compare across studies or publish, use a validated instrument instead
  of the kit's original items: the miniPXI (11 single items, one per player-experience
  construct) or BANGS (need satisfaction and frustration). Use them as published, and check
  their terms of use.

## Sources
- See `fun-curve` → `references/what-makes-it-fun.md` for the evidence per driver ([A32]–[A46]).
- [A9] Ryan, Rigby & Przybylski (2006), SDT and games. · [A38] BANGS. · [A47] miniPXI.
- Full bibliography: `research/SOURCES.md` in the repository.
