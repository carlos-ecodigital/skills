
| DRAFTER: Follow these steps before issuing |
| :---- |
| 1. Fill the Parameter Table below |
| 2. Find-and-replace each [PLACEHOLDER] in the body |
| 3. Choose: IF: PRICING or IF: NO_PRICING (Cl. 3.5) — delete unused |
| 4. Choose: IF: PHASING or delete (Cl. 3.3) |
| 5. Choose: ALT-A or ALT-B for Confidentiality (Cl. 6) — delete unused |
| 6. Confirm [PLATFORM_MW] and [SITE_COUNT] with CPO/CEO. State MW IT, not MVA |
| 7. Delete all shaded instruction blocks. Verify no [BRACKETS] remain |
| 8. Result: 6-7 pages |

---

## Parameter Table

### Provider

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [DE:LEGAL_NAME] | Digital Energy Netherlands B.V. | Letterhead, Cl. 1, Signature |
| [DE:SHORT_NAME] | Digital Energy | Cl. 1 (defined as "the Provider") |
| [DE:ADDRESS] | [Registered address] | Letterhead |
| [DE:KVK] | [KvK number] | Letterhead, Signature |
| [DE:PARENT] | Digital Energy Group AG (CHE-408.639.320) | Cl. 1 (parent reference) |
| [DE:SIGNATORY_NAME] | | Signature |
| [DE:SIGNATORY_TITLE] | | Signature |

### Customer

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [CUSTOMER_NAME] | | Addressee, Cl. 1, Signature |
| [CUSTOMER_SHORT] | | Cl. 1 (defined as "the Customer") |
| [CUSTOMER_ADDRESS] | | Addressee |
| [CUSTOMER_JURISDICTION] | | Cl. 1 |
| [CUSTOMER_REG_TYPE] | | Signature (e.g., "KvK", "Company No.", "EIN") |
| [CUSTOMER_REG_NUMBER] | | Signature |
| [CUSTOMER_CONTACT_NAME] | | Attention line |
| [CUSTOMER_CONTACT_TITLE] | | Attention line |
| [CUSTOMER_SALUTATION] | | Dear line |
| [CUSTOMER_SIGNATORY_NAME] | | Signature |
| [CUSTOMER_SIGNATORY_TITLE] | | Signature |
| [CUSTOMER_DESCRIPTION] | | Cl. 1.2 — brief description incl. credit indicators |

### Capacity

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [INDICATIVE_MW] | | Cl. 3.1 — total IT load (MW) |
| [DEC_BLOCK_COUNT] | | Cl. 3.1 — number of DEC Blocks |
| [EXPANSION_MW] | | Cl. 3.4 — future expansion target (MW IT) |
| [MIN_TERM] | | Cl. 3.6 — minimum commitment (e.g., 5 years) |
| [PLATFORM_MW] | | Recital (A) — programme IT capacity target |
| [SITE_COUNT] | | Recital (A) — number of identified sites |

### Phasing (if applicable)

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [PHASE_1_MW] | | Cl. 3.3 |
| [PHASE_1_TIMELINE] | | Cl. 3.3 |
| [PHASE_2_MW] | | Cl. 3.3 |
| [PHASE_2_TIMELINE] | | Cl. 3.3 |

### Commercial

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [BASE_PRICE] | | Cl. 3.5 pricing table |
| [TERM_YEARS] | | Cl. 3.5 pricing table |
| [TARGET_RFS_DATE] | | Cl. 3.5 pricing table |
| [RAMP_SCHEDULE] | | Cl. 3.5 pricing table |

### Protection

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [NC_DURATION] | 24 months (default) | Cl. 7.2 |
| [CONFIDENTIALITY_SURVIVAL] | 3 years (default) | Cl. 6.14 |

### Dates

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [LOI_DATE] | | Letterhead |
| [VALIDITY_DATE] | | Cl. 8.3 |
| [NDA_DATE] | | Cl. 6 ALT-A (if existing NDA) |

---

**Digital Energy Netherlands B.V.**

[DE:ADDRESS]

KvK: [DE:KVK]

Date: [LOI_DATE]

**PRIVATE AND CONFIDENTIAL**

To:

