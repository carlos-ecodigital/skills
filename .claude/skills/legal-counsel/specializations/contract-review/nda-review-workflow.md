# NDA Review Workflow

8-phase workflow for reviewing counterparty-drafted NDAs. Counterparty-first: identify, validate, enrich, and categorize the counterparty BEFORE reading the document. The counterparty profile drives every downstream decision.

**Target:** AI does the full analysis. Carlos sees a summary + recommendation + decision point. 80%+ of NDAs should be signable without escalation. 48-hour turnaround from receipt to signature.

---

## How to Run This Workflow

This section governs how the AI runs the NDA review as a conversation. Read this FIRST — it controls the entire arc from "review this NDA" to "signed."

### Document Acquisition

When the user triggers an NDA review, obtain the document:

| User provides... | Action |
|---|---|
| File path (e.g., `/Users/crmg/Documents/stelia-nda.pdf`) | Read file directly. For PDFs: use `pages` parameter if >10 pages. |
| Pasted text | Use directly as the NDA content. |
| URL | WebFetch the URL. If it fails (login wall, JavaScript), ask: "I couldn't fetch that URL. Can you save it locally or paste the text?" |
| Reference only (e.g., "NDA from Stelia") | Ask: "Please share the NDA — file path, paste the text, or drop it into the chat." |
| Nothing (just "review this NDA") | Ask: "Please share the NDA — file path, paste the text, or drop it into the chat." |

### Session Resumption Check

Before starting Phase 0, search for prior reviews:
1. Grep `/Users/crmg/Documents/DE Claude/legal/nda-reviews/` for the counterparty name (if known).
2. If a `DRAFT-*.md` file exists → this is a **resumed review**, not a new one. Load the draft and continue from where it left off.
3. If a final review memo exists with Decision = "REDLINED (pending)" or "Pending" → this is a **Phase 6 re-negotiation**. Load the prior memo and enter Phase 6 (Step 6.0).
4. If a final review memo exists with Decision = "SIGNED" → this is a **new NDA from a known counterparty**. Note the prior review for precedent matching (Pass 4).

### File Loading Strategy

Do NOT load all reference files at once. Load on-demand per phase:

| Phase | Files to load |
|---|---|
| Activation | This file only (`nda-review-workflow.md`) |
| Phase 0 | No additional files needed |
| Phase 1 | `nda-policy-positions.md` Section 10 only (read with offset/limit targeting Section 10) |
| Phase 1 (after governing law identified) | Jurisdiction files: `contract-law.md`, `entity-types.md`, `dispute-resolution.md`, `terminology.md` for the identified jurisdiction |
| Phase 3 | `nda-review-checklist.md` + full `nda-policy-positions.md` + `authority-matrix.md` |
| Phase 5 | `redline-playbook.md` |
| Phase 7 | `review-log-template.md` |

**Context window management:** After using enrichment data (HubSpot results, registry data, web search results), summarize findings into the counterparty profile and do not retain raw API responses. Use Grep (not Read) for precedent search across prior review memos.

### Interaction Model: When to Pause, When to Continue

The workflow has exactly **2-4 user interactions** depending on risk level. Everything else runs autonomously.

**Pause points (require user input):**

| Pause Point | What user sees | When it fires |
|---|---|---|
| **Intake confirmation** (Phase 1, Step 1.3) | Counterparty profile + categorization + intake summary | Always |
| **Recommendation** (Phase 4) | Risk-appropriate analysis + decision point | Always |
| **Redline approval** (Phase 5, Step 5.4) | Redlines + cover email | Only if redlines generated |
| **Signature confirmation** (Phase 7, Step 7.5) | Pre-signature checklist + CRM update approval | Always |

**Autonomous phases (run silently — do NOT present intermediate output):**

| Phase | Behavior |
|---|---|
| Phase 0 (Document Validation) | Run silently. Only pause if a blocking issue is found (wrong document type, missing schedules, non-English). |
| Phase 1 Steps 1.1-1.2 (Enrichment) | After getting counterparty name, run all enrichment (CRM, registry, web, prior NDAs) autonomously. |
| Phase 2 (Structural Scan) | Internal only. Include in review memo but do not present to user unless structural issues found. |
| Phase 3 (Three-Layer Analysis) | Run all 4 passes autonomously. Do not present intermediate results. |
| Phase 7 Steps 7.1-7.4 (Checks) | Run silently. Only surface if a check fails. |

### Minimum Interaction Count by Risk Level

| Risk Level | Minimum Turns | Flow |
|---|---|---|
| STANDARD | 3 | Provide NDA + counterparty → Confirm profile → Confirm sign |
| ELEVATED + low-stakes | 3 | Provide NDA + counterparty → Confirm profile → Confirm sign |
| ELEVATED + high-stakes | 4 | Provide NDA + counterparty → Confirm profile → Review full analysis → Confirm sign or approve redlines |
| HIGH | 4 | Provide NDA + counterparty → Confirm profile → Review analysis + redlines → Approve redline email |
| UNACCEPTABLE | 4+ | Provide NDA + counterparty → Confirm profile → Review analysis → Choose path (reject / external counsel / template swap) |

### Quick Assessment Mode

If the user says "just tell me if I can sign it", "quick check", or similar:
- Run the full analysis silently (all phases)
- Present ONLY a 1-3 sentence recommendation
- Save the full analysis in the review memo regardless
- If risk is HIGH or UNACCEPTABLE, override quick mode and present the full analysis — these cannot be rubber-stamped

### Phase 4→5 Auto-Flow Rules

After presenting the Phase 4 recommendation, the flow depends on risk level:

| Risk Level | Auto-flow behavior |
|---|---|
| STANDARD | Present summary → wait for "confirm" → skip Phase 5 → Phase 7 |
| ELEVATED + low-stakes | Present summary → wait for user → Phase 7 (or Phase 5 if user asks for redlines) |
| ELEVATED + high-stakes | Present full analysis WITH pre-generated redlines for any NEGOTIATE/DEFEND items. Wait for approval. |
| HIGH | Present analysis + redlines + cover email in ONE output. Wait for approval of the full package. |
| UNACCEPTABLE | Present analysis + "DO NOT SIGN" + paths. Wait for user decision before generating anything further. |

