# Question-Deliverable Map

Traceability matrix showing which questions feed each deliverable section. Ensures every question is outcome-mapped and every deliverable section has source questions.

---

## Deliverable 1: Lead Qualification Score

| Scoring Factor | Primary Source Questions | Secondary Sources |
|---------------|------------------------|-------------------|
| Capacity/Grid value | Q3.1, Q2.1, Q2.5-NEO (power density), Q3.4-GRW (grid), Q3.5-DHN (baseload), Q2.5-IND (energy mix) | Research (company size, funding) |
| Timeline match | Q3.2, Q0.4 (meeting status), Q2.2 (trigger), Q2.6-GRW (WKK status), Q4.4-ENT (budget authority) | CRM (last activity, deal stage) |
| Technical fit | Q3.1, Q3.3, Q2.5-NEO (workload), Q2.6-NEO (density), Q3.4-ENT (hybrid arch), Q3.6-GRW (heat profile), Q3.4-DHN (supply temp), Q2.6-IND (process temp) | Research (current infra) |
| Budget/Price fit | Q4.1, Q4.4-NEO (price benchmarks), Q2.5-ENT (cloud spend), Q4.4-INS (budget model), Q2.5-GRW (gas costs), Q2.8-DHN (heat price), Q4.4-IND (energy budget) | Research (public financials) |
| Decision authority | Q4.2, Q1.2 (key contact), Q1.5-ENT (IT decision structure), Q1.5-GRW (ownership), Q1.5-DHN (governance), Q4.5-IND (procurement) | CRM (contact role) |
| Strategic driver | Q5.2, Q2.7-NEO (EU driver), Q2.6-ENT (sovereignty), Q2.7-ENT (cloud exit), Q2.7-GRW (sustainability), Q2.6-DHN (Wcw gap), Q1.5-IND (ESG targets) | Research (ESG reports, strategy) |
| Founder assessment | Q5.4, Q5.3, Q0.6 | Founder intuition |

---

## Deliverable 2: Opportunity Brief

| Brief Section | Primary Source Questions | ICP-Specific Additions |
|--------------|------------------------|----------------------|
| 1. Company Profile | Q1.1, Q0.1 | Q1.4-NEO (funding), Q1.4-ENT (AI maturity), Q1.4-INS (type), Q1.4-GRW (farm profile), Q1.4-DHN (network profile), Q1.4-IND (industry) |
| 2. Key People | Q1.2, Q0.6 | Q1.5-ENT (IT decision structure), Q1.5-DHN (governance) |
| 3. What They Need | Q2.1, Q3.1 | Q2.5-NEO (workload), Q2.6-NEO (density), Q2.8-ENT (workload), Q2.5-GRW (gas costs), Q2.7-DHN (expansion), Q2.6-IND (process temp) |
| 4. Why Now (Trigger) | Q2.2, Q5.2 | Q2.7-NEO (EU driver), Q2.6-ENT (sovereignty), Q2.7-ENT (cloud exit), Q2.6-GRW (WKK status), Q2.6-DHN (Wcw gap), Q2.7-IND (cost pressure) |
| 5. How We Fit | Q3.1, Q3.2, Q3.3, Q2.1 | Q3.4-NEO (deployment model), Q3.4-GRW (grid), Q3.5-GRW (location), Q3.6-DHN (connection), Q3.6-IND (proximity) |
| 6. Positioning Angle | Q5.2, Q2.2 | Per icp-profiles.md messaging pillars |
| 7. Competitive Landscape | Q2.3, Q5.1 | Per icp-profiles.md competitive set. Q1.5-NEO (footprint), Q2.5-ENT (cloud spend), Q2.7-INS (SURF), Q2.7-GRW (sustainability), Q2.5-DHN (sources) |
| 8. Obstacles & Risk | Q5.3, validation red flags | Q1.5-GRW (ownership), Q3.7-GRW (zoning), Q3.8-GRW (fiber), Q3.8-DHN (redundancy), Q3.5-IND (process risk) |
| 9. Commercial Parameters | Q4.1, Q4.2, Q4.3, Q3.2 | Q4.4-NEO (benchmarks), Q4.5-NEO (contract), Q4.5-ENT (procurement), Q4.6-ENT (TCO frame), Q4.4-GRW (ground rent), Q4.5-DHN (duration), Q4.4-IND (budget) |
| 10. Recommended Actions | Derived from all above | ICP-specific skill routing from SKILL.md section 12 |

---

## Deliverable 3: Pre-Meeting Prep

| Prep Section | Primary Source Questions | Research Inputs |
|-------------|------------------------|-----------------|
| Background | Q0.1, Q1.1, Q0.2, Q0.6, Q1.3 | Company website, news, CRM history |
| Their Likely Priorities | Q2.1, Q2.2, Q5.2 | ICP pain points from icp-profiles.md |
| Our Talking Points | Q2.1, Q3.1, Q4.1, Q5.2 | ICP messaging pillars from icp-profiles.md |
| Questions They Will Ask | Q5.1, Q2.3 | ICP objections from icp-profiles.md |
| Questions We Should Ask | Gap list from Phase 0 processing | Remaining unanswered questions |
| Collateral to Prepare | Q2.1 (need type), Q0.3 (ICP) | ICP collateral refs from icp-profiles.md |
| Meeting Objective | Q2.2 (trigger), Q3.2 (timeline), Q4.2 (decision process) | Overall qualification score |

