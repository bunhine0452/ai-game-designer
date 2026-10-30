# Playtest kit

A playtest answers a **question**, not "is it fun?". Write the question first, then build
the session around it. Use `playtest-analysis.md` to turn what you collect into findings.

## 1. Plan (one page)

```
Question:     Do first-time players understand that light is both health and currency by level 3?
Build:        vertical slice v0.4, levels 1–5, ~25 min
Players:      8–12 who match the target (played 2+ action roguelites this year); none from the team
Tasks:        play from the title screen until they choose to stop, or 30 minutes pass
We will know: ≥ 7 of 8 can explain the light rule unprompted; < 25% drop between levels 3 and 4
Collect:      observer sheet, event log (playtest_report.py format), 7-point questionnaire, 5-minute interview
Consent:      recording and data use explained and agreed; under-18 players need a guardian's consent
```

## 2. Observer sheet

Watch; don't help. If a player is stuck for 2 minutes, log it and give the smallest hint
(and log it as a `hint` event).

| Time | Level | What the player did or said (verbatim when possible) | Emotion (😀 😐 😣) | Intended experience? (Y/N) |
|---|---|---|---|---|
| 04:12 | Market | "Wait, why did my lantern dim?" Re-reads the HUD | 😣 | N |

Mark **firsts** (first death, first purchase, first time a mechanic is used deliberately).
They show what was learned and when.

## 3. Questionnaire (7-point, original items)

Ask right after play, before any discussion. 1 = strongly disagree, 7 = strongly agree.

| id | Item |
|---|---|
| `fun` | I enjoyed playing. |
| `clarity` | I understood what I was supposed to do and why. |
| `fairness` | When I failed, I felt it was my mistake rather than the game's. |
| `control` | The controls did what I meant them to. |
| `want_more` | I want to keep playing past where I stopped. |
| `<custom>` | One item that targets this test's question directly. |

Then three open questions: *What do you remember most? Where did you feel stuck or confused?
If you could change one thing, what would it be?* (the last one hints at a need, not a fix).

## 4. Event log for `playtest_report.py`

Log these events, from the build or by hand from video. Columns: `player,t,event,level,value`.

| event | When | level | value |
|---|---|---|---|
| `session_start` | play starts | – | – |
| `level_start` / `level_complete` | entering / clearing a level or segment | level id | – |
| `death` | every failure state | level id | – |
| `hint` | help asked for or given | level id | – |
| `quit` | the player stops by choice | level id | – |
| `rating` | each questionnaire answer | item id (`fun`, …) | 1–7 |

```bash
python3 scripts/playtest_report.py examples/playtest-log.csv --out ./out
```

The report gives the funnel (reached and completed per level), deaths per player, hints,
median time per level, quit points and questionnaire means. It flags `DROP_OFF` (over 25% lost
between levels), `DIFFICULTY_SPIKE`, `SLOW_LEVEL`, `QUIT_CLUSTER`, `HINT_HEAVY` and `LOW_RATING`.
The example shows a deliberately spiky "Bell Tower": 3 of 4 quits, 2.6 deaths per player
against a median of 0.6, and a low fairness score.

## 5. From flags to fixes

1. **Locate** with the numbers (which level, which players).
2. **Explain** with the observer notes and quotes. Numbers say *where*, people say *why*.
3. **Fix the cause** with the smallest change (difficulty, readability, teaching), stated as
   a hypothesis: "If we telegraph the bell swing 0.5 s earlier, deaths per player in Bell Tower
   drop below 1.5."
4. **Re-test** with new players and the same log format, and compare the two reports.

## Ethics and practicalities

- Pay or thank players. Never use a playtest to sell.
- Don't record faces or voices without explicit consent. Store logs without real names.
- With minors, follow local consent rules and keep sessions short.

## Sources
- [A20] Ambinder (2009), *Valve's Approach to Playtesting*. · [A19] RITE method.
- [A21] Drachen, Mirza-Babaei & Nacke (eds., 2018), *Games User Research*.
- [A22] Seif El-Nasr, Drachen & Canossa (eds., 2013), *Game Analytics*.
- Full bibliography: `research/SOURCES.md` in the repository.
