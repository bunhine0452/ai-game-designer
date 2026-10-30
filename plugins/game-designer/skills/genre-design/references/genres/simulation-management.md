# Simulation, management and tycoon

Covers business and tycoon games, management sims (hospital, zoo, theme park, prison),
factory and automation games, life sims and vehicle or job simulators. City builders have
their own file.

## Core loop
Observe the system state → identify a bottleneck or opportunity → build or adjust (place,
hire, research, set a policy) → let the simulation run → read the results (money,
satisfaction, throughput) → optimize again.

## Signature mechanics
- Interlocking systems with feedback loops (demand ↔ supply ↔ prices ↔ satisfaction).
- Resource chains and converters (raw → intermediate → product).
- Agents with needs (guests, patients, workers) who make visible decisions.
- Data overlays, graphs and tooltips explaining *why* something happens.
- Time controls (pause, speed-up).

## Pacing shape
Early: small, fast feedback (first sale, first customer). Mid: complexity grows, with new
systems unlocked one at a time. Late: optimization and scale, often a plateau. Scenarios,
challenges, disasters or prestige goals add new peaks. Players set their own goals in
sandbox modes.

## Progression model
Unlock trees (buildings, research), scenario campaigns with goals, and growing scale.
Factorio-style automation games progress by **automating what you did by hand before**.
That's a strong, self-reinforcing loop.

## Balancing levers
- Converter ratios and throughput (set up in a spreadsheet, check by simulation).
- Price elasticity and the demand model.
- Upkeep and running costs (sinks) vs. income (faucets).
- How fast complexity is introduced.
- Failure pressure: bankruptcy thresholds, disasters, satisfaction decay.

## Failure modes
- **Opaque simulation:** players can't tell why numbers changed. Add overlays, cause
  tooltips and agent thoughts.
- **Solved economy:** one optimal layout or product, endlessly repeated.
- **Late-game plateau:** money stops mattering (inflation, no sinks).
- **Micromanagement with no new decisions.**
- **Punitive failure states** that wipe out hours of work without warning.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| RollerCoaster Tycoon | Visible guest thoughts explain the simulation and make players care |
| Factorio | Automation as progression; the "factory must grow" loop compounds itself |
| Two Point Hospital | Humor and readable rooms lower the barrier to a complex management sim |
| Frostpunk | Societal systems (hope, discontent, laws) carry the game's message and force moral trade-offs |

## Talks and postmortems
- Fijak, *Ghost in the Machine: Authorial Voice in System Design, Frostpunk & Beyond* (GDC IGS).
- Librande, *Simulating a City, One Page at a Time* (GDC 2013).
- Adams & Dormans, *Game Mechanics: Advanced Game Design*: internal economies (sources,
  drains, converters).

## Design questions
1. Can a player trace any number on screen back to its causes within two clicks?
2. Which feedback loop is positive (snowballing), which negative (stabilizing), and which do
   you want in charge?
3. What new decision appears every 30–60 minutes?
4. What's the late-game goal once money no longer matters?

## Sources
- [B15] Fijak, GDC IGS. https://gdcvault.com/play/1027186/Independent-Games-Summit-Ghost-in
- [D2] Librande (2013). · [C4] Adams & Dormans (2012).
- Full bibliography: `research/SOURCES.md` in the repository.
