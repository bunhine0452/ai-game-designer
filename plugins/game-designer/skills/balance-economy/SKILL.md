---
name: balance-economy
description: Designs and checks game numbers with runnable models. Covers progression curves and XP/level tables, stat and damage formulas, TTK and DPS budgets, cost curves for cards, units and items, transitive and intransitive (rock-paper-scissors) balance, faucets and sinks, currencies and inflation, drop rates, loot tables, gacha, pity systems and loot-box disclosure rules. Use when the user asks to balance, tune or model numbers, build an XP table, simulate an economy, check drop or gacha odds, or find overpowered or underpowered content. Includes scripts for progression tables, Monte Carlo economy and gacha simulation with exact pity math, and cost-curve outlier detection. Also triggers on 밸런스, 경험치 테이블, 성장 곡선, 재화 설계, 인플레이션, 확률형 아이템, 천장, 드롭률, 데미지 공식; バランス調整, 経験値テーブル, 経済設計, ガチャ, 天井, ドロップ率; 数值平衡, 经验值表, 经济系统, 抽卡, 保底, 掉落率; balance, economía del juego, tasa de botín.
argument-hint: "[config or CSV path, or a balance question]"
license: MIT
compatibility: Any agent that reads SKILL.md folders (Claude Code, Claude apps, Codex, Antigravity, Cursor, Copilot). Scripts need Python 3; matplotlib optional.
metadata:
  author: bunhine0452
  version: "1.9.0"
  repository: https://github.com/bunhine0452/ai-game-designer
---

# Balance and economy

Treat numbers as design: every curve, price and drop rate is a decision about how the game
*feels over time*. Build a transparent model, simulate the variance, and validate with
playtests. Don't guess, and never tune by vibes alone.

**Language (required):**
- Answer in the language of the user's latest message.
- In a non-English answer, write **every** technical term the first time it appears (headings
  and table headers included) as the localized term plus the English term in parentheses, e.g.
  `천장 (Pity)`, `실질 확률 (Consolidated Probability)`, `재화 소모처 (Sink)`, `天井 (Pity)`, `保底 (Pity)`. After that, use the localized term alone.
- Standard terms are in `references/glossary.md` if bundled, or
  `../game-design/references/glossary.md`.
- Keep code, file names and CLI flags in English. Script output is English; translate it when
  summarizing.

## Workflow

1. **Start from the intended feeling and time.** "Level 10 in the first 2 hours", "a rare
   drop about once per session", "the boss dies in 90 s for a geared party". Turn feelings
   into targets before you touch formulas.
2. **Write the model.** List variables, formulas and assumptions in a table. Keep it simple
   enough for the user to rebuild in a spreadsheet.
3. **Run the matching script** (below) or compute by hand when code execution isn't
   available.
4. **Read the result as an experience,** not a number: time per level, sessions to the
   next upgrade, pulls to the item, shots to kill.
5. **Name the problems and propose specific changes** (parameter → new value → expected
   effect). Re-run to show before and after.
6. **Run the ethics check** whenever randomness and real money meet (see
   `references/randomness-and-loot.md`). It's mandatory, not optional.
7. **Give a validation plan:** which telemetry to watch after release (time-to-level, currency
   balances by percentile, pulls per hit).

## Scripts (Python 3 stdlib; matplotlib optional, with CSV/Markdown fallback)

### Progression tables: `scripts/progression_curve.py`
```bash
# One curve, with play time per level
python3 scripts/progression_curve.py --curve poly --levels 50 --first 300 --exponent 2.2 \
    --offset 5 --xp-per-hour 3000 --income-growth 1.05 --name rpg_xp --out ./out
# Solve the shape for a target total (first level stays fixed)
python3 scripts/progression_curve.py --curve exp --levels 60 --first 100 --total 2000000
# Compare linear / poly / exp / logistic at the same first level and total
python3 scripts/progression_curve.py --curve all --levels 50 --first 300 --xp-per-hour 3000
```
Outputs CSV tables, a Markdown report (when half the XP is earned, hours to the cap,
time-per-level walls) and charts.

