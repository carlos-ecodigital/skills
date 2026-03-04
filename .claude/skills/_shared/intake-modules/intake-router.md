# Investment Case Intake — Router & Orchestration

## Purpose

This router determines the intake track (Seed Round, Project Financing, or Both), identifies the company and asset types, then progressively loads the appropriate intake modules. Each module is self-contained and fits within a 25K token context window.

---

## Phase 0: Identity & Track Selection

Before loading any intake module, ask these 4 routing questions:

### R1. Company Identity
`ANS` | `REQUIRED`

- Company name
- One-sentence description of what the company does
- Jurisdiction of incorporation (e.g., Switzerland, Netherlands, US, UK)
- Stage (pre-revenue, early revenue, growth)

### R2. Investment Case Track
`ANS` | `REQUIRED`

What type of investment case are you building?

| Track | Description | Use When |
|-------|-------------|----------|
| **SEED** | Equity fundraise (seed, Series A, growth equity) | Raising equity from VCs, angels, family offices, infra funds |
| **PF** | Project/program financing (non-recourse debt) | Sizing and securing project-level debt for specific assets |
| **BOTH** | Combined equity + project finance | Raising equity at holdco level AND debt at project SPV level |

### R3. Asset Types
`ANS` | `REQUIRED`

Which asset types are included? (Select all that apply)

- [ ] BESS (battery energy storage system)
- [ ] DC/AI (data center / AI colocation)
- [ ] Heat (waste heat recovery, district heating, greenhouse supply)
- [ ] Other (describe)

### R4. Existing Materials
`ANS` | `REQUIRED`

What materials already exist? (Share any available)

- [ ] Pitch deck
- [ ] Executive summary
- [ ] Financial model
- [ ] Cap table
- [ ] Corporate structure diagram
- [ ] LOIs / term sheets
- [ ] Technical specifications
- [ ] Permit documents
- [ ] Other (describe)

---

## Module Loading Matrix

Based on R2 (track) and R3 (asset types), load modules in this order:

| Module | File | Seed | PF | Both | Condition |
|--------|------|------|----|------|-----------|
| **M0** | `m0-document-ingestion.md` | Always | Always | Always | — |
| **M1** | `m1-entity-tax.md` | Always | Always | Always | — |
| **M2** | `m2-founder-team.md` | Always | Optional | Always | PF: load only if sponsor DD needed |
| **M3** | `m3-market-solution.md` | Always | Always | Always | PF: skip `[SEED-ONLY]` questions |
| **M4** | `m4-bess-technical.md` | If BESS | If BESS | If BESS | Seed: P0 questions only |
| **M5** | `m5-dc-ai-technical.md` | If DC/AI | If DC/AI | If DC/AI | Seed: P0 questions only |
| **M6** | `m6-sites-assets.md` | Always | Always | Always | Repeat per site |
| **M7** | `m7-revenue-debt.md` | Always | Always | Always | Seed: S9 full, S10 light; PF: full |
| **M8** | `m8-equity-capital.md` | Always | Skip | Seed portions | PF: only yield/co-invest questions |
| **M9** | `m9-synthesis.md` | Always | Always | Always | PF: skip `[SEED-ONLY]` sections |

**Progressive loading rule**: Load ONE module at a time. Complete its questions before loading the next. This keeps context usage under 25K tokens per interaction phase.

---

## Parallel Track Assignment

Modules can be worked on in parallel tracks when dependencies allow:

| Track | Modules | Dependencies |
|-------|---------|-------------|
| **A** (Immediate) | M2 (team), M3 partially (problem, solution), M9 partially (founder narrative S20) | None |
| **B** (Entity) | M1 (entity + tax) | None |
| **C** (Site/Technical) | M4, M5, M6, M7 (S9 revenue) | M6 feeds M4, M5 |
| **D** (Financial) | M7 (S10 debt), M9 (S12 financial model) | Depends on Track C |
| **E** (Synthesis) | M8, M9 (S14-S20, validations) | Depends on Tracks A-D |

---

## Legends (Shared Across All Modules)

### Input Method Tags
| Tag | Meaning |
|-----|---------|
| `DOC` | Upload or reference an existing document |
| `ANS` | Direct answer from founder/team |
| `VAL` | Validate an existing assumption with evidence |
| `CAL` | Calculate from provided data |
| `EXT` | Requires external verification (counsel, engineer, auditor) |

