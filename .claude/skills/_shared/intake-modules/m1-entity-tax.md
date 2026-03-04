# M1: Entity & Corporate Structure + Tax Structuring

**Module metadata:**
- Questions: 37 (S1: 12, S2: 25)
- Priority: P0 (S1.1-S1.9, S2.1-S2.6) · P1 (S1.10-S1.12, S2.7-S2.19) · P2 (S2.20-S2.25)
- Track: `[BOTH]` — always loaded for both seed and PF
- Feeds: `SF` `PF` `LC` `DR` `NP`
- Dependencies: None
- Parallel track: B (Entity)
- Mini-deliverable trigger: After M1 complete → **Corporate Structure Summary** (2 pages)

---

## Section 1: Entity & Corporate Structure

### 1.1 Holding Entity
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

Holding company details:
- Legal name and form (e.g., AG, GmbH, BV, Ltd, Corp)
- Jurisdiction of incorporation
- Date of incorporation
- Registered office address
- Commercial register number (e.g., KvK, Handelsregister, Companies House)
- LEI (Legal Entity Identifier) if obtained

---

### 1.2 Operating Entities
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

List all operating entities (subsidiaries, SPVs, JVs):
- Legal name, form, and jurisdiction for each
- Ownership percentage held by holding entity
- Purpose of each entity (e.g., project SPV for Site 1, IP holding, employment entity)
- Any minority shareholders or joint venture partners in each entity

---

### 1.3 Corporate Structure Diagram
`DOC` | `P0` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `SF` `PF` `LC` `DR`

Provide or create a corporate structure diagram showing:
- All entities and their jurisdiction
- Ownership lines with percentages
- Intercompany flows (management fees, IP royalties, intercompany loans)
- Any planned future entities (e.g., project SPVs not yet formed)

**Gate:** Structure diagram must be complete and current. If entities are planned but not yet formed, show as dashed lines.

---

### 1.4 Articles of Association
`DOC` | `P0` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `SF` `LC` `DR`

For each entity, provide current articles:
- Share capital structure (number of shares, nominal value, share classes)
- Transfer restrictions (e.g., Vinkulierung for Swiss AG, blokkeringsregeling for Dutch BV)
- Board composition and appointment rules
- General meeting requirements (quorum, voting thresholds)
- Dividend and distribution provisions

**Gate:** Articles must be current (latest version). If share classes exist, each class must be documented with rights attached.

---

### 1.5 Shareholders' Agreement
`DOC` | `P0` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `SF` `LC` `DR`

If a SHA exists:
- Parties to the agreement
- Key provisions: vesting, transfer restrictions, pre-emption rights, drag-along/tag-along, board seats, reserved matters, non-compete, information rights
- Expiry or termination provisions
- Any amendments since execution

If no SHA exists: state this explicitly. For seed fundraising, a SHA will typically be required as part of the round.

---

### 1.6 Cap Table
`DOC` | `P0` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `SF` `LC` `DR`

Current cap table (fully diluted):
- Each shareholder: name, share class, number of shares, percentage
- ESOP/option pool: size (% of fully diluted), granted vs. available
- Existing SAFEs, convertible notes, or warrants: terms, conversion mechanics
- Any anti-dilution provisions already in effect

**Gate:** Cap table must sum to exactly 100% on a fully diluted basis (including all convertible instruments at their caps).

---

### 1.7 Share Register
`DOC` | `P0` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `LC` `DR`

Official share register:
- Maintained by: company, notary, or third-party service?
- Current and reconciled with articles?
- All transfers properly recorded?
- Any shares pledged or encumbered?

---

### 1.8 Board & Governance
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `LC`

Current governance structure:
- Board members: name, role, appointment date, term
- Board meeting frequency and format
- Management (Geschäftsführung / bestuur): who has signatory authority?
- Any advisory board members? Role and engagement terms?

---

### 1.9 UBO & Beneficial Ownership
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `LC` `DR`

Ultimate Beneficial Owner (UBO) compliance:
- UBO filing current in each jurisdiction? (e.g., UBO-register Netherlands, Transparenzregister Germany/Switzerland)
- All UBOs identified (>25% direct or indirect ownership, or significant control)?
- Any PEP (Politically Exposed Person) status among UBOs?

