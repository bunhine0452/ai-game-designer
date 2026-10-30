# Economy design: faucets, sinks and currencies

## The model

An internal economy is a network of:
- **Sources (faucets):** create resources (quest rewards, loot, daily login, generators).
- **Drains (sinks):** destroy resources (purchases, upgrades, repairs, taxes, consumables).
- **Converters:** turn one resource into another (crafting, refining).
- **Traders:** exchange between actors (players, NPC shops, auction houses).
- **Pools:** where resources accumulate (wallets, banks, inventories).

Feedback loops in this network decide behavior. **Positive feedback** (more gold → better
gear → more gold) snowballs. **Negative feedback** (rising costs, taxes, diminishing returns)
stabilizes. Machinations-style diagrams (Adams & Dormans) help to sketch it before running
numbers.

## Currency design

| Type | Earned by | Typical use | Risks |
|---|---|---|---|
| Soft currency | Play | Upgrades, consumables, shops | Inflation if sinks don't scale |
| Hard / premium currency | Real money (and small earnable amounts) | Cosmetics, convenience, gacha | Price obfuscation; spending pressure on minors |
| Event / token currency | Time-limited activities | Event shops | FOMO pressure |
| Crafting materials | Drops, gathering | Converters | Inventory bloat |
| Reputation / XP-like | Activity | Unlock gates | Grind walls |

Guidelines:
- **Few currencies.** Each new currency adds UI weight and confusion. Ask whether it does
  anything a soft currency can't.
- **Show real-money prices.** Hiding the real cost behind premium currency, especially in odd
  bundle sizes that leave leftovers, has drawn regulator attention (for example, the 2025 FTC
  settlement with HoYoverse over obscured loot-box costs).
- **Convert in one direction only** (hard → soft is fine; soft → hard invites real-money
  trading and arbitrage).

## Inflation and how to control it

Inflation happens when faucets outgrow sinks: balances pile up, prices tied to the currency
stop meaning anything, and newcomers get priced out of player markets.

Controls:
1. **Scaling sinks:** costs that grow with progression (upgrade tiers, consumables and repairs
   that scale with level, percentage-based taxes on trades).
2. **Prestige and cosmetic sinks** for late-game wealth (houses, cosmetics, vanity items).
3. **Faucet discipline:** cap repeatable faucets; use diminishing returns on farming.
4. **Item decay or destruction** (durability, consumption) in player-driven economies.
5. **Monitoring:** track faucet and sink totals by source, the money supply and price indexes
   over time. EVE Online publishes monthly economic reports with exactly this data.

## Reading `economy_sim.py` results

- **In/Out ratio (last third):** total inflow divided by outflow in the final third of sessions.
  Around 1.0–1.2 is stable; above 1.25 with rising median balances means inflation.
- **Median balance trend:** the rise per session, and how many sessions of income players
  hoard.
- **Gini of final balances:** 0 means equal, 1 means one player holds everything. High
  values are fine in single-player but harmful in shared markets.
- **STARVATION / SLOW_SINK:** the median player can't afford the core purchase. The economy is
  too tight, or the price is too high.
- **Archetype table:** check casual vs. engaged vs. spender outcomes. A big gap in *power*
  (rather than convenience or cosmetics) is a pay-to-win signal.

## Worked example (see `examples/economy-walkthrough.md`)

Draft: gold faucet growth 7% per session vs. upgrade cost growth 5% per purchase, at one
upgrade per session. That gives a late In/Out of 1.51 and the median balance keeps rising
(INFLATION). Fix: allow two upgrades per session and add consumables at 18% of gold income
(a sink that scales with income). Late In/Out drops to 1.01.

## Sources
- [C4] Adams & Dormans (2012), *Game Mechanics: Advanced Game Design*. · [C5] Dormans (2012), *Engineering Emergence*.
- [B34] CCP, EVE Online Monthly Economic Reports. https://www.eveonline.com/news/view/monthly-economic-report-november-2024
- [B35] Lehdonvirta & Castronova (2014), *Virtual Economies*.
- [C17] FTC–HoYoverse settlement (2025, coverage). · [C16] FTC–Epic orders (2022).
- [C2] Schreiber & Romero (2021).
- Full bibliography: `research/SOURCES.md` in the repository.