---

## Deliverable 4: HubSpot Contact/Deal Creation

| CRM Field | Source Question | Notes |
|-----------|---------------|-------|
| Contact: firstname | Q0.1 | |
| Contact: lastname | Q0.1 | |
| Contact: email | Q0.1, Q0.5 | May come from materials |
| Contact: phone | Q0.1, Q0.5 | |
| Contact: company | Q0.1, Q1.1 | |
| Contact: jobtitle | Q1.2 | |
| Contact: hs_lead_status | Derived from score | active / cold |
| Contact: hubspot_owner_id | Q0.6 (founder context) | Which founder owns this |
| Company: name | Q0.1, Q1.1 | |
| Company: domain | Q0.1 | From email or website |
| Company: industry | Q1.1, Q1.4-* | ICP-specific |
| Company: city | Q3.3, Q1.4-GRW | Location from intake or research |
| Deal: dealname | Q0.1, Q0.3 | Format: `[Company] - [Type]` |
| Deal: pipeline | Q0.3 | Sales (Colocation) / Project (Site) |
| Deal: dealstage | Derived | Lead (Colocation) / Identified (Site) |
| Deal: amount | Q4.1, Q3.1 | Estimated from capacity/scale |
| Deal: closedate | Q3.2, Q4.2 | From timeline + decision process |
| Deal: description | Summary | Auto-generated from Opportunity Brief |

---

## Deliverable 5: Recommended Next Actions

| Action Category | Source Questions | Routing Logic |
|----------------|----------------|---------------|
| Immediate follow-up | Q0.4 (meeting status), Q3.2 (timeline) | If meeting scheduled → `ops-meetingops` |
| Collateral preparation | Q0.3 (ICP), Q2.1 (need) | ICP-specific collateral → `collateral-studio` |
| Outreach | Q0.3 (ICP), Q1.2 (contact) | ICP-specific sequence → `ops-outreachops` |
| Legal preparation | Q4.3 (contract), Q0.3 (ICP) | ICP-specific document → `legal-counsel` |
| Deep research | Q0.1 (company), gaps | `ops-targetops` for research dossier |
| Permitting assessment | Q3.3 (location), Q3.7-GRW (zoning) | Site Track only → `netherlands-permitting` |
| CRM entry | All contact/company data | `ops-dealops` for tracking |
| Narrative check | Q5.2 (positioning angle) | `ops-storyops` for consistency |

---

## Deliverable 6: Waitlist Entry

| Entry Section | Source Questions |
|--------------|----------------|
| Company/Contact | Q0.1, Q1.1, Q1.2 |
| Disqualification Reason | Score breakdown, red flags from validation |
| What We Know | All collected answers (abbreviated) |
| Revisit Trigger | Q2.2 (trigger), Q3.2 (timeline), specific red flag mitigation |
| HubSpot Action | Q0.1 (identity), Q0.3 (ICP for pipeline), revisit date |

---

## Coverage Matrix

Verify every question feeds at least one deliverable:

| Question | D1 Score | D2 Brief | D3 Prep | D4 HubSpot | D5 Actions | D6 Waitlist |
|----------|----------|----------|---------|------------|------------|-------------|
| Q0.1 | - | S1 | BG | Contact | - | Contact |
| Q0.2 | Source | S1 | BG | - | - | - |
| Q0.3 | ICP | Track | Track | Pipeline | Routing | Pipeline |
| Q0.4 | - | - | Mode | - | Priority | - |
| Q0.5 | - | Multiple | Multiple | Multiple | - | - |
| Q0.6 | Founder | S1,S4 | BG | Owner | - | - |
| Q1.1 | - | S1 | BG | Company | - | Company |
| Q1.2 | Decision | S2 | Attendees | Contact | - | Contact |
| Q1.3 | - | S1 | BG | - | - | - |
| Q2.1 | Capacity | S3 | Priorities | Amount | Collateral | - |
| Q2.2 | Timeline | S4 | Why Now | - | Priority | Trigger |
| Q2.3 | - | S7 | Competitive | - | - | - |
| Q2.4 | Timeline | S4 | - | - | Priority | - |
| Q3.1 | Capacity | S3,S5 | Tech | Amount | - | - |
| Q3.2 | Timeline | S5,S9 | Objective | CloseDate | Priority | Revisit |
| Q3.3 | - | S5 | - | City | Permitting | - |
| Q4.1 | Budget | S9 | Economic | Amount | - | - |
| Q4.2 | Decision | S2,S9 | Stakeholders | - | - | - |
| Q4.3 | - | S9 | - | - | Legal | - |
| Q5.1 | - | S7 | Q&A | - | - | - |
| Q5.2 | Strategic | S4,S6 | Talking Pts | - | Narrative | - |
| Q5.3 | Red Flags | S8 | - | - | - | Reason |
| Q5.4 | Founder | Rec | - | - | - | - |

D = Deliverable, S = Section, BG = Background
