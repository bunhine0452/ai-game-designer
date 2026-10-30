# Playtest report: playtest-log

- Players: **12**
- Finished the last level: **8 of 12**

## Funnel and difficulty

| Level | Reached | Completed | Completion | Deaths / player | Hints | Median time | Quits here |
|---|---|---|---|---|---|---|---|
| Docks | 12 of 12 | 12 | 100% | 0.1 | 0 | 4.1 min | 0 |
| Market | 12 of 12 | 12 | 100% | 0.4 | 0 | 5.6 min | 0 |
| Sewers | 12 of 12 | 11 | 92% | 0.7 | 7 | 5.8 min | 1 |
| Bell Tower | 11 of 12 | 8 | 73% | 2.6 | 3 | 10.4 min | 3 |
| Rooftops | 8 of 12 | 8 | 100% | 0.6 | 0 | 7.8 min | 0 |

## Fun drivers: outcomes and curiosity

Close = final margin within ±0.2; one-sided = ±0.6 or more. Optional actions come from `explore` events.

| Level | Contests | Close | One-sided | Wins / losses | Optional actions / player |
|---|---|---|---|---|---|
| Docks | 0 | – | – | – | 1.7 |
| Market | 12 | 100% | 0% | 5 / 7 | 1.3 |
| Sewers | 0 | – | – | – | 1.2 |
| Bell Tower | 11 | 0% | 100% | 4 / 7 | 0.2 |
| Rooftops | 0 | – | – | – | 1.0 |

## Questionnaire (1–7)

| Question | n | Mean | Range |
|---|---|---|---|
| challenge | 12 | 3.8 | 3–5 |
| clarity | 12 | 4.2 | 3–6 |
| curious | 12 | 5.1 | 4–6 |
| fairness | 12 | 3.2 | 2–5 |
| fun | 12 | 4.8 | 3–7 |
| pressure (reversed: high is bad) | 12 | 2.2 | 1–3 |
| want_more | 12 | 4.5 | 2–6 |

## Flags

- DROP_OFF: 11 reached Bell Tower but only 8 reached Rooftops (27% lost).
- DIFFICULTY_SPIKE: Bell Tower averages 2.6 deaths per player (median across levels 0.6).
- QUIT_CLUSTER: 3 of 4 quits happened in Bell Tower.
- LOW_RATING: 'fairness' averages 3.2 / 7 (n=12).
- LOW_RATING: 'challenge' averages 3.8 / 7 (n=12).
- ONE_SIDED: Bell Tower: 100% of 11 contests were decided by a wide margin (4 wins, 7 losses). Close contests are more enjoyable than blowouts.
- LOW_CURIOSITY: Bell Tower: 0.2 optional actions per player against a median of 1.2. Nothing here invites players to find something out.

Numbers show *where* players struggled, not *why*. Pair each flag with observer notes
(see `references/playtest-kit.md`) before deciding on a fix, and re-test the fix.
