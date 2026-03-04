# Clause Library

Reusable clause skeletons for common contractual provisions. Each clause includes a universal skeleton, jurisdiction-specific annotations, and key variables. Clauses are designed to be composed across document types -- an NDA, MSA, SPA, and SHA all use the same confidentiality skeleton adapted for context.

**Usage:** Select clauses relevant to the document type. Replace `{{VARIABLES}}` with intake values. Apply jurisdiction layer from the relevant `jurisdictions/` files.

---

## 1. Preamble and Recitals

### Skeleton

```
This {{DOCUMENT_TYPE}} (the "Agreement") is entered into on {{AGREEMENT_DATE}}

BETWEEN:

(1) {{PARTY_A_NAME}}, a {{PARTY_A_ENTITY_TYPE}} incorporated under the laws of {{PARTY_A_JURISDICTION}}, with registered address at {{PARTY_A_ADDRESS}}, registered under number {{PARTY_A_REG_NUMBER}} (the "{{PARTY_A_SHORT}}"); and

(2) {{PARTY_B_NAME}}, a {{PARTY_B_ENTITY_TYPE}} incorporated under the laws of {{PARTY_B_JURISDICTION}}, with registered address at {{PARTY_B_ADDRESS}}, registered under number {{PARTY_B_REG_NUMBER}} (the "{{PARTY_B_SHORT}}").

BACKGROUND:

(A) {{PARTY_A_SHORT}} {{RECITAL_A}}.
(B) {{PARTY_B_SHORT}} {{RECITAL_B}}.
(C) The Parties wish to {{RECITAL_PURPOSE}}.
(D) {{ADDITIONAL_RECITAL}}

The Parties agree as follows:
```

### Jurisdiction Notes

| Jurisdiction | Adaptation |
|---|---|
| NL | Entity types: BV, NV, Cooperatie, Stichting. Registration: KvK number. Heading: "OVERWEGINGEN" or "Background". |
| NO | Entity types: AS, ASA, ANS, NUF. Registration: Bronnoysundregistrene. Heading: "BAKGRUNN" or "Background". |
| UK | Entity types: Ltd, PLC, LLP. Registration: Companies House number. Use "WHEREAS" or "BACKGROUND". |
| US | Entity types: LLC, Corp, LP. Registration: state of incorporation. "RECITALS" heading common. |

---

## 2. Definitions and Interpretation

### Core Defined Terms (Universal)

```
2.1 In this Agreement, unless the context requires otherwise:

"Affiliate" means, in relation to a Party, any entity that directly or indirectly controls, is controlled by, or is under common control with that Party, where "control" means the ownership of more than 50% of the voting rights or equivalent ownership interest;

"Applicable Law" means all laws, regulations, codes of practice, and regulatory requirements applicable to the relevant Party in the performance of its obligations under this Agreement;

"Business Day" means a day other than a Saturday, Sunday, or public holiday in {{JURISDICTION}};

"Confidential Information" has the meaning given in Clause {{CONF_CLAUSE}};

"Losses" means all damages, losses, liabilities, costs (including reasonable legal fees), charges, and expenses;

"Party" means {{PARTY_A_SHORT}} or {{PARTY_B_SHORT}}, and "Parties" means both of them.
```

### Interpretation Boilerplate

```
2.2 In this Agreement, unless the context requires otherwise:
(a) headings do not affect interpretation;
(b) references to Clauses and Schedules are to clauses of, and schedules to, this Agreement;
(c) "including" means "including without limitation";
(d) words in the singular include the plural and vice versa;
(e) references to legislation include amendments, re-enactments, and subordinate legislation;
(f) "writing" and "written" include email;
(g) a "person" includes any individual, body corporate, partnership, or unincorporated association;
(h) in the event of conflict between the main body and a Schedule, the main body prevails, unless the Schedule expressly states otherwise.
```

---

## 3. Confidentiality

**Used in:** NDA, MSA, SPA, SHA, JV Agreement, Employment Agreement, Settlement Agreement

### Skeleton