**Gate:** UBO filings must be current. Non-compliance is a deal-stopper for regulated investors.

---

### 1.10 Related-Party Transactions
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `LC` `PF`

List all related-party transactions:
- Intercompany services (management fees, shared services, secondments)
- Intercompany loans (amount, rate, tenor, arm's length basis)
- Founder transactions (loans to/from company, personal guarantees, asset transfers)
- Any transactions with entities owned by shareholders, board members, or their families

**Gate:** All related-party transactions must be documented and at arm's length. Undisclosed related-party transactions that surface in DD are highly damaging.

---

### 1.11 Pending Corporate Actions
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `LC`

Any pending or planned corporate actions:
- Share issuances, splits, or consolidations
- Entity formations (new SPVs, holding restructuring)
- Mergers, acquisitions, or disposals
- Liquidations or strike-offs of dormant entities
- Amendments to articles or SHA

---

### 1.12 Litigation & Disputes
`ANS` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `LC` `DR`

Any current or threatened litigation, arbitration, or regulatory proceedings?
- Parties, jurisdiction, subject matter, amount at stake
- Status (pre-action, filed, in discovery, trial scheduled)
- Legal counsel engaged? Opinion on merits?
- Any settlements or judgments in the past 3 years?

**Gate:** Full disclosure mandatory. Non-disclosure of material litigation discovered in DD is a trust-destroying event.

---

### Section 1 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| All entities registered and in good standing | P0 | [ ] |
| Corporate structure diagram complete | P0 | [ ] |
| Share register sums to 100% (fully diluted) | P0 | [ ] |
| UBO filings current for all entities | P0 | [ ] |
| Board validly constituted | P0 | [ ] |
| Articles current for all entities | P1 | [ ] |
| Substance demonstrated for holding jurisdiction | P1 | [ ] |
| SHA or investor agreements documented | P1 | [ ] |
| Related-party transactions documented | P1 | [ ] |

---

## Section 2: Tax Structuring & Treaty Benefits

### 2.1 Jurisdictional Rationale
`ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

Why was each jurisdiction chosen for each entity?
- Holding entity jurisdiction: tax benefits, treaty network, reputation, regulatory requirements
- Operating entity jurisdiction(s): proximity to assets, local law requirements, tax efficiency
- Was tax counsel involved in the structuring decision? Provide the name of the advising firm.

**Gate:** Jurisdictional choice must have a documented rationale beyond tax minimization. Substance requirements must be addressed.

---

### 2.2 Double Tax Treaty Benefits
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

Identify applicable double tax treaties between holding and operating jurisdictions:
- Treaty name and effective date
- Dividend withholding tax rate under treaty (vs. domestic rate)
- Interest withholding tax rate under treaty
- Royalty withholding tax rate under treaty
- Capital gains treatment under treaty
- Limitation on Benefits (LOB) clause: does the structure qualify?

---

### 2.3 Withholding Tax Optimization
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

For each intercompany payment flow (dividends, interest, royalties, management fees):
- Source jurisdiction and applicable WHT rate (domestic)
- Treaty-reduced rate (if applicable)
- EU Parent-Subsidiary Directive or Interest/Royalty Directive applicability
- Net effective WHT after all reliefs
- Annual estimated WHT cost (EUR)

---

### 2.4 Participation Exemption
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

Does the holding entity qualify for a participation exemption on:
- Dividends received from subsidiaries?
- Capital gains on disposal of subsidiaries?
- Requirements: minimum ownership percentage, holding period, active business test, or similar
- Jurisdiction-specific rules (e.g., Netherlands deelnemingsvrijstelling requires >5% ownership; Swiss Beteiligungsabzug requires >10% or CHF 1M FMV)

**Gate:** Participation exemption qualification must be confirmed or assessed. Non-qualification changes the effective tax rate materially.

---

### 2.5 Substance Requirements
`ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

For the holding entity jurisdiction, demonstrate economic substance:
- Physical office presence (not just a registered agent)
- Qualified employees in jurisdiction (number, roles)
- Board meetings held in jurisdiction (frequency, location, minutes)
- Strategic decisions made from jurisdiction (evidence)
- Bank accounts in jurisdiction
- ATAD (EU Anti-Tax Avoidance Directive) compliance if applicable

**Gate:** Substance requirements must be demonstrably met. If using a jurisdiction with substance rules (EU members, Switzerland), provide evidence of real economic activity.

---

### 2.6 Conditional WHT Risk
`ANS` | `P0` | `[BINARY]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

Is there a risk of conditional withholding tax on dividends, interest, or royalties?
- Does any jurisdiction impose conditional WHT on payments to low-tax jurisdictions?
- Are any group entities in jurisdictions on EU/OECD blacklists or graylists?
- Would a restructuring trigger WHT on deemed distributions?

---

### 2.7 Transfer Pricing Policy
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `LC`

Transfer pricing for intercompany transactions:
- Transfer pricing policy documented?
- Methods used (CUP, TNMM, cost-plus, profit split)
- Key intercompany transactions: management fees, IP royalties, intercompany loans, service agreements
- Arm's length basis demonstrated for each transaction
- TP documentation file (Master File / Local File) prepared?

**Gate:** If intercompany transactions exist, TP documentation is mandatory in most jurisdictions. Absence is a tax audit risk.

---

### 2.8 Intercompany Loans
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

For each intercompany loan:
- Lender, borrower, amount (EUR), currency
- Interest rate and basis (fixed/floating, reference rate + margin)
- Arm's length interest rate benchmark
- Tenor and repayment schedule
- Subordination or priority ranking
- Earningsstripping / thin cap impact (if applicable)

---

### 2.9 IP Ownership & Location
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `LC`

Where is IP held and why?
- IP holding entity and jurisdiction
- Type of IP (software, patents, trade secrets, know-how, brand)
- IP development activity: DEMPE functions (Development, Enhancement, Maintenance, Protection, Exploitation) — where do they occur?
- IP licensing arrangements to operating entities
- Innovation box or patent box regime applicability

---

### 2.10 Permanent Establishment Risk
`ANS` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `LC`

Is there a risk of creating a permanent establishment (PE) in any jurisdiction?
- Do founders or employees work in a jurisdiction where no entity exists?
- Are contracts negotiated or concluded in a jurisdiction other than the entity's jurisdiction?
- Is there a fixed place of business (office, warehouse, construction site) in an unplanned jurisdiction?
- Agent PE risk: does anyone habitually conclude contracts on behalf of a foreign entity?

---

### 2.11 VAT / GST Treatment
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

VAT treatment per revenue stream:
- Which revenue streams are subject to VAT? At what rate?
- Which are exempt or zero-rated?
- Input VAT recovery: can construction VAT be fully recovered?
- VAT registration status per entity per jurisdiction
- Cross-border supply of services: reverse charge applicable?
- Construction-phase VAT: timing mismatch between input VAT paid and output VAT received — impact on cash flow

---

### 2.12 Earningsstripping / Interest Limitation
`ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF` `LC`

If applicable in the operating entity's jurisdiction:
- Earningsstripping threshold (e.g., 24.5% of fiscal EBITDA in Netherlands + EUR 1M franchise)
- Current and projected net interest expense per entity
- Does net interest exceed the threshold? In which years?
- Impact on effective tax rate and cash flow
- Grouping election available? (e.g., Dutch fiscal unity / fiscale eenheid)

**Gate:** If debt financing is planned, earningsstripping impact MUST be modeled. Non-deductible interest directly reduces post-tax cash flow and DSCR.

---

### 2.13 Fiscal Unity / Group Taxation
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

Is a fiscal unity or group taxation election in place or planned?
- Which entities are / will be included?
- Requirements met (e.g., >95% ownership for Dutch fiscale eenheid)?
- Tax consequences of formation (deemed asset transfers, intercompany settlements)
- Impact on earningsstripping calculation (group-level vs. entity-level)

---

### 2.14 Corporate Income Tax Rates
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

Current and projected CIT rates per entity jurisdiction:
- Standard rate and any reduced rates (e.g., Netherlands: 19% on first EUR 200K, 25.8% above)
- Innovation box or patent box rate (if applicable)
- Effective tax rate after reliefs and deductions
- Known upcoming rate changes

---

### 2.15 Loss Carry-Forward
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

Tax loss position per entity:
- Accumulated tax losses (EUR)
- Carry-forward period and limitations (e.g., Netherlands: unlimited forward, 1 year back; limited to EUR 1M + 50% of taxable profit above EUR 1M)
- Risk of loss forfeiture on change of control (shareholding test)
- Impact of funding round on loss utilization

---

### 2.16 Real Estate Transfer Tax
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

If entities hold or will acquire real estate:
- Transfer tax rate on direct real estate acquisition (e.g., Netherlands: 10.4% for non-residential)
- Share deal vs. asset deal: does a share transfer trigger transfer tax? (e.g., Dutch BV with >30% real estate assets: share transfer may be deemed real estate transfer)
- Exemptions available (restructuring exemption, group exemption)
- Impact on exit planning: share sale tax cost

---

### 2.17 Subsidy & Grant Tax Treatment
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP`

For any subsidies or grants received or expected:
- Taxable or tax-exempt?
- Impact on CIT calculation
- Clawback provisions (does failure to meet conditions trigger tax liability?)
- SDE++, ISDE, EIA, MIA/VAMIL or equivalent in your jurisdiction — tax treatment of each

---

### 2.18 Withholding on Exit
`ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

Tax treatment of exit proceeds:
- Share sale by holding entity: capital gains tax rate?
- Participation exemption on disposal gains?
- Transfer tax on share sale (if real estate heavy entities)?
- Tax treaty benefits on exit proceeds distribution to shareholders?
- Estimated net-of-tax exit proceeds as % of gross proceeds

---

### 2.19 Tax Ruling or Advance Pricing Agreement
`ANS` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `LC`

Has a tax ruling or advance pricing agreement been sought?
- If yes: jurisdiction, subject matter, ruling obtained? Validity period?
- If no: is one planned? For which aspects of the structure?
- Cost and timeline estimate for obtaining a ruling

---

### 2.20-2.25 Deep Tax (P2)

**2.20** Tax due diligence scope: what does a buyer's tax DD team need to review? List all open tax positions, pending assessments, and uncertain tax treatments. `ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `LC` `DR`

**2.21** Tax indemnity: what tax indemnities will the company provide to investors? Scope, duration, cap? `ANS` | `P2` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `LC`

**2.22** Tax authority audit history: any prior tax audits? Outcomes? Outstanding disputes? `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `LC`

**2.23** Pillar Two / Global Minimum Tax: does the group exceed EUR 750M revenue threshold? If growth trajectory reaches this threshold, when? Impact of 15% minimum effective tax rate? `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `LC`

**2.24** DAC6 / MDR reporting: any reportable cross-border arrangements under DAC6 (EU) or equivalent mandatory disclosure regime? `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `LC`

**2.25** Exit tax planning: model the tax cost of each exit scenario (trade sale at holdco level, share sale at SPV level, asset sale, IPO). Which structure minimizes total tax on exit? `CAL` | `P2` | `[EXACT]` | `[SEED]` | Feeds: `SF` `PF` `LC`

---

### Section 2 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| Jurisdictional rationale documented | P0 | [ ] |
| Treaty benefits identified and quantified | P0 | [ ] |
| Substance requirements demonstrated | P0 | [ ] |
| WHT on each intercompany flow quantified | P0 | [ ] |
| Participation exemption qualification assessed | P0 | [ ] |
| Conditional WHT risk assessed | P0 | [ ] |
| TP policy documented (if intercompany transactions) | P1 | [ ] |
| Earningsstripping impact modeled (if debt planned) | P1 | [ ] |
| VAT treatment per revenue stream confirmed | P1 | [ ] |
| Exit tax treatment assessed | P2 | [ ] |

**Critical flag:** If tax counsel has not reviewed the structure → **"Tax structuring without professional advice risks costly errors. Engage tax counsel before investor conversations."**