### Phase 4 User Decision Paths

When the user responds to the Phase 4 recommendation, handle these paths:

| User says... | Action |
|---|---|
| "Confirm" / "Sign" / "Approved" | Skip Phase 5 → Phase 7 |
| "Redline" / "Push back" | Phase 5 (generate redlines if not already generated) |
| "Show full analysis" / "Details" | Re-present with full RAG table, then return to decision point |
| "Explain [item]" | Drill into the specific item, then return to decision point |
| "Sign anyway" / "Override" | Log the override in the review memo → Phase 7 |
| "Escalate to [person]" | Generate escalation brief → present for approval |
| "Pause" / "Save for later" | Save DRAFT memo → exit workflow |
| "Just handle it" | Auto-proceed per risk level auto-flow rules |

---

## Phase 0: Document Validation

**Actor:** AI-driven. Quick sanity checks before the full workflow begins.

### Step 0.1: Document Type Check
Read the document. Classify silently as: Mutual NDA / One-way NDA (DE as Recipient) / One-way NDA (DE as Discloser). Record the classification for the intake summary (Phase 1, Step 1.5). Do NOT ask the user to confirm — the document type will be stated in the intake summary.

If the document is NOT an NDA (e.g., service agreement, LOI, SPA):
> "This document appears to be a [document type], not an NDA. Routing to general Review Workflow."

Exit this workflow and route to the general review workflow in SKILL.md.

### Step 0.2: Language Check
Confirm document language = English.

If non-English:
> "This document is in [language]. The NDA review workflow is designed for English-language agreements. Options:
> (a) Proceed with caveats — analysis will be based on English legal concepts, which may not apply
> (b) Obtain an English translation first and re-submit"

### Step 0.3: Completeness Check
Verify all referenced schedules, exhibits, and appendices are present.

If any are missing:
> "**Blocking:** Schedule [X] is referenced in clause [Y] but is not attached. The review cannot be completed without it. Please provide the missing document."

If all present: proceed to Phase 1.

---

## Phase 1: Counterparty-First Intake

**Actor:** AI performs counterparty identification, validation, and enrichment. Asks user ONE question, then auto-pulls everything else.

### Step 1.1: Ask for Counterparty
Single question:
> "Who is the counterparty? (Company name, or the person's name and company)"

**Fallback:** If the user doesn't know (e.g., "not sure", "it's in the NDA"), extract the counterparty from the NDA's party clause and confirm: "The NDA names [Entity Name] as the counterparty. Correct?" If the user wants to skip intake entirely, run auto-extraction only — extract counterparty from NDA, run enrichment, present profile for confirmation as usual.

### Step 1.2: Identify and Validate
AI performs the following automatically:

**1. Extract from NDA:**
- Party name, registration number, jurisdiction, registered office
- Signatory name and title
- Governing law and jurisdiction clause
- Direction (mutual or one-way)
- Structure (number of clauses, schedules, unfilled fields)
- Template origin (law firm branded, industry standard, bespoke)
- Execution method (DocuSign, wet ink, other)

**2. HubSpot CRM lookup:**
- Search for counterparty: company name match, contact match, domain match
- If found: pull company record, all contacts, associated deals, deal stage, notes, recent activities
- If not found: note "New counterparty — not in CRM"

**3. Registry validation (by jurisdiction):**
- UK: Companies House — company number, status (active/dissolved), directors, registered office, filing status
- NL: KvK — KvK number, legal form, status, bestuurders
- CH: ZEFIX/UID — UID, legal form, domicile, status
- US: State Secretary of State — if identifiable state
- Other: flag "[VERIFY: Entity status not independently verified — manual check recommended]"
- Verify signatory is listed as director/officer where registry data is available

**4. Web enrichment:**
- Company website → what they do, size indicators (headcount, funding, revenue if available)
- LinkedIn company page → scale, key people, industry
- News → recent funding rounds, M&A activity, partnerships, controversies
- Red flags → litigation, regulatory action, financial distress, sanctions associations

**5. Prior NDA lookup:**
- Search review log at `/Users/crmg/Documents/DE Claude/legal/nda-reviews/` for any prior reviews involving this counterparty
- If found: retrieve prior review memo(s), note outcomes, extract any policy lessons

### Step 1.3: Build Counterparty Profile
Present enriched profile for user confirmation:

```
COUNTERPARTY PROFILE: [Name]

IDENTITY
Entity:          [Full legal name] ([jurisdiction], [reg number])
Status:          [Active / Dissolved / Not verified] — Source: [Companies House / KvK / ZEFIX]
Registered:      [Address]
Directors:       [List from registry, if available]
Signatory:       [Name from NDA] — [Director listed? Y/N / Not verifiable]

BUSINESS
Industry:        [Industry / sector]
Size:            [Headcount / funding stage / revenue indicator]
Website:         [URL]
Description:     [1-2 sentences: what they do]

RELATIONSHIP WITH DE
CRM Status:      [Found in HubSpot — deal link / Not found]
Prior Dealings:  [List of deals, notes, contacts]
Prior NDAs:      [List with dates and outcomes / "None — first-time counterparty"]
Key DE Contacts: [Who at DE has dealt with this counterparty]
Active Deal:     [Deal name, stage, if any]

RISK INDICATORS
Jurisdiction:    [Familiar / Unfamiliar / Sanctioned]
Size Asymmetry:  [They're larger / Roughly equal / DE is larger]
Sector:          [Neocloud / Investor / Grower / Vendor / Advisor / Broker / Other]
Red Flags:       [List — or "None identified"]
```

Ask user to confirm and fill gaps:
> "Does this look right? Anything to add about your relationship, the deal context, or urgency?"

This single confirmation question captures any context the auto-pull missed: relationship nuances, urgency, pre-disclosed information, or corrections.

### Step 1.4: Categorize — Counterparty Risk Profile
Based on the enriched profile, auto-categorize using DE company policy (nda-policy-positions.md Section 10):