```
{{CONF_CLAUSE}}.1 "Confidential Information" means all information (whether technical, commercial, financial, or otherwise) disclosed by one Party (the "Disclosing Party") to the other (the "Receiving Party") in connection with this Agreement, whether in writing, orally, electronically, or by inspection, that:
(a) is marked as confidential or proprietary; or
(b) would reasonably be understood to be confidential given the nature of the information or the circumstances of disclosure.

{{CONF_CLAUSE}}.2 The Receiving Party shall:
(a) keep all Confidential Information strictly confidential;
(b) not disclose Confidential Information to any third party except as permitted under this Clause;
(c) use Confidential Information solely for the purposes of this Agreement;
(d) apply no less than reasonable care to protect Confidential Information (and no less than the care it applies to its own confidential information).

{{CONF_CLAUSE}}.3 Confidential Information does not include information that:
(a) is or becomes publicly available through no fault of the Receiving Party;
(b) was already in the Receiving Party's possession without restriction before disclosure;
(c) was independently developed by the Receiving Party without use of Confidential Information;
(d) was received from a third party without breach of any obligation of confidentiality.

{{CONF_CLAUSE}}.4 The Receiving Party may disclose Confidential Information to:
(a) its Affiliates, employees, officers, directors, and professional advisers who have a need to know and are bound by confidentiality obligations no less restrictive than this Clause;
(b) as required by Applicable Law, regulation, or court order, provided the Receiving Party (where legally permitted) gives the Disclosing Party prior written notice and reasonable opportunity to seek a protective order.

{{CONF_CLAUSE}}.5 The obligations under this Clause shall continue for {{CONFIDENTIALITY_DURATION}} after termination or expiry of this Agreement. Obligations in respect of trade secrets shall continue indefinitely.

{{CONF_CLAUSE}}.6 Upon termination or upon the Disclosing Party's written request, the Receiving Party shall promptly return or destroy all Confidential Information and certify destruction in writing.
```

### Document-Specific Adaptations

| Document | Adaptation |
|---|---|
| NDA | This IS the agreement -- expand to include term, return of materials, remedies, no implied licence |
| SPA | Add: DD information carve-out, announcement restrictions, warranty disclosure letter |
| SHA | Add: company information sharing between shareholders, board confidentiality |
| Employment | Add: social media, post-termination, garden leave scope |
| Settlement | Add: terms of settlement themselves are confidential, agreed public statement |

---

## 4. Limitation of Liability

**Used in:** Service Agreement, MSA, SPA (as warranty cap), License Agreement, EPC Contract

### Skeleton

```
{{LOL_CLAUSE}}.1 Subject to Clause {{LOL_CLAUSE}}.3, each Party's total aggregate liability arising under or in connection with this Agreement (whether in contract, tort including negligence, breach of statutory duty, or otherwise) shall not exceed {{LIABILITY_CAP}}.

{{LOL_CLAUSE}}.2 Neither Party shall be liable to the other for any indirect, special, incidental, or consequential loss or damage, including:
(a) loss of profit or anticipated profit;
(b) loss of revenue;
(c) loss of data;
(d) loss of goodwill;
(e) loss of anticipated savings;
(f) loss of business opportunity,
whether or not such loss was foreseeable or the Party had been advised of the possibility.

{{LOL_CLAUSE}}.3 Nothing in this Agreement limits or excludes liability for:
(a) death or personal injury caused by negligence;
(b) fraud or fraudulent misrepresentation;
(c) any liability that cannot be limited or excluded by Applicable Law;
{{ADDITIONAL_CARVEOUTS}}

{{LOL_CLAUSE}}.4 The limitations in this Clause apply equally to both Parties unless expressly stated otherwise.
```

### Common Cap Formulations

| Cap Type | Wording | Typical Use |
|---|---|---|
| Fixed amount | "EUR {{AMOUNT}}" | High-value, bespoke contracts |
| Fee multiple | "an amount equal to {{MULTIPLIER}} times the Fees paid or payable in the 12-month period preceding the event giving rise to the claim" | Service agreements |
| Annual fees | "the total Fees paid under this Agreement in the 12 months preceding the claim" | Recurring services |
| Purchase price | "the Purchase Price" | SPA (warranty claims) |

### Jurisdiction Notes

| Jurisdiction | Key Consideration |
|---|---|
| NL | Avtalewet (BW 6:248): exclusions must not be unreasonable. BW 6:94: penalty clauses subject to judicial moderation. |
| NO | Avtaleloven § 36: general fairness control -- unreasonable exclusions may be set aside. |
| UK | UCTA 1977 s.2(2)/s.3: exclusions must be reasonable. Watford Electronics test for B2B. |
| US | Varies by state. Some states restrict consequential damage exclusions for certain claims. UCC 2-719: unconscionability standard. |

