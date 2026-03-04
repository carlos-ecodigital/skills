# NDA Redline Playbook

Pre-drafted redlines for common NDA issues. Each redline includes the issue, risk assessment, preferred language, fallback position, walk-away trigger, and tone guidance.

**Usage:** When the review workflow identifies DEFEND or NEGOTIATE items, pull the relevant redline from this playbook. Apply only DEFEND + NEGOTIATE items (never raise ACCEPT items). Limit each redline round to 3-4 points maximum.

---

## Redline Principles

1. **Maximum 3-4 points per round.** If you have more, either the NDA is genuinely problematic (escalate per authority matrix) or you are over-lawyering (accept more).
2. **Frame as mutual benefit.** "This simplifies the agreement for both parties" beats "this is unacceptable to us."
3. **One sentence of reasoning per ask.** The counterparty's lawyer does not need a legal brief — they need to see the ask is reasonable and move on.
4. **Collaborative spirit.** The goal is to sign, not to win. Every redline should make the counterparty think DE is professional, reasonable, and fast.
5. **Know when to stop.** If the counterparty pushes back on a NEGOTIATE item, accept it. Save credibility for DEFEND items.

---

## Redline Items

### 1. Overbroad One-Sided CI Definition
**Priority:** NEGOTIATE
**Trigger:** One-way NDA where DE is Recipient and CI definition covers "all information whatsoever" or "all information of any nature" without Purpose limitation.
**Risk:** DE could inadvertently breach by using general knowledge gained during discussions. Overbroad definitions in one-sided NDAs create disproportionate exposure.

**Preferred language:**
> "Confidential Information" means all information disclosed by the Discloser to the Recipient **in connection with the Purpose**, whether in writing, orally, electronically, or by inspection, that is marked as confidential or that by its nature or the circumstances of disclosure would reasonably be understood to be confidential.

**Fallback:** Accept if the NDA is mutual (broad mutual definition protects DE equally).
**Walk-away:** Not a walk-away issue.
**Tone:** "We'd suggest tying the definition to the Purpose to ensure clarity for both parties on what's covered."

---

### 2. Missing Standard Exclusions
**Priority:** DEFEND
**Trigger:** Any of the four standard exclusions absent: (a) public domain, (b) prior knowledge, (c) independent development, (d) third-party receipt without breach.
**Risk:** Without exclusions, DE could be liable for information it already possessed or independently developed. This is a fundamental NDA deficiency.

**Preferred language:**
> The obligations in this Agreement do not apply to information that the Receiving Party can demonstrate: (a) is or becomes publicly available through no fault of the Receiving Party or its Representatives; (b) was already in the lawful possession of the Receiving Party before disclosure, without restriction as to use or disclosure; (c) was independently developed by the Receiving Party without use of or reference to the Confidential Information; or (d) was received from a third party who was not, to the Receiving Party's knowledge, under any obligation of confidentiality in respect of that information.

**Fallback:** None. All four exclusions are required.
**Walk-away:** If counterparty refuses to include standard exclusions, escalate per authority matrix (likely UNACCEPTABLE).
**Tone:** "The standard four exclusions appear to be missing. These are market-standard in virtually all NDAs and protect both parties equally. We'd ask that they be included."

---

### 3. No Compliance Retention Exception
**Priority:** NEGOTIATE
**Trigger:** Return/destruction clause requires return or destruction of all copies without any carve-out for legal, regulatory, or compliance retention.
**Risk:** DE may be required to retain certain information for regulatory, tax, or compliance purposes. A blanket destruction obligation creates an impossible compliance conflict.

**Preferred language:**
> The Receiving Party may retain copies of Confidential Information to the extent required by applicable law, regulation, or its internal compliance policies, provided such retained copies remain subject to the confidentiality obligations of this Agreement.

**Fallback:** Accept if counterparty adds a narrower carve-out (e.g., "to the extent required by applicable law or regulation" without the internal compliance policies element).
**Walk-away:** Not a walk-away issue.
**Tone:** "We'd suggest adding a standard compliance retention carve-out — this is practical for both parties given regulatory requirements."

---

### 4. Blanket Electronic Copies Prohibition
**Priority:** NEGOTIATE
**Trigger:** Return/destruction clause requires purging "all electronic copies including backup drives and cloud storage" without carve-out for automated systems.
**Risk:** Modern IT generates automated backups that cannot be selectively purged. Requiring certification of complete electronic destruction is impractical and creates a perpetual compliance risk.

