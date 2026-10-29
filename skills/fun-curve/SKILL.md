---
name: fun-curve
description: Designs, plots and critiques interest curves (fun curves), flow and pacing for a play session, level, run, chapter or whole game. Use when the user asks about pacing, tension and release, intensity graphs, difficulty curves, flow channel, boredom or frustration points, a boring middle, climax placement, session length, game feel or juice, or wants a beat list plotted and diagnosed, or wants playtest or telemetry data turned into a curve. Runs a script that flags missing hooks, flat zones, peaks without relief, early climaxes and non-escalating peaks. Also triggers on 재미 곡선, 관심 곡선, 페이싱, 완급 조절, 긴장과 이완, 난이도 곡선, 몰입, 지루한 구간, 타격감; 面白さの曲線, 興味曲線, ペーシング, 緩急, 緊張と緩和, 難易度曲線, 手触り; 趣味曲线, 兴趣曲线, 节奏, 心流, 难度曲线, 打击感; curva de diversión, ritmo, curva de dificultad.
---

# Fun curve: interest, flow and pacing

Turn "it feels slow in the middle" into a plotted curve, named problems and concrete beat
changes. Work at whatever scale the user cares about. Curves nest: a whole game is made of
sessions, sessions of levels or runs, and levels of encounters. Each scale needs its own
good shape.

**Language:** answer in the user's language. On first use, write each technical term
localized with the English term in parentheses, e.g. `관심 곡선 (Interest Curve)`. Standard
terms are in `references/glossary.md` if bundled, or `../game-design/references/glossary.md`.
Script output is English; translate finding names when summarizing.

## Workflow

### 1. Fix the scale and the target shape
Ask (or infer) what is being plotted: one encounter, a level, a run or session, a chapter,
or the whole game. Also ask for the intended duration and the genre. Look up the typical
shape for that genre and scale in `references/pacing-models.md` and state the target shape
in one sentence before analysing ("a 20-minute run should hook within 2 minutes, sawtooth
upward, and peak in the last 10%").

### 2. Get a beat list
A beat is `time, intensity, type, label`:
- **time**: minutes by default (or `mm:ss`, or another unit with `--unit`).
- **intensity**: 0–10 *felt* engagement or tension, not action density. A silent corridor
  with a stalker nearby can be an 8. Use the rubric in `references/beat-list-format.md`.
- **type**: a short category (combat, puzzle, explore, story, reward, shop, rest, boss,
  scare…). It drives the monotony checks and the chart legend.
- **label**: what happens.

If the user has a level outline, a script, playtest notes or telemetry instead of a beat
list, **draft the beat list yourself**, show it as a table, and continue straight into the
analysis. Invite corrections at the end rather than stopping to ask. For telemetry, map observed signals to intensity as explained in
`references/measuring-fun.md` (deaths, quit points, input rate, pauses).

### 3. Run the analysis
Save the beats as CSV (header `time,intensity,type,label`; optional `# title:` and
`# unit:` comment lines) or JSON, then run:

```bash
python3 scripts/fun_curve.py beats.csv --out ./fun_curve_out --reference
```

Useful flags: `--title`, `--unit s`, `--label-all`, `--format svg`, `--no-plot`. All
thresholds can be changed (`--hook-window`, `--hook-min`, `--flat-tolerance`, `--flat-min`,
`--peak-min`, `--relief-window`, `--relief-drop`, `--climax-min`, `--high`, `--low`,
`--sustain-max`). Adjust them for the genre: horror tolerates longer low-intensity dread,
and arcade loops may end on the peak with no resolution.

The script writes `<stem>_curve.png` (if matplotlib is installed), `<stem>_report.md`,
`<stem>_report.json` and `<stem>_resampled.csv`, and prints an ASCII curve. Without
matplotlib it still produces the text, JSON and CSV outputs. Show the user the chart and
the findings.

**If code execution is unavailable,** apply the same checks by hand to the beat table:

| Check | Rule (defaults) |
|---|---|
| Hook | some beat ≥ 6 within the first 10% of the duration |
| Flat zone | the curve stays within a 1-point band for ≥ 12% of the duration |
| Relief | after each peak ≥ 7 (except the climax), a drop of ≥ 2.5 within 12% of the duration |
| Sustained peak | no continuous stretch ≥ 8 longer than 15% of the duration |
| Climax | the highest beat sits at ≥ 70% of the duration |
| Escalation | peaks after the hook trend upward |
| Monotony | no ≥ 4 consecutive beats of one type, and no single-type run covering ≥ 25% |
| Load | ≤ 35% of the time at ≥ 8, and ≤ 40% of the time at ≤ 3 |

### 4. Interpret and fix
For each finding, explain **why it hurts the experience** (flow, fatigue, anticipation,
contrast) and propose a **specific beat change**: what to insert, cut, move or re-tune, with
the new time and intensity. Prioritize:
1. Missing hook and early climax (they decide whether players stay and how the experience
   is remembered).
2. Low flat zones (boredom and quit risk), then peaks without relief and sustained peaks
   (fatigue).
3. Escalation, monotony and load balance.

Then **write the revised beat list, re-run the script and show before/after metrics.**
Changing a curve on paper is cheap. Say plainly that the curve is a prediction to be
checked in playtests.

### 5. Connect to flow and difficulty
When the issue is difficulty rather than content order (spikes, walls, players bouncing
off), use `references/flow-and-difficulty.md`: the flow channel, sawtooth ramps,
player-chosen challenge over hidden adjustment, and fail-state design. When the issue is
that moments feel weak rather than badly ordered, use `references/game-feel.md` (juice,
forgiveness windows, feedback layering).

### 6. Plan validation
End with how to check the curve against real players: what to observe, which telemetry to
log (quit points, deaths, session length, time per segment), and what result would show the
fix worked. See `references/measuring-fun.md`.

## Output format

1. Target shape (one sentence) and the scale being analysed.
2. Beat table (drafted or given).
3. Chart plus a short read of the curve.
4. Findings ranked by severity, each as problem → why it matters → exact beat change.
5. Revised beat table and before/after metrics (pacing health, climax position, share of
   time at high/low intensity).
6. Validation plan.

## Principles

- Contrast creates intensity. Peaks need valleys, and a valley with purpose (anticipation,
  reward, story) is not downtime.
- Players remember the peak and the end best, so protect both (climax late, short
  resolution).
- Escalate the kind of challenge, not just the numbers: new combinations, a twist on a known
  mechanic, higher stakes.
- The "pacing health" score is a heuristic summary, not a measure of quality. Never present
  it as one.

## References

- `references/interest-curves.md`: Schell's interest curve, nested curves, shapes, and how to
  read a curve.
- `references/pacing-models.md`: tension and release, the L4D AI Director, Alien: Isolation's
  menace, kishōtenketsu, session-length design, and typical shapes per genre.
- `references/flow-and-difficulty.md`: flow theory, Chen's flow channel, DDA, sawtooth
  difficulty, failure design.
- `references/game-feel.md`: Swink's game feel, juice, forgiveness techniques, cautions.
- `references/measuring-fun.md`: playtest methods, questionnaires, telemetry signals, and
  mapping data to beats.
- `references/beat-list-format.md`: input format and the intensity rubric.
- `examples/`: a 20-minute roguelite run (healthy), a horror chapter (deliberately flawed),
  their outputs, and a worked fix in `examples/horror-fix-walkthrough.md`.
