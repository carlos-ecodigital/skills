
| DRAFTER: Follow these steps before issuing |
| :---- |
| 1. Fill the Parameter Table below |
| 2. Find-and-replace each [PLACEHOLDER] in the body |
| 3. Choose one Service Type (Cl. 3.1) — or combine if customer wants multiple |
| 4. Choose: IF: PRICING or IF: NO_PRICING (Cl. 3.4) — delete unused |
| 5. Choose: ALT-A or ALT-B for Confidentiality (Cl. 6) — delete unused |
| 6. Confirm [PLATFORM_MW] and [SITE_COUNT] with CPO/CEO |
| 7. Delete all shaded instruction blocks. Verify no [BRACKETS] remain |
| 8. Result: ~4 pages |

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
| [CUSTOMER_DESCRIPTION] | | Cl. 1.2 — brief description |

### Service and Capacity

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [SERVICE_TYPE] | Bare Metal / Shared Cloud / Tokens | Cl. 3.1 — select one or combine |
| [INDICATIVE_CAPACITY] | | Cl. 3.2 — capacity in kW, DEC Blocks, or GPU-hours |
| [MIN_TERM] | | Cl. 3.5 — minimum commitment (e.g., 12 months, 3 years) |
| [PLATFORM_MW] | | Recital (A) — programme capacity target |
| [SITE_COUNT] | | Recital (A) — number of identified sites |

### Commercial

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [BASE_PRICE] | | Cl. 3.4 pricing table |
| [TERM_YEARS] | | Cl. 3.4 pricing table |
| [TARGET_RFS_DATE] | | Cl. 3.4 pricing table |

### Dates

| Parameter | Value | Used in |
| :---- | :---- | :---- |
| [LOI_DATE] | | Letterhead |
| [VALIDITY_DATE] | | Cl. 8.3 |
| [NDA_DATE] | | Cl. 6 ALT-A (if existing NDA) |
| [CONFIDENTIALITY_SURVIVAL] | 3 years (default) | Cl. 6.7 |

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

**Re: Letter of Intent — AI Compute Infrastructure Services**

---

## Recitals

(A) [DE:SHORT_NAME] (the "**Provider**") operates Digital Energy Centers ("**DECs**"): purpose-built, liquid-cooled colocation facilities designed for high-density AI and accelerated compute workloads. DECs integrate AI compute with energy recycling and generation. The Provider's programme spans [SITE_COUNT] identified sites with secured energy and grid access, offering European data sovereignty and capacity across multiple service models — including dedicated bare metal colocation, shared cloud environments, and token-based GPU access.

(B) [CUSTOMER_SHORT] (the "**Customer**") [CUSTOMER_DESCRIPTION].

(C) The Parties wish to record their mutual interest in the Customer procuring AI compute infrastructure services at the Provider's DEC facilities, on the indicative terms set out below. This letter of intent (the "**LOI**") reflects both Parties' intent and is intended to form the basis for further technical scoping and commercial negotiation toward a service agreement (the "**MSA**").

---

## 1. Definitions

1.1 In this LOI, unless the context requires otherwise:

"**Affiliate**" means, in relation to a Party, any entity that directly or indirectly controls, is controlled by, or is under common control with that Party, where "control" means the ownership of more than 50% of the voting rights or equivalent ownership interest;

"**Business Day**" means a day other than a Saturday, Sunday, or public holiday in the Netherlands;

"**Confidential Information**" means all information (whether technical, commercial, financial, or otherwise) disclosed by a Party to the other in connection with the Purpose, whether in writing, orally, electronically, or by inspection, including any information that by its nature or the circumstances of disclosure would reasonably be understood to be confidential. The existence and contents of this LOI are Confidential Information;

"**DEC**" means a Digital Energy Center: a purpose-built colocation facility developed and operated by the Provider;

"**DEC Block**" means a standardised compute unit of approximately 1.2 MW IT capacity;

"**Financing Party**" means any bank, financial institution, fund, security trustee, or other entity providing or arranging finance to the Provider or any of its Affiliates in connection with the development or operation of any DEC;

