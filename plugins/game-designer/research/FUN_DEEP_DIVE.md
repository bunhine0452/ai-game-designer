# Fun, the hard problem: a deep dive

*October 2026. Companion to `RESEARCH_NOTES.md` §A and to `fun-curve/references/what-makes-it-fun.md`.
Source IDs refer to `SOURCES.md`. Where a source was checked only at the abstract level or through
secondary coverage, `SOURCES.md` says so.*

Designers can plan structure, numbers and content. Whether the result is *fun* is the part nobody
can guarantee in advance. This note asks four questions: why is fun so hard, what is the best
current account of it, can it be computed or predicted, and how do you measure it without fooling
yourself? It ends with a working loop for teams and the open problems.

## Summary

1. **Fun is not a property of the game.** It emerges between a player and a system, and designers
   shape it only indirectly [A5], [A57]. Studies don't even agree on what "enjoyment" is: a review of
   87 quantitative studies found overlapping, inconsistent definitions and measures [A48].
2. **Few design rules transfer.** A meta-analysis of design choices found that, across studies, only
   the presence of music had a significant effect on enjoyment; even difficulty and control mode did
   not [A49]. Effects depend on the game and the audience, so you have to test in yours.
3. **The best unifying account is uncertainty resolution.** Play seeks a sweet spot of uncertainty,
   and pleasure comes when uncertainty shrinks *faster than expected* [A50], [A51], [A53]. This explains
   balanced challenge, curiosity, close contests, the inverted U of recreational fear [A52], and why a
   mastered game turns boring [A10].
4. **It doesn't explain everything.** Sensation (music, feel), effectance (seeing your influence on the
   world) [A61], other people [A42], and meaning, including enjoyed sadness [A60], add separate
   layers.
5. **Engagement can grow without fun.** "Wanting" and "liking" are different systems [A59]. Telemetry
   mostly measures wanting; fun is liking [A39].
6. **Computation screens out anti-fun but can't certify fun.** Self-play metrics predicted part of human
   preference for abstract games [A55]; bots measure difficulty reasonably [A58]; nothing yet predicts
   fun before people play.
7. **Measure behavior and comparisons, not just ratings.** Free-choice continuation [A63], [A68] and
   rank-based questions [A54] beat single ratings. Memories are biased by peaks and endings [A62],
   [A67].
8. **The market confirms that fun is unpredictable.** About 1% of paid Steam games take roughly 85% of
   revenue [A64]; Supercell reported 30+ killed games for 5 hits [A65]. The studios that do well
   build the toy first, test early and kill often [A65], [A66], [A45].

## 1. Why fun is hard

### 1.1 It emerges; designers only set the conditions

MDA [A5] puts it simply: designers author mechanics, players experience aesthetics, and the
dynamics in between come from play. Automatic game design research calls it a *second-order*
design problem for the same reason [A57]. A rule can be fun in one game and dull in another,
because fun depends on what the rule interacts with: other rules, the player's skill, the
moment, the people present.

### 1.2 Nobody agrees what "fun" is

- A systematic review of 87 quantitative studies [A48] found enjoyment defined and measured in
  overlapping, inconsistent ways, often confused with flow, presence and immersion. Its proposal:
  treat enjoyment as the overall *valence* of the player experience. Enjoyment can happen without
  challenge or concentration, so it is not the same as flow.
- Kinds of fun really differ: hard fun, easy fun, people fun and serious fun [A6]; eight aesthetics
  [A5]; twelve motivations that cluster and change with age [A8]. A design "for fun" with no
  audience and kind named can't be checked.

### 1.3 Most design effects don't transfer

The meta-analysis of game design choices [A49] is sobering. Of the many factors studied (content,
difficulty, control mode, information presentation, multiplayer), only music had a significant
overall effect on enjoyment. The companion meta-analysis on immersion found only multiplayer
effects. That doesn't mean difficulty doesn't matter. It means the effect *depends on context*,
so "make it harder" or "add touch controls" is not reliably good advice without your game and
your players. Studies within one game (§2) show strong effects. Pooled across games, they wash out.

### 1.4 Fun moves while you watch

- **Learning consumes it.** Once a pattern is mastered, the same play turns routine [A10].
- **Sweet spots are personal and shift.** In a haunted attraction (110 visitors with heart-rate
  monitors), enjoyment followed an inverted U with fear: more fear helped up to a point, then hurt
  [A52]. Each visitor's peak was in a different place.
- **Players travel the difficulty range.** Free to choose among short games of varied difficulty,
  adults started easy, moved to harder ones, and kept returning to *moderately* hard games more than
  chance would predict [A68].

### 1.5 Measuring it changes what you see

