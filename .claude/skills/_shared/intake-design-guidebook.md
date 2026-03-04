# Intake Design Guidebook

> Universal methodology for designing structured intake processes and workflows.
> Abstracted from 20+ skills across fundraising, legal, marketing, and operations.
> Stress-tested against 10 DE-relevant use cases spanning strategic decisions, multi-party negotiations, compliance filings, recurring reports, vendor evaluations, and time-constrained research.

## How to Use This Guidebook

- **First read**: Follow Sections 1-8 sequentially. They build on each other.
- **Reference**: Jump to the section you need. Templates are in Section 8. Anti-patterns in Section 9.
- **New intake**: Follow the 8-Step Process (Section 2). Use the templates (Section 8). Check anti-patterns (Section 9).
- **Existing intake audit**: Run the validation framework (Section 6) against your current intake. Check anti-patterns (Section 9).
- **Specialized intake types**: See Sections 12-16 for research-augmented, multi-party, multi-instance, progressive/recurring, and compliance-driven intakes.

**Example implementations in this ecosystem:**
- Heavy: `seed-fundraising/references/intake-guide.md` (~75 questions, 7 phases, 9 deliverables)
- Standard: `legal-counsel/.../questionnaire-service-agreement.md` (82 questions, 6 batches, 1 deliverable)
- Light: `legal-counsel/.../questionnaire-nda.md` (24 questions, 2 batches, 1 deliverable)
- Meta-framework: `legal-counsel/.../intake-framework.md` (6-batch methodology for all contract types)

---

## 1. Intake Philosophy -- Why Most Intakes Fail

An intake is the structured process of gathering information before producing output. Its quality determines output quality. There is no workaround for a bad intake -- a pitch deck built on shallow answers is a shallow pitch deck.

Most intakes fail in one of three ways:

### The Three Failure Types

**1. Under-Specified**
The intake asks too few questions, or asks them too broadly. "Tell me about your cap table" is one question that hides 8-10 data points. The designer thinks 30 questions is thorough; the deliverables need 75.

*Cost*: Output has gaps. Designer fills gaps with assumptions. User gets something that looks complete but is wrong in the details. Rework is expensive because the errors are embedded throughout.

**2. Over-Specified**
The intake asks 80 questions upfront as a wall of text, or asks questions the user cannot answer at this stage. The user feels interrogated, gives terse answers, or abandons the process entirely.

*Cost*: User disengagement. Shallow or missing answers. The intake technically covers everything but practically captures nothing useful.

**3. Mis-Specified**
The intake asks the wrong questions -- questions that feel relevant but do not feed any deliverable. "What inspired you to start this company?" is a nice question but useless if no deliverable has a "founder inspiration" section.

*Cost*: User's time wasted on information that never appears in output. Meanwhile, the information that IS needed was never asked for. The intake feels thorough but the deliverables have holes.

### Eight Core Principles

These principles prevent all three failure types. They are non-negotiable for any intake worth building.

**Principle 1: Document-First**
Always ingest existing materials before asking questions. If the user has a pitch deck, financial model, prior proposal, or any relevant document, review it first. Extract what you can. Only ask about what remains unanswered.

*Violation consequence*: User re-answers information that's already documented. They lose trust in the process ("I already told you this"). 30-40% of questions become redundant.

**Principle 2: Outcome-Mapped**
Every question must feed at least one deliverable or analytical artifact. If you cannot specify which output section a question supports, delete the question. The "Feeds" field is mandatory. Valid targets include document sections, decision frameworks, alignment analyses, and negotiation strategies -- not just document deliverables.

*Violation consequence*: Floating questions waste user time. Intake feels bloated. No one can explain why certain questions exist.

**Principle 3: Phased by Domain**
Group questions by subject matter (company, market, financials, team), not by deliverable (questions for the deck, questions for the memo). Multiple deliverables need the same information; grouping by domain avoids asking the same thing twice.

*Violation consequence*: Repetitive intake. User answers "tell me about your team" for the deck, then again for the executive summary, then again for the memo. They get irritated or give shorter answers each time.

**Principle 4: Batched for Conversation**
Present 2-4 questions per interaction round. One question per round is tedious. Five or more is overwhelming. Three is the empirical sweet spot. Exception: time-constrained intakes may present all questions in a single batch (see Section 5).

*Violation consequence*: Cognitive overload (too many questions per round) or tedium (too few). Both produce worse answers.

**Principle 5: Conditionally Adaptive**
Not every question is relevant to every engagement. Branch based on answers: if the company is US-only, skip Dutch regulatory questions. If there's no financial model, skip questions about model assumptions and add questions about building one.

*Violation consequence*: Irrelevant questions erode trust. The user thinks "this process doesn't understand my situation." Generic intake feels like a checkbox exercise.

**Principle 6: Validated Before Output**
After the intake is complete, run validation checks before generating any deliverable. Cross-reference answers for contradictions. Compare against benchmarks. Scan for red flags. Score completeness.

*Violation consequence*: Contradictions propagate into deliverables (budget says EUR 2M, use of proceeds sums to EUR 3.5M). Unrealistic claims go unchallenged. Output looks professional but crumbles under scrutiny.

**Principle 7: Partial-Output Capable**
"Intake complete" and "sufficient for deliverable X" are different thresholds. An intake can be complete but only sufficient for the pitch deck (not the financial model). Allow partial output -- produce what you can with what you have. Exception: binary-completeness deliverables (regulatory filings, grant applications) where partial submission is not possible (see Section 16).

*Violation consequence*: All-or-nothing intake. User must answer every question before getting anything. They wait too long; momentum dies. Meanwhile, 80% of one deliverable could already be produced.

**Principle 8: Source-Aware**
Not all information comes from asking the user questions. Some information lives in systems (CRM, accounting, project management), some must be researched from external sources (websites, databases, public filings), and some is derived through synthesis and analysis. Design the intake to pull from the right source for each information item. Only ask the user for information that only the user has.

*Violation consequence*: The user is asked for information the agent could look up independently. User's scarce time is wasted on data entry instead of judgment calls. The intake feels like a bureaucratic form instead of an intelligent conversation.

### When the Value Is Synthesis, Not Collection

Some intakes exist not to gather new information but to synthesize and analyze existing information into a new form. Meeting preparation, competitive intelligence, market analysis, and strategic assessments are examples. The raw data may already exist across multiple sources; the value lies in combining, analyzing, and presenting it with judgment.

In synthesis-driven intakes: the user provides relatively few inputs (anchor information + strategic context), the agent gathers most data from existing sources, and the primary deliverable value is analysis, not documentation. Quality depends on the agent's judgment (thesis fit assessment, objection anticipation), not just data completeness. For synthesis validation, see Section 6.

### When the Output Is a Decision, Not a Document

The guidebook's default framing is document-centric ("deliverable," "section," "component"). Some intakes produce decisions (go/no-go recommendations), alignment (stakeholders reaching shared understanding), or negotiation positions (alignment analysis between counterparties). Treat these as valid output types in the Output Inventory Table. A "Go/No-Go Recommendation" has sections (market attractiveness, strategic fit, risk register) just like a pitch deck has slides.

---

## 2. The 8-Step Design Process

This is the methodology for designing an intake from scratch. Follow the steps in order. Each step produces an artifact that feeds the next.

### Step 1: Define Outputs (Work Backwards)

Before writing a single question, know exactly what you're building toward.

1. List every deliverable the intake must support
2. For each deliverable, list every section or component
3. For each section, describe what information it requires
4. Classify each section's information source and audience

**Output Inventory Table:**

| Deliverable | Section/Component | Information Required | Source Type | Audience |
|---|---|---|---|---|
| [Deliverable 1] | [Section A] | [What data this section needs] | User / CRM / External / Synthesis | Shared / Internal |
| [Deliverable 1] | [Section B] | [What data this section needs] | User | Internal |
| [Deliverable 2] | [Section A] | [What data this section needs] | External | Shared |
| ... | ... | ... | ... | ... |

**Source Type** values:
- **User**: Must be asked as an intake question (only the user has this information)
- **CRM**: Can be pulled from existing system data (HubSpot, ClickUp, accounting)
- **External**: Agent researches from public sources (websites, databases, news)
- **Synthesis**: Agent generates through analysis of combined data (not captured from any single source)

**Audience** values:
- **Shared**: The intake subject sees and may receive this deliverable
- **Internal**: The intake subject never sees this deliverable (e.g., internal risk assessment, deal memo)

This classification affects question design: questions feeding internal-only deliverables must be asked without revealing the internal assessment purpose.

This table is the demand side of your intake. Every row represents information that must come from somewhere. The intake is the supply side.

**Rule**: If a deliverable section has no corresponding intake question, research task, or data point, that section will be empty or fabricated. If an intake question feeds no deliverable section, it should not exist.

**Conditional deliverables**: Some deliverables depend on intermediate findings. A Market Entry Plan only exists if the Go/No-Go Recommendation is "go." Mark conditional deliverables with `[Conditional on: trigger]` in the table.

**Binary-completeness deliverables**: Some deliverables do not support partial output -- a regulatory application is either complete or rejected. Mark these with `[Completeness: Binary]`. See Section 16.

**Comparative deliverables**: Some outputs synthesize data from multiple intake instances into a comparison (evaluation matrices, ranking tables). Mark these with `[Comparative]`. See Section 14.

### Step 2: Inventory Information Dimensions

Take the "Information Required" column from Step 1 and group it by subject matter domain -- not by deliverable.

**Standard domains** (adapt to your context):
- **Identity/Parties**: Who is involved? Legal entities, people, roles, relationships
- **Scope/Problem**: What is being done and why? Problem definition, solution, differentiation
- **Market/Context**: What is the environment? Market size, competition, regulations, trends
- **Technical/Operational**: How does it work? Technology, processes, assets, infrastructure
- **Financial/Commercial**: What are the numbers? Revenue, costs, pricing, projections, budget
- **Legal/Regulatory**: What are the constraints? Contracts, permits, compliance, risk
- **People/Team**: Who does the work? Skills, experience, gaps, organizational structure
- **Strategy/Roadmap**: What happens next? Timeline, milestones, goals, exit/endgame

**Why domains, not deliverables**: The pitch deck needs team information. So does the executive summary. So does the investment memo. If you group by deliverable, you ask about the team three times. If you group by domain, you ask once and map the answers to all three deliverables.

**Domain Inventory Table:**

| Domain | Information Items | Source Type | Feeds Deliverables |
|---|---|---|---|
| Identity | Entity name, type, jurisdiction, structure | User | [List] |
| Scope | Problem, solution, differentiation, moat | User | [List] |
| Market | Size, competition, trends | External + User | [List] |
| ... | ... | ... | ... |

### Step 3: Write the Questions

Convert each information item into a question. Every question has four mandatory fields, with an optional fifth for multi-respondent intakes.

**The Question Architecture:**