"**MSA**" means the definitive service agreement to be negotiated between the Parties;

"**Purpose**" means evaluating, negotiating, and progressing toward the execution of an MSA;

"**Representatives**" means, in relation to a Party, its Affiliates, and its and their respective directors, officers, employees, agents, and professional advisers;

"**Services**" means the AI compute infrastructure services to be provided by the Provider, the scope of which will depend on the service model selected under Clause 3.1.

---

## 2. Purpose and Scope

2.1 This LOI records the Parties' mutual interest in the Customer procuring AI compute infrastructure services at the Provider's DEC facilities, on the indicative terms set out in Clauses 3 and 4.

2.2 The commercial terms in Clauses 3 and 4 are non-binding expressions of intent. The confidentiality and general provisions in Clauses 5 through 7 are legally binding and enforceable from the date of execution.

| *Note: This template does not include a Non-Circumvention clause (unlike DE-LOI-Distributor and DE-LOI-Wholesale). End users do not access the Provider's supply-side relationships. If non-circumvention protection is required for a specific engagement, use the Distributor or Wholesale template instead.* |
| :---- |

---

## 3. Service Requirements (NON-BINDING)

3.1 **Service Model.** The Customer has indicated interest in the following service model:

| *DRAFTER: Select the applicable service model(s). Delete unused options. If the customer wants a combination, retain multiple and note "combined" in the parameter table.* |
| :---- |

**Bare Metal Colocation** — Dedicated, liquid-cooled rack space within a DEC, supporting densities of 40 kW per rack and above. The Provider supplies power distribution, direct liquid cooling, physical security, and 24/7 facility operations. The Customer deploys and manages its own hardware and software. The demarcation point is at the rack: everything below (facility infrastructure) is the Provider's responsibility; everything above (compute hardware, operating system, workloads) is the Customer's. Billed monthly on a per-kW basis with a committed term.

**Shared Cloud** — Managed GPU compute capacity hosted on sovereign European infrastructure at the Provider's DEC facilities. The Customer accesses reserved or on-demand compute resources without procuring, deploying, or managing hardware. The Provider or a designated delivery partner operates the compute platform, including hardware lifecycle, scheduling, and platform software. The Customer manages workloads, data, and application layers. Billed on reserved capacity or metered usage, with a committed term or minimum spend.

**Token-Based GPU Access** — Flexible, on-demand access to GPU compute measured in GPU-hours or equivalent units. The Customer purchases compute tokens — pre-paid or pay-as-you-go — redeemable against available capacity across the Provider's DEC network. No dedicated hardware allocation or minimum infrastructure commitment. The Provider or a designated delivery partner manages all infrastructure and scheduling. The Customer submits workloads and consumes capacity as needed. Lowest entry threshold; designed for variable or exploratory workloads.

| *For Shared Cloud and Token-Based models: the Provider may deliver these services in partnership with a qualified delivery partner. The specific delivery partner, platform, and commercial terms will be confirmed in the MSA.* |
| :---- |

3.2 **Indicative Capacity.** The Customer has indicated interest in approximately [INDICATIVE_CAPACITY] of compute capacity. The exact capacity, configuration, and technical requirements will be determined during the technical scoping phase.

3.3 **Technical Requirements.** The Provider's DEC facilities support rack densities of 40 kW and above with direct liquid cooling, designed for GPU-intensive training and inference workloads. The Customer's specific requirements — including GPU type, rack density, network connectivity, and data sovereignty needs — will be confirmed during technical scoping and formalised in the MSA.

3.4 **Indicative Pricing.**

| IF: PRICING — include if indicative pricing has been discussed |
| :---- |

Based on preliminary discussions, the Provider's indicative pricing is as follows:

| Parameter | Indicative Terms |
| :---- | :---- |
| **Service rate** | EUR [BASE_PRICE] [per kW per month / per GPU-hour] |
| **Contract term** | [TERM_YEARS] |
| **Indicative RFS** | [TARGET_RFS_DATE] |

All terms are indicative and subject to the outcome of technical scoping and the Customer's final requirements.

*/IF: PRICING*

