# Site QA Gate — Rule Catalogue (Sites Stream)

**Purpose:** Pre-output lint for every Site LOI and HoT produced by the Sites engines (`site_loi_generate`, `site_hot_generate`). Catches template regressions, anti-patterns, bilingual-pair errors, and editorial slippage before the .docx reaches the user.

**Enforced by:** `site_qa_lint.py` pre-save hook. Runs against the rendered document text (extracted post-build, pre-save). Produces `{output_filename}_qa.txt` alongside the .docx. Mirrors the structure of `_shared/loi-qa-gate.md` (commercial stream) — rule IDs prefixed `R-S` (Sites) to avoid collision with the `R-` IDs used on the commercial side.

**Authority anchors:**
- `_shared/loi-qa-gate.md` — parent pattern (structure, severity levels, report format, overrides).
- `recital_b_pillars.md` — Sites-specific Recital B anti-patterns (mirrored here as `R-S23/24/25/27/28`).
- `deal_yaml_schema.md` — source of truth for parties, locations, contributions, returns used by several content rules.
- `hot/field-registry.json` — escalation rules + supporting-document expectations.
- `feedback_cover_page_title.md` — cover-title + footer policy.
- `feedback_document_formatting.md` — native-tools-only rule.
- Van Gog LOI (14-04-2026) — anchor reference for bilingual pair balance, NL diacritic preservation, signature-block conventions, validity period (§5.3 / §6.1.6).

---

## Severity levels

| Severity | Behaviour |
|---|---|
| `fail` | Blocks output. Must be auto-fixed by the engine, or require explicit user acknowledgement via `--override {rule_id}` with a recorded reason. |
| `warn` | Produces output. Visible warning in the QA report and returned to the skill for SAL acceptance. |
| `info` | Logged to QA report only. No SAL surfacing. |

**Override invocation:**

```bash
python site_qa_lint.py deal.yaml drafts/..._v1_(DRAFT).docx \
  --override R-S11,R-S28 \
  --override-reason "ISO 27001 genuinely relevant for data-centre security pitch; TBC count at 6 because three SPs pending KvK at Phase-1"
```

Override + reason are written to the QA report.

---

## Rule catalogue

