<p align="center">
  <img src="docs/images/banner.png" alt="claude-game-designer: research-backed game design skills for every genre" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="Skills: 6" src="https://img.shields.io/badge/skills-6-fcbf49">
  <img alt="Genre playbooks: 26" src="https://img.shields.io/badge/genre%20playbooks-26-2a78d6">
  <img alt="Languages" src="https://img.shields.io/badge/answers%20in-EN%20%C2%B7%20KO%20%C2%B7%20JA%20%C2%B7%20ZH%20%C2%B7%20ES-1baf7a">
  <img alt="Works in Claude Code and the Claude app" src="https://img.shields.io/badge/works%20in-Claude%20Code%20%7C%20Claude%20app-14213d">
</p>

<p align="center"><b>English</b> · <a href="README.ko.md">한국어</a></p>

# claude-game-designer

**Turn Claude into a senior game designer who can show its work.** Six skills cover every genre,
from first concept to soft launch: pacing you can plot, numbers you can simulate, documents your
team will actually read, and reviews that catch dark patterns before players or regulators do.

- **Research-backed.** Every reference file cites its sources: GDC talks, designer postmortems,
  books and peer-reviewed games research. A 120+ entry bibliography with trust levels is in
  [`research/`](research/).
- **Runs real analysis.** It ships with a fun-curve plotter with pacing diagnostics, an XP curve
  solver, a Monte Carlo economy and gacha simulator with exact pity math, and a cost-curve
  outlier finder. They need only Python 3; matplotlib is optional.
- **Covers every genre.** 26 playbooks, from platformers to MMOs and from idle games to serious
  games, plus a method for designing hybrids.
- **Answers in your language.** It detects the language you write in, answers in it, and
  shows each technical term with the English term on first use, e.g. `관심 곡선 (Interest Curve)`.
  A 5-language glossary ships with it.
- **Works everywhere.** Skills only: no MCP servers, API keys or hooks. Install it in Claude Code
  or upload it to the Claude app.

> Unofficial community project. Not affiliated with or endorsed by Anthropic.

---

## What's inside

| Skill | What it does | Ships with |
|---|---|---|
| **`game-design`** | Entry point and router. Runs a quick intake (genre, platform, session, audience, stage) and produces a design brief: MDA aesthetics, pillars with test questions, core loops at three time scales, and risks with their cheapest tests. Holds the multilingual rules. | Frameworks, player-motivation models, 5-language glossary |
| **`fun-curve`** | Designs and critiques interest curves, flow and pacing for an encounter, level, run or whole game. Flags missing hooks, flat zones, peaks without relief, early climaxes and peaks that don't escalate. | `fun_curve.py`, pacing models, game-feel and playtest guides |
| **`genre-design`** | Genre playbooks: core loop, signature mechanics, pacing shape, progression, balancing levers, failure modes, reference games and *why* they work, and the talks behind them. | 26 playbooks plus a hybrid-genre method |
| **`balance-economy`** | XP tables, combat math (TTK, DPS, armor), cost curves, faucets and sinks, inflation, drop rates, pity, and the 2026 loot-box legal landscape. | `progression_curve.py`, `economy_sim.py`, `cost_curve.py` |
| **`gdd-art-direction`** | One-page designs, living GDDs, feature specs, asset lists with scope estimates, art and audio style guides, readability and silhouette rules, accessibility checklists. | 5 templates, accessibility (GAG/XAG/APX) guide |
| **`design-review`** | Structured critique of concepts, specs, builds or playtest notes, with prioritized issues, evidence and specific fixes, plus a **mandatory ethics pass** for dark patterns. | 12 review lenses, P0–P3 rubric, dark-pattern taxonomy |

## See it work

**Diagnose pacing, fix it, prove it.** A flawed horror chapter (left) becomes a healthy one
(right). The script found the missing hook, an 11-minute chase plateau, and a climax at 58%.
([walkthrough](skills/fun-curve/examples/horror-fix-walkthrough.md))

<p align="center">
  <img src="docs/images/fun-curve-horror-flawed.png" width="49%" alt="Flawed horror chapter interest curve">
  <img src="docs/images/fun-curve-horror-revised.png" width="49%" alt="Revised horror chapter interest curve">
</p>

**Model the math players feel.** The exact pity distribution of a 0.6% gacha with soft pity
from pull 74 and hard pity at 90: a mean of 62.3 pulls and a consolidated rate of 1.61%. Four
XP curve families solved to the same first level and the same total XP, compared on what players
actually feel, which is time per level.
([economy walkthrough](skills/balance-economy/examples/economy-walkthrough.md) ·
[XP table](skills/balance-economy/examples/rpg-xp-table.md))

<p align="center">
  <img src="docs/images/gacha-pity.png" width="49%" alt="Exact pity distribution">
  <img src="docs/images/curve-families.png" width="49%" alt="XP curve families compared">
</p>

**Find the broken cards.** A least-squares cost curve recovers what each attribute is worth
and flags undercosted and overcosted cards.
([walkthrough](skills/balance-economy/examples/card-cost-curve.md))

<p align="center"><img src="docs/images/cost-curve.png" width="60%" alt="Card cost curve with outliers"></p>

---

## Install

### Claude Code

```text
/plugin marketplace add bunhine0452/claude-game-designer
/plugin install game-designer@claude-game-designer
```

Skills trigger automatically from what you ask. You can also call one directly, e.g.
`/game-designer:fun-curve`.

### Claude app (claude.ai / desktop)