**Preferred language:**
> Notwithstanding the foregoing, the Receiving Party shall not be required to purge Confidential Information from automated backup or archival systems, provided that such information is not accessed or used except as required by applicable law, and the confidentiality obligations of this Agreement continue to apply to any retained copies.

**Fallback:** Accept if counterparty narrows to "use commercially reasonable efforts to purge electronic copies from active systems."
**Walk-away:** Not a walk-away issue.
**Tone:** "The electronic copies obligation is impractical for modern IT environments — automated backups can't be selectively purged. We'd suggest adding a standard carve-out that keeps the confidentiality obligations in place."

---

### 5. "Indemnity Basis" Costs
**Priority:** NEGOTIATE (always — DE policy)
**Trigger:** Indemnity clause specifies costs "on an indemnity basis" or "on a full indemnity basis."
**Risk:** "Indemnity basis" means the breaching party pays full actual legal costs without judicial assessment of reasonableness. For a startup, this exposure is disproportionate. "Reasonable and documented costs" provides equivalent practical protection while capping unreasonable spending.

**Preferred language:**
> ... including reasonable and documented costs incurred in connection with such breach.

**Alternative preferred:**
> ... including costs on the standard basis.

**Fallback:** Accept "reasonable costs" without "documented" qualifier.
**Walk-away:** Not a walk-away issue (this is a NEGOTIATE item), but always raise it. It is a low-effort, high-signal ask that demonstrates DE reads the document carefully.
**Tone:** "We'd suggest 'reasonable and documented costs' rather than 'indemnity basis' — this is standard commercial practice and still provides full protection."

---

### 6. One-Way or Disproportionate Indemnity
**Priority:** DEFEND
**Trigger:** DE indemnifies the counterparty for breach but the counterparty does not indemnify DE. Or: indemnity includes indirect, consequential, or special damages. Or: indemnity has no cap in NDA context.
**Risk:** One-sided financial exposure with no reciprocal protection. Uncapped indemnity for an NDA is disproportionate to the risk profile of a confidentiality agreement.

**Preferred language (make mutual):**
> Each Party shall indemnify the other Party against all losses, damages, and reasonable and documented costs arising from a breach of this Agreement by the indemnifying Party or its Representatives.

**Preferred language (add cap if uncapped):**
> The aggregate liability of each Party under this Clause shall not exceed [EUR amount / a reasonable pre-agreed sum].

**Fallback:** If counterparty insists on asymmetry, negotiate: (a) reasonable cap on DE's indemnity, and (b) exclusion of indirect/consequential damages.
**Walk-away:** One-way uncapped indemnity without limitation is a Critical Red flag (authority matrix: UNACCEPTABLE). Do not sign without resolution.
**Tone:** "The indemnity as drafted is one-sided. We'd propose making it mutual — this is standard for a mutual NDA and reflects the equal obligations both parties are undertaking."

---

### 7. Reverse Burden of Proof
**Priority:** DEFEND
**Trigger:** Clause requiring the Receiving Party to demonstrate it did not use Confidential Information for an unauthorised purpose, based on the Disclosing Party's "reasonable opinion" that a breach has occurred. (Example: Stelia cl.7 "Establishing Purpose of Use.")
**Risk:** Reverses the normal burden of proof. Creates a subjective trigger ("reasonable opinion") that forces DE to prove a negative. Combined with full-cost indemnity, this creates a low-bar trigger with high-cost consequences (compound risk).

**Preferred language:** Remove the clause entirely.

**Fallback:** If counterparty insists on retaining something: "Each Party acknowledges that Confidential Information shall be used solely for the Purpose. In the event of a dispute regarding the use of Confidential Information, the burden of proof shall rest with the Party alleging misuse."

**Walk-away:** If removal is refused and fallback is rejected, escalate per authority matrix. This clause compounds with indemnity provisions.
**Tone:** "We'd propose removing Clause [X]. In a mutual NDA where both parties are equally bound, the standard confidentiality obligations provide sufficient protection without a reverse burden of proof mechanism. This simplifies the agreement for both sides."

---

### 8. No Legal Compulsion Prior Notice
**Priority:** DEFEND
**Trigger:** NDA has no legal compulsion carve-out, or has a carve-out without any requirement for prior notice to the Disclosing Party.
**Risk:** Without prior notice, the Disclosing Party has no opportunity to seek a protective order or limit the scope of legally compelled disclosure. This is a fundamental protective mechanism.