| ID | Severity | Scope | Rule | Auto-fix? |
|---|---|---|---|---|
| R-S1 | fail | Cover | Cover title equals primary document type only: `"Letter of Intent"` / `"Intentieverklaring"` for LOI; `"Heads of Terms"` / `"Contractvoorwaarden"` for HoT. No concatenated types (`"LOI + NCNDA"`). | Yes — template-level title enforcement |
| R-S2 | fail | Cover | Cover uses `"Between / Tussen"` + `"And / En"` parties format. No `"Dear"` / `"To"` salutation on cover. | Yes — template-level |
| R-S3 | fail | Cover | Cover footer drops `"Confidential"` prefix (per `feedback_cover_page_title.md` — redundant with cover metadata). | Yes — strip prefix |
| R-S4 | fail | Body bilingual pairs | Every bilingual row has both an English cell and a Nederlands cell populated. No empty cells. | No — template/data bug; reject |
| R-S5 | fail | Body bilingual pairs | Length ratio of paired cells within threshold. v1.0 initial: `max(en,nl) / min(en,nl) ≤ 1.25` (25%). v1.1 calibrated target (post-calibration against `hot-grower-body-v1.docx`): `≤ 1.15` (15%). Applied row-by-row. | No — reviewer rewrites |
| R-S6 | fail | Body | No Unicode arrows anywhere: `→` (U+2192), `⇒` (U+21D2), `➜` (U+279C), `⟶` (U+27F6), `↦` (U+21A6), `⟹` (U+27F9), `⇨` (U+21E8). | No — template bug; reject |
| R-S7 | fail | Body | NL diacritic integrity preserved: any occurrence of `ë`, `ï`, `ij`, `€`, `°C` in source data renders correctly in output (no `\u00eb` escape artefacts, no mojibake). Spot-checked by comparing input YAML against rendered text. | No — encoding bug; reject |
| R-S8 | fail | Body | Native Word list/table tools only. No manual `"1. "`, `"(a) "`, `"• "` at paragraph start where Word numbering / bullets should render (per `feedback_document_formatting.md`). | No — template fix required |
| R-S9 | fail | Tables | Table columns match text margins (per `feedback_document_formatting.md`). Programmatic check: table.left_indent == body.left_indent (allow 2pt tolerance). | No — template fix |
| R-S10 | fail | LOI signature block | KvK number NOT present in LOI signature block (per Van Gog pattern — LOI sig block names + titles only; KvK is stated in Section R body). Regex: `KvK|KVK|\bChamber of Commerce\b` not present in the sig block paragraph range. | Yes — template-level filter |
| R-S11 | fail | HoT signature block | KvK number IS present in HoT signature block (binding document needs formal registry reference). Same regex as R-S10, applied to HoT; absence → fail. | Yes — template-level injection |
| R-S12 | fail | Body | Dutch governing law clause present (LOI §6.2.1: "This LOI is governed by Dutch law" / "Op deze LOI is Nederlands recht van toepassing"). | No — data/template bug |
| R-S13 | fail | Body | Amsterdam District Court (Rechtbank Amsterdam) named as exclusive jurisdiction (LOI §6.2.2 per Van Gog). Regex: `Rechtbank Amsterdam` present AND `District Court of Amsterdam` present. | No — data/template bug |
| R-S14 | fail | LOI body | Validity period clause present: either "6 months" / "zes (6) maanden" (Van Gog §5.3) OR "supersession by HoT execution" / "ondertekening van de HoT" language present. | No — template bug |
| R-S15 | fail | LOI body | Confidentiality 2-year period clause present (§6.1.6 per Van Gog). Regex: `two \(2\) years|twee \(2\) jaar`. | No — template bug |
| R-S16 | fail | Recital B / Section R | Every material numeric claim in Section R Recital B (regex: `\b\d+[\d,.]*\s*(ha\|MVA\|MW\|MWh\|m²\|m2\|customers\|connections\|years\|%)\b`) MUST be backed by (a) a tier-1 source URL in `site_partners[].source_map`, (b) a parsed-document reference on `deal.yaml.documents[]`, or (c) a `[TBC]` marker in the Recital text. Mirrors commercial R-23. | No — hard gate; resolve by adding source_map URLs, parsed-doc refs, or `[TBC]`s |
| R-S17 | fail | Recital B | No inline bracket citations in Recital B prose (e.g., `[kvk.nl]`, `[website.com]`). Source attribution lives in `source_map` only. Mirrors commercial R-24. | No — rewrite required |
| R-S18 | fail | Recital B | No vanity-financial patterns in Recital B: valuation-of / raised-$X-at-$Y / generic "Series X" / turnover ranges. Mirrors commercial R-25. | No — rewrite required |
| R-S19 | fail | Signature blocks | No `[TBC]` rendered literally in sig-block Name / Title. Must route through `_render_placeholder` so the line becomes a fillable blank. Mirrors commercial R-27. | Yes — template helper replaces bare `[TBC]` with blank underline |
| R-S20 | warn | Recital B | Per-SP word count outside 80–200 (Sites target: 120–180). Mirrors commercial R-12. | No — reviewer rewrite |
| R-S21 | warn | Recital B | More than 1 parenthetical per sentence. Mirrors commercial R-13. | No — reviewer rewrite |
| R-S22 | warn | Body (Sites-wide) | Salesy adjectives present: `\b(leading\|innovative\|cutting-edge\|world-class\|best-in-class\|state-of-the-art\|purpose-built)\b` (case-insensitive). Mirrors commercial R-14 + R-21. | No — surface for SAL review |
| R-S23 | warn | Body | Meta-commentary patterns — sentences that explain the LOI's purpose rather than asserting operational facts. Regex covers commercial R-22 patterns adapted for Sites: `is intended to evidence`, `while non-binding in its commercial terms`, `to support the Partner's financing`, `The Parties acknowledge that the Partner intends`. | No — reviewer rewrites in operative register |
| R-S24 | warn | Body | `positioning (its\|itself) as` pattern. Mirrors commercial R-15. | No — surface for SAL review |
| R-S25 | warn | Whole document | `[TBC]` count exceeds 5 body-wide — intake likely incomplete; consider completing Phase-2/3 gaps before external delivery. Mirrors commercial R-28. | No — surface for SAL review |
| R-S26 | warn | Body | Role labels in Section R match role-derivation logic in `deal_yaml_schema.md § Role-label derivation`. Check: every SP with a `grid_*` contribution is labelled "Grid Contributor / Netbijdrager"; every SP with `land` or `property` contribution is labelled "Landowner / Grondeigenaar"; every SP with `energy_heat` return is labelled "Heat Offtaker / Warmteafnemer". Mismatch → warn (may be intentional per SAL override). | No — surface for SAL review |
| R-S27 | warn | Section L | Every row in Section L has at least `parcel_id`, `address`, `postcode`, `dso`. "TBD" / "n.t.b." / "N/A" / "n.v.t." are acceptable placeholders but should be minimised at HoT stage. Row with more than 3 placeholders → warn. | No — SAL completes intake |
| R-S28 | warn | Body | Any clause heading contains `"(NON-BINDING)"` — style regression (per Van Gog pattern, the non-binding signal lives in §5.1 only, not in clause headings). Mirrors commercial R-19. | No — template fix |
| R-S29 | info | YAML (pre-run) | `deal.yaml.deal_yaml_schema_version` present and matches expected major version (`1.x`). | — |
| R-S30 | info | YAML | No `gate_overrides` applied (clean gate run). | — |
| R-S31 | info | Generation | Engine runtime metadata recorded (start, end, engine version, parser versions used). | — |
| R-S32 | fail | Body | Section R (parties table) is rendered with role labels in bilingual format. Check: for every `site_partners[]` entry, the rendered Section R row shows both the EN and NL role label on a single row (comma-separated where multi-labeled: `"Grid Contributor, Landowner / Netbijdrager, Grondeigenaar"`). | No — template bug |
| R-S33 | fail | LOI body §3.5 | When any `contributions[].asset == "land"`, the body §3.5 ("Land / Grond") is rendered; when no land contribution exists, §3.5 is omitted. Registry-driven conditional. | Yes — conditional renderer |
| R-S34 | fail | LOI body §3.2 | When `addons.bess_co_development: true`, the body §3.2 ("BESS Co-Development / BESS Co-Ontwikkeling") is rendered with the 3-paragraph pattern from Van Gog; when false, §3.2 is omitted. | Yes — conditional renderer |

---

## Report format

File: `{output_filename}_qa.txt`. Example:

```
Site LOI QA Report
File: drafts/20260419_DE_LOI_Site_van-gog-grubbenvorst_v1_(DRAFT).docx
Generated: 2026-04-19T14:32:17+02:00
Schema version: 1.0
Overrides: none

