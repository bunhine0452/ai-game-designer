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

## Five kinds of checks

| Kind | Example from the showcase prototypes |
|---|---|
| Fidelity | cost(1) = 200; chapter 1 production ≈ 41.4 min; five chapters ≈ 4.59 h; exact mean 47.1 pulls per pickup |
| Rules | tide 10 → Crest hits all, resets to 5; armor halves damage, pierce ignores it; unwatered crops pause instead of dying |
| Bots | a greedy bot plays 30 seeded runs of the whole deckbuilder without errors; a BFS bot clears the horror chapter with the threat off |
| Balance probes | report, don't assert: deckbuilder bot wins 8/30; TD bot wins with 3/15 lives at the normal starting money |
| Anti-fun screen | the 3D glider's autopilot finishes every delivery inside its target time; the pixel puzzle's solver shows every seed is needed and the last room has two solutions |

Add **Monte Carlo against exact math** wherever randomness meets money (gacha, drops). In
Hoshiyobi Island, 40,000 simulated pulls matched the exact mean within 2%.

## The anti-fun screen

Bots can't tell you a game is fun, but they find what reliably kills fun, before any person
plays. Every prototype's `?test=1` should cover the screens that apply:

| Screen | Assert | Why it matters |
|---|---|---|
| **Beatable** | a simple bot finishes every level, mission or run | an unwinnable stretch ends the session |
| **Not trivial** | a random or do-nothing policy does *not* win, or takes far longer | if anything works, no decision matters |
| **No dominant option** | no single "always pick X" policy wins (nearly) every run while the others lose; report the pick rates of an optimizing bot | one right answer removes choice |
| **Outcome in doubt** | in matched bot-vs-bot or bot-vs-content runs, under half the outcomes are one-sided (final margin ±0.6 or more) | close finishes are more enjoyable than blowouts |
| **Decisions keep coming** | the longest stretch with no meaningful choice stays under a limit you set (e.g. 20 s, or 10 turns) | dead time is where players leave |
| **Questions keep coming** | in content order, something new (rule, enemy, place, reveal) arrives at least every N minutes | nothing left to find out means nothing to look forward to |

```js
// Not trivial + no dominant option: compare simple policies on the same seeds.
const policies = { greedy: botGreedy, random: botRandom, alwaysFirst: (s) => 0, alwaysLast: (s) => s.options.length - 1 };
const wins = Object.fromEntries(Object.entries(policies).map(([k, p]) => [k, runSeeds(p, 30).wins]));
ok("not trivial: random play rarely wins", wins.random <= 5, JSON.stringify(wins));
ok("no dominant option: no fixed choice wins 27/30", Math.max(wins.alwaysFirst, wins.alwaysLast) < 27);
// Decisions keep coming: instrument the rules to log every point with 2+ viable options.
ok("decisions keep coming", maxGap(S.decisionTimes) <= 20, `longest gap ${maxGap(S.decisionTimes).toFixed(1)} s`);
```

Treat a failed screen as a design finding, not a test to loosen. The template
(`assets/template.html`) shows two of them on its tiny upgrade game.

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

- **Headless screenshots freeze compositor animations.** Entrance animations
  (opacity and transform keyframes) can be captured on frame 0 and look like missing content.
  Add a `shot` class that disables them in screenshot mode, and confirm in a real browser.
- **Never kill a process you didn't start.** Before starting a local server, check that the
  port is free (`lsof -iTCP:<port> -sTCP:LISTEN`) and pick another one if it isn't.

## Screenshots

`?shot=1` should build the most informative state: mid-session, several systems visible, a
caption or badge on screen, no modal covering the play area (or offer `?shot=report` for the
modal). Seed it so screenshots are reproducible. Open every screenshot before you report.

## Sources
- [A34] outcome uncertainty · [A55] self-play metrics (Ludi) · [A57] learnability as a necessary condition · [A58] agent playtesters: difficulty yes, experience unproven.

- [A20] Ambinder, playtests as experiments; [C2] Schreiber & Romero, simulation in balancing;
  [B2] Giovannetti, metrics-driven balance. Full bibliography: `research/SOURCES.md`.
