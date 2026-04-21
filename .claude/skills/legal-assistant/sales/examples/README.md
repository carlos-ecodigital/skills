# Examples Directory -- LOI Intake YAML Reference

**Purpose:** Baseline examples illustrating v3.2 intake structure for each LOI type.

> **IMPORTANT (v3.7.0, scope D):** For production intakes, start from the **newest regression fixture** in `regression/v{X.Y}/*_intake.yaml` that matches your LOI type. The regression fixtures reflect the latest production patterns (current: v3.7). Fall back to these example files only if no regression fixture matches your type.

> **NEW (v3.7.2):** `intake_example_strategic_supplier_v37_full.yaml` is the **kitchen-sink** reference demonstrating every v3.7.x field in one working fixture. 12 feature branches fire together. Copy-adapt for SS deals that need multiple extensibility features.

| LOI type | Regression fixture (preferred) | Example file (v3.2 baseline) |
|---|---|---|
| Wholesale (WS) | regression/v3.7/cerebro_wholesale_intake.yaml (dark-web + brochure)<br/>regression/v3.5/cudo_wholesale_intake.yaml | intake_example_wholesale.yaml |
| Strategic Supplier (SS) | regression/v3.7/infrapartners_strategic_supplier_v6_intake.yaml (full v3.7.x)<br/>regression/v3.7/armada_strategic_supplier_intake.yaml (joint stocking + referral)<br/>regression/v3.5/infrapartners_supplier_intake.yaml (v3.5 baseline) | intake_example_strategic_supplier.yaml<br/>**intake_example_strategic_supplier_v37_full.yaml** (v3.7.x kitchen sink) |
| Distributor Mode A (DS-A) | regression/v3.5/sag_distributor_intake.yaml | intake_example_distributor.yaml |
| Distributor Mode B (DS-B) | (use DS-A fixture as structural template) | intake_example_distributor_referral.yaml |
| End User (EU) | (no regression fixture yet; use example) | intake_example_enduser.yaml |
| Ecosystem Partnership (EP) | (no regression fixture yet; use example) | intake_example_ecosystem_partnership.yaml |

## v3.7.x feature-specific regression fixtures

Use these as reference when your deal exercises a particular v3.7.x feature branch:

- `regression/v3.7/name_homonym_collision.yaml` — Phase 4.5 signatory cross-check pattern
- `regression/v3.7/dual_role_founder.yaml` — Phase 2 dual-role detection via relationship_cluster
- `regression/v3.7/dark_web_counterparty.yaml` — Phase 3.5 dark-web detection + elevated Phase 7.5
- `regression/v3.7/brochure_sourced_recital_b.yaml` — tier-2 brochure token handling
- `regression/v3.7/prior_loi_regeneration.yaml` — `--audit-only` lineage tracking

See `FEATURE_MATRIX.md` "v3.7.x Extensibility Layer" for the full field/rule/flag/artefact map.

## What the example files illustrate

- Basic YAML structure and field ordering for each type
- Default value conventions (provider entity, signatory, protection periods)
- recital_a_variant usage (v3.4 canonical body -- all examples updated to default)
- source_map pillar format (URL list or [TBC])

## What the regression fixtures illustrate

- Real production intake patterns (tier-1 URLs, source_map with verified pillar content)
- v3.5.x field additions (rack_density_kw, gpu_platform, phasing blocks)
- Edge-case handling (prior LOI regeneration, dark-web counterparty, brochure-sourced pillars)
- Baseline for CI / regression test runner

## source_map and brochure tokens

When a source is a private artefact (brochure, deck, one-pager) rather than a public URL, use the brochure token format in source_map:

    source_map:
      pillar_3:
        - url: "internal:brochure_2026-04-17_cerebro"
          tier: 2
          qualifier: "Cerebro Cloud GTC 2026 brochure (operator-collected)"

Tier-2 brochure entries pass R-23 (URL presence not required for internal tokens) but trigger R-24 warn: "Brochure-sourced claims require tier-1 public corroboration before signing."