Findings:
  [INFO]  R-S29  YAML       deal_yaml_schema_version=1.0
  [INFO]  R-S30  YAML       No gate overrides applied
  [INFO]  R-S31  ENGINE     Runtime 4.2s; parsers kvk@1.0, ato@1.0
  [WARN]  R-S20  Recital B  Van Gog Grubbenvorst B.V. — word count 206 (above 180)
  [WARN]  R-S25  Doc        [TBC] count 7 (above 5)

Status: PASS_WITH_WARN (warnings: 2, failures: 0)
```

On `fail`:

```
Status: FAIL
  [FAIL] R-S5   Body        Bilingual pair ratio 1.38 in §3.3 para 2 (exceeds 1.25)
                            EN: 512 chars; NL: 370 chars. Rewrite NL paragraph.
  [FAIL] R-S10  LOI sig     KvK detected in LOI signature block para 2: "KvK 12345678"
                            Auto-fix applied: removed KvK clause from LOI sig block
  [FAIL] R-S16  Recital B   Numeric claim "25.5 MVA" unsourced; no source_map entry
                            Resolve by: adding URL to site_partners[0].source_map.pillar_2,
                            or marking as [TBC], or providing parsed ato_document reference.

Build blocked. Fix inputs or run with --override {id} --override-reason "..."
```

---

## Generator integration

Pseudocode, embedded at the tail of `SiteLOI.build()` and `SiteHoT.build()`:

```python
def build(self) -> Document:
    # ... existing sections ...
    self.signature_block()
    self.section_r()
    self.section_l()
    self.footer()
    report = site_qa_lint(
        doc=self.doc,
        deal=self.deal,
        doc_type="loi" | "hot",
        overrides=self.overrides,
    )
    if report.fails and not report.all_overridden:
        raise SiteQAFailure(report)
    report.write_to(self.qa_report_path)
    return self.doc
