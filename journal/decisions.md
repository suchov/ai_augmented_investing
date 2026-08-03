# Decisions Log

<!--
Запис ТІЛЬКИ в момент дії: buy / sell / add / trim / pass.
Нові записи — зверху. Кожен запис самодостатній: читається без контексту.
Заповнюється через інтерв'ю-режим (скажи Claude: "журнал: рішення по TICKER").

Calibration-review: раз на квартал, якір — вихід листа Semper Augustus.
Проход: по кожному запису з review_date у минулому — що передбачав vs що сталось.
-->

---

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
