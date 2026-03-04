# Contract Drafting -- Specialization Overview

## Scope

This specialization covers the drafting, review, and negotiation of commercial contracts including: Service Agreements, Master Service Agreements (MSA), Non-Disclosure Agreements (NDA/NCNDA), Letters of Intent (LOI), Memoranda of Understanding (MOU), Term Sheets, Distribution Agreements, License Agreements, Consulting Agreements, and general B2B commercial contracts.

For EPC contracts, see also `energy-project-finance/epc-contracts.md`. For SPA, SHA, and JV agreements, see `corporate-ma/`.

## 5-Layer Knowledge Model

| Layer | Content | Source |
|---|---|---|
| 1. Core concepts | Contract law principles, party autonomy, risk allocation, consideration/cause | Universal (adapted per jurisdiction in `jurisdictions/*/contract-law.md`) |
| 2. Jurisdiction-specific rules | Mandatory provisions, interpretation standards, limitation periods | `jurisdictions/*/contract-law.md` + `terminology.md` |
| 3. Templates & precedents | Reusable document structures with placeholder variables | `examples/*.md` |
| 4. Process workflows | Intake questionnaires, 3-phase drafting workflow | This file + `intake-framework.md` |
| 5. Checklists & best practices | Pre-signing verification, clause-level drafting notes | `pre-signing-checklist.md` + `sections-guide.md` |

## 3-Phase Workflow

### Phase 1: Intake

Conduct the applicable questionnaire in conversational batches. **Never present all questions at once.** Group questions into logical batches (typically 6), presenting each batch only after the previous is answered. See `intake-framework.md` for the batch methodology.

**Available questionnaires:**
- Service Agreement: `questionnaire-service-agreement.md` (82 questions, 12 parts)
- NDA/NCNDA: `questionnaire-nda.md` (Planned)
- LOI / MOU: `questionnaire-loi.md` (Planned)
- Term Sheet (commercial): `questionnaire-term-sheet.md` (Planned)
- MSA: `questionnaire-msa.md` (Planned)
- SPA: see `corporate-ma/questionnaire-spa.md` (Planned)
- SHA: see `corporate-ma/questionnaire-sha.md` (Planned)

For document types without a dedicated questionnaire, use the general intake framework.

### Phase 2: Generation

After completing intake:
1. Use the applicable template from `examples/` as structural baseline
2. Load `core/drafting-conventions.md` for formatting rules
3. Load `core/clause-library.md` for reusable clause skeletons
4. Load the relevant jurisdiction file(s) from `jurisdictions/*/contract-law.md`
5. Replace all `{{PLACEHOLDER}}` variables with intake answers
6. Omit sections not applicable based on intake
7. Adapt clause language to the governing law jurisdiction
8. Mark unresolved items with `[REVIEW REQUIRED: reason]`

### Phase 3: Review and Refinement

After generating the draft:
1. Present a summary table of sections included with key commercial positions
2. Flag ambiguities and areas with multiple drafting approaches
3. Offer to adjust risk balance (liability cap, termination rights, performance guarantees)
4. Offer to generate companion documents (SLA, DPA, rate card)
5. Run `pre-signing-checklist.md` and flag items requiring attention

## 26-Section Contract Structure

A complete Service Agreement contains up to 26 sections. Include or exclude based on intake.

| # | Section | Required | Trigger |
|---|---|---|---|
| -- | Cover Page / Title Block | Always | -- |
| 1 | Preamble and Recitals | Always | -- |
| 2 | Definitions and Interpretation | Always | -- |
| 3 | Scope of Services | Always | -- |
| 4 | Service Standards and SLAs | Conditional | Performance metrics needed |
| 5 | Term and Duration | Always | -- |
| 6 | Compensation and Payment | Always | -- |
| 7 | Expenses and Reimbursement | Conditional | Reimbursable expenses exist |
| 8 | Taxes | Always | -- |
| 9 | Intellectual Property | Always | -- |
| 10 | Confidentiality | Always | -- |
| 11 | Data Protection and Privacy | Conditional | Personal data processed |
| 12 | Representations and Warranties | Always | -- |
| 13 | Limitation of Liability | Always | -- |
| 14 | Indemnification | Always | -- |
| 15 | Insurance | Conditional | Insurance requirements specified |
| 16 | Termination | Always | -- |
| 17 | Consequences of Termination | Always | -- |
| 18 | Force Majeure | Always | -- |
| 19 | Dispute Resolution | Always | -- |
| 20 | Governing Law and Jurisdiction | Always | -- |
| 21 | Assignment and Subcontracting | Always | -- |
| 22 | Notices | Always | -- |
| 23 | Amendment and Waiver | Always | -- |
| 24 | Severability | Always | -- |
| 25 | Entire Agreement | Always | -- |
| 26 | Counterparts | Always | -- |
| -- | Signature Block | Always | -- |
| -- | Schedules and Exhibits | Conditional | Based on intake |

## Key Files in This Specialization

| File | Purpose | Lines |
|---|---|---|
| `overview.md` | This file -- workflow, section structure, methodology | ~150 |
| `intake-framework.md` | Batch questioning methodology for all document types | ~80 |
| `sections-guide.md` | Detailed drafting guidance for all 26 sections | ~635 |
| `pre-signing-checklist.md` | Pre-execution verification checklist | ~157 |
| `questionnaire-service-agreement.md` | 82 questions across 12 parts for SA intake | ~310 |
| `examples/service-agreement-template.md` | Full SA template with placeholder variables | ~1,372 |
