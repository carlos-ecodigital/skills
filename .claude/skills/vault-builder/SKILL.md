---
tier: 1

name: vault-builder
description: >-
  Builds a structured LLM wiki vault (Karpathy pattern) for any domain — legal,
  sales, finance, HR, product, compliance. Conducts a guided intake to discover
  what data should be stored, designs the full schema and taxonomy, then executes:
  creates the CLAUDE.md constitution, directory structure, MASTER-INDEX, page
  templates, and seed content. Use when the user wants to build a new knowledge
  vault from scratch, migrate documents into a structured AI-queryable wiki, or
  set up a new domain-specific assistant context. The skill is self-directing:
  it runs intake → vault brief (user-approved) → build → first ingestion in
  sequence without requiring repeated user instruction.
---

# Vault Builder — Karpathy LLM Wiki Pattern (v2)

## Why This Pattern (Read Before Building)

Tell the user this once, at the start — it anchors everything that follows:

> "Standard RAG retrieves document chunks that may silently contradict each other.
> This vault surfaces contradictions explicitly, forces synthesis into structured
> pages, and makes every claim traceable to a source. The difference is: RAG
> fails silently. This vault fails loudly — which means you can fix it."

The three layers:
```
vault/
├── CLAUDE.md              ← Constitution: schema, rules, workflows, taxonomy
├── raw/                   ← Immutable source documents (AI reads, never modifies)
│   ├── [domain-a]/
│   ├── [domain-b]/
│   └── HOW-TO-POPULATE.md
├── wiki/                  ← AI-synthesized knowledge (AI writes and maintains)
│   ├── index/
│   │   ├── MASTER-INDEX.md
│   │   └── ACTIVITY-LOG.md
│   ├── [page-type-1]/
│   ├── [page-type-2]/
│   └── contradictions/
├── QUICK-START.md         ← Magic words cheat-sheet for the user
├── MEMORY.md              ← Cross-session memory pointer
└── logs/
    └── ingestion-log.md
```

---

## Execution Rules (Non-Negotiable)

1. **Phase 1 is a hard gate.** No files are created until the user approves the Vault Brief at the end of Phase 2.
2. **The CLAUDE.md is the highest-value output.** Thin CLAUDE.md = vault degrades over time. Never rush it.
3. **[VERIFY] tags are mandatory** for any fact not provided by the user in intake. Never hallucinate into a new vault.
4. **Domain adapters are applied in Phase 2** based on the domain answer. They are not optional extras.
5. **After BUILD, always offer first ingestion.** An empty vault is a failed vault.
6. **If the user says "just start" or skips questions**, apply the defaults table from Phase 1.4 and mark every assumption `[ASSUMED — update CLAUDE.md if wrong]`.

---

## PHASE 1 — DISCOVERY

**Goal:** Understand domain, data, location, and framing rules. Output: confirmed answers feeding Phase 2.

### 1.1 — Batch A: Identity + Location

Use AskUserQuestion for the first batch. Structure it as follows:

```
Questions batch A — vault identity:

Q1 (header: "Domain"): What is this vault for?
  Options: Sales knowledge base | Finance & modelling | Legal research |
           HR & people ops | Product & GTM | Custom (describe)

Q2 (header: "Primary user"): Who is the main user of this vault?
  Options: Just me | My team | An AI agent | Both me and an agent

Q3 (header: "Vault location"): Where should the vault be created?
  [Free text — user provides an absolute path or says "ask me"]
  If user doesn't specify: ask explicitly before proceeding.
  Never assume a default path.
```

### 1.2 — Batch B: Data Inventory

```
Questions batch B — your data:

Q4 (header: "Documents"): What kinds of raw sources will go in?
  Options (multi-select): Contracts/agreements | Emails/comms | CRM exports |
  Financial statements/models | Court decisions/laws | Research reports |
  Meeting transcripts | Product specs | Other

Q5 (header: "Volume"): Approximate number of source documents now?
  Options: <20 (starting fresh) | 20–100 | 100–500 | 500+ (migration)

Q6 (header: "Key entities"): What are the most important recurring entities?
  Examples: clients, laws, products, competitors, deals, people, regions
  [Free text — ask for 3–8 examples]
```

### 1.3 — Batch C: Framing Rules

This is the most powerful and most underexplained feature. Introduce it before asking:

> "Framing rules are the single most valuable thing in a vault. They prevent
> the AI from using the wrong word, citing the wrong number, or framing a
> concept in a way that could cause real damage. Examples from other vaults:
> 'Never call our facilities datacenters — always energie-installaties';
> 'Never cite a revenue figure without naming the model version and date';
> 'Never say a feature is available without a source dated < 90 days ago'.
> What are yours?"

