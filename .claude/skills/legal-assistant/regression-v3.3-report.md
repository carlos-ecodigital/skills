# v3.3 Regression — 3 Reviewed LOIs Regenerated

**Date:** 2026-04-16
**Scope:** Three of the five LOIs reviewed in the 2026-04 post-mortem, regenerated against the v3.3 engine.

The five originally reviewed LOIs were Cerebro Cloud, Aldewereld, SAG Man-of-Solutions, InfraPartners, and Cudo Compute. Cerebro and Aldewereld share issue classes with Cudo and SAG respectively; regenerating the other three covers all issue classes that drove v3.2 + v3.3.

## Summary

| File | Original anti-pattern hits | v3.3 regen hits | Status |
|---|---|---|---|
| Cudo Compute (Wholesale) | 9 | 0 | ✅ CLEAN |
| SAG Man-of-Solutions (Distributor Mode B) | 7 | 0 | ✅ CLEAN |
| InfraPartners (Strategic Supplier) | 4 | 0 | ✅ CLEAN |

Every user-flagged anti-pattern from the 2026-04 post-mortem is eliminated in the regenerated versions.

## Intake artifacts

- `/tmp/intake_regen_cudo.yaml` — WS intake, Recital B reworked per 5-pillar framework (ISO 27001 + OEM list trimmed; 20.4 MW IT only; no DEC Block count).
- `/tmp/intake_regen_sag.yaml` — DS Mode B intake, Recital B reworked per consortium guidance (coordinating entity focus; jargon glossed; demand-side credentials only).
- `colocation/examples/intake_example_strategic_supplier.yaml` — SS intake seeded from InfraPartners, regenerated through the new SS clause builders.

## Regeneration output

- `/tmp/regen_cudo.docx` (+ `_qa.txt`) — QA PASS.
- `/tmp/regen_sag.docx` (+ `_qa.txt`) — QA PASS.
- `/tmp/regen_infrapartners.docx` (+ `_qa.txt`) — QA PASS.

## Per-file diff

### Cudo Compute (Wholesale)

**Original anti-patterns** (9):

1. "14 identified sites" (Recital A)
2. "12 months of commercial commitment" (Recital A)
3. "DEC Block" in Cl. 3.1 (17 DEC Blocks (20.4 MW IT))
4. "minimum commitment term of 5 years" (Cl. 3.6)
5. "We are confident that" (closing paragraph)
6. Unicode arrow `→` (Cl. 4.2 Revenue Chain)
7. "Revenue Chain" heading (Cl. 4.2)
8. "(NON-BINDING)" suffix in Schedule 1 title
9. ISO 27001 reference in Recital B (padding)

**v3.3 fixes:**

1. → Recital A now library-sourced (`default` variant, no site counts, no delivery deadlines)
2. → (same as 1)
3. → Cl. 3.1 now "20.4 MW IT to be delivered across one or more Designated Sites"
4. → Cl. 3.6 now "approximately 5 (five) years, indicative only and subject to confirmation in the MSA"
5. → Closing hardcoded single sentence (OPEN-1 honored)
6. → Cl. 4.2 now "Contractual Sequence" with numbered list (a)-(d), no arrows
7. → (same as 6)
8. → Schedule 1 title "Schedule 1 — Capacity and Technical Requirements"; italic prefatory note carries non-binding signal
9. → Recital B trimmed per 5-pillar framework (ISO 27001 chain + OEM list removed; kept NVIDIA Preferred Partner + 300,000+ GPUs + 750 MW pipeline)

**Size:** original 3,694 words → regen 3,669 words (roughly flat — Recital B trimming balanced by Cl. 4.2 numbered-list expansion).

### SAG Man-of-Solutions (Distributor Mode B)

**Original anti-patterns** (7):

1. "14 identified sites" (Recital A)
2. "12 months of commercial commitment" (Recital A)
3. "DEC Block" in Cl. 1 definitions
4. "We are confident that" (closing)
5. Duplicated "We look forward to working with you" (closing)
6. Untranslated "centrale knooppunt" (Recital B)
7. Untranslated "Article 12b architecture" (Recital B)

**v3.3 fixes:**

1–2. → Recital A library-sourced `sovereignty` variant (EU-mission consortium).
3. → DEC Block removed from customer-facing definitions; SS/EP never use it.
4. → Closing hardcoded (OPEN-1).
5. → (same as 4 — eliminated by eliminating bespoke closings).
6. → "centrale knooppunt" replaced with "coordinating entity" (English).
7. → "Article 12b architecture" replaced with "EuroHPC hosting framework (Article 12b of Regulation (EU) 2021/1173)" — glossed with formal citation.

Additionally, Recital B reworked per consortium guidance:
- Describes coordinating entity (Man of Solutions B.V.), not every member.
- Demand-side credentials only (removed supply-side technical infrastructure credentials that belonged in a different LOI type).
- Pillar 3 (Track record) anchored to coordinating entity's MD institutional relationships + datacentre capacity origination track record.
- Pillar 4 (Strategic fit) stated explicitly as one sentence.

**Size:** original 4,259 words → regen 3,683 words (−576 words, −14%). Reduction comes from eliminating jargon + removing irrelevant supply-side credentials + tighter Cl. 3 (v3.3 inherits v3.2 cleanups).

### InfraPartners (Strategic Supplier)

**Original anti-patterns** (4):

1. "14 identified sites" (Recital A)
2. "12 months of commercial commitment" (Recital A)
3. "DEC Block" in Cl. 1 definitions (inherited from Distributor chassis misuse)
4. Generic closing with "We look forward to working with you" repetition

**v3.3 fixes:**

1–2. → Recital A library-sourced `default` variant + SS-specific tail ("The Provider seeks qualified supply and engineering partners to accelerate the delivery of its DEC platform...").
3. → SS engine now has its own definitions (no DEC Block; Framework Agreement instead of MSA; supplier-scoped AC).
4. → Closing hardcoded; dedupe no longer needed.

Additionally:
- Now uses the dedicated SS chassis (v3.3) rather than a repurposed Distributor chassis (v3.1/v3.2 partial).
- Cl. 3 purpose-driven: this intake specifies `[engineering_integration, pipeline_visibility]`, firing 3.1 (always), 3.7 (design integration + IP), 3.8 (preferred supplier / ROFR 20-BD window), 4.1 (project introduction), 4.2 (contractual sequence), 4.3 (joint-dev governance), 4.4 (CoC), 4.6 (roadmap).
- Schedule 1 is "Scope and Capability Matrix" — shows capability category, core capability, declared strategic purposes, joint IP allocation.
- Cl. 7 NC is the light supply-side variant, scoped to Provider's supply-side relationships (not Partner's end-user customers).
- Cl. 7.6 and Cl. 8 reference "Framework Agreement" as downstream binding document (not "MSA").

**Size:** original 3,930 words → regen 3,509 words (−421 words, −11%). Reduction comes from eliminating borrowed DS/WS clauses that weren't relevant to a supplier relationship (e.g., customer credit assessment, site allocation).

## QA reports

All three regenerations produced `PASS` QA status with zero failures. See `/tmp/regen_*_qa.txt` for full reports.

## Conclusion

v3.3 eliminates every user-flagged anti-pattern from the 2026-04 LOI post-mortem across three reviewed LOIs spanning three LOI types (WS, DS Mode B, SS). The 5-pillar Recital B methodology tightens counterparty descriptions (−14% on SAG, −11% on InfraPartners). The Strategic Supplier engine produces InfraPartners-class supplier LOIs with supply-tuned commercial logic that the repurposed DS chassis could not.