```

`site_qa_lint` extracts paragraph + table text from the built Document, runs each rule's regex / structural check, records findings, applies auto-fixes where the rule supports it (re-mutates the Document in place), and returns a `SiteQAReport` object.

---

## Rule calibration policy

- **R-S5 ratio** starts at 1.25 (25% tolerance) at v1.0. After 10 generated deals, reviewer measures actual empirical ratios across passed outputs and proposes a tightened threshold (target 1.15 / 15%) for v1.1. Tightening is gradual; never loosened.
- **R-S25 TBC threshold** starts at 5 body-wide. If the typical mature HoT has 3–4 TBCs (signatory details pending, specific parcel boundaries, fresh ATO validity), threshold is stable. Revisit after 10 deals.
- **R-S16 regex** mirrors commercial R-23 with Sites-specific units (ha, MVA, MW, MWh, m²). Regex extends if a new unit appears in drafts (e.g., `GWh` for district-heating network scale).

---

## Adding rules

New rule → add row to the table above + a check function in `site_qa_lint.py`. Rules are evaluated in declaration order. Auto-fixes run before severity evaluation, so a rule with an auto-fix typically downgrades itself to `info` after the fix applies.

**Naming:** `R-S{next-free-integer}`. Do not renumber existing rules — QA reports cite by ID and may be attached to HubSpot / ClickUp audit records.

---

## Rule review cadence

After every 10 generated Site LOIs or HoTs (whichever hits 10 first), reviewer (skill owner) should:

1. Read the latest 10 QA reports end-to-end.
2. Identify any consistently-warned pattern that could be upgraded to `fail` with auto-fix.
3. Identify any `fail` that is frequently overridden — either the rule is wrong or the auto-fix logic needs work.
4. Update this file + generator `site_qa_lint()` + CHANGELOG.

Do not add rules speculatively. Every rule should correspond to an observed anti-pattern in produced output.

---

## Relationship to `_shared/loi-qa-gate.md`

Commercial LOIs (EU / DS / WS / SS / EP types) use `loi-qa-gate.md` with rule IDs `R-1` … `R-28`. Site LOIs + HoTs use this file with rule IDs `R-S1` … `R-S34`. The two rulesets share:

- Same severity levels.
- Same report format.
- Same override mechanism.
- Parallel fabrication gate (commercial R-23 ↔ Sites R-S16).
- Parallel Recital B anti-patterns (commercial R-24/R-25/R-27/R-28 ↔ Sites R-S17/R-S18/R-S19/R-S25).

They differ on:

- Sites rules for bilingual pair balance (R-S4, R-S5) — not applicable to commercial (commercial LOIs are monolingual EN).
- Sites rules for NL diacritics (R-S7) — commercial has no NL content.
- Sites rules for signature-block KvK presence (R-S10 LOI-no, R-S11 HoT-yes) — commercial LOIs use different signature conventions.
- Sites rules for conditional body sections (R-S33 land, R-S34 BESS) — these are Sites-specific conditional renderers.
- Sites rules for Section R / Section L structural contracts (R-S26, R-S27, R-S32) — unique to the Site LOI schedule pattern.

No shared rules are duplicated across files — an LOI for a commercial counterparty goes through `loi-qa-gate.md`, a Site LOI/HoT goes through this file. The engine dispatch picks the right gate based on `deal.yaml.deal_type` / doc-class.