```
Questions batch C — framing and constraints:

Q7 (header: "Framing rules"): Are there any terms, framings, or claims
  the AI should NEVER use in this vault?
  [Free text — ask for at least 3, give the examples above as prompts]

Q8 (header: "Language"): What language should wiki pages be in?
  Options: English | Dutch | German | French | Mixed (specify)

Q9 (header: "Key question"): What is the single most important question
  this vault must be able to answer reliably?
  [Free text — this becomes the vault's north star]
```

### 1.4 — Default Values (for "just start" users)

If the user skips questions, apply these defaults and mark each `[ASSUMED]`:

| Question | Default |
|----------|---------|
| Domain | General business knowledge base |
| Primary user | Just me |
| Vault location | `~/Documents/[domain]-vault/` — **always confirm before creating** |
| Document types | Mixed documents |
| Volume | Starting fresh |
| Key entities | To be discovered during first ingestion |
| Framing rules | "Always cite the source document. Never fabricate statistics." |
| Language | English |
| Key question | [Left blank — user must provide this before Phase 3] |

---

## PHASE 2 — DESIGN + VAULT BRIEF

**Goal:** Produce the full schema design, then present the Vault Brief for user approval. Nothing is built until the user says "yes."

### 2.1 — Domain Adapter Selection

Based on Q1 answer, automatically apply the matching adapter. **Do not ask the user to choose — apply it and confirm in the Vault Brief.**

| Domain answer | Apply adapter | Primary page types added |
|---------------|--------------|--------------------------|
| Sales | Sales adapter (§ 6.1) | accounts/, competitors/, objections/, wins/, losses/ |
| Finance | Finance adapter (§ 6.2) | models/, transactions/, covenants/, scenarios/ |
| Legal | Legal adapter (§ 6.3) | case-law/, laws/, regulations/, opinions/ |
| HR / People | HR adapter (§ 6.4) | policies/, roles/, compensation-bands/ |
| Product / GTM | Product adapter (§ 6.5) | features/, personas/, competitors/, roadmap/ |
| Custom | Ask one follow-up: "What are your 3 main categories of knowledge?" |

### 2.2 — Page Type Decision Table

**Standard page types** — include all by default:

| Type | Directory | One line | Include? |
|------|-----------|----------|----------|
| Source/Document | `wiki/sources/` | One page per raw document | Always |
| Entity | `wiki/entities/` | People, orgs, products, clients, courts | Always |
| Concept | `wiki/concepts/` | Defined terms, doctrines, frameworks | Always |
| Topic | `wiki/topics/` | Cross-source operational clusters | Always |
| Playbook | `wiki/playbooks/` | Step-by-step action guides | Always |
| Contradiction | `wiki/contradictions/` | Flagged conflicts between sources | Always |
| Domain-specific | (from adapter) | Per adapter table above | Domain-dependent |

### 2.3 — Domain-Specific Seed Page Defaults

These are the 5 pages to pre-create in Phase 4. Do not ask — use these defaults per domain:

| Domain | Seed page 1 | Seed page 2 | Seed page 3 | Seed page 4 | Seed page 5 |
|--------|-------------|-------------|-------------|-------------|-------------|
| Sales | Top priority account | Top competitor | ICP definition | Core objection library | Win/loss template |
| Finance | Company entity / SPV | Financial model register | Capital structure | Key lender | Core metric definitions |
| Legal | Primary regulatory body | Primary statute | Core legal doctrine | Key jurisdiction | Open questions tracker |
| HR | Org structure overview | Core policies index | Compensation band overview | Key role definitions | Compliance calendar |
| Product | Product vision / ICP | Feature inventory | Top 3 competitors | Pricing structure | Launch playbook |

### 2.4 — Priority Source Queue

Based on Q4 and Q5, produce a tiered ingestion queue. Tier 1 = must exist before vault is useful.

**Tier 1 (ingest first — vault not useful without these):**
- The 3 most critical existing documents the user named in Q4
- Any single source that answers Q9 (the key question)

**Tier 2 (ingest within 30 days):**
- Supporting documents, exports, secondary sources

**Tier 3 (ingest within 90 days):**
- Historical data, nice-to-have context

### 2.5 — Vault Brief (Hard Gate)

Before creating any file, present this for explicit approval:

```
## Vault Brief — [Vault Name]

**Location:** [absolute path]
**Domain:** [domain]
**Primary user:** [answer]
**Language:** [answer]
**North-star question:** [Q9 answer]

**Directory structure:**
[show the full tree with all directories that will be created]

**Page types:**
[list all page types and their directories]

**Domain adapter applied:** [name]

**Framing rules (will be enforced in every AI response):**
1. [Rule 1]
2. [Rule 2]
3. [Rule 3]

**Seed pages (pre-created with known content):**
1. [name] → wiki/[type]/[slug].md
2-5. [...]

**Priority source queue:**
Tier 1 (ingest first): [list]
Tier 2 (within 30 days): [list]
Tier 3 (within 90 days): [list]

**Known limitations for this vault type:**
[1-2 relevant items from § 7]

---
✅ Approve this brief to begin building.
❌ Or tell me what to change.
```