[CUSTOMER_NAME]

[CUSTOMER_ADDRESS]

Attention: [CUSTOMER_CONTACT_NAME], [CUSTOMER_CONTACT_TITLE]

Dear [CUSTOMER_SALUTATION],

**Re: Letter of Intent and Non-Circumvention Non-Disclosure Agreement — Purpose-Built AI Colocation Capacity**

---

## Recitals

(A) [DE:SHORT_NAME] (the "**Provider**") develops and operates Digital Energy Centers ("**DECs**"): purpose-built, liquid-cooled colocation facilities designed for high-density accelerated compute workloads. DECs integrate AI compute with energy recycling and generation. The Provider's programme spans [SITE_COUNT] identified sites with secured energy and grid access, positioning its platform as one of the leading sovereign AI infrastructure programmes capable of delivering capacity at scale within 12 months of commercial commitment.

(B) [CUSTOMER_SHORT] (the "**Customer**") [CUSTOMER_DESCRIPTION].

(C) The Parties wish to record their mutual interest in the Provider making available, and the Customer procuring, dedicated AI colocation capacity at the Provider's DEC facilities, on the indicative terms set out below. This letter of intent and non-circumvention non-disclosure agreement (the "**LOI**") reflects both Parties' strategic intent to establish a long-term infrastructure partnership and is intended to form the basis for further technical scoping and commercial negotiation toward a Master Services Agreement (the "**MSA**").

(D) The Parties recognise that the commercial discussions contemplated by this LOI will require the exchange of commercially sensitive information, including site-specific data, pricing models, and infrastructure specifications, and wish to establish binding confidentiality and non-circumvention protections to facilitate those discussions.

---

## 1. Definitions

1.1 In this LOI, unless the context requires otherwise:

"**Affiliate**" means, in relation to a Party, any entity that directly or indirectly controls, is controlled by, or is under common control with that Party, where "control" means the ownership of more than 50% of the voting rights or equivalent ownership interest;

"**Associated Counterparty**" means, in relation to a Site Identifier, any of the following with whom the Provider has a contractual, commercial, or active non-public engagement in connection with that site: (a) landowners and land lessors; (b) greenhouse operators and agricultural partners; (c) heat offtake counterparties; (d) energy procurement counterparties; (e) engineering, procurement, and construction contractors engaged or under negotiation; and (f) grid connection holders and distribution system operators (to the extent of non-public engagement). For the avoidance of doubt, government agencies and regulatory bodies are excluded unless the Provider has made a specific named introduction;

"**Business Day**" means a day other than a Saturday, Sunday, or public holiday in the Netherlands;

"**Confidential Information**" means all information (whether technical, commercial, financial, or otherwise) disclosed by a Party to the other in connection with the Purpose, whether in writing, orally, electronically, or by inspection, including any information that by its nature or the circumstances of disclosure would reasonably be understood to be confidential, and including metadata, EXIF data, digital artifacts, file names, folder names, and any derivative information. The existence and contents of this LOI are Confidential Information;

"**DEC**" means a Digital Energy Center: a purpose-built colocation facility developed and operated by the Provider;

"**DEC Block**" means a standardised compute unit of approximately 1.2 MW IT capacity, factory-manufactured and modular;

"**Financing Party**" means any bank, financial institution, fund, security trustee, or other entity providing or arranging debt, mezzanine, or structured finance to the Provider or any of its Affiliates in connection with the development or operation of any DEC;

"**MSA**" means the definitive Master Services Agreement to be negotiated between the Parties, incorporating the Sales Order Form, SLA Schedule, and Pricing Framework;

"**Purpose**" means evaluating, negotiating, and progressing toward the execution of an MSA for the provision of AI colocation services;

"**Ready-for-Service**" or "**RFS**" means the date on which a DEC or DEC Block has been commissioned and is available for the provision of colocation services;

"**Representatives**" means, in relation to a Party, its Affiliates, and its and their respective directors, officers, employees, agents, and professional advisers;

"**Sales Order Form**" means the document that will form the basis for each binding service order under the MSA, setting out confirmed capacity, pricing, site allocation, and RFS date;

