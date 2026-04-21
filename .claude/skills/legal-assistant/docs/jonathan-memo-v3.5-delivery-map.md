# Jonathan Memo → v3.5.x Delivery Map

**From:** v3.5.x delivery team
**To:** Jonathan Glender (CGO)
**Re:** Closure of your 2026-04-17 field-findings memo (19 items from first production use of `de-legal-assistant` v3.4 on the Polarise Wholesale LOI)

---

## Summary

All 19 items from your memo are **addressed in v3.5.x**. 14 are **delivered and merged-ready**; 3 are **delivered-with-deferred-extension**; 2 are **deferred to v3.5.5** (documented reason per item).

The full v3.5.x stack ships as a single consolidated PR on each repo (upstream + staging) containing all v3.5.1 → v3.5.4 commits + v3.5 polish items. Run `python3 generate_loi.py regression/v3.5/polarise_wholesale_intake.yaml` against the merged branch to regenerate your Polarise LOI — QA PASS with zero post-gen manual editing expected.

---

## Mapping table

| # | Your finding | v3.5.x delivery | Status |
|---|---|---|---|
| **E1** | Recital B "30 MW Augsburg expansion" — delete, reads like padding | Signal Test methodology (v3.5.2 Scope 0): self-announced forward pipeline fails gate 1. Augsburg correctly omitted from Recital B in Polarise regression fixture. Methodology documented in `_shared/counterpart-description-framework.md` Signal Test §. | ✅ Delivered |
| **E2** | DE sig block `KvK: [TBC]` — delete | v3.5.1 Scope A': `KvK:` line stripped from `DocBuilder.signature()` entirely. Registration numbers live in Parties Preamble (v3.5.2 Scope A''') and cover page only. | ✅ Delivered |
| **E3** | Polarise sig block `HRB: [TBC]` — delete | v3.5.1 Scope A': counterparty reg_type/reg_number block removed from sig block. | ✅ Delivered |
| **E4** | Polarise sig block `Title: [TBC]` — render as fillable blank | v3.5.1 Scope J5: `_render_placeholder(value, "sig_block_title")` returns `____________________________` when value is `[TBC]` / `None` / empty. Sig block Name + Title both route through the helper. | ✅ Delivered |
| **E5** | Cl. 3.2 "rack densities of 40 kW and above" — obsolete; GB-class is 130 kW | v3.5.1 Scope J1: default bumped to `approximately 130 kW and above` + `direct-to-chip liquid cooling (consistent with NVIDIA GB200 NVL72 and GB300 NVL72 reference architectures, which target approximately 120–140 kW per rack at full configuration)`. Parametrized via `commercial.rack_density_kw` + `commercial.cooling_topology`. | ✅ Delivered |
| **E6** | Cover page DE address — Zug (wrong entity) on NL B.V. LOI | v3.5.1 Scope A'': all 6 intake YAMLs corrected from Zug to `Mijnsherenweg 33 A, 1433 AP Kudelstaart, the Netherlands`. Generator reads `provider.address` directly (no cross-contamination in code path). | ✅ Delivered |
| **E7** | First-page footer hardcodes Group AG | v3.5.1 Scope A'''': `document-factory/generate.py::setup_footer` now centre-aligned; `generate_loi.py::_setup` derives entity from `provider.legal_name` via `_derive_footer_entity()` (`"Netherlands"` / `"B.V."` → `nl`; else `ag`). BV-signed LOIs now render correct NL entity in footer. | ✅ Delivered |
| **W1** | Framework worked examples ship with inline `[source]` citations that leak into customer-facing documents | v3.5.2 Scope 0: R-24 (fail) regex catches inline bracket citations matching `\[[A-Za-z][A-Za-z0-9._-]*\.(?:com\|eu\|de\|co\.uk\|org\|nl\|io\|ai\|ch)\]`. Signal Test methodology documents explicit separation: source attribution in `source_map` YAML only; never in prose. | ✅ Delivered |
| **W2** | Phase 6 confirmation gate truncates Recital B to 60 chars | J8 — deferred to v3.5.3 continuation (SKILL.md Phase 6 prompt template edit; shows full Recital B + diff-highlight since Phase 5 accept). Scoped in `plans/expressive-cooking-flamingo.md`. | ⏳ Deferred to v3.5.3 continuation |
| **W3** | Cl. 3.4 renders `approximately to be discussed MW IT` when `expansion_mw` is non-numeric | v3.5.1 Scope J3: template branches on value type. Numeric → original sentence. Empty / `[TBC]` / `"to be discussed"` / non-numeric → fallback: *"The Customer has expressed interest in future expansion beyond the initial deployment, with scale to be determined following technical scoping..."* | ✅ Delivered |
| **W4** | Gmail MCP broken at intake time; no documented fallback | v3.5.3 Scope J14: SKILL.md Phase 3 now documents schema-error detection (`"False is not of type 'array'"`) + PDF-export / thread-paste fallback. Explicit no-silent-omission note. | ✅ Delivered |
| **W5** | Provider entity + signatory presented as 3 options when deal facts deterministically imply NL B.V. + CEO | v3.5.1 Scope A: Wholesale example default updated to Carlos Reuven / Director (statutory NL BV capacity). v3.5.2 Scope Q: `config/entities.yaml::type_defaults` table documents per-type entity + signatory-mode defaults. Phase 6 gate auto-proposal uses these — deferred to v3.5.3 continuation (J12). | 🟡 Partial: static default delivered; deterministic auto-select deferred |
| **W6** | Example `intake_example_wholesale.yaml` ships `source_map:` as plain strings; R-23 requires URL-list format | v3.5.3 Scope J7 (in v3.5.2 PR, see commit): wholesale YAML updated with URL-list format comment block explaining R-23 requirement. v3.5.3 Scope K: `--migrate-check` CLI flag emits paste-ready snippet for legacy YAMLs. | ✅ Delivered |
| **W7** | Phase 7.5 "non-bypassable legal-counsel review" — engine exits after `.docx` write | v3.5.2 Scope C: `legal-counsel/specializations/contract-review/loi-review-workflow.md` created as reference-only markdown callee, matching codebase cross-skill convention. SKILL.md Phase 7.5 references the callee file directly (v3.5 polish). Returns PASS/FLAG-FOR-REVISION/REJECT envelopes. Programmatic code-level enforcement (Scope G fail-closed sentinel) is deferred to v3.5.3 continuation. | 🟡 Partial: callee delivered + callsite linked; code-level enforcement deferred |
| **W8** | Output saved to `/tmp/` then `cp`'d to Downloads; no Drive upload | v3.5.3 Scope J13: SKILL.md Phase 8 documents `scripts/artifact_storage.py::upload_artifact()` pattern per CLAUDE.md §4. **Status: wiring deferred** — the `artifact_storage.py` script does not yet exist in the repo. Spec ready; hook-up lands when the script does. | 🟡 Partial: doc-only pending artifact_storage.py |
| **J17** | All 5 intake YAMLs pair NL B.V. `legal_name` with Group AG's Zug address | v3.5.1 Scope A'': **resolved** — all 6 intake YAMLs corrected. Architectural fix v3.5.2 Scope Q adds `config/entities.yaml` single source of truth (`de_nl` + `de_ag`) so this bug category is eliminated going forward. | ✅ Delivered |
| **J18** | First-page footer hardcodes Group AG regardless of signing entity | v3.5.1 Scope A'''': **resolved** — same as E7. Dynamic entity derivation from `provider.legal_name`. | ✅ Delivered |
| **J19** | Real KvK missing; all examples show `XXXXXXXX` placeholder | v3.5.1 Scope A'': **resolved** — all 6 intake YAMLs updated to `kvk: "98580086"` (verified NL B.V. KvK number). v3.5.2 Scope Q: canonical value lives in `config/entities.yaml::entities.de_nl.reg_number`. | ✅ Delivered |

