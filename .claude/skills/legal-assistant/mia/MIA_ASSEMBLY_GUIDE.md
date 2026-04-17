# MIA Assembly Guide (DE-MIA v1.0)

Operator-facing guide for assembling and issuing a Master Introduction Agreement (MIA) using the templates in `legal-assistant/mia/templates/`.

For the *why* behind the design decisions, read `legal-assistant/DE-MIA_HANDOVER.md` (in particular the answered MIA-Q1…Q14).

---

## 1. What an MIA is and when to use it

The MIA is a fee instrument. It governs introductions made by a third party (the "**Introducer**") to Digital Energy. Two flavours of introduction are covered, separated into severable annexes:

| Annex | Subject | Regulated? |
| :---- | :---- | :---- |
| Annex A — Commercial Introductions | Customers (colocation services) | No |
| Annex B — Capital Introductions | Investors (capital into DE or a DE-sponsored vehicle) | Touches AFM/FCA/SEC perimeter |

A single Introducer can sign Master + A only, Master + B only, or Master + both. Most Introducers will be one-or-the-other; very few will be both (different skill sets).

Use the MIA when:
- A third party has approached DE proposing to introduce customers or investors and DE is willing to pay a fee for qualifying introductions, OR
- DE proactively wants to formalise a referral arrangement with a known partner.

**Do not** use the MIA for:
- DE's customers themselves (use the colocation LOI then MSA).
- DE's distribution partners with broader scope (use the Distributor LOI; the MIA may sit alongside it as the Cl. 3.4 Referral Agreement).
- Any arrangement where the Introducer is a regulated investment firm acting in that capacity (regulated placement-agent arrangements need a different document — escalate to `legal-counsel`).

### Closing line — deliberately absent

MIA templates have no closing salutation. The generator moves directly from the final clause (Cl. 8.13) to the signature block. This is intentional: an MIA is an executed agreement, not a letter. Do not add a closing line for consistency with LOI/NCNDA templates — the LOI is a letter-form instrument; the MIA is not.

---

## 2. Decision tree

```
Counterparty wants to introduce parties to DE for a fee.
│
├─ Customers only → Master + Annex A
│
├─ Investors only → Master + Annex B  ← REQUIRES legal-counsel review
│
└─ Both → Master + Annex A + Annex B  ← REQUIRES legal-counsel review (for B)
```

Outside scope (escalate):
- Introducer is licensed broker/placement agent → bespoke document, not MIA
- Counterparty wants equity in DE in exchange for introductions → not MIA, restructure as advisor agreement
- Counterparty is a sitting director/officer of DE → not MIA, related-party policy applies

---

## 3. Build sequence per execution

1. **Intake.** Open `legal-assistant/mia/examples/intake_example_<scenario>.yaml` matching the scope (master_only, commercial, capital, both). Copy and rename for the specific Introducer.
2. **Fill YAML.** Complete every field. Anything left as `[…]` becomes a hole in the output document.
3. **Run generator.** `python legal-assistant/mia/generate_mia.py <intake.yaml>` produces the executed `.docx` (Master + activated Annex(es), with cover page).
4. **Counsel review (Annex B only).** Hand the generated draft to the `legal-counsel` skill. Do not send to Introducer until counsel review is complete and any required edits applied.
5. **Issue.** Send via the standard channel (email + DocuSign / eIDAS-compliant signature platform).
6. **Post-execution.** File the executed PDF in the deal vault using the naming convention in §7. Create CRM records for the Introducer in HubSpot. Add the executed Schedule(s) (A-1, B-1) to the Introducer's HubSpot record so per-execution Fee details are retrievable.

For manual (non-script) drafting, work directly from the `_TEMPLATE.md` files; the YAML/script flow is recommended for consistency.

---

## 4. Default values reference

| Parameter | Default | Override guidance |
| :---- | :---- | :---- |
| `[NC_DURATION]` (Master Cl. 6.2) | 12 months | Increase to 18–24 months only for very high-value introductions; never below 12. |
| `[CONFIDENTIALITY_SURVIVAL]` (Master Cl. 5.14, ALT-B) | 3 years | 2-5 negotiable. Trade secrets indefinite by clause. |
| `[LOOKBACK_MONTHS]` (Master Cl. 7) | 12 months | Defend at 12. Shortening exposes DE to fee leakage on warm pipeline. |
| `[ANNEX_A_TAIL]` | 12 months | Harmonised with Master per MIA-Q13. |
| `[ANNEX_B_TAIL]` | 12 months | Harmonised with Master per MIA-Q13. |
| Annex A fee — election default | Capitalised one-time | Operationally simpler. Tiered residual % is option; Introducer elects per Schedule A-1. |
| Annex B fee structure | 2% of Capital Committed, EUR 250,000 cap per intro | Fixed by MIA-Q9. Do not negotiate to flat (Option 1) or uncapped % (Option 3) without commercial sign-off; Option 3 also requires escalated counsel review. |
| Annex B Named Investor List approval window | 10 Business Days | Defend; longer windows weaken the carve-out evidence. |
| Annex B suspension restructure window | 60 days | Defend. |
| Currency | EUR | Default; Schedule A-1 / B-1 may override per execution. |
| Payment terms | Net 30 | Default; Schedule may override per execution. |
| Signing entity (Provider side) | B.V. for Master + A; AG for B (default guidance, MIA-Q7) | Per-deal selectable in YAML. Confirm with finance before locking. |

