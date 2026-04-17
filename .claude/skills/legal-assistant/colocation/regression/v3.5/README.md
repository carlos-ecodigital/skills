# v3.5 Regression Intake YAMLs

Synthetic-but-realistic intake YAMLs for regression-regenerating real counterparty LOIs against the v3.5 engine. These are **not** signed instruments — they're fixtures for validating that the v3.5 engine produces a sendable .docx on the first pass for known-hard cases.

## Purpose

v3.5.1 + v3.5.2 + v3.5.3 closed 20+ field-surfaced gaps. Before the next real LOI runs, these fixtures let us confirm that:

1. The generator produces expected rendered output for each type (EU / DS / WS / SS / EP)
2. New rules (R-24, R-25, R-27, R-28, R-23 pillar-specific) fire correctly on realistic content
3. The Parties Preamble + Signal-Test-conforming Recital B + brand-rename + footer + sig block all land consistently
4. Schedule 1 technical parameters (GPU platform, rack density, cooling) render from intake YAML

## Files

| File | Type | Counterparty | Tier-1 verification status |
|---|---|---|---|
| `polarise_wholesale_intake.yaml` | Wholesale | Polarise GmbH | Agent-reported facts (polarise.com JS-gated at research time); source_map pillars all `[TBC]` pending direct WebFetch-verified re-source in v3.5.5 |
| `cudo_wholesale_intake.yaml` | Wholesale | Cudo Compute Limited | Tier-1 verified via `cudocompute.com/about` (HQ, NVIDIA Preferred Partner status, NVIDIA-certified engineers, Supermicro/Dell/Lenovo/HPE/NetApp/Red Hat partners, Conapto deployment) |
| `sag_distributor_intake.yaml` | Distributor Mode B | Man of Solutions B.V. (Sovereign AI Grid) | Tier-1 verified via `sovereignaigrid.nl` (Amstelveen HQ, consortium coordination role, EuroHPC JU, named member institutions, Nick Aldewereld Lead Coordinator). **v3.4-corrected language applied** — NO "centrale knooppunt" (v3.3 fabrication) |

## Regenerating

```bash
cd /path/to/skills/.claude/skills/legal-assistant/colocation
python3 generate_loi.py regression/v3.5/polarise_wholesale_intake.yaml
python3 generate_loi.py regression/v3.5/cudo_wholesale_intake.yaml
python3 generate_loi.py regression/v3.5/sag_distributor_intake.yaml
```

Expected for each: QA PASS, 0 failures. Inspect rendered .docx to confirm the Parties Preamble, Recital B signal quality, Schedule 1 GPU platform, brand rename, sig block, footer are all correct.

## Not included

- **InfraPartners LLC (Strategic Supplier)** — deferred; tier-1 verification of Nscale / Caddis partnerships required before fixture. Will be added in v3.5.5.
- **Direct re-fetch of Polarise tier-1 sources** — the polarise.com site was JS-gated at fixture-creation time; source_map pillars currently `[TBC]` pending retry (v3.5.5).

## Non-goals

- These fixtures are **not** templates for generating actual signing-ready LOIs (use `examples/intake_example_*.yaml` as templates)
- These fixtures are **not** substitutes for `legal-counsel` Phase 7.5 review on real LOIs
