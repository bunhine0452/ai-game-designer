# From design documents to a playable scope

## 1. Find the test the design already asks for

Good design documents name their riskiest assumption and the cheapest test for it. Build that
test, not the whole game.

| Document | Look for | Becomes |
|---|---|---|
| Design brief / one-pager | "Biggest risks" plus "cheapest test" | The prototype's scope and pass criterion |
| Pillars | Test questions | A visible mechanic or UI element per pillar |
| Core loops | verb → feedback → reward → reinvestment | The main interaction and its feedback |
| Beat list / interest curve | Ordered beats with intensity | Level or session order; checkpoint placement |
| Card, unit or tower table | Rows with costs and stats | Data arrays copied verbatim |
| Economy config | Faucets, sinks, prices, pity | Constants and formulas, plus fidelity tests |
| Progression table | XP or cost per level | A formula, tested against two or three table rows |
| Accessibility checklist | Captions, flashing, controls | Settings panel items that actually work |

If nothing names a risk, ask: *what would make this design not fun?* Prototype that question.

## 2. Cut to one session

- **One core loop**, with one session's content (one run, one day, one chapter, 10 waves).
- **A real end state**: win, loss, summary, or "the demo ends here". Testers need closure.
- **Compress time, not structure.** A 15-minute game day can run in 3–4 minutes if the phases
  stay in order (hook → midday peak → evening climax). Offer a clearly labeled speed control
  when the design's real pacing is long (idle games), so testers can see both.
- **Fewer kinds, full depth.** Six towers that each do something distinct beat twelve that
  blur together. Prefer the subset the design marks as core.

## 3. Copy numbers with provenance

```js
// Cards: showcase/02 cards/tidecaller-starter-v3.csv (FINAL v3)
const CSV = `Splash,1,6,0,0,0,1,0,0,Surge,Basic
...`;
```

- Paste tables as CSV or JSON strings and parse them. Keep the original column names.
- Implement formulas exactly as written (`cost(L) = 200 * 1.18^(L-1)`), including the
  rounding rules the document states.
- Write one fidelity test per table or formula that checks a number the document quotes.
- Missing value? Pick one, comment `// placeholder: not in the design`, and list it in the
  report.

## 4. Genre starter patterns (from the six showcase prototypes)

| Genre | State | Loop to build first | Bot policy |
|---|---|---|---|
| Deckbuilder | deck, draw, hand, discard, exhaust, energy, enemies with intents | play cards → end turn → enemy intents resolve | play the first affordable card until none are left |
| Tower defense | grid, path, towers, pests, waves queue, currency, lives | place → start wave → simulate → reward | buy from a fixed spot list whenever affordable |
| Idle / incremental | level, currency, rate, chapter, multiplier | earn → buy when affordable → prestige | event-based auto-buy (exactly when affordable) |
| Farming / life sim | tiles, crops, helpers, clock, phase events | act on tiles → overnight resolution → payout | act on every tile each morning, sleep each night |
| Stealth / horror | map, rooms, doors and locks, threat AI, noise, checkpoints | move → interact → unlock next room | BFS path to each objective in order, threat disabled |
| Gacha / economy | currency, pity counters, odds, history | spend → roll → update counters | pull until the target item, many seeds, compared with exact odds |

## Sources

- [D1] Librande, one-page designs; [D3] Fullerton, playcentric prototyping; [B21] Dallas, many
  small prototypes (Edith Finch). Full bibliography: `research/SOURCES.md`.
- Live examples: the six prototypes in `games/` of the repository.
