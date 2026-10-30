# Research Notes

Findings that back the skills in this plugin. Each claim has a source ID from [`SOURCES.md`](SOURCES.md).
All text here is a paraphrase. Nothing is copied verbatim from copyrighted works. Where a fact rests on
secondary or low-trust sources, the note says so.

---

## A. Fun, engagement and pacing

### A.1 Interest curves (Schell)
- Schell treats an experience as a line of *interest over time*. The typical good shape opens with a
  strong **hook**, dips, then climbs in a series of rising peaks and valleys toward a **climax** near the
  end, followed by a short resolution [A1].
- Interest curves nest. A whole game, a level, a session and a single encounter each have their own
  curve, and a good shape at one scale doesn't guarantee one at another [A1].
- The curve is a diagnostic tool. Plotting predicted interest beat by beat, then comparing it with
  observed playtest behaviour, shows where an experience sags [A1].
- **Implication for this plugin:** a beat list of (time, intensity, type) is a workable stand-in for an
  interest curve. Its standard failure modes can be detected automatically: missing hook, long flat
  stretches, peaks without relief, climax too early, peaks that don't escalate.

### A.2 Flow and the flow channel
- Csikszentmihalyi defines flow as deep absorption that happens when challenge and skill are both high
  and balanced, goals are clear, and feedback is immediate. If challenge outruns skill you get anxiety;
  if skill outruns challenge you get boredom [A2].
- Chen applies this to games as a *flow channel* (a band between anxiety and boredom). Players differ, so
  one fixed difficulty curve can't keep everyone in the channel. He argues for player-driven, embedded
  choices of challenge (active DDA), as in *flOw*, where the player picks the depth or intensity
  themselves [A3].
- **Implication:** recommend *player-chosen* difficulty affordances (optional challenges, risk-reward
  routes, assist modes) before hidden rubber-banding. Hidden adjustment, when used, should be invisible
  and should never punish skill.

### A.3 Pacing, tension and release, intensity graphs
- **Left 4 Dead's AI Director** models each survivor's "emotional intensity" from damage taken and
  nearby enemies. It runs a cycle of *build-up*, *sustained peak*, *peak fade* and *relax*. It pulls back
  spawns after peaks so players get relief, and it varies where enemies and items appear so runs can't be
  memorised [A4].
- **Alien: Isolation** pairs a director AI, which always knows where the player is, with an alien that
  must find the player using its own senses. A "menace" measure rises while the alien is close or
  perceived; past a threshold the alien retreats into the vents for a while. This produces ebb and flow
  without cheating [A27, A28]. (These mechanism details come from secondary analysis.)
- **Kishōtenketsu in Nintendo level design:** a mechanic is introduced, developed, given a twist and
  then concluded within one short stage. Each level is a self-contained mini-arc [A29] (secondary).
- **Sawtooth difficulty** (a common practice) means each segment ramps up and ends harder, then the
  next segment resets lower but above the previous trough. It gives relief while the overall line still
  rises. This fits Schell's curve [A1] and Chen's channel, which drifts upward as skill grows [A3].
- **Session-length design:** the natural session (one run, one match, one day-cycle, one level) should
  complete its own mini-arc. On mobile, retention benchmarks are low: median D1 is in the low 20s %, and
  top-quartile D1 is about 27% in 2024 data [A26]. That is why the first session's hook and early arc
  get so much attention.

### A.4 MDA and the eight kinds of fun
- MDA separates **Mechanics** (rules and data), **Dynamics** (run-time behaviour that emerges when
  players interact with the mechanics) and **Aesthetics** (the emotional responses evoked). Designers
  work from M toward A; players experience A first [A5].
- MDA's aesthetic taxonomy has eight entries: **Sensation, Fantasy, Narrative, Challenge, Fellowship,
  Discovery, Expression, Submission** [A5].
- Lazzaro's "Four Keys" come from observing players' emotions: **Hard Fun** (challenge and mastery,
  *fiero*), **Easy Fun** (curiosity and novelty), **People Fun** (social), and **Serious Fun** (meaning,
  changing yourself or the world). She reports that well-liked games tend to offer several keys [A6].
- **Implication:** the router asks the user to name 2–3 target aesthetics and derives pillars from them.
  Every critique ties issues back to the aesthetics the user declared.