1. Download the files from the [latest release](https://github.com/bunhine0452/claude-game-designer/releases/latest):
   - `game-designer.plugin` (the whole plugin), for apps that support uploading plugins, or
   - `skills/*.zip` (one zip per skill), for **Settings → Capabilities → Skills → Upload skill**.
2. Turn on **code execution** so the scripts can run (charts appear when matplotlib is
   available, otherwise text and CSV).
3. Upload `game-design.zip` first: it's the router and holds the glossary. Add the others as
   you need them. Each zip is self-contained.

Menu names can differ between app versions. Look for "Skills" or "Plugins" in Settings.

### Other agents that read `SKILL.md` folders

Copy `skills/<name>/` into your agent's skills directory (e.g. `~/.claude/skills/`). The
scripts are plain Python 3.

---

## Usage examples

Ask in any language. These are just starting points.

| Skill | English | 한국어 |
|---|---|---|
| `game-design` | "I want a short-run roguelite where light is both health and currency. Help me write a design brief." | "몬스터랑 같이 농사짓는 힐링 게임 아이디어가 있어. 디자인 기둥이랑 코어 루프 잡아줘." |
| `fun-curve` | "My 15-minute dungeon feels boring in the middle. Here are the beats… what's wrong?" | "20분 런의 관심 곡선을 그려서 지루한 구간 찾아줘." |
| `genre-design` | "What do players expect from a metroidvania, and how could mine stand out?" | "로그라이크 덱빌딩 장르 관습이랑 흔한 실패 요인 알려줘." |
| `balance-economy` | "Build a 50-level XP table where the cap takes about 40 hours." · "Simulate this economy JSON for 60 sessions." | "가챠 0.6%에 90회 천장이면 평균 몇 번 뽑아야 해? 확률 공개 주의점도." |
| `gdd-art-direction` | "Write a one-page design for a cozy fishing game on a floating island." | "2인 팀용 아트 스타일 가이드 만들어줘. 실루엣·가독성 기준 포함." |
| `design-review` | "Review my monetization: streaks reset daily, energy costs gems, 0.5% rares with no pity." | "플레이테스트 노트 정리해서 문제점 우선순위 매겨줘." |

It also understands Japanese, Chinese and Spanish (e.g. 「ホラーの緩急を見て」, 「塔防加放置怎么结合？」,
"lista de accesibilidad para mi juego de plataformas").

## Multilingual behavior

- Answers in the language of your latest message, even when files or quotes are in another
  language.
- On first use in a non-English answer, each technical term is written as
  **localized (English)**, e.g. `관심 곡선 (Interest Curve)`, `天井 (Pity)`, `心流 (Flow)`,
  `bucle principal (Core Loop)`. After that, only the localized term is used.
- Terms come from a [glossary](skills/game-design/references/glossary.md) of 130+ terms in
  EN, KO, JA, ZH-Hans and ES.
- Code, file names, CLI flags and script outputs stay in English; Claude summarizes them in
  your language.

## Scripts at a glance

| Script | Input | Output |
|---|---|---|
| `skills/fun-curve/scripts/fun_curve.py` | beats CSV/JSON (`time,intensity,type,label`) | chart, report (MD/JSON), resampled CSV, ASCII curve |
| `skills/balance-economy/scripts/progression_curve.py` | CLI flags (curve family, levels, first, total, income) | XP tables (CSV), report, chart |
| `skills/balance-economy/scripts/economy_sim.py` | economy JSON (currencies, archetypes, faucets, sinks, gacha) | per-session and per-player CSVs, exact pity CSV, report, charts |
| `skills/balance-economy/scripts/cost_curve.py` | items CSV (`name,cost,attributes…`) | fitted weights, fair costs, outliers, chart |

All scripts use only the Python 3 standard library. When matplotlib isn't installed they
write text and CSV outputs instead of charts.

## Research

The research phase came first: [`research/RESEARCH_NOTES.md`](research/RESEARCH_NOTES.md)
(findings by area) and [`research/SOURCES.md`](research/SOURCES.md) (full bibliography with
trust levels). Highlights: Schell's interest curves, Csikszentmihalyi and Chen on flow, the Left
4 Dead AI Director, MDA, Lazzaro's four keys, Quantic Foundry, SDT/PENS, Koster, Swink, *Juice
it or lose it*, Valve's playtesting, RITE, PXI vs. GEQ, Schreiber's *Game Balance*, Sirlin,
Machinations, Pecorella's idle math, Zendle & Cairns on loot boxes, Librande's one-page designs,
TF2's readability, Riot's clarity guidelines, the Game Accessibility Guidelines, the Xbox
Accessibility Guidelines and APX. All content is paraphrased and cited; nothing is copied
verbatim.

Weakly sourced areas are flagged openly (racing, battle royale and party games have thin primary
sources). The loot-box law map is dated **October 2026** and is **not legal advice**.

## How it compares

Popular game-dev agent projects focus on *production* (studio role-play agents) or *engines*
(Godot, Unity and Phaser skills). This plugin focuses on **design knowledge and analysis**:
cited playbooks, runnable models and an ethics layer. It works in both Claude Code and the Claude
app, and it pairs well with engine or production plugins. See the competitive scan in
[`research/RESEARCH_NOTES.md`](research/RESEARCH_NOTES.md#e-competitive-scan).

## Quality checks

- `claude plugin validate .` passes for both the plugin and the marketplace manifest.
- Every script runs against the bundled examples (with and without matplotlib).
- `evals/`: 18 trigger-and-language cases (3 per skill: English, Korean, and Japanese, Chinese or
  Spanish), run with `claude plugin eval .`.

## Contributing

Native-speaker glossary fixes, new genre playbooks, better sources and new example walkthroughs
are very welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © bunhine0452