```
COUNTERPARTY RISK CATEGORIZATION

Category:        [Neocloud buyer / Investor / Grower / Vendor / Advisor / Broker / Other]
Stakes:          [High-stakes / Low-stakes] — Reason: [per Section 10.1]
Leverage:        [DE has leverage / Roughly equal / They have leverage] — Reason: [per Section 10.2]
NC Required:     [Yes / No / Conditional] — Trigger: [per Section 10.3]
Governing Law:   [Accept theirs / Push ours / Negotiate] — Per Section 10.4
Review Depth:    [Summary + confirm / Full analysis] — Per Section 10.5
Tone:            [Per Section 10.6]
Urgency:         [None / Deadline: date / Blocking: reason]
Pre-Disclosure:  [None / Yes — describe]
Prior NDA Round: [New / Re-negotiation round N — link to prior memo]
```

**How the categorization drives every downstream phase:**

| Categorization | Downstream Effect |
|---|---|
| **Stakes** | Phase 4: presentation depth (summary vs full analysis) |
| **Leverage** | Phase 3: priority adjustments per authority-matrix.md Section 7 (NEGOTIATE → ACCEPT when no leverage) |
| **NC Required** | Phase 3: NC check + Phase 5: NC addendum generation |
| **Governing Law** | Phase 3: Items 24-25 scoring (GREEN/AMBER depends on stance) |
| **Review Depth** | Phase 4: output template selection |
| **Tone** | Phase 5: cover email template and language selection |
| **Urgency** | Phase 4: urgent mode per authority-matrix.md Section 8 |
| **Prior NDA Round** | Phase 3: precedent auto-loaded + Phase 6: diff-based analysis |
| **Pre-Disclosure** | Phase 3: NC scope assessment (if info already shared, flag retroactive exposure) |

### Step 1.5: Intake Summary
Combine document data + counterparty profile:

```
INTAKE SUMMARY
─────────────
Counterparty:    [Name] ([Jurisdiction], [Reg No.]) — [Status]
DE Entity:       Digital Energy Group AG (CHE-408.639.320, Zug)
Direction:       [Mutual / One-way]
Governing Law:   [Law], [Jurisdiction] ([exclusive/non-exclusive])
Category:        [Type] → [Stakes] | Leverage: [position]
NC Check:        [Required / Not required / Conditional]
Gov. Law Stance: [Accept / Push / Negotiate]
Review Depth:    [Summary / Full]
Tone:            [Selected tone]
Urgency:         [None / Deadline / Blocking]
Prior Dealings:  [Summary or "First-time counterparty"]
Pre-Disclosure:  [None / Description]
Round:           [New / Round N — prior memo: filename]
─────────────
Proceed to analysis? [Confirm / Adjust]
```

### Step 1.6: Template Battle Check
If DE has already sent its own NDA template to this counterparty (known from CRM or user confirmation):

> "DE previously sent its own NDA template to [counterparty]. They've sent their own instead. Options:
> 1. **Push back once:** 'We've already sent our standard NDA — happy to discuss any comments.'
> 2. **Accept their paper:** Proceed with reviewing their NDA."

Apply leverage modifier: if they have leverage, skip push-back and accept their paper immediately.

---

## Phase 2: Structural Scan

**Actor:** AI-driven, no user input required. **This phase is internal — do NOT present output to the user.** Include results in the review memo. Only pause if a blocking structural issue is found (e.g., missing schedule that prevents analysis).

### Step 2.1: Clause Mapping
Map the counterparty's clauses against DE's 14-section NDA structure (from the NDA template):

| DE Section | Counterparty Clause | Status |
|---|---|---|
| 1. Definitions | [Clause X] | Present / Modified / Missing |
| 2. Confidentiality Obligations | [Clause Y] | Present / Modified / Missing |
| 3. Permitted Disclosures | [Clause Z] | Present / Modified / Missing |
| 4. Exclusions | ... | ... |
| 5. No Obligation to Disclose | ... | ... |
| 6. No Implied Rights | ... | ... |
| 7. Non-Circumvention | ... | ... |
| 8. Return and Destruction | ... | ... |
| 9. Announcements | ... | ... |
| 10. Standstill | ... | ... |
| 11. Non-Solicitation | ... | ... |
| 12. Term and Survival | ... | ... |
| 13. Remedies | ... | ... |
| 14. General | ... | ... |
| 15. Governing Law | ... | ... |

### Step 2.2: Flag Structural Issues
- **Missing sections:** Flag any DE-standard sections that are absent. Note whether the omission matters (e.g., missing exclusions = RED; missing standstill = expected for non-M&A).
- **Extra sections:** Flag any clauses in the counterparty NDA that do not map to DE's standard structure. These are the most important to review carefully — unusual clauses may contain hidden obligations.
- **Unfilled fields:** Flag any blank fields (Specified Information, Purpose, dates, addresses).
- **Structural anomalies:** Inconsistent definitions, undefined terms used in obligations, circular references.

### Step 2.3: Structural Summary
Brief output:

```
STRUCTURAL SCAN
Sections mapped:    [X] of 15 DE-standard sections found
Missing sections:   [List]
Extra sections:     [List — REVIEW CAREFULLY]
Unfilled fields:    [List]
Anomalies:          [List or "None identified"]
```

---

## Phase 3: Three-Layer Analysis

**Actor:** AI-driven. This is the rigorous analytical core.

### Pass 1: Clause-by-Clause RAG Assessment

Run each of the 25 items from the NDA Review Checklist. For each item:

1. **Score:** GREEN (acceptable) / AMBER (flag) / RED (unacceptable)
2. **Priority:** DEFEND / NEGOTIATE / ACCEPT (from checklist default, adjusted for context)
3. **Finding:** One-line description of what was found
4. **Action:** What DE should do (sign as-is / note / redline / escalate)

Context-triggered additional checks:
- **Neocloud buyer context:** Check for NC presence. If absent and grower/site info will be shared, flag NC ADDITION REQUIRED.
- **Investor context:** Check for standstill clause. Flag if present (appropriate only for M&A).
- **Any context:** Check for hidden IP assignment, non-compete, exclusivity (Critical Red flags per Authority Matrix).

