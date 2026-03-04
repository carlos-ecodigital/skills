# United Kingdom -- Contract Law

## Governing Framework

English contract law is **common law** (case-law-based), supplemented by key statutes. There is no single civil code equivalent to the Dutch BW or Swiss OR. The primary sources are:

| Source | Role |
|---|---|
| Common law (case law) | Core contract principles: formation, interpretation, remedies, breach |
| Unfair Contract Terms Act 1977 (UCTA) | Controls exclusion/limitation clauses in B2B contracts |
| Consumer Rights Act 2015 (CRA) | B2C fairness (not relevant for DE's commercial NDAs) |
| Contracts (Rights of Third Parties) Act 1999 (TPA) | Third-party enforcement rights |
| Misrepresentation Act 1967 | Pre-contractual misrepresentation |
| Law of Property (Miscellaneous Provisions) Act 1989 | Deeds |
| Limitation Act 1980 | Limitation periods |

**Key contrast with civil law:** No overarching good faith doctrine. No statutory gap-filling. Contracts are self-contained instruments — the court enforces what the parties agreed, not what seems fair.

---

## Contract Formation

English law requires four elements for a binding contract:

| Element | Rule | NDA Relevance |
|---|---|---|
| **Offer** | Clear, certain terms capable of acceptance | NDA sent for signature = offer |
| **Acceptance** | Unqualified assent to the offer | Signing = acceptance. Counter-offer kills original offer (Hyde v Wrench) |
| **Consideration** | Something of value exchanged. Past consideration is no consideration (Roscorla v Thomas) | In mutual NDAs: mutual promises to maintain confidentiality = good consideration. One-way NDAs: receiving confidential information = consideration |
| **Intention to create legal relations** | Presumed in commercial context (Edwards v Skyways) | Satisfied for all commercial NDAs |

**Consideration and NDA modifications:** If the parties want to amend an NDA (e.g., extend term, change scope), the amendment needs fresh consideration or must be executed as a deed. Contrast with NL where amendments to existing contracts do not require separate consideration.

**Deeds:** A deed requires: (a) writing, (b) clear statement that it is a deed, (c) signature, (d) attestation by a witness, and (e) delivery. Companies can execute deeds under s.44 Companies Act 2006 (two directors, or one director + company secretary, or common seal).

---

## UCTA 1977 — Reasonableness Test

Critical for NDA enforceability. UCTA applies to **B2B contracts** and controls exclusion and limitation clauses.

### Key Sections

| Section | Effect | NDA Relevance |
|---|---|---|
| s.2(1) | Cannot exclude liability for death or personal injury caused by negligence | Rarely relevant to NDAs |
| s.2(2) | Can only exclude liability for other loss caused by negligence if the term is **reasonable** | Relevant if NDA disclaims liability for negligent disclosure |
| s.3 | Where one party deals on the other's **written standard terms**: cannot exclude liability for breach, or claim to render substantially different performance, unless reasonable | Applies when counterparty's NDA is their standard form — their limitation/exclusion clauses must pass reasonableness |
| s.11 | **Reasonableness test**: the term must be fair and reasonable having regard to all circumstances known or contemplated at the time of contracting | See guidelines below |

### Reasonableness Guidelines (s.11 + Schedule 2)

Courts consider:
1. **Relative bargaining positions** — Were the parties on equal footing?
2. **Inducement** — Was there any inducement to agree to the term (discount, benefit)?
3. **Knowledge** — Did the party know or ought to have known of the term's existence and extent?
4. **Practicability of compliance** — Could the condition for liability reasonably be complied with?
5. **Custom-made or off-the-shelf** — Was the term individually negotiated or part of standard terms?

**NDA application:** Overbroad indemnity clauses, one-sided limitation of liability, or exclusion of remedies in a counterparty's standard-form NDA may fail the UCTA reasonableness test. If DE is presented with a counterparty's standard-form NDA containing aggressive exclusion clauses, UCTA provides a backstop — but it is better to redline than rely on a court to strike the term down.

---

## Interpretation Principles

English law takes an **objective approach** to contractual interpretation. The court asks what a reasonable person with all the background knowledge available to the parties would have understood the parties to have meant.

### Key Cases

| Case | Principle |
|---|---|
| **ICS v West Bromwich** [1998] | The meaning of a document is what a reasonable person with the background knowledge available to the parties would have understood the author to be using the words to mean |
| **Arnold v Britton** [2015] | Warns against departing from natural meaning of words on the basis of commercial common sense alone. Clear words prevail even if the outcome seems uncommercial |
| **Wood v Capita** [2017] | Iterative process: consider the natural and ordinary meaning of the clause, read in the context of the contract as a whole, informed by commercial common sense |
| **Rainy Sky v Kookmin** [2011] | Where there are two possible constructions, the court should prefer the construction consistent with business common sense |

### Contrast with Civil Law

| Issue | English Law | Dutch Law (Haviltex) | Practical Impact |
|---|---|---|---|
| Starting point | Objective meaning of the words | Subjective intent of the parties | English courts focus on the document; Dutch courts consider wider context |
| Good faith gap-filling | No general duty of good faith (Walford v Miles [1992]) | Art. 6:248 BW supplements and overrides | English law will not imply reasonable terms to cure a bad bargain |
| Entire agreement clause | Effective. Excludes pre-contractual representations and prior agreements | May be overridden by redelijkheid en billijkheid | In English law, the four corners of the NDA are the whole agreement |
| Parol evidence | Generally excluded by entire agreement clause | Haviltex allows extrinsic evidence | Drafting accuracy matters more in English law — what you write is what you get |
| Contra proferentem | Ambiguity construed against the drafter | Similar principle exists | Counterparty-drafted NDA: ambiguity may be read in DE's favour |

**NDA implication:** Every clause in an English law NDA matters. Courts will not read down aggressive terms using good faith. If a clause says something unfavourable, assume the court will enforce it as written. Redline rather than assume judicial moderation.

---

## Boilerplate Reliance

English law contracts are **self-contained**. Courts will not readily imply terms that contradict express provisions.

**Implied terms** (only if):
1. **Business efficacy** — The term is necessary to make the contract work (The Moorcock [1889])
2. **Officious bystander** — The term is so obvious it goes without saying (Shirlaw v Southern Foundries [1939])
3. **Statute** — Certain terms are implied by statute (e.g., Sale of Goods Act 1979)

**Threshold is high:** The test from Marks & Spencer v BNP Paribas [2015] requires that the term would spell out what the contract actually means. Courts do not imply terms to make a contract fairer or to improve a bad bargain.

**NDA implication:** Boilerplate clauses (entire agreement, severability, waiver, assignment) are not mere decoration. They control how the contract is interpreted and enforced. Missing boilerplate in an English law NDA creates genuine gaps that the court will not fill with reasonable defaults.

---

## Equitable Remedies

### Injunctions

The primary enforcement mechanism for NDAs under English law.

| Type | Purpose | Threshold |
|---|---|---|
| **Interim injunction** | Preserve the position pending trial | American Cyanamid test (see below) |
| **Final injunction** | Permanent restraint after trial | Balance of justice; discretionary |
| **Without notice (ex parte)** | Extreme urgency where delay would cause irreparable harm | Must show real urgency + full and frank disclosure |

### American Cyanamid Test (Interim Injunctions)

From American Cyanamid v Ethicon [1975]:

1. **Serious question to be tried** — Is there a genuine issue? (Low threshold)
2. **Damages not adequate** — Would damages compensate the claimant? For confidential information, damages are often inadequate because the harm is irreversible.
3. **Balance of convenience** — Which party would suffer more harm if the injunction is granted/refused?
4. **Undertaking in damages** — The applicant must undertake to compensate the respondent if the injunction turns out to have been wrongly granted.

**NDA clause relevance:** Clauses acknowledging that breach "may cause irreparable harm for which damages would not be an adequate remedy" (as in Stelia cl.8.6) are **enforceable and meaningful** under English law. They pre-empt argument on step 2 of American Cyanamid.

### Specific Performance

Rarely ordered for NDA obligations (obligation is negative — to not disclose — so the remedy is an injunction, not specific performance).

---

## Limitation Periods

The Limitation Act 1980 governs time limits for bringing claims.

| Claim Type | Period | Start Date | Section |
|---|---|---|---|
| Breach of contract (simple contract) | **6 years** | Date of breach | s.5 |
| Breach of contract (deed) | **12 years** | Date of breach | s.8 |
| Tort (negligence) | 6 years | Date damage occurs | s.2 |
| Fraud | 6 years | Date of discovery | s.32 |
| Contribution claims | 2 years | Date of judgment or settlement | s.10 |

**Key differences from civil law:**
- **No discovery rule for contract claims:** Time runs from the date of breach, not from when the claimant discovers the breach. Contrast with NL where limitation runs from knowledge.
- **Deed vs simple contract:** If the NDA is executed as a deed, the limitation period doubles to 12 years.

**NDA implication:** A perpetual NDA with English governing law still has a 6-year limitation on bringing breach claims (unless executed as a deed). This is a natural backstop even for NDAs with perpetual confidentiality obligations.

---

## Penalty Clause Doctrine

### The Test: Cavendish v Makdessi / ParkingEye v Beavis [2015]

The Supreme Court reformulated the penalty rule. A clause is a penalty (and therefore unenforceable) if it:
- Imposes a **detriment on the contract-breaker** that is **out of all proportion to any legitimate interest** of the innocent party in the enforcement of the obligation.

**Legitimate interests** include: compensation for loss, deterring breach, and protecting goodwill or reputation.

**What this means for NDAs:**
- A liquidated damages clause in an NDA pegged to actual loss or reasonable pre-estimate = enforceable.
- A clause imposing a fixed sum grossly disproportionate to likely harm = potentially a penalty.
- Indemnity clauses (as opposed to liquidated damages) are generally not caught by the penalty doctrine because they compensate for actual loss rather than imposing a pre-determined sum.

---

## Contracts (Rights of Third Parties) Act 1999

### Core Rule (s.1)

A person who is not a party to the contract may enforce a term if:
- The contract **expressly provides** that the third party may enforce it (s.1(1)(a)); or
- The term purports to **confer a benefit** on the third party (s.1(1)(b)), unless the parties did not intend the term to be enforceable by the third party.

The third party must be **expressly identified** in the contract by name, as a member of a class, or by description (s.1(3)).

### Variation and Rescission (s.2)

The parties cannot vary or rescind the contract to extinguish the third party's right without the third party's consent if:
- The third party has communicated assent to the promisor; or
- The third party has relied on the term.

### NDA Application

Many NDAs include TPA 1999 clauses granting enforcement rights to Affiliates (e.g., Stelia cl.11.7). This means:
- Each Affiliate can independently enforce the NDA without being a signatory.
- The parties cannot amend the NDA to remove Affiliate rights without Affiliate consent (if the Affiliate has relied).
- This extends the enforcement universe beyond the two signatory parties.

**Drafting note:** If DE wants to limit TPA 1999 rights, the NDA should include an explicit exclusion clause: "The Contracts (Rights of Third Parties) Act 1999 does not apply to this Agreement." This is standard boilerplate in English law contracts where parties want to control the scope of enforcement.

---

## Key Differences: English vs Civil Law Summary

| Issue | English Law | Dutch Law | Swiss Law |
|---|---|---|---|
| **Formation** | Offer + acceptance + consideration + intent | Offer + acceptance + intent (no consideration) | Offer + acceptance + intent (no consideration) |
| **Good faith** | No general duty (Walford v Miles) | Pervasive: Art. 6:248 BW overrides and supplements | Art. 2 ZGB: good faith in exercise of rights |
| **Interpretation** | Objective: words of the contract (Arnold v Britton) | Subjective-objective: Haviltex (party intent) | Vertrauensprinzip (trust principle): objective |
| **Penalties** | Unenforceable if disproportionate (Cavendish) | Enforceable but subject to judicial reduction (Art. 6:94 BW) | Enforceable but subject to judicial reduction (Art. 163 OR) |
| **Limitation** | 6 years from breach (contract); 12 years (deed) | 5 years from knowledge; 20-year absolute (Art. 3:307/310 BW) | 10 years from claim becoming due (Art. 127 OR) |
| **Remedies** | Damages primary; injunctions discretionary | Nakoming (specific performance) primary; damages secondary | Specific performance primary under Art. 97 OR |
| **Entire agreement** | Effective to exclude parol evidence | May be overridden by redelijkheid en billijkheid | Generally effective but subject to good faith limits |
| **Standard terms** | UCTA s.3 reasonableness test | Art. 6:231-247 BW (grey/black lists for B2C) | Art. 8 UWG: unfair terms in B2C |
