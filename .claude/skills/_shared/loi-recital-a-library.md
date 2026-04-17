# LOI Recital A — Canonical Variant Library

Single source of truth for Recital A language across all LOI types produced by `legal-assistant`. Templates and `generate_loi.py` reference variants by key.

**Last synced to:** Master Pitch Narrative v3.2 (2026-04-16).
**Re-sync trigger:** Any MPN revision. Check MPN § 1.3 (Identity), § 4.6 (Integration Logic), § 9.1 (Investor Thesis) against the variants below.

---

## Why this exists

Prior LOIs (through v3.1) hard-coded tactical metrics into Recital A — "14 identified sites", "12 months of commercial commitment", "positioning as one of the leading…". This created three problems:

1. **Limiting**: Counts become dated the moment a site is added or de-risked.
2. **Exposing**: "12 months of commercial commitment" reads as a delivery promise; in a non-binding LOI this is wrong framing.
3. **Puffery risk**: "positioning as one of the leading" is salesy; lender-grade documents read it as weak signal.

v3.2 replaces the metrics-in-Recital-A pattern with institutional platform framing drawn from the Master Pitch Narrative.

---

## Variant selection

The skill suggests a variant based on counterparty profile; user confirms at the assumption-confirmation gate.

| Counterparty profile | Recommended variant |
|---|---|
| Neocloud / GPU cloud / wholesale buyer | `default` |
| European enterprise, AI lab, government / institution, policy-adjacent | `sovereignty` |
| Grower, district-heating utility, energy-led partner, circular-economy counterparty | `integration` |
| System integrator / distributor / channel partner | `default` (use `sovereignty` only if the partner's end-users are sovereignty-sensitive) |
| Strategic supplier / EPC / equipment vendor | `default` |
| Ecosystem partner (standards body, university, co-marketing) | `sovereignty` if EU-mission; else `default` |

`bespoke` is the escape hatch. Must clear the QA linter (R-2, R-3, R-15, R-14).

---

## Variant: `default`

Use for most LOIs. Institutional, geography-agnostic, platform-level framing.

> Digital Energy (the "Provider") develops and operates Digital Energy Centers ("DECs"): purpose-built, liquid-cooled colocation facilities that integrate accelerated compute with on-site energy recycling, thermal recovery, and grid-flexible operation. The Provider is building an integrated sovereign AI infrastructure platform across European markets, structured for institutional project financing and designed to deliver compute capacity alongside heat and grid value from a single energy input.

**Structure:** (1) what a DEC is, (2) what the platform is, (3) how it is financed and what it delivers.
**Word count:** 65. Single paragraph.

---

## Variant: `sovereignty`

Use when the counterparty's decision-making is driven by EU data residency, AI Act / GDPR compliance, or European industrial-policy alignment.

> Digital Energy (the "Provider") develops and operates Digital Energy Centers ("DECs"): purpose-built, liquid-cooled colocation facilities for high-density accelerated compute workloads. The Provider operates a sovereign AI infrastructure platform on European soil, controlled by European operators, designed to serve European enterprises, institutions, and public-sector customers with compliance-grade data residency and independent supply-chain control. DECs integrate AI compute with energy recycling and grid-flexible operation, and the platform is structured for institutional project financing.

**Structure:** (1) what a DEC is, (2) sovereignty mission and audience, (3) integration + financing signal.
**Word count:** 78. Single paragraph.
**MPN anchor:** § 3.3 "Enterprises — Implement AI or Disappear"; § 6.4 "Two-Sided Platform Mechanics".

---

## Variant: `integration`

Use for energy-adjacent counterparties — growers, district-heating operators, renewable / circular partners — where the energy-recycling story is the strategic fit.

> Digital Energy (the "Provider") develops and operates Digital Energy Centers ("DECs"): integrated energy infrastructure assets in which electricity entering a site powers accelerated compute, the resulting heat is recovered and upgraded for thermal offtake to greenhouses or district-heating networks, and residual grid and power-system value is captured through battery storage, flexible generation, and grid-balancing services. DECs turn energy into digital intelligence and capture heat, power, and grid value along the way.

**Structure:** (1) the physical integration (electron path), (2) "One Watt, Three Jobs" framing.
**Word count:** 78. Single paragraph.
**MPN anchor:** § 4.6 "Integration Logic"; "One Watt, Three Jobs"; "One cable, three factories, three revenue streams".

---

## Variant: `bespoke`

Escape hatch. Populates `programme.recital_a_bespoke` verbatim. Must pass the QA linter:

- **R-2 (fail):** No `"14 identified sites"` (or any fixed site count language)
- **R-3 (fail):** No `"12 months of commercial commitment"`
- **R-15 (warn):** No `"positioning (its|itself) as"`
- **R-14 (warn):** No salesy adjectives (`"leading"`, `"innovative"`, `"cutting-edge"`, `"world-class"`, `"best-in-class"`)

If the bespoke text trips `fail` rules, the generator refuses to embed it and falls back to `default`. If it trips `warn` rules, it prompts for user acknowledgement.

---

## Recital B, C, D are NOT in this library

Only Recital A is library-sourced. Recital B is counterparty-specific and must be written per the methodology in `counterpart-description-framework.md`. Recitals C and D are generated per-type by the engine (Distributor / Wholesale / End User / Strategic Supplier / Ecosystem Partnership variants) and are template-fixed.

---

## Drift guard

When MPN v3.2 is superseded:

1. Read the new MPN § 1.3, § 4.6, § 9.1 (Identity, Integration, Investor Thesis).
2. Check whether any sentence in the variants above contradicts the new narrative.
3. Update variants **in this file first**, then bump `Last synced to` header.
4. The generator reads variants from this file each run — no cascade update needed to templates.
5. Old LOIs executed under prior variants do not need re-execution; this is forward-only.

If Recital A variants drift behind MPN for more than one quarter, escalate to the skill owner (Carlos).