"**Services**" means the AI colocation services to be provided by the Provider, comprising power supply and distribution, liquid cooling infrastructure, physical security, building management, and facility operations;

"**Site Identifier**" means any information that identifies or could reasonably be used to identify a specific DEC location, including: address, GPS coordinates, cadastral reference, project codename, photographs, aerial imagery, file names, folder names, metadata, and any information derived from the foregoing;

"**Whitespace**" means designated floor area within a DEC available for the deployment of IT hardware and supporting infrastructure.

---

## 2. Purpose and Scope

2.1 This LOI records the Parties' mutual interest in the Customer procuring dedicated AI colocation capacity at the Provider's DEC facilities, on the indicative terms set out in Clauses 3 and 4.

2.2 The Parties intend this LOI to provide the basis for technical scoping and commercial negotiation toward a definitive MSA. The commercial terms in Clauses 3 and 4 are non-binding expressions of intent.

2.3 The confidentiality, non-circumvention, and general provisions in Clauses 5 through 8 are legally binding and enforceable from the date of execution.

---

## 3. Indicative Capacity and Commercial Terms (NON-BINDING)

3.1 **Capacity Requirement.** The Customer has indicated interest in approximately **[DEC_BLOCK_COUNT] DEC Blocks ([INDICATIVE_MW] MW IT)** of purpose-built AI colocation capacity. Capacity is provisioned in whole DEC Block increments of 1.2 MW IT each; partial requirements are rounded up to the nearest full DEC Block.

3.2 **Technical Specification.** All DEC facilities are designed for high-density AI compute workloads and are expected to include, at minimum: facility power supply and distribution, direct liquid cooling infrastructure supporting rack densities of 40 kW and above, building management, physical security, and 24/7 facility operations. The exact capacity, rack configuration, power density, and cooling requirements will be determined during the technical scoping phase following this LOI.

| IF: PHASING — include if customer has phasing needs |
| :---- |

3.3 **Deployment Phasing.** The Customer has indicated the following high-level phasing interest:

| Phase | Approximate Capacity | Indicative Timeline |
| :---- | :---- | :---- |
| Phase 1 | [PHASE_1_MW] MW IT | [PHASE_1_TIMELINE] |
| Phase 2 | [PHASE_2_MW] MW IT | [PHASE_2_TIMELINE] |

*/IF: PHASING*

3.4 **Expansion.** The Customer has expressed interest in future expansion to approximately **[EXPANSION_MW] MW IT**, subject to availability, commercial agreement, and the terms of the MSA. The Provider will use reasonable endeavours to accommodate expansion requirements within its DEC programme.

3.5 **Indicative Pricing.**

| IF: PRICING — include if indicative pricing has been discussed |
| :---- |

Based on the Customer's indicated capacity and term preferences, the Provider's indicative pricing is as follows:

| Parameter | Indicative Terms |
| :---- | :---- |
| **Base colocation fee** | EUR [BASE_PRICE] per kW per month |
| **Contract term** | [TERM_YEARS] years |
| **Power** | Metered IT Load (kWh) x PUE x Energy Rate (EUR/kWh) — billed additionally |
| **Price escalation** | Subject to annual escalation, the mechanism for which will be agreed in the MSA |
| **Indicative RFS** | [TARGET_RFS_DATE] |
| **Ramp schedule** | [RAMP_SCHEDULE] |

All commercial terms are indicative and subject to the outcome of the technical scoping phase, the Customer's final capacity requirements, contract term, and credit profile.

*/IF: PRICING*

| IF: NO_PRICING — select if pricing is deferred |
| :---- |

Pricing for the Services will be determined following the technical scoping phase and set out in the Sales Order Form. The Provider will provide indicative pricing upon completion of the Customer's capacity, density, and term requirements.

*/IF: NO_PRICING*

3.6 **Term and Commitment.** The Customer has indicated willingness to enter into a minimum commitment term of **[MIN_TERM]** under the MSA. The Customer acknowledges that the Provider intends the MSA to include take-or-pay provisions commensurate with the committed capacity, the terms of which will be negotiated in good faith.

