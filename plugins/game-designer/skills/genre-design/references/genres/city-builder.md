# City builder

Build and manage a settlement or city: zoning, infrastructure, services, population needs.
Variants: classic SimCity-likes, survival city builders (Frostpunk, Banished), colony sims
(RimWorld-adjacent), cozy builders (no fail state), and Anno-style production chains.

## Core loop
Zone or place buildings → population and needs respond → services and infrastructure strain
(traffic, power, happiness) → fix the bottleneck → the city grows → new needs and tiers
unlock.

## Signature mechanics
- Zoning vs. direct placement; road and network building.
- Service coverage radii (health, fire, police, education).
- Population tiers with rising needs (Anno: higher tiers need more goods).
- Overlays and heatmaps (land value, traffic, pollution).
- External pressure: disasters, weather, winter (survival builders), events.

## Pacing shape
Early: quick growth and frequent unlocks, which is satisfying. Mid: problems multiply (traffic,
budgets) and become the source of challenge. Late: optimization and beautification, with
risk of a plateau. Survival builders impose an external pacing curve, such as escalating
cold or storms, that sets the peaks.

## Progression model
Population milestones unlock buildings and policies. Tiered needs force supply chains to
expand. Scenario and campaign goals give direction. Sandbox mode lets players set their own
goals and express themselves through layout.

## Balancing levers
- Growth rate vs. service demand (how fast problems arrive).
- Budget: taxes vs. upkeep (faucets vs. sinks).
- Service radii and capacities.
- Traffic model complexity, which shapes how much road layout matters.
- Disaster frequency and severity; recovery cost.

## Failure modes
- **Death spirals:** one failure cascades (no money → no services → people leave → no money)
  with no recovery tools.
- **Optimal grid syndrome:** one layout beats every creative one.
- **Late-game nothing to do:** a self-sustaining city with no new goals.
- **Opaque simulation:** "Why are they unhappy?" Make causes traceable.
- **Performance limits at scale**, which decide your maximum city size. Know them early.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| SimCity (classic) | Readable cause-and-effect overlays turn urban planning into a toy |
| Cities: Skylines | Deep traffic simulation makes road design the central creative puzzle |
| Frostpunk | An external survival clock plus moral laws gives the city a dramatic arc and a theme |
| Townscaper | A no-goals building toy: pure Expression and Submission aesthetics, zero failure |

## Talks and postmortems
- Librande, *Simulating a City, One Page at a Time* (GDC 2013): designing SimCity's
  simulation systems as one-page designs.
- Fijak, *Ghost in the Machine* (GDC IGS): Frostpunk's systems as authorial voice.

## Design questions
1. What is the most common way a city fails, and what tool lets players recover?
2. Which layout decisions express personality, and which are solved optimization?
3. What creates new goals at population 10×, 100×, 1000× the start?
4. What does the player see to explain unhappiness or a budget deficit?

## Sources
- [D2] Librande (2013). https://gdcvault.com/play/1017708/Simulating-a-City-One-Page
- [B15] Fijak (GDC IGS). · [C4] Adams & Dormans (2012): feedback loops in economies.
- Full bibliography: `research/SOURCES.md` in the repository.