**Preferred language:**
> The Receiving Party may disclose Confidential Information to the extent required by applicable law, regulation, court order, or the rules of any relevant regulatory authority, provided that (where legally permitted) the Receiving Party: (a) gives the Disclosing Party prior written notice as soon as reasonably practicable; (b) consults with the Disclosing Party regarding the scope and manner of disclosure; and (c) discloses only the minimum information required to comply.

**Fallback:** Accept without the "consults with" element if counterparty views it as impractical. The prior notice is the critical element.
**Walk-away:** If counterparty refuses any form of prior notice, escalate. This is a standard protective mechanism.
**Tone:** "We'd ask for a prior notice requirement on legally compelled disclosures — this is standard and gives both parties the opportunity to seek protective measures."

---

### 9. No Financing Source Carve-Out
**Priority:** NEGOTIATE
**Trigger:** Permitted disclosures do not include bona fide financing sources or potential co-investors.
**Risk:** DE needs to share certain counterparty information with its financing sources during fundraising and project finance activities. Without this carve-out, DE would breach the NDA every time it discusses the deal with a potential investor or lender.

**Preferred language:**
> The Receiving Party may disclose Confidential Information to its bona fide financing sources and potential co-investors, provided such persons are bound by obligations of confidentiality no less restrictive than those in this Agreement.

**Fallback:** Accept a narrower formulation: "bona fide lenders" without "co-investors" if counterparty resists.
**Walk-away:** Not a walk-away issue, but flag as a practical risk for Carlos's awareness.
**Tone:** "We'd suggest adding a standard financing source carve-out — this is practical for both parties and subject to equivalent confidentiality protections."

---

### 10. Representatives Limited to Employees Only
**Priority:** NEGOTIATE
**Trigger:** Definition of Representatives is limited to "employees and directors" without including professional advisers (lawyers, accountants, auditors).
**Risk:** DE needs to share CI with its legal and financial advisers for deal evaluation. Without adviser inclusion, routine professional consultation would breach the NDA.

**Preferred language:**
> "Representatives" means, in relation to a Party, its Affiliates, and its and their respective directors, officers, employees, agents, and professional advisers (including lawyers, accountants, and financial advisers).

**Fallback:** Accept "professional advisers bound by professional duty of confidentiality" as a qualifier.
**Walk-away:** Not a walk-away issue.
**Tone:** "We'd suggest including professional advisers in the definition of Representatives — both parties will need to consult their legal and financial advisers in connection with the Purpose."

---

### 11. One-Way Non-Solicitation
**Priority:** DEFEND (if one-way) / NEGOTIATE (if mutual but unreasonable)
**Trigger:** Non-solicitation clause restricts only DE from soliciting the counterparty's employees, without reciprocal obligation. Or: mutual but without general recruitment carve-out.
**Risk:** One-way non-solicitation creates an asymmetric restriction that limits DE's ability to hire talent. Even mutual non-solicitation should include a carve-out for general advertisements and unsolicited approaches.

**Preferred language (make mutual with carve-out):**
> During the term of this Agreement and for 12 months thereafter, neither Party shall, without the prior written consent of the other, directly solicit or entice away any employee or officer of the other Party who has been involved in the Purpose. This restriction does not apply to general recruitment advertisements or approaches by recruitment agencies not specifically targeting the other Party's personnel.

**Fallback:** Accept mutual non-solicitation for 12 months with general recruitment carve-out.
**Walk-away:** One-way non-solicitation without reciprocal obligation: escalate if counterparty refuses to make mutual.
**Tone:** "We'd propose making the non-solicitation mutual and adding a standard carve-out for general recruitment — this is fair to both sides."

---

### 12. NC Without Scope Limits or Duration Cap
**Priority:** NEGOTIATE
**Trigger:** Non-circumvention clause without defined Protected Contacts, or without a fixed duration, or with an overly broad scope.
**Risk:** Unbounded NC creates perpetual, undefined restrictions. NC should be specific (named contacts or specific introductions) and time-limited (maximum 3 years for NDA-level NC).

**Preferred language:**
> The Protected Contacts under this Agreement are: [specific named persons or entities]. The obligations in this Clause shall continue for [24/36] months from the date of this Agreement.

**Fallback:** Accept a broader formulation ("persons introduced by the Discloser in connection with the Purpose") provided there is a fixed duration cap of no more than 36 months.
**Walk-away:** NC without any scope limitation or duration cap: escalate. Open-ended NC is commercially unreasonable.
**Tone:** "We're happy to include non-circumvention protections — we'd suggest defining the Protected Contacts specifically and adding a duration cap, which is standard practice."