- **Memory is biased.** Re-ordering otherwise identical casual games strongly changed how
  challenging players *remembered* them; effects on remembered enjoyment were mixed [A62]. In
  Hearthstone, retrospective reports matched peak-and-end self-reports but not facial expressions
  [A67].
- **Ratings are noisy.** People use scales differently, and the same person drifts. Rank-based
  questions ("which was more fun, A or B?") give more reliable labels and better models [A54].
- **Wanting is not liking.** Incentive salience ("wanting") can grow without pleasure ("liking")
  [A59]. Retention and session length measure the first. In telemetry from 38,935 players, *why*
  people played mattered and *how long* barely did [A39].

### 1.6 The market says nobody can call it in advance

About 1% of paid Steam games earn roughly 85% of the platform's revenue, and in 2025 about 300 of
some 20,000 releases passed $1 million [A64]. Supercell, among the most successful mobile studios,
reported killing 30+ games for 5 hits, some at an advanced stage [A65]. These numbers mix fun with
marketing, timing and luck, but they rule out the idea that experienced teams can predict fun from
a document.

## 2. What fun is: the best current account

### 2.1 Uncertainty resolved faster than expected

The strongest unifying theory comes from predictive processing:

- **Play seeks a sweet spot of uncertainty.** Brains try to reduce prediction error. Play is the odd
  case where we *add* uncertainty on purpose, because reducing it is rewarding [A51].
- **Pleasure is the rate, not the state.** Positive feeling comes when uncertainty is reduced *faster
  than expected* [A50]. Steady competence feels flat; sudden understanding feels great.
- **Earlier versions of the same idea.** Schmidhuber's "formal theory of fun" defines fun as
  *compression progress*: getting better at predicting or compressing your experience [A53].
  Learning-progress accounts of curiosity say the same [A35]. Koster's "fun is learning" is the
  designer's version [A10].

What it explains:

| Observation | Why, in this account |
|---|---|
| Balanced challenge beats easy and impossible [A32], [A33] | Easy: little uncertainty to resolve. Impossible: no progress in resolving it |
| Close contests beat blowouts [A34] | The outcome stays uncertain, so its resolution at the end is large and fast |
| Curiosity predicts enjoyment and play time [A35] | Open questions are uncertainty the player expects to resolve |
| Fear has a sweet spot [A52] | Arousal that can be resolved ("it was a scare, I'm fine") is pleasant; arousal that can't is not |
| Mastered games get boring [A10] | Nothing left to predict better |
| Idle games and Soulslikes both work [A50] | Idle: small, frequent, reliable resolutions. Soulslike: rare, huge ones after long buildup |

**Design translation:** a game needs a steady *supply of resolvable uncertainty*. New questions
(which enemy, which build, what's behind the door, who will win) must arrive as fast as old ones
are answered. A stretch where nothing is in doubt is a curiosity drought. A stretch where nothing
can be resolved is overload.

### 2.2 What the account leaves out

Uncertainty resolution is the engine, but players report other kinds of reward:

- **Sensation and effectance.** Seeing your influence on the world drives enjoyment: an experiment
  (n = 500) that reduced the player's felt influence reduced enjoyment [A61]. The music finding in
  [A49] and the juice studies [A36] point the same way: the sensory layer matters in itself.
- **Other people.** Shared, co-located play raises enjoyment through social presence [A42].
- **Meaning.** Most of 121 players who described emotionally moving moments enjoyed and appreciated
  even sad ones [A60]; appreciation and reflection are a second kind of reward [A44].
- **Wanting systems.** Collections, streaks and variable rewards can create wanting without liking
  [A59]. They are not fun on their own, and the ethics pass treats them as costs.

A practical model:

```
fun ≈ a supply of resolvable uncertainty at the right rate
      × a sensory layer that makes each action and outcome felt
      × (optionally) people to share it with and something that matters
      for this audience
```

Each factor can zero out the product, which is why a game with brilliant systems and dead feel,
or great feel and nothing in doubt, still isn't fun.

## 3. Can fun be computed or predicted?

| Approach | What it achieved | Limits |
|---|---|---|
| **Self-play aesthetic metrics** (Ludi) [A55] | Measured 57 properties of evolved board games through self-play; 17 correlated with which games people preferred. *Yavalath*, an evolved game, was published commercially | Abstract strategy games only; criteria counts from secondary sources |
| **Game refinement theory** [A56] | A ratio of resolved uncertainty to game length clusters around 0.07–0.08 for long-lived games (chess, go, shogi, football) | Mostly one research group; a necessary-looking zone, not a sufficient one |
| **Learnability as fitness** [A57] | Evolved rules that a learning agent could improve at | Learnable is necessary for fun, not sufficient |
| **RL and LLM agents as playtesters** [A58] | Agents estimate difficulty usefully, even when they play worse than humans | Weaker on hard levels; claims about predicting *experience* have no published agreement figures yet |
| **Player modeling** [A54] | Models of experience trained on rank labels outperform rating-based ones | Needs real players to label first |

**Conclusion:** computation is good at finding **anti-fun**: unwinnable or trivial content,
dominant strategies, outcomes decided early, no decisions for long stretches, difficulty spikes.
It can't yet certify fun. Use it as a filter before human tests, never instead of them. (Every game
in this repository already does this: autopilots and solvers prove each level is beatable and the
targets are fair before anyone plays.)