---

## 5. Indemnification

**Used in:** Service Agreement, MSA, SPA, License Agreement, EPC Contract

### Skeleton

```
{{INDEM_CLAUSE}}.1 {{INDEMNIFYING_PARTY}} shall indemnify, defend, and hold harmless {{INDEMNIFIED_PARTY}} from and against all Losses arising out of or in connection with any third-party claim that {{INDEMNITY_TRIGGER}}.

{{INDEM_CLAUSE}}.2 {{INDEMNIFIED_PARTY}} shall indemnify {{INDEMNIFYING_PARTY}} from and against all Losses arising out of or in connection with {{REVERSE_INDEMNITY_TRIGGER}}.

{{INDEM_CLAUSE}}.3 The indemnified Party shall:
(a) promptly notify the indemnifying Party in writing of any claim;
(b) grant the indemnifying Party sole conduct of the defence and settlement (provided no settlement admits liability without the indemnified Party's consent);
(c) provide reasonable cooperation at the indemnifying Party's cost.

{{INDEM_CLAUSE}}.4 Failure to notify promptly shall not relieve the indemnifying Party of its obligations except to the extent actually prejudiced.

{{INDEM_CLAUSE}}.5 The indemnification obligations under this Clause are subject to the limitations set out in Clause {{LOL_CLAUSE}} [unless expressly carved out].
```

### Jurisdiction Notes

| Jurisdiction | Key Term | Note |
|---|---|---|
| NL | "vrijwaren" | Standard Dutch indemnity concept. Cross-ref LOL clause essential. |
| NO | "skadesløsholde" | Functions similarly to English law. |
| UK | "indemnify and hold harmless" | Technically tautological but conventional. |
| US | "indemnify, defend, and hold harmless" | Some states distinguish "indemnify" (reimburse) from "hold harmless" (prevent loss). Include "defend" explicitly. |

---

## 6. Termination

**Used in:** All agreement types

### Skeleton

```
{{TERM_CLAUSE}}.1 Material breach: either Party may terminate this Agreement by written notice if the other Party commits a material breach and:
(a) the breach is not capable of remedy; or
(b) the breach is capable of remedy and the breaching Party fails to remedy it within {{CURE_PERIOD}} days of receiving written notice specifying the breach and requiring its remedy.

{{TERM_CLAUSE}}.2 Insolvency: either Party may terminate this Agreement immediately by written notice if the other Party:
(a) becomes unable to pay its debts as they fall due;
(b) has a receiver, administrator, liquidator, or similar officer appointed;
(c) enters into any voluntary arrangement or composition with its creditors;
(d) ceases or threatens to cease to carry on business; or
(e) suffers any analogous event under the laws of any jurisdiction.

{{TERM_CLAUSE}}.3 Convenience: {{CONVENIENCE_PARTY}} may terminate this Agreement for any reason by giving not less than {{CONVENIENCE_NOTICE}} prior written notice.

{{TERM_CLAUSE}}.4 Change of control: either Party may terminate this Agreement by giving {{COC_NOTICE}} written notice if there is a change of control of the other Party.

{{TERM_CLAUSE}}.5 Force majeure: either Party may terminate this Agreement if a Force Majeure Event continues for more than {{FM_TERMINATION_DAYS}} consecutive days.
```

### Jurisdiction Notes

| Jurisdiction | Key Consideration |
|---|---|
| NL | "Ingebrekestelling" (notice of default, BW 6:82) required before termination for breach ("ontbinding", BW 6:265). BW 6:265: court may grant partial ontbinding. |
| NO | "Vesentlig mislighold" (material breach) threshold. Heving (termination) requires written notice. 30-day cure standard. |
| UK | CIGA 2020: ipso facto insolvency clauses restricted for supply contracts. Material breach vs condition/warranty distinction. |
| US | State variation. "Material adverse effect" definition critical. Delaware: substantial impairment standard. |

---

## 7. Force Majeure

**Used in:** Service Agreement, MSA, EPC Contract, PPA, O&M Agreement

### Skeleton