---

### 13. NC Addendum Needed (DE Initiates)
**Priority:** NEGOTIATE (DE's ask)
**Trigger:** Counterparty NDA has no NC clause, but the deal context involves DE sharing grower identities, site locations, or other introduction-sensitive information with a neocloud buyer or broker/intermediary.
**Risk:** Without NC protection, the counterparty could bypass DE and approach growers or site contacts directly after receiving the information through DE.

**Preferred language (propose as addendum or additional clause):**
> **Non-Circumvention.** The Recipient shall not, directly or indirectly, without the prior written consent of the Discloser: (a) contact, deal with, or enter into any business relationship with any Protected Contact; (b) circumvent, avoid, or bypass the Discloser in order to deal directly with any Protected Contact; or (c) attempt to divert or appropriate any business opportunity disclosed by the Discloser in connection with the Purpose. "Protected Contacts" means: [list specific growers, site contacts, or introductions]. This obligation continues for [24/36] months from the date of this Agreement.

**Alternative approach:** Withhold site-specific and grower-identifying information until a more protective agreement (NCNDA or commercial agreement with NC) is in place.

**Fallback:** Accept a narrower NC covering only named contacts (not categories).
**Walk-away:** If counterparty refuses any NC protection and DE needs to share grower/site information, do not share the sensitive information under the NDA alone. Propose signing a separate NCNDA.
**Tone:** "Before we share site-specific information, we'd like to include a non-circumvention clause covering the specific contacts we'll be introducing. This is standard practice for intermediary introductions and protects the value of the relationship for both sides."

---

### 14. Assignment Without Affiliate Carve-Out
**Priority:** NEGOTIATE
**Trigger:** Assignment clause prohibits all assignment without consent, with no carve-out for intra-group transfers to Affiliates.
**Risk:** DE may restructure or transfer obligations to a subsidiary as part of normal corporate development. A blanket prohibition without Affiliate carve-out creates unnecessary friction for routine corporate actions.

**Preferred language:**
> Neither Party may assign this Agreement without the prior written consent of the other Party (not to be unreasonably withheld), except to an Affiliate, provided the assignor remains liable for its obligations under this Agreement.

**Fallback:** Accept "with prior written consent, not to be unreasonably withheld" without the Affiliate carve-out.
**Walk-away:** Not a walk-away issue.
**Tone:** "We'd suggest adding a standard Affiliate assignment carve-out — this is practical for both parties and the assignor remains liable."

---

### 15. Blanket Announcement Restriction Without Carve-Out
**Priority:** NEGOTIATE
**Trigger:** Media/announcement clause prohibits any public disclosure of the existence of the NDA or discussions, without carve-out for required regulatory or stock exchange disclosures.
**Risk:** DE may be required to disclose the existence of discussions (not the content) for regulatory or corporate governance purposes. A blanket prohibition without a regulatory carve-out creates a compliance conflict.

**Preferred language:**
> Neither Party shall make any public announcement concerning the existence or subject matter of this Agreement without the prior written consent of the other Party, except as required by applicable law, regulation, or the rules of any relevant regulatory authority or stock exchange.

**Fallback:** Accept the restriction as drafted if it already includes a legal compulsion carve-out (many announcement clauses do).
**Walk-away:** Not a walk-away issue.
**Tone:** "We'd suggest adding a regulatory carve-out to the announcement restriction — this ensures compliance for both parties."

---

## Cover Email Framework

### Principles
- Always collaborative spirit. Match formality to the relationship.
- Frame redlines as "in both parties' interests" or "standard commercial practice."
- Maximum 3-4 points per email. If you have more, the NDA may need escalation.
- One sentence of reasoning per ask. Brief and professional.
- Close with an offer to discuss by call. Shows good faith and speeds resolution.

### Tone by Counterparty Type

Select tone based on the counterparty categorization from nda-review-workflow.md Phase 1, Step 1.4 (per nda-policy-positions.md Section 10.6).

| Counterparty | Tone | Key Adjustments |
|---|---|---|
| Neocloud buyer | Professional, efficient, tech-fluent | Short. "Two quick comments." Speed signals competence. No legalese. |
| Investor (VC/PE/family office) | Formal, legally sophisticated | Precise. Cite clause numbers. Their lawyers will review — write for that audience. |
| Grower partner | Warm, plain language, patient | Simple terms. Explain why each ask matters in practical terms. Avoid legal jargon. |
| Vendor / service provider | Straightforward, businesslike | "Let's get this done." Minimal preamble. Efficient and direct. |
| Advisor / consultant | Collegial, collaborative | "Let's make sure we're both covered." Conversational but precise. |
| Broker / intermediary | Careful, NC-focused | Direct about NC scope and duration. They understand why DE is asking — don't over-explain. |

**Leverage adjustment to tone (per authority-matrix.md Section 7):**
- **They have leverage:** More appreciative opening. Lead with thanks. Frame asks as "minor." Use "we'd suggest" not "we require."
- **Roughly equal:** Balanced, professional. Standard templates apply as-is.
- **DE has leverage:** More direct. Frame asks as "our standard position." Can use "we require" for DEFEND items.

### Template: Standard Redline (2-3 Points)

> Subject: [Counterparty] / DE — NDA comments
>
> Dear [Name],
>
> Thank you for sending through the NDA. We've reviewed it and have [two/three] minor comments:
>
> 1. **[Clause reference] ([Short description]):** [One-sentence ask]. [One-sentence reasoning].
>
> 2. **[Clause reference] ([Short description]):** [One-sentence ask]. [One-sentence reasoning].
>
> 3. **[Clause reference] ([Short description]):** [One-sentence ask]. [One-sentence reasoning].
>
> We're happy to discuss these by call if useful. Otherwise, if you're comfortable with these changes, we can sign promptly.
>
> Best regards,
> [Name]

### Template: Single Critical Redline

> Subject: [Counterparty] / DE — NDA: one comment
>
> Dear [Name],
>
> Thank you for the NDA — it's well drafted and we're comfortable with the vast majority of terms. We have one point we'd like to address:
>
> **[Clause reference]:** [Ask]. [Reasoning]. [Brief explanation of why this matters for both parties].
>
> Happy to discuss by call if easier. Otherwise, we'd appreciate the amendment and can sign straight away.
>
> Best regards,
> [Name]

### Template: NC Addendum Request

> Subject: [Counterparty] / DE — NDA + non-circumvention
>
> Dear [Name],
>
> Thank you for the NDA. Before we proceed to sharing site-specific information, we'd like to include a non-circumvention clause covering the contacts and sites we'll be discussing.
>
> This is standard practice for introductions of this nature and protects the value of the relationship for both sides. We've drafted a short addendum [attached / below] — happy to discuss the scope and duration.
>
> We can sign both documents together and move forward quickly.
>
> Best regards,
> [Name]

### Template: Pushing DE's Template First

> Subject: [Counterparty] / DE — NDA
>
> Dear [Name],
>
> Thank you for reaching out. We've already prepared our standard NDA for this discussion — attached for your review. It's mutual, market-standard, and should be straightforward.
>
> Happy to discuss any questions or comments you may have. We'd like to get this signed quickly so we can move forward with the conversation.
>
> Best regards,
> [Name]

---

## Quick Reference: Priority Summary

| # | Issue | Default Priority | When to Raise |
|---|---|---|---|
| 1 | Overbroad one-sided CI | NEGOTIATE | Only in one-way NDAs where DE is Recipient |
| 2 | Missing standard exclusions | DEFEND | Always if any of the four are absent |
| 3 | No compliance retention | NEGOTIATE | Always — low-effort, standard ask |
| 4 | Electronic copies prohibition | NEGOTIATE | When blanket "purge all" with no carve-out |
| 5 | "Indemnity basis" costs | NEGOTIATE | Always — DE policy |
| 6 | One-way/disproportionate indemnity | DEFEND | When asymmetric or uncapped |
| 7 | Reverse burden of proof | DEFEND | Always — request removal |
| 8 | No legal compulsion notice | DEFEND | When absent entirely |
| 9 | No financing source carve-out | NEGOTIATE | When missing — DE needs this for fundraise |
| 10 | Representatives = employees only | NEGOTIATE | When professional advisers excluded |
| 11 | One-way non-solicitation | DEFEND/NEGOTIATE | DEFEND if one-way; NEGOTIATE if mutual without carve-out |
| 12 | NC without scope/duration | NEGOTIATE | When NC present but unbounded |
| 13 | NC addendum needed | NEGOTIATE | When DE needs NC but NDA omits it |
| 14 | No Affiliate assignment carve-out | NEGOTIATE | When blanket prohibition without carve-out |
| 15 | Blanket announcement restriction | NEGOTIATE | When no regulatory carve-out |