## 4. Measuring fun without fooling yourself

1. **Watch what players do when they don't have to.** Voluntary continuation after the required play
   ("you can stop now") is the standard behavioral proxy for intrinsic motivation. In one study,
   children chose the intrinsically motivating version of a game 7× longer in free time [A63].
2. **Compare instead of rate.** Ask "A or B?" between two builds or two moments. Ranks are more
   reliable than ratings [A54], and comparing versions is what design decisions need.
3. **Capture the moment and the memory.** Observer notes and in-game prompts catch the moment;
   questionnaires capture the memory, which peaks and endings bias [A62]. Design the ending knowing
   it will dominate the memory, but don't mistake the memory for the experience.
4. **Separate wanting from liking.** Pair retention with a "want to vs. have to" item, and test
   whether players return when the streaks and timers are switched off [A39], [A59].
5. **Use standard scales to compare across tests.** The miniPXI and BANGS [A47], [A38] support
   comparisons across builds and studies. Original items are fine for one test question.
6. **Expect inconsistency across games.** Effects that don't replicate across studies [A49] mean
   every conclusion is about *your* game and *your* players, and must be re-tested after changes.

## 5. How studios cope

- **Build the toy before the game.** Super Mario 64's team spent about half its effort on movement,
  animation and physics; courses and enemies came last [A66]. Breath of the Wild's systems were
  proven in a 2D mock-up first [A45].
- **Escalate tests and kill early.** Supercell's projects pass internal tests, then a small soft
  launch, and are cut at any stage. The ritual celebrates what was learned, not the failure [A65].
- **Test with outsiders, early and often.** Valve's playtesting practice [A20] and the RITE method
  [A19] turn play into evidence quickly.
- **Know the audience.** Motivation profiles differ by age far more than by gender, and competition
  appeal falls fastest [A8].

## 6. A working loop for the hard problem

```
1. Fun hypothesis    Which uncertainty will players want resolved, how fast, and what makes
                     each resolution felt? For whom? (one paragraph, falsifiable)
2. Smallest toy      The core verb and one source of uncertainty. No content, no meta.
3. Bot screen        Anti-fun checks: beatable, not trivial, no dominant strategy,
                     outcome margins not one-sided, decisions every N seconds.
4. People            5–8 outsiders. Free-choice continuation, A/B preference between two
                     variants, observer notes, then a short questionnaire.
5. Decide            Kill, pivot or grow, against thresholds written in step 1.
6. Grow              Add content and meta only on top of a toy that holds.
```

## 7. Open problems

- **No validated way to predict fun before something is playable.** Documents, models and AI
  playtesters can rule things out, not in.
- **Individual differences.** Sweet spots differ per person [A52] and motivations by audience [A8].
  Adaptive systems help with difficulty but have mixed effects on enjoyment [A40].
- **Long-term fun.** Most studies cover minutes to hours. How fun holds over months (and how it
  differs from habit) is barely studied.
- **Meaning is hard to measure** and easy to confuse with pleasure [A44].
- **AI playtesters.** Promising for difficulty; whether they can model *experience* is open [A58].

## Sources

New in this note (details and trust levels in `SOURCES.md`):
[A48] Mekler et al. 2014 · [A49] Caroux & Pujol 2023 · [A50] Deterding et al. 2022 · [A51] Andersen
et al. 2023 · [A52] Andersen et al. 2020 · [A53] Schmidhuber 2010 · [A54] Yannakakis & Martínez 2015
· [A55] Browne 2008; Browne & Maire 2010 · [A56] Iida et al., game refinement · [A57] Togelius &
Schmidhuber 2008 · [A58] LLM and agent playtesters 2025–26 · [A59] Berridge & Robinson 2016 · [A60]
Bopp et al. 2016 · [A61] Klimmt et al. 2007 · [A62] Gutwin et al. 2016 · [A63] Habgood & Ainsworth
2011 · [A64] Steam revenue concentration 2025–26 · [A65] Supercell · [A66] Super Mario 64 interviews ·
[A67] peak-end in Hearthstone 2020 · [A68] Baranes, Oudeyer & Gottlieb 2014.

Also cited: [A5] MDA · [A6] Lazzaro · [A8] Quantic Foundry · [A10] Koster · [A19] RITE · [A20] Valve ·
[A32]–[A47] from `what-makes-it-fun.md`.
