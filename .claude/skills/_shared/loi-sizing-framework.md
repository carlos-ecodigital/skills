# LOI Sizing Framework (v3.7.0)

**Source:** Cerebro Cloud Wholesale session retrospective SS2.3 (2026-04-17).
**Used by:** legal-assistant Phase 4 -- emit when operator asks "is this good?" or commercial terms fall outside the R1 10-30% absorption band.

---

## The Four Sizing Ratios

| Ratio | Calculation | Interpretation |
|---|---|---|
| **R1 -- Absorption ratio** | LOI capacity / counterparty current operating capacity | 10-30% = credibly absorbable; <5% = too small to signal commitment; >50% = aspirational to lender |
| **R2 -- Programme share** | LOI expansion / counterparty disclosed programme target | 3-10% = meaningful tranche; <1% = rounding error; >25% = unrealistic anchor |
| **R3 -- RFS alignment** | DE first RFS date vs counterparty build cadence (Fireflies-observed) | +-2 quarters = aligned; >4 quarters drift = flag |
| **R4 -- Term vs tier** | 5-yr minimum vs their public annual/monthly tiers | If customer's own longest public tier is 1yr, 5yr is a step-up requiring negotiation flag |

---

## Worked Example -- Cerebro Cloud Wholesale LOI (2026-04-17)

Inputs: 4.8 MW initial / 12.0 MW expansion / 22 MW counterparty current capacity / 200 MW programme target / H2 2026 RFS / annual public tier.

| Ratio | Value | Status |
|---|---|---|
| R1 -- Absorption | 4.8 / 22 = 22% | Credibly absorbable (10-30% band) |
| R2 -- Programme share | 12.0 / 200 = 6% | Meaningful tranche (3-10% band) |
| R3 -- RFS alignment | H2 2026 vs H2 2026 | Aligned (+-0 quarters) |
| R4 -- Term step-up | 5yr vs 1yr public tier | Step-up -- flag for MSA negotiation |

Operator output: R1 = 22% credibly absorbable, R2 = 6% meaningful tranche, R3 aligned. R4: 5-yr is a step-up from annual public tier -- standard LOI positioning but flag for MSA commercial discussion.

---

## When to Emit

- Operator asks "is this good?" or "should this be more or less?"
- Any R1 value outside the 10-30% band at Phase 4
- Any R2 value >25% (unrealistic anchor)
- Any R3 drift >4 quarters
- Any R4 step-up situation

Do not emit for every intake. Only when there is a question or a band violation.
