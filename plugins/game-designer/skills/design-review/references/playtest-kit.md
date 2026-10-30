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
| `curious` | I wanted to find out what would happen next. |
| `challenge` | The game was hard in a way I enjoyed. |
| `pressure` | I felt I had to keep playing, more than I wanted to. *(reversed: a high mean is the warning)* |
| `<custom>` | One item that targets this test's question directly. |

`curious`, `challenge` and `pressure` cover three fun drivers: curiosity, enjoyable challenge,
and playing because you have to rather than because you want to (see `fun-diagnosis.md`).
These items are original and not validated. To compare across studies, use a validated
instrument as published instead: the miniPXI (11 items) for player experience, or BANGS for
need satisfaction and frustration.

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
| `outcome` | a contest ends (fight, race, match, boss) | level id | final margin −1..1: + the player won, − lost, 0 = dead even (e.g. the winner's health left) |
| `explore` | an optional action: a side path, an unexplained mechanic tried, lore read | level id | – |
| `prefer` | after playing two versions, which one the player enjoyed more | comparison id | variant (`A`, `B`, …) |
| `free_play` | time played after "you can stop now" (see below) | – | seconds (0 = stopped at once) |
| `rating` | each questionnaire answer | item id (`fun`, …) | 1–7 |

```bash
python3 scripts/playtest_report.py examples/playtest-log.csv --out ./out
```

The report gives the funnel (reached and completed per level), deaths per player, hints,
median time per level, quit points and questionnaire means. It flags `DROP_OFF` (over 25% lost
between levels), `DIFFICULTY_SPIKE`, `SLOW_LEVEL`, `QUIT_CLUSTER`, `HINT_HEAVY` and `LOW_RATING`.
With `outcome` and `explore` events it adds a fun-driver table (close and one-sided contests,
optional actions per player) and flags `ONE_SIDED` (half or more of a level's contests decided
by ±0.6 or more), `LOW_CURIOSITY` (a level's optional actions under a quarter of the median) and
`PRESSURE` (the `pressure` item averaging 4.5 or more).
The example shows a deliberately spiky "Bell Tower": 3 of 4 quits, 2.6 deaths per player
against a median of 0.6, and a low fairness score. Its duel is also one-sided (11 of 11
contests decided by a wide margin) and nobody explores there, while the Market chase is close
every time.

## 5. Watch free choice, and compare instead of rating

Two measures are more trustworthy than any rating:

- **Free-choice play.** When the planned tasks are done, say: "That's everything we needed. You
  can stop now, or keep playing as long as you like." Leave the room or look away, and log how
  long they keep going as `free_play`. Playing without being asked is the standard behavioural
  sign of intrinsic motivation; in one study children chose the intrinsically motivating version
  of a game seven times longer [A63].
- **A/B comparisons.** When you are deciding between two versions (a telegraph timing, a camera,
  a reward), let each player try both in counterbalanced order (half see A first) and ask
  "Which did you enjoy more?". Log it as `prefer`. Rank-based answers are more reliable than
  ratings [A54]. With two versions, the report adds an exact sign test; at 12 players, 10 of 12
  is the first clear result (p ≈ 0.04), so treat 8 or 9 of 12 as a lead to re-test, not a verdict.

Memory favours peaks and endings [A62], so keep the observer's moment-by-moment notes beside the
questionnaire, and don't let a strong ending hide a weak middle.

The report flags `LOW_FREE_PLAY` when fewer than a quarter of players keep going for a minute.
The example log compares the Bell Tower as it is (A) with the bell swing telegraphed 0.5 s
earlier (B): 9 of 12 chose B (p = 0.15, a lead), and half the players kept playing a minute or
more.

## 6. From flags to fixes

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
- [A34] outcome uncertainty · [A35] curiosity · [A38] BANGS · [A39] motivation and well-being · [A47] miniPXI.
- [A54] ranks over ratings · [A62] peak-end effects · [A63] free-choice play.
- Full bibliography: `research/SOURCES.md` in the repository.
