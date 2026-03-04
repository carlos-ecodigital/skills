# Contract Drafting -- Intake Framework

## Batch Questioning Methodology

All contract drafting begins with a structured intake process. **Never present all questions at once.** Questions are grouped into logical batches, presented conversationally. Each batch is presented only after the previous batch is answered.

## Principles

1. **Conversational batches:** Present 5--15 questions per batch, grouped thematically. Wait for answers before proceeding.
2. **Adaptive skipping:** If an answer makes subsequent questions irrelevant, skip them. Example: if no personal data is processed, skip all data protection questions.
3. **Progressive detail:** Start with high-level context (who, what, when), then drill into commercial terms, then risk allocation, then governance.
4. **Jurisdiction first:** Always identify governing law early (Batch 1 or 2). This determines which jurisdiction-specific questions to ask and which adaptation rules to apply.
5. **Document type detection:** If the user's request implies a specific document type, load the dedicated questionnaire. If no dedicated questionnaire exists, use the general batch structure below.
6. **Energy/BESS/JV flag:** If energy, BESS, EPC, or JV is identified in Batch 2, flag that dedicated clauses are available and incorporate them.

## Standard 6-Batch Structure

This structure applies to all commercial contract types. Dedicated questionnaires (SA, NDA, etc.) refine and expand these batches.

### Batch 1: Parties and Context
- Full legal names and entity types
- Jurisdictions of incorporation
- Registered addresses
- Registration numbers
- Role designation (who provides, who receives)
- **Governing law** (always ask -- never assume)

### Batch 2: Scope and Term
- Nature of services/goods/rights
- Deliverables or scope description
- Commencement date and initial term
- Renewal mechanism
- Key milestones or phases
- Subcontracting needs

### Batch 3: Commercial Terms
- Payment structure (fixed, T&M, milestone, retainer)
- Amounts or rates
- Invoicing frequency and payment terms
- Currency
- Late payment consequences
- Tax treatment (VAT applicability, WHT considerations)

### Batch 4: IP, Confidentiality, and Data
- IP ownership model
- Pre-existing/background IP
- Confidentiality scope and duration
- Personal data processing (triggers DPA)
- Applicable data protection regime

### Batch 5: Risk Allocation
- Liability cap
- Consequential damages exclusion
- Carve-outs from cap
- Indemnification scope
- Insurance requirements
- Force majeure events

### Batch 6: Governance and Disputes
- Dispute resolution (courts vs. arbitration vs. mediation)
- Arbitral institution and seat
- Termination rights (convenience, breach, insolvency, change of control)
- Transition assistance requirements
- Industry-specific compliance
- Additional schedules needed

## Document-Type Variations

### NDA / NCNDA
Simplified intake: parties, direction (mutual/one-way), scope of CI, duration, return/destruction, carve-outs, governing law. Typically 2--3 batches.

### LOI / MOU / Heads of Terms
Focus on: parties, proposed transaction, key terms, conditions precedent, exclusivity, binding vs. non-binding provisions, confidentiality, governing law. Typically 2--3 batches.

### Term Sheet
Focus on: parties, transaction type, key commercial terms (price, structure, conditions), timeline, exclusivity, confidentiality. Typically 2 batches.

### MSA + SOW Structure
MSA intake covers the umbrella terms (governance, liability, IP default, dispute resolution). Each SOW intake is a mini-version of Batches 2--3 focused on specific engagement scope and fees.

## Drafter Notes

- Not all questions will be relevant for every engagement. Skip questions that clearly do not apply.
- Where the user cannot answer a question, mark it `[REVIEW REQUIRED: awaiting input on [topic]]`.
- Gather enough detail to populate all `{{PLACEHOLDER}}` variables in the template.
- If the user provides a term sheet or prior agreement, extract answers from it and confirm with the user rather than re-asking.