### A.5 Player motivation models
- **Bartle (1996):** four MUD play styles (Achievers, Explorers, Socialisers, Killers) on two axes: acting
  vs. interacting, and world vs. players. It was written for MUDs. It is often misapplied as a
  personality test or a universal segmentation [A7].
- **Quantic Foundry:** 12 motivations from factor analysis of survey data from hundreds of thousands of
  gamers, grouped into six pairs. The pairs are Action (Destruction, Excitement), Social (Competition,
  Community), Mastery (Challenge, Strategy), Achievement (Completion, Power), Immersion (Fantasy, Story)
  and Creativity (Design, Discovery). These form three higher clusters [A8]. The item set is
  proprietary [A8].
- **SDT / PENS:** perceived **autonomy**, **competence** and **relatedness** independently predict
  enjoyment and continued play [A9]. PENS is free for academic use; commercial use needs permission [A9].
- **Implication:** use Quantic Foundry–style motivations to describe the audience and SDT needs to
  diagnose *why* something feels bad. Mention Bartle only with its MUD context.

### A.6 Core loops, compulsion loops, reward schedules, ethics
- Cook models play as nested **loops**: act, get feedback, update a mental model. Loops repeat at many
  time scales. **Arcs** are one-shot experiences such as story beats. Skill atoms chain into skill
  trees [A16, A17].
- Meier: a game is a series of **interesting decisions**. A decision stops being interesting when one
  option dominates or the outcome is unreadable [A18].
- Hopson: reward contingencies shape behaviour. Fixed-ratio schedules cause a **post-reward pause**.
  Variable-ratio schedules give high, steady response rates. Extinction (removing a reward) causes
  frustration. He later argued that the Skinner box is a research instrument, not a design template
  [A14].
- Zagal, Björk & Lewis define **dark game design patterns** as elements a designer uses deliberately to
  create experiences that go against players' interests and likely happen without their consent. Their
  categories are temporal (grinding, playing by appointment), monetary (pay to skip, pre-delivered
  content, monetized rivalries), social (social pyramid schemes, impersonation) and psychological
  (e.g. invested/endowed value) [A15].
- Legal enforcement against manipulative flows now exists. The FTC's Epic order required $245M in
  refunds for purchase flows that caused unwanted charges [C16]. The 2025 HoYoverse settlement concerned
  misleading loot-box odds and price obfuscation aimed at minors [C17].
- **Implication:** the design-review skill runs a mandatory ethics pass. Every retention or monetization
  mechanic is checked against these patterns and given a "healthy alternative".

### A.7 A Theory of Fun, game feel, juice
- Koster: fun is the feeling of learning, of mastering patterns. A game gets boring once its patterns are
  exhausted, so depth comes from systems that keep producing new patterns to learn [A10].
- Swink defines **game feel** as the overlap of real-time control, simulated space and polish. Polish is
  the impression of physicality that comes from animation, sound and effects in harmony with
  input-driven motion [A11]. A later survey notes the definition doesn't cover every game form [A31].
- "Juice it or lose it" showed live how tweening, squash-and-stretch, particles, screen shake and sound
  turn a flat prototype into a lively one [A12]. A counter-talk warned that excessive juice can hurt
  readability and immersion [A30].
- *Celeste* forgiveness techniques include coyote time, jump buffering, halved gravity at the jump apex
  and corner correction. They make precise platforming feel fair [A13].

### A.8 Measuring fun
- **Valve:** a design is a hypothesis and a playtest is an experiment. Valve combined observation,
  verbal reports and Q&A with stat collection, surveys and physiological measures, and kept testing after
  release [A20].
- **RITE** (Microsoft Games): fix a problem as soon as its cause and solution are clear, even after one
  participant, then confirm with the next participants [A19].
- **Games User Research** (OUP 2018) and **Game Analytics** (Springer 2013) cover research planning,
  surveys, telemetry design, funnels and spatial analysis [A21, A22].
- **Questionnaires:** the GEQ is widely used, but a 2018 systematic review found inconsistent use and
  did not confirm its proposed factor structure [A23, A24]. The PXI was validated across five studies
  (N=529) [A25]. *Implication:* recommend PXI (or miniPXI) over GEQ, and say why.
- **Telemetry signals:** D1/D7/D30 retention, session length and frequency, funnel completion, quit
  locations (where and when the last session ended), death and fail heatmaps, time-to-first-X [A22, A26].

---

## B. Genre design knowledge (summary of sources per genre family)