### Priority Tiers
| Tier | When Required | Typical Questions |
|------|--------------|-------------------|
| `P0` | Before any investor/lender conversation | ~120 questions across modules |
| `P1` | Before due diligence | ~180 additional questions |
| `P2` | Before term sheet / financial close | ~200 additional questions |

### Track Tags
| Tag | Meaning |
|-----|---------|
| `[SEED]` | Ask only in Seed track |
| `[PF]` | Ask only in Project Finance track |
| `[BOTH]` | Ask in all tracks |
| `[SEED-SKIP]` | Skip in Seed track (PF-depth only) |
| `[PF-SKIP]` | Skip in PF track (Seed-depth only) |

### Gate Criteria Tags
| Tag | Meaning |
|-----|---------|
| `[EXACT]` | Requires a specific number or date |
| `[RANGE]` | Acceptable as a range with stated assumptions |
| `[NARRATIVE]` | Requires 3+ sentences of substantive explanation |
| `[BINARY]` | Yes/no with mandatory supporting detail |
| `[DOC-REQUIRED]` | Must provide or reference an actual document |

### Skill Feed Tags
| Tag | Skill |
|-----|-------|
| `SF` | seed-fundraising |
| `PF` | project-financing |
| `LC` | legal-counsel |
| `DR` | ops-dataroomops |
| `NP` | netherlands-permitting |
| `CS` | collateral-studio |
| `PE` | positioning-expert |
| `BB` | de-brand-bible |
| `SO` | ops-storyops |
| `DO` | ops-dealops |
| `TO` | ops-targetops |
| `OO` | ops-outreachops |
| `IR` | ops-irops |

---

## Mini-Deliverable Triggers

After completing module clusters, produce intermediate deliverables:

| Trigger | Modules Completed | Output |
|---------|-------------------|--------|
| **Corporate Structure Summary** | M1 | 2-page entity + tax overview |
| **Pitch Narrative Draft** | M2 + M3 | 5-page narrative (team, problem, solution) |
| **Technical Asset Summary** | M4/M5 + M6 | Per-site one-pager (tech specs + site details) |
| **Financial Overview Draft** | M7 + M9 (S12) | Revenue model + financial projections summary |
| **Investment Materials Package** | All above | Pitch deck draft + executive summary draft |
| **Complete Investment Case** | All modules | Full IM + all deliverables |

---

## Investment Case Readiness Score

After each module is completed, update the readiness score:

| Level | Criteria | Score |
|-------|----------|-------|
| **Level 1: Conversation-Ready** | M1 + M2 + M3 (P0 only) | 20% |
| **Level 2: First Meeting-Ready** | Level 1 + M6 + M7 (S9) + M9 (S14 traction) | 40% |
| **Level 3: Materials-Ready** | Level 2 + M4/M5 + M9 (S12 model) + M9 (S16 exit) | 60% |
| **Level 4: DD-Ready** | Level 3 + M1 (S2 tax) + M7 (S10 debt) + M8 + M9 (S15 risk, S18 negotiation, S19 data room) | 80% |
| **Level 5: Institutional-Grade** | Level 4 + all cross-cutting validations pass + all P2 questions answered | 100% |

---

## Orchestration Rules

1. **Always start with this router** — determine track and asset types before loading any content module
2. **Load M0 (document ingestion) second** — ingest existing materials before asking questions
3. **Progressive loading** — load one module at a time; complete it before loading the next
4. **Track-aware question skipping** — respect `[SEED]`, `[PF]`, `[BOTH]` tags on every question
5. **Asset-conditional modules** — only load M4 (BESS) and M5 (DC/AI) if those asset types are selected
6. **Per-site repetition** — M6 (sites) is answered once per site; M4/M5 may have per-site variations
7. **Batching** — present 2-4 questions per interaction round (3 is the sweet spot)
8. **Document-first** — if a document can answer a question, mark it `[CAPTURED FROM: document_name]` and skip
9. **Gate enforcement** — each module has its own gate summary; failing gates blocks advancement to synthesis modules
10. **Company variable** — use `{company}` placeholder throughout; replace with R1 answer when presenting questions
