# LOI Recital A — Canonical Library (v3.4)

Single source of truth for Recital A language across all LOI types produced by `legal-assistant`. The generator `generate_loi.py` reads `RECITAL_A_BODY` + `RECITAL_A_TAIL_BY_TYPE` dicts that mirror this file.

**Last synced to:** Master Pitch Narrative v3.2 + user polish 2026-04-17.
**Re-sync trigger:** Any MPN revision or user-authored rewrite. Check MPN § 1.3 (Identity), § 4.6 (Integration Logic), § 9.1 (Investor Thesis) against the body below.

**v3.4 change:** collapsed v3.3's 3-variant library (default / sovereignty / integration) into a **single canonical body**. User-approved wording 2026-04-17. Per-type tails now cover all 5 LOI types (v3.3 only had tails for DS/SS/EP; EU/WS were empty strings).

---

## Why this exists

Prior LOIs (through v3.1) hard-coded tactical metrics into Recital A — "14 identified sites", "12 months of commercial commitment", "positioning as one of the leading…". This created three problems:

1. **Limiting**: Counts become dated the moment a site is added or de-risked.
2. **Exposing**: "12 months of commercial commitment" reads as a delivery promise; in a non-binding LOI this is wrong framing.
3. **Puffery risk**: "positioning as one of the leading" is salesy; lender-grade documents read it as weak signal.

v3.2 replaced the metrics-in-Recital-A pattern with institutional platform framing drawn from the MPN. v3.3 added per-type tails for DS/SS/EP. v3.4 collapses the three variants into a single canonical body (user-authored) and adds tails for EU + WS as well.

---

## Shared body (v3.4 canonical — used for all 5 types)

> {Provider short name} (the "Provider") develops and operates Digital Energy Centers ("DECs"), distributed energy hubs for liquid-cooled AI colocation, integrating accelerated compute with heat recycling and behind-the-meter (BTM) power production, engineered as one integrated system. The Provider is building an integrated sovereign AI infrastructure platform for enterprise and institutional customers, designed for edge inference.

**Word count:** 72. Two sentences. Single paragraph.

**Structure:**
1. DEC definition as appositive-based noun phrase: distributed energy hub + liquid-cooled AI colocation + three co-located outputs (compute / heat / BTM power) + system-integrated design
2. Platform framing: integrated sovereign AI platform, enterprise + institutional customers, edge-inference positioning

**Key wording decisions (user-approved 2026-04-17):**
- "distributed energy hubs" — term-of-art for grid-interconnected distributed energy resources (DER); carries the grid-tie story implicitly
- "heat recycling" — plain English; matches how growers and district-heating operators describe the offtake
- "behind-the-meter (BTM) power production" — precise energy-industry term for on-site generation
- "engineered as one integrated system" — active-design verb; signals system-level engineering (not assembled from parts)
- "edge inference" — workload positioning; narrower than v3.3's "compute capacity" but intentional (inference is DE's current sales motion)
- "enterprise and institutional customers" — customer scope without geographic restriction (DE sells European-sited capacity to buyers internationally)

**Dropped v3.3 phrases:** "purpose-built" (marketing register; see QA rule R-21), "on-site energy recycling" (conflated generation with recovery), "grid-flexible operation" (marketing-adjacent), "structured for institutional project financing" (meta-commentary; see QA rule R-22), "from a single energy input" (factually wrong — power is produced, not single-input recycled), "across European markets" (customer-scope restriction; fixed by S3 user polish)

---

## Per-type tails (appended after shared body)

The skill appends one tail based on the LOI type. Customer-facing types (EU, WS) use "**The Provider's integrated platform [verb]**" subject (procurement framing); relationship-facing types (DS, SS, EP) use "**The Provider [verb]**" subject (counterpart-engagement framing).

### EU — End User
> The Provider's integrated platform supplies dedicated AI inference capacity to enterprises, AI labs, and research institutions requiring sovereign, high-density and low-latency infrastructure on European soil.

### DS — Distributor
> The Provider seeks qualified channel and integration partners to extend its platform reach to end-user segments where the Partner holds established customer relationships and domain expertise.

### WS — Wholesale
> The Provider's integrated platform contracts liquid-cooled AI colocation capacity at megawatt scale to NeoCloud operators and GPU cloud providers internationally.

### SS — Strategic Supplier
> The Provider seeks qualified EPC contractors, modular infrastructure manufacturers, and OEM vendors to deliver the DEC platform and secure supply continuity across its active development pipeline.

### EP — Ecosystem Partnership
> The Provider engages with ecosystem partners on sovereign AI infrastructure, sustainable datacentre design, and European industrial policy alignment.

---

## Bespoke override

YAML field: `programme.recital_a_variant: bespoke` + `programme.recital_a_bespoke: "full Recital A body text"`. The bespoke text fully replaces the library body (tails still append per type unless the bespoke also supplies the tail).

Bespoke text is still subject to the QA linter:

- **R-1 (fail):** `"minimum commitment term of 5 years"` banned
- **R-2 (fail):** `\b\d+\s+identified\s+sites\b` — no fixed site counts
- **R-3 (fail):** `"12 months of commercial commitment"`
- **R-5 (fail):** `"We are confident that"`
- **R-14 (warn, body-wide v3.4):** salesy adjectives — `"leading"`, `"innovative"`, `"cutting-edge"`, `"world-class"`, `"best-in-class"`
- **R-15 (warn):** `"positioning (its|itself) as"` — formulaic
- **R-21 (warn, v3.4):** `"purpose-built"`, `"state-of-the-art"` — marketing register
- **R-22 (warn, v3.4):** meta-commentary patterns — `"Provider's ability to"`, `"depends in part on"`, `"is intended to evidence"`, etc.

If the bespoke text trips any `fail` rule, the generator refuses to embed it and falls back to the canonical body. If it trips `warn` rules, the user is prompted for acknowledgement.

---

## Legacy variant keys (backward compatibility)

Legacy YAMLs from v3.2 / v3.3 that set `programme.recital_a_variant` to `"default"`, `"sovereignty"`, or `"integration"` continue to render correctly. The three variant keys are accepted but ignored — all three resolve to the single canonical body. No migration break for existing intake files.

QA rule R-16 (info-level) notes when `recital_a_variant` is not explicitly set; no user action required.

---

## Recital B, C, D are NOT in this library

Only Recital A is library-sourced. Recital B is counterparty-specific and must be written per the methodology in `counterpart-description-framework.md` (including the v3.4 Tier Hierarchy Policy and Fabrication Gate). Recitals C and D are generated per-type by the engine (`recitals()` method in `generate_loi.py`).

---

## Drift guard

When MPN supersedes v3.2:

1. Read the new MPN § 1.3, § 4.6, § 9.1 (Identity, Integration, Investor Thesis).
2. Check whether any clause in the canonical body above contradicts the new narrative.
3. Update the body **in this file first**, then update the generator's `RECITAL_A_BODY` constant to match, then bump the `Last synced to` header.
4. The generator reads `RECITAL_A_BODY` + `RECITAL_A_TAIL_BY_TYPE` as Python constants — they must be kept in sync with this library file manually (no automated sync today; future work).
5. Old LOIs executed under prior bodies do not need re-execution; this is forward-only.

If the library drifts behind MPN for more than one quarter, escalate to the skill owner (Carlos).