```
{{FM_CLAUSE}}.1 "Force Majeure Event" means an event beyond a Party's reasonable control that could not have been reasonably foreseen or prevented, including: natural disasters, war, armed conflict, terrorism, civil unrest, government action or sanction, embargo, fire, flood, earthquake, epidemic or pandemic, failure of utility supplies or telecommunications, and {{ADDITIONAL_FM_EVENTS}}.

{{FM_CLAUSE}}.2 A Force Majeure Event does not include: {{FM_EXCLUSIONS}}.

{{FM_CLAUSE}}.3 The affected Party shall:
(a) notify the other Party in writing within {{FM_NOTICE_DAYS}} Business Days, specifying the event and its expected impact and duration;
(b) use reasonable endeavours to mitigate the impact and resume performance as soon as practicable;
(c) provide regular updates on the status of the Force Majeure Event.

{{FM_CLAUSE}}.4 The affected Party's obligations (other than payment obligations) are suspended to the extent affected by the Force Majeure Event for the duration of that event.

{{FM_CLAUSE}}.5 If the Force Majeure Event continues for more than {{FM_TERMINATION_DAYS}} consecutive days, either Party may terminate this Agreement by giving {{FM_TERM_NOTICE}} written notice.
```

### Jurisdiction Notes

| Jurisdiction | Key Consideration |
|---|---|
| NL | BW 6:75: "overmacht" -- party not liable if non-performance not attributable. No statutory list; contractual definition recommended. |
| NO | Kontrollansvaret (kjøpsloven § 27): liability unless impediment beyond control, unforeseeable, and unavoidable. Contractual definition adds certainty. |
| UK | No general common law force majeure doctrine -- must be contractual. Frustration (narrow) is the fallback. |
| US | UCC 2-615 (impracticability for goods). Common law impossibility/impracticability (narrow). Contractual clause essential. |

### Energy/Infrastructure Note

For project finance and energy contracts, explicitly exclude from FM:
- Grid congestion / transportschaarste (foreseeable, insurable)
- Market price fluctuations
- Equipment supply delays (unless caused by an FM event)
- Counterparty non-performance
- Permit delays attributable to the affected party

---

## 8. Intellectual Property

**Used in:** Service Agreement, MSA, License Agreement, SPA (IP warranties), JV Agreement

### Skeleton -- Client-Owns Model

```
{{IP_CLAUSE}}.1 Background IP: each Party retains all rights in its pre-existing intellectual property ("Background IP").

{{IP_CLAUSE}}.2 Foreground IP: all intellectual property rights in Deliverables and work product created by {{PROVIDER}} in performing the Services ("Foreground IP") shall vest in {{CLIENT}} upon creation. {{PROVIDER}} hereby assigns (by way of present assignment of future rights) all Foreground IP to {{CLIENT}} with full title guarantee.

{{IP_CLAUSE}}.3 Licence of Background IP: {{PROVIDER}} grants {{CLIENT}} a non-exclusive, perpetual, irrevocable, royalty-free licence to use {{PROVIDER}}'s Background IP solely to the extent necessary to use the Deliverables and receive the benefit of the Services.

{{IP_CLAUSE}}.4 Third-party IP: {{PROVIDER}} warrants that the Services and Deliverables do not infringe any third-party intellectual property rights.

{{IP_CLAUSE}}.5 Moral rights: {{PROVIDER}} shall procure that its Personnel waive moral rights in the Foreground IP to the fullest extent permitted by Applicable Law.
```

### Skeleton -- Provider-Retains Model

```
{{IP_CLAUSE}}.2 [Alternative] Foreground IP: {{PROVIDER}} retains all intellectual property rights in the Foreground IP and grants {{CLIENT}} a perpetual, irrevocable, non-exclusive, royalty-free licence to use, copy, modify, and create derivative works of the Foreground IP for {{CLIENT}}'s internal business purposes.
```

### Jurisdiction Notes

| Jurisdiction | Key Consideration |
|---|---|
| NL | Auteurswet: copyright vests in creator. Assignment must be in writing. Work-for-hire doctrine limited -- employer owns if employment scope. |
| NO | Åndsverkloven: moral rights (§ 3) cannot be fully waived. Contractual commitment not to exercise is permissible but unenforceable if unreasonable. |
| UK | CDPA 1988 s.90(3): assignment must be in writing. "With full title guarantee" is standard. Moral rights can be waived (s.87). |
| US | Work-for-hire doctrine (17 USC § 101): employer owns if within scope. For contractors, only 9 specific categories qualify. Assignment for other works. |

