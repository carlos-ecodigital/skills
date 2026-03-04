# Investment Case Intake Questionnaire -- MODULARIZED

This file has been modularized into 10 reusable modules + 1 router.

**New location:** `_shared/intake-modules/`

## Module Index

| Module | File | Contents | Questions |
|--------|------|----------|-----------|
| Router | `intake-router.md` | Track selection, module loading matrix, legends, readiness score | 4 |
| M0 | `m0-document-ingestion.md` | Phase 0 triage, document checklist | 8 |
| M1 | `m1-entity-tax.md` | S1: Corporate Structure + S2: Tax Structuring | 37 |
| M2 | `m2-founder-team.md` | S3: Founder & Team | 24 |
| M3 | `m3-market-solution.md` | S4: Problem & Market + S5: Solution | 46 |
| M4 | `m4-bess-technical.md` | S6: BESS Technical Specifications | 45 |
| M5 | `m5-dc-ai-technical.md` | S7: DC/AI Infrastructure Technical | 50 |
| M6 | `m6-sites-assets.md` | S8: Sites & Assets (per site) | 22 |
| M7 | `m7-revenue-debt.md` | S9: Revenue Model + S10: Debt Structure | 55 |
| M8 | `m8-equity-capital.md` | S11: Equity Structure + S13: Capital Structure | 36 |
| M9 | `m9-synthesis.md` | S12-S20 + 8 cross-cutting validation dimensions | ~150 |

**Total:** ~500 questions across all modules.

## Why Modularized

- Original monolith was 3,583 lines (~45K tokens) -- exceeded 25K token context ceiling
- Modules are now track-aware: Seed / Project Finance / Both
- Each module stays under 12K tokens
- Progressive loading: one module at a time
- Fully generic: works for any infrastructure/energy company (no longer DE-specific)

## How to Use

1. Load `intake-router.md` first -- it determines the track and module loading order
2. See `seed-fundraising/SKILL.md` Mode C for orchestration instructions
3. See `project-financing/SKILL.md` Integration section for PF data consumption