3.7 **Credit Assessment.** The Provider will complete a credit assessment of the Customer (or the entity that will execute the MSA) as part of the commercial process. The Customer agrees to cooperate with such assessment, which may include provision of audited financial statements, credit references, evidence of parent company support, or other financial information as reasonably requested. Where the Customer does not hold an investment-grade credit rating (or equivalent), the Parties will discuss appropriate credit support mechanisms, which may include a parent company guarantee, security deposit, or letter of credit.

3.8 **Site Allocation.** The Provider is developing DEC facilities across multiple locations. The Provider will allocate capacity to the Customer based on the DEC(s) best suited to the Customer's requirements, taking into account development readiness, grid availability, RFS timeline, and the Customer's latency and connectivity needs. Site allocation will be confirmed during the technical scoping phase and formalised in the Sales Order Form.

| *No specific site is named by default. If customer has a strong preference, add: "The Customer has indicated a preference for initial deployment at [PRIMARY_SITE_NAME], subject to availability."* |
| :---- |

---

## 4. Relationship Structure and Next Steps (NON-BINDING)

4.1 **MSA Structure.** The Parties intend to execute a Master Services Agreement incorporating: (a) a Pricing Framework setting out the commercial terms for the Services; (b) Sales Order Forms for each capacity commitment; and (c) an SLA Schedule defining availability, performance, and remediation commitments. The MSA will be the sole binding commercial agreement between the Parties.

4.2 **Revenue Chain.** The Parties acknowledge the intended contractual chain: this LOI (non-binding commercial intent) → Sales Order Form (binding capacity commitment and pricing) → MSA (definitive commercial terms). Each stage is designed to provide increasing commercial certainty and to support the Provider's project finance activities.

4.3 **Direct Agreement Willingness.** The Customer confirms its willingness, subject to commercially reasonable terms, to enter into a direct agreement with the Provider's Financing Parties if requested under Clause 5.3. The Customer acknowledges that its cooperation in this regard materially supports the Provider's ability to deliver the committed capacity on the indicative timeline.

4.4 **Expansion and Priority.** The Provider will offer the Customer priority access to additional capacity within the DEC(s) allocated to the Customer, subject to availability. Expansion terms will be governed by the MSA.

4.5 **Implementation Roadmap.** Following execution of this LOI, the Parties intend to proceed as follows:

(a) **Technical scoping** (target: 30 days post-LOI) — Detailed technical discovery to determine exact capacity, rack layout, power distribution, cooling specifications, and connectivity requirements.

(b) **Credit assessment** (target: 30 days post-LOI, concurrent with technical scoping) — The Provider will complete a credit assessment of the Customer or the entity that will execute the MSA.

(c) **Sales Order Form** (target: 60 days post-LOI) — Upon completion of technical scoping, the Provider will issue a Sales Order Form setting out confirmed commercial terms, facility specifications, and service level framework.

(d) **MSA negotiation and execution** (target: 90 days post-LOI) — The Parties will negotiate and execute the MSA.

These timelines are indicative and non-binding.

4.6 **No Capacity Reservation.** This LOI does not reserve capacity at any DEC. Capacity allocation is on a first-come, first-served basis and will only be confirmed upon execution of the MSA.

---

## 5. Project Finance and Assignment (BINDING)

5.1 **Revenue Bankability.** The Parties acknowledge that the Provider intends to finance the development and operation of its DEC programme through a combination of equity investment and non-recourse project finance. The Provider's ability to secure favourable financing terms depends in part on demonstrating contracted or committed revenue streams. This LOI, while non-binding in its commercial terms, is intended to evidence the Parties' genuine commercial intent and to support the Provider's financing activities.

5.2 **Assignment.** Neither Party may assign its rights or obligations under this LOI without the prior written consent of the other Party, except that:

(a) the Provider may assign this LOI, or any rights under it, to any Financing Party or security trustee as security for project finance obligations; and

(b) the Provider may assign this LOI to any Affiliate or special-purpose vehicle within its corporate group without the Customer's consent, provided the Provider remains liable for the performance of the assignee's obligations.

