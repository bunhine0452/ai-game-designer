# Reproducing the analysis

Run from this folder with Python 3 (standard library sufficient):

```sh
python3 scripts/fun_curve.py beats_before.csv --out analysis --reference --format svg --title 'Low Tide — original draft'
python3 scripts/fun_curve.py beats_after.csv --out analysis --reference --format svg --title 'Low Tide — revised chapter'
python3 scripts/build_comparison.py
```

`fun_curve.py` is an unchanged local copy of `.agents/skills/fun-curve/scripts/fun_curve.py`. No matplotlib was installed during these runs, so the analyzer emitted Markdown, JSON, resampled CSV and ASCII charts but no individual image files. `build_comparison.py` creates the combined SVG directly from analyzer JSON using the standard library. It does not alter diagnostics. If matplotlib is available, the first two commands also emit individual SVGs with the generic reference overlay; those are optional outputs.

Identical defaults for both runs: hook ≥6 within first 10% (4 min); flat band ≤1 point lasting ≥12% (4.8 min); peaks ≥7 require relief ≥2.5 within 12% (4.8 min), except the global climax and peaks too near the endpoint for the window; high ≥8 lasting more than 15% (6 min) flags sustained pressure; climax earliest at 70% (28 min); maximum high share 35%; low ≤3 maximum share 40%; monotony at 4 consecutive same-type samples or a same-type span ≥25% (10 min). Other implementation defaults remain unchanged in the copied script. See `python3 scripts/fun_curve.py --help`.

The analyzer samples a linearly interpolated curve; percentages are estimates of predicted time, not counts of beat rows or player measurements. Both inputs begin at 0 min and end at 40 min. The combined SVG contains accessible title/description text and differentiates lines by dash style and color. Markdown reports include full text charts and tables.
