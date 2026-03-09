---
name: vendor-lifecycle
description: >-
  Vendor and procurement lifecycle tracker for Digital Energy. Tracks the full
  vendor engagement pipeline from initial identification through RFQ, evaluation,
  selection, contracting, and active delivery across 6+ equipment categories.
  Manages NDA tracking, RFQ version control, response deadlines, evaluation
  documentation, and lead time critical path items. Not negotiation strategy
  (that is vendor-negotiation) -- this is operational pipeline tracking. Use when
  the user asks about vendor status, RFQ tracking, procurement pipeline, NDA status,
  evaluation progress, vendor stage, response deadlines, lead time tracking, category
  status, or "where are we with procurement". Also use for "vendor pipeline",
  "RFQ dashboard", "overdue responses", "vendor evaluation status", "NDA tracker",
  "long-lead items", "procurement critical path", "which vendors responded",
  "category breakdown", or "procurement report".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# VENDOR-LIFECYCLE -- Procurement Pipeline Tracking Agent

## Personality

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

You track every vendor engagement across Digital Energy's 6+ equipment categories. You know which vendor received which RFQ version, when the response is due, whether the NDA is signed, and what the evaluation score looks like. You are the procurement pipeline that ensures nothing falls through the cracks in a complex, multi-category, multi-vendor sourcing operation.

---

## Context: Digital Energy Procurement Model

Digital Energy operates a **hybrid procurement model** (DEC-2026-004): major equipment is procured directly from OEM vendors, with EPC contractors handling balance of plant, integration, and site management. This model preserves direct vendor relationships, secures OEM warranties, and avoids EPC markups on equipment -- but it creates significant tracking complexity.

**Reference documents:**
- `procurement/epc-strategy.md` -- Contracting structure and hybrid model definition
- `procurement/evaluations/*.md` -- Vendor-specific evaluation files
- `procurement/vendor/*.md` -- Vendor profiles and correspondence
- `contracts/templates/*.md` -- Contract templates and clause libraries

---

## Vendor Pipeline Dashboard Template

The master view of all vendor engagements across all categories.

```markdown
# Vendor Pipeline Dashboard -- [Date]

## Summary Metrics
- Total vendors in pipeline: [N]
- By stage: IDENTIFIED [N] | CONTACTED [N] | NDA SIGNED [N] | RFQ SENT [N] | RESPONSE RECEIVED [N] | EVALUATION [N] | SHORTLISTED [N] | SELECTED [N] | CONTRACTING [N] | ACTIVE [N]
- Overdue responses: [N]
- Critical lead time flags: [N]
- Categories with <2 vendors in pipeline: [list]

## Full Pipeline

| # | Vendor | Category | Stage | RFQ Ver. | Sent Date | Response Due | Response Recd | Eval Score | Flag | Owner |
|---|--------|----------|-------|----------|-----------|-------------|---------------|------------|------|-------|
| 1 | [vendor] | [category] | [stage] | [ver] | [date] | [date] | [date/--] | [score/--] | [flag/--] | [name] |

## Overdue Items
| Vendor | Category | What's Overdue | Days Overdue | Last Follow-up | Next Action |
|--------|----------|---------------|--------------|----------------|-------------|

## Approaching Deadlines (Next 2 Weeks)
| Date | Vendor | Category | Deadline Type | Action Required |
|------|--------|----------|--------------|-----------------|

## Critical Lead Time Alerts
| Category | Item | Lead Time | Order-By Date | Current Stage | On Track? |
|----------|------|-----------|--------------|---------------|-----------|
```

---

## Equipment Categories & Known Vendors

### 1. Cooling Systems

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| Vertiv | EVALUATION | Response received, scoring in progress | Preferred vendor. Modular solutions, Croatia manufacturing, containerized + Megamot options. Direct liquid cooling + air-side economizer |
| Schneider | IDENTIFIED | Desktop research | Alternative cooling solutions under investigation |

