# Gacha deep dive: featured SSR, spark, carry-over, paid/free stones

Exact math from a fresh account; simulation uses each config's players, sessions and seed.

![featured CDF](featured_cdf.png)

## Scenarios (exact)

| Scenario | SSR base | Pulls/SSR | Featured mean | p50 | p90 | p99 | Max | Via spark | JPY mean | JPY p90 | JPY max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| hoshiyobi_economy_v1 | 2.00% | 50.0 | 95.1 | 69 | 230 | 300 | 300 | 4.9% | 23,779 | 57,512 | 75,015 |
| hoshiyobi_economy_v2 | 3.00% | 33.3 | 47.1 | 38 | 108 | 120 | 120 | 7.4% | 11,779 | 27,005 | 30,006 |
| A_carryover_only | 2.00% | 50.0 | 95.1 | 69 | 230 | 300 | 300 | 4.9% | 23,779 | 57,512 | 75,015 |
| B_spark200_carry | 2.00% | 50.0 | 86.6 | 69 | 200 | 200 | 200 | 13.4% | 21,655 | 50,010 | 50,010 |
| C_rate3_guarantee_spark120 | 3.00% | 33.3 | 47.1 | 38 | 108 | 120 | 120 | 7.4% | 11,779 | 27,005 | 30,006 |
| D_hard80_guarantee_spark200 | 2.00% | 36.2 | 54.3 | 58 | 102 | 130 | 146 | 0.0% | 13,576 | 25,505 | 36,507 |
| C2_same_as_C_but_paid_first | 3.00% | 33.3 | 47.1 | 38 | 108 | 120 | 120 | 7.4% | 11,779 | 27,005 | 30,006 |
| E_hard70_guarantee_spark120 | 2.00% | 34.9 | 52.3 | 56 | 98 | 120 | 120 | 1.3% | 13,070 | 24,505 | 30,006 |

## Scenarios (simulated banner outcomes)

