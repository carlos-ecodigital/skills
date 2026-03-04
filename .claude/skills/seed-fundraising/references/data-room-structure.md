# Data Room Structure -- Seed Round Due Diligence

## 1. Purpose

The virtual data room (VDR) is where investors go deep. After the pitch deck earns a meeting and the IM earns conviction, the data room is where due diligence happens. A well-organized data room signals professionalism, builds trust, and accelerates closing. A disorganized one creates doubt.

## 2. Folder Structure

```
/[Company Name] -- Seed Round Data Room
|
|-- 01_Overview
|   |-- Executive Summary (PDF)
|   |-- Pitch Deck (PDF)
|   |-- Investment Memorandum (PDF)
|   |-- Company Fact Sheet (1-page)
|
|-- 02_Corporate
|   |-- Certificate of Incorporation / Handelsregister extract
|   |-- Articles of Association (Statuten / Statuten AG)
|   |-- Shareholders Agreement (if existing)
|   |-- Board resolutions
|   |-- Organizational chart
|   |-- UBO register extract
|   |-- KvK / Handelsregisteramt extracts
|
|-- 03_Financial
|   |-- Financial Model (Excel)
|   |-- Financial Model Assumptions Document (PDF)
|   |-- Historical Financial Statements (if any)
|   |-- Cap Table (current)
|   |-- Cap Table (pro forma post-round)
|   |-- Bank statements (last 6 months)
|   |-- Existing SAFEs / Convertible Notes / Loan Agreements
|
|-- 04_Legal
|   |-- Material Contracts (executed)
|   |   |-- Customer contracts / LOIs
|   |   |-- Supplier / EPC contracts
|   |   |-- Land / recht van opstal agreements
|   |   |-- Grid connection agreements
|   |   |-- O&M contracts
|   |-- IP Documentation
|   |   |-- Patent filings
|   |   |-- Trademark registrations
|   |   |-- IP assignment agreements
|   |-- Regulatory
|   |   |-- Permits (omgevingsvergunning, etc.)
|   |   |-- SDE++ beschikking (if applicable)
|   |   |-- Environmental assessments
|   |-- Compliance
|   |   |-- Privacy policy / GDPR compliance
|   |   |-- AML/KYC procedures
|
|-- 05_Technical
|   |-- Technical Architecture Document
|   |-- Site Plans and Layouts
|   |-- Grid Connection Technical Specifications
|   |-- Equipment Specifications (BESS, cooling, power)
|   |-- Independent Engineer Reports (if available)
|   |-- PUE Analysis / Energy Efficiency Data
|
|-- 06_Market
|   |-- Market Research Reports (third-party)
|   |-- Competitive Analysis
|   |-- Customer References / Testimonials
|   |-- Pipeline Summary
|   |-- LOI / Expression of Interest Summary
|
|-- 07_Team
|   |-- Founder CVs / Biographies
|   |-- Key Employee Profiles
|   |-- Advisory Board Profiles
|   |-- Employment Agreements (founders)
|   |-- ESOP / Option Plan Documentation
|
|-- 08_Fundraise_Documents
|   |-- Term Sheet (when issued)
|   |-- SAFE / Convertible Note Template
|   |-- Subscription Agreement Template
|   |-- Side Letter Templates (if any)
|   |-- NDA Template
```

## 3. Staging Strategy

Not all documents should be available from day one. Stage disclosure to match the investor relationship:

| Stage | What to Share | When |
|---|---|---|
| Initial interest | 01_Overview folder only | First meeting or warm intro |
| Post-NDA | Full data room access | After NDA signed + second meeting |
| Deep DD | 04_Legal + 05_Technical in detail | After term sheet or strong interest |
| Pre-close | 08_Fundraise_Documents | Term sheet negotiation |

## 4. Document Preparation Checklist

### Minimum Viable Data Room (Seed)

These documents should be ready BEFORE you start outreach:

- [ ] Pitch deck (PDF, <10MB)
- [ ] Executive summary (1-2 pages PDF)
- [ ] Financial model (Excel, clean, with assumptions tab)
- [ ] Cap table (current + pro forma)
- [ ] Company incorporation documents
- [ ] Articles of association
- [ ] Founder CVs
- [ ] NDA template (for you to send, not for investor to provide)
- [ ] SAFE or convertible note template (pre-drafted with your lawyer)