| Field | Purpose | Rule |
|---|---|---|
| **ID** | Unique reference for mapping tables | Hierarchical: `[Phase].[Number]` (e.g., 2.3, 4.7). For complex intakes with workstream tracks, use namespaced format: `[Workstream]-[Phase].[Number]` (e.g., GRID-2.3). |
| **Text** | The question itself | One concept per question. Specific, not vague. Quantified where possible. Includes format guidance. |
| **Why It Matters** | 1-2 sentences explaining the need | Connects to the output. Uses the respondent's frame ("Investors benchmark this at..."), not the designer's ("We need this for the model"). |
| **Feeds** | Deliverable sections this question supports | If empty, delete the question. |
| **Asked Of** | *(Optional, for multi-respondent intakes)* Who answers this | Values: `All` / `Founder-A` / `Founder-B` / `Each-Separately` / `Joint`. See Section 13. |

**Question format:**

| Q# | Question | Why It Matters | Feeds |
|---|---|---|---|
| 2.3 | What are your top 3 differentiators vs. alternatives? For each, state: "We do [X] while they do [Y] because [Z]." | Positioning matrix requires specific contrast, not generic claims. Investors will test each differentiator. | Deck Slide 3, 8; IM Section 4; Exec Summary |

**Question types and when to use each:**

| Type | When to Use | Example |
|---|---|---|
| **Factual** | One objectively correct answer | "What is your company registration number?" |
| **Judgmental** | Respondent's assessment needed; provide a framework | "Estimate your TAM, or say 'help me calculate'." |
| **Creative** | Synthesis required; provide structure but allow freedom | "What is your origin story? Why this company, why now, why you?" |
| **Choice** | Finite valid options; always include "other" | "Instrument: SAFE / Convertible Note / Priced Equity / Unsure" |
| **File Upload** | Answer exists in a document | "Share your current pitch deck for review." |
| **Decision** | A design choice that must be made, not a fact to be collected | "Should this role report to the CEO or the CTO? Trade-offs: [CEO = strategic visibility, CTO = technical alignment]" |

**Formatting rules for question text:**
- One concept per question. Never: "Tell me about your team, advisory board, and hiring plan." Always: three separate questions.
- Provide answer format guidance. "For each founder: name, role, relevant experience, prior exits, % time committed" -- not just "describe your team."
- Quantify: specify units (EUR, MW, months, %). "What is your monthly burn rate?" not "describe your expenses."
- Use parenthetical examples when the question is abstract: "What is your moat? (e.g., grid connections, patents, exclusive partnerships, regulatory licenses)"

**Regulated terminology note**: In compliance-driven intakes where specific terms carry legal weight (e.g., Dutch grid terminology: aansluitwaarde vs. transportvermogen vs. teruglevering), add a **Terminology Note** to the question clarifying the precise meaning and distinguishing it from commonly confused terms. See Section 16.

**Question count guidance:**
- 5-15 questions per domain
- 40-100 total core questions depending on complexity
- Conditional questions tracked separately (see Step 6)
- First draft will have too few -- multiply by 2.0-2.5 (see Lessons Learned)

### Step 4: Design Phase 0 (Document Ingestion)

Phase 0 is always first. It prevents redundant interrogation.

**Phase 0 has three sub-phases:**

**Phase 0A: Internal Document Ingestion**
1. What materials already exist? (document checklist)
2. Can you share them for review? (file upload)
3. What is your priority/urgency? (triage)

**Phase 0B: External Research** *(for research-augmented intakes, see Section 12)*
1. Identify external sources to gather (websites, databases, CRM records)
2. Execute research tasks in parallel with user response
3. Capture structured outputs and map to deliverable sections

**Phase 0C: System Data Ingestion** *(for recurring intakes, see Section 15)*
1. Pull current data from system sources (HubSpot, bank, ClickUp)
2. For recurring intakes, load prior run's output as reference
3. Compute deltas against prior period data

**Generic Document Checklist Template:**

```
## Document Existence Checklist
For each, mark: exists / in progress / doesn't exist / N/A

**[Domain Category 1]:**
- [ ] [Document type 1]
- [ ] [Document type 2]
- [ ] [Document type 3]

**[Domain Category 2]:**
- [ ] [Document type 4]
- [ ] [Document type 5]
- [ ] [Document type 6]

**[Domain Category N]:**
- [ ] ...
```

**For compliance-driven intakes**, extend the checklist with validation fields:

| Document | Status | Issued By | Date | Valid Until | Content Confirms |
|---|---|---|---|---|---|
| [Document] | exists / in progress / N/A | [Issuer] | [Date] | [Expiry] | [What it must confirm] |

**Phase 0A Processing Rules:**
1. Read every provided document thoroughly
2. For each document, extract answers to intake questions
3. Note which questions are fully answered, partially answered, or unanswered
4. Generate a gap list of remaining questions
5. Mark skipped questions: `[CAPTURED FROM: document name, page/section]`
6. If documents conflict with each other, flag the conflict and ask the user to resolve
7. If a document is dated, ask: "This is from [date]. Has anything changed since then?"

**The result**: Phase 0 determines the actual intake length. A company with extensive existing materials may skip 40% of questions. A company starting from scratch gets the full intake.

**For progressive intakes**, add a stage detection question at the start of Phase 0:

> Q0.0: "What is the current development stage of this project?"
> Options: [list the stages from the Stage Model -- see Section 15]

This answer determines which question sets are unlocked and which prior answers need re-validation.

### Step 5: Sequence the Phases

Group questions into 4-8 phases by domain. Order them from general to specific, from context to detail.

**Standard Phase Ordering Pattern:**

| Phase | Domain | Purpose | Why This Order |
|---|---|---|---|
| 0 | Document Ingestion | Ingest existing materials, set priority | Must come first to prevent redundancy |
| 1 | Identity / Context | Who are we dealing with? | Everything else depends on knowing who |
| 2 | Problem / Scope | What is being done and why? | Defines the playing field |
| 3 | Market / Environment | What is the landscape? | Contextualizes the problem and solution |
| 4 | Technical / Operational | How does it work? Specifics. | Requires problem and market context first |
| 5 | Financial / Commercial | What are the numbers? | Requires operational specifics to be meaningful |
| 6 | Legal / Risk | What could go wrong? Constraints. | Can only assess risk after understanding the plan |
| 7 | Strategy / Next Steps | What happens next? | Synthesizes everything above into action |

Not every intake needs all 8 phases. A light intake (NDA) may have 2-3 phases. A heavy intake (seed fundraising) may have 7.

**Interaction round design:**
- 2-4 questions per round (golden range)
- Group questions within a round that are topically related
- Signal phase transitions: "Phase 2 complete. Moving to Phase 3: Market & Competitive Landscape."
- Estimate total rounds: total core questions / 3

**Phase template:**

```
## Phase [N]: [Domain Name]
**Purpose:** [1-2 sentences -- what this phase captures and why]
**Feeds:** [List of deliverables this phase supports]
**Interaction rounds:** [N] (Q[X.1]-Q[X.N])
```

**Handling "I don't know" answers:**
- Offer to help: "I can help you estimate this based on [industry data / comparable companies / standard assumptions]."
- Provide benchmarks: "Typical range for this is [X-Y]. Does that match your sense?"
- Mark as gap: if the user genuinely cannot answer and you cannot help, mark it as a gap and note which deliverable sections will be affected.
- Never skip silently. If a primary question is unanswered, the downstream deliverable section will be incomplete. Flag this.

### Time-Constrained Intakes

When the intake has a hard deadline (meeting in 48 hours, filing due tomorrow), the standard phasing rules adapt:

**Batch size override**: Under time pressure, present ALL user questions in a single batch. The 2-4 questions/round guideline assumes interactive multi-session process. When the user has 15 minutes to respond, a single batch of 8-12 questions is correct. Mitigate the "Wall of Questions" risk by grouping questions visually by topic, marking critical vs. nice-to-have, and providing a time estimate.