| Scenario | Archetype | Avg JPY | Avg pulls | Avg featured | Win rate on wanted banners | Via spark | Lost pity / player | Lost spark pts / player | JPY per featured | End free | End paid |
|---|---|---|---|---|---|---|---|---|---|---|---|
| hoshiyobi_economy_v1 | light_f2p | 0 | 49.8 | 0.47 | 13% | 0% | 0.0 | 45.8 | 0 | 852 | 0 |
| hoshiyobi_economy_v1 | core_f2p | 0 | 92.6 | 0.93 | 22% | 0% | 0.0 | 83.8 | 0 | 1,350 | 0 |
| hoshiyobi_economy_v1 | monthly_pass | 1,635 | 122.5 | 1.20 | 24% | 0% | 0.0 | 105.6 | 1,360 | 1,419 | 201 |
| hoshiyobi_economy_v1 | dolphin | 29,401 | 233.4 | 2.40 | 38% | 0% | 0.0 | 210.1 | 12,237 | 812 | 909 |
| hoshiyobi_economy_v1 | whale | 116,364 | 567.8 | 4.73 | 44% | 0% | 0.0 | 557.1 | 24,615 | 70 | 23 |
| hoshiyobi_economy_v2 | light_f2p | 0 | 49.0 | 0.83 | 23% | 0% | 0.0 | 0.0 | 0 | 988 | 0 |
| hoshiyobi_economy_v2 | core_f2p | 0 | 88.0 | 1.70 | 40% | 0% | 0.0 | 0.0 | 0 | 2,083 | 0 |
| hoshiyobi_economy_v2 | monthly_pass | 1,677 | 112.4 | 2.53 | 52% | 20% | 0.0 | 0.0 | 664 | 2,540 | 355 |
| hoshiyobi_economy_v2 | dolphin | 29,576 | 194.6 | 5.04 | 82% | 24% | 0.0 | 0.0 | 5,869 | 2,899 | 5,285 |
| hoshiyobi_economy_v2 | whale | 116,364 | 494.0 | 12.64 | 95% | 30% | 0.0 | 0.0 | 9,209 | 784 | 11,477 |
| A_carryover_only | light_f2p | 0 | 49.9 | 0.48 | 14% | 0% | 0.0 | 0.0 | 0 | 835 | 0 |
| A_carryover_only | core_f2p | 0 | 92.5 | 0.95 | 22% | 0% | 0.0 | 0.0 | 0 | 1,392 | 0 |
| A_carryover_only | monthly_pass | 1,662 | 119.3 | 1.22 | 25% | 0% | 0.0 | 0.0 | 1,366 | 1,985 | 242 |
| A_carryover_only | dolphin | 29,751 | 234.9 | 2.27 | 36% | 0% | 0.0 | 0.0 | 13,090 | 794 | 723 |
| A_carryover_only | whale | 115,455 | 568.2 | 5.36 | 48% | 20% | 0.0 | 0.0 | 21,525 | 36 | 25 |
| B_spark200_carry | light_f2p | 0 | 50.0 | 0.48 | 14% | 0% | 0.0 | 0.0 | 0 | 851 | 0 |
| B_spark200_carry | core_f2p | 0 | 92.3 | 0.95 | 23% | 0% | 0.0 | 0.0 | 0 | 1,454 | 0 |
| B_spark200_carry | monthly_pass | 1,659 | 121.8 | 1.11 | 22% | 0% | 0.0 | 0.0 | 1,497 | 1,440 | 204 |
| B_spark200_carry | dolphin | 29,687 | 223.5 | 3.44 | 54% | 26% | 0.0 | 0.0 | 8,626 | 1,646 | 1,992 |
| B_spark200_carry | whale | 119,091 | 584.2 | 6.55 | 65% | 32% | 0.0 | 0.0 | 18,194 | 44 | 21 |
| C_rate3_guarantee_spark120 | light_f2p | 0 | 49.0 | 0.83 | 23% | 0% | 0.0 | 0.0 | 0 | 988 | 0 |
| C_rate3_guarantee_spark120 | core_f2p | 0 | 88.0 | 1.70 | 40% | 0% | 0.0 | 0.0 | 0 | 2,083 | 0 |
| C_rate3_guarantee_spark120 | monthly_pass | 1,677 | 112.4 | 2.53 | 52% | 20% | 0.0 | 0.0 | 664 | 2,540 | 355 |
| C_rate3_guarantee_spark120 | dolphin | 29,576 | 194.6 | 5.04 | 82% | 24% | 0.0 | 0.0 | 5,869 | 2,899 | 5,285 |
| C_rate3_guarantee_spark120 | whale | 116,364 | 494.0 | 12.64 | 95% | 30% | 0.0 | 0.0 | 9,209 | 784 | 11,477 |
| D_hard80_guarantee_spark200 | light_f2p | 0 | 49.7 | 0.60 | 17% | 0% | 0.0 | 0.0 | 0 | 909 | 0 |
| D_hard80_guarantee_spark200 | core_f2p | 0 | 89.6 | 1.43 | 34% | 0% | 0.0 | 0.0 | 0 | 1,852 | 0 |
| D_hard80_guarantee_spark200 | monthly_pass | 1,638 | 115.3 | 1.88 | 38% | 0% | 0.0 | 0.0 | 873 | 2,246 | 278 |
| D_hard80_guarantee_spark200 | dolphin | 29,560 | 206.9 | 4.60 | 74% | 18% | 0.0 | 0.0 | 6,430 | 2,330 | 3,328 |
| D_hard80_guarantee_spark200 | whale | 114,545 | 548.5 | 11.91 | 91% | 17% | 0.0 | 0.0 | 9,618 | 492 | 1,757 |
| C2_same_as_C_but_paid_first | light_f2p | 0 | 49.0 | 0.83 | 23% | 0% | 0.0 | 0.0 | 0 | 988 | 0 |
| C2_same_as_C_but_paid_first | core_f2p | 0 | 88.0 | 1.70 | 40% | 0% | 0.0 | 0.0 | 0 | 2,083 | 0 |
| C2_same_as_C_but_paid_first | monthly_pass | 1,677 | 112.4 | 2.53 | 52% | 20% | 0.0 | 0.0 | 664 | 2,723 | 172 |
| C2_same_as_C_but_paid_first | dolphin | 29,576 | 194.6 | 5.04 | 82% | 24% | 0.0 | 0.0 | 5,869 | 6,505 | 1,679 |
| C2_same_as_C_but_paid_first | whale | 116,364 | 494.0 | 12.64 | 95% | 30% | 0.0 | 0.0 | 9,209 | 5,920 | 6,341 |
| E_hard70_guarantee_spark120 | light_f2p | 0 | 49.7 | 0.62 | 18% | 0% | 0.0 | 0.0 | 0 | 872 | 0 |
| E_hard70_guarantee_spark120 | core_f2p | 0 | 90.1 | 1.53 | 36% | 0% | 0.0 | 0.0 | 0 | 1,730 | 0 |
| E_hard70_guarantee_spark120 | monthly_pass | 1,623 | 111.4 | 2.37 | 49% | 21% | 0.0 | 0.0 | 683 | 2,637 | 355 |
| E_hard70_guarantee_spark120 | dolphin | 29,600 | 200.3 | 5.36 | 84% | 23% | 0.0 | 0.0 | 5,519 | 2,559 | 4,314 |
| E_hard70_guarantee_spark120 | whale | 119,091 | 518.9 | 13.27 | 100% | 29% | 0.0 | 0.0 | 8,973 | 726 | 8,652 |

## Paid stones (有償石)

| Scenario | Consume order | Paid share of gacha spend | Unused paid balance per 1,000 players (JPY) |
|---|---|---|---|
| hoshiyobi_economy_v1 | free_first | 8.9% | 92,548 |
| hoshiyobi_economy_v2 | free_first | 7.3% | 504,445 |
| A_carryover_only | free_first | 9.0% | 87,616 |
| B_spark200_carry | free_first | 8.7% | 162,551 |
| C_rate3_guarantee_spark120 | free_first | 7.3% | 504,445 |
| D_hard80_guarantee_spark200 | free_first | 8.2% | 276,785 |
| C2_same_as_C_but_paid_first | paid_first | 9.0% | 195,039 |
| E_hard70_guarantee_spark120 | free_first | 7.7% | 416,292 |

_A model, not a forecast: replace archetype shares and behaviour with telemetry._
