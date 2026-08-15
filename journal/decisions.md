# Decisions Log

<!--
Запис ТІЛЬКИ в момент дії: buy / sell / add / trim / pass.
Нові записи — зверху. Кожен запис самодостатній: читається без контексту.
Заповнюється через інтерв'ю-режим (скажи Claude: "журнал: рішення по TICKER").

Calibration-review: раз на квартал, якір — вихід листа Semper Augustus.
Проход: по кожному запису з review_date у минулому — що передбачав vs що сталось.
-->

---

## 2026-08-15 — BRK.B: Urge to reallocate — no action, conditions defined

**Ticker:** BRK.B
**Position:** 335 shares @ ~$495.29 avg cost, price $504.03, +1.77% unrealized (~91% of portfolio)
**Decision type:** Hold / trim / exit review (triggered by discomfort, slitely thesis change - Albert deploying capital agressively)
**Verdict:** **No action.** Conditions defined below.

---

## What triggered this entry

Q2 2026 earnings (released Aug 8) landed fine, but the position is barely green after ~18 months of accumulation, BRK has underperformed SPX YTD (+3% vs +13%), and a feeling emerged: *"I could deploy this money better; there's not enough margin of safety going forward."* Simultaneously: *"I don't want to sell at current prices."*

## The contradiction (recorded honestly)

These two statements cannot both be true. If forward expected returns elsewhere genuinely beat BRK.B from $504, then $504 is the right selling price. Wanting a "better exit" implies expecting BRK to outperform near-term — which contradicts the reallocation thesis. Most likely explanation: **anchoring on a flat blended return** (+1.77%) and reluctance to "waste" the 2025 holding period. Sunk time is not forward information.

## Evidence against the "no margin of safety" feeling

- Berkshire repurchased ~$4.5B of stock in Q2 (vs $235M in Q1) — management's own conservative repurchase policy implies they see the stock **below** intrinsic value at roughly current prices.
- Q2 operating earnings +16% YoY ($12.98B); MSR +24%, BHE +27%, BNSF +6%. Insurance soft (underwriting −13%, GEICO the drag) — looks cyclical, not structural.
- Cash still $365.5B after deploying ~$40B into equities in H1. Optionality intact.

## Evidence for legitimate concern (the real question)

The honest version of the unease is not price — it is **allocator change**. The 91% concentration was underwritten on Buffett's capital allocation record. Abel, two quarters in, is doing things Buffett would not: Alphabet at scale (now #1 holding, displacing Apple), Taylor Morrison ($8.5B homebuilder), OxyChem. This is a thesis-relevant change that deserves re-underwriting on its own timeline — it is a *concentration* question (trim gradually?), not a *valuation* question (exit now?).

## The named alternative test (FAILED — this decides the verdict)

Rule: no reallocation without a named alternative that clears the BRK.B benchmark today.

- KSPI — own verdict from Q1 2026 review: "watch, do not buy" pending margin of safety. Unchanged.
- PGR / ADM / Nordic insurers — no completed valuation showing MoS at current prices.
- Cash — is a timing bet, not a deployment thesis.

**No concrete alternative currently clears the benchmark. Therefore the feeling is discomfort with concentration + a flat year, not an identified mispricing.**

## Structural / tax context

- Currently PL tax resident: 19% Belka on realized gains. Trivial today (~$550 on ~$2.9K gain) — tax is NOT a reason to defer now.
- Cyprus non-dom scenario (0% CGT on securities) materially changes *when* to realize gains over a multi-year horizon. This IS a legitimate reason to be slow — realize large gains after residency change, not before, if the move happens.

## revisit_if

- [ ] `revisit_if` BRK.B P/B exceeds ~1.7x (valuation stretch)
- [ ] `revisit_if` buybacks stop for 2+ consecutive quarters while cash grows (management signals overvaluation)
- [ ] `revisit_if` a named alternative reaches my margin-of-safety price with a completed writeup (KSPI, PGR, ADM, or new)
- [ ] `revisit_if` Cyprus non-dom residency is confirmed/scheduled (tax-optimal window for any realization opens)
- [ ] `revisit_if` Abel makes a capital allocation decision I cannot rationalize under Berkshire principles (re-underwrite concentration, consider gradual trim to a defined ceiling, e.g. ≤70%)
- [ ] `revisit_if` position concentration causes decision paralysis or sleep-loss (behavioral signal outranks valuation)

## Interview-mode: answer before any future action

1. What specifically do I believe about BRK.B's next 5-year CAGR from $504, and what number does the alternative need to beat it after tax and error bars?
2. Is my concern *price* or *allocator*? (Different concerns → different actions: exit vs. gradual trim.)
3. If BRK dropped 15% tomorrow, would I buy more? (If yes — the "no margin of safety" claim is not sincere.)
4. What concentration ceiling am I actually comfortable with under Abel, independent of price?

---
*Benchmark note: BRK.B is the mandatory opportunity-cost benchmark, so this decision is self-referential — the burden of proof sits entirely on the alternative, not on BRK.*


## 2026-08-01 · PASS · KNSL (приклад)

- **decision:** pass
- **mispricing_category:** — (не знайдено; quality є, mispricing немає)
- **thesis:** чудовий underwriter в E&S ніші, але ~7.5x book — оптимізм уже в ціні
- **must_be_true_to_buy:** book multiple < 5x АБО тимчасовий скандал/страх без пошкодження underwriting-культури
- **kill_criteria:** —
- **confidence:** 80% що на цій ціні forward return < BRK.B
- **emotional_state:** спокійний, без FOMO
- **revisit_if:** ціна -35% від сьогоднішньої, або комбінований ratio > 95% два квартали поспіль (ринок панікуватиме — перевірити чи проблема тимчасова)
- **review_date:** 2027-02-01

---

## YYYY-MM-DD · BUY · TICKER (шаблон)

- **decision:** buy | sell | add | trim | pass
- **price / size:** $X · Y% портфеля
- **mispricing_category:** regulatory_fear | temporary_problem | complexity_overreaction
- **thesis:** 2-3 речення — чому ринок помиляється і чому я правий
- **must_be_true:** 2-3 перевірювані твердження
- **kill_criteria:** що змусить продати незалежно від ціни
- **expected_outcome:** прибл. річна дохідність + горизонт
- **confidence:** 0-100%
- **base_rate_check:** як часто подібні ситуації (ця категорія mispricing) відпрацьовували історично?
- **vs_BRK:** чому це краще, ніж просто додати в BRK.B? (дефолтна альтернатива)
- **emotional_state:** втома / азарт / страх / спокій — чесно
- **review_date:** дата першої перевірки тези

---