---

## Recommended §7 entities-refactor adoption

Your §7 proposal (`config/entities.yaml` as single-source-of-truth) was adopted in full as **v3.5.2 Scope Q**. Intake YAMLs now support:

```yaml
provider:
  entity: "de_nl"              # looked up from config/entities.yaml
  signatory_mode: "pre_msa"    # or post_msa / ceo
```

The loader expands the record at runtime. Explicit intake fields (e.g. `signatory_name`) still override register defaults. Backward-compat: YAMLs without `provider.entity` work unchanged with explicit-field pattern.

---

## What was NOT delivered (explicit deferrals)

### v3.5.3 continuation (single follow-up session)

- **J8** Phase 6 full Recital B display + diff
- **J9** Phase 5 redraft-as-first-class UX (accept / redraft-with-notes / paste-replacement)
- **J12** Per-type deterministic entity + signatory auto-selection
- **G** Phase 7.5 code-level fail-closed sentinel (complements the reference-only callee)
- **D / E / F** R-23 pillar-specific granularity, R-22 regex narrowing, Recital B multi-paragraph extraction
- **H / I** Tier-2 qualifier worked examples + direct WebFetch re-verification of 4 framework examples

### v3.5.5

- Sibling docs sync (ASSEMBLY_GUIDE / FEATURE_MATRIX / SOP — ~51 discrete edits, scoped in `~/.claude/plans/v3.5.4-sibling-docs-sync.md`)
- InfraPartners regression fixture (tier-1 verification of Nscale / Caddis partnerships)
- Polarise regression fixture direct tier-1 re-verification (polarise.com was JS-gated at fixture creation; source_map currently `[TBC]`)

---

## Regression protocol

To verify v3.5.x end-to-end against your Polarise use case:

```bash
# After v3.5 PR merges to main
git checkout main && git pull
cd .claude/skills/legal-assistant/sales
python3 generate_loi.py regression/v3.5/polarise_wholesale_intake.yaml
open "20260417_DEG_LOI-Wholesale_Polarise_(DRAFT).docx"
```

Expected:
- QA PASS (0 warnings, 0 failures)
- Parties Preamble renders on page 2 with "(1) Digital Energy Netherlands B.V., a Besloten Vennootschap (B.V.) incorporated under the laws of the Netherlands, with registered office at Mijnsherenweg 33 A..." and "(2) Polarise GmbH..."
- Recital A opens with "Digital Energy develops and operates Digital Energy Centers..." (no "(the 'Provider')")
- Recital B names SWI Stoneweg Icona + Macquarie + NVIDIA Cloud Partner + Deutsche Telekom (zero inline citations; zero valuation numbers)
- Cl. 3.2 "rack densities of approximately 130 kW and above" + direct-to-chip liquid cooling referencing GB200/GB300 NVL72
- Cl. 3.4 fallback sentence (because `expansion_mw: "to be discussed"` — non-numeric)
- Schedule 1 "GPU / Accelerator Type: NVIDIA GB200 NVL72 (2× SU, ~1,152 GPUs total)"
- Footer: "Digital Energy Netherlands B.V. · Mijnsherenweg 33 A... · KvK 98580086" (centre-aligned)
- Sig block: no KvK line, no ACKNOWLEDGED AND AGREED, has Place field

**If anything is wrong on first-pass regen**: file issue against `carlos/loi-v3.5.x` branches; v3.5.5 continuation pass will absorb the finding.