5.3 **Lender Acknowledgment.** The Customer acknowledges and agrees that, upon the Provider's written request, the Customer shall negotiate in good faith and execute a direct agreement (or lender acknowledgment letter) with the Provider's Financing Party within 30 Business Days of such request. Such direct agreement may include, as is customary in project finance transactions: (a) step-in rights for the Financing Party upon a Provider default; (b) cure periods in favour of the Financing Party; and (c) information rights enabling the Financing Party to monitor the commercial relationship. The terms of any such direct agreement shall be commercially reasonable and consistent with market practice for project finance transactions.

---

## 6. Confidentiality and Non-Disclosure (BINDING)

| *Choose ALT-A if an NDA is already signed. Choose ALT-B if no NDA exists. Delete the unused alternative.* |
| :---- |

### ALT-A: EXISTING NDA

6.1 The Non-Disclosure Agreement between the Parties dated [NDA_DATE] (the "**NDA**") remains in full force and effect and applies to all information exchanged in connection with this LOI and the proposed transaction.

6.2 The existence and contents of this LOI shall be treated as Confidential Information under the NDA.

6.3 To the extent of any conflict between the NDA and this LOI, the provisions of this LOI shall prevail.

6.4 Neither Party shall make any public announcement regarding this LOI or the proposed transaction without the prior written consent of the other Party, except as required by applicable law.

*/ALT-A*

### ALT-B: EMBEDDED NCNDA (Tier B — Enhanced)

6.1 **Purpose Limitation.** Each Party shall use the other Party's Confidential Information solely for the Purpose and for no other purpose.

6.2 **Non-Disclosure.** Each Party shall keep confidential all Confidential Information received from the other Party and shall not disclose such information to any person except as permitted under this Clause 6.

6.3 **Standard of Care.** Each Party shall apply no less than reasonable care to protect the other Party's Confidential Information, and no less than the care it applies to its own confidential information of a similar nature.

6.4 **Permitted Disclosures.** A Party may disclose Confidential Information to:

(a) its Representatives who have a genuine need to know for the Purpose and who are bound by confidentiality obligations no less restrictive than this Clause 6 (whether by professional duty or written undertaking);

(b) its bona fide Financing Parties and potential co-investors, provided they are bound by confidentiality obligations no less restrictive than this Clause 6; and

(c) to the extent required by applicable law, regulation, court order, or the rules of any relevant regulatory authority or stock exchange, provided that (where legally permitted) the disclosing Party: (i) gives the other Party prior written notice as soon as reasonably practicable; (ii) consults with the other Party regarding the scope and manner of disclosure; and (iii) discloses only the minimum information required to comply.

6.5 **Liability for Representatives.** Each Party shall be responsible for any breach of this Clause 6 by its Representatives.

6.6 **Exclusions.** The obligations in Clauses 6.1 through 6.3 do not apply to information that the receiving Party can demonstrate:

(a) is or becomes publicly available through no fault of the receiving Party or its Representatives;

(b) was already in the lawful possession of the receiving Party before disclosure, without restriction as to use or disclosure;

(c) was independently developed by the receiving Party without use of or reference to the Confidential Information; or

(d) was received from a third party who was not, to the receiving Party's knowledge, under any obligation of confidentiality in respect of that information.

6.7 **No Implied Rights.** No licence or right is granted under this LOI to the receiving Party in respect of any intellectual property rights of the disclosing Party. All Confidential Information remains the property of the disclosing Party.

6.8 **Return and Destruction.** Upon the earlier of: (a) the disclosing Party's written request, or (b) the expiry or termination of this LOI, the receiving Party shall promptly return or destroy all documents, materials, and tangible items containing Confidential Information and certify such return or destruction in writing within 15 Business Days. The receiving Party may retain copies to the extent required by applicable law or its internal compliance policies, provided such retained copies remain subject to this Clause 6.

6.9 **Onward-Sharing Controls.** If the receiving Party receives an inquiry from any third party regarding the disclosing Party's Confidential Information, the receiving Party shall: (a) not respond to such inquiry without the disclosing Party's prior written consent; and (b) promptly notify the disclosing Party of such inquiry. The receiving Party shall not further distribute or re-disclose Confidential Information beyond the persons authorised under Clause 6.4 without the disclosing Party's prior written consent.

