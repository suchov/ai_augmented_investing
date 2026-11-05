# 2026-11-01 — BRK.B: DCF addendum to the 2026-08-15 hold decision

**Ticker:** BRK.B
**Verdict:** **Hold the core, partial trim order placed (2026-11-01):** GTC limit sell of ~50% of the position at $560 (see "Order placed" section). The remaining ~half stays. Price is slightly above my weighted DCF value; no `revisit_if` from the 2026-08-15 entry is fully hit, one is partially met (#3, see trigger check). Re-run after Q3 results (Nov 6–7).
**Price at time of writing:** $542.49 (Oct 30 close). Updated 2026-11-03: **$556.11 (Nov 2 close**, from the Morningstar report). The tables below use $542.49; see "Morningstar cross-check" for the updated comparison.
**Position context:** ~92.7% of portfolio (self-reported 2026-11-01); ~91% on 2026-08-15.

---

## Why this addendum

BRK.B closed at a record $539.82 on Oct 20 (first record since May 2025). Price is up ~7.6% since 2026-08-15 ($504.03 → $542.49, my arithmetic). Worry: "there might be a drop behind this." Asked for a DCF to replace the feeling with numbers.

## Method (short)

- **Operating businesses (ex investment income):** after-tax earnings ≈ $36B TTM (underwriting, BNSF, BHE, manufacturing/service/retail, other). Valued with FCFE DCF: FCFE = earnings × (1 − g / ROIC). Hurdle 9%, 10 explicit years + terminal.
- **Investments at market:** cash and T-bills $364.7B + equity securities $321.9B × (1 − tax haircut).
- **Shares:** 2,147.5M B-equivalent (1,431,693 A-equivalent × 1,500) at 30 Jun 2026; book value ≈ $348 per B share.
- **Source data (Q2 2026 10-Q / 8-K):** FY2025 operating earnings $44.5B; H1 2026 $24.3B (+17%, ≈ +5% excluding FX/one-offs); float $177.5B; borrowings $43.3B (insurance and other) + $85.3B (railroad, utilities, energy), whose interest is already inside segment earnings.

## Results (per B share)

| | Bear | Base | Bull |
|---|---|---|---|
| Starting earnings of operating businesses | $33B | $36B | $37.5B |
| Growth 2027 → 2036 | 1% | 5% → 3% | 7% → 3.5% |
| Return on new investment | 8% | 10% | 12% |
| Terminal growth | 2% | 3% | 3.5% |
| Tax haircut on equity portfolio | 20% | 15% | 10% |
| Operating businesses value | $373B (11.3x) | $452B (12.6x) | $545B (14.5x) |
| **Value per share** | **$464** | **$508** | **$559** |
| vs $542.49 | −15% | −6% | +3% |

Weights 25/50/25 (subjective) → **weighted ≈ $510**. Price is ~6% above it ($556 would be ~9% above).

- **Margin of safety:** 25% → **$382**; **30% (my checklist) → $357** (≈ −34% from $542).
- **Implied return at today's price (base = price):** ≈ **8.2% per year**. This is the opportunity-cost floor for any alternative.
- **Book value cross-check:** base value ≈ 1.46x book vs price 1.56x; Berkshire's own June buybacks were at ~1.4x book (≈ $488), between my bear ($464) and base ($508).
- ~58% of value is cash + equities at market, so the scenario range is narrow by construction.

## Sensitivity

| Hurdle | Weighted | 30% MoS price |
|---|---|---|
| 8% | $554 | $388 |
| 9% | $510 | $357 |
| 10% | $478 | $335 |
| 11% | $455 | $318 |

- **Float as debt** (−$177.5B ≈ −$83 per share): weighted $427, 30% MoS $299. Base case treats float as permanent, Buffett-style.
- **Equity portfolio −30% / −50%** (operating-business value unchanged): base value $470 / $444.

## What this says about the fear

- Price is near fair value, not cheap. The ~9% run since late September was largely a defensive rotation out of AI/semiconductor stocks, not a change in intrinsic value.
- If the rotation reverses, a move toward ~$460–510 (−6% to −15% from $542) is consistent with the model. That is a range, not a prediction.
- A 30% fall in the stock portfolio only lowers base value ~7.5%, because ~$365B is cash. The price could still fall more than value.
- Reaching the 30% MoS price ($357) would need a ~34% fall. At 92.7% concentration that is ≈ −32% on the portfolio.

## Concentration arithmetic (rest of portfolio assumed flat)

| BRK.B move | Portfolio move |
|---|---|
| −20% | −18.5% |
| −30% | −27.8% |
| −50% | −46.4% |

## Trigger check vs the 2026-08-15 `revisit_if` list

1. **P/B above ~1.7x (≈ $592):** not hit (≈ 1.56x).
2. **Buybacks stopping:** not hit as of June ($4.5B in Q2). Check the monthly buyback table and average price in the Q3 10-Q.
3. **A named alternative reaching its margin-of-safety price:** **partially met.**
   - Adyen: €827 vs 30% MoS €1,009 at a 9% hurdle (`ADYEN.md` is WATCH; pre-mortem and 48-hour rule not done; fails at an 11% hurdle).
   - Cigna: ≈ at its 30% MoS only in the central stress case ($274 vs $279); fails the harshest stress.
   - Implied return if my base case holds (price = base value): BRK.B ≈ 8.2%, Adyen ≈ 13%, Broadridge ≈ 10%, Cigna ≈ 15% (headline case, before stress), GOOGL ≈ 7%. All alternative models are mine and need my review; this is not a recommendation to switch.
4. **Residency change confirmed:** no new information.
5. **Unrationalizable capital allocation by Abel:** not hit. Recent deployment reported: Alphabet, Taylor Morrison, reported ~$930M in Bending Spoons. Re-check after Q3.
6. **Concentration causing behavioral issues:** logged. Anxiety at a record high with 92.7% in one name.

## New `revisit_if` thresholds

- Price ≥ $559 (above bull-case value) → review trimming toward a lower concentration.
- Price ≤ $488 (≈ 1.4x book, June buyback level) → buyback-supported zone; hold/add review.
- Price ≤ $382 (25% MoS) or ≤ $357 (30% MoS) → add-capital review, through the checklist.
- **Q3 report (Nov 6–7):** operating earnings vs $13.48B (Q3 2025); cash trend; buyback pace and price; GEICO underwriting; refresh cash and share count and re-run the model.
- If I decide float should be treated as debt → use weighted $427 / MoS30 $299.

## Interview-mode questions (answer before any action)

1. Is the worry about the price or about concentration? If concentration, what is the target weight and how is it reached: new contributions only, or trims?
2. If BRK.B fell 35% tomorrow at 92.7%, what would I do in the first 48 hours, and what cash cushion do I have outside the portfolio?
3. Which named alternative would I fund, with how much, and why does its implied return beat BRK.B's ≈ 8.2% after the stress cases?
4. What changed in the business versus the price since 2026-08-15? (Price +7.6%; Q3 numbers still pending.)

## Morningstar cross-check (added 2026-11-03)

**Source:** Morningstar Equity Analyst Report on BRK.B, as of 3 Nov 2026 (uploaded PDF). Last close in the report: **$556.11 (Nov 2)**, +2.5% vs the Oct 30 close.

| | Morningstar | My model |
|---|---|---|
| Central value per B share | $510 | $510 weighted ($508 base) |
| Downside case | $408 | $464 (bear) |
| Bull case | $638 | $559 (bull) |
| Cost of equity | 9.0% | 9.0% |
| Rating | 2 stars, Price/FVE 1.09, uncertainty Low, narrow moat, capital allocation Exemplary | — |
| 5-star / 1-star price | $408 / $637.50 | — |

- Morningstar fair value ≈ 1.45x / 1.35x estimated book value at end-2026 / end-2027; shares traded at 1.51x (5-year) and 1.45x (10-year) average trailing book.
- Their sum of the parts: insurance incl. insurance investment portfolio $247, manufacturing/service/retail $162, railroad $63, utilities/energy $38 = $510.
- **Where we differ:** Morningstar expects the insurance combined ratio to average ~97.6% in 2026–30 (vs 93.3% in 2021–25), premium growth 4.2% (vs 7.0%), and investment yield falling from 2.3% to 1.6%. Their net income path dips in 2027–28 (≈ $39–45B vs ≈ $51.6B in 2026) before recovering. My base case assumed steadier earnings, but both approaches land on the same central value.
- **Their downside case ($408):** GEICO keeps weakening, P&C pricing softens, and growth in the two non-insurance segments stalls.

### Updated numbers at $556.11

- Price vs my weighted $510: **+9.1%**. Vs Morningstar's three cases weighted 25/50/25 (≈ $517): +7.7%.
- Implied return (base case = price): **≈ 7.9% per year** (was ≈ 8.2% at $542.49).
- From $556.11: to Morningstar's downside $408 = **−27%**; to their bull case $638 = **+15%** (same for their 1-star price $637.50: +14.6%).
- 30% margin-of-safety price ($357) would need a ≈ −36% fall.
- P/B ≈ 1.60x (book ≈ $348). The `revisit_if` trigger "P/B above ~1.7x (≈ $592)" is not hit.
- The $560 limit is only **0.7% above** the Nov 2 close, so the order is likely to fill soon. The sale price is ~10% above both fair value estimates.

### Other points logged from the report

- Buffett stepped back as executive chair in Sept 2026; Howard Buffett was elected chair. Morningstar says Abel has so far focused more on maintaining the status quo than on improving returns, and that he will be judged as both operator and investor.
- Morningstar expects more buybacks (slightly above the 2018–25 average of ~$2.5B per quarter) and eventually a dividend. At ~1.6x book versus their 1.45x fair multiple, buyback pace in the Q3 10-Q is the thing to check (`revisit_if` #2).
- It estimated ~$321.6B of "dry powder" at end of Q2 and Abel's deployment since January: $25–30B into Alphabet, Taylor Morrison ($8.5B including debt), >$1.8B more into Lennar, ~$930M into Bending Spoons.
- Morningstar said after Q2 it was "likely to slightly increase" its $510 estimate, but it was still $510 as of the report.

### What this changes

Nothing in the decision. Two independent estimates put fair value near $510 and the price ~9% above it; that is consistent with a partial trim, not with an exit. The main issue remains concentration (92.7%), not valuation. The report adds no new reason to cancel the order and no reason to widen it.

## Order placed (2026-11-01)

- **Order:** SELL BRK.B (Interactive Brokers), Limit $560.00, time in force GTC, Outside RTH off.
- **Quantity:** ~50% of the position. Exact share count: [fill in]. The other ~half stays.
- **Why $560:** about 10% above my weighted DCF value ($510) and near the bull case ($559), and it matches the new threshold "price ≥ $559 → review trimming toward lower concentration."
- **Why partial:** the main issue is concentration (92.7%), not the valuation call. I am not claiming BRK.B is a bad holding.

### Effect on concentration (if exactly half is sold, proceeds not put back into BRK.B, price ≈ unchanged)

BRK.B weight falls from ~92.7% to ≈ 46–47%. Rest of portfolio assumed flat:

| BRK.B move | Portfolio move before | Portfolio move after |
|---|---|---|
| −20% | −18.5% | ≈ −9.3% |
| −30% | −27.8% | ≈ −13.9% |
| −50% | −46.4% | ≈ −23.2% |
| to the 30% MoS price ($357, ≈ −34%) | ≈ −32% | ≈ −16% |

### Costs of this action (recorded honestly)

1. **Foregone upside** if the rotation continues or Q3 is strong. My base case return from holding is ~8% per year.
2. **Tax drag.** If the average cost is still ~$495.29 (from the 2026-08-15 entry; check IBKR lots for the real number), gain ≈ $65 per share, tax at 19% ≈ $12 per share ≈ 2.2% of proceeds. A replacement must beat BRK.B by roughly 0.4–0.5 points per year over 5 years to cover it (my arithmetic). Verify the tax rules and the residency question from the 2026-08-15 entry before the order fills.
3. **Reinvestment risk.** My alternatives are my own models with many assumptions. Adyen passes the 30% margin of safety only up to a hurdle of ~10%, and its pre-mortem and 48-hour rule are not done.
4. **FX and execution.** Proceeds arrive in USD; conversion has a cost. A GTC order can fill while I am not watching.
5. **No downside protection.** A resting limit sell does nothing if the price falls.
6. **Regret risk.** If price runs above $560 after the fill I do not chase.

### Where the proceeds go

Not decided yet. Proposed default (edit): keep in USD cash until a named alternative passes its checklist (pre-mortem + 48 hours). Rule: no buying BRK.B back above $560 without a new valuation.

### Cancel or re-check the order if

- Q3 results (Nov 6–7) change my view of intrinsic value (large earnings surprise, buybacks stopping, cash/float change): re-run the model before the order can fill.
- The tax or residency situation changes before it fills.
- A named alternative fails its checklist and I have no plan for the cash.
- Check the order monthly (GTC remains until filled or cancelled; read the expiry on the IBKR confirmation).

### After a fill

Record shares sold and the average price, the realized gain (for the annual tax return), the new BRK.B weight, and where the cash went.

## Caveats

- Equity portfolio taxed with a flat 10–20% haircut (assumption; each 5 points ≈ $7.5 per share). Actual deferred taxes ($90.2B total) include non-equity items.
- TTM earnings include FX and one-off effects; GEICO weakened sharply in Q2 (pre-tax underwriting −45%).
- Equity-method holdings (e.g. Occidental, Kraft Heinz) not valued; Q3 deployment of cash is a swap of cash for assets.
- Scenario weights are subjective; model built with Claude and needs my review. Not financial advice.
