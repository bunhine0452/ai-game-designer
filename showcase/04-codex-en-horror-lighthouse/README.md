# Low Tide — 40-minute horror chapter

Start with [chapter design and revision rationale](chapter_design.md), the [before/after comparison](analysis/comparison.md), and the [accessibility checklist](accessibility_checklist.md).

The first draft produced **12 pacing findings**. The revised draft produced **zero under identical thresholds**: the hook now lands at 2 min, rising threat peaks have protected recovery, and the climax moves from 12 min (30%) to 38 min (95%). Both versions span 40 min. Predicted time at intensity ≥8 falls from 21.9% to 7.7%; the heuristic score rises from 0/100 to 100/100. These are design predictions, not playtest results or a quality rating. The next step is to test duration, recovery and final-escape clarity with players.

Accessibility requirements cover redundant audio cues, beam/flashing and motion review, remapping and input alternatives, subtitles/captions, and chapter-specific acceptance tests for PC and console. All implementation checks remain pending build verification. Guidance is linked to primary sources inside the checklist.

## Deliverables

| File | Purpose |
|---|---|
| [chapter_design.md](chapter_design.md) | Target shape, assumptions, all 12 fixes, revised playable sequence, checkpoints and playtest plan |
| [beats_before.csv](beats_before.csv) | Original 21-sample beat list, minutes and predicted intensity |
| [beats_after.csv](beats_after.csv) | Revised 23-sample beat list, minutes and predicted intensity |
| [accessibility_checklist.md](accessibility_checklist.md) | Chapter-specific requirements, owners, test matrix and source links |
| [analysis/comparison.md](analysis/comparison.md) | Before/after metrics and combined chart |
| [analysis/comparison.svg](analysis/comparison.svg) | Standalone vector chart, dashed original and solid revised, with text description |
| [analysis/beats_before_report.md](analysis/beats_before_report.md) | Initial findings, ASCII chart and full original beat table |
| [analysis/beats_after_report.md](analysis/beats_after_report.md) | Rerun findings, ASCII chart and full revised beat table |
| [analysis/beats_before_report.json](analysis/beats_before_report.json) | Machine-readable original diagnosis and beat list |
| [analysis/beats_after_report.json](analysis/beats_after_report.json) | Machine-readable revised diagnosis and beat list |
| [analysis/beats_before_resampled.csv](analysis/beats_before_resampled.csv) | Interpolated original curve used for time-share estimates |
| [analysis/beats_after_resampled.csv](analysis/beats_after_resampled.csv) | Interpolated revised curve used for time-share estimates |
| [scripts/fun_curve.py](scripts/fun_curve.py) | Unmodified analyzer copied from the local fun-curve skill |
| [scripts/build_comparison.py](scripts/build_comparison.py) | Dependency-free chart and comparison builder |
| [reproduce.md](reproduce.md) | Exact commands, thresholds and environment notes |
| [README.md](README.md) | File index and key conclusions |

The analyzer ran successfully using Python 3 without matplotlib. Its reports contain text charts; the included combined SVG was generated from actual report data with the standard library. No external Python packages are needed to reproduce the delivered outputs.
