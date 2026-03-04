# Term Sheet Template / Voorbeeldtermsheet -- Nederlandse Projectfinanciering

Template for indicative term sheet for Dutch infrastructure project finance (BESS, colocation DC, AI factory). Replace all `{{PLACEHOLDER}}` variables with project-specific information. Adapt structure and terms to actual transaction.

**THIS IS A TEMPLATE FOR ILLUSTRATIVE PURPOSES ONLY. NOT LEGAL OR FINANCIAL ADVICE.**

---

## PROJECT TERM SHEET -- INDICATIEF / INDICATIVE

**PROJECT:** {{PROJECT_NAME}}
**DATE:** {{DATE}}
**STATUS:** Indicatief en niet-bindend / Indicative and Non-Binding

---

### 1. PARTIJEN / PARTIES

| Role | Entity |
|---|---|
| Borrower (Kredietnemer) | {{SPV_NAME}} B.V., a besloten vennootschap incorporated under Dutch law, KvK nr. {{KVK_NUMBER}} |
| Sponsor(s) | {{SPONSOR_1_NAME}}, {{SPONSOR_1_JURISDICTION}} ({{SPONSOR_1_STAKE}}%); {{SPONSOR_2_NAME}}, {{SPONSOR_2_JURISDICTION}} ({{SPONSOR_2_STAKE}}%) |
| Arranger(s) (Arrangeur) | {{ARRANGER_NAME}} |
| Agent (Administratief Agent) | {{AGENT_NAME}} |
| Security Agent (Zekerheidsagent) | {{SECURITY_AGENT_NAME}} |
| Technical Adviser (Technisch Adviseur) | {{IE_NAME}} |
| Model Auditor | {{MODEL_AUDITOR_NAME}} |

---

### 2. PROJECT BESCHRIJVING / PROJECT DESCRIPTION

**Project Type:** {{BESS / Colocation Data Center / AI Factory / Hybrid}}
**Location:** {{MUNICIPALITY}}, {{PROVINCE}}, Netherlands
**Site:** {{SITE_DESCRIPTION}} (eigendom / erfpacht / recht van opstal)
**Capacity:** {{CAPACITY}} MW (IT load / installed capacity)
**Technology:** {{TECHNOLOGY_DESCRIPTION}} (e.g., LFP BESS {{DURATION}} hour; Tier {{TIER}} DC; GPU compute {{GPU_TYPE}})
**EPC Contractor:** {{EPC_NAME}} under {{UAV_2012 / UAV_GC_2025 / FIDIC / Custom}} contract
**Expected COD:** {{COD_DATE}}
**Project Life:** {{PROJECT_LIFE}} years

---

### 3. FINANCIERINGSSTRUCTUUR / FINANCING STRUCTURE

| Component | Amount (EUR) | % of Total |
|---|---|---|
| Senior Term Loan | {{SENIOR_AMOUNT}} | {{SENIOR_PCT}}% |
| Construction Facility (if separate) | {{CONSTR_AMOUNT}} | Converts to term loan at COD |
| Mezzanine (if applicable) | {{MEZZ_AMOUNT}} | {{MEZZ_PCT}}% |
| Equity Contribution | {{EQUITY_AMOUNT}} | {{EQUITY_PCT}}% |
| **Total Project Cost** | **{{TOTAL_COST}}** | **100%** |

**Total CAPEX:** EUR {{CAPEX}} (including contingency of {{CONTINGENCY_PCT}}%)
**IDC (Interest During Construction):** EUR {{IDC}}
**Working Capital / Reserves:** EUR {{WC_RESERVES}}
**Gearing:** {{GEARING}}% D / {{100-GEARING}}% E

---

### 4. SENIOR FACILITEIT / SENIOR FACILITY TERMS