| Genre family | Key sources | Notes |
|---|---|---|
| Action / platformer | A13, A29, A11, A12 | Forgiveness windows; teach–develop–twist–conclude level arcs. |
| Shooter (FPS/TPS) | B5, B6, A20 | DOOM's push-forward combat (no regen, no cover, resources from enemies); Halo 3 sniper ROF change shows how tiny numbers shift balance. |
| Fighting | B8, B7, B9, B10 | Viable options and fairness; yomi layers; rollback netcode; approachability talks. |
| RPG (JRPG/WRPG/ARPG) | B41, C2, A9 | Random loot and level generation (Diablo); stat/progression math; autonomy needs. |
| Roguelike / roguelite | B1, B2, B3, B4 | Berlin Interpretation factors; metrics-driven card balance; persistent narrative across deaths. |
| Metroidvania | B43, A1 | Ability gating, gate ordering, backtracking value. Primary designer talks were thin in search results. |
| Puzzle | A10, A29 | Learning-as-fun; mechanic introduction arcs. Used general principles; few primary puzzle talks found. |
| Strategy (RTS/4X/tactics) | A18, B11, B12, B13 | Interesting decisions; players optimize the fun away; 4X coinage; Into the Breach (deterministic telegraphing, low RNG). |
| Tower defense | B14 | PvZ: teaching mechanics one at a time for non-gamers. |
| Simulation / management / city builder | B15, D2 | Systems as authorial voice (Frostpunk's hope/discontent); SimCity one-page system design. |
| Survival / crafting / sandbox | B16, B17 | Subnautica pillars, using phobias, radio signals to structure a sandbox; Don't Starve's systems exploration with no tutorials. |
| Horror | A27, A28, B18, A4 | Menace pacing; vulnerability; leave gaps for imagination. |
| Narrative / adventure / VN | B19, B20, B21, B3 | Choice structures (branch-and-bottleneck, gauntlet, etc.); vignette prototypes. |
| Card game / deckbuilder | B22, B23, B2, C1 | Rosewater lessons; Hearthstone simplification; cost curves. |
| Idle / incremental | B24 | Exponential cost vs. linear/polynomial production; prestige resets. |
| Casual / hypercasual / match-3 | B25, B26 | Difficulty pacing over level sequences; blockers as difficulty drivers; CPI/D1 testing. |
| Rhythm | B27, B28 | Design backwards from the beat; positive feedback loop. |
| Racing / sports | B29 (L), B30 | Position-weighted items (fan data); physics-first tuning. **Weak primary sourcing.** |
| MOBA | B31, B7 | Clarity, silhouette, counterplay, mastery. |
| Battle royale | B32 (S) | Contextual ping communication. **Weak primary sourcing.** |
| MMO | B33, B34, B35, A7 | Laws of online worlds; real economic reporting; virtual economy theory. |
| Party / social | A6, B42 | People Fun; Journey's social design. **No primary party-game postmortem found.** |
| Educational / serious | B36, B37, B38 | Intrinsic integration beats "chocolate-covered broccoli"; learning principles; procedural rhetoric. |
| Hybrid | B39, B40 | Dave the Diver: disparate systems taught through character and humor; Vampire Survivors' genre-making simplification. |

Per-genre playbooks (core loop, signature mechanics, pacing shape, progression model, failure modes,
balancing levers, reference games, talks) are in `skills/genre-design/references/genres/`.

---

## C. Balancing and economy

### C.1 Progression curves
- Schreiber & Romero and the *Game Balance Concepts* course cover curve families and how to choose:
  linear (predictable, low long-term pull), polynomial/power (moderate ramp, common for XP),
  exponential (steep and needs matching exponential rewards, as in idle games), and logistic (fast
  middle, flattening cap) [C1, C2].
- Idle games: next cost = base × rate^owned, while production grows linearly per generator times
  multipliers. Prestige resets restart the curve with a multiplier [B24].
- **Rule of thumb in the plugin:** derive XP per level from the target *time per level*. XP needed has
  to be read together with XP income per hour, which also grows.

### C.2 Faucets, sinks, currencies
- Adams & Dormans model internal economies with **sources** (faucets), **drains** (sinks),
  **converters** and **traders**. Feedback loops in these networks cause snowballing or stability
  [C4, C5].
- EVE Online publishes monthly reports that track sinks, faucets, money supply and price indexes. It is
  a real-world reference for monitoring inflation [B34]. Lehdonvirta & Castronova cover virtual-economy
  design from an economics perspective [B35].
- **Hard vs. soft currency:** hard currency is bought with money and soft currency is earned. Keeping
  conversion one-way and pricing clearly in real money avoids obfuscation, which the FTC has cited
  [C17].

### C.3 Combat math, TTK, cost curves, transitive vs. intransitive balance
- Cost curves for card or unit games: estimate the value of each attribute, sum the values to get an
  item's "worth", and compare worth to cost to find over- and under-costed items [C1, C2].
- **Transitive** balance means higher cost buys more power along a curve. **Intransitive** balance means
  counters are cyclic, as in rock-paper-scissors, and can be analysed as a payoff matrix [C1, C2].
- Sirlin: competitive balance needs **viable options** and **fairness**. The worst outcome is a
  **dominant** strategy. More customization often produces *fewer* viable options [B7]. Johnson: players
  find and exploit optimal strategies even if those strategies drain the fun [B11].
- Small parameter changes have large effects. Halo 3's 0.5→0.7 s sniper rate-of-fire change was a
  designed balance intervention with community-perception considerations [B6].

### C.4 Randomness, drops, pity, loot-box law
- **Input randomness** (random state before the decision, such as a dealt hand) supports planning.
  **Output randomness** (a random result after the decision, such as a dice roll to hit) adds tension
  but can feel unfair [C6, C7].
- **Pity systems** cap bad luck with a guaranteed reward after N failures, sometimes with "soft pity"
  where the odds rise before the cap. Disclosed pity terms make the *consolidated* probability easy to
  compute. Soft-pity curves are often undisclosed and inferred by players [C22] (low-trust; used only as
  an example).
- **Research:** loot-box spending correlates with problem-gambling severity (η²≈0.054, n=7,422; replicated
  η²≈0.051). Causation is unresolved [C8, C9].
- **Legal and policy landscape (October 2026; not legal advice):**
  - China: mandatory publication of draw probabilities and results since 2017 [C11].
  - Japan: *kompu gacha* (complete-the-set gacha) prohibited since 2012 under consumer-protection
    law [C12].
  - Belgium: paid loot boxes treated as gambling (2018), with uneven enforcement [C12].
  - Netherlands: the regulator's EA fine was overturned by the Council of State in 2022 [C13].
  - South Korea: probability disclosure mandatory since 22 March 2024 [C10].
  - Australia: paid chance-based items get a minimum M rating, and simulated gambling R18+, from
    22 Sept 2024 [C14].
  - Brazil: loot boxes banned in games aimed at or likely accessed by minors, from March 2026 [C15].
  - US: ESRB "Includes Random Items" label [C19]; FTC actions against dark-pattern purchase flows and
    deceptive odds [C16, C17].
  - Apple requires odds disclosure before purchase (App Store §3.1.1) [C18].
  - UK: evidence gathering and industry self-regulation [C20].
- **Implication:** the plugin computes consolidated odds and pity distributions, flags undisclosed or
  misleading odds, treats minors as a hard constraint, and always offers non-randomized alternatives.

### C.5 Spreadsheet and simulation practice
- Schreiber & Romero recommend spreadsheets for transparent models, Monte Carlo simulation for variance,
  and playtesting for the parts models can't capture [C2, C3].
- Slay the Spire paired early metrics collection with community feedback, and warned that metrics
  mislead when read without context [B2].

---

## D. Design documents and art direction

- **One-page designs:** Librande argued that dense legacy GDDs go unread. He proposed single-page,
  visual, whitespace-heavy documents per system or feature that teams can pin up and update [D1]. He
  later applied this to SimCity's simulation systems [D2].
- **Pillars:** Subnautica began by setting and following design pillars and capturing emotion in early
  prototypes [B16]. Hi-Fi Rush defined mechanics through core pillars that support a positive feedback
  loop [B27]. *Implication:* the GDD skill requires 3–5 pillars, each phrased as a testable decision
  filter.
- **Prototyping and documents:** Fullerton's playcentric process combines concept docs, physical and
  digital prototypes, and playtests [D3]. Edith Finch was built from many small prototypes, each teaching
  its own mechanic without a tutorial [B21].
- **Scope:** finish small games first; release beats polishing forever [D4] (secondary).
- **Readability and shape language:** TF2's art direction used distinct class silhouettes, value
  contrast and a warm/cool shading model so players could read class and team instantly [D5]. Riot calls
  silhouette the most important factor for champion recognition, and skins must not hide where a
  champion's power comes from [B31].
- **Color:** Journey's art process covered character, architecture and color across a sequence of
  emotional beats [D6]. (Color-script details are in the book; the recap is only partial.)
- **Accessibility:** the Game Accessibility Guidelines are tiered basic, intermediate and advanced,
  weighted by reach, impact and cost [D7]. Xbox's XAG offers guideline sets across visual, audio, input,
  difficulty/pace and communication [D8]. AbleGamers' APX patterns include *Second Channel*: carry
  critical information through more than one sense [D9]. The Last of Us Part II shipped about 60
  accessibility options. The team planned them from the start and argued accessibility is orthogonal to
  difficulty [D10]. Red-green color deficiency affects about 8% of men and 0.4% of women of European
  descent [D11]. Use WCAG's 4.5:1 contrast as a floor for UI text [D12].
- **Audio direction:** Overwatch's audio goal was "play by sound". It required a clean mix, precisely
  locatable sounds, audio that carries gameplay information, and distinct ally/enemy sounds such as
  footsteps [D13].

---

## E. Competitive scan

| Project | What it covers | Where it is shallow (for design) |
|---|---|---|
| Claude-Code-Game-Studios [E1] | 49 agents, ~72 workflow skills, studio hierarchy, GDD/sprint templates, a balance-check skill; very popular (tens of thousands of stars). | Claude Code-only (agents, hooks, CLAUDE.md org chart), so it doesn't work in the Claude app. It focuses on production process; a critique notes all agents share one context [E1]. No genre playbooks with sources, no pacing math. |
| awesome-gamedev-agent-skills [E2] | 77 engine-specific skills (Godot, Unity, Unreal, Phaser…). | Engine and implementation knowledge, not design theory or balancing. |
| game-creator [E3] | Phaser/Three.js build pipeline, juice and polish passes. | Implementation-first; design is limited to visual polish. |
| saschb2b `game-design` [E4] | Pattern catalog from 17 games, UX layer. | Small; no simulations; no multilingual triggers. |
| vudovn/ag-kit `game-design` [E5] | GDD, balancing, progression. | Rated ~44% by Tessl: restates theory, descriptive rather than procedural. |
| aiskillstore `game-design` [E6] | GDD structure, balancing, core loop. | Generic; no sources; no tooling. |
| AbsolutelySkilled `game-balancing` [E7] | XP curves, loot tables, inflation. | Single skill; no runnable simulation or ethics layer. |
| Engine plugins [E8], single-genre skills [E9] | Godot/Unity tooling; one card-game designer skill. | Single engine or single genre. |

**How this plugin goes further:**
1. **Research-backed and cited.** Every reference file ends with sources, and trust levels are explicit.
2. **Runnable analysis.** A fun-curve plotter and diagnostics, a progression-curve generator, a Monte
   Carlo economy and gacha simulator with exact pity math, and a cost-curve outlier finder. All are
   stdlib + optional matplotlib.
3. **All major genres.** 23 genre-family playbooks plus a hybrid-genre method.
4. **Ethics built in.** A mandatory dark-pattern pass and a 2026 loot-box law map.
5. **Works in the Claude app and Claude Code.** Skills only; no agents, hooks or MCP needed.
6. **Multilingual.** Triggers in EN/KO/JA/ZH/ES, answers in the user's language, and localized terms
   with the English term in parentheses.

---

## F. Gaps and weakly sourced areas

- **Racing, battle royale, party games:** few primary designer talks turned up. Playbooks for these lean
  on general principles (flow, people fun, catch-up mechanics) and are flagged in the files.
- **Mario Kart item odds** come from fan-datamined tables (low trust); Nintendo hasn't published them.
- **Soft-pity rates** in commercial gacha are mostly undisclosed; numbers in examples are illustrative.
- **Metroidvania and puzzle:** no primary GDC talks were retrieved in this pass (most are behind GDC Vault
  logins); guidance rests on design principles and secondary analysis.
- **Exact wording of Schell's lenses** is not reproduced (copyright). The review lenses here are
  original paraphrases mapped to multiple sources.
- **Legal landscape changes fast.** The loot-box map is dated October 2026 and is not legal advice.