---

## 5. Bespoke language guide

Most MIAs do **not** require bespoke prose. The Master, Annex A, and Annex B are designed to apply standard text across Introducers. The only fields that must be customised per Introducer are:

- `[INTRODUCER_DESCRIPTION]` (Master Recital B) — one or two sentences describing who the Introducer is and what relationships/credibility they bring. Keep factual; no commercial puffery.
- Schedule A-1 / B-1 fields per Qualifying Introduction — these are filled per execution, not at template assembly.

Avoid bespoke clauses in Annex B in particular. The regulatory safeguards (Cl. B.3, B.4, B.5, B.12, B.13) work as a tightly-drafted suite; any addition or deletion changes the risk profile and must be reviewed by `legal-counsel`.

---

## 6. Red-line protocol

| Clause | Posture | Rationale |
| :---- | :---- | :---- |
| Master Cl. 5 (Confidentiality) | Flexible | Use ALT-A if existing LOI/NDA in place; otherwise ALT-B. |
| Master Cl. 6 (Non-Circumvention) | Defend at 12 months minimum | Below 12 months exposes DE to circumvention risk. |
| Master Cl. 7 (Pipeline Carve-Out) | Defend | This clause replaces an upfront exclusion list (per MIA-Q12). Removing it transfers the risk back to DE. |
| Master Cl. 8.7 / 8.8 (Dutch law / Amsterdam jurisdiction) | Defend | Non-negotiable per LOI v3.0 default. |
| Annex A Cl. A.4 (Fee schedule) | Negotiate | Bands and percentages are commercial. Introducer's election (Capitalised vs Tiered) is contractual. |
| Annex B Cl. B.3 / B.4 / B.5 (Activity limitations and reps) | Defend (do not weaken) | These keep the arrangement outside the regulatory perimeter. Escalate to `legal-counsel` if Introducer pushes back. |
| Annex B Cl. B.8 (Fee schedule) | Defend at 2% / EUR 250k cap | Per MIA-Q9. Switching to uncapped % requires CEO + counsel sign-off. |
| Annex B Cl. B.12 (Automatic suspension) | Defend | Removing this clause materially elevates regulatory risk. |
| Annex B Cl. B.13 (Enhanced severability) | Defend | This is what protects Master + Annex A from a regulatory hit on Annex B. |

---

## 7. Naming convention

Same convention as LOI v3.0:

```
YYYYMMDD_DEG_MIA-{ANNEX}_{Introducer-Short}_(STATUS).pdf
```

Where:
- `{ANNEX}` = `Master`, `A`, `B`, or `MasterAB` (for combined execution)
- `{Introducer-Short}` = short form of Introducer name (no spaces)
- `(STATUS)` = `DRAFT` → `SENT` → `SIGNED` → `LAPSED` → `SUPERSEDED`

Examples:
- `20260420_DEG_MIA-MasterA_NickAlderwelde_(DRAFT).pdf`
- `20260420_DEG_MIA-B_Rutger_(SENT).pdf`
- `20260420_DEG_MIA-MasterAB_TalKatran_(SIGNED).pdf`

---

## 8. HubSpot integration checklist

Per execution:
- [ ] Introducer contact created in HubSpot (Contact type: "MIA Introducer").
- [ ] Deal record created with stage = "MIA Signed" (or equivalent).
- [ ] Schedule A-1 fields uploaded as a Note attachment to the Introducer record (so per-execution Fee details are retrievable).
- [ ] Schedule B-1 fields uploaded as a Note attachment, with `legal-counsel` review confirmation.
- [ ] Named Investor List (Annex B) attached as a private Note; updates appended chronologically.
- [ ] Pipeline carve-out evidence (Master Cl. 7): ensure HubSpot retains contact-history records that can be cited if a Fee is later disputed.

---

## 9. Version control

If a binding clause in the Master is updated (Cl. 5, 6, 7, 8), the change applies to **all** in-flight MIAs from the date of update. Existing executed MIAs are not retroactively amended; they remain governed by the version they were executed under.

If Annex A or Annex B is updated, executed Annexes are not retroactively amended; new executions use the new version.

Version log lives in `legal-assistant/DE-MIA_HANDOVER.md` §Revision log.

---

## 10. Counsel review gate (Annex B)

**No Annex B execution may issue without `legal-counsel` skill review.** Per MIA-Q5 and MIA-P3:

- Run the `legal-counsel` skill on the generated draft (Master + Annex B).
- Capture the review confirmation (date, reviewer note) in Schedule B-1.
- If `legal-counsel` flags items requiring outside Dutch counsel, escalate before sending.
- This gate is a hard build-sequence step, not an open decision.

---

## 11. Onboarding pipeline

The first wave of MIA executions covers four Introducers identified in `DE-MIA_HANDOVER.md` §Introducer pipeline:

| Introducer | Annex(es) | Notes |
| :---- | :---- | :---- |
| Nick Alderwelde (Sovereign AI) | A | First commercial-only execution. Pilot the script. |
| Rutger | B | First capital-only execution. Run through `legal-counsel` end-to-end as a pilot. |
| Tal Katran | A + B | Both annexes. Confirm whether one signing event or staggered. |
| Arie Rastinger | A + B | Both annexes. Same. |

Operational follow-ups before each first execution: confirm full names, entities, jurisdictions, and signing order.