| Term | Detail |
|---|---|
| Facility Type | Senior secured non-recourse term loan |
| Currency | EUR |
| Amount | EUR {{SENIOR_AMOUNT}} |
| Availability Period | From financial close to {{AVAILABILITY_END}} ({{AVAILABILITY_MONTHS}} months) |
| Final Maturity | {{MATURITY_DATE}} ({{TENOR}} years from financial close) |
| Reference Rate | EURIBOR {{1M/3M/6M}} |
| Margin | {{MARGIN}} bps per annum |
| Commitment Fee | {{COMMIT_FEE}}% per annum on undrawn committed amounts |
| Upfront Fee | {{UPFRONT_FEE}}% flat |
| Repayment | {{Sculpted / Annuity / Bullet}} based on {{DSCR_TARGET}}x target DSCR |
| Interest Rate Hedging | Mandatory; minimum {{HEDGE_PCT}}% of outstanding principal; tenor {{HEDGE_TENOR}} years |
| Cash Sweep | {{CASH_SWEEP_PCT}}% of excess cash flow above lock-up DSCR of {{LOCKUP_DSCR}}x |
| Prepayment | Permitted with {{PREPAYMENT_NOTICE}} days notice; make-whole during first {{MAKE_WHOLE_YEARS}} years |

---

### 5. FINANCIELE RATIO'S / FINANCIAL COVENANTS

| Covenant | Level | Test Frequency |
|---|---|---|
| Minimum DSCR | {{MIN_DSCR}}x | Semi-annual |
| Lock-up DSCR (distribution test) | {{LOCKUP_DSCR}}x | Prior to each distribution |
| Default DSCR | {{DEFAULT_DSCR}}x | Semi-annual |
| Minimum LLCR | {{MIN_LLCR}}x | Annual |
| Maximum Gearing | {{MAX_GEARING}}% | Semi-annual |

---

### 6. RESERVEREKENINGEN / RESERVE ACCOUNTS

| Account | Required Balance |
|---|---|
| DSRA (Debt Service Reserve Account) | {{DSRA_MONTHS}} months forward debt service |
| Maintenance Reserve | EUR {{MAINT_RESERVE}} or {{MAINT_MONTHS}} months O&M |
| Distribution Reserve | Minimum cash balance EUR {{MIN_CASH}} |
| {{AUGMENTATION_RESERVE (BESS only)}} | EUR {{AUG_RESERVE}} funded from cash flow over {{AUG_YEARS}} years |
| {{GPU_REFRESH_RESERVE (AI only)}} | EUR {{GPU_RESERVE}} funded from cash flow |

---

### 7. ZEKERHEDENPAKKET / SECURITY PACKAGE

- [ ] First-priority pandrecht on all aandelen (shares) in the Borrower
- [ ] First-priority pandrecht on all bankrekeningen (bank accounts) of the Borrower
- [ ] First-priority stille cessie (silent assignment) of all vorderingen (receivables)
- [ ] First-priority hypotheek on recht van opstal / erfpacht (if applicable)
- [ ] First-priority pandrecht on all roerende zaken (movable assets / equipment)
- [ ] First-priority pandrecht on all verzekeringsuitkeringen (insurance proceeds)
- [ ] First-priority pandrecht on all contractuele rechten (project contracts)
- [ ] Assignment of permits (omgevingsvergunning, SDE++ beschikking) to extent legally permissible
- [ ] Direct agreements (step-in rights) with: EPC contractor, O&M provider, offtaker(s), lessor/opstalhouder
- [ ] Parallel debt structure for security agent (zekerheidsagent)

---

### 8. VOORWAARDEN PRECEDENT / CONDITIONS PRECEDENT TO FIRST DRAWDOWN

- [ ] All project agreements executed (EPC, O&M, offtake, land, grid connection, insurance)
- [ ] All permits obtained (omgevingsvergunning -- onherroepelijk; stikstof clearance)
- [ ] Financial model: clean audit opinion from {{MODEL_AUDITOR}}
- [ ] Independent engineer: satisfactory technical due diligence report
- [ ] Legal opinions: Dutch law opinion on enforceability of finance documents and security
- [ ] Insurance: confirmation of placement per agreed insurance programme
- [ ] Security: all security interests created and perfected (registered at Kadaster/KvK as applicable)
- [ ] Equity contribution: minimum {{EQUITY_FIRST_PCT}}% of total equity committed and available
- [ ] KYC/AML: completion of Wwft identification and verification (klantidentificatie)
- [ ] Tax: BTW registration confirmed; advance ruling on earningsstripping (if applicable)
- [ ] Environmental: satisfactory NEN 5725/5740 reports
- [ ] Grid: confirmed aansluit- en transportovereenkomst (ATO) with {{DSO_TSO}}