| IF: NO_PRICING — select if pricing is deferred |
| :---- |

Pricing will be determined following the technical scoping phase and set out in the MSA. The Provider will provide indicative pricing upon agreement of the Customer's capacity, density, and service model requirements.

*/IF: NO_PRICING*

3.5 **Term.** The Customer has indicated willingness to enter into a minimum commitment of **[MIN_TERM]** under the MSA.

---

## 4. Next Steps (NON-BINDING)

4.1 Following execution of this LOI, the Parties intend to proceed as follows:

(a) **Technical scoping** (target: 30 days post-LOI) — Detailed discovery to determine capacity, configuration, connectivity, and service model requirements.

(b) **Commercial proposal** (target: 60 days post-LOI) — The Provider will issue a commercial proposal setting out confirmed pricing, service scope, and SLA framework.

(c) **MSA negotiation and execution** (target: 90 days post-LOI) — The Parties will negotiate and execute the MSA.

These timelines are indicative and non-binding.

4.2 This LOI does not reserve capacity at any DEC. Capacity allocation will be confirmed upon execution of the MSA.

---

## 5. Project Finance and Assignment (BINDING)

5.1 **Revenue Bankability.** The Parties acknowledge that the Provider intends to finance the development and operation of its DEC programme through a combination of equity investment and non-recourse project finance. The Provider's ability to secure favourable financing terms depends in part on demonstrating contracted or committed revenue streams. This LOI, while non-binding in its commercial terms, is intended to evidence the Parties' genuine commercial intent and to support the Provider's financing activities.

5.2 **Assignment.** Neither Party may assign its rights or obligations under this LOI without the prior written consent of the other Party, except that:

(a) the Provider may assign this LOI, or any rights under it, to any Financing Party or security trustee as security for project finance obligations; and

(b) the Provider may assign this LOI to any Affiliate or special-purpose vehicle within its corporate group without the Customer's consent, provided the Provider remains liable for the performance of the assignee's obligations.

5.3 **Lender Acknowledgment.** The Customer acknowledges and agrees that, upon the Provider's written request, the Customer shall negotiate in good faith and execute a direct agreement (or lender acknowledgment letter) with the Provider's Financing Party within 30 Business Days of such request. Such direct agreement may include, as is customary in project finance transactions: (a) step-in rights for the Financing Party upon a Provider default; (b) cure periods in favour of the Financing Party; and (c) information rights enabling the Financing Party to monitor the commercial relationship. The terms of any such direct agreement shall be commercially reasonable and consistent with market practice for project finance transactions.

---

## 6. Confidentiality (BINDING)

| *Choose ALT-A if an NDA is already signed. Choose ALT-B if no NDA exists. Delete the unused alternative.* |
| :---- |

### ALT-A: EXISTING NDA

6.1 The Non-Disclosure Agreement between the Parties dated [NDA_DATE] (the "**NDA**") remains in full force and effect and applies to all information exchanged in connection with this LOI.

6.2 The existence and contents of this LOI shall be treated as Confidential Information under the NDA.

6.3 Neither Party shall make any public announcement regarding this LOI without the prior written consent of the other Party, except as required by applicable law.

*/ALT-A*

### ALT-B: EMBEDDED NDA (Tier A — Standard)

6.1 Each Party shall keep confidential all Confidential Information received from the other Party and shall use such information solely for the Purpose.

6.2 Each Party may disclose Confidential Information only to its Representatives who have a genuine need to know for the Purpose and who are bound by confidentiality obligations no less restrictive than this Clause 6.

6.3 The obligations in Clauses 6.1 and 6.2 do not apply to information that the receiving Party can demonstrate: (a) is or becomes publicly available through no fault of the receiving Party; (b) was already in the receiving Party's possession without restriction; (c) was independently developed without use of the Confidential Information; or (d) was received from a third party without breach of any confidentiality obligation.

6.4 A Party may disclose Confidential Information to the extent required by applicable law, regulation, or court order, provided that (where legally permitted) the disclosing Party gives the other Party prior written notice and discloses only the minimum required.

