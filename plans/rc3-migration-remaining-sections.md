# rc3 clause-library migration — remaining sections

Phase 3 (rc3.3) shipped the loader infra and migrated §1 Parties as proof of
concept. The sections below stay inline in `generate_site_loi.py` until each
sub-PR moves them to `sites/loi/templates/clauses/de-loi-site-v1.0.yaml`.

Each item is one sub-PR (~1 hour). No re-release required — every sub-PR
asserts byte-identical output against an rc3.1 baseline of the same Van Gog
LOI before the change is approved.

- [ ] §2 Background (1 sub-clause: 2.1, 2.2 collapsed under one heading)
- [ ] §3 Project Overview (sub-sections 3.1–3.9, with addon-gating preserved
      via the engine composing section_id lists; gate predicates
      ``_any_partner_contributes`` / ``_any_partner_returns`` /
      ``_find_bess_details`` move from inline calls to the YAML's
      ``asset_gate`` field, with the engine reading and applying them)
- [ ] §4 Pre-Feasibility + HoT (4.1–4.4)
- [ ] §5 Term (5.1, 5.2)
- [ ] §6 Binding Provisions (6.1.1–6.1.6, 6.2.1–6.2.2, 6.3, 6.4.1–6.4.6)
- [ ] §7 Execution (signature-page lead-in)

## Per-section sub-PR checklist

For each section above:

1. Translate the inline EN/NL strings into YAML rows under the existing
   `clauses:` list, preserving smart quotes, em dashes, and whitespace
   exactly.
2. Replace the inline `_clause_*()` call site in `build_document()` with
   `render_bilingual_section(doc, _CLAUSES, [...], heading_en=..., heading_nl=...)`.
3. Delete the now-unused `_clause_*()` helper function.
4. Drop the `TODO(rc3-migration)` marker above the deleted helper.
5. Run `pytest sites/_shared/ sites/loi/ legal-assistant/sales/`.
6. Diff §X output against an rc3.1 baseline byte-for-byte.

## Documentation surface

- `sites/_shared/site_clause_library.md` becomes the legal-review surface
  (footer-marked design doc that mirrors the schema). The YAML file is the
  runtime source of truth — engines never read the .md.
- `legal-assistant/CHANGELOG.md` rolls up the full §1–§7 migration as one
  Phase 4 entry; intermediate sub-PRs do not edit CHANGELOG.
