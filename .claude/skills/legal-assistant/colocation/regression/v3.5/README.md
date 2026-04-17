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
| `polarise_wholesale_intake.yaml` | Wholesale | Polarise. GmbH | **v3.5.5: tier-1 updated.** HRB 17714 Amtsgericht Paderborn verified (online-handelsregister.de). Pillars 1+2+3 now cite online-handelsregister.de + swi.com direct investor release (SWI Stoneweg Icona majority stake; Deutsche Telekom Industrial AI Cloud anchor; NVIDIA Cloud Preferred Partner). Signatory pool: Michel Boutouil or Tirat Demir (Geschäftsführer, Einzelvertretung). Pillar 5 `[TBC]` — polarise.com still JS-gated across 5 path attempts. |
| `cudo_wholesale_intake.yaml` | Wholesale | Cudo Compute Limited | Tier-1 verified via `cudocompute.com/about` (HQ, NVIDIA Preferred Partner status, NVIDIA-certified engineers, Supermicro/Dell/Lenovo/HPE/NetApp/Red Hat partners, Conapto deployment) |
| `sag_distributor_intake.yaml` | Distributor Mode B | Man of Solutions B.V. (Sovereign AI Grid) | Tier-1 verified via `sovereignaigrid.nl` (Amstelveen HQ, consortium coordination role, EuroHPC JU, named member institutions, Nick Aldewereld Lead Coordinator). **v3.4-corrected language applied** — NO "centrale knooppunt" (v3.3 fabrication) |
| `infrapartners_supplier_intake.yaml` | Strategic Supplier | InfraPartners LLC | **v3.5.5 NEW.** Tier-1 verified via nscale.com press release (60 MW Glomfjord partnership; announced 25 Mar 2025; InfraPartners role = modular prefab construction) + GlobeNewswire press release (Caddis Cloud Solutions strategic partnership; 100+ MW EMEA+NA pipeline; US+Romania manufacturing). CEO Michalis Grigoratos verified. **v3.4 correction applied** — NO "90-day RFS" claim; NO unqualified "80% off-site completion" (tier-1 unverifiable). |

## Regenerating

```bash
cd /path/to/skills/.claude/skills/legal-assistant/colocation
python3 generate_loi.py regression/v3.5/polarise_wholesale_intake.yaml
python3 generate_loi.py regression/v3.5/cudo_wholesale_intake.yaml
python3 generate_loi.py regression/v3.5/sag_distributor_intake.yaml
python3 generate_loi.py regression/v3.5/infrapartners_supplier_intake.yaml
```

Expected for each: QA PASS, 0 failures. Inspect rendered .docx to confirm the Parties Preamble, Recital B signal quality, Schedule 1 GPU platform, brand rename, sig block, footer are all correct.

## Remaining [TBC] markers

- **Polarise pillar 5** — polarise.com direct site JS-gated; awaiting future direct WebFetch.
- **InfraPartners jurisdiction / reg_type / reg_number** — the US-registered LLC structure requires Delaware/State-level lookup; not yet done.
- **Polarise signatory selection** — either Michel Boutouil or Tirat Demir (both have Einzelvertretung per Handelsregister); deal-specific choice at signing.

## Non-goals

- These fixtures are **not** templates for generating actual signing-ready LOIs (use `examples/intake_example_*.yaml` as templates)
- These fixtures are **not** substitutes for `legal-counsel` Phase 7.5 review on real LOIs
