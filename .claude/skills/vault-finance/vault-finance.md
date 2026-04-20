---
tier: 1

name: vault-finance
description: >-
  Load this skill when the user asks about Dutch tax compliance, entity structuring, 
  VPB/BTW/loonheffingen obligations, SDE++ fiscal treatment, project finance 
  structuring (DC/BESS), deelnemingsvrijstelling, innovatiebox, DGA salary, 
  jaarrekening preparation, dividend distribution, or any NL tax concept affecting 
  DE entities (DEG, DEN BV, EcoDigital AG, GREENTECH AG). Also use for: checking 
  quarterly BTW obligations, verifying VPB loss carry-forwards, or structuring cross-border 
  NL-DE transactions. Companion skills: financial-model-interpreter, project-financing, 
  legal-counsel.
---

# Vault Skill — NL Finance & Tax

This skill connects Claude to the **DE_NL Finance knowledge vault**: Dutch tax law, compliance playbooks, entity-specific accounting scenarios, and fiscal structuring guides relevant to DE's multi-entity energy-technology group.

---

## Vault Location

**Current local path (Mac) — pre-Drive migration:**
```
~/Documents/DE_NL_Finance/
```

**Future path (post-migration to Google Drive):**
```
~/Library/CloudStorage/GoogleDrive-jelmer@ecodigital.group/Gedeelde drives/NEW_FINANCE_Q4 25/DE_NL_Finance/
```

> Update this skill file when the migration is complete.

---

## Vault Structure

```
DE_NL_Finance/
└── nl-tax-vault/
    ├── wiki/
    │   ├── tax-regimes/        ← VPB, BTW, loonheffingen, dividendbelasting, IB
    │   ├── concepts/           ← deelnemingsvrijstelling, innovatiebox, verliesverrekening,
    │   │                          interest-aftrekbeperkingen, excessief-lenen,
    │   │                          substance-vereisten, wbso-rd-tax-credit, uitkeringstest
    │   ├── playbooks/          ← btw-quarterly-checklist, vpb-aangifte-checklist,
    │   │                          payroll-monthly-checklist, jaarrekening-preparation,
    │   │                          dividend-distribution-checklist, dga-salary-checklist,
    │   │                          sde-plus-plus-application-playbook, wkr-annual-check
    │   ├── scenarios/          ← energy-project-vpb-structure, dc-bess-project-finance-
    │   │                          structuring, nl-de-cross-border-holding, dga-box2-dividend
    │   ├── rulings/            ← Tax authority rulings and advance pricing agreements
    │   └── contradictions/     ← Conflicting interpretations flagged for review
    └── QUICK-START.md          ← Load this first
```

---

## Step 1 — Load Quick-Start on Every Invocation

```
[vault-root]/nl-tax-vault/QUICK-START.md
```

---

## Step 2 — Load Relevant Files

**For tax compliance questions:**
```
[vault-root]/nl-tax-vault/wiki/tax-regimes/{regime}.md
```
Available: `vpb-overview.md`, `btw-overview.md`, `loonheffingen.md`, `dividendbelasting.md`, `ib-overview.md`

**For structuring concepts:**
```
[vault-root]/nl-tax-vault/wiki/concepts/{concept}.md
```

**For compliance checklists:**
```
[vault-root]/nl-tax-vault/wiki/playbooks/{checklist}.md
```

**For project-specific scenarios (most useful for DE deal structuring):**
```
[vault-root]/nl-tax-vault/wiki/scenarios/energy-project-vpb-structure.md
[vault-root]/nl-tax-vault/wiki/scenarios/dc-bess-project-finance-structuring.md
[vault-root]/nl-tax-vault/wiki/scenarios/nl-de-cross-border-holding.md
```

---

## Key Facts

| Entity | Type | Jurisdiction |
|--------|------|-------------|
| DEG | Digital Energy Group (parent) | NL |
| DEN BV | Digital Energy Netherlands BV | NL |
| EcoDigital AG | Swiss holding | CH |
| GREENTECH AG | Swiss Greentech entity | CH |

---

## Critical Rules (apply always)

- **FM v3.0 is the active financial model** (`DEG - FM - v3.0 (1).xlsx` in Downloads). Do not cite figures from older versions.
- **Never derive financial conclusions from vault content alone** — vault contains law and structure, not live figures. Cross-reference FM v3.0 for any numbers.
- Colo fee: **€150/kW IT/mth** (2% annual escalation) — not €175.
- SDE++ toggle is currently **OFF** in v3.0.
- FaaS/aFRR revenue is **€0** in v3.0 (needs Ampowr data added).

---

## Example Queries

> "Run through the btw-quarterly-checklist for DEN BV — what needs to be filed this quarter?"

> "What are the substance vereisten for EcoDigital AG to qualify for deelnemingsvrijstelling in NL?"

> "Using the dc-bess-project-finance-structuring scenario as a template, how should we structure UITHOORN-01-DEC for VPB efficiency?"

> "Check the innovatiebox concept page — does our WKC R&D activity qualify for the reduced VPB rate?"

> "What does the dividend-distribution-checklist say about the uitkeringstest for DEN BV?"

---

## Compounding with Other Skills

| Scenario | Add This |
|----------|----------|
| Permitting costs and project finance modelling | `/financial-model-interpreter` |
| Legal basis for a tax structure | `/legal-counsel` or `/vault-legal` |
| SDE++ permitting flow alongside fiscal treatment | `/netherlands-permitting` |
| Project financing structuring (debt/equity) | `/project-financing` |