6.10 **Compliance Confirmation.** Upon the disclosing Party's reasonable written request (not more than once per calendar year), the receiving Party shall confirm in writing its compliance with the obligations in this Clause 6.

6.11 **Breach Notification.** Each Party shall notify the other Party in writing within 72 hours of becoming aware of any actual or suspected breach of this Clause 6, and shall take all reasonable steps to mitigate the effects of such breach.

6.12 **Disclaimer.** All Confidential Information is disclosed "as is." The disclosing Party makes no representation or warranty, express or implied, as to the accuracy, completeness, or reliability of any Confidential Information. The receiving Party shall be solely responsible for its own assessment and due diligence.

6.13 **Metadata Protection.** Confidential Information includes metadata, EXIF data, geolocation data, timestamps, file names, folder names, and any digital artifacts associated with or derived from disclosed materials. The receiving Party shall not extract, analyse, or use such metadata except as necessary for the Purpose.

6.14 **Survival.** The obligations in this Clause 6 shall survive termination or expiry of this LOI for a period of [CONFIDENTIALITY_SURVIVAL] from the date of termination or expiry. Obligations in respect of information that constitutes a trade secret under applicable law shall continue indefinitely.

6.15 **Announcements.** Neither Party shall make any public announcement regarding this LOI or the proposed transaction without the prior written consent of the other Party, except as required by applicable law.

6.16 **Remedies.** Each Party acknowledges that a breach of this Clause 6 may cause the disclosing Party irreparable harm for which damages would not be an adequate remedy. The disclosing Party shall be entitled to seek injunctive or other equitable relief from any court of competent jurisdiction, without the need to prove actual loss and without prejudice to any other rights or remedies.

*/ALT-B*

---

## 7. Non-Circumvention (BINDING)

7.1 The Customer shall not, directly or indirectly, without the prior written consent of the Provider:

(a) contact, solicit, deal with, or enter into any business relationship with any Associated Counterparty introduced by the Provider in connection with this LOI or the Services; or

(b) circumvent, avoid, or bypass the Provider in order to deal directly or indirectly with any Associated Counterparty in connection with the development, ownership, or operation of colocation or energy infrastructure on or adjacent to a site identified by the Provider.

7.2 **Duration.** The obligations in this Clause 7 shall continue for [NC_DURATION] after the earlier of: (a) the expiry or termination of this LOI; or (b) the expiry or termination of the MSA, if one is executed.

7.3 **Deemed Introduction.** The Provider's sharing of any Site Identifier with the Customer shall constitute a deemed introduction of all Associated Counterparties for that site. The Provider is not required to separately name each Associated Counterparty.

7.4 **Scope Limitation.** The non-circumvention obligations in this Clause 7 are limited to the Provider's supply-side relationships (site partners, energy counterparties, and infrastructure providers). Nothing in this Clause 7 restricts the Customer from conducting its own business with its existing or future end-user customers, cloud service customers, or compute buyers.

7.5 **Independent Knowledge Exception.** The obligations in Clause 7.1 do not apply to any Associated Counterparty with whom the Customer can demonstrate, by contemporaneous written evidence, that it had an existing business relationship or substantive commercial contact before the date of this LOI or before the Provider's disclosure.

7.6 **MSA Supersession.** If the Parties execute an MSA, the non-circumvention provisions of the MSA shall replace this Clause 7 upon execution of the MSA, except that the survival period in Clause 7.2 shall apply to any introduction made before the MSA effective date that is not separately covered by the MSA.

---

## 8. General Provisions (BINDING)

**8.1 Non-Binding Status.**

(a) **Non-binding provisions.** Clauses 2 through 4 and Schedule 1 of this LOI are non-binding expressions of the Parties' current intentions. They do not create legally enforceable obligations and are subject to the negotiation and execution of the MSA.

(b) **Binding provisions.** Clauses 5 (Project Finance and Assignment), 6 (Confidentiality), 7 (Non-Circumvention), and 8 (General Provisions) are legally binding and enforceable obligations.

