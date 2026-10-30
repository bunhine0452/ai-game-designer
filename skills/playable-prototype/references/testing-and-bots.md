# Self-tests and bots

## The contract

```js
function selftest() {
  const out = [], ok = (name, cond, info = "") => out.push({ name, pass: !!cond, info });
  // ...checks...
  const pass = out.every((o) => o.pass);
  $("selftest").textContent = JSON.stringify({ game: "my-game", pass, results: out }, null, 1);
  $("selftest").hidden = false; document.title = `SELFTEST ${pass ? "PASS" : "FAIL"}`;
  S = fresh();                       // leave a clean state for the player
}
if (new URLSearchParams(location.search).has("test")) selftest();
```

`scripts/check.py` loads `?test=1` in headless Chrome, parses the JSON, and fails if anything
fails.

## Four kinds of checks

| Kind | Example from the showcase prototypes |
|---|---|
| Fidelity | cost(1) = 200; chapter 1 production ≈ 41.4 min; five chapters ≈ 4.59 h; exact mean 47.1 pulls per pickup |
| Rules | tide 10 → Crest hits all, resets to 5; armor halves damage, pierce ignores it; unwatered crops pause instead of dying |
| Bots | a greedy bot plays 30 seeded runs of the whole deckbuilder without errors; a BFS bot clears the horror chapter with the threat off |
| Balance probes | report, don't assert: deckbuilder bot wins 8/30; TD bot wins with 3/15 lives at the normal starting money |

Add **Monte Carlo against exact math** wherever randomness meets money (gacha, drops). In
Hoshiyobi Island, 40,000 simulated pulls matched the exact mean within 2%.

## Bot design

- Keep the policy dumb and readable (first affordable card, fixed placement list, BFS to the
  next objective). A dumb bot winning easily means the game has no challenge. A dumb bot never
  finishing means the game is broken.
- Run many seeds (`rng = seeded(100 + i)`), and catch and record exceptions with stack excerpts.
- Bound every loop (`guard++ < N`) so a stuck state fails the test instead of hanging.
- Bots call the same rule functions as the UI. If a bot needs a back door, the logic is too
  coupled to the screen.

## Pitfalls we actually hit

- **A comment swallowed a test.** Inserting `// note` mid-line commented out the rest of the
  line, so one test silently disappeared and the next failed for the wrong reason. Watch the
  check count, not just pass or fail.
- **A test that measured a dead enemy.** An enemy damaged by an earlier check died mid-test,
  capping the damage. Reset the subject's HP before each rule check.
- **Pattern-matching JSON across lines.** Read the result from the title or parse the JSON.
  Don't grep pretty-printed output.
- **Testing only `file://`.** Re-run against the deployed URL. In our case all six passed on
  GitHub Pages, but paths and fonts can differ there.

## Screenshots

`?shot=1` should build the most informative state: mid-session, several systems visible, a
caption or badge on screen, no modal covering the play area (or offer `?shot=report` for the
modal). Seed it so screenshots are reproducible. Open every screenshot before you report.

## Sources

- [A20] Ambinder, playtests as experiments; [C2] Schreiber & Romero, simulation in balancing;
  [B2] Giovannetti, metrics-driven balance. Full bibliography: `research/SOURCES.md`.
