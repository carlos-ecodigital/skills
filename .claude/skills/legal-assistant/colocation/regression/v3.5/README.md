# v3.5 Regression Intake YAMLs

Synthetic-but-realistic intake YAMLs for regression-regenerating real counterparty LOIs against the v3.5 engine. These are **not** signed instruments — they're fixtures for validating that the v3.5 engine produces a sendable .docx on the first pass for known-hard cases.

## Purpose

v3.5.1 + v3.5.2 + v3.5.3 closed 20+ field-surfaced gaps. Before the next real LOI runs, these fixtures let us confirm that:

1. The generator produces expected rendered output for each type (EU / DS / WS / SS / EP)
2. New rules (R-24, R-25, R-27, R-28, R-23 pillar-specific) fire correctly on realistic content
3. The Parties Preamble + Signal-Test-conforming Recital B + brand-rename + footer + sig block all land consistently
4. Schedule 1 technical parameters (GPU platform, rack density, cooling) render from intake YAML

## Files

| File | Type | Counterparty | v3.4 correction context |
|---|---|---|---|
| `polarise_wholesale_intake.yaml` | Wholesale | Polarise GmbH | Jonathan's actual LOI; `schedule_1.technical.gpu_platform: "NVIDIA GB200 NVL72"` is the regression smoke for v3.5.1 Scope N-subset; Recital B applies Signal Test with SWI Stoneweg Icona + Macquarie as named endorsers (not vanity-financial) |

## Regenerating

```bash
cd /path/to/skills/.claude/skills/legal-assistant/colocation
python3 generate_loi.py regression/v3.5/polarise_wholesale_intake.yaml
```

Expected: QA PASS, 0 failures. Inspect rendered .docx to confirm the Parties Preamble, Recital B signal quality, Schedule 1 GPU platform, brand rename, sig block, footer are all correct.

## Not included

- Cudo Compute (Wholesale) — deferred; tier-1 source verification required before fixture
- Sovereign AI Grid / Man of Solutions B.V. (Distributor Mode B) — deferred; KVK lookup + v3.4 corrected language require session time
- InfraPartners LLC (Strategic Supplier) — deferred; tier-1 verification of Nscale / Caddis partnerships required

These three will be added in subsequent v3.5.4 commits or v3.5.5 as a dedicated regression-completion scope.

## Non-goals

- These fixtures are **not** templates for generating actual signing-ready LOIs (use `examples/intake_example_*.yaml` as templates)
- These fixtures are **not** substitutes for `legal-counsel` Phase 7.5 review on real LOIs