**Parallel execution**: Start research tasks (Phase 0B) IN PARALLEL with the user answering questions. The moment you have minimum anchor information (e.g., the investor's name), begin research. Do not wait for user responses.

**Phase compression**: Merge validation into output generation rather than running it as a separate pre-output step. Check for consistency and red flags as you draft, not in a separate validation pass.

**"Good enough" threshold**: Define the minimum viable output. For meeting prep: investor profile + thesis fit + 3 talking points + 3 likely questions constitutes a usable brief even if the full package is incomplete. Ship the minimum viable output on time; enhance if time permits.

### Parallel Workstream Support

Some intakes span parallel activities that do not follow a sequential phase order (e.g., site development where grid, permits, and land workstreams all run simultaneously). For these:

- Use **workstream tracks** instead of a single phase sequence. Each workstream is a mini-intake with its own internal phases.
- Use the standard domain-based ordering WITHIN each track, but allow tracks to progress at their own pace.
- Use namespaced IDs: `GRID-2.3`, `PERMIT-1.5`, `BESS-3.2`.
- See Section 15 for the full progressive intake model.

### Step 6: Add Conditional Logic

Conditional questions are triggered by specific answers. They are not asked to everyone.

**Four types of conditionals:**

| Type | When | Example |
|---|---|---|
| **Skip** | Answer makes a question irrelevant | If "no employees" -> skip questions about employment agreements and ESOP |
| **Expand** | Answer reveals complexity needing deeper questions | If "Swiss AG" -> ask about authorized capital, stamp duty, capital band |
| **Redirect** | Answer shifts to a different domain entirely | If "existing debt" -> ask about covenant compliance, change-of-control provisions |
| **Hard Fork** | Answer changes the deliverable or receiving authority entirely | If capacity >10 MVA -> switch from DSO application to TenneT application (different form, timeline, requirements) |

**Rules:**
- Conditional questions are triggered by answers, not by phase completion
- Ask them immediately after detecting the trigger condition (same round if possible, next round at latest)
- Track them separately from core question count: "65 core + up to 15 conditional"
- Use suffix notation for IDs: if Q1.2 triggers a conditional, it becomes Q1.2a, Q1.2b
- If a conditional would require third-level nesting, promote it to a new numbered question with a trigger annotation

**Cross-domain conditionals**: Some conditionals are triggered by the relationship between answers in different domains (e.g., "if grid capacity < BESS design capacity"). These are evaluated after each session, not after each question, because they require data from multiple domains collected at different times.

**Conditional Question Table:**

| Condition | Triggered By | Additional Question(s) | Why |
|---|---|---|---|
| [If X answer to Q Y] | Q[N.N] = [value] | [Question text] | [Why this matters given the trigger] |

**Design tip**: Conditionals are where intakes transform from generic checklists to tailored conversations. A good intake adapts to the user's situation. Most of the "that was surprisingly relevant" moments come from conditional questions, not core questions.

### Step 7: Build the Validation Framework

After all phases are complete, run seven checks before generating any output. See Section 6 for the full framework.

### Step 8: Map Questions to Deliverables

Create the traceability matrix that connects every question to every output, and every output back to every question. See Section 7 for the full methodology.

---

## 3. Phase 0 Deep Dive -- Document Ingestion

Phase 0 is the highest-ROI phase in any intake. It eliminates 30-40% of redundant questions and prevents "I already told you this" frustration.

### Why Document Ingestion Matters

Users rarely start from zero. They have prior presentations, proposals, financial models, strategy documents, contracts, research reports, or at minimum, a website and LinkedIn profile. Asking questions that these documents already answer is:
- Wasteful of the user's time
- A signal that the process is generic, not tailored
- An opportunity to capture nuance that questions alone miss (a financial model reveals assumptions; a prior deck reveals narrative framing; a contract reveals risk allocation)

### The Document Ingestion Protocol

**Step 1: Ask what exists**

Use the document checklist (see template in Section 8). Group by domain. Status options: exists / in progress / doesn't exist / N/A.

**Step 2: Request priority materials**

Not everything needs to be ingested at once. Prioritize:
1. Documents that answer the most intake questions (e.g., a pitch deck covers identity, problem, solution, market, team, financials)
2. Documents that are hardest to reconstruct from questions alone (e.g., financial models with embedded assumptions, signed contracts with specific terms)
3. Documents the user considers most current and accurate

**Step 3: Process each document**

For each ingested document:
1. Read completely -- do not skim
2. For each intake question (Phases 1-N), check: does this document contain the answer?
3. If yes: extract the answer and mark the question as `[CAPTURED FROM: document name]`
4. If partially: extract what you can, note what's missing, prepare a targeted follow-up question
5. If no: leave the question in the active intake

**Step 4: Handle edge cases**

| Situation | Action |
|---|---|
| Documents conflict with each other | Surface both versions. Ask: "Your pitch deck says [X], but your financial model shows [Y]. Which is current?" |
| Document is outdated | Ask: "This is dated [month/year]. Has anything changed since then?" Focus on the sections most likely to have shifted. |
| User says "I don't have anything" | Still ask the checklist. Users often have more than they realize -- articles of association, a LinkedIn company page, a one-pager for partners, WhatsApp messages with key decisions. |
| Too many documents to process | Prioritize by deliverable coverage. A pitch deck and a financial model together answer more questions than any other combination. Start there. |

**Step 5: Generate the gap list**

After processing all documents, produce a gap list:

```
## Phase 0 Gap Analysis
**Documents ingested:** [List]
**Questions answered from documents:** [Count] of [Total]
**Remaining questions by phase:**
- Phase 1: [N] questions remaining (out of [M])
- Phase 2: [N] questions remaining
- ...
**Questions with partial answers (need confirmation):** [List with specifics]
```

This gap list becomes the active intake. Only remaining questions are asked.

### Domain-Specific Document Examples

**Website redesign project**: existing brand guidelines, current sitemap, analytics reports (Google Analytics export), prior design proposals, competitor screenshots, content inventory, SEO audit, hosting/infrastructure documentation

**M&A transaction**: financial statements (3 years), management accounts, data room index, information memorandum, LOIs received, due diligence reports, material contracts, cap table, shareholder agreements

**Consulting engagement**: prior proposals, project plans, status reports, deliverable samples, client briefs, stakeholder maps, meeting notes, budget spreadsheets

**Product launch**: product requirements document, market research, competitor analysis, positioning statements, pricing models, go-to-market plan, launch timeline, beta test results

---

## 4. Question Architecture -- Writing Questions That Work

The quality of your questions determines the quality of your answers. This section covers the craft of writing intake questions that produce usable, specific, deliverable-ready responses.

### The Mandatory Fields

Every question in every intake has exactly four fields (five for multi-respondent intakes). No exceptions.

**Field 1: ID**

Format: `[Phase].[Number]` -- e.g., 2.3 means Phase 2, Question 3.

Why hierarchical: enables referencing in mapping tables, validation matrices, and gap lists without ambiguity. "Q2.3" is unambiguous; "the question about differentiation" is not.

Conditional questions use suffix notation: Q1.2a, Q1.2b (triggered by Q1.2).

For complex intakes with workstream tracks: `[Workstream]-[Phase].[Number]` (e.g., `GRID-2.3`). If a conditional would require third-level nesting (`Q3.1a.i`), promote it to a new numbered question instead (`Q3.10` with trigger annotation).

**Field 2: Text**

The question itself. This is what the user sees. Rules:

*One concept per question.* The most common intake defect is the compressed question. "Tell me about your cap table, ESOP, and share class structure" is three questions disguised as one. The user will answer whichever part they find easiest and skip the rest. Decompose it.

Test: if you need to use "and" or a semicolon, it's probably two questions.

*Be specific.* "Describe your team" gets a vague paragraph. "For each founder: name, current role, relevant prior experience (companies, roles, years), notable achievements or exits, and percentage of time committed to this company" gets usable data.

*Quantify where possible.* "What is your burn rate?" could get "moderate" or "sustainable." "What is your current monthly burn rate in EUR?" gets a number. Specify units (EUR, USD, MW, months, %, headcount) and whether you want absolute values or ranges.

*Provide format guidance.* When the answer needs structure, say so: "List each revenue stream with: stream name, pricing model (e.g., EUR/MWh, $/kW/month), contract structure (fixed/variable, term in years, escalation), and current status (contracted/LOI/pipeline)."

*Use parenthetical examples for abstract questions.* "What is your moat?" is abstract. "What is your defensibility -- what prevents a well-funded competitor from replicating your position in 12-18 months? (e.g., proprietary grid connections, patented technology, exclusive land agreements, regulatory licenses, long-term customer contracts)" is concrete.

**Field 3: Why It Matters**

1-2 sentences explaining why this question needs to be answered. Serves two purposes:

1. *Educates the respondent*: They understand the importance of giving a thorough answer, not a throwaway one.
2. *Disciplines the designer*: If you cannot explain why a question matters, it probably doesn't. Delete it.

Writing guide for "Why It Matters":
- Connect to the output: "This feeds the financial model's revenue tab and determines whether projections are top-down or bottom-up."
- Show downstream impact: "Without this, we cannot calculate post-round dilution or model the cap table."
- Use the respondent's frame, not the designer's: "Investors will benchmark your cost-per-MW against industry data" is better than "we need cost data for our comparison."
- Keep it honest. If the real reason is "the pitch deck template has a team slide," say that.
- For non-cooperative contexts (sales qualification, adversarial negotiations): frame "Why It Matters" in terms of VALUE TO THE RESPONDENT. "This helps us structure appropriate payment terms for your timeline" not "This feeds our credit risk scoring." See Section 13.
- For compliance-driven intakes: include the CONSEQUENCE of getting it wrong. "Providing the wrong value here will result in a mismatched grid allocation that cannot be corrected without re-filing." See Section 16.

**Field 4: Feeds**

List of deliverable sections this question supports. Format: `[Deliverable] [Section]`.

Example: `Deck Slide 11, IM Section 10, Financial Model Cash Flow tab`

If a question feeds nothing, it does not belong in the intake. If a deliverable section has no question feeding it, the section will be empty. Both conditions are errors.

For living deliverables, a question may feed a section that does not yet exist in the current version: `SDP v2: Grid Connection Detail [unlocks at: grid allocation received]`.

**Field 5: Asked Of** *(Optional -- for multi-respondent intakes only)*

Who provides the answer. Values: `All` / `[Person/Role A]` / `[Person/Role B]` / `Each-Separately` / `Joint`.

Use `Each-Separately` when the same question is asked to multiple respondents independently (e.g., JV where each party states their ownership expectation). Use `Joint` when the question requires collaborative deliberation.

### Respondent Archetypes

Not all respondents interact the same way. Calibrate question framing, "Why It Matters," and round sizing based on:

| Archetype | Characteristics | Adaptation |
|---|---|---|
| **Sophisticated Professional** | Domain expert, familiar with structured processes | Standard framing. Can handle technical language. |
| **Domain Expert, Process Outsider** | Knows their field but unfamiliar with intake processes | More "Why It Matters." Avoid process jargon. |
| **Delegating Principal** | Senior person who sends a subordinate to answer | Design for proxy: explicit format guidance, multiple-choice where possible. |
| **Reluctant Participant** | Doesn't want to be doing this (e.g., grower, non-technical partner) | Shorter rounds, simpler language, clear benefit framing, minimize jargon. |
| **Non-Cooperative Subject** | External party with competing interests (e.g., sales prospect) | Conversational wrapper around structured questions. Frame value exchange. See Section 13. |

### Conditional Question Design

Conditionals transform generic intakes into tailored conversations.

**Trigger mechanism**: A conditional question is triggered by a specific answer value to an earlier question. Not by phase completion. Not by the designer's guess about what might be relevant.

Example: Q1.1 asks "Entity type and jurisdiction." If the answer includes "Swiss AG," conditional Q1.1a asks "Has the AG established authorized capital (genehmigtes Kapital)? If so, what amount and what resolution date?" This question is irrelevant to a Dutch BV or a US Delaware LLC.

**Timing**: Ask conditional questions immediately after detecting the trigger. Do not defer them to a later phase. The user's mind is already on the topic.

**Tracking**: Conditional questions are tracked separately from core questions. Report intake size as "65 core + up to 15 conditional" so the user understands the range.

---

## 5. Phase Design -- Sequencing and Batching

Phases are the macro-structure of your intake. Rounds are the micro-structure. Getting both right determines whether the intake feels like a conversation or an interrogation.

### Phase Grouping: By Domain, Not by Deliverable

This is the single most impactful design decision in intake architecture.

**By deliverable** (wrong): "First, let's collect everything for the pitch deck. Now, let's collect everything for the executive summary. Now, the investment memo."

Problem: The pitch deck, exec summary, and memo all need team information. The user answers "describe your team" three times. By the third time, answers are terse.

**By domain** (right): "First, let's cover your team and organization. Now, your market and competitive landscape. Now, your financials."

Benefit: Each topic is covered once, thoroughly. The question-to-deliverable mapping (Section 7) routes each answer to every deliverable that needs it.

### Standard Phase Ordering

The recommended ordering follows a natural information hierarchy:

**Context before detail**: You need to know WHO the company is before asking WHAT they're building. You need to know WHAT they're building before asking HOW MUCH it costs.

**Facts before opinions**: Entity registration numbers are facts. Market size estimates are opinions. Start with what the user knows with certainty. Build to what requires judgment.

**Broad before narrow**: "What is your target market?" before "What is your per-unit pricing in the secondary market?"

### Adaptable Phase Template

Not every project needs every phase. A light intake (NDA) needs only Identity and Scope. A heavy intake (seed fundraising) needs all phases plus domain-specific additions (Assets/Traction for infrastructure).

Select phases based on your deliverables. If no deliverable needs financial information, skip the Financial phase.

### Interaction Round Design

**Golden range: 2-4 questions per round.**

| Round Size | Effect |
|---|---|
| 1 question/round | Tedious. Too many back-and-forths. User feels like they're being drip-fed. |
| 2 questions/round | Comfortable for complex questions that need thought. |
| 3 questions/round | Optimal for most situations. Fast enough to feel like progress, small enough to answer thoroughly. |
| 4 questions/round | Maximum for straightforward factual questions. |
| 5+ questions/round | Overwhelming. User skims, gives shorter answers, misses questions entirely. |

**Within a round**: Group questions that are topically related. If Round 3 asks about team composition (Q1.5), advisory board (Q1.6), and key hires (Q1.7), the user's mind stays in "people" mode. Don't mix team questions with financial questions in the same round.

**Between rounds**: Signal the transition. "Phase 1 complete -- we now have a clear picture of your company structure and team. Moving to Phase 2: Problem, Solution & Moat."

**Estimating total rounds**: Total core questions / 3 = approximate number of rounds. A 75-question intake = ~25 rounds. At 3-5 minutes per round, that's ~75-125 minutes total. For heavy intakes, split across sessions.

---

## 6. Validation Framework -- Post-Intake Quality Gates

After all intake phases are complete, run seven validation checks before generating any deliverable. These checks catch errors that humans miss -- contradictions between answers, unrealistic figures, missing documentation, and structural red flags.

Run validation BEFORE output, not after. Catching a contradiction before the deck is written costs one follow-up question. Catching it after costs a full rewrite.

### Check 1: Internal Consistency

**Purpose**: Cross-reference answers for contradictions.

**Method**: Create a consistency matrix -- pairs of questions whose answers must logically align. Run each check. Flag mismatches.

**Generic consistency patterns:**

| Check Category | Compare | Red Flag If |
|---|---|---|
| Budget vs. Scope | Total budget/funding vs. itemized allocations | Allocations don't sum to total (+-10%) |
| Timeline vs. Resources | Stated timeline vs. team size and capabilities | Timeline requires capabilities the team doesn't have |
| Claims vs. Evidence | Claimed achievements vs. supporting documentation | Claims exist but no documents to support them |
| Strategy vs. Capabilities | Planned approach vs. available skills/resources/assets | Strategy depends on resources not yet acquired |
| Revenue vs. Operations | Revenue projections vs. operational capacity | Revenue projected from capacity that doesn't yet exist |
| Headcount vs. Budget | Planned hires vs. allocated hiring budget | Hires cost more than budget allows |
| Milestones vs. Funding | Stated milestones vs. funding amount and runway | Key milestones fall after cash runs out |

**Template:**

| # | Check | Q[X] Says | Q[Y] Says | Aligned? | Note |
|---|---|---|---|---|---|
| 1 | Budget vs. allocations | Round size: EUR [X] | Allocations sum to: EUR [Y] | Y/N | |
| 2 | ... | ... | ... | ... | |

**Action on mismatch**: Surface to the user. Ask them to reconcile. Do not silently resolve contradictions -- your interpretation may be wrong.

### Check 2: Benchmark Comparison

**Purpose**: Compare key quantitative answers against domain-specific norms.

**Method**: For each quantitative answer, compare against known benchmarks. Flag values outside expected ranges.

**Template:**

| Metric | User's Value | Benchmark Range | Source | Flag If |
|---|---|---|---|---|
| [Metric name] | [Value from intake] | [Low] - [High] | [Where benchmark comes from] | [Condition that triggers flag] |

**Important**: The intake designer must define benchmarks as part of intake design. This is not generic "does this seem reasonable?" -- it requires domain expertise. If you're building a fundraising intake, know the benchmark pre-money valuations for seed rounds. If you're building a website intake, know the benchmark timeline for a redesign of this complexity.

If no benchmarks exist for your domain, skip this check and note its absence. A missing benchmark check is better than a fabricated one.

### Check 3: Red Flag Scan

**Purpose**: Identify issues that downstream consumers (investors, counterparties, reviewers, decision-makers) would flag.

**Key insight: Red flags are NOT auto-disqualifiers.** A solo founder is a red flag at seed stage. It does not mean "do not proceed." It means "this will be questioned -- we must address it proactively in the materials with a clear mitigation plan."

**Template:**

| Category | Red Flag | Trigger Condition | Severity |
|---|---|---|---|
| [Area] | [What the flag is] | [What answer triggers it] | High / Medium / Low |

**Severity calibration:**
- **High**: Likely deal-breaker or project-stopper if unaddressed. Must be resolved or explicitly framed with strong mitigation before output generation.
- **Medium**: Will be questioned by reviewers/counterparties. Needs framing in the deliverables but doesn't block production.
- **Low**: Minor concern. Can be noted without special treatment.

**Generic red flag categories (adapt to your domain):**
- **Single point of failure**: One person, one customer, one supplier, one technology, one permit
- **Missing documentation**: Claimed achievements without supporting evidence
- **Unrealistic projections**: Values outside benchmark ranges without justification
- **Legal/compliance gaps**: Missing agreements, permits, registrations that should exist at this stage
- **Team gaps**: Critical roles unfilled without a plan to fill them
- **Dependency risks**: Success depends on factors outside the team's control

**Action on red flags**: Surface all flags to the user with their severity. For each High flag, ask: "How should we address this?" The answer becomes mitigation framing in the deliverables. Never suppress red flags.

### Check 4: Completeness Assessment

**Purpose**: Score the intake against each deliverable's requirements.

**Method**: For each deliverable, count primary questions answered vs. required.

**Template:**

| Deliverable | Primary Qs Required | Primary Qs Answered | Missing | Status |
|---|---|---|---|---|
| [Deliverable 1] | [N] | [N] | [List Q#s] | Ready / Partial / Blocked |
| [Deliverable 2] | [N] | [N] | [List Q#s] | Ready / Partial / Blocked |

**Status definitions:**
- **Ready**: All primary questions answered. Output can be generated.
- **Partial**: Some primary questions missing. Output can be generated with gaps clearly marked.
- **Blocked**: Critical primary questions missing. Cannot generate output without these answers.

For binary-completeness deliverables (regulatory filings): the only valid statuses are Ready and Blocked. There is no "Partial."

### Check 5: Output Recommendation

**Purpose**: Based on the user's context and intake completeness, recommend what to produce first.

**Method**: Matrix of user context (stage, urgency, stated priority from Phase 0) vs. completeness status.

**Template:**

| If [Context] | And [Status] | Then Recommend |
|---|---|---|
| User hasn't started [process] | Deliverable A is Ready | Produce Deliverable A first |
| User is actively in [process] | Deliverable B is Partial | Produce Deliverable B with gaps flagged; ask remaining questions for gaps |
| User needs [urgent thing] | Deliverable C is Blocked | Ask the [N] blocking questions immediately, then produce |

This check is deterministic. Given the user's stated priority (from Phase 0) and the completeness scores, the recommendation writes itself. No judgment required.

### Check 6: Temporal Consistency *(for recurring intakes)*

**Purpose**: Compare this run's answers against prior runs for consistency and trend coherence.

**Method**: For each metric that appeared in a prior run, check for unexpected changes.

| Sub-Check | Method | Flag If |
|---|---|---|
| Month-over-month delta | Compare each metric to last period | Any metric changes >X% without explanation |
| Trend analysis | Compare 3-6 period trend for key metrics | Sustained negative trend without acknowledged mitigation |
| Plan vs. actual | Compare stated plans (from last period's "next steps") to actual results | Milestones consistently slip without plan adjustment |
| Narrative consistency | Compare this period's narrative to last period's | Strategic direction changed without explicit acknowledgment |
| Action item tracking | Check if prior period's asks/actions were resolved | Items open for 3+ periods without update |

### Check 7: Regulatory/External Compliance *(for compliance-driven intakes)*

**Purpose**: Verify that intake answers satisfy external requirements imposed by the receiving authority.

**Method**: For each key parameter in the application, verify against the authority's published rules.

| # | Parameter | Applicant's Value | External Requirement | Source | Compliant? | Action If Not |
|---|---|---|---|---|---|---|
| 1 | [Field] | [Value from intake] | [Rule from authority] | [Publication/guideline] | Y/N | [Remediation] |

Common checks: document recency, parameter feasibility (within authority's capacity), cross-document consistency (values match across supporting documents from different authorities), procedural prerequisites completed.

### Synthesis Validation *(for synthesis-driven intakes)*

When the primary value is analysis rather than data collection, add these checks:

- [ ] Analysis is specific to THIS situation (not generic)
- [ ] Conclusions are supported by cited evidence from research
- [ ] Opposing viewpoints or risks are acknowledged
- [ ] Recommendations are actionable and concrete
- [ ] The user could not have produced this themselves with a simple search (agent added analytical value)

### Pre-Flight Checklist (Run Before Every Output)

Before generating any specific deliverable, verify:

- [ ] All primary questions for this deliverable have been answered (or research tasks completed)
- [ ] Internal consistency check passed for this deliverable's data
- [ ] Red flags relevant to this deliverable have been discussed
- [ ] Benchmark comparison completed for quantitative claims in this deliverable
- [ ] User has reviewed and approved the intake summary / profile
- [ ] Output format confirmed with user

---

## 7. Question-to-Deliverable Mapping -- The Traceability Matrix

The mapping is the backbone of the intake. It connects every question to every output, and every output back to every question. Without it, the intake is a list of questions and the deliverables are a list of outputs with no verifiable connection between them.

### Why the Mapping Matters

1. **Enables partial output**: If you know which questions feed the pitch deck, you can produce the deck as soon as those questions are answered -- even if the financial model questions are incomplete.
2. **Enforces discipline**: A question with no feeds is waste. A deliverable section with no feeding question or research task is a gap. The mapping catches both.
3. **Enables Mode B (targeted)**: When the user wants one specific deliverable, look up its primary questions. Ask only those. Skip the rest. This is faster than the full intake.

### Building the Map

**Step 1**: Take the Output Inventory Table from Step 1 of the design process.

**Step 2**: For each deliverable section, identify which intake questions, research tasks, or data points provide the data.

**Step 3**: Classify each relationship as:
- **Primary**: This question MUST be answered to produce this section. If it's missing, the section is either empty or blocked.
- **Secondary**: This question enhances the section. If it's missing, the section can still be produced but may be thinner.

**Step 4**: Verify coverage:
- Every deliverable section has at least one primary question, research task, or data point feeding it. (If not: add one.)
- Every question feeds at least one deliverable section. (If not: delete the question.)

### Map Formats

**Format A: Deliverable-Centric** (most common, used for output generation)

```
### [Deliverable Name]
| Section | Primary Sources (Q/R/D) | Secondary Sources |
|---|---|---|
| [Section 1] | Q1.1, Q1.3, R2 | Q2.7 |
| [Section 2] | Q2.1, Q2.2, D1.3 | Q3.9, R5 |
| ... | ... | ... |
```

Where Q = Question, R = Research Task, D = Data Point (system-sourced).

**Format B: Question-Centric** (used in the question table itself, via the "Feeds" field)

Each question's Feeds field lists: `Deck Slide 3, IM Section 4, Exec Summary Solution`

Both formats encode the same information. Use Format A when generating deliverables. Use Format B when designing questions.

### Binary-Completeness Mapping

For deliverables that do not support partial output (regulatory filings, grant applications): ALL mapped sources are effectively Primary. There is no meaningful Secondary classification. The Completeness Assessment status has only two values: Ready or Blocked.

### Mode A vs. Mode B

**Mode A (Full Intake)**: All questions across all phases. All deliverables can be produced. Use when starting from scratch or when the user wants comprehensive output.

**Mode B (Targeted Deliverable)**: User requests a specific deliverable. Look up its primary questions in the mapping. Ask only those (plus Phase 0 for document ingestion). Produce that one deliverable.

Mode B is faster but carries a risk: cross-deliverable inconsistencies may not be caught because validation runs on a subset of data. Flag this to the user: "We have enough to produce the [deliverable]. Note that a full intake would enable consistency checking across all materials."

---

## 8. Templates -- Reusable Structures

Copy, paste, and fill. These templates are designed to be used as-is with minimal adaptation.

### Template 1: Intake Design Canvas

```
# [Project/Skill Name] Intake Design

## Overview
- **Deliverables:** [List all outputs this intake supports]
- **Phases:** [Count] (Phase 0 + Phases 1-[N])
- **Core questions:** [Count] (~[N] interaction rounds)
- **Conditional questions:** up to [Count] additional
- **Research tasks:** [Count] (if research-augmented)
- **System data points:** [Count] (if recurring/system-sourced)
- **Estimated intake time:** [N] minutes at [N] rounds
- **Deliverable completeness:** Standard / Binary

## Phase Summary
| Phase | Domain | Purpose | Qs | Rounds | Feeds |
|---|---|---|---|---|---|
| 0 | Document Ingestion | Ingest existing materials, set priority | [N] | 1 | All |
| 1 | [Domain] | [Purpose] | [N] | [N] | [Deliverables] |
| ... | ... | ... | ... | ... | ... |

## Weight Class: [Ultra-Light / Light / Standard / Heavy / Ultra-Heavy]
```

### Template 2: Phase Header

```
## Phase [N]: [Domain Name]
**Purpose:** [1-2 sentences]
**Feeds:** [Deliverable list]
**Interaction rounds:** [N] (Q[X.1]-Q[X.N])
```

### Template 3: Question Table

```
| Q# | Question | Why It Matters | Feeds |
|---|---|---|---|
| [N.N] | [Question text] | [1-2 sentences] | [Deliverable sections] |
```

### Template 4: Conditional Question Table

```
**Conditional Questions (Phase [N]):**
| Condition | Triggered By | Additional Question | Why |
|---|---|---|---|
| If [answer value] | Q[N.N] | [Question text] | [Why this matters given the trigger] |
```

### Template 5: Document Ingestion Checklist

```
## Phase 0: Document Checklist
For each, mark: exists / in progress / doesn't exist / N/A

**[Category 1]:**
- [ ] [Document type]
- [ ] [Document type]

**[Category 2]:**
- [ ] [Document type]
- [ ] [Document type]

**[Category N]:**
- [ ] [Document type]
```

### Template 6: Consistency Check Matrix

```
## Post-Intake: Internal Consistency Check
| # | Check | Q[X] Says | Q[Y] Says | Aligned? | Action If Not |
|---|---|---|---|---|---|
| 1 | [Description] | [Value] | [Value] | Y/N | [Ask user to reconcile] |
```

### Template 7: Benchmark Comparison Table

```
## Post-Intake: Benchmark Comparison
| Metric | User's Value | Benchmark Range | Source | Flag? |
|---|---|---|---|---|
| [Metric] | [Value] | [Low]-[High] | [Source] | Y/N |
```

### Template 8: Red Flag Scan Table

```
## Post-Intake: Red Flag Scan
| Category | Red Flag | Trigger | Severity | Status |
|---|---|---|---|---|
| [Area] | [Flag] | [Q# answer condition] | H/M/L | Open / Discussed / Resolved |
```

### Template 9: Deliverable Readiness Scorecard

```
## Post-Intake: Deliverable Readiness
| Deliverable | Primary Qs Required | Answered | Missing | Status |
|---|---|---|---|---|
| [Name] | [N] | [N] | [Q#s] | Ready / Partial / Blocked |
```

### Template 10: Question-to-Deliverable Map

```
## Question-to-Deliverable Mapping: [Deliverable Name]
| Section/Component | Primary Sources (Q/R/D) | Secondary Sources |
|---|---|---|
| [Section] | Q[N.N], R[N] | Q[N.N] |
```

### Template 11: Pre-Flight Checklist

```
## Pre-Flight: [Deliverable Name]
- [ ] All primary questions answered (per mapping)
- [ ] All research tasks completed (per mapping)
- [ ] Consistency check passed -- no unresolved contradictions
- [ ] Red flags surfaced and discussed with user
- [ ] Benchmark comparison completed for quantitative claims
- [ ] User approved the intake summary / profile
- [ ] Output format confirmed with user
```

### Template 12: Intake Completion Criteria

```
## Intake Completion Criteria

**COMPLETE** when ALL of these are met:
- [ ] All phases completed (Phase 0 through Phase [N])
- [ ] All triggered conditional questions asked and answered
- [ ] Internal consistency check passed (no unresolved contradictions)
- [ ] Benchmark comparison completed (outliers explained or corrected)
- [ ] Red flags identified and discussed
- [ ] Completeness scored per deliverable
- [ ] Output recommendation provided
- [ ] Intake summary / profile generated and approved by user

**SUFFICIENT for [Deliverable X]** when:
- [ ] All primary questions for that deliverable answered
- [ ] No critical (High severity) red flags unresolved for that deliverable
```

### Template 13: Research Task Table

```
## Research Tasks
| R# | Source | Data Points to Extract | Feeds | Priority | Est. Time |
|---|---|---|---|---|---|
| R1 | [Source/URL] | [What to extract] | [Deliverable sections] | High/Med/Low | [Minutes] |
```

### Template 14: Data Point Table (System-Sourced)

```
## System Data Points
| D# | Data Point | Source System | Retrieval Method | Validation Rule | Feeds |
|---|---|---|---|---|---|
| D1.1 | [Value needed] | [System + field] | [API/export/manual] | [Range/delta check] | [Deliverable sections] |
```

### Template 15: Automation Maturity Tracker

```
## Automation Maturity (for recurring intakes)
| Item | Current Level | Target Level | Promotion Criteria |
|---|---|---|---|
| [Info item] | L0-Manual / L1-Assisted / L2-Trusted / L3-Auto | [Target] | [What must happen to promote] |
```

### Template 16: Delta Conditional Table

```
## Delta-Based Conditionals (for recurring intakes)
| Delta Type | Trigger Condition | Action |
|---|---|---|
| Spike | [Metric] increased >X% vs. last period | Ask: "What drove the increase?" |
| Drop | [Metric] decreased >X% vs. last period | Ask: "What happened? Is this structural?" |
| Slip | [Milestone] not achieved by stated date | Ask: "What blocked this? New timeline?" |
| Stale | [Value] unchanged for 3+ periods | Ask: "Is this still accurate?" |
```

### Template 17: Temporal Validation Check

```
## Post-Intake: Temporal Consistency (Run [N])
| Metric | Last Period | This Period | Delta | Explained? | Action |
|---|---|---|---|---|---|
| [Metric] | [Value] | [Value] | [Change] | Y/N | [Follow-up if unexplained] |
```

### Template 18: Multi-Party Intake Canvas

```
## Multi-Party Intake: [Project Name]
**Parties:** [Party A], [Party B]
**Operator role:** Advisor to [A] / Neutral facilitator / Hybrid
**Confidentiality model:** [Shared / Party-Confidential / Operator-Only tags]
**Parallel streams:** [Party A intake] || [Party B intake]
**Synchronization points:** [After Phase N, run alignment analysis]
**Deliverables:** [Per-party + joint + alignment analysis]
```

### Template 19: Alignment Gap Analysis

```
## Alignment Analysis: [Topic]
| Dimension | Party A Position | Party B Position | Gap Classification | Resolution Mechanism |
|---|---|---|---|---|
| [Dimension] | [Position] | [Position] | Aligned / Negotiable / Structural / Conflict / Deal-Breaker | [Proposed approach] |
```

### Template 20: Weighted Scoring Matrix

```
## Evaluation Matrix: [Category]
| Criterion | Weight | [Subject 1] Score | [Subject 2] Score | [Subject 3] Score |
|---|---|---|---|---|
| [Criterion] | [%] | [1-5] | [1-5] | [1-5] |
| **Weighted Total** | **100%** | **[Sum]** | **[Sum]** | **[Sum]** |
```

### Template 21: Compliance Document Checklist

```
## Compliance Document Checklist
| Document | Status | Issued By | Date | Valid Until | Content Confirms | Format |
|---|---|---|---|---|---|---|
| [Document] | exists/in progress/N/A | [Required issuer] | [Date] | [Expiry] | [Required content] | [PDF/original/certified] |
```

---

## 9. Anti-Patterns -- What NOT to Do

These are documented failure modes observed across 20+ skill intake designs. Each follows the same structure: what it looks like, why it happens, the damage it causes, and how to fix it.

### Anti-Pattern 1: The Wall of Questions

**What it looks like**: Presenting 20, 30, or 50 questions at once in a single batch.

**Why it happens**: The designer knows all the questions needed and wants to be "efficient" by asking everything upfront. Or the designer hasn't thought about phasing.

**The damage**: User is overwhelmed. They skim the list, answer the easy questions, skip the hard ones, and give terse responses throughout. Completion rates drop. Answer quality drops. The intake looks thorough on paper but captures shallow data.

**The fix**: Phase into 2-4 question batches. Present Phase 0, wait for answers, present Phase 1 Round 1, wait, continue. The user's cognitive load stays manageable. Exception: time-constrained intakes (see Section 5) where a single well-structured batch is the correct approach.

### Anti-Pattern 2: The Compressed Question

**What it looks like**: "Tell me about your team, cap table, and corporate structure." Or: "Describe your market opportunity, competitive landscape, and go-to-market strategy."

**Why it happens**: The designer confuses topics with questions. They think of "team" as one question when it's actually 4-6 (founders, advisors, headcount, key hires, governance, ESOP).

**The damage**: The user answers whichever sub-component they find easiest or most interesting. The rest is skipped. The designer gets a paragraph about the founders but nothing about the advisory board, ESOP, or hiring plan. The deliverable has gaps that only surface during output generation.

**The fix**: One concept per question. If you need "and" or a semicolon, split it. "For each founder: name, role, experience, exits, % time committed" is one specific question. "Team, advisors, and governance" is three.

### Anti-Pattern 3: The Floating Question

**What it looks like**: A question that feels relevant but feeds no deliverable. "What inspired you to enter this industry?" when no deliverable has an "inspiration" section.

**Why it happens**: The designer asks "nice to know" questions out of curiosity or because they seem like good intake questions in general.

**The damage**: User's time wasted on information that never appears in any output. The intake feels bloated. Over time, trust erodes as users realize some answers go nowhere.

**The fix**: Every question gets a "Feeds" field. If empty, delete the question. The mapping table (Section 7) catches this automatically.

### Anti-Pattern 4: No Document Ingestion

**What it looks like**: Jumping straight to questions without asking what materials already exist.

**Why it happens**: The designer assumes a blank slate. Or the designer hasn't built a Phase 0.

**The damage**: User re-answers information that's already in their pitch deck, financial model, prior proposals, or contracts. They get frustrated. 30-40% of questions are redundant. The intake takes twice as long as necessary.

**The fix**: Always start with Phase 0. Even if the user says "I don't have anything," ask the document checklist. They usually have more than they think.

### Anti-Pattern 5: Grouping by Deliverable

**What it looks like**: "Let me collect everything for the pitch deck first, then everything for the executive summary, then the investment memo."

**Why it happens**: Feels logical from the designer's perspective -- finish one output's inputs, then the next.

**The damage**: The pitch deck needs team information. So does the exec summary. So does the memo. The user answers "describe your team" three times in slightly different framings. By the third time, answers are minimal. Or the user says "I already told you this," breaking the interaction flow.

**The fix**: Group by domain (Section 5). Ask about team ONCE. Map the answers to all deliverables that need them (Section 7).

### Anti-Pattern 6: No Conditional Logic

**What it looks like**: The same 50 questions asked to every user regardless of their situation.

**Why it happens**: The designer builds a static questionnaire. It covers all possible scenarios but doesn't adapt to the actual scenario.

**The damage**: Irrelevant questions erode trust. A US-only company being asked about Dutch BV structures. A pre-revenue startup being asked about revenue growth rates. A sole proprietor being asked about board composition. Each irrelevant question signals "this process doesn't understand me."

**The fix**: Add conditional logic (Step 6). If the entity is US-only, skip Dutch regulatory questions. If pre-revenue, replace revenue growth questions with go-to-market questions. The intake adapts to the user's reality.

### Anti-Pattern 7: Post-Hoc Validation

**What it looks like**: Generate the deliverable first, then review it for quality.

**Why it happens**: The designer wants to show output quickly. Validation feels like unnecessary overhead.

**The damage**: Contradictions, unrealistic projections, and red flags get embedded in the deliverable. Rework is expensive -- you're fixing a finished document instead of correcting an input. The user sees a polished deck with numbers that don't add up. Trust is damaged.

**The fix**: Validate before output (Section 6). Run the checks. Fix issues at the intake level, not the deliverable level.

### Anti-Pattern 8: Binary Red Flags

**What it looks like**: "Solo founder detected. CANNOT PROCEED." Or: "No revenue. INTAKE FAILED."

**Why it happens**: The designer treats red flags as pass/fail gates instead of discussion triggers.

**The damage**: Adversarial dynamic. The user feels judged rather than supported. Real red flags go unaddressed because the user avoids triggering them (e.g., lies about team size). The process loses its value as a diagnostic tool.

**The fix**: Red flags are conversation starters, not blockers (Section 6, Check 3). "Solo founder" doesn't mean stop -- it means: "How will you frame this for investors? Options include: highlighting advisory board strength, demonstrating a clear first-hire plan, showing that the founder has previously built teams at scale."

### Anti-Pattern 9: No "Why It Matters"

**What it looks like**: Questions presented as a bare list with no context for why the answer is needed.

**Why it happens**: The designer knows why each question matters but doesn't externalize that knowledge.

**The damage**: The user doesn't understand what level of detail is needed. They give surface-level answers. "Cap table: 3 founders, equal split" when what's needed is share classes, vesting schedules, prior instruments, and ESOP status. The user isn't being lazy -- they just don't know what's expected.

**The fix**: Every question gets "Why It Matters" (Section 4). "Cap table detail is needed because investors model dilution, lawyers draft instruments based on share classes, and the financial model needs post-round ownership to calculate returns" -- now the user knows to be thorough.

### Anti-Pattern 10: Static Intake

**What it looks like**: The exact same intake for a pre-revenue startup and a profitable growth company. The same questionnaire for a simple NDA and a complex multi-jurisdictional services agreement.

**Why it happens**: The designer builds one intake and uses it everywhere. Economies of scale thinking applied where it doesn't belong.

**The damage**: Light projects are over-interrogated (killing engagement). Complex projects are under-interrogated (missing critical detail). Neither gets an appropriately calibrated experience.

**The fix**: Weight classes (Section 11). Light, standard, heavy, ultra-light, and ultra-heavy intakes with clear calibration criteria. Plus conditional logic within each weight class to adapt further.

### Anti-Pattern 11: Single-Stream Multi-Party

**What it looks like**: Running a JV, partnership, or negotiation intake as one questionnaire sent to "the parties" together, or asking Party A to answer questions about Party B's position.

**Why it happens**: The intake designer assumes all information is shared, or does not recognize that each party has confidential interests.

**The damage**: Confidential positions are exposed. One party dominates the conversation. The other party's real positions are never captured. Alternatively, both parties give diplomatic non-answers in each other's presence. The resulting deliverable reflects one party's view, not an aligned position.

**The fix**: Parallel intake streams with explicit confidentiality barriers (see Section 13). Each party's intake is conducted separately. Cross-party alignment is analyzed by the operator, not by asking one party to describe the other's position.

### Anti-Pattern 12: Treating All Information as User-Provided

**What it looks like**: An intake that asks the user for information that the agent could research independently. "What is the investor's thesis?" when their website states it clearly. "How many portfolio companies do they have?" when Crunchbase has the answer.

**Why it happens**: The designer treats the intake as a questionnaire where the user is the sole information source. The designer doesn't consider agent research capabilities.

**The damage**: The user's time is wasted answering questions they don't know the answers to (or would have to research themselves). The user loses trust: "Why are you asking ME what their portfolio looks like?" The intake feels like the agent is offloading research to the user.

**The fix**: For every information requirement, ask: "Can the agent obtain this without asking the user?" If yes, make it a research task, not a question. Only ask the user for information that ONLY the user has: strategic intent, internal context, tribal knowledge, preferences, and judgment calls. See Section 12.

### Anti-Pattern 13: Ignoring Time Constraints

**What it looks like**: Running the standard multi-round, phased intake process when the user needs output in 2 hours.

**Why it happens**: The designer builds one intake process and applies it regardless of time pressure.

**The damage**: The intake process takes longer than the time available. The user either abandons ("I'll just wing it") or gets a partial output too late to be useful.

**The fix**: Design time-aware intake variants. For every intake, define a "rapid mode" that: asks all questions in a single batch, runs research in parallel, compresses validation into output generation, and defines a minimum viable output. See Section 5.

### Anti-Pattern 14: The Frozen Recurring Intake

**What it looks like**: A monthly intake that asks the same 20 questions in Month 12 that it asked in Month 1.

**Why it happens**: The designer treats recurring intakes as static. No one tracks which questions could now be answered by systems.

**The damage**: Monthly overhead never decreases. The founder dreads the intake process. Data quality degrades as fatigue sets in. Information that COULD be auto-populated is still manually entered, introducing error risk.

**The fix**: Track automation maturity per question (see Section 15). After each run, evaluate: "Which questions could be answered by a system next time?" Promote questions to data points. Target: 50% reduction in human questions within 6 months.

### Anti-Pattern 15: The Compliance Underweight

**What it looks like**: A compliance intake treated as "Light" because it produces only one deliverable. 20 questions, 2 phases, no regulatory validation.

**Why it happens**: The designer uses the calibration table, sees "1 deliverable," and selects "Light." The calibration table's first factor dominates even though every other factor points to Heavy.

**The damage**: Critical fields are missed. Terminology is imprecise. Documents are marked "exists" without validation. The application is submitted and rejected -- or worse, accepted with wrong parameters that lock the project into an incorrect capacity or connection type for years.

**The fix**: Apply the Weight Class Override (Section 11). If the deliverable has binary completeness, high error cost, terminology precision requirements, or an external authority with no obligation to help fix errors, override the weight class upward.

---

## 10. Worked Example -- Building an Intake for a Website Redesign

This section applies the 8-step methodology to a domain outside the existing ecosystem. It demonstrates that the principles are genuinely domain-agnostic.

### Step 1: Define Outputs

| Deliverable | Section | Information Required |
|---|---|---|
| Website Design Spec | Brand compliance | Current brand guidelines, colors, fonts, tone |
| Website Design Spec | Site architecture | Pages, hierarchy, navigation structure |
| Website Design Spec | Functional requirements | Forms, integrations, dynamic content, CMS needs |
| Website Design Spec | Visual direction | Style preferences, reference sites, photography |
| Content Migration Plan | Content inventory | Existing pages, what migrates, what's retired |
| Content Migration Plan | New content needed | Gaps, new pages, rewrites required |
| Content Migration Plan | SEO preservation | High-traffic pages, redirects, keyword targets |
| SEO Strategy | Current performance | Analytics baseline, rankings, backlinks |
| SEO Strategy | Target keywords | Priority terms, search intent, competitive gaps |
| SEO Strategy | Technical SEO | Site speed, mobile, crawlability, structured data |
| Launch Checklist | Infrastructure | Hosting, domain, SSL, CDN, staging environment |
| Launch Checklist | Testing | Browser testing, QA, accessibility, performance |
| Launch Checklist | Go-live | Redirect plan, DNS, monitoring, rollback plan |

### Step 2: Inventory Dimensions

| Domain | Information Items | Feeds |
|---|---|---|
| Brand & Identity | Guidelines, tone, visual identity, logo usage | Design Spec |
| Current State | Existing site, analytics, content, SEO baseline | Migration Plan, SEO Strategy |
| Technical | CMS, hosting, integrations, performance requirements | Design Spec, Launch Checklist |
| Content | Pages, copy, media assets, blog, content calendar | Migration Plan, Design Spec |
| Audience | Users, personas, journey maps, conversion goals | Design Spec, SEO Strategy |
| Timeline & Budget | Launch date, budget, phases, team availability | Launch Checklist, all |
| Stakeholders | Decision makers, approval process, brand gatekeepers | All |

### Steps 3-8: Summary

- **Questions**: ~31 core, ~4 conditional. Weight class: Standard-Light.
- **Phase 0**: Brand guidelines, sitemap, GA export, Search Console, prior proposals, competitor list, content calendar, SEO audit, hosting docs, post-mortem.
- **5 phases**: Document Ingestion, Business Goals & Audience, Current State & Content, Technical & Functional, Timeline/Budget/Stakeholders.
- **Conditionals**: CMS migration (content types), e-commerce (products/SKUs), multilingual (languages/hreflang), no analytics (alternative measures).
- **Consistency checks**: Budget vs. scope, timeline vs. scope, SEO expectations vs. baseline.
- **Red flags**: No analytics (M), no brand guidelines (M), scope exceeds budget >2x (H), launch <4 weeks (H), no decision-maker (H), no content writer (M).

---

## 11. Scaling Intakes -- Weight Classes and Calibration

Not every project needs a 75-question intake. Calibrate to the complexity.

### Five Weight Classes

**Ultra-Light (3-5 human questions, 1-2 rounds)**

Use when: mature recurring intake where most data is auto-populated from systems. Only narrative/judgment questions remain for the user.

Characteristics: system provides most data, human provides only narrative, strategic judgment, and exception explanations. Validation is fully automated. See Section 15.

**Light (15-25 core questions, 2-3 phases, 5-8 rounds)**

Use when: simple scope, single deliverable, low stakes, straightforward domain.

Characteristics:
- Phase 0 may be a single question: "Do you have a prior version or template?"
- 2-3 phases (Identity + Scope + Terms)
- Minimal conditional logic (0-2 branches)
- Validation: consistency check only. Skip benchmarks and red flag scan.
- Total intake time: 15-25 minutes

Example: NDA drafting (24 questions, 2 batches).

**Standard (40-65 core questions, 4-6 phases, 12-18 rounds)**

Use when: moderate complexity, 2-4 deliverables, moderate stakes, multiple domains involved.

Characteristics:
- Full Phase 0 with document checklist
- 4-6 phases covering 3-5 domains
- Moderate conditional logic (3-6 branches)
- Full validation: all five checks
- Total intake time: 40-90 minutes (may split across sessions)

Example: Service agreement drafting (82 questions, 6 batches). Website redesign (31 questions, 5 phases).

**Heavy (65-100+ core questions, 6-8 phases, 18-25 rounds)**

Use when: high complexity, 5+ deliverables, high stakes, multiple domains, extensive conditional logic, benchmark data available.

Characteristics:
- Full Phase 0 with extensive document checklist (40+ items)
- 6-8 phases covering all relevant domains
- Extensive conditional logic (7+ branches, domain-specific paths)
- Full validation with domain-specific benchmarks and red flag library
- Total intake time: 90-180 minutes (always split across sessions)

Example: Seed fundraising (75 questions, 7 phases, 9 deliverables). M&A data room preparation.

**Ultra-Heavy (100-200+ core questions, 8+ phases or workstream tracks, 30+ rounds)**

Use when: extreme complexity, 5+ parallel workstreams, high stakes, multiple jurisdictions, extensive regulatory interaction, project timelines measured in months/years, living deliverable required.

Characteristics:
- Phase 0 with extensive document checklist (50+ items), re-run at each stage
- 8+ workstream-specific tracks, each with internal phases
- Extensive conditional logic (15+ branches, cross-domain triggers)
- Progressive validation with stage-specific benchmarks
- Living deliverable with version history
- Total intake time: distributed across multiple sessions over months
- Cannot be completed in a single sitting by design

Example: Infrastructure site development (6 workstreams, 150+ questions, 12-18 month lifecycle).

### Calibration Table

| Factor | Ultra-Light | Light | Standard | Heavy | Ultra-Heavy |
|---|---|---|---|---|---|
| Deliverables | 1 (template) | 1 | 2-4 | 5+ | Living doc + derivatives |
| Domains touched | 1-2 | 1-2 | 3-5 | 6+ | 8+ |
| Conditional paths | 0 | 0-2 | 3-6 | 7+ | 15+ |
| Stakeholders providing input | 1 | 1 | 1-2 | 2+ | 3+ |
| Benchmark data available | N/A | No | Some | Yes | Yes, requires refresh |
| Regulatory/legal complexity | None | Low | Medium | High | Multi-body |
| Document ingestion scope | Prior run | 1-3 docs | 5-10 docs | 10+ docs | 20+ docs, progressive |
| **Time available** | **Ongoing cadence** | **< 2 hours** | **2h - 2 weeks** | **> 2 weeks** | **Months** |
| **Research proportion** | **0%** | **0-20%** | **20-50%** | **Variable** | **Variable** |
| **Deliverable lifespan** | **Single use** | **Single use** | **Weeks-months** | **Months-years** | **Years (living)** |
| **Stakes / error cost** | **Low** | **Low** | **Medium** | **High** | **Very high** |
| **Intake instances** | **1** | **1** | **1-2** | **1-2** | **2+ (multi-instance)** |
| Typical total questions | 3-5 | 15-25 | 40-65 | 65-100+ | 100-200+ |
| Typical interaction rounds | 1 | 5-8 | 12-18 | 18-25 | 30+ across sessions |

**Rule**: When in doubt, go one weight class heavier. An intake that's slightly more thorough than needed is better than one that misses critical information.

### Weight Class Override for High-Stakes Single Deliverables

The calibration table can mislead when deliverable count is low but STAKES are high. Override factors:

| Override Factor | Condition | Effect |
|---|---|---|
| Binary completeness | Deliverable is accepted or rejected (no partial credit) | +1 weight class |
| Error cost | Errors cause delays measured in months/years | +1 weight class |
| Terminology precision | Wrong term = wrong outcome | +1 weight class |
| External authority | Receiving authority has no obligation to help fix errors | +1 weight class |

If any two override factors are present, the intake is at minimum Standard. If three or more, it is Heavy regardless of deliverable count.

---

## 12. Research-Augmented Intakes -- When Information Comes From Outside

Some intakes require the agent to GATHER information from external sources, not just ASK the user for it. Meeting preparation, competitive analysis, due diligence, market research, and counterparty assessment all involve significant external data gathering alongside user questions.

### The Research Task Architecture

When an intake involves external research, add a parallel track alongside the question architecture:

**Research Task Table:**

| R# | Source | Data Points to Extract | Feeds | Priority | Est. Time |
|---|---|---|---|---|---|
| R1 | [Source name/URL] | [What to extract] | [Deliverable sections] | High/Med/Low | [Minutes] |

Research tasks have six fields: R# (sequential ID with R prefix), Source, Data Points to Extract, Feeds (same as question Feeds), Priority (for time-constrained triage), and Est. Time.

### Phase 0B: External Research Protocol

When the intake involves external research, split Phase 0:

**Phase 0A: Internal Document Ingestion** (existing Phase 0 protocol)
**Phase 0B: External Research**

1. Identify all external sources needed (from the Research Task Table)
2. Prioritize by: (a) blocks other work if missing, (b) highest-value for deliverables, (c) fastest to obtain
3. Execute research tasks, capturing structured outputs
4. For each task, note: data captured / source quality / gaps remaining / confidence level
5. Flag any research that contradicts user-provided information

Key difference: External research populates deliverable sections directly. The Research Task Table maps outputs to deliverable sections, not to intake questions.

### Source-Aware Traceability

The traceability rule becomes: "Every deliverable section must have at least one feeding question OR research task OR data point. If it has none, the section will be empty."

### Time Budget Template (for time-constrained research intakes)

| Activity | Time | Notes |
|---|---|---|
| Anchor questions to user | 2 min | Send immediately; don't wait for full context |
| Phase 0A: CRM pull | 5-10 min | Parallel with user response |
| Phase 0B: External research | 15-20 min | Parallel with user response |
| Synthesis + draft | 20-30 min | After user responds + research complete |
| User review | 10-15 min | Send draft; incorporate feedback |
| Buffer | 10-15 min | Unexpected gaps, additional research |
| **Total** | **~60-90 min** | |

---

## 13. Multi-Party Intake Architecture

Some intakes involve multiple parties with different interests, different information, and potentially confidential positions. JV structuring, partnership negotiations, multi-stakeholder alignment, and adversarial/sales qualification all require parallel information streams.

### When to Use Multi-Party Architecture

Use when ANY of these conditions apply:
- Two or more parties each have information the other does not
- Parties have confidential positions that must not be disclosed
- The deliverable requires alignment between parties, not just information from one
- The intake subject has competing interests (sales qualification, adversarial negotiation)

### The Three-Layer Model

**Layer 1: Parallel Intake Streams**
Each party gets their own intake stream. The same domain structure applies, but questions are tagged with `Asked Of` to route them correctly. Some questions are asked of each party separately; some are joint.

**Layer 2: Information Barriers**
Tag every answer with an access level:
- **Shared**: Both parties see this information
- **Party-A-Confidential**: Only Party A and the operator see this
- **Party-B-Confidential**: Only Party B and the operator see this
- **Operator-Only**: Only the intake operator sees this (e.g., analysis notes)

**Layer 3: Alignment Analysis**
After collecting from both streams, analyze alignment. This is a fundamentally different step from consistency checking -- you are looking for ALIGNMENT (positions close enough to negotiate), not CONSISTENCY (answers that match).

### Alignment Gap Classification

| Classification | Meaning | Action |
|---|---|---|
| **Aligned** | Positions match or are within normal negotiation range | Proceed to deliverable |
| **Negotiable** | Gap exists but is bridgeable through standard mechanisms | Note in deliverable; suggest mechanisms |
| **Structural** | Significant gap requiring bespoke structural solutions | Flag; may need dedicated resolution session |
| **Conflict** | Incompatible positions on operational matters | Must resolve before deliverable; one party concedes |
| **Deal-Breaker** | Fundamental misalignment that may prevent proceeding | Surface immediately; do not produce deliverables until addressed |

### Operator Role

The operator's role depends on who engaged them:
- **Advisor to one party**: Design the intake to serve that party's interests. May not have direct access to the other party.
- **Neutral facilitator**: Equal duty to both parties. Parallel streams with symmetric treatment.
- **Hybrid**: Gathers both parties' information but frames deliverables for one party's decision-making.

### Confidentiality Rules for Conditionals

When cross-party conditionals are needed (triggered by comparing two parties' answers):
- NEVER reference the other party's specific answer in a question
- Use neutral framing: "What range of ownership splits would you consider acceptable?" NOT "The other party wants 60/40; can you accept that?"
- Frame follow-ups around flexibility and mechanisms, not specific positions

---

## 14. Multi-Instance Intakes -- Evaluation and Comparison

Some intakes run the same question template against multiple subjects to produce a comparative output. Vendor evaluation, candidate assessment, technology selection, and partner comparison all follow this pattern.

### The Three-Stage Model

**Stage 1: Criteria Definition** *(internal, run once)*
Define requirements, establish evaluation criteria, agree on weights with stakeholders. This is a standard single-respondent intake.

**Stage 2: Subject Evaluation** *(repeated per subject)*
Run the same question template against each subject. Each instance produces a profile. Use consistent questions, order, and response time across all subjects.

**Stage 3: Synthesis** *(no new questions -- analysis only)*
Build the comparative evaluation matrix. Score, rank, normalize, and draft recommendation.

### Question Population Design

Multi-instance intakes have distinct question populations:

| Prefix | Population | Asked To | Example |
|---|---|---|---|
| **R** | Requirements | Internal stakeholders | "What is the minimum acceptable cycle life?" |
| **V** | Subject evaluation | Each subject identically | "What cell chemistry do you propose?" |
| **D** | Diligence/reference | Third parties about each subject | "What was contracted vs. actual availability?" |
| **F** | Facilitation | Internal synthesis | "Based on scoring, which subject best fits?" |

### Instance-Parameterized Feeds

The Feeds field uses a placeholder: `{Subject} Profile: Technical Section`. When run for BYD, it maps to "BYD Profile: Technical Section." Same question, different output cell.

### Cross-Instance Normalization

Before scoring, verify that answers are comparable:
- Same units (EUR/MWh at cell level vs. rack level?)
- Same scope (warranty covers cells only vs. full system?)
- Same test conditions (cycle life at 80% DoD vs. 90%?)
- Same delivery terms (FOB vs. DDP vs. installed?)

### Weighted Scoring

Evaluation requires quantitative ranking, not just pass/fail:
1. Define criteria and weights BEFORE reviewing any subject data (prevents reverse-engineering weights to justify preference)
2. Score each subject on each criterion (1-5 scale recommended)
3. Calculate weighted totals
4. Run sensitivity analysis (do results change if weight priorities shift?)

### Question Count Guidance

Count UNIQUE questions for weight class calibration. Count TOTAL INSTANCES for time estimation. A 25-question intake run against 4 vendors is "Light" in design complexity but requires 100 question-instances of processing time. Formula: Stage 1 time + (Stage 2 time x N subjects) + synthesis time.

---

## 15. Progressive and Recurring Intakes

Not all intakes are single events. Some processes span months with information emerging gradually. Others run on a regular cadence (monthly, quarterly). Both require extensions to the standard model.

### Progressive Intakes (Lifecycle-Spanning)

Use when the project timeline is measured in months, information depends on external parties whose responses arrive over time, and the deliverable evolves in structure as the project advances.

**Stage Model**: Define lifecycle stages. Each stage is a development milestone, not a phase of questions.

| Stage | Entry Criterion | Example |
|---|---|---|
| Identified | Initial parameters known | Cadastral reference available |
| Under Option | Key rights secured | LOI or option agreement signed |
| Under Development | Active workstreams progressing | Grid study underway, permits filed |
| Permitted | Key approvals received | Omgevingsvergunning granted |
| Construction-Ready | All prerequisites met | Grid, EPC, financing confirmed |

**Stage-Specific Question Sets**: Each stage unlocks new questions and re-validates prior answers. Phase 0 is re-run at every stage transition.

**Living Deliverable Support**: Progressive intakes produce living deliverables:
- Version numbering (v0.1, v0.2)
- Placeholder sections marked `[Pending: dependent on X]`
- Change log per version
- Structural evolution as workstreams are added or dropped

### Recurring Intakes (Cadenced)

Use when the same information is gathered on a regular schedule (monthly investor updates, quarterly board reports, weekly pipeline reviews).

**Prior-Run Ingestion**: For recurring intakes, Phase 0 loads the prior run's OUTPUT as the primary reference document, plus any open action items from the prior run, and current system data with computed deltas.

**Progressive Automation**: Recurring intakes should get more efficient over time:

| Maturity Level | Description | Human Effort |
|---|---|---|
| Level 0: Manual | No system source; fully human-answered | Full question |
| Level 1: Assisted | System provides draft; human confirms | Confirm/correct |
| Level 2: Trusted | System provides data; human reviews exceptions only | Review flagged items |
| Level 3: Automated | System provides data; validated automatically | Zero (unless anomaly) |

Target: most items at Level 0-1 in Month 1, financial/CRM data at Level 2 by Month 3, only narrative/judgment items remaining at Level 0 by Month 6.

**Delta-Based Conditionals**: In addition to answer-based conditionals, recurring intakes use delta-based conditionals triggered by comparing current data to prior periods (see Template 16).

**Weight Class Evolution**: A recurring intake starts Heavy and should migrate toward lighter classes as automation matures. If the weight class is NOT decreasing over time, the intake designer has failed to implement progressive automation.

### Data Point Architecture (System-Sourced Information)

When data lives in a system (CRM, accounting, project management), design a Data Point instead of a Question.

| Field | Purpose |
|---|---|
| **D#** | Unique ID with D prefix (D1.3) |
| **Data Point** | What specific value is needed |
| **Source System** | Where the data lives (e.g., "HubSpot > Deals > Amount") |
| **Retrieval Method** | API call, export, manual lookup, calculated |
| **Validation Rule** | Range check, delta check vs. prior period |
| **Feeds** | Same as questions -- deliverable sections |

When to use Data Point vs. Question: if the answer exists in a system of record, use Data Point. If it requires human judgment or narrative, use Question. If partially in a system but needs context, use Hybrid (auto-populate from system, present to human for confirmation/enrichment).

---

## 16. Compliance-Driven Intakes

Some intakes produce deliverables whose structure, terminology, and acceptance criteria are defined by an external authority (regulator, grant body, counterparty). These carry additional constraints.

### Externally-Defined Outputs

When the authority defines the form:
- The Output Inventory Table is constrained by the form fields (not designed by you)
- Step 1 becomes "map the authority's form fields to information items" instead of "design the output structure"
- The designer's role shifts from architect to translator: converting form requirements into answerable questions

### Regulated Terminology

In compliance domains, specific terms carry legal weight. Using the wrong term changes the outcome.

For each high-confusion term in the intake, add a **Terminology Note**:

> **Terminology Note**: "Aansluitwaarde" (connection value) is the contracted maximum capacity. "Transportvermogen" (transport capacity) is the grid's available capacity. These are different values -- using one in place of the other will produce an incorrect application.

### Document Validation Beyond "Exists"

For compliance documents, the standard checklist (exists / in progress / doesn't exist) is insufficient. Validate:
- **Recency**: Is the document within the validity window? (e.g., kadaster extract < 3 months old)
- **Issuer**: Was it issued by the correct authority? (e.g., het Kadaster, not a third-party search)
- **Content match**: Does the document confirm the required condition? (e.g., cadastral extract confirms ownership of the correct parcel)
- **Format**: Is it in the required format? (PDF, certified copy, original)

### Binary Completeness

Some deliverables do not support partial output. A regulatory application is either complete or rejected. For these:
- ALL questions mapped to the deliverable are effectively Primary
- Completeness Assessment has only two statuses: Ready or Blocked
- The Pre-Flight Checklist must include a submission-readiness gate
- Mark in the Intake Design Canvas as `Deliverable Completeness: Binary`

Principle 7 (Partial-Output Capable) still applies to the intake PROCESS (complete phases incrementally), but NOT to the deliverable (cannot submit an incomplete form).

### Hard Forks

When a conditional answer changes the deliverable or receiving authority entirely (not just adds questions):
1. Detect the fork as early as possible (Phase 1-2)
2. Communicate clearly: "Based on your capacity of 15 MVA, this is a TenneT application, not a DSO application."
3. Rebuild remaining intake phases against the correct deliverable
4. If the fork is uncertain, capture information for BOTH paths

### Form Order vs. Cognitive Order

When the deliverable is an externally-defined form, the form's section order and the optimal intake question order may differ. The intake should follow cognitive order (context before detail, broad before narrow). The mapping table translates between intake order and form order during output generation.

---

## 17. Lessons Learned -- What the Ecosystem Taught Us

These lessons were extracted from building and iterating on 20+ skills with intake processes, then stress-tested against 10 DE-relevant use cases.

### Lesson 1: The 2x Multiplier

Your first-draft question count is always too low. The pattern is consistent: designers think 30 questions covers the domain, then discover during output generation that they need 60-75.

Why: designers think in topics ("team," "market," "financials") when they should think in data points ("each founder's %, time commitment, prior exits, relevant experience, sector expertise"). One topic is 3-8 data points. 10 topics = 30-80 questions, not 10.

Rule of thumb: first-draft question count x 2.0-2.5 = actual requirement.

### Lesson 2: "Why It Matters" Is Not Optional

Questions without justification get shallow answers. This was observed repeatedly: the same question with and without "Why It Matters" produces dramatically different answer quality.

Bonus: "Why It Matters" also disciplines the designer. If you cannot explain why a question matters, it probably shouldn't be there.

### Lesson 3: Conditional Logic Is 20% of Questions but 50% of Value

The difference between a generic intake and one that feels tailored is conditional branching. When a Swiss AG gets follow-up questions about authorized capital and stamp duty planning -- questions that a Dutch BV never sees -- the user thinks "this process understands my situation."

### Lesson 4: Phase 0 Is the Highest-ROI Phase

Companies that provide existing documents skip 30-40% of intake questions. The single most impactful improvement to any existing intake: add a Phase 0 document ingestion step.

### Lesson 5: Validation Catches What Humans Miss

Cross-referencing answers reveals contradictions the user didn't notice. Benchmark comparison is equally powerful: "Your CAPEX estimate is EUR 200K/MW, but the industry range is EUR 330-700K/MW."

### Lesson 6: Partial Output Beats No Output

Produce what you can with what you have. Users get immediate value. Momentum continues. Remaining questions feel purposeful.

### Lesson 7: Red Flags Are Conversation Starters

Red flags are discussion triggers with severity ratings, not binary gates. "Solo founder" prompts framing strategies, not rejection.

### Lesson 8: Group by Domain, Map to Deliverable

Group questions by domain, then use the mapping table to route answers to all deliverables that need them. This pattern governs all intakes in the ecosystem.

### Lesson 9: 2-4 Questions Per Round Is the Empirical Sweet Spot

The default is 3. Use 2 for complex questions. Use 4 for factual questions. Never 5+.

### Lesson 10: The Pre-Flight Checklist Prevents Rework

Run validation before output generation, not after. Fixing inputs is cheaper than fixing deliverables.

### Lesson 11: Not All Information Comes From Questions

60-70% of meeting prep data, investor update metrics, and market entry research comes from external sources and systems, not user questions. Design intakes with Research Tasks and Data Points alongside Questions. The user's time is the scarcest resource -- spend it only on information that requires their unique knowledge.

### Lesson 12: Recurring Intakes Must Get Faster

A monthly intake that takes the same effort in Month 12 as Month 1 is a design failure. Track automation maturity. Promote questions to data points. Target: 50% reduction in human questions within 6 months.

### Lesson 13: Multi-Party Intakes Need Information Barriers

When two parties have confidential positions, running a single intake stream is dangerous. Parallel streams with alignment analysis produce better outcomes and protect trust.

### Lesson 14: Compliance Intakes Are High-Stakes Despite Low Deliverable Count

A single regulatory filing can be heavier than a 9-deliverable fundraise if the error cost is measured in years and the completeness requirement is binary. Use the weight class override.

### Lesson 15: The Guidebook Covers a Spectrum, Not a Single Pattern

The original guidebook was designed for single-respondent, single-pass, document-output intakes. Real-world use cases span research-augmented, multi-party, multi-instance, progressive, recurring, and compliance-driven patterns. The core principles (8 principles, 4-field architecture, domain grouping, validation) are universal. The execution patterns vary. Design for your pattern.

---

## 18. Cross-Reference Index

Living index of all intake implementations in this ecosystem. Update when new intakes are added.

### Implementations

| Implementation | File Path | Qs | Phases | Deliverables | Weight |
|---|---|---|---|---|---|
| Seed fundraising | `seed-fundraising/references/intake-guide.md` | ~75 | 7 phases | 9 | Heavy |
| Service agreement | `legal-counsel/.../questionnaire-service-agreement.md` | 82 | 12 parts / 6 batches | 1 | Standard |
| NDA / NCNDA | `legal-counsel/.../questionnaire-nda.md` | 24 | 5 parts / 2 batches | 1 | Light |
| LOI / MOU | `legal-counsel/.../questionnaire-loi.md` | varies | varies | 1 | Light |
| Term Sheet | `legal-counsel/.../questionnaire-term-sheet.md` | varies | varies | 1 | Light |
| MSA | `legal-counsel/.../questionnaire-msa.md` | varies | varies | 1 | Standard |
| SPA | `legal-counsel/.../questionnaire-spa.md` | varies | varies | 1 | Heavy |
| SHA | `legal-counsel/.../questionnaire-sha.md` | varies | varies | 1 | Standard |

### Meta-Frameworks

| Framework | File Path | Purpose |
|---|---|---|
| Contract intake methodology | `legal-counsel/.../intake-framework.md` | 6-batch structure for all contract types |
| Pre-signing quality gate | `legal-counsel/.../pre-signing-checklist.md` | Post-output validation checklist for contracts |
| Seed fundraising SKILL.md | `seed-fundraising/SKILL.md` | Shows how intake embeds in a skill workflow |
| Ops playbook | `_shared/ops-playbook.md` | Shows cross-skill orchestration patterns |

### This Guidebook

`_shared/intake-design-guidebook.md` -- the document you are reading. The methodology that governs all implementations above. v2: expanded with 5 specialized intake patterns (research-augmented, multi-party, multi-instance, progressive/recurring, compliance-driven), 15 anti-patterns, 7 validation checks, 21 templates, 5 weight classes, and 15 lessons learned.