---

## 9. Data Protection (GDPR/DPA)

**Used in:** Service Agreement, MSA, SaaS Agreement, any agreement involving personal data processing

### Skeleton -- Controller-Processor Relationship

```
{{DPA_CLAUSE}}.1 For the purposes of Data Protection Legislation, {{CLIENT}} is the data controller and {{PROVIDER}} is the data processor in respect of Personal Data processed by {{PROVIDER}} in performing the Services.

{{DPA_CLAUSE}}.2 The Parties shall comply with the Data Processing Agreement set out in Schedule {{DPA_SCHEDULE}}, which forms an integral part of this Agreement.

{{DPA_CLAUSE}}.3 {{PROVIDER}} shall not engage any sub-processor without {{CLIENT}}'s prior {{SUB_PROCESSOR_CONSENT}} consent. {{PROVIDER}} shall impose data protection obligations on each sub-processor no less onerous than those in this Agreement.

{{DPA_CLAUSE}}.4 {{PROVIDER}} shall not transfer Personal Data outside the EEA without ensuring appropriate safeguards are in place (adequacy decision, Standard Contractual Clauses, or Binding Corporate Rules).

{{DPA_CLAUSE}}.5 {{PROVIDER}} shall notify {{CLIENT}} without undue delay (and in any event within {{BREACH_HOURS}} hours) upon becoming aware of any Personal Data breach.

{{DPA_CLAUSE}}.6 Upon termination, {{PROVIDER}} shall, at {{CLIENT}}'s election, return or securely delete all Personal Data within {{DATA_RETURN_DAYS}} days and certify deletion in writing, subject to any legal retention obligations.
```

### Jurisdiction Notes

| Jurisdiction | Key Consideration |
|---|---|
| NL | AP (Autoriteit Persoonsgegevens) is supervisory authority. GDPR applies directly. |
| NO | Datatilsynet is supervisory authority. GDPR applies via EEA Agreement. Personopplysningsloven supplements. |
| UK | ICO is supervisory authority. UK GDPR + DPA 2018. UK International Data Transfer Agreement / UK Addendum to EU SCCs for EEA-UK transfers. |
| US | No federal omnibus. CCPA/CPRA (California), sectoral (HIPAA, GLBA). DPA structure differs -- "service provider" under CCPA, not "processor". |

---

## 10. Governing Law and Dispute Resolution

**Used in:** All agreement types

### Skeleton

```
{{GL_CLAUSE}}.1 This Agreement shall be governed by and construed in accordance with the laws of {{GOVERNING_LAW}}, without regard to its conflict of laws principles.

{{GL_CLAUSE}}.2 The United Nations Convention on Contracts for the International Sale of Goods (CISG) is expressly excluded.

{{DR_CLAUSE}}.1 The Parties shall attempt to resolve any dispute arising out of or in connection with this Agreement by good faith negotiation between senior representatives within {{NEGOTIATION_DAYS}} Business Days of written notice of the dispute.

{{DR_CLAUSE}}.2 [Arbitration] If the dispute is not resolved under Clause {{DR_CLAUSE}}.1, it shall be finally resolved by arbitration under the rules of {{ARBITRAL_INSTITUTION}}, by {{NUM_ARBITRATORS}} arbitrator(s), with the seat of arbitration in {{SEAT}}, conducted in {{LANGUAGE}}.

{{DR_CLAUSE}}.2 [Litigation alternative] If the dispute is not resolved under Clause {{DR_CLAUSE}}.1, the courts of {{JURISDICTION}} shall have exclusive jurisdiction.

{{DR_CLAUSE}}.3 Nothing in this Clause prevents either Party from seeking interim or injunctive relief from any court of competent jurisdiction.
```

### Common Pairings

| Governing Law | Court/Tribunal | Typical Use |
|---|---|---|
| Netherlands | Amsterdam District Court / NAI arbitration | Dutch entities, NL-seated projects |
| Norway | Oslo tingrett / OCC/NCC arbitration | Norwegian entities |
| England & Wales | English Commercial Court / LCIA | International contracts, finance |
| New York | NY Supreme Court Commercial Division / AAA/JAMS | US domestic, finance |
| Delaware | Delaware Court of Chancery | Corporate governance, M&A |

---

