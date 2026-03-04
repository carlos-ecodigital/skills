# M0: Document Ingestion & Triage

**Module metadata:**
- Questions: 8 + 40-item document checklist
- Priority: P0 (all)
- Track: `[BOTH]` — always loaded
- Feeds: All downstream modules
- Dependencies: None (this is always first)
- Load after: `intake-router.md`

---

## Purpose

Before asking a single question, ingest everything that already exists. Every document shared reduces the question count by answering questions upfront. This module runs a 3-step protocol: CRM/system lookup → external research → document ingestion → gap list.

---

## Phase 0 Questions

### 0.1 Document Share
`DOC` | `P0` | `[BOTH]`

Share all existing materials. Anything you have — polished or rough draft:
- Pitch deck (any version)
- Executive summary or one-pager
- Financial model or projections spreadsheet
- Cap table (current)
- Corporate structure diagram
- Articles of association / incorporation documents
- Shareholders' agreement (SHA) or SAFE/convertible note instruments
- Letters of intent, term sheets, or framework agreements
- Technical specifications or engineering reports
- Permit applications or approvals
- Site plans or layout drawings
- Insurance quotes or broker engagement letters
- Investor updates or board materials
- Business plan or strategy documents

**Processing**: For each document shared, extract answers to downstream module questions and mark them as `[CAPTURED FROM: document_name]`. Only ask questions that remain unanswered after document review.

---

### 0.2 CRM & System Data
`ANS` | `P0` | `[BOTH]`

Is there an existing CRM record (HubSpot, Salesforce, or other) for this company or its contacts?
- CRM system used
- Company record exists? Contact records?
- Deal/pipeline stage if tracked
- Notes or activity history available?

**Processing**: If CRM access is available, look up the company and extract: contact details, deal stage, prior meeting notes, activity history. Feed into context for all modules.

---

### 0.3 External Research
`ANS` | `P0` | `[BOTH]`

Conduct external research on {company} before asking detailed questions:
- Company website review
- LinkedIn profiles of founders/key team
- Crunchbase / PitchBook for funding history
- Chamber of Commerce / company registry (KvK, Handelsregister, etc.)
- News articles, press releases
- Industry reports mentioning the company
- Patent/IP databases if relevant

**Processing**: Summarize findings. Identify information already available publicly that does not need to be asked.

---

### 0.4 Prior Context
`ANS` | `P0` | `[BOTH]`

Any prior context the intake operator should know:
- Previous meetings or conversations (dates, participants, key takeaways)
- Referral source (who introduced this company)
- Known competitors or market position
- Known strengths or concerns
- Urgent timeline or deadlines

---

### 0.5 Intake Mode
`ANS` | `P0` | `[BOTH]`

What is the immediate goal?
- **Full intake**: Comprehensive investment case (all relevant modules)
- **Targeted deliverable**: Specific output needed (pitch deck, IM, financial model, data room)
- **Meeting prep**: Quick context package before a specific meeting
- **Gap analysis**: Identify what's missing from existing materials

If targeted deliverable or meeting prep: which deliverable or which meeting? This determines which modules to prioritize.

---

### 0.6 Priority Level
`ANS` | `P0` | `[BOTH]`

What priority tier is needed now?
- **P0 only**: Minimum viable — enough for first investor/lender conversations
- **P0 + P1**: Full due diligence readiness
- **P0 + P1 + P2**: Institutional-grade, term sheet / financial close ready

This determines how deep each module goes.

---

### 0.7 Timeline
`ANS` | `P0` | `[BOTH]`

What is the timeline?
- First investor/lender meeting date (if scheduled)
- Target date for materials to be ready
- Any external deadlines (subsidy applications, permit windows, fund closing dates)

---

### 0.8 Founder Availability
`ANS` | `P0` | `[BOTH]`

Who will answer intake questions?
- Name(s) and role(s)
- Availability (hours per week for intake sessions)
- Preferred format (live conversation, async written answers, document upload)
- Who else may need to contribute? (CFO, CTO, legal counsel, technical advisor)

---

## Document Existence Checklist

After Q0.1, map every document against this checklist. Mark each as: ✅ Exists | 🔄 In Progress | ❌ Missing | N/A

### Corporate (feeds M1)
- [ ] Certificate of incorporation
- [ ] Articles of association (current)
- [ ] Corporate structure diagram
- [ ] Share register (current)
- [ ] UBO filing / beneficial ownership declaration
- [ ] Board resolutions (material)
- [ ] Shareholders' agreement (SHA)

### Tax & Legal (feeds M1)
- [ ] Tax counsel opinion on structure
- [ ] Transfer pricing documentation
- [ ] Intercompany agreements
- [ ] Tax residency certificates

### Team (feeds M2)
- [ ] Founder CVs / bios
- [ ] Employment agreements (founders + key hires)
- [ ] IP assignment agreements
- [ ] ESOP/option plan documentation
- [ ] Vesting schedules

### Market & Strategy (feeds M3)
- [ ] Pitch deck
- [ ] Executive summary / one-pager
- [ ] Market sizing analysis
- [ ] Competitive landscape analysis

### Technical — BESS (feeds M4)
- [ ] Battery manufacturer specifications
- [ ] Degradation curve data
- [ ] Revenue stacking model
- [ ] Fire safety assessment (PGS 37 or equivalent)
- [ ] Grid code compliance documentation
- [ ] Independent engineer report

### Technical — DC/AI (feeds M5)
- [ ] Facility design specifications
- [ ] Cooling system design
- [ ] Network topology design
- [ ] GPU/accelerator procurement agreements
- [ ] SLA templates

### Sites (feeds M6)
- [ ] Land agreements (per site)
- [ ] Grid connection agreements (per site)
- [ ] Permit applications / approvals (per site)
- [ ] Site plans / layout drawings (per site)
- [ ] Environmental assessments (per site)
- [ ] Soil investigation reports (per site)

### Financial (feeds M7, M8, M9)
- [ ] Financial model (Excel/Google Sheets)
- [ ] Assumptions document
- [ ] Cap table (fully diluted)
- [ ] SAFE / convertible note instruments
- [ ] Bank statements (last 12 months)
- [ ] Revenue contracts / LOIs

### Debt / Insurance (feeds M7)
- [ ] Lender term sheets or indicative terms
- [ ] Insurance broker engagement letter
- [ ] Preliminary insurance quotes
- [ ] EPC contract (draft or executed)

### Data Room (feeds M9)
- [ ] NDA template
- [ ] Data room access set up (VDR platform)
- [ ] Document index / inventory

---

## Post-Ingestion Output

After processing all documents and research, produce:

1. **Gap List by Module**: For each module (M1-M9), list the questions that remain unanswered after document ingestion. This becomes the effective question set.
2. **Document Quality Assessment**: Flag any documents that are outdated, incomplete, or inconsistent.
3. **Recommended Module Sequence**: Based on gaps, suggest which module to start with (typically the one with the most gaps in P0 questions).
4. **Estimated Remaining Effort**: Approximate number of questions remaining, grouped by priority tier.