---

### 9. UITKERINGEN / DISTRIBUTION CONDITIONS

Distributions to shareholders permitted only if ALL of the following are satisfied:

1. No Event of Default or Potential Event of Default is continuing or would result
2. DSCR for the preceding test period >= {{LOCKUP_DSCR}}x
3. Projected DSCR for the next test period >= {{LOCKUP_DSCR}}x
4. DSRA and all reserve accounts fully funded
5. All financial covenants in compliance
6. All insurance in place and current
7. No material adverse change in the Project

---

### 10. EVENTS OF DEFAULT (SELECTIE) / EVENTS OF DEFAULT (SELECTION)

- Non-payment (after {{GRACE_DAYS}} Business Days grace)
- Financial covenant breach (after {{CURE_DAYS}} day cure period)
- Material misrepresentation
- Cross-default (to other indebtedness exceeding EUR {{CROSS_DEFAULT_THRESHOLD}})
- Insolvency events (faillissement, surseance van betaling, WHOA)
- Material adverse change
- Abandonment of the Project
- Permit revocation
- Change of control without lender consent
- Environmental non-compliance (material)

---

### 11. INFORMATIEVERSCHAFFING / INFORMATION UNDERTAKINGS

- Quarterly unaudited management accounts within {{Q_REPORTING}} days
- Annual audited financial statements within {{A_REPORTING}} days (NL GAAP / IFRS)
- Semi-annual compliance certificates
- Annual insurance renewal certificates
- Annual updated financial model
- Prompt notification of: Events of Default, material litigation, permit changes, environmental incidents, material contract amendments

---

### 12. KOSTEN EN VERGOEDINGEN / COSTS AND FEES

- All costs of the Arranger, Agent, legal counsel, IE, model auditor, and insurance adviser payable by the Borrower
- Annual agent fee: EUR {{AGENT_FEE}}
- Annual security agent fee: EUR {{SEC_AGENT_FEE}}
- Amendment/waiver fee: as agreed

---

### 13. TOEPASSELIJK RECHT / GOVERNING LAW AND JURISDICTION

- Governing Law: {{Netherlands law / English law}}
- Dispute Resolution: {{Rechtbank Amsterdam / Arbitration (NAI/ICC) / English courts}}
- Language: {{Dutch / English}}

---

### 14. VERTROUWELIJKHEID / CONFIDENTIALITY

This Term Sheet is confidential and for discussion purposes only. It does not constitute a commitment to lend or an offer of financing. Any commitment is subject to satisfactory completion of due diligence, credit committee approval, and execution of definitive documentation.

---

### 15. GELDIGHEID / VALIDITY

This indicative Term Sheet is valid until {{VALIDITY_DATE}} unless extended in writing.

---

**For and on behalf of {{ARRANGER_NAME}}:**

Name: ____________________________
Title: ____________________________
Date: ____________________________

**Acknowledged by {{SPONSOR_NAME}}:**

Name: ____________________________
Title: ____________________________
Date: ____________________________

---

## Usage Notes

This template covers a standard senior secured project finance term sheet. For specific asset classes, consider:

**BESS additions:**
- Augmentation reserve mechanics
- Battery performance testing regime
- Degradation cure events
- Revenue floor/hedge requirements

**DC additions:**
- Pre-lease conditions (50-70% for construction drawdown)
- Customer concentration limits
- PUE performance covenants
- Expansion option mechanics

**AI Factory additions:**
- GPU refresh reserve mechanics
- Technology obsolescence triggers
- Customer concentration (startup vs IG)
- GPU-as-collateral provisions

---

## Disclaimer

This is a template for educational and illustrative purposes only. It does not constitute juridisch advies, financieringsadvies, or belastingadvies. Engage qualified Dutch legal, financial, and tax advisers for actual transactions. Terms are indicative and non-binding.

---

## Cross-References

- Debt instruments: [references/debt-instruments.md](references/debt-instruments.md)
- Security package (Dutch law): [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md)
- Risk allocation: [references/risk-allocation.md](references/risk-allocation.md)
- Due diligence: [references/due-diligence-checklist.md](references/due-diligence-checklist.md)
