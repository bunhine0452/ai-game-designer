# Survival and crafting

Survive a hostile environment by gathering, crafting, building and managing needs (hunger,
temperature, sanity, oxygen). Variants: open-world survival, survival-exploration
(Subnautica), co-op survival (Valheim), and survival with strong narrative goals.

## Core loop
Need pressure (hunger, cold, night) → gather resources → craft tools, food, shelter → push
further into danger for better resources → craft better gear → push further.

## Signature mechanics
- Needs meters that decay over time.
- Crafting recipes and tech tiers, gated by resources from deeper or riskier areas.
- Base building as safety and as a sink.
- Day/night or weather cycles that set pacing.
- Exploration with dangerous frontiers (depth, biome, distance).

## Pacing shape
Early: tense and scarce, with every resource precious. Mid: comfort rises, with the base
secure and needs automated. The risk here is a *comfort plateau*. Late: the frontier gets more
dangerous (deep biomes, bosses) or a narrative goal pulls the player forward. Day/night
cycles add a short-term tension-and-release rhythm.

## Progression model
Tech tiers unlocked by resources from riskier zones, which means the progression **is** the
exploration. Subnautica used radio signals and mysterious tooltips to give the sandbox a
structure, and used depth as the difficulty dial. Don't Starve expected players to learn its
systems by exploring, with no tutorials.

## Balancing levers
- Need decay rates vs. resource availability.
- Crafting costs per tier; resource rarity by zone.
- Risk vs. reward of the frontier (enemy strength vs. resource value).
- Death penalty: lose inventory? corpse run? permadeath?
- Automation timing: when the chores of early survival become automated.

## Failure modes
- **Chore fatigue:** meters demand attention but no longer create decisions.
- **Comfort plateau:** once safe, there's no reason to take risks.
- **Inventory tedium:** small bags, unclear recipes, endless sorting.
- **No direction:** a vast sandbox and no idea what to aim for.
- **Punishing death** that wipes hours of progress without a lesson.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Subnautica | Depth equals difficulty equals curiosity; it uses players' fear of the deep, and radio signals structure the sandbox |
| Don't Starve | Lethal systems learned by exploring; a strong art direction sets it apart |
| Valheim | Co-op survival with boss-gated tiers gives groups shared milestones |
| Minecraft | Survival mode with an optional goal (the End) and infinite expression; the night creates the first tension |

## Talks and postmortems
- Cleveland, *The Design of Subnautica* (GDC 2019): pillars, emotion-first prototyping,
  using phobias, radio signals.
- Klei, *Don't Starve* GDC session and interviews: systems exploration without tutorials.

## Design questions
1. Which needs create *decisions*, and which only create *chores*? Cut or automate the
   chores.
2. What pulls the player out of their safe base at hour 10?
3. How does the frontier get more dangerous, and what makes it worth the risk?
4. What does the player lose on death, and what do they learn?

## Sources
- [B16] Cleveland (2019). https://gdcvault.com/play/1025745/The-Design-of-Subnautica
- [B17] Klei / Don't Starve (GDC session; interview, secondary).
- [A9] SDT: competence and autonomy vs. chores.
- Full bibliography: `research/SOURCES.md` in the repository.