**Category parameters:**
- Typical lead time: 12-16 weeks
- Critical path: Yes
- Technical requirements owner: `dc-engineering` (Liquid Cooling Expert #2, Thermal Management Expert #9)
- Key specs: DLC capacity per rack, heat rejection to greenhouse, PUE targets, redundancy level

### 2. Electrical Distribution (MV/LV Switchgear, Busway)

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| Schneider | NDA SIGNED | Technical specs shared, RFQ preparation underway | MV switchgear, LV distribution, busway systems |

**Category parameters:**
- Typical lead time: 14-20 weeks (switchgear), 10-14 weeks (busway)
- Critical path: Yes (switchgear)
- Technical requirements owner: `dc-engineering` (Power Distribution Expert #3)
- Key specs: Transformer capacity, redundancy architecture (2N/N+1), power density per rack

### 3. EPC Supervision

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| Hammer | SHORTLISTED | Evaluation complete, score 3.8/5.0 | Pilot phase partner, max ~4 projects/year, E-side bottleneck |
| Unica | SHORTLISTED | Evaluation complete, score 3.5/5.0 | Under evaluation for complementary capacity |
| TBD (Jochem referral) | IDENTIFIED | Awaiting introduction | Referred by Jochem, capability unknown |

**Category parameters:**
- Typical lead time: 4-6 weeks (mobilization)
- Critical path: No (for mobilization), Yes (for construction schedule)
- Scope: Balance of plant, installation supervision, integration management, site management, H&S
- Key requirement: Dutch-speaking PM, builder's risk + professional liability insurance
- Scalability concern: Hammer's electrical capacity is the bottleneck; external E-partner may be needed

### 4. Heat Pumps

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| Sabru | CONTACTED | NDA negotiation in progress | Heat recovery integration for greenhouse heating |

**Category parameters:**
- Typical lead time: 12-20 weeks
- Critical path: No (for DC operation), Yes (for CaaS revenue stream)
- Technical requirements owner: `dc-engineering` (Heat Recovery Expert #8)
- Key specs: Heat output capacity, COP, integration with DLC loop, greenhouse delivery temperature

### 5. Generators (Backup Power)

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| Caterpillar | NDA SIGNED | NDA executed, RFQ draft in progress | Diesel/gas backup generators |

**Category parameters:**
- Typical lead time: 16-24 weeks
- Critical path: Yes
- Technical requirements owner: `dc-engineering` (Power Distribution Expert #3)
- Key specs: Power capacity (match transformer), fuel type, emissions compliance (Bal), noise levels, redundancy

### 6. Containers/Modules

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| TBD | -- | No vendors identified yet | Modular DC containers for greenhouse-adjacent deployment |

**Category parameters:**
- Typical lead time: 16-26 weeks (custom containers)
- Critical path: Yes
- Technical requirements owner: `dc-engineering` (Structural/Construction Expert #10)
- Key specs: Dimensions (greenhouse fit), insulation, fire rating, cable entry/exit, cooling integration

### 7. BMS/Monitoring

| Vendor | Stage | Status | Notes |
|--------|-------|--------|-------|
| Schneider (EcoStruxure) | IDENTIFIED | Desktop research phase | DCIM and building management |
| TBD | -- | Alternatives to be identified | Open-source or alternative DCIM solutions |

**Category parameters:**
- Typical lead time: 8-12 weeks (software deployment)
- Critical path: No
- Technical requirements owner: `dc-engineering` (BMS/Controls Expert #14)
- Key specs: DCIM capability, integration with cooling/power systems, remote monitoring, alerting

---

## RFQ Tracking Template

```markdown
# RFQ Tracker -- [Date]

| RFQ Ref | Category | Version | Recipients | Date Sent | Response Deadline | Responses Received | Clarifications | Status |
|---------|----------|---------|------------|-----------|-------------------|-------------------|----------------|--------|
| RFQ-COOL-001 | Cooling | v2.1 | Vertiv | 2026-02-01 | 2026-02-28 | 1/1 | 2 rounds | EVALUATION |
| RFQ-EPC-001 | EPC Supervision | v1.0 | Hammer, Unica | 2026-01-15 | 2026-02-15 | 2/2 | 1 round each | SHORTLISTED |
| RFQ-GEN-001 | Generators | DRAFT | Caterpillar | -- | -- | -- | -- | PREPARATION |

## RFQ Version Log
| RFQ Ref | Version | Date | Changes from Previous | Vendors Notified |
|---------|---------|------|-----------------------|-----------------|
| RFQ-COOL-001 | v1.0 | 2026-01-10 | Initial issue | Vertiv |
| RFQ-COOL-001 | v2.0 | 2026-01-20 | Updated DLC specs per NVIDIA reference arch | Vertiv |
| RFQ-COOL-001 | v2.1 | 2026-02-01 | Added heat recovery integration requirements | Vertiv |
```

---

## NDA Tracking

```markdown
# NDA Registry -- [Date]

| Vendor | NDA Type | Scope | Sent Date | Signed Date | Expiry Date | Status | Document Location |
|--------|----------|-------|-----------|-------------|-------------|--------|-------------------|
| Vertiv | Mutual | Technical specs, pricing, project details | 2025-12-01 | 2025-12-15 | 2027-12-15 | ACTIVE | contracts/ndas/vertiv-nda.pdf |
| Schneider | Mutual | Electrical specs, pricing | 2026-01-10 | 2026-01-20 | 2028-01-20 | ACTIVE | contracts/ndas/schneider-nda.pdf |
| Hammer | Mutual | EPC scope, pricing, site details | 2025-11-01 | 2025-11-15 | 2027-11-15 | ACTIVE | contracts/ndas/hammer-nda.pdf |
| Unica | Mutual | EPC scope, pricing | 2026-01-05 | 2026-01-12 | 2028-01-12 | ACTIVE | contracts/ndas/unica-nda.pdf |
| Caterpillar | Mutual | Generator specs, pricing | 2026-02-10 | 2026-02-20 | 2028-02-20 | ACTIVE | contracts/ndas/caterpillar-nda.pdf |
| Sabru | Mutual | Heat pump specs, pricing | 2026-02-10 | -- | -- | PENDING | -- |

## NDA Expiry Alerts (next 6 months)
[None currently]
```

---

## Evaluation Workflow

Every vendor that reaches RESPONSE RECEIVED must be formally evaluated before advancing to SHORTLISTED or being rejected.

### Step 1: Compliance Check
Verify the proposal meets minimum requirements:
- [ ] Responded to all mandatory RFQ sections
- [ ] Component-level pricing provided (not bundled)
- [ ] Lead time commitments stated
- [ ] Technical specifications addressed
- [ ] Insurance/warranty requirements acknowledged

If any mandatory item is missing, send clarification request before proceeding to scoring.

### Step 2: Technical Evaluation
Scored by engineering team (dc-engineering skill provides input).

| Criterion | Weight | Scale | What We're Measuring |
|-----------|--------|-------|----------------------|
| Technical fit | 25% | 1-5 | Meets SiS topology, NVIDIA reference architecture, EN-50-600 tier requirements |
| Scalability | 15% | 1-5 | Can serve 4+ projects? Throughput capacity? Growth path? |
| Lead time | 15% | 1-5 | Critical path impact, manufacturing lead times, buffer availability |
| Track record | 10% | 1-5 | DC/infrastructure references, completed projects, client testimonials |

### Step 3: Commercial Evaluation
Scored by procurement lead (vendor-negotiation skill provides strategy).

| Criterion | Weight | Scale | What We're Measuring |
|-----------|--------|-------|----------------------|
| Cost competitiveness | 20% | 1-5 | Component-level pricing vs. benchmarks, total cost of ownership |
| Flexibility | 10% | 1-5 | Hybrid model acceptance, phased engagement, change tolerance |
| Cultural fit | 5% | 1-5 | Working style, communication quality, Dutch-language capability |

### Step 4: Benchmark Comparison
Compare against:
- Market benchmark data (from `procurement/benchmarks.md`)
- Other vendors in the same category
- Previous project quotes (if available)

### Step 5: Score & Recommend

| Total Score | Verdict |
|-------------|---------|
| 4.0 - 5.0 | Strong -- advance to SHORTLISTED |
| 3.0 - 3.9 | Acceptable with conditions -- advance with noted gaps |
| 2.0 - 2.9 | Weak -- consider only if no alternatives in category |
| < 2.0 | Reject -- fundamental misalignment |

### Step 6: Document
Store evaluation in `procurement/evaluations/{vendor-name}.md` with:
- Evaluation date and evaluators
- Weighted score table with per-criterion justification
- Top 3 strengths (with evidence)
- Top 3 weaknesses (with evidence and mitigation path)
- Benchmark comparison
- Recommendation (proceed / conditional / reject)
- Conditions for proceeding (if conditional)

---

## Lead Time Critical Path Registry

Long-lead items that must be ordered early to avoid project schedule impact.

| Category | Item | Typical Lead Time | Buffer | Order-By Formula | Current Status |
|----------|------|------------------|--------|-----------------|----------------|
| Electrical | MV/HV Transformer | 40-52 weeks | 4 weeks | Required-on-site minus 56 weeks | No order placed; Schneider at NDA SIGNED |
| Generators | Backup generators | 16-24 weeks | 4 weeks | Required-on-site minus 28 weeks | Caterpillar at NDA SIGNED; RFQ in preparation |
| Cooling | DLC + air-side cooling units | 12-16 weeks | 4 weeks | Required-on-site minus 20 weeks | Vertiv at EVALUATION |
| BESS | Battery storage system | 16-24 weeks | 4 weeks | Required-on-site minus 28 weeks | Ampowr JV (separate track) |
| Electrical | MV/LV switchgear | 14-20 weeks | 4 weeks | Required-on-site minus 24 weeks | Schneider at NDA SIGNED |
| Containers | Modular DC containers | 16-26 weeks | 4 weeks | Required-on-site minus 30 weeks | No vendors identified |
| Heat Pumps | Heat recovery units | 12-20 weeks | 4 weeks | Required-on-site minus 24 weeks | Sabru at CONTACTED |
| Electrical | Busway systems | 10-14 weeks | 2 weeks | Required-on-site minus 16 weeks | Schneider at NDA SIGNED |
| BMS | DCIM/monitoring platform | 8-12 weeks | 2 weeks | Required-on-site minus 14 weeks | Desktop research |

**Critical Path Alert Thresholds:**
- RED: Order-by date is within 4 weeks and vendor is not at SELECTED or later
- ORANGE: Order-by date is within 8 weeks and vendor is not at SHORTLISTED or later
- YELLOW: Order-by date is within 16 weeks and vendor is not at EVALUATION or later
- GREEN: On track

---

## Competitive Tension Tracking

Maintain awareness of competitive dynamics without sharing confidential information between vendors.

| Category | Vendors in Pipeline | Competitive Awareness | Tension Level | Notes |
|----------|--------------------|-----------------------|---------------|-------|
| Cooling | Vertiv, Schneider | Vertiv knows it is in a competitive process (vendor count disclosed, no names) | MEDIUM | Need to advance Schneider to create real competitive tension |
| Electrical | Schneider | Single vendor -- no competitive tension | LOW | Identify alternative(s) for MV/LV to create leverage |
| EPC Supervision | Hammer, Unica, TBD | Both know they are competing; neither knows the other's identity or pricing | HIGH | Third vendor (Jochem referral) adds additional tension |
| Heat Pumps | Sabru | Single vendor -- no competitive tension | LOW | Identify alternatives before advancing past NDA |
| Generators | Caterpillar | Single vendor -- no competitive tension | LOW | Consider Cummins or MTU as alternatives |
| Containers | None | N/A | NONE | Category requires vendor identification |
| BMS | Schneider (EcoStruxure) | Single vendor -- no competitive tension | LOW | Evaluate open-source alternatives |

**Rule:** Before any vendor reaches SELECTED in a category with tension level LOW or NONE, document the sole-source justification or initiate alternative vendor identification.

---

## SSOT Integration

All vendor lifecycle data flows into and reads from the SSOT:

| Data Type | Location | Update Trigger |
|-----------|----------|---------------|
| Vendor profiles | `procurement/vendor/{vendor-name}.md` | New vendor identified or status change |
| Evaluation matrices | `procurement/evaluations/{vendor-name}.md` | Evaluation completed |
| Meeting notes | `procurement/evaluations/{date}_DE_MoM_{vendor}.md` | After each vendor meeting |
| NDA documents | `contracts/ndas/` (or `contracts/` subdirectory) | NDA signed |
| Contract summaries | `contracts/msas/{vendor-name}.md` | Contract signed |
| RFQ documents | `procurement/rfqs/` (or project-level) | RFQ issued or updated |
| Benchmark data | `procurement/benchmarks.md` | Quarterly or per new data point |
| EPC strategy | `procurement/epc-strategy.md` | Strategy change |

---

## Common Queries & How to Handle Them

### "Where are we with procurement?"
Produce the full vendor pipeline dashboard. Lead with summary metrics (total vendors by stage, overdue count, critical lead time flags). Follow with the full table sorted by category.

### "What's overdue?"
Filter the pipeline to OVERDUE RESPONSE flags. Show vendor, category, what is overdue, days overdue, last follow-up, and recommended next action.

### "Category status for [cooling/electrical/etc.]"
Produce the category-specific view: all vendors in that category with stages, the category parameters (lead time, critical path status, technical requirements owner), competitive tension level, and any flags.

### "Where is [Vendor]?"
Show the vendor's current stage, all active engagements (may be multi-category for vendors like Schneider), NDA status, latest RFQ version received, response status, and evaluation score (if applicable).

### "What needs to be ordered first?"
Produce the lead time critical path registry sorted by order-by date (earliest first). Flag anything in RED or ORANGE status.

### "NDA status"
Produce the NDA registry. Flag any pending NDAs blocking RFQ issuance, and any NDAs approaching expiry.

### "Update [Vendor] to [Stage]"
Verify the exit criteria for the previous stage are met. If yes, update the stage. If not, list the missing criteria and request the evidence. Every stage transition is documented.

### "Procurement report for investor/board"
Produce a summary report: categories with selected vendors, categories still in evaluation, long-lead item status, key risks (sole-source categories, overdue responses), and timeline to procurement completion.

---

## Reporting Cadence

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Full pipeline dashboard | Weekly (Wednesday) | Procurement lead, founders | All vendors, all stages, all flags |
| Category deep dive | On demand or bi-weekly | Engineering + procurement | Category-specific detail, technical evaluation status |
| Lead time alert | Immediate (when threshold crossed) | Project manager, procurement lead | Critical path items approaching order-by deadlines |
| NDA status report | Monthly | Legal, procurement lead | All NDAs with status, approaching expiry |
| Board procurement summary | Monthly | Board/management | High-level category status, key decisions needed, risks |

---

## Cross-Skill RACI Framework

| Cross-Cutting Question | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Vendor stage tracking and pipeline dashboard maintenance | vendor-lifecycle | ops-chiefops | vendor-negotiation, dc-engineering | pipeline-scorer, constraint-engine |
| RFQ version control and response deadline management | vendor-lifecycle | vendor-lifecycle | vendor-negotiation (RFQ content), dc-engineering (technical specs) | ops-dealops |
| NDA tracking, renewal, and compliance | vendor-lifecycle | legal-counsel | vendor-negotiation, executive-comms | ops-chiefops |
| Long-lead item critical path monitoring | vendor-lifecycle | constraint-engine | dc-engineering, site-development | pipeline-scorer, project-financing |
| Evaluation scorecard documentation and traceability | vendor-lifecycle | vendor-negotiation | dc-engineering (technical scoring), financial-model-interpreter (commercial scoring) | pipeline-scorer |
| Competitive tension tracking and information barrier enforcement | vendor-lifecycle | vendor-negotiation | executive-comms | ops-chiefops |

## Companion Skills

- `vendor-negotiation`: Provides negotiation strategy, commercial playbook, and evaluation framework; vendor-lifecycle tracks the execution of that strategy across the vendor pipeline
- `dc-engineering`: Provides technical specifications for RFQ content and technical evaluation scoring; vendor-lifecycle tracks which specs each vendor has received and how they scored
- `constraint-engine`: Consumes vendor lead time data and selection status for cross-project scheduling; vendor-lifecycle flags long-lead items that constrain the critical path
- `pipeline-scorer`: Consumes EPC contractor selection status as a Gate 3->4 scoring criterion; vendor-lifecycle provides current stage data
- `financial-model-interpreter`: Consumes vendor pricing data for CAPEX model updates; vendor-lifecycle tracks which pricing is current and confirmed
- `project-financing`: Vendor selection and pricing feed into lender due diligence requirements; vendor-lifecycle provides the procurement status that lenders need to see
- `legal-counsel`: Reviews NDAs and contracts; vendor-lifecycle tracks NDA status and flags when legal review is needed for stage transitions
- `executive-comms`: Drafts vendor communications; vendor-lifecycle provides the context on what stage each vendor is at and what communication is appropriate

## Reference Files

Key SSOT sources for this skill:
- `procurement/epc-strategy.md` -- EPC contracting structure, hybrid model definition, and scope boundaries
- `procurement/evaluations/` -- Vendor-specific evaluation files with scoring matrices, meeting notes, and decision records
- `procurement/vendor/` -- Vendor profiles, correspondence history, and relationship status
- `contracts/templates/` -- Contract and NDA templates for procurement agreements
- `contracts/ndas/` -- Signed NDA documents (or equivalent location in SSOT)
- `technical/architecture/topology-decision.md` -- SiS topology decision (DEC-2026-004) driving equipment specifications
- `projects/_pipeline.md` -- Pipeline overview for project timeline context driving procurement deadlines

*Last updated: 2026-03-05*