**8.2 Good Faith.** The Parties agree to engage in the technical scoping and commercial negotiation process in good faith (*te goeder trouw*) and in accordance with the principles of reasonableness and fairness (*redelijkheid en billijkheid*) as contemplated by Article 6:248 of the Dutch Civil Code (*Burgerlijk Wetboek*). For the avoidance of doubt, the good faith obligation does not oblige either Party to enter into the MSA. Either Party may discontinue negotiations at any time, provided it does so in good faith. Any liability arising from a breach of this good faith obligation shall be limited to verifiable reliance damages (*negatief contractsbelang*) and shall not extend to loss of profit or expectation damages (*positief contractsbelang*).

**8.3 Validity.** This LOI shall remain valid until [VALIDITY_DATE], after which it shall lapse automatically unless extended by mutual written agreement. Upon lapse, Clauses 5.2, 5.3, 6, and 7 shall survive for their respective stated periods.

**8.4 Costs.** Each Party shall bear its own costs in connection with this LOI and the negotiation of the MSA.

**8.5 Counterparts.** This LOI may be executed in counterparts, including by electronic signature within the meaning of the eIDAS Regulation (EU) No 910/2014. Each counterpart constitutes an original.

**8.6 Notices.** All notices under this LOI shall be in writing (including email) and addressed to the contact details in the preamble. A notice is effective upon receipt. Each Party shall promptly notify the other of any change to its contact details.

**8.7 Governing Law.** This LOI shall be governed by and construed in accordance with the laws of the Netherlands. The United Nations Convention on Contracts for the International Sale of Goods (CISG) is expressly excluded.

**8.8 Jurisdiction.** The courts of Amsterdam (*Rechtbank Amsterdam*) shall have exclusive jurisdiction over any dispute arising out of or in connection with the binding provisions of this LOI.

**8.9 Entire Agreement.** This LOI, together with any NDA referenced in Clause 6 (ALT-A), constitutes the entire agreement between the Parties in relation to its subject matter and supersedes all prior negotiations, representations, and agreements relating to the proposed transaction. Nothing in this Clause limits liability for fraud.

**8.10 Partnership Disclaimer.** Nothing in this LOI shall be construed as creating a partnership, joint venture, agency, or employment relationship between the Parties. Neither Party has authority to bind the other or to incur any obligation on the other's behalf.

---

We look forward to working with you.

Yours faithfully,

**For and on behalf of [DE:LEGAL_NAME]**

KvK: [DE:KVK]

Signature: ____________________________

Name: [DE:SIGNATORY_NAME]

Title: [DE:SIGNATORY_TITLE]

Date: ____________________________

---

**ACKNOWLEDGED AND AGREED:**

**For and on behalf of [CUSTOMER_NAME]**

[CUSTOMER_REG_TYPE]: [CUSTOMER_REG_NUMBER]

Signature: ____________________________

Name: [CUSTOMER_SIGNATORY_NAME]

Title: [CUSTOMER_SIGNATORY_TITLE]

Date: ____________________________

---

## Schedule 1 — Capacity and Technical Requirements (NON-BINDING)

| Item | Detail |
| :---- | :---- |
| **Indicative Capacity** | [DEC_BLOCK_COUNT] DEC Blocks ([INDICATIVE_MW] MW IT) |
| **GPU / Accelerator Type** | [e.g., NVIDIA GB200 NVL72 or equivalent] |
| **Target Rack Density** | [e.g., 40-130 kW per rack] |
| **Cooling Requirement** | [e.g., Direct liquid cooling, rear-door CDU] |
| **Power Redundancy** | [e.g., Block redundant, N+1 CDU/dry coolers] |
| **Network Connectivity** | [e.g., NVIDIA Spectrum-X fabric, AMS-IX peering] |
| **Deployment Phasing** | [As per Cl. 3.3 if applicable] |
| **Implementation Milestones** | |
| — Technical scoping complete | [LOI_DATE + 30 days] |
| — Credit assessment complete | [LOI_DATE + 30 days] |
| — Sales Order Form issued | [LOI_DATE + 60 days] |
| — MSA executed | [LOI_DATE + 90 days] |
| — Target RFS | [TARGET_RFS_DATE] |
| **Expansion Target** | [EXPANSION_MW] MW IT |

---

*DE-LOI-Wholesale-v3.0 | [LOI_DATE] | Digital Energy Netherlands B.V. | CONFIDENTIAL*