### Economy and gacha: `scripts/economy_sim.py`
```bash
python3 scripts/economy_sim.py examples/f2p-economy.json --out ./out
```
The JSON config defines currencies, player archetypes (share, play probability, income
multiplier, purchases), faucets (mean, sd, growth, probability), sinks (`fixed`, `percent` of
income, or `buy` with growing cost) and an optional gacha (cost, rates, soft and hard pity, a
`featured` rate-up with an optional guarantee after a lost 50/50, and a `spark` exchange).
The report flags INFLATION, NO_SINK, STARVATION, SLOW_SINK, INEQUALITY (Gini), NO_CEILING,
RARE_FOR_MOST and DISCLOSURE. It shows the exact pity distribution (mean, p50/p90/p99 pulls,
consolidated rate) next to the simulation, and the real-money cost per rare item. The format
is in the script's docstring; start from `examples/f2p-economy.json`.

### Cost curves: `scripts/cost_curve.py`
```bash
python3 scripts/cost_curve.py examples/card-set.csv --robust --out ./out
```
CSV columns are `name,cost,<numeric attributes...>` (booleans as 0/1). It fits
cost ≈ intercept + Σ weight × attribute, reports the cost value of each attribute, and lists
**undercosted** (too strong) and **overcosted** (too weak) items. Use `--robust` so the
outliers don't bend the curve they're judged against.

### Engine hand-off: `scripts/export_engine.py`
```bash
python3 scripts/export_engine.py examples/card-set.csv --name Card --engine all --out ./export
```
Turns a final table (CSV, or JSON with `--key` for one list) into engine-ready data and code:
Godot (`Resource` class, JSON and a typed loader), Unity (a `[Serializable]` row and a
`ScriptableObject` table with a JSON loader), Unreal (a `USTRUCT : FTableRowBase` header and a
DataTable CSV), or plain typed JSON. Every file names its source table. See
`references/engine-handoff.md`, which covers engine MCP servers too.

## Choosing the model

| Question | Reference | Tool |
|---|---|---|
| How fast should players level? Which curve family? | `references/progression-curves.md` | `progression_curve.py` |
| Will currency inflate? Can players afford the core sink? | `references/economy-design.md` | `economy_sim.py` |
| How many hits to kill? DPS budget per role? Armor formula? | `references/combat-math.md` | by hand or spreadsheet |
| Is this card or unit fairly costed? Is there a dominant option? | `references/cost-curves-and-balance.md` | `cost_curve.py` |
| Drop rates, pity, input vs. output randomness, legal limits | `references/randomness-and-loot.md` | `economy_sim.py` (gacha) |
| How to run a balancing process (spreadsheets, sims, metrics) | `references/balancing-practice.md` | all |
| Move final numbers into Godot, Unity or Unreal | `references/engine-handoff.md` | `export_engine.py` |

## Output format

1. Targets (feelings turned into numbers).
2. Model table (variables, formulas, assumptions).
3. Results: chart or table plus a read-out in player terms (minutes, sessions, pulls, shots).
4. Problems ranked, each with a specific parameter change and its predicted effect.
5. Ethics and compliance notes (when randomness and money are involved).
6. Validation plan (telemetry plus playtest questions).

## Principles

- **Players feel time and decisions, not numbers.** Always convert to time-per-thing and
  choices-per-thing.
- **Faucets and sinks must be designed together.** Every faucet needs a sink that scales with
  it.
- **Prefer input randomness for strategy and output randomness for drama,** and cap bad luck.
- **No dominant options.** A strictly best choice deletes every other choice. Check viable
  options with cost curves and win and pick rates.
- **Disclose odds and protect minors.** Never design spending pressure on top of
  uncertainty. See the dark-pattern checks in `design-review`.
- **Models are hypotheses.** State the assumptions (archetype shares, session counts) and
  tell the user to replace them with telemetry.

## Examples

- `examples/rpg-xp-table.md`: a 50-level RPG table (~44 h to the cap) and a comparison of
  curve families.
- `examples/economy-walkthrough.md`: an F2P economy draft that inflates, then the fix
  (`f2p-economy.json` → `f2p-economy-revised.json`), plus the pity analysis.
- `examples/card-cost-curve.md`: a 20-card starter set with three planted outliers, found by
  the robust fit.
