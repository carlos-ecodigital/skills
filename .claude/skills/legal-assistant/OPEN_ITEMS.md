# legal-assistant — Open Items

Cross-cutting TODOs for the `legal-assistant` skill that don't belong in any single template handover.

---

## OPEN-1 — Bespoke closing line constraints (CLOSED by removal)

**Resolution (2026-04-16):** The bespoke_closing feature was removed entirely rather than constrained.

Constraining the feature required a validator, drafter examples, a SKILL.md policy section, a YAML field in every intake, and drafter-comment blocks in two templates — all to police a one-sentence optional add-on whose only observed uses (in the Distributor and Wholesale template examples themselves) violated the constraint. Every legitimate operational content that belonged near the signature ("John will follow up re: workshop", scheduling hooks) belongs in the body, not crammed into the closing line. Killing the feature was cleaner than policing it.

**What was removed:**
- `generate_loi.py`: deleted bespoke concatenation in `signature()`; no validator added.
- `SKILL.md`: deleted §"Bespoke Closing Line — Constraints".
- `colocation/templates/DE-LOI-Distributor-v3.0_TEMPLATE.md` line 422: drafter comment row deleted.
- `colocation/templates/DE-LOI-Wholesale-v3.0_TEMPLATE.md` line 391: drafter comment row deleted.
- `colocation/examples/*.yaml` (all 4 intakes): `bespoke_closing` field removed from `choices:`.

**What remained unchanged:** the standard closing `"We look forward to working with you."` is hardcoded in `generate_loi.py::signature()` and kept — letters benefit from the conventional signpost; absence reads as abrupt. MIA has no closing line (codified in `mia/MIA_ASSEMBLY_GUIDE.md §1`).

---

## Revision log

- **2026-04-13** — Created during DE-MIA handover restructure (v2). Original path `loi-generator/OPEN_ITEMS.md`.
- **2026-04-13** — Relocated to `legal-assistant/OPEN_ITEMS.md` following the `loi-generator` → `legal-assistant` skill rename. Heading updated.
- **2026-04-14** — File recreated after discovering it was missing at the legal-assistant path (lost during the skill rename/migration). Content reconstructed from the DE-MIA handover's §Cross-skill TODOs reference.
- **2026-04-16** — OPEN-1 closed by feature removal. Bespoke_closing mechanism deleted across generator, templates, SKILL.md, and all intake YAMLs. See resolution block above.