### Documents to Prepare During Fundraise

- [ ] Investment memorandum (if targeting institutional investors)
- [ ] Term sheet (typically investor-led, but have your own template)
- [ ] Pipeline / LOI summary (updated monthly)
- [ ] Customer references (with permission)

### Documents to Have Ready for DD

- [ ] Bank statements
- [ ] All material contracts
- [ ] IP documentation
- [ ] Employment agreements
- [ ] Permit applications / approvals
- [ ] Grid connection documentation

## 5. Naming Conventions

| Convention | Example |
|---|---|
| Folder numbering | `01_Overview`, `02_Corporate`, `03_Financial` |
| File naming | `[Category]_[Document]_[Version]_[Date].pdf` |
| Example | `03_Financial_Model_v2.1_2026-02-15.xlsx` |
| Version tracking | v1.0 = first shared; v2.0 = major update; v2.1 = minor update |
| Date format | YYYY-MM-DD (ISO 8601) |

## 6. VDR Platform Selection

| Platform | Cost | Best For | Notes |
|---|---|---|---|
| Google Drive | Free | Pre-seed, angel rounds | Limited tracking |
| Notion | Free-low cost | Seed rounds, tech-savvy investors | Clean presentation |
| DocSend | $10-45/month | Seed rounds | Excellent tracking, per-page analytics |
| Datasite (Merrill) | $$$$ | Series A+, institutional | Enterprise-grade; overkill for seed |
| Ansarada | $$$ | Series A+, infrastructure funds | AI-powered, compliance features |
| DealRoom | $$ | Mid-market | Good balance of cost and features |

**Recommendation at seed**: DocSend for pitch deck tracking + Google Drive or Notion for full data room. Upgrade to Datasite/Ansarada when institutional investors require it.

## 7. Access Tracking

Monitor investor engagement to prioritize follow-up:

| Metric | What It Tells You |
|---|---|
| Time spent per document | Which sections interest them most |
| Documents accessed | How deep they're going |
| Repeat visits | Serious interest signal |
| Forwarded links | Being shared internally (good sign) |
| No access after invite | Polite pass -- follow up once, then move on |

## 8. Infrastructure-Specific DD Items

Beyond standard startup DD, infrastructure investors will request:

| Category | Documents | Why |
|---|---|---|
| Grid | Connection agreement, TenneT/DSO correspondence | Validate grid access claim |
| Site | Recht van opstal, erfpacht, bestemmingsplan | Land rights and zoning |
| Permits | Omgevingsvergunning, MER, stikstof assessment | Regulatory clearance |
| Technical | Independent engineer report, equipment specs | Asset quality validation |
| Insurance | Broker quotes, coverage terms | Risk transfer adequacy |
| Environmental | Soil surveys, contamination reports | Environmental liability |
| Construction | EPC contract (or heads of terms), timeline | Execution risk assessment |
| Revenue | Offtake agreements, LOIs, market analysis | Revenue certainty |

## 9. Consistency Audit

Before sharing the data room, verify:

| Check | Details |
|---|---|
| Financial consistency | Model numbers match deck, IM, and exec summary |
| Cap table accuracy | Percentages add to 100%; ESOP correctly sized |
| Entity names | Consistent across all documents |
| Date currency | No documents with outdated data (>6 months) |
| Version control | Latest versions only; remove drafts |
| Confidentiality | "Confidential" marking on all documents |
| Links | All hyperlinks and cross-references work |

---

## Cross-References

| Topic | Reference File |
|---|---|
| Due diligence checklist (project-level) | `project-financing/references/due-diligence-checklist.md` |
| Financial model guide | [references/financial-projections.md](financial-projections.md) |
| Cap table structure | [references/cap-table-guide.md](cap-table-guide.md) |
| Investment memo | [references/investment-memo-guide.md](investment-memo-guide.md) |
| Legal framework (NL) | `project-financing/references/netherlands-legal-framework.md` |