**Do not proceed until the user explicitly approves.**

---

## PHASE 3 — CONSTITUTION

**Goal:** Write the full `CLAUDE.md` at the vault root. This is the vault's governing document. It must be self-sufficient — if someone opens this vault 12 months from now with no memory of this conversation, CLAUDE.md should tell them everything.

Write all 11 sections. Do not use placeholders for sections 1, 5, 9, 10, 11 — write them fully based on the Phase 1 answers.

```markdown
# [Vault Name] — Schema & Constitution
## For [User/Team] — [Domain]

> This file governs all AI behavior in this vault. It defines the architecture,
> ingestion workflows, query protocols, and framing rules.

---

## 1. OPERATIONAL CONTEXT

**User/Team:** [who uses this vault]
**Domain:** [what business or knowledge area it covers]
**Purpose:** [the north-star question from Q9, restated as a mission]
**Active data footprint:** [document types, approximate volume, key entities]

**Critical framing rules — enforced in every AI response:**
1. [Framing rule 1 — verbatim from Q7]
2. [Framing rule 2]
3. [Framing rule 3]
[Add all rules provided. Repeat these in Section 5 and Section 11.]

---

## 2. VAULT ARCHITECTURE

[Full directory tree with inline comments]

---

## 3. PAGE TYPES AND CONVENTIONS

[Full template for every page type — see § Standard Page Templates below.
Adapt field names to the domain. Every template must include:
  - Header metadata
  - Relevance/significance section
  - Open questions with [VERIFY] tags
  - Related pages with [[wikilinks]]]

---

## 4. WORKFLOWS

### 4.1 INGEST — Adding a New Source

When the user says "ingest [file/URL/content]":

1. Read the full source
2. Extract: title, type, date, author/issuer, key claims/holdings/data points
3. Assign DE-relevance: HIGH / MEDIUM / LOW with a one-sentence reason
4. Present a 5-bullet summary to the user for confirmation
5. If confirmed, proceed. If not, adjust based on feedback.
6. Create or update `wiki/sources/[source-slug].md`
7. For each key entity mentioned: create or update `wiki/entities/[entity-slug].md`
8. For each key concept mentioned: create or update `wiki/concepts/[concept-slug].md`
9. Check all new claims against existing wiki pages — flag any numerical or factual discrepancy as a contradiction:
   - Create `wiki/contradictions/[slug].md` using the contradiction template
   - Add a note to both conflicting pages
10. Add entry to `wiki/index/ACTIVITY-LOG.md`
11. Add/update entries in `wiki/index/MASTER-INDEX.md`
12. Report: pages created, pages updated, contradictions flagged, [VERIFY] tags placed

### 4.2 QUERY — Answering a Question

When the user asks any question about the domain:

1. Read `wiki/index/MASTER-INDEX.md` to identify relevant pages
2. Read all relevant pages (sources, entities, concepts, topics, playbooks)
3. Synthesize an answer with [[wikilink]] citations
4. Flag unresolved questions with `[VERIFY: reason]`
5. If the answer is substantial and novel, offer to file it as a new wiki page

### 4.3 LINT — Health Check

When the user says "lint the wiki":

1. Glob all `.md` files in `wiki/`
2. For each file: grep for `\[\[` patterns, confirm each linked page exists in the vault. Report broken links.
3. Check every wiki file against MASTER-INDEX — report any page not listed (orphans)
4. Check every MASTER-INDEX entry — report any page listed but file not found (dead links)
5. Grep for `[VERIFY:` across all pages — list all open verification items
6. Grep for `[ASSUMED` — list all assumed values that need confirmation
7. Check "Last update" dates on source pages — flag any source older than [freshness threshold from § 10]
8. Report by severity: CRITICAL / HIGH / MEDIUM / LOW
9. Offer to fix each issue

### 4.4 DRAFT — Produce a Document

When the user asks for a document draft:

1. Identify document type and governing framework
2. Load relevant wiki/sources/, wiki/concepts/, wiki/playbooks/, wiki/topics/
3. Draft using the correct format for the domain
4. Mark unresolved items with `[REVIEW REQUIRED: reason]`
5. Never draft content that contradicts an existing wiki page without flagging it

---

## 5. CROSS-CUTTING RULES

1. **Source citation:** Always cite the specific wiki page or raw source for factual claims. Never make unsupported assertions.
2. **Framing rules (repeated):** [repeat all rules from § 1 — intentional redundancy survives context compression]
3. **[VERIFY] tags:** Use for any claim requiring specialist confirmation, regulatory deadline, or data point not yet in the vault. Format: `[VERIFY: specific reason]`
4. **[ASSUMED] tags:** Use for any value defaulted during vault setup that the user has not explicitly confirmed.
5. **Currency:** Always note the date of source documents. Flag if relying on a source older than [threshold].
6. **Contradictions:** Never silently resolve a conflict. Always create a contradictions/ page and link to it from both conflicting pages.
7. **Specialist referral:** Always recommend qualified professional consultation for [domain-specific high-risk areas].

---

## 6. DOMAIN MAP

[The confirmed domain map from Phase 1]

| Domain | Subdomains | Priority |
|--------|-----------|----------|
| [A] | [...] | CRITICAL |
| [B] | [...] | HIGH |

---

## 7. PRIORITY SOURCE LIST

### Tier 1 — Foundation (must have before vault is useful)
[Numbered list from Phase 2]

### Tier 2 — Operational (within 30 days)
[Numbered list]

### Tier 3 — Deepening (within 90 days)
[Numbered list]

---

## 8. ESTABLISHED POSITIONS

[Key facts, positions, or rules that are already known and confirmed.
These are the vault's "ground truth" — things that don't need to be
re-derived from sources every time.]

| Position | Basis | Status |
|----------|-------|--------|
| [Claim] | [Source] | CONFIRMED / [VERIFY] |

---

## 9. GLOSSARY

[Domain terms, in alphabetical order]

| Term | Translation/Alias | Definition |
|------|------------------|------------|
| [term] | [alias] | [definition — cite source if possible] |

---

## 10. FRESHNESS POLICY

Different source types go stale at different rates. Re-ingest or flag when:

| Source type | Freshness threshold | Action when stale |
|-------------|--------------------|--------------------|
| [e.g. Competitor pricing] | 90 days | Re-ingest and compare |
| [e.g. Regulations / law] | On amendment | Flag with ⚠️ STALE |
| [e.g. CRM export] | 30 days | Re-export and ingest |
| [e.g. Financial model] | Each version | Create new versioned source page |

When a page is stale, mark it: `⚠️ STALE — last ingested [date], threshold [n] days, re-check before relying`

---

## 11. AI BEHAVIOR CONSTRAINTS

1. Do NOT rely on training knowledge for [domain]-specific facts — always read from raw/ or wiki/.
2. Do NOT cite [specific source type, e.g. case numbers, revenue figures] from memory — only cite what appears in wiki/ or raw/.
3. [Framing rule 1 from § 1 — again, intentional]
4. [Framing rule 2]
5. [Framing rule 3]
6. ALWAYS include `[VERIFY: reason]` when advising on [domain-specific sensitive areas].
7. ALWAYS recommend specialist consultation for [high-risk areas: legal proceedings, tax positions, medical, financial advice].
8. If you find yourself making claims without a source citation, STOP — check wiki/ before continuing.
9. If a query requires information not yet in the vault, say so explicitly rather than inferring from training data.
```

---

## PHASE 4 — BUILD

**Goal:** Create all files. Execute in order. Report each file as it's created.

### 4.1 — Create Directories

```bash
mkdir -p [vault_path]/raw/{[domain-a],[domain-b],[domain-c]}
mkdir -p [vault_path]/wiki/index
mkdir -p [vault_path]/wiki/sources
mkdir -p [vault_path]/wiki/entities
mkdir -p [vault_path]/wiki/concepts
mkdir -p [vault_path]/wiki/topics
mkdir -p [vault_path]/wiki/playbooks
mkdir -p [vault_path]/wiki/contradictions
mkdir -p [vault_path]/wiki/[domain-specific-dirs]
mkdir -p [vault_path]/logs
```

### 4.2 — Write CLAUDE.md

Write the full constitution from Phase 3. Verify all 11 sections are present before moving on.

### 4.3 — Write MASTER-INDEX.md

```markdown
# [Vault Name] — Master Index
**Maintainer:** [User/Team]
**Last update:** [date] — vault initialized
**Status:** 🟡 INITIALIZING — structure built; population pending

---

## Navigation
- [[ACTIVITY-LOG]] — all ingestions, updates, conflicts
- [[CLAUDE]] — vault schema and AI rules
- [[QUICK-START]] — magic words and how to use this vault

---

## [DOMAIN SECTION 1]
| Page | Description | Priority | Status |
|------|-------------|----------|--------|
| [[seed-page-1]] | [what it contains] | CRITICAL | 🟡 Seed created |
| [[planned-page-1]] | [what it will contain] | HIGH | ⬜ Not yet created |

## [DOMAIN SECTION 2]
...

---

## ⚠️ OPEN VERIFICATIONS
| Item | Location | Added |
|------|----------|-------|
| [VERIFY item from intake] | [[page]] | [date] |

---

## PRIORITY SOURCE QUEUE
| # | Source | Type | Tier | Status |
|---|--------|------|------|--------|
| 1 | [Source name] | [type] | 1 | ⬜ Not ingested |
| 2 | ... | | 1 | ⬜ |

---

## STATISTICS
| Category | Planned | Created | Populated |
|----------|---------|---------|-----------|
| Sources | [n] | 0 | 0 |
| Entities | [n] | [seed count] | [seed count] |
| Concepts | [n] | [seed count] | [seed count] |
| Topics | [n] | 0 | 0 |
| Playbooks | [n] | 0 | 0 |
| raw/ files | 0 | 0 | — |
```

### 4.4 — Write ACTIVITY-LOG.md

```markdown
# Activity Log — [Vault Name]

| Date | Action | Source | Pages created | Pages updated | Conflicts |
|------|--------|--------|---------------|---------------|-----------|
| [date] | INIT | System | CLAUDE.md, MASTER-INDEX, ACTIVITY-LOG, QUICK-START, MEMORY, [n] seed pages | — | — |

---

## Detail log

### [date] — Vault initialization
- **Type:** Full vault setup via vault-builder skill
- **Executed by:** Claude
- **Domain:** [domain]
- **Structure created:** [list directories]
- **Seed pages:** [list]
- **Framing rules:** [list]
- **Open assumptions:** [list any [ASSUMED] items]
- **Next step:** Ingest Tier 1 sources — see MASTER-INDEX § Priority Source Queue
```

### 4.5 — Write HOW-TO-POPULATE.md (in raw/)

```markdown
# How to Populate This Vault

## The three ways to add a source

**Option A — Drop a file into raw/**
1. Save to `raw/[relevant-subdir]/[filename]`
2. Say: "ingest [filename]"
3. Claude runs the full 12-step INGEST workflow from CLAUDE.md

**Option B — Paste content**
Say: "ingest this:" followed by the content.
Claude asks for metadata (title, date, author) then proceeds.

**Option C — URL**
Say: "ingest [URL]"
Claude fetches, parses, and ingests (public URLs only).

## Source naming conventions
- Documents: `[type]-[YYYY-MM]-[short-title].md`
- Reports: `report-[YYYY]-[author]-[slug].md`
- Data exports: `export-[system]-[YYYY-MM-DD].csv`
- Legal/regulatory: `[law-name]-[article]-[date].md`

## What happens when you ingest
Claude will: read → extract → confirm (5-bullet summary) → create wiki pages
→ check contradictions → update MASTER-INDEX → update ACTIVITY-LOG → report.
You confirm before any pages are written.

## Known limitations
[From § 7 of CLAUDE.md — repeated here for discoverability]
```

### 4.6 — Write QUICK-START.md (vault root)

```markdown
# Quick Start — [Vault Name]

## Magic words

| Say this... | Claude does this |
|-------------|-----------------|
| `ingest [filename or URL]` | Reads source, creates wiki pages, logs everything |
| `lint the wiki` | Finds broken links, orphan pages, stale sources, open VERIFYs |
| `[any question about the domain]` | Searches wiki and answers with citations |
| `draft a [document type]` | Produces a draft using wiki content as source |
| `what does [term] mean?` | Looks up wiki/concepts/ and explains |
| `what do we know about [entity]?` | Looks up wiki/entities/ and summarizes |
| `what's the status of [topic]?` | Reads wiki/topics/ and reports |
| `update [page name]` | Re-reads the source and refreshes the wiki page |

## Framing rules (critical)
[The 3-5 rules from CLAUDE.md § 1 — repeat verbatim here]

## What NOT to ask
- Don't ask for information not yet in the vault without saying "even if you don't have a source" — Claude will use training data if you don't flag it
- Don't skip ingestion and ask directly — the wiki answer is always more reliable than training data

## Next step
Ingest your first document: `ingest [name of your most important source]`
```

### 4.7 — Write MEMORY.md (vault root)

```markdown
# [Vault Name] — Session Memory

**Vault path:** [absolute path]
**Domain:** [domain]
**CLAUDE.md:** [absolute path]/CLAUDE.md
**MASTER-INDEX:** [absolute path]/wiki/index/MASTER-INDEX.md
**Last session:** [date]

## To resume
Read MASTER-INDEX.md first. It lists all pages, their status, and open items.

## Critical reminders for Claude
[The 3 most important framing rules — so they survive session restart even
without loading CLAUDE.md first]
1. [Rule 1]
2. [Rule 2]
3. [Rule 3]
```

### 4.8 — Write Seed Wiki Pages

For each of the 5 domain-specific seed pages from § 2.3:

- Use the relevant template from § Standard Page Templates
- Fill in everything already known from Phase 1 answers
- Mark every unknown field `[VERIFY: populate when source ingested]`
- Add [[wikilinks]] to other seed pages (even if they're also stubs)
- Add each seed page to MASTER-INDEX with status 🟡

### 4.9 — Write Contradiction Template (in wiki/contradictions/)

Create `wiki/contradictions/TEMPLATE.md` as the reusable contradiction format:

```markdown
# Contradiction: [Short description]
**ID:** CONTRA-[NNN]
**Detected:** [date]
**Severity:** CRITICAL / HIGH / MEDIUM
**Status:** OPEN / RESOLVED / ACCEPTED

## Conflicting claims

**Claim A:**
- Source: [[source-page-a]]
- Text: "[exact quote or paraphrase]"

**Claim B:**
- Source: [[source-page-b]]
- Text: "[exact quote or paraphrase]"

## Nature of conflict
[What exactly conflicts: date, number, name, interpretation, etc.]

## Resolution options
1. [Option A — e.g. "Source A is more recent; deprecate B"]
2. [Option B — e.g. "Both are correct in different contexts — add scope labels"]
3. [Option C — e.g. "Verify with specialist before relying on either"]

## Decision
[OPEN — awaiting user decision]

## Affected pages
- [[page-a]] — notified
- [[page-b]] — notified
```

---

## PHASE 5 — VALIDATE

**Goal:** Confirm structure is complete and content is non-trivial. Report readiness.

### 5.1 — Structural Check

```
✅/❌ CLAUDE.md exists — all 11 sections present
✅/❌ MASTER-INDEX.md exists — all planned pages listed
✅/❌ ACTIVITY-LOG.md exists — init entry logged
✅/❌ QUICK-START.md exists — magic words present
✅/❌ MEMORY.md exists — vault path and framing rules captured
✅/❌ HOW-TO-POPULATE.md exists in raw/
✅/❌ wiki/contradictions/ exists with TEMPLATE.md
✅/❌ All [n] domain directories exist in raw/
✅/❌ All [n] page-type directories exist in wiki/
✅/❌ All 5 seed pages exist in wiki/
```

### 5.2 — Content Quality Check

Pick one seed page at random. Verify:
- Does it have real content from Phase 1 answers, not just section headers?
- Does it have at least one [[wikilink]] to another page in the vault?
- Does it have a "Relevance to [User]" section with at least one concrete sentence?
- Does every unknown field have a [VERIFY] tag rather than being left blank?

If any seed page is just headers with no content: flag it as CRITICAL and rewrite it before delivering.

### 5.3 — CLAUDE.md Completeness Check

- Framing rules: ≥3 listed in § 1, repeated in § 5, repeated in § 11 ✅/❌
- INGEST workflow: all 12 steps present ✅/❌
- LINT workflow: includes grep/glob instructions ✅/❌
- Freshness policy: thresholds defined for each source type ✅/❌
- Glossary: ≥5 domain terms defined ✅/❌

### 5.4 — Readiness Report

```
## Vault Readiness Report — [Vault Name]

**Status:** 🟡 READY FOR POPULATION

**Built:**
- CLAUDE.md constitution ([n] sections, [n] page templates, [n] framing rules)
- [n] directories ([raw]: [n] subdirs, [wiki]: [n] page-type dirs)
- [n] seed wiki pages (entities: [n], concepts: [n], topics: [n])
- QUICK-START.md, MEMORY.md, HOW-TO-POPULATE.md, contradiction template

**First ingestion recommended:**
→ [Name the single highest-priority Tier 1 source]
→ Say: "ingest [source name]" to begin

**Open assumptions (confirm these):**
[List all [ASSUMED] items with their defaults]

**Open verifications (from intake):**
[List all [VERIFY] items placed during seed page creation]

**Framing rules active:**
1. [Rule 1]
2. [Rule 2]
3. [Rule 3]

**Known limitations for this vault:**
[2-3 relevant items from § Known Limitations]

**To evolve the schema later:**
See § Schema Evolution in this skill file.
```

---

## PHASE 6 — FIRST INGESTION (offer immediately after Phase 5)

Do not end the conversation after delivering the readiness report. Say:

> "The vault is ready. Your highest-priority Tier 1 source is [source name].
> Do you want to ingest it now? If you drop the file or paste the content,
> I'll run the full ingestion workflow immediately."

If the user provides a source: execute the 12-step INGEST workflow from CLAUDE.md § 4.1 right now, in this session.

If the user declines: remind them of the magic word (`ingest [filename]`) and end.

---

## Standard Page Templates

These go into the vault's CLAUDE.md § 3. Adapt field names to the domain.

### Source / Document Page
```markdown
# [Document title]
**Type:** [Report / Contract / Law / Export / Transcript / ...]
**Author/Issuer:** [name or org]
**Date:** [YYYY-MM-DD]
**Ingested:** [YYYY-MM-DD]
**Source location:** raw/[subdir]/[filename]
**Relevance:** HIGH / MEDIUM / LOW — [one sentence reason]
**Freshness:** ✅ Current / ⚠️ STALE — re-check by [date]

## Summary
[3-5 bullets: key facts, holdings, or data points from this source]

## Key Sections / Provisions
| Section | Content | Operational significance |
|---------|---------|------------------------|
| [§ or clause] | [what it says] | [why it matters to [user]] |

## Relevance to [User/Company]
[Direct operational implications — named, concrete, specific]

## Contradictions / Conflicts
[Any conflicts with other wiki pages — link to wiki/contradictions/]

## Open Questions
[VERIFY: ...]

## Related Pages
[[link1]] [[link2]]
```

### Entity Page
```markdown
# [Entity name]
**Type:** [Client / Competitor / Regulator / Person / Product / Court / ...]
**[Key field 1]:** [value]
**[Key field 2]:** [value]
**Relevance:** HIGH / MEDIUM / LOW — [reason]

## Overview
[2-3 sentences: who/what this is and why it matters to [user]]

## Key Facts
| Field | Value | Source | Last verified |
|-------|-------|--------|---------------|
| [field] | [value] | [[source-page]] | [date] |

## Relevance to [User/Company]
[How [user] interacts with or is affected by this entity — specific and named]

## Open Questions / To Verify
[VERIFY: ...]

## Related Pages
[[link1]] [[link2]]
```

### Concept Page
```markdown
# [Concept name]
**Domain:** [area of knowledge]
**Defined in:** [[source-page]] — [specific section]
**Synonym / related:** [aliases]

## Definition
[Authoritative definition — cite source with section number]

## Key Criteria / Requirements
[The elements that establish or invoke this concept]

## Application at [User/Company]
[How this concept is used operationally — specific projects or cases named]

## Edge Cases / Exceptions
[When the concept doesn't apply; limitations]

## Open Questions
[VERIFY: ...]

## Related Pages
[[link1]] [[link2]]
```

### Topic Page
```markdown
# [Topic name]
**Domain:** [area]
**Core sources:** [[link1]] [[link2]]
**Status for [User]:** [current operational state in one sentence]
**Last reviewed:** [date]

## Overview
[2-3 paragraphs synthesizing this topic as it applies to [user] — not abstract law,
but what it means for the business right now]

## Framework
[Structured breakdown — tables, numbered lists, decision trees as appropriate]

## [User]-Specific Application
[Named strategies, open decisions, active risks — concrete and current]

## Critical Timelines / Deadlines
| Date | Event | Action required |
|------|-------|----------------|
| [date] | [event] | [what to do] |

## Open Questions
[VERIFY: ...]

## Related Pages
[[link1]] [[link2]]
```

### Playbook Page
```markdown
# Playbook: [Task name]
**Domain:** [area]
**Triggered by:** [when to use — specific condition]
**Owner:** [who executes]
**Typical duration:** [timeline]
**Last used:** [date / never]

## Steps
1. [Step 1 — who does what, what document is produced, what tool is used]
2. [Step 2]
...

## Required Templates / Tools
[[link1]] [[link2]]

## Governing Framework
[Rules, laws, or policies this playbook must comply with]

## Common Mistakes
[Specific documented pitfalls — not generic advice]

## Precedents
[Prior uses of this playbook — named examples]
```

---

## § 6 — Domain-Specific Adapters

### 6.1 — Sales Vault
**Extra framing rules:**
- "Always attribute claims to a named account or source — no generic 'customers say' statements"
- "Distinguish 'confirmed deal terms' from 'discussed in conversation'"
- "Never state a competitor's feature as current without a source dated < 60 days"

**Extra page types:** `wiki/accounts/`, `wiki/competitors/`, `wiki/objections/`, `wiki/wins/`, `wiki/losses/`

**Extra topics:** Territory overview, ICP definition, Objection-handling library, Competitive positioning

**Extra AI constraints:** "Never fabricate pipeline numbers. Only cite figures from a named CRM export with date."

**Key source types:** CRM export (CSV/JSON), call transcripts, win/loss interviews, competitor teardowns, pricing sheets, proposals

### 6.2 — Finance Vault
**Extra framing rules:**
- "Never cite a financial figure without naming the model version and date — e.g. 'FM v3.51, 2026-04-20'"
- "Distinguish 'committed' from 'projected' from 'sensitized' figures — always label which"
- "Never state a covenant is met without citing the calculation source"

**Extra page types:** `wiki/models/`, `wiki/transactions/`, `wiki/covenants/`, `wiki/scenarios/`

**Extra topics:** Capital structure, Debt sizing, Revenue stack, Sensitivity analysis, Liquidity position

**Extra AI constraints:** "Always flag when a figure depends on assumptions marked [VERIFY] or [ASSUMED] in the model source."

**Key source types:** Financial model (xlsx → converted to md summary), term sheets, bank credit approval memos, audited accounts, investor decks, board reports

### 6.3 — Legal Vault
**Extra framing rules:**
- "Never cite a case number or statute article from memory — only cite what appears in wiki/ or raw/"
- "Always note the last-amended date of any statute relied on"
- "Never use [forbidden term] — use [permitted term] instead" [fill in per project]

**Extra page types:** `wiki/case-law/`, `wiki/laws/`, `wiki/regulations/`, `wiki/opinions/`

**Extra topics:** Permitting strategy, Subsidy compliance, Contractual risk, Regulatory timeline

**Extra AI constraints:** "Do NOT rely on training knowledge for statute text — always read from raw/ or wiki/laws/. Do NOT cite ECLI numbers from memory."

**Key source types:** Court decisions, statutes from official databases, regulatory opinions, legal memos, government guidance

### 6.4 — HR / People Vault
**Extra framing rules:**
- "All PII (names, salaries, performance ratings) stays in raw/ — wiki pages use role/function titles only"
- "Never state a policy is 'current' without confirming the version date"
- "Label every jurisdiction: UK / NL / NO / US — employment law is jurisdiction-specific"

**Extra page types:** `wiki/policies/`, `wiki/roles/`, `wiki/compensation-bands/`

**Extra topics:** Onboarding checklist, Performance cycle, Compliance calendar, Offboarding procedure

**Extra AI constraints:** "Never store individual names in wiki/ pages — use role identifiers. Never state a legal position without jurisdiction."

**Key source types:** Employment contracts (anonymized), HR handbooks, org charts, compensation benchmarks, works council agreements

### 6.5 — Product / GTM Vault
**Extra framing rules:**
- "Distinguish 'committed roadmap' (in Jira/source) from 'aspirational roadmap' (in decks) — always tag which"
- "Never state a feature is 'available' without a source dated < 90 days"
- "Never describe a competitor's product without citing a source"

**Extra page types:** `wiki/features/`, `wiki/personas/`, `wiki/roadmap/`, `wiki/competitors/`

**Extra topics:** ICP definition, Pricing structure, Launch playbook, Feature adoption data

**Extra AI constraints:** "Never assert product capability without confirming from a source. Never state a pricing figure without model version and date."

**Key source types:** Product specs, user research reports, NPS/CSAT data, competitor teardowns, pricing sheets, launch briefs

---

## § 7 — Known Limitations

Tell the user these upfront (include 2-3 relevant ones in the Vault Brief):

1. **High-quantitative data:** Financial models with hundreds of dynamic formulas belong in spreadsheets, not markdown. The vault stores the *output and interpretation* of models — not the model itself. Ingest a narrative summary or key-metrics extract, not the raw xlsx.

2. **Image-heavy content:** Design specs, UI mockups, and visual assets can't be stored meaningfully in markdown. The vault stores text descriptions and links to external asset stores.

3. **Large documents (>50K tokens):** Very long documents should be chunked before ingestion — e.g. by chapter or section. Otherwise Claude may summarize incompletely. HOW-TO-POPULATE.md explains chunking.

4. **Multi-user vaults:** Multiple people asking Claude to update the vault simultaneously will create divergence. Designate one person (or one agent session) as the authoritative updater at a time.

5. **Real-time data:** The vault reflects a point-in-time snapshot. Live data (stock prices, pipeline stages) must be re-ingested regularly per the Freshness Policy in CLAUDE.md § 10.

6. **Training data bleed:** Claude may use training knowledge when vault content is sparse. The more the vault is populated, the more reliable citations become. Use [VERIFY] tags aggressively in early stages.

---

## § 8 — Schema Evolution

When the vault needs to change (new page type, new framing rule, updated template):

1. **Update CLAUDE.md first.** Change the relevant section and add a "Changed: [date] — [what changed]" note inline.
2. **Update MASTER-INDEX.md** to add the new page type / directory.
3. **Create the new directory** if a new page type was added.
4. **Retroactively tag affected pages.** If an existing page type now has a new required field, add `[VERIFY: new field — add [field name]]` to existing pages of that type.
5. **Log in ACTIVITY-LOG.md** under a "Schema update" entry.
6. **Do NOT retroactively rewrite all existing pages.** Let them accumulate `[VERIFY]` tags and update on next re-ingestion.

---

## § 9 — Worked Example (Legal Vault — Dutch Legal)

This is what a completed vault looks like. Reference this if the user wants to see the pattern in action.

**CLAUDE.md § 1 (Operational Context) — example:**
> "Company: Digital Energy Group — Dutch operations of EcoDigital AG. Business: AI-factory datacenters embedded in Dutch greenhouses; waste-heat recovery to growers; BESS flexibility-as-a-service; SDE++ subsidy projects. Active footprint: 16 projects across 8 municipalities; 13 signed grower agreements; EUR 800M+ pipeline.
> Critical framing rule: All facilities are 'energie-installaties' or 'warmteproductie-installaties' — NEVER 'datacenters' in permitting, municipality, or grid operator contexts."

**What made it work:**
- 3 confirmed framing rules prevented hundreds of wrong documents
- INGEST workflow surfaced 230 fabricated ECLIs that would have caused legal damage
- [VERIFY] tags flagged Art. 4.1 Energiewet error before it appeared in a brief
- MASTER-INDEX with ✓/⚠️/🚨 status gave real-time project risk visibility
- Contradiction pages caught the "Buitengebied Epe" case being mislabeled as a datacenter ruling

**What to replicate:**
- Framing rules × 3 minimum
- Every source page gets a "Relevance to [User]" section — no orphan knowledge
- VERIFY tags on anything not confirmed from a primary source
- MASTER-INDEX updated every session — it's the dashboard, not just an index