**Extra sections from Phase 2:** After scoring the 25 standard checklist items, score each "extra section" identified in Phase 2 (Step 2.2) using the same RAG methodology. Reference nda-policy-positions.md Section 8 (Unusual Clauses) for scoring guidance. Number extra items as 26, 27, etc.

**Leverage modifier:** After initial scoring, apply the Leverage Modifier from authority-matrix.md Section 7. If counterparty has leverage, downgrade NEGOTIATE items to ACCEPT where the policy allows flexibility. If DE has leverage, consider upgrading ACCEPT items to NEGOTIATE for better terms.

Output: RAG Assessment Table

| # | Item | RAG | Priority | Finding | Action |
|---|---|---|---|---|---|
| 1 | Entity Name | G/A/R | D/N/A | ... | ... |
| 2 | Entity Status | G/A/R | D/N/A | ... | ... |
| ... | ... | ... | ... | ... | ... |
| 25 | Jurisdiction | G/A/R | D/N/A | ... | ... |
| 26+ | [Extra sections from Phase 2] | G/A/R | D/N/A | ... | ... |

Scoring summary:

| Category | Green | Amber | Red |
|---|---|---|---|
| A. Parties & Authority | | | |
| B. CI Definition | | | |
| C. Exclusions | | | |
| D. Obligations | | | |
| E. Permitted Disclosures | | | |
| F. Return & Destruction | | | |
| G. Term & Duration | | | |
| H. Remedies & Indemnity | | | |
| I. Governing Law | | | |
| **Total** | | | |

### Pass 2: Clause-Interaction Analysis

After individual scoring, a second pass examines how clauses interact as a system. Check for these compound risk patterns (from NDA Policy Positions Section 2.2):

| Pattern | Clauses Involved | Compound Risk | Upgrade Action |
|---|---|---|---|
| Broad CI + reverse burden + full-cost indemnity | Items 5, 7*, 23 | Low-bar trigger, high-cost consequences | Upgrade weakest clause |
| Mutual obligations + one-sided remedies | Multiple | Hidden asymmetry | Upgrade remedies |
| No term + no compliance retention | Items 20, 18 | Perpetual obligation, impossible compliance | Upgrade return/destruction |
| Broad Representatives + strict liability + full indemnity | Items 15, 3.4*, 23 | Cascading exposure through people DE doesn't control | Upgrade Representative liability |
| Broad CI scope + no defined Purpose | Items 5, 13 | Everything captured forever, no use restriction | Upgrade Purpose to DEFEND |
| NC + broad CI + no public information carve-out | Items NC*, 5, 9 | NC effectively permanent | Upgrade NC duration or CI scope |

*Items marked with * may not be in the standard 25-item checklist but may appear as extra sections in the counterparty NDA.

**Upgrade rules:** If a compound risk pattern is identified, upgrade the priority of the weakest clause in the chain by one level:
- ACCEPT → NEGOTIATE
- NEGOTIATE → DEFEND

Output: Compound Risk Flags section (or "No compound risk patterns identified").

### Pass 3: Devil's Advocate

After the initial recommendation, argue the case AGAINST following it. Address:

1. **Worst-case scenario:** What is the worst thing that could happen to DE under these specific terms?
2. **Counterparty intent:** What was the counterparty's lawyer optimising for when drafting the flagged clauses?
3. **Regret test:** In what specific, realistic scenario would Carlos regret having signed this?
4. **Litigation lens:** If this NDA were ever disputed, what would a litigation lawyer focus on?

Rules:
- The devil's advocate MUST identify at least one genuine concern, even for a clean NDA.
- If no genuine concern can be identified after thorough analysis, the NDA is genuinely clean (state this explicitly: "This NDA is genuinely clean. The devil's advocate could not identify a material concern beyond [theoretical risk X].").
- The final recommendation either holds (with concerns acknowledged and dismissed with reasoning) or gets adjusted.