6.5 Upon written request or expiry of this LOI, the receiving Party shall promptly return or destroy all Confidential Information and certify such return or destruction in writing. The receiving Party may retain copies required by applicable law or internal compliance policies, subject to continued confidentiality.

6.6 Neither Party shall make any public announcement regarding this LOI without the prior written consent of the other Party, except as required by applicable law.

6.7 The obligations in this Clause 6 shall survive for [CONFIDENTIALITY_SURVIVAL] from the date of termination or expiry of this LOI. Obligations in respect of trade secrets shall continue indefinitely.

6.8 Each Party acknowledges that a breach of this Clause 6 may cause irreparable harm for which damages would not be an adequate remedy. The disclosing Party shall be entitled to seek injunctive or other equitable relief without the need to prove actual loss.

*/ALT-B*

---

## 7. General Provisions (BINDING)

**7.1 Non-Binding Status.**

(a) **Non-binding provisions.** Clauses 2 through 4 of this LOI are non-binding expressions of the Parties' current intentions. They do not create legally enforceable obligations and are subject to the negotiation and execution of the MSA.

(b) **Binding provisions.** Clauses 5 (Project Finance and Assignment), 6 (Confidentiality), and 7 (General Provisions) are legally binding and enforceable obligations.

**7.2 Good Faith.** The Parties agree to engage in the technical scoping and commercial negotiation process in good faith (*te goeder trouw*) and in accordance with the principles of reasonableness and fairness (*redelijkheid en billijkheid*) as contemplated by Article 6:248 of the Dutch Civil Code (*Burgerlijk Wetboek*). The good faith obligation does not oblige either Party to enter into the MSA. Either Party may discontinue negotiations at any time, provided it does so in good faith. Any liability arising from a breach of this good faith obligation shall be limited to verifiable reliance damages (*negatief contractsbelang*).

**7.3 Validity.** This LOI shall remain valid until [VALIDITY_DATE], after which it shall lapse automatically unless extended by mutual written agreement. Upon lapse, Clauses 5.2, 5.3, and 6 shall survive for their respective stated periods.

**7.4 Costs.** Each Party shall bear its own costs in connection with this LOI.

**7.5 Counterparts.** This LOI may be executed in counterparts, including by electronic signature within the meaning of the eIDAS Regulation (EU) No 910/2014.

**7.6 Notices.** All notices under this LOI shall be in writing (including email) and addressed to the contact details in the preamble. A notice is effective upon receipt.

**7.7 Governing Law.** This LOI shall be governed by and construed in accordance with the laws of the Netherlands. The United Nations Convention on Contracts for the International Sale of Goods (CISG) is expressly excluded.

**7.8 Jurisdiction.** The courts of Amsterdam (*Rechtbank Amsterdam*) shall have exclusive jurisdiction over any dispute arising out of or in connection with the binding provisions of this LOI.

**7.9 Entire Agreement.** This LOI constitutes the entire agreement between the Parties in relation to its subject matter and supersedes all prior negotiations, representations, and agreements. Nothing in this Clause limits liability for fraud.

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

## Schedule 1 — Service Requirements (NON-BINDING)

| Item | Detail |
| :---- | :---- |
| **Service Model** | [As selected in Cl. 3.1] |
| **Indicative Capacity** | [INDICATIVE_CAPACITY] |
| **GPU / Accelerator Type** | [e.g., NVIDIA GB200 NVL72 or equivalent] |
| **Target Rack Density** | [e.g., 40-130 kW per rack] |
| **Cooling Requirement** | [e.g., Direct liquid cooling] |
| **Network Connectivity** | [e.g., AMS-IX peering, low-latency requirements] |
| **Data Sovereignty** | [e.g., EU-only, NL-only, no restrictions] |
| **Implementation Milestones** | |
| — Technical scoping complete | [LOI_DATE + 30 days] |
| — Commercial proposal issued | [LOI_DATE + 60 days] |
| — MSA executed | [LOI_DATE + 90 days] |

---

*DE-LOI-EndUser-v3.0 | [LOI_DATE] | Digital Energy Netherlands B.V. | CONFIDENTIAL*
