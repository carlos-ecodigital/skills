# DE NDA Policy Positions

This document defines Digital Energy Group AG's company-specific policy positions on NDA terms. It is the reference standard that the NDA review workflow scores counterparty NDAs against. All positions reflect DE's commercial reality: a Swiss AG (CHE-408.639.320, Zug) operating across UK, NL, NO, US, and CH jurisdictions, in early-growth stage, with speed and relationship quality as competitive advantages.

**This is not legal advice.** It is a codified set of commercial preferences and risk tolerances. For high-stakes or novel situations, engage qualified external counsel.

---

## 1. Policy Principles

1. **NDAs unlock value.** DE signs NDAs to enable commercial conversations, not to create legal barriers. Every NDA is a tool to get to the next step of a deal.

2. **Speed is a competitive advantage.** Slow or adversarial NDA processes signal dysfunction. The counterparty should experience DE as professional, fast, and reasonable. A 48-hour NDA turnaround is the target.

3. **Protect what matters.** DE's crown jewels are: grower relationships, site-specific data (locations, grid connections, permits), and the commercial model economics (heat-for-land, colocation pricing). The NDA policy prioritises protecting these over theoretical legal perfection.

4. **Accept market standard.** Imperfect but market-standard terms are acceptable. Save negotiation capital for commercial agreements (SPAs, service agreements, joint ventures) where the stakes justify the effort.

5. **Consistency builds reputation.** Apply the same positions across all counterparties. When DE does push back, the counterparty should know it is principled, not arbitrary.

6. **Learn and adapt.** This policy is a starting point. As DE signs more NDAs, positions should evolve based on actual experience, counterparty feedback, and lessons learned. The review log is the feedback mechanism.

---

## 2. Negotiation Judgement Framework

### 2.1 The Defend / Negotiate / Accept Classification

Every Amber or Red clause in an NDA review is classified into one of three priorities:

| Priority | Criteria | Behaviour |
|---|---|---|
| **DEFEND** | Real, material, realistic risk to DE. One-sided exposure. Could actually cause harm. | Always redline. Walk away if counterparty will not move. |
| **NEGOTIATE** | Imperfect but manageable risk. Worth one collaborative ask. | Propose change once. Accept if counterparty pushes back. Do not escalate. |
| **ACCEPT** | Market-standard term or theoretical risk that is unlikely to materialise. | Sign as-is. Do not raise it. Raising it wastes negotiation capital. |

**Decision tree for classification:**

```
1. Could this clause actually hurt DE in a realistic scenario?
   NO → ACCEPT

2. If yes: is the potential damage material (financial > EUR 50k,
   operational disruption, reputational, or loss of key relationship)?
   NO → ACCEPT or NEGOTIATE (one round maximum)

3. If material: is the exposure mutual or one-sided?
   MUTUAL (both parties bear equal risk) → NEGOTIATE at most
   ONE-WAY against DE → DEFEND

4. Does this clause compound with other clauses to create a risk
   bigger than any single clause alone?
   YES → UPGRADE priority by one level (ACCEPT → NEGOTIATE, NEGOTIATE → DEFEND)

5. Would a seasoned in-house counsel at a comparable infrastructure
   company bother redlining this in a mutual NDA?
   NO → DE should not either
```

### 2.2 Three-Layer Analysis

The Defend/Negotiate/Accept classification is the starting point. To achieve rigorous, trustworthy judgement, every NDA review runs three analytical layers:

**Layer 1: Clause-Interaction Analysis**

After scoring individual clauses, a second pass examines how clauses interact as a system. Compound risks that individual scoring misses:

| Interaction Pattern | Risk | Effect |
|---|---|---|
| Broad CI definition + reverse burden of proof + full-cost indemnity | Low-bar trigger with high-cost consequences | UPGRADE the weakest clause in the chain |
| Mutual obligations + one-sided remedies | Hidden asymmetry | UPGRADE remedies/indemnity clause |
| No term limit + no compliance retention exception | Practical trap: perpetual obligation with no way to comply with destruction | UPGRADE return/destruction clause |
| Broad "Representatives" definition + strict liability for Representatives + full-cost indemnity | Cascading exposure through people DE does not fully control | UPGRADE Representatives liability clause |
| "Before and after the date" CI scope + vague or no defined Purpose | Everything ever discussed is captured forever with no use restriction | UPGRADE Purpose definition to DEFEND |
| NC clause + broad CI definition + no carve-out for public information | NC becomes effectively permanent because CI never expires | UPGRADE NC duration or CI scope |

Output: Compound Risk Flags section identifying any clause interactions that elevate risk beyond individual scores.