Output: Devil's Advocate section with:
- Strongest case against the recommendation
- Specific scenarios or risks identified
- Response to each concern (why the recommendation holds, or how it's been adjusted)

### Pass 4: Precedent Matching

Compare this NDA against the review log (at `/Users/crmg/Documents/DE Claude/legal/nda-reviews/`):

- **Structural similarity:** "This NDA is structurally similar to the [Counterparty X] NDA reviewed on [date]. Key differences: [list]."
- **Clause consistency:** "The last time DE encountered [clause type], the decision was [accept/redline/remove]. Consistent recommendation: [same/different — explain why]."
- **Policy drift check:** "DE has [accepted/rejected] this clause [N] times. Consider: update policy to match practice, or reassert policy position?"
- **New territory:** "This is DE's first NDA from a [jurisdiction/counterparty type/industry]. No precedent available."

When the review log is empty or no relevant precedent exists:
> "No precedent data available. This review will establish the baseline for future comparisons."

Output: Precedent Context section with relevant comparisons and consistency checks.

---

## Phase 4: Risk Summary and Recommendation

**Actor:** AI presents analysis. User decides.

### Step 4.1: Risk Level Determination
Aggregate scores per Authority Matrix:

| Risk Level | Criteria |
|---|---|
| STANDARD | All Green, max 2 minor Amber (both ACCEPT-tagged) |
| ELEVATED | 3-5 Amber (any priority), no Red |
| HIGH | Any Red, or 6+ Amber |
| UNACCEPTABLE | Any Critical Red flag, or 3+ Red |

Apply upgrade rules from Three-Layer Analysis:
- Compound risk identified → upgrade by one level
- Devil's advocate concern not dismissible → upgrade by one level
- Precedent matching shows DE previously rejected similar terms → flag for consistency

### Step 4.2: Presentation (Context-Adaptive)

**STANDARD risk (any context):**
```
NDA REVIEW: [Counterparty]
Risk: STANDARD | Context: [type]

This NDA is clean. [Counterparty], [governing law], [mutual/one-way].
[Green count]G / [Amber count]A / [Red count]R.
Recommend signing. Confirm?

Devil's advocate: [One sentence — strongest concern + dismissal].
```

**ELEVATED risk + Low-stakes context:**
```
NDA REVIEW: [Counterparty]
Risk: ELEVATED | Context: [type]

[5-8 line summary]:
- Overall: [Green]G / [Amber]A / [Red]R
- Key Amber items:
  - [Item]: [finding] → [priority tag: ACCEPT / NEGOTIATE]
  - [Item]: [finding] → [priority tag]
- Recommendation: [Sign as-is / Light redline on items X, Y]
- Devil's advocate: [One sentence]

Confirm? Or type "show full analysis" for the complete RAG table.
```

**ELEVATED risk + High-stakes context:**
Present the full analysis:
- Complete RAG assessment table
- Compound risk flags (if any)
- Devil's advocate section (full)
- Precedent context (if available)
- Recommended action with reasoning
- Redline options if applicable

**HIGH risk (any context):**

```
NDA REVIEW: [Counterparty]
Risk: HIGH | Category: [type] | Leverage: [position]

CRITICAL ISSUES:
1. [RED] Clause [X] — [Issue]
   Risk: [What DE is exposed to]
   Action: [Redline — preferred language from playbook]

2. [RED] Clause [Y] — [Issue]
   Risk: [What DE is exposed to]
   Action: [Redline / Remove / Escalate]

ADDITIONAL FLAGS (DEFEND):
- [AMBER/DEFEND] Clause [Z] — [Issue] → Redline included below
- [AMBER/DEFEND] Clause [W] — [Issue] → Redline included below

COMPOUND RISKS:
- [Pattern name]: Clauses [X + Y] interact to create [compound risk].
  Upgrade: [which clause upgraded, from what to what]

DEVIL'S ADVOCATE:
1. [Strongest concern]: [Scenario]. Response: [Why recommendation holds / how adjusted].
2. [Second concern]: [Scenario]. Response: [Reasoning].
3. [Third concern if applicable]: [Scenario]. Response: [Reasoning].

PRECEDENT:
- [Prior review comparison, or "No precedent — this review establishes the baseline."]

RECOMMENDED ACTION: Redline [N] clauses. [For high-stakes: "Consider having external counsel review the Red flags before signing."]

REDLINES + COVER EMAIL: Generated below (proceed to Phase 5).
```

**UNACCEPTABLE risk (any context):**

```
NDA REVIEW: [Counterparty]
Risk: UNACCEPTABLE | Category: [type]

⚠ DO NOT SIGN

CRITICAL RED FLAGS:
1. [Critical flag name] — Clause [X]
   Issue: [What the clause does]
   DE Exposure: [Specific risk to DE]
   Why unacceptable: [Per authority-matrix.md Section 4 criteria]

2. [Critical flag name] — Clause [Y]
   Issue: [What the clause does]
   DE Exposure: [Specific risk to DE]
   Why unacceptable: [Criteria]

ADDITIONAL RED/DEFEND ITEMS:
[Full RAG table for all non-GREEN items]

COMPOUND RISKS:
[Full interaction analysis]

DEVIL'S ADVOCATE:
[Full section — but here argues FOR signing to stress-test the rejection]

RECOMMENDED PATH:
Option A: Reject this NDA. Propose DE's template instead.
           Pro: Clean start, DE controls terms. Con: May delay or end discussions.
Option B: Engage external counsel to review and negotiate.
           Pro: Professional handling of critical issues. Con: Cost + time.
Option C: [Context-specific alternative, e.g., "Request a simplified mutual NDA from their side"]
           Pro: [Benefit]. Con: [Trade-off].

ESCALATION BRIEF (for external counsel if Option B selected):
───────────────────────────────────────────────
Parties:        Digital Energy Group AG ↔ [Counterparty]
Document:       [Title], [Date], [Pages]
Governing Law:  [Law], [Jurisdiction]
Deal Context:   [Category, stakes, leverage position]

Key Issues Requiring Counsel Review:
1. [Critical flag]: Clause [X] — [1-sentence description of issue and DE's exposure]
2. [Critical flag]: Clause [Y] — [1-sentence description]
[Continue for all Critical/Red items]

DE's Preferred Positions:
1. [Issue]: [DE's preferred resolution — per policy]
2. [Issue]: [DE's preferred resolution]

Questions for Counsel:
1. Are DE's proposed redlines on clauses [X, Y] legally appropriate under [governing law]?
2. Are there alternative approaches to mitigate [specific risk] that we haven't considered?
3. [Any deal-specific question]

Deadline:       [If urgent — otherwise "No hard deadline, but NDA is blocking commercial discussions"]
Fee Expectation: Fixed-fee or capped engagement for NDA review (per authority-matrix.md Section 6)
───────────────────────────────────────────────
```

### Intermediate Save (after Step 4.2)

After completing the Phase 4 analysis and BEFORE presenting to the user, save a DRAFT review memo:
- Path: `/Users/crmg/Documents/DE Claude/legal/nda-reviews/DRAFT-[YYYY-MM-DD]-[counterparty-name].md`
- Use the review-log-template.md format
- Mark incomplete fields as `[PENDING]`
- Decision field: `PENDING — review in progress`
- This enables session resumption if the chat is interrupted before Phase 7

Update the DRAFT as the workflow progresses (after Phase 5, after Phase 6 rounds). At Phase 7.6 (post-signature), rename to remove the `DRAFT-` prefix.

### Step 4.3: User Decision

**Auto-flow rules** (how Phase 4 flows into Phase 5 or Phase 7):
- **STANDARD** → present summary, wait for "confirm" → skip Phase 5 → Phase 7
- **ELEVATED + low-stakes** → present summary, wait for user → Phase 7 (or Phase 5 if user requests redlines)
- **ELEVATED + high-stakes** → present full analysis WITH pre-generated redlines for NEGOTIATE/DEFEND items. Wait for user approval of the full package.
- **HIGH** → present analysis + redlines + cover email in ONE output. Wait for user approval. On "Approved" → Phase 7.
- **UNACCEPTABLE** → present analysis + "DO NOT SIGN" + paths. Wait for user decision before generating anything further.

**User decision paths** (see also the Orchestrator's "Phase 4 User Decision Paths" table):
- **"Confirm" / "Sign" / "Approved"** → Phase 7 (Pre-Signature)
- **"Redline" / "Push back"** → Phase 5 (generate redlines if not already pre-generated)
- **"Show full analysis" / "Details"** → Re-present with full RAG table, then return to this decision point
- **"Explain [item]"** → Drill into the specific item with full reasoning, then return to this decision point
- **"Sign anyway" / "Override"** → Log override reason in review memo, proceed to Phase 7
- **"Escalate to [person]"** → Generate escalation brief (per UNACCEPTABLE template format), present for approval
- **"Pause" / "Save for later"** → Save DRAFT review memo (see Intermediate Save below), exit workflow
- **"Just handle it"** → Auto-proceed per the auto-flow rules above

---

## Phase 5: Redline Generation

**Actor:** AI generates redlines. User reviews and approves.

### Step 5.1: Select Redline Items
From the RAG assessment, select items to redline:
- All DEFEND items: always include
- NEGOTIATE items: include in first round
- ACCEPT items: never include

Check: total redline points <= 4. If more than 4:
- Verify all are genuinely necessary (not over-lawyering)
- If NDA is genuinely problematic with 5+ issues, note this: "This NDA has [N] material issues. Consider whether to proceed with a long redline or propose DE's template instead."

### Step 5.2: Draft Redlines
For each selected item, pull language from the Redline Playbook:
- Preferred language (first choice)
- Fallback position (if counterparty pushes back)
- Reasoning (one sentence)

**Playbook fallback:** If no playbook entry exists for the issue (e.g., an unusual clause not covered by the 10 standard playbook entries), draft custom redline language following the playbook format (Current → Proposed → Fallback → Reasoning). Flag as `[CUSTOM REDLINE — no playbook entry]` in the review memo.

Present as a redline summary:

```
PROPOSED REDLINES: [Counterparty] NDA

1. [DEFEND] Clause [X] — [Issue]
   Current: "[current language]"
   Proposed: "[preferred language from playbook]"
   Fallback: "[fallback if they push back]"
   Reasoning: [One sentence]

2. [NEGOTIATE] Clause [Y] — [Issue]
   Current: "[current language]"
   Proposed: "[preferred language]"
   Fallback: Accept as-is if they push back.
   Reasoning: [One sentence]

Items NOT raised (ACCEPT):
- [Item]: [why it's acceptable despite being Amber]
```

### Step 5.3: Draft Cover Email
Generate a cover email using the appropriate template from the Redline Playbook:
- Match formality to the relationship
- Maximum 3-4 points
- One sentence of reasoning per ask
- Close with offer to discuss by call

### Step 5.4: User Approval
Present redlines + cover email for user review:
- User can approve as-is
- User can modify individual redlines (accept, strengthen, remove)
- User can adjust cover email tone or content
- User can add items not flagged by the workflow

Once approved, user sends the redlines to the counterparty.

---

## Phase 6: Negotiation Tracking and Re-Negotiation

**Actor:** AI re-analyses when counterparty responds. User decides next steps.

### Step 6.0: Re-Negotiation Detection
If the intake (Phase 1, Step 1.4) flagged this as a **re-negotiation round** (Prior NDA Round ≠ "New"):

1. **Retrieve prior review memo** from `/Users/crmg/Documents/DE Claude/legal/nda-reviews/` for this counterparty.
2. **Diff-based analysis:** Compare the current NDA against the version reviewed in the prior round:
   - Identify changed clauses (additions, deletions, modifications)
   - Identify unchanged clauses (carry forward prior scores — do NOT re-analyse unless context has changed)
   - Flag new clauses not present in the prior version
3. **Present diff summary:**

```
RE-NEGOTIATION ANALYSIS: [Counterparty] NDA — Round [N]
Prior Review: [filename] ([date])

CHANGES FROM PRIOR VERSION:
| Clause | Prior Score | Change Made | New Score | Action |
|---|---|---|---|---|
| Cl. [X] | AMBER/NEGOTIATE | [Description of change] | GREEN | Resolved |
| Cl. [Y] | RED/DEFEND | [Description of change] | AMBER/ACCEPT | Improved — acceptable |
| Cl. [Z] | — (new) | [New clause added] | AMBER/NEGOTIATE | Review required |

UNCHANGED FROM PRIOR VERSION:
[N] clauses unchanged. Prior scores carried forward. [List any that warrant re-review due to changed context.]

NET EFFECT: Prior risk [LEVEL] → Current risk [LEVEL]
```

4. **Only re-score changed clauses** through the full Three-Layer Analysis. Unchanged clauses retain prior scores unless the counterparty context has materially changed (e.g., new leverage position, new deal context).

### Step 6.1: Counterparty Response Intake
When the counterparty responds to DE's redlines (within the same negotiation):
- Read the modified NDA or counterparty's response
- Re-run RAG assessment on modified clauses only
- Track: what DE asked → what they conceded → what's still open

### Step 6.2: Negotiation Status Table

```
NEGOTIATION STATUS: [Counterparty] NDA — Round [N]

| # | DE's Ask | CP Response | Status | Recommendation |
|---|---|---|---|---|
| 1 | Remove cl.7 | Agreed — clause removed | RESOLVED | — |
| 2 | Reasonable costs | Counter: "standard basis" | OPEN | Accept "standard basis" (equivalent) |
| 3 | NC addendum | No response | OPEN | Re-raise in next round |

Open items: [count]
Recommendation: [Accept remaining / Push again on item X / Escalate]
```

### Step 6.3: Next Steps
Based on the negotiation status:
- **All resolved:** Proceed to Phase 7 (Pre-Signature)
- **NEGOTIATE items open:** Recommend accepting (one round maximum per policy)
- **DEFEND items open:** Recommend pushing again or escalating
- **New issues introduced by counterparty's changes:** Re-run full analysis on new clauses

---

## Phase 7: Pre-Signature Verification

**Actor:** AI performs checks. User confirms and signs.

### Step 7.1: Pre-Signature Checklist
Run through all items before signing:

- [ ] **All Red items resolved.** No unresolved Red clauses remain.
- [ ] **All fields completed.** Purpose, Specified Information, dates, addresses, entity details.
- [ ] **Correct DE entity.** Digital Energy Group AG (CHE-408.639.320, Zug).
- [ ] **Correct signatory.** Carlos Reuven, Verwaltungsrat / Director.
- [ ] **Counterparty entity verified.** Name matches registry, entity is active.
- [ ] **Counterparty signatory authority.** Signatory title and authority confirmed (or flagged as unverifiable).
- [ ] **NC addressed.** If NC was required (per context), it is included or an alternative arrangement is in place.
- [ ] **Specified Information filled in.** Categories appropriate for the deal context (per NDA Policy Positions Section 9).
- [ ] **Governing law acceptable.** Per Governing Law Policy for this counterparty type.
- [ ] **Execution method clear.** Wet ink, DocuSign, or other method confirmed.

### Step 7.2: Specified Information Completion
If the NDA has a Specified Information field, populate it per deal context:

| Deal Context | Recommended Categories |
|---|---|
| Neocloud buyer | Site locations, grower identities and relationships, grid connection data and capacity, commercial model economics, project pipeline and development status, permit and regulatory information |
| Investor | Financial projections and models, capitalisation table, site-specific economics, pipeline data and deal status, partnership terms, fundraising strategy and terms |
| Grower partner | Technology specifications, financial terms and revenue projections, neocloud buyer identities and requirements, site development plans |
| Vendor | Technical specifications and architecture, pricing and commercial terms, integration requirements, roadmap and development plans |
| Advisor | Pipeline overview and deal status, financial information and projections, strategic plans, relationship context |

### Step 7.3: Save Review Memo
Save a structured review memo to disk at:
`/Users/crmg/Documents/DE Claude/legal/nda-reviews/[YYYY-MM-DD]-[counterparty-name].md`

Use the Review Log Template format. Include:
- All RAG scores and findings
- Compound risk flags
- Devil's advocate analysis
- Precedent context
- Decision taken (signed / redlined / rejected / escalated)
- Any policy update suggestions

### Step 7.3.1: Save NDA Source Text
Save the NDA text to:
`/Users/crmg/Documents/DE Claude/legal/nda-reviews/documents/[YYYY-MM-DD]-[counterparty-name]-nda-text.md`

This preserves the exact text for future diff comparison in re-negotiation rounds (Phase 6, Step 6.0).

### Step 7.4: Update CRM
Use the HubSpot CRM Update Procedure (Appendix B) to update records:
1. Search for the counterparty company in HubSpot
2. If found → update deal record (if deal exists) or add a note to the company record
3. Present proposed CRM changes in the standard confirmation table format (required by the `manage_crm_objects` tool)
4. Wait for user approval before writing to CRM
5. If no deal record exists → ask: "No deal record for [counterparty]. Create one, add note to company, or skip?"

### Step 7.5: Final Confirmation

```
PRE-SIGNATURE VERIFICATION: [Counterparty] NDA

All checks passed: [Yes / No — list blocking issues]

Review memo saved to: [file path]
NDA text saved to: [file path]
HubSpot update: [Completed / Pending approval / Skipped]

Ready to sign. Confirm?
```

### Step 7.6: Post-Signature (after user confirms execution)

Once the user confirms the NDA has been signed:

1. **Update review memo:** Change Decision to "SIGNED", add Date Signed.
2. **Rename DRAFT:** If the review memo was saved as `DRAFT-*.md`, rename to remove the `DRAFT-` prefix.
3. **Prompt signed copy storage:** "Please save the executed copy to `/Users/crmg/Documents/DE Claude/legal/signed/[YYYY-MM-DD]-[counterparty-name]-signed.[ext]`"
4. **CRM update:** Update NDA status to "Signed" + date using Appendix B procedure.
5. **Expiry tracking:** If the NDA has a fixed term, note the expiry date. If NC is included, note the NC expiry date. Add both to the review memo Notes section.
6. **Save outbound correspondence:** If redlines or cover emails were sent, save to `/Users/crmg/Documents/DE Claude/legal/nda-reviews/outbound/[YYYY-MM-DD]-[counterparty-name]-redlines.md`

---

## Workflow Summary

| Phase | Actor | Input | Output | User Decision? |
|---|---|---|---|---|
| 0. Document Validation | AI | NDA document | Type, language, completeness check | Only if issue detected |
| 1. Counterparty-First Intake | AI + User | Counterparty name | Enriched profile + categorization + intake summary | Yes (confirm profile) |
| 2. Structural Scan | AI | NDA document | Structural comparison | No |
| 3. Three-Layer Analysis | AI | NDA + Policy + Checklist + Counterparty Profile | RAG table + Compound Risks + Devil's Advocate + Precedent | No |
| 4. Risk Summary | AI → User | Analysis results | Risk-appropriate recommendation + decision point | Yes (confirm / redline / override) |
| 5. Redline Generation | AI → User | Selected items + Tone from categorization | Redlines + tone-matched cover email | Yes (approve / modify) |
| 6. Negotiation / Re-Negotiation | AI → User | Counterparty response or new NDA version | Status table / diff analysis + next steps | Yes (accept / push / escalate) |
| 7. Pre-Signature | AI → User | Final NDA | Verification checklist + review memo + CRM update | Yes (confirm signature) |

---

## Quick Reference: When to Show What

| Situation | Presentation |
|---|---|
| STANDARD risk, any context | 3-line summary + confirm |
| ELEVATED + low-stakes | 5-8 line summary + confirm (full analysis on request) |
| ELEVATED + high-stakes | Full RAG table + compound risks + devil's advocate + precedent + recommendation |
| HIGH, any context | Full analysis + generated redlines + cover email + external counsel note (if high-stakes) |
| UNACCEPTABLE, any context | Full analysis + "DO NOT SIGN" + alternative paths (A/B/C) + escalation brief |
| Re-negotiation round | Diff-based analysis: only re-score changed clauses, carry forward prior scores |
| Urgent mode | Skip "show full analysis" option → straight to recommendation + decision. Pre-generate redlines. |

---

## Appendix A: HubSpot CRM Lookup Procedure

Use this procedure in Phase 1 (Step 1.2) for counterparty enrichment.

### Step 1: Company Search

```
search_crm_objects:
  objectType: "companies"
  query: "[counterparty name]"
  properties: ["name", "domain", "industry", "numberofemployees",
               "hs_lead_status", "notes_last_updated"]
```

If no result by name and a domain is known (from NDA or web enrichment):
```
search_crm_objects:
  objectType: "companies"
  query: "[domain]"
  properties: [same as above]
```

If no match → record: "New counterparty — not in CRM."

### Step 2: Associated Deals (if company found)

```
search_crm_objects:
  objectType: "deals"
  filterGroups:
    - associatedWith:
        - objectType: "companies"
          operator: "EQUAL"
          objectIds: ["[company_id]"]
  properties: ["dealname", "dealstage", "amount", "closedate", "pipeline"]
```

### Step 3: Associated Contacts (if company found)

```
search_crm_objects:
  objectType: "contacts"
  filterGroups:
    - associatedWith:
        - objectType: "companies"
          operator: "EQUAL"
          objectIds: ["[company_id]"]
  properties: ["firstname", "lastname", "email", "jobtitle", "hs_lead_status"]
```

### Step 4: Summarize for Counterparty Profile

Extract and summarize into the Phase 1 profile format:
- CRM Status: "Found in HubSpot" + link (use URL template from search results + UTM params)
- Active Deal: deal name, stage, amount (if any)
- Key DE Contacts: contacts associated with the company
- Prior Dealings: notes summary, recent activities
- If NDA signatory matches a CRM contact, note this

---

## Appendix B: CRM Update Procedure

Use this procedure in Phase 7 (Steps 7.4 and 7.6) for post-review CRM updates.

### Pre-Update Check

1. Run `get_user_details` to confirm write access to companies, deals, and notes.
2. If write access is not AVAILABLE, inform the user and skip CRM update.

### Update Flow

**If company exists in HubSpot and deal exists:**

Prepare the update and present in confirmation format:

```
Proposed Changes:

| Object Type | ID    | Property    | Current Value | New Value              |
|-------------|-------|-------------|---------------|------------------------|
| Deal        | [id]  | nda_status  | [current]     | Signed / Pending       |
| Deal        | [id]  | nda_date    | [current]     | [YYYY-MM-DD]           |

Approve? [✅ Yes / ❌ No]
```

Wait for user approval. Then execute via `manage_crm_objects` with `confirmationStatus: "CONFIRMED"`.

**If company exists but no deal:**

Ask: "No deal record for [counterparty]. Options:
1. Create a new deal and log the NDA status
2. Add a note to the company record
3. Skip CRM update"

**If company not in CRM:**

Ask: "Should I create a company record for [counterparty] in HubSpot?"

### Standard Note Body

For notes added to company or deal records:

```
NDA Review: [Risk Level]. Decision: [SIGNED / REDLINED / REJECTED].
Counterparty: [Name] ([Jurisdiction]).
Governing Law: [Law].
Review memo: [file path].
Date: [YYYY-MM-DD].
```

---

## Appendix C: Registry Validation Protocol

Use this procedure in Phase 1 (Step 1.2) for entity verification.

### Per-Jurisdiction Lookup

**UK (Companies House):**
1. If company number is in the NDA → WebFetch `https://find-and-update.company-information.service.gov.uk/company/[COMPANY_NUMBER]`
2. If company number not in NDA → WebSearch `"[company name] site:company-information.service.gov.uk"`
3. Extract: company status, registered office, directors, PSC entries, filing status
4. Verify: signatory is listed as director or company secretary
5. Fallback: `[VERIFY: Entity status not independently verified. Check Companies House at https://find-and-update.company-information.service.gov.uk/ for [company name].]`

**NL (KvK):**
1. WebSearch `"[company name] KvK nummer"` to find KvK number
2. KvK website is JavaScript-heavy — WebFetch unlikely to work for search pages
3. If KvK number found in search results, note it
4. Fallback: `[VERIFY: Check KvK at https://www.kvk.nl/zoeken/ for [company name].]`

**CH (ZEFIX):**
1. WebFetch `https://www.zefix.ch/en/search/entity/list/firm/[company_name]` — may work for direct entity pages
2. Cross-reference UID in NDA (CHE-xxx.xxx.xxx format) against ZEFIX
3. Fallback: `[VERIFY: Check ZEFIX at https://www.zefix.ch/ for [company name].]`

**US:**
1. WebSearch `"[company name] [state] secretary of state"` — highly variable by state
2. If state of incorporation not known, check NDA for registered agent or state references
3. Fallback: `[VERIFY: Entity status not verified. US registry lookup requires knowing the state of incorporation.]`

**Other jurisdictions:**
Always flag: `[VERIFY: Entity status not independently verified — manual check recommended for [jurisdiction].]`

### Web Enrichment Boundaries

| Source | Method | Notes |
|---|---|---|
| Company website | WebFetch | Usually works. Extract: business description, size indicators, key people. |
| LinkedIn | WebSearch only | Do NOT WebFetch LinkedIn (login wall). Use search snippets for headcount, industry, key people. |
| News | WebSearch `"[company name] funding OR acquisition OR lawsuit"` | Look for recent events, red flags, funding rounds. |
| Sanctions | WebSearch `"[company name] sanctions"` | Basic web check only. Flag: "Not a formal sanctions screening." |

### Verification Confidence Levels

| Level | Meaning | When to use |
|---|---|---|
| **Verified** | Registry data confirms entity name, status, signatory authority | Registry lookup succeeded, all data matches NDA |
| **Partially verified** | Some data confirmed, gaps remain | Registry found entity but signatory not listed as director, or filing status unclear |
| **Not verified** | Registry lookup failed or jurisdiction not supported | WebFetch/WebSearch returned no results, or jurisdiction has no accessible online registry |

Record the verification confidence level in the Counterparty Profile (Step 1.3) and in the review memo (Section 1.5).
