---
tier: 1

name: vault-zoning
description: >-
  Load this skill whenever the user asks about a Dutch zoning plan, bestemmingsplan, 
  gemeente permitting strategy, BOPA route, nevenactiviteit rules, TAM moratorium, 
  energie-installatie framing, glastuinbouw bestemming, or any specific plan ID 
  (NL.IMRO.*). Provides structured access to the 128-plan Zoning Plans knowledge vault 
  with gemeente wiki pages, legal concept pages, and the BOPA submission template. 
  Companion skills: netherlands-permitting, legal-counsel, permit-drafter.
---

# Vault Skill — Zoning Plans

This skill connects Claude to the **Zoning Plans knowledge vault**: 128+ parsed bestemmingsplan wiki pages, gemeente strategy pages, legal concept guides, and the full BOPA submission template for the DE shell-in-shell permitting programme.

---

## Vault Location

**Local path (Mac):**
```
~/Library/CloudStorage/GoogleDrive-jelmer@ecodigital.group/Gedeelde drives/NEW_Ops/Projects Benelux_Ops/Zoning Plans/
```

> If this path returns no files, the vault may not be synced locally. Ask the user to right-click the folder in Finder → "Make available offline."

---

## Step 1 — Load Index on Every Invocation

Before answering any question, read:

```
[vault-root]/wiki/_index.md
```

This is the master index of all 128 plans — plan ID, municipality, plan type, status (ENRICHED / STUB), and tier. Use it to:
- Confirm whether a plan has been parsed (ENRICHED) or is a placeholder (STUB)
- Find all plans for a given gemeente
- Identify which plans are Tier 1 (highest permitting priority)

---

## Step 2 — Load Relevant Source Pages

For plan-specific questions, read:
```
[vault-root]/wiki/sources/{PLAN_ID}.md
```

For gemeente-level questions, read:
```
[vault-root]/wiki/entities/gemeenten/{Gemeente}.md
```

Available gemeente pages: Uithoorn, Westland, Haarlemmermeer, Lansingerland, Venlo, Ridderkerk, Waddinxveen, Pijnacker-Nootdorp, Hollands-Kroon, Zuidplas, Weststellingwerf (check index for full list).

---

## Step 3 — Load Concept Pages When Relevant

| Topic | File |
|-------|------|
| Nevenactiviteit rules & BVO caps | `wiki/concepts/nevenactiviteit.md` |
| BOPA route & ETFAL justification | `wiki/concepts/bopa.md` |
| Energie-installatie framing | `wiki/concepts/energie-installatie.md` |
| Parapluplan-datacenter overlay plans | `wiki/concepts/parapluplan-datacenter.md` |
| Verbredingsactiviteiten (VNG buitengebied) | `wiki/concepts/verbredingsactiviteiten.md` |

---

## Step 4 — BOPA Template (for drafting)

When the user is preparing a BOPA submission:
```
[vault-root]/wiki/templates/BOPA-WCK-glastuinbouw-template-v1.md
[vault-root]/wiki/templates/BOPA-field-registry.md
```

---

## Critical Framing Rules (apply always)

- **NEVER** write "datacenter" in permitting or gemeente contexts — always "energie-installatie" or "warmteproductie-installatie"
- **NEVER** write "datacenter-toelating" — always "tuinbouwversterking"
- **WKC** = Warmte-Kracht-Computer — primary output is warmth, not compute

---

## Key Facts to Know Before Answering

| Fact | Value |
|------|-------|
| Highest-relevance plan | NL.IMRO.0394.BPGrysglastb1ewijz-C001 (PrimAviera 4 — AS-OF-RIGHT gemeenschappelijke glastuinbouwvoorziening C) |
| Strongest datacenter precedent | NL.IMRO.0451.BPDatacenters-VG01 (Uithoorn — VASTGESTELD) |
| Active TAM moratorium | Westland (TAMDATACNTSpbp-ON01, ONTWERP — prohibits datacenter permits) |
| Total plans in vault | 128 (as of 2026-04-20) |
| Plans enriched (not stub) | Check `wiki/_index.md` for current count |

---

## Freshness Check

To verify when the vault was last updated:
```
[vault-root]/wiki/_log.md
```

---

## Compounding with Other Skills

Stack this vault skill with:

| Scenario | Add This |
|----------|----------|
| Need statutory basis (Omgevingswet articles) | `/vault-legal` |
| Drafting a formal BOPA application | `/permit-drafter` |
| Gemeente-specific permitting strategy | `/netherlands-permitting` |
| Financial implications of permitting route | `/vault-finance` |
