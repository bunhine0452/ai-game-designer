---
name: design-review
description: Structured, research-backed critique of a game concept, pitch, GDD, prototype description, build notes or playtest notes, in any genre. Produces prioritized issues with evidence, severity and specific fixes, plus a mandatory ethics pass for dark patterns, manipulative monetization, loot-box and odds-disclosure risks and protections for minors. Use when the user asks for feedback, a critique, a review, "what's wrong with my game", "is it fun" or "why isn't it fun" (a fun diagnosis across challenge, outcome uncertainty, curiosity, feedback and player needs), a sanity check before pitching or launch, playtest analysis, or a monetization or ethics review. Also triggers on 피드백, 기획 리뷰, 기획서 검토, 문제점, 재미없다, 왜 재미없지, 재미 진단, 플레이테스트 분석, 다크 패턴, 과금 구조 검토; フィードバック, 企画レビュー, 問題点, 面白くない, なぜ面白くない, プレイテスト分析, ダークパターン, 課金設計; 反馈, 策划评审, 问题, 不好玩, 为什么不好玩, 试玩分析, 暗黑模式, 付费设计; revisión de diseño, crítica, no es divertido, patrones oscuros.
argument-hint: "[document, build notes, or playtest notes to review]"
license: MIT
compatibility: Any agent that reads SKILL.md folders (Claude Code, Claude apps, Codex, Antigravity, Cursor, Copilot). Scripts need Python 3; matplotlib optional.
metadata:
  author: bunhine0452
  version: "1.10.0"
  repository: https://github.com/bunhine0452/ai-game-designer
---

# Design review

Review like a senior designer who wants the game to succeed: specific, evidence-based,
prioritized, and constructive. Every issue ends in a fix the team can try. Every review
includes an ethics pass.

**Language (required):**
- Answer in the language of the user's latest message.
- In a non-English answer, write **every** technical term the first time it appears (headings
  and table headers included) as the localized term plus the English term in parentheses, e.g.
  `다크 패턴 (Dark Pattern)`, `심각도 (Severity)`, `판정 (Verdict)`, `暗黑模式 (Dark Pattern)`. After that, use the localized term alone.
- Standard terms are in `references/glossary.md` if bundled, or
  `../game-design/references/glossary.md`.
- Keep code, file names and CLI flags in English. Script output is English; translate it when
  summarizing.

## Workflow

1. **Understand the intent before judging.** Pull out (or ask briefly for) the target
   aesthetics, pillars, audience, platform, session length and stage. Review against *their*
   goals, not your taste. If the goals are missing, state the goals you assumed.
2. **Classify the material:** concept/pitch, GDD/spec, prototype or build description,
   playtest notes, telemetry, or a monetization plan. Each needs a different depth (see below).
3. **Apply the lenses** in `references/review-lenses.md` that fit the material. At concept
   stage, focus on experience, loops, decisions, motivation, scope and ethics. With
   playtest data, focus on observed behavior vs. intent, onboarding, pacing and feel.
4. **Write the issues.** One issue per row: what (observable), evidence (a quote from the
   material or a playtest observation), why it matters (the principle and its source), fix
   (specific), cost (S/M/L), and how to verify.
5. **Prioritize** with `references/severity-rubric.md` (P0–P3, by impact × reach ×
   confidence). Put P0s first, and flag cheap high-impact fixes as quick wins.
6. **Run the ethics pass**, always. Fill the dark-pattern table in
   `references/ethics-dark-patterns.md` (present / at risk / absent) for every retention and
   monetization mechanic, and give a healthy alternative for each one found. Legal exposure
   (odds disclosure, minors) is P0.
7. **Hand off:** pacing problems → `fun-curve`, number problems → `balance-economy`, genre
   conventions → `genre-design`, document gaps → `gdd-art-direction`.

## Depth by material

| Material | Focus | Typical output |
|---|---|---|
| Concept / pitch | Fantasy clarity, aesthetics ↔ pillars ↔ loops, differentiation, scope, ethics | 5–8 issues, 3 strengths, the riskiest assumption plus the cheapest test |
| GDD / feature spec | Internal consistency, edge cases, pillar alignment, missing systems (save, accessibility, localization) | Issue table plus a missing-section list |
| Prototype / build notes | Core verb feel, readability, onboarding, pacing, balance hot spots | Issues ranked by player impact |
| Playtest notes | Observed vs. intended experience, frequency, severity | Clustered findings (n of N), fixes, next test plan (`references/playtest-analysis.md`); with an event log, run `scripts/playtest_report.py` first |
| Planning a playtest | The question, players, tasks, what to collect | A one-page plan and kit (`references/playtest-kit.md`) |
| "Is it fun?" / "Why isn't it fun?" | Each fun driver scored separately: challenge, outcome uncertainty, curiosity, feedback, autonomy, competence, relatedness, meaning | Driver table with evidence, the bottleneck driver, fixes as predictions (`references/fun-diagnosis.md`) |
| Monetization plan | Value perception, fairness, dark patterns, legal compliance | Ethics table plus compliance checklist plus healthy alternatives |

## Output format

```
## Verdict
One paragraph: what works, the single biggest problem, and the recommended next step.

## Strengths (keep these)
- 3 specific strengths, each tied to a pillar or aesthetic

## Issues
| ID | Sev | Lens | Issue | Evidence | Why it matters | Fix | Cost | Verify by |
|---|---|---|---|---|---|---|---|---|

## Ethics and dark-pattern check
| Pattern | Status | Where | Healthy alternative |
|---|---|---|---|
+ compliance notes (odds disclosure, minors, real-money pricing) when relevant

## Questions for the designer
- 3-5 questions whose answers would change the review

## Next test
The cheapest experiment that addresses the top issue, with a pass criterion
```

## Principles

- **Specific beats general.** "Room 3's turret kills players before they see it (4 of 6
  testers)" beats "combat is unfair".
- **Separate observation, interpretation and recommendation.** Players are reliable about
  what they feel and unreliable about how to fix it.
- **Cite the principle, not just your opinion,** e.g. "no relief after peaks (L4D AI
  Director model)", "dominant option (Sirlin)". Keep it to a short reference.
- **Fix the cause, not the symptom.** Trace aesthetic → dynamic → mechanic (MDA).
- **Respect the vision.** Suggest fixes inside the user's pillars. If a pillar itself is the
  problem, say so explicitly, as a separate point.
- **Never shame.** Plain and kind, always actionable.

## References

- `references/review-lenses.md`: 12 lens groups with original guiding questions, mapped to
  sources.
- `references/severity-rubric.md`: P0–P3 definitions and the prioritization formula.
- `references/ethics-dark-patterns.md`: dark-pattern taxonomy, healthy alternatives, minors
  and compliance checklist.
- `references/playtest-analysis.md`: turning raw notes and telemetry into findings.
- `references/playtest-kit.md`: test plan, observer sheet, 7-point questionnaire, event-log format,
  free-choice play and A/B comparisons.
- `references/fun-diagnosis.md`: scoring eight fun drivers (need satisfaction and frustration
  separately), finding the bottleneck, and measuring it in the next playtest.
- `scripts/playtest_report.py`: event log → funnel, difficulty spikes, drop-off, quit clusters and questionnaire means (`python3 scripts/playtest_report.py examples/playtest-log.csv --out ./out`).
- `examples/concept-review-example.md`: a full review of a fictional mobile concept with
  monetization issues.
