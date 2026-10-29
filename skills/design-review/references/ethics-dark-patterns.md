# Ethics and dark-pattern check

Zagal, Björk & Lewis define **dark game design patterns** as patterns a designer uses on
purpose to create negative experiences for players that go against their interests, likely
without their consent. Regulators now act on similar patterns. The FTC's 2022 Epic orders
($245M in refunds) concerned purchase flows that caused unwanted charges. Its 2025 HoYoverse
settlement concerned misleading loot-box odds and obscured prices aimed at minors.

Run this check for **every** review that touches retention or monetization. Mark each pattern
**present**, **at risk** or **absent**, and give a healthy alternative for anything not absent.

## Taxonomy and healthy alternatives

| Category | Pattern | What it looks like | Healthy alternative |
|---|---|---|---|
| Temporal | **Grinding** | Repetitive, low-decision play required to progress | Remove the need, add decisions, or offer variety; respect time-per-level targets |
| Temporal | **Playing by appointment** | Rewards or progress lost unless the player logs in at set times; streaks that reset | Accumulating rewards (e.g. claim up to 7 days later); streaks that pause rather than reset |
| Temporal | **Infinite treadmill** | Progress that never resolves, used to keep players paying | Clear end states, seasons with endings, opt-in endless modes |
| Monetary | **Pay to skip** | Friction designed in so players pay to remove it | Tune friction for fun first; sell convenience that isn't required |
| Monetary | **Pre-delivered content** | Content on disc or in the download, locked behind payment | Sell new content; be transparent about what's included |
| Monetary | **Monetized rivalries** | Spending decides competitive outcomes (pay-to-win) | Cosmetic or side-grade purchases; separate brackets |
| Monetary | **Obfuscated pricing** | Premium-currency bundles sized to leave remainders; hidden real cost | Show real-money prices; currency packs that match item prices |
| Monetary | **Accidental purchases** | One-button buys, confusing button layouts, no confirmation | Explicit confirmation, easy refunds, parental controls |
| Monetary | **Undisclosed or misleading odds** | Random paid items without rates, or headline rates that hide pity mechanics | Disclose base rates, consolidated rates and pity terms before purchase |
| Social | **Social pyramid schemes** | Progress requires recruiting or pestering friends | Optional social bonuses; never gate core progress on recruiting |
| Social | **Impersonation** | Messages that appear to come from friends but are automated | Only real player actions are shown as player actions |
| Psychological | **FOMO pressure** | Countdown timers, "last chance", limited banners stacked back to back | Rotating returns of limited items; clear schedules |
| Psychological | **Sunk-cost and endowed value** | "You'll lose your progress or items" to stop players leaving | Let players leave cleanly; no loss for absence |
| Psychological | **Near-miss and variable-reward theatrics** | Slot-machine animations, "almost got it!" reveals | Plain result reveals; deterministic progress next to chance |
| Psychological | **Confirmshaming** | "No thanks, I don't like winning" buttons | Neutral wording |
| Interface | **Hidden or nagging prompts** | Hard-to-close offers, repeated pop-ups after a refusal | One clear offer; respect "no" for the session |

## Minors and compliance checklist (not legal advice; check current law)

- [ ] No paid random items in games aimed at or likely played by minors (Brazil prohibits them
      from March 2026; Australia requires at least an M rating for paid chance items from Sept 2024).
- [ ] Probability disclosure: base rates, pity, and where shown (in game, store pages, ads),
      required in South Korea (since March 2024) and China (since 2017), and by Apple §3.1.1.
- [ ] Real-money prices visible; no remainder-bundle obfuscation.
- [ ] Parental consent for purchases by younger players (the FTC–HoYoverse settlement requires
      it for under-16s in that case) and age-appropriate data handling (children's privacy
      law; both FTC cases included privacy violations).
- [ ] Ratings labels: ESRB "In-Game Purchases (Includes Random Items)", PEGI equivalents.
- [ ] Refund path for accidental purchases.
- [ ] Spending limits or spending dashboards (good practice).

## Three questions to ask the team

1. Would we be comfortable explaining this mechanic, and its purpose, to players in a patch note?
2. If a player fully understood how it works, would they still choose it?
3. Does it make the game better for the player, or only better at metrics?

## Sources
- [A15] Zagal, Björk & Lewis (2013), *Dark Patterns in the Design of Games*, FDG. https://gup.ub.gu.se/file/101018
- [A14] Hopson (2001; 2012 follow-up): reward contingencies and their misuse.
- [C8]/[C9] Zendle & Cairns (2018, 2019): loot boxes and problem gambling.
- [C16] FTC–Epic (2022). · [C17] FTC–HoYoverse (2025). · [C10] Korea. · [C11] China. · [C14] Australia. · [C15] Brazil. · [C18] Apple. · [C19] ESRB. · [C12] Comparative review.
- Full bibliography: `research/SOURCES.md` in the repository.
