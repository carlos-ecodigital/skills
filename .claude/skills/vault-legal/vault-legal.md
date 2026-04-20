---
tier: 1

name: vault-legal
description: >-
  Load this skill when the user needs to cite or interpret Dutch legislation, 
  regulations, or case law relevant to DE's permitting programme. Covers 
  Omgevingswet, Wabo, Warmtewet, Wcw, Energiewet, Mijnbouwwet, and ECLI 
  case law. Use for: drafting legal arguments, verifying statutory basis for 
  a permitting route, checking BOPA criteria, interpreting warmtelevering 
  definitions, or confirming shell-in-shell legal certainty. Companion skills: 
  netherlands-permitting, permit-drafter, vault-zoning.
---

# Vault Skill — Dutch Legal

This skill connects Claude to the **Dutch Legal knowledge vault**: primary legislation, subordinate regulations, ECLI-referenced court decisions, and BOPA playbooks covering all statutory and case law relevant to DE's shell-in-shell programme.

---

## Vault Location

**Local path (Mac):**
```
~/Library/CloudStorage/GoogleDrive-jelmer@ecodigital.group/Gedeelde drives/NEW_Ops/Projects Benelux_Ops/Dutch Legal/
```

> If this path returns no files, the vault may not be synced locally. Ask the user to right-click the folder in Finder → "Make available offline."

---

## Vault Structure

```
Dutch Legal/
├── wiki/
│   ├── laws/             ← Omgevingswet, Wabo, Warmtewet, Wcw, Energiewet, Mijnbouwwet
│   ├── regulations/      ← Bbl, Bal, Bkl, Omgevingsbesluit, AMvBs
│   ├── case-law/         ← ECLI-referenced Raad van State decisions
│   ├── concepts/         ← BOPA, bruidsschat, functionele binding, nevenactiviteit
│   ├── playbooks/        ← BOPA 26-week route, shell-in-shell, principeverzoek
│   ├── entities/         ← Regulatory bodies (RvS, DSO, RVO, provinces)
│   └── contradictions/   ← Conflicting interpretations flagged for legal review
└── raw/
    ├── laws/             ← Source XML/HTML from wetten.nl
    ├── case-law/         ← ECLI PDFs
    └── guidance/         ← Circulaires, beleidsregels, IPLO guidance
```

---

## Step 1 — Load Master Index

Before answering, read:
```
[vault-root]/wiki/index/MASTER-INDEX.md
```

---

## Step 2 — Load Relevant Files

**For statutory questions:**
```
[vault-root]/wiki/laws/{wet-name}.md
```

**For case law:**
```
[vault-root]/wiki/case-law/{ECLI-ID}.md
```

**For concept definitions:**
```
[vault-root]/wiki/concepts/{concept-name}.md
```

**For permitting route guidance:**
```
[vault-root]/wiki/playbooks/{route-name}.md
```

---

## Established Legal Positions (pre-loaded)

These are DE's confirmed legal positions — do not contradict without flagging:

| Position | Source | Confidence |
|----------|--------|-----------|
| Shell-in-Shell vergunningsvrij (≤50 m² binnen productiekas) | Naulanden precedent, 3 Feb 2026 | HIGH |
| WKC = energie-installatie, not datacenter | Looije legal memo v1.2 | HIGH |
| BOPA is primary permitting route (26-week track) | Omgevingswet Art. 5.1 | HIGH |
| ≥85% productiekas rule applies for bijbehorend bouwwerk | Omgevingswet Bijlage II | HIGH |
| Warmtelevering must be "substantieel en onmiskenbaar" | Looije functionele binding definition | HIGH |
| WKC "gemeenschappelijke glastuinbouwvoorziening C" as-of-right | PrimAviera 4 Art. 3.1b | MEDIUM (plan-specific) |

---

## Critical Framing Rules (apply always)

- WKC is never a "datacenter" — it is an "energie-installatie" or "warmteproductie-installatie"
- Cite articles by law + article number (e.g., "Omgevingswet Art. 5.1b Ow")
- Distinguish: VASTGESTELD (binding) vs. ONTWERP (not yet binding) plans
- Distinguish: Omgevingswet (Ow, post-Jan 2024) vs. Wabo (pre-2024) procedures

---

## Freshness Check

```
[vault-root]/logs/ingestion-log.md
[vault-root]/wiki/index/ACTIVITY-LOG.md
```

---

## Compounding with Other Skills

| Scenario | Add This |
|----------|----------|
| Need zoning plan text for the legal argument | `/vault-zoning` |
| Drafting a formal BOPA application | `/permit-drafter` |
| Full permitting strategy for a specific project | `/netherlands-permitting` |
| Tax/financial structuring implications | `/vault-finance` |