**Layer 2: Devil's Advocate**

After the initial recommendation, a second analytical pass explicitly argues the case for NOT following the recommendation:

- What is the worst-case scenario for DE under these specific terms?
- What was the counterparty's lawyer optimising for when they drafted this clause?
- In what scenario would Carlos regret having signed this?
- What would a litigation lawyer focus on if this NDA were ever in dispute?

Rules:
- The devil's advocate MUST identify at least one genuine concern, even for a clean NDA
- If no genuine concern can be found, the NDA is genuinely clean (note this explicitly)
- The final recommendation either holds (with devil's advocate concerns acknowledged and dismissed with reasoning) or gets adjusted

Output: Devil's Advocate section with strongest case against the recommendation, plus response to each concern.

**Layer 3: Precedent Matching**

Each review is compared against the review log of previously reviewed NDAs:

- "This NDA is structurally similar to the [Counterparty X] NDA reviewed on [date]. Key differences: [list]."
- "The last time DE encountered a reverse burden of proof clause, it was removed. Consistent recommendation: request removal."
- "DE has accepted 'indemnity basis' from 3 previous counterparties despite this policy saying NEGOTIATE. Consider: update policy to ACCEPT, or maintain consistency by continuing to NEGOTIATE?"
- "This is DE's first NDA from a [jurisdiction] counterparty. No precedent available."

When the review log is empty (first NDAs), Layer 3 notes: "No precedent data available. This review will establish the baseline." As the log grows, this layer becomes the most valuable: it codifies Carlos's actual judgement over time.

Output: Precedent Context section with relevant comparisons and consistency checks.

### 2.3 The Golden Rule

"Redline only what matters. Accept everything else. The counterparty should feel that DE is professional, reasonable, and fast — and that when DE does push back, it is worth paying attention to."

**Corollary:** If the redline email has more than 3-4 points, reconsider. Either the NDA is genuinely problematic (escalate), or DE is over-lawyering (accept more).

### 2.4 Resolving Precedent Conflicts

When precedent matching (Layer 3) shows DE has taken different positions on the same clause type across different NDAs, resolve as follows:

1. **Check context first.** Did the different positions reflect different deal contexts? Example: DE accepted "indemnity basis" from a large neocloud buyer (no leverage) but negotiated it with a vendor (DE had leverage). If yes → both positions are consistent with policy. Apply the context-appropriate position for the current NDA.

2. **Check timing.** Did DE's position evolve? Example: DE accepted cl.7 reverse burden in early NDAs before this policy was established, but removed it in later NDAs. If yes → the most recent position reflects current policy. Apply it.

3. **Check outcome.** Did accepting the clause cause an actual problem? If yes → strengthen the policy position. If no → the acceptance was likely pragmatic and correct.

4. **If genuinely conflicting with no clear resolution:** Flag for Carlos: "DE has taken inconsistent positions on [clause type]. Accepted in [NDA A, context], removed in [NDA B, context]. Options: (a) update policy to [position], (b) maintain current policy and apply [position] here, (c) define context-specific rules for when each position applies."

---

## 3. Governing Law Policy

DE's position depends on counterparty leverage and the commercial importance of the relationship.

### 3.1 Governing Law Preference Matrix

| Counterparty Jurisdiction | DE's Preferred Law | Acceptable | Resist |
|---|---|---|---|
| UK / England | English law | — | — |
| Netherlands | Dutch law | English law | — |
| Norway | Norwegian law | English law | — |
| Switzerland | Swiss law | English law | — |
| US (New York, Delaware) | English law | NY law | — |
| US (other states) | English law | — | State law without specific analysis |
| Other known jurisdictions | English law or Swiss law | Counterparty local law if well-established legal system | — |
| Unfamiliar or sanctioned jurisdictions | — | — | RED: do not accept without external counsel review |

### 3.2 Leverage-Based Application

| Leverage Position | Application |
|---|---|
| Big counterparty (neocloud, institutional investor, major grower) | Accept their governing law. Do not waste negotiation capital. |
| Roughly equal | Propose English law or Swiss law. Accept counterparty's law if they push. |
| DE has leverage | Propose Swiss law or English law. |

### 3.3 Rationale

For NDAs specifically, governing law is a low-stakes concession. NDAs are rarely litigated. English law is the global commercial default: well-understood, predictable, strong injunctive relief framework. Accept it freely. Swiss law is fine but counterparties often resist it as unfamiliar. Do not waste negotiation capital on governing law for NDAs.

### 3.4 Jurisdiction (Courts vs Arbitration)

- **Prefer non-exclusive jurisdiction** (allows DE to enforce in Switzerland if needed)
- **Accept exclusive foreign jurisdiction** for NDAs (low enforcement probability makes this theoretical)
- **Arbitration for NDAs:** generally overkill and expensive. Courts are fine.
- **For high-value relationships:** accept exclusive foreign jurisdiction without question — the NDA is a stepping stone, not the deal itself

---

## 4. Confidential Information Definition Policy

| Scenario | Position | Priority |
|---|---|---|
| Broad definition in a mutual NDA | ACCEPT — broad protects DE equally | GREEN |
| Broad definition in a one-way NDA where DE is Recipient | NEGOTIATE scope — ensure it is reasonable and bounded | AMBER |
| "Before or after the date" temporal scope | ACCEPT — standard UK practice, covers pre-NDA discussions | GREEN |
| "Including but not limited to" catch-all | ACCEPT — standard drafting practice | GREEN |
| "Ideas" or "concepts" without qualification | NEGOTIATE — could restrict independent thinking | AMBER |
| No defined Purpose or Purpose is vague | DEFEND — meaningless use restriction without defined Purpose | RED |
| Derived information included (findings, analyses) | ACCEPT — standard and appropriate | GREEN |
| Compilation of public information treated as CI | ACCEPT — standard protective provision | GREEN |

---

## 5. Non-Circumvention Policy

NC creates real, enforceable obligations. Do not accept as boilerplate. Apply only when commercially justified.

### 5.1 When DE Needs NC Protection

| Scenario | NC Needed? | Scope if Yes |
|---|---|---|
| Neocloud buyer + DE sharing grower/site info | **YES** | Protected Contacts = named growers and specific sites. Duration: 2-3 years. |
| Neocloud buyer + general commercial discussion | NO | Standard NDA sufficient. |
| Investor + financial information | NO | Standard NDA sufficient. |
| Grower partner + general | NO | Standard NDA sufficient. |
| Vendor + technical information | NO | Standard NDA sufficient. |
| Broker/intermediary introducing DE to anyone | **YES** | Protected = specific introductions made. Duration: 2-3 years. |
| Advisor/consultant with access to site pipeline | **MAYBE** | NC on specific sites if advisor sees full pipeline. Otherwise no. |

### 5.2 When Counterparty NDA Contains NC

- If deal context warrants NC: ACCEPT, but NEGOTIATE scope limits and duration cap
- If deal context does NOT warrant NC: NEGOTIATE removal or narrowing. NC creates real obligations; do not accept as boilerplate
- NC without defined Protected Contacts: NEGOTIATE — must be specific
- NC without duration cap: NEGOTIATE — must have fixed term (max 3 years for NDA-level NC)
- NC with liquidated damages in NDA context: DEFEND (RED) — disproportionate unless genuinely agreed

### 5.3 When Counterparty NDA Omits NC but DE Needs It

Flag as "NC ADDITION REQUIRED." Two options:
1. Propose NC addendum to the counterparty's NDA
2. Withhold site-specific and grower-identifying information until a more protective agreement (NCNDA or commercial agreement with NC) is in place

---

## 6. Indemnity Policy

| Scenario | Position | Priority |
|---|---|---|
| Mutual indemnity in a mutual NDA | ACCEPT | GREEN |
| "Indemnity basis" costs (full actual costs, no judicial assessment) | **ALWAYS NEGOTIATE** to "reasonable and documented costs" or "standard basis" | AMBER |
| One-way indemnity (DE indemnifies counterparty but not vice versa) | DEFEND | RED |
| No indemnity clause at all | ACCEPT — remedies + equitable relief is sufficient for NDAs | GREEN |
| Indemnity covering Representatives' actions | ACCEPT — DE is already responsible for its Representatives | GREEN |
| Indemnity with no cap | NEGOTIATE cap for NDAs (unusual to have uncapped indemnity in NDA) | AMBER |

**Rationale for always negotiating "indemnity basis":** This is a low-effort, high-signal ask. It demonstrates DE reads the document carefully. "Indemnity basis" means the breaching party pays full actual legal costs without any court assessment of reasonableness. For a startup, this exposure is disproportionate. "Reasonable and documented costs" provides equivalent protection while capping unreasonable spending.

---

## 7. Return and Destruction Policy

| Scenario | Position | Priority |
|---|---|---|
| Compliance/regulatory retention exception present | ACCEPT | GREEN |
| No compliance retention exception | NEGOTIATE — add carve-out | AMBER |
| "No copies in any form including electronic" without carve-out | NEGOTIATE — impractical for modern IT (backups, compliance archives) | AMBER |
| Destruction certificate requirement | ACCEPT — standard; DE should be prepared to provide these too | GREEN |
| Return/destruction within 30 days | ACCEPT — standard | GREEN |
| Return/destruction within less than 14 days | NEGOTIATE — impractical for thorough compliance | AMBER |
| Retention permitted for legal/regulatory obligations (with continued confidentiality) | ACCEPT — well-drafted and protective | GREEN |

---

## 8. Unusual Clauses — Position Guide

These clauses are not standard in all NDAs. When encountered, apply these positions:

| Clause Type | Position | Priority | Notes |
|---|---|---|---|
| **TPA 1999 third-party rights** (Contracts (Rights of Third Parties) Act 1999) | ACCEPT if mitigated by "parties may vary without third-party consent" clause. NEGOTIATE exclusion if no mitigant. | ACCEPT or NEGOTIATE | Expands enforcement universe to Affiliates. Mitigant removes the main risk. |
| **Reverse burden of proof** ("establishing purpose of use") | DEFEND — request removal | AMBER→RED | Non-standard. Creates subjective trigger ("reasonable opinion") for reverse burden. Unnecessary in a mutual NDA with standard confidentiality obligations. |
| **Standstill** (restriction on acquiring counterparty shares/assets) | DEFEND (RED) unless M&A context | RED | Prevents DE from acquiring counterparty shares — irrelevant for most DE relationships. Only appropriate in genuine M&A exploratory NDAs. |
| **Non-solicitation of employees** | NEGOTIATE if mutual + reasonable term (12 months) + general recruitment carve-out. DEFEND (RED) if one-way. | NEGOTIATE or RED | Accept mutual with carve-out for general advertisements and headhunters not specifically targeting. |
| **Liquidated damages** | DEFEND (RED) in NDA context unless for NC breach | RED | Disproportionate for a confidentiality agreement. |
| **Audit rights** | DEFEND (RED) in NDA context | RED | Disproportionate. Counterparty should not have the right to audit DE's compliance with an NDA. |
| **Exclusivity** (hidden in NDA) | DEFEND (RED) — Critical Red flag | RED | An NDA should never create exclusivity obligations. If found, this is a deal-structure issue masquerading as confidentiality. |
| **Non-compete** (hidden in NDA) | DEFEND (RED) — Critical Red flag | RED | Must never accept competitive restrictions in an NDA. These belong in commercial agreements with consideration. |

---

## 9. Specified Information Categories

When the counterparty NDA includes a "Specified Information" or "Particular Confidential Information" field, fill it in with categories appropriate to the deal context. Do NOT leave blank or mark "NA" — listing categories ensures the most sensitive information is explicitly covered.

### 9.1 Context-Dependent Categories

| Deal Context | Recommended Categories for DE's Specified Information |
|---|---|
| **Neocloud buyer** | Site locations, grower identities and relationships, grid connection data and capacity, commercial model economics (heat-for-land, colocation pricing), project pipeline and development status, permit and regulatory information |
| **Investor** | Financial projections and models, capitalisation table, site-specific economics, pipeline data and deal status, partnership terms, fundraising strategy and terms |
| **Grower partner** | Technology specifications, financial terms and revenue projections, neocloud buyer identities and requirements, site development plans |
| **Vendor** | Technical specifications and architecture, pricing and commercial terms, integration requirements, roadmap and development plans |
| **Advisor** | Pipeline overview and deal status, financial information and projections, strategic plans, relationship context |

### 9.2 Categories DE Should Always Include

Regardless of deal context, consider including: "business plans, financial information, proprietary technology and methods, customer and partner identities and relationships, and strategic plans."

### 9.3 Counterparty's Specified Information

If the counterparty's Specified Information field is blank, do not flag this — it is their commercial decision. Focus on ensuring DE's own sensitive information is covered.

---

## 10. Counterparty Risk Categorization

The NDA review workflow starts by building a counterparty profile. That profile is auto-categorized using the rules below, and the categorization drives every downstream decision in the workflow.

### 10.1 Stakes Classification

| Counterparty Type | Stakes | Reasoning |
|---|---|---|
| Neocloud buyer | High | Core revenue source. Commercial relationship directly impacts pipeline. |
| Investor (VC, PE, family office, strategic) | High | Fundraise-critical. Relationship and terms set precedents. |
| Grower partner | High | Supply-side partner. Site access and long-term relationship at stake. |
| M&A context (any party) | High | Transformative transactions with significant legal exposure. |
| Broker / intermediary with deal access | High | Introduction-dependent. NC protection critical. |
| Vendor / service provider | Low | Replaceable. Standardised relationship. |
| Advisor / consultant (non-pipeline) | Low | Limited exposure. Advisory relationship. |
| General commercial exploration | Low | Early-stage, no committed relationship. |
| Other / unrecognized | Low (default) | Counterparty doesn't fit standard categories. Default to Low-stakes and Roughly equal leverage. Flag for user confirmation: "Counterparty type is [description]. Defaulting to Low-stakes / Roughly equal. Adjust?" |

### 10.2 Leverage Assessment

| Indicator | Position | Effect on Workflow |
|---|---|---|
| Counterparty is significantly larger, is the buyer/investor, or DE needs them more than they need DE | **They have leverage** | NEGOTIATE items on market-standard clauses → downgrade to ACCEPT. DEFEND items unchanged. Max 2 redline points. Frame asks as "minor." |
| Similar scale, mutual interest, neither party dependent | **Roughly equal** | Apply standard DEFEND/NEGOTIATE/ACCEPT per policy. Max 3-4 redline points. |
| DE controls access (to growers, sites, pipeline) and counterparty needs DE's assets | **DE has leverage** | Keep NEGOTIATE items. Can add 1 "nice-to-have" beyond strict policy. Frame asks as "our standard position." |

**Leverage heuristic when data is ambiguous:**
- If counterparty headcount > 10× DE's, or counterparty is listed/PE-backed with >€50M revenue → lean toward "They have leverage"
- If DE is the party with the asset (site, pipeline, grower relationship) that the counterparty needs access to → lean toward "DE has leverage"
- If the counterparty is a potential customer or investor for DE → lean toward "They have leverage"
- If the counterparty is seeking DE's business (vendor pitching, advisor seeking engagement) → lean toward "DE has leverage"
- When genuinely unclear → default to "Roughly equal"

### 10.3 NC Trigger Rules

| Context | NC Required? | Trigger |
|---|---|---|
| Neocloud buyer + grower/site info will be shared | Yes | Grower identities, site locations, or introduction-sensitive data |
| Broker / intermediary | Yes | Specific introductions or deal access |
| Advisor with full pipeline visibility | Conditional | Only if specific sites or contacts will be disclosed |
| Investor | No | Standard NDA sufficient for financial information |
| Grower partner | No | Standard NDA sufficient |
| Vendor | No | Standard NDA sufficient |
| General commercial | No | No sensitive introductions |

**If NC determination cannot be made at intake** (e.g., it is unclear what information will be shared): set NC to "Conditional" and flag: "NC requirement depends on what information DE shares under this NDA. Resolve before sharing grower identities, site locations, or introduction-sensitive data. If in doubt, add NC before disclosing."

### 10.4 Governing Law Stance (by leverage)

| Leverage Position | Stance |
|---|---|
| They have leverage | Accept their governing law (per Section 3.2) |
| Roughly equal | Propose English or Swiss law; accept theirs if they push |
| DE has leverage | Propose Swiss or English law |

### 10.5 Review Depth (by stakes)

| Stakes | Review Depth |
|---|---|
| High-stakes | Full analysis: complete RAG table, compound risks, devil's advocate, precedent, recommendation |
| Low-stakes + STANDARD risk | Summary: 3-line summary + confirm |
| Low-stakes + ELEVATED risk | Summary with key items: 5-8 lines + confirm (full on request) |
| Any stakes + HIGH/UNACCEPTABLE risk | Full analysis + redlines/escalation |

### 10.6 Cover Email Tone (by counterparty type)

| Counterparty Type | Tone | Key Characteristics |
|---|---|---|
| Neocloud buyer | Professional, efficient, tech-fluent | Short. Speed signals competence. "Two quick comments." |
| Investor (VC/PE) | Formal, legally sophisticated | Precise. Cite clause numbers. Their lawyers will review. |
| Grower partner | Warm, plain language, patient | Explain why each ask matters in simple terms. |
| Vendor | Straightforward, businesslike | "Let's get this done." Minimal preamble. |
| Advisor / consultant | Collegial, collaborative | "Let's make sure we're both covered." |
| Broker / intermediary | Careful, NC-focused | Direct about NC scope. They understand why DE is asking. |

---

## 11. Policy Review and Updates

This policy should be reviewed and updated:
- After every 10 NDA reviews (pattern check: are the positions working?)
- When a counterparty pushes back on a position DE has been defending (is the position justified?)
- When Carlos overrides the workflow's recommendation (why? should the policy change?)
- When an NDA term causes an actual problem in practice (the most valuable learning)

The review log's "Notes" field captures lessons learned and policy update suggestions.