## 11. Assignment and Change of Control

**Used in:** All agreement types

### Skeleton

```
{{ASS_CLAUSE}}.1 Neither Party may assign, transfer, charge, or otherwise deal with any of its rights or obligations under this Agreement without the prior written consent of the other Party (such consent not to be unreasonably withheld or delayed).

{{ASS_CLAUSE}}.2 Notwithstanding Clause {{ASS_CLAUSE}}.1, a Party may assign this Agreement to an Affiliate without consent, provided:
(a) the assignor remains liable for the Affiliate's performance; and
(b) the assignor notifies the other Party within {{ASSIGNMENT_NOTICE}} Business Days.

{{ASS_CLAUSE}}.3 This Agreement shall be binding on and enure to the benefit of the Parties and their permitted successors and assigns.
```

---

## 12. General Boilerplate

### No Oral Modification

```
No amendment to this Agreement shall be effective unless in writing and signed by or on behalf of both Parties.
```

### Waiver

```
A failure or delay by a Party to exercise any right under this Agreement shall not constitute a waiver of that right. A waiver of any breach shall not constitute a waiver of any subsequent breach. Any waiver shall be effective only if in writing.
```

### Severability

```
If any provision of this Agreement is held to be invalid, illegal, or unenforceable, the remaining provisions shall continue in full force and effect. The invalid provision shall be replaced by a valid provision that most closely reflects the Parties' original commercial intention.
```

### Entire Agreement

```
This Agreement (including its Schedules) constitutes the entire agreement between the Parties and supersedes all prior negotiations, representations, and agreements (whether written or oral) relating to its subject matter. Nothing in this Clause limits liability for fraud or fraudulent misrepresentation.
```

### Counterparts and E-Signature

```
This Agreement may be executed in any number of counterparts, each of which shall constitute an original, and all of which together shall constitute one and the same agreement. This Agreement may be executed by electronic signature, which shall have the same legal effect as a handwritten signature.
```

### Notices

```
Any notice under this Agreement shall be in writing and delivered by hand, recorded mail, reputable courier, or email (with delivery confirmation) to the address specified in the preamble. Deemed delivery: (a) hand: on delivery; (b) recorded mail: {{DOMESTIC_DAYS}} Business Days after posting (domestic), {{INTL_DAYS}} Business Days (international); (c) courier: next Business Day (domestic), {{COURIER_INTL_DAYS}} Business Days (international); (d) email: on the Business Day sent if before 17:00, otherwise the next Business Day.
```

---

## 13. Survival

### Skeleton

```
The following Clauses shall survive termination or expiry of this Agreement: Clause {{DEF_CLAUSE}} (Definitions), Clause {{CONF_CLAUSE}} (Confidentiality), Clause {{IP_CLAUSE}} (Intellectual Property), Clause {{LOL_CLAUSE}} (Limitation of Liability), Clause {{INDEM_CLAUSE}} (Indemnification), Clause {{CONSEQ_CLAUSE}} (Consequences of Termination), Clause {{GL_CLAUSE}} (Governing Law), and Clause {{DR_CLAUSE}} (Dispute Resolution).
```

**Note:** Always enumerate surviving clauses by number. "Provisions which by their nature should survive" creates ambiguity and should be avoided.

---

## Usage Guide

### Selecting Clauses by Document Type

| Document Type | Essential Clauses from this Library |
|---|---|
| NDA | 1, 2, 3 (expanded), 4, 6, 10, 12, 13 |
| Service Agreement | All (1-13) |
| MSA | All (1-13) + order form mechanics |
| SPA | 1, 2, 3, 4 (as warranty cap), 5, 6, 10, 11, 12, 13 |
| SHA | 1, 2, 3, 4, 6, 10, 11, 12, 13 |
| License Agreement | 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13 |
| EPC Contract | 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13 |
| Employment Agreement | 1, 2, 3, 8 (adapted), 10, 12 |
| Settlement Agreement | 1, 2, 3, 4, 10, 12, 13 |

### Jurisdiction Application Order

1. Start with the universal skeleton from this library
2. Load the relevant jurisdiction's `contract-law.md` for mandatory adaptations
3. Apply the jurisdiction notes from each clause section
4. Load the jurisdiction's `terminology.md` for bilingual terms (NL, NO)
5. Review against the jurisdiction's `overview.md` for systemic considerations
