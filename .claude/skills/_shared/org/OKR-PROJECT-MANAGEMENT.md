# Connecting OKRs to Project Management

**How initiatives and projects drive OKR achievement.**

---

## 1. The Relationship

OKRs define **what** we need to achieve. Project management defines **how** we get there.

```
OKRs (What)                    Project Management (How)
─────────────                  ────────────────────────
2026-O1.KR1
  ↑ supported by
GRTH-Q1-O1.KR1
  ↑ supported by
                               AGRIPORT-02-DEC-PERM (Initiative)
                                 └── Milestones, Tasks, Sprints
```

**Key principle:** OKRs are reviewed in OKR meetings. Projects are managed in project meetings. Do not conflate them.

---

## 2. Methodology: Stage-Gate + Agile

We use a hybrid approach optimised for infrastructure development.

### 2.1 Stage-Gate (Strategic Control)

Major projects pass through defined gates. Each gate requires specific deliverables and a Go/No-Go decision.

**Site Development Gates:**

| Gate | Name | Key Deliverables | Decision Maker |
|------|------|------------------|----------------|
| G0 | Identification | Site screened, initial feasibility | Growth |
| G1 | Control | LOI/Option signed, power + plot secured | CEO |
| G2 | Permitting | All permits obtained | CEO |
| G3 | Financing | Project finance closed | CEO |
| G4 | Construction | EPC contract executed, mobilisation | CEO |
| G5 | Operation | COD achieved, handover complete | CEO |

**Gate Review Format:**
- Deliverables checklist: Complete or not?
- Risk assessment: What could still go wrong?
- Resource request: What is needed for next stage?
- Recommendation: Go / No-Go / Conditional Go

**Rule:** No significant capital deployed before gate approval.

### 2.2 Agile Execution (Weekly Sprints)

Within each stage, work is executed in weekly sprints.

**Weekly Sprint Structure:**

| Day | Activity |
|-----|----------|
| Monday | Sprint planning (30 min per team) |
| Tuesday-Thursday | Execution |
| Friday | Sprint review + retrospective (30 min) |

**Daily Standups (Optional):**
- 15 minutes maximum
- Three questions: What did I do? What will I do? What is blocking me?
- Use for active construction or high-intensity periods
- Skip when not needed

---

## 3. Initiative Structure

### 3.1 What Is an Initiative?

An initiative is a body of work that supports one or more KRs. It has:
- A clear objective
- Defined milestones
- An owner
- A timeline

### 3.2 Naming Convention

**Project-Based Initiatives (Site Development)**
```
Format: [LOCATION]-[##]-[TYPE]-[PHASE]

AGRIPORT-02-DEC-DEV   → Development phase
AGRIPORT-02-DEC-PERM  → Permitting phase
AGRIPORT-02-DEC-CON   → Construction phase
AGRIPORT-02-DEC-COM   → Commissioning phase
```

**Current Project Codes:**
*Current as of 2026-01-22. Update this list when projects are added or retired.*

| Code | Project Name |
|------|--------------|
| AGRIPORT-01-DEC | Rainbow Wieringermeer |
| AGRIPORT-02-DEC | ECW |
| ANDEL-01-DEC | Butterfly Orchids |
| BLEISWIJK-01-DEC | Bunnik Bromelia |
| MOERKAPELLE-01-DEC | EP Flora |
| SCHIPHOL-01-DEC | Schenkeveld Schiphol |
| DEKWAKEL-01-DEC | Powergrow De Kwakel |
| SGRAVENZANDE-01-DEC | Knoppert |
| SGRAVENZANDE-02-DEC | YoungGrow 1 |
| DELIER-01-DEC | Moerman 1 |
| MAASLAND-01-DEC | Senzaro |

**Team-Based Initiatives (Non-Project Work)**
```
Format: [TEAM]-[YEAR]-[##]

GRTH-2026-01  → Growth initiative 1 (e.g., Website Redesign)
PROD-2026-01  → Product initiative 1 (e.g., Heat Offering v2)
CORP-2026-01  → Corporate initiative (cross-functional)
```

### 3.3 Linking Initiatives to KRs

Every initiative must support at least one KR. Document the link:

```
Initiative: AGRIPORT-02-DEC-PERM
Supports: PROJ-Q1-O1.KR1 (Submit 3 permit applications)
Owner: [Name]
Timeline: Q1 2026
```

If an initiative does not support any KR, question whether it should be prioritised.

---

## 4. Milestone Structure

### 4.1 What Is a Milestone?

A milestone is a checkpoint within an initiative. It marks completion of a significant deliverable.

### 4.2 Naming Convention

**Project Milestones (Gate-Aligned)**
```
Format: M-[PROJECT]-G[#]

M-AGRIPORT-02-G1  → Gate 1 milestone (Control secured)
M-AGRIPORT-02-G2  → Gate 2 milestone (Permitting complete)
```

**Initiative Milestones (Sequential)**
```
Format: M-[INITIATIVE]-[##]

M-GRTH-2026-01-01  → First milestone of Growth initiative 1
M-GRTH-2026-01-02  → Second milestone
```

### 4.3 Milestone vs KR

| Milestone | Key Result |
|-----------|------------|
| Binary (done/not done) | Measured on spectrum |
| Internal checkpoint | External accountability |
| Part of a plan | Part of a commitment |
| Managed in ClickUp | Tracked in OKR system |

**Example:**
- Milestone: "Submit environmental assessment" (done or not)
- KR: "Advance permitting from 0% to 100% complete" (progress measured)

---

## 5. ClickUp Integration

*ClickUp schema is directional. Specific workspace URLs, custom field IDs, and view configurations to be added when ClickUp MCP is activated.*

### 5.1 Structure

```
ClickUp Workspace
├── Space: Projects
│   ├── Folder: AGRIPORT-02-DEC
│   │   ├── List: G1-Control
│   │   ├── List: G2-Permitting
│   │   ├── List: G3-Financing
│   │   └── ...
│   └── Folder: [Other Projects]
│
├── Space: Growth
│   ├── Folder: Capacity
│   ├── Folder: Supply
│   └── Folder: Initiatives
│       └── List: GRTH-2026-01 Website Redesign
│
├── Space: Product
│   └── [Similar structure]
│
└── Space: Finance
    └── [Similar structure]
```

### 5.2 Custom Fields

Each task should have:
- **Supports KR:** Link to the KR it supports
- **Initiative:** Which initiative it belongs to
- **Gate:** Which stage-gate (for project work)
- **Sprint:** Which weekly sprint

### 5.3 Views

**For OKR Reviews:**
- Board view grouped by KR
- Filter: This quarter's KRs

**For Sprint Planning:**
- List view grouped by Sprint
- Filter: This week

**For Gate Reviews:**
- Board view grouped by Gate
- Filter: Specific project

---

## 6. Handoff Protocols

### 6.1 Growth → Projects Handoff

**Trigger:** Binding term sheet signed (power + plot secured)

**Deliverables from Growth:**
- Signed term sheet
- Site due diligence package
- Customer requirements document
- Commercial terms summary
- Key contacts and relationship notes

**Handoff Meeting:**
- 60 minutes
- Attendees: Growth lead, Projects lead, relevant team members
- Output: Projects confirms acceptance, timeline agreed

**After Handoff:**
- Growth retains customer relationship ownership
- Projects leads technical delivery
- Weekly sync between Growth + Projects on customer-facing matters

### 6.2 Projects → Growth Handoff (Post-COD)

**Trigger:** COD achieved and commissioning complete

**Deliverables from Projects:**
- As-built documentation
- Operations manual
- Warranty information
- Punch list status (should be zero open items)
- Lessons learned

**Handoff Meeting:**
- 60 minutes
- Attendees: Projects lead, Growth lead, customer (if appropriate)
- Output: Growth confirms acceptance for ongoing relationship

---

## 7. Weekly Sprint Rhythm

### 7.1 Sprint Planning (Monday)

**Duration:** 30 minutes per team

**Agenda:**
1. Review last sprint (5 min) — What was completed? What rolled over?
2. Review KR status (5 min) — Are we on track for the quarter?
3. Prioritise this sprint (15 min) — What must be done this week?
4. Assign and estimate (5 min) — Who owns what?

**Output:** Sprint backlog in ClickUp

### 7.2 Sprint Execution (Tuesday-Thursday)

- Work the backlog
- Update task status as work progresses
- Flag blockers immediately (do not wait for Friday)

### 7.3 Sprint Review (Friday)

**Duration:** 30 minutes per team

**Agenda:**
1. Demo completed work (15 min) — What did we ship?
2. Retrospective (10 min) — What worked? What did not?
3. Preview next sprint (5 min) — What is coming?

**Output:** Tasks marked complete, blockers documented, learnings captured

---

## 8. Reporting

### 8.1 Weekly Project Status

Each project owner provides:

```
PROJECT: [Code] — [Name]
GATE: G[#] — [Name]
STATUS: 🟢/🟡/🔴

PROGRESS THIS WEEK:
• [Completed item]
• [Completed item]

NEXT WEEK:
• [Planned item]
• [Planned item]

BLOCKERS:
• [Issue + owner + needed resolution]

SUPPORTS: [KR reference]
```

### 8.2 Monthly Initiative Review

First week of each month, review all active initiatives:
- On track?
- Blockers?
- Resource needs?
- Still aligned to current KRs?

Sunset initiatives that no longer support active KRs.

---

## 9. Quick Reference

### 9.1 Stage-Gate Summary

| Gate | Name | Key Question |
|------|------|--------------|
| G0 | Identification | Is this site worth pursuing? |
| G1 | Control | Do we have rights to develop? |
| G2 | Permitting | Can we legally build? |
| G3 | Financing | Can we afford to build? |
| G4 | Construction | Are we ready to build? |
| G5 | Operation | Is it ready for customers? |

### 9.2 Sprint Checklist

- [ ] Monday: Sprint planning complete, backlog set
- [ ] Daily: Tasks updated in ClickUp
- [ ] Friday: Sprint review complete, demos done
- [ ] Friday: Blockers escalated if unresolved

### 9.3 Linkage Checklist

- [ ] Every task links to an initiative
- [ ] Every initiative links to a KR
- [ ] Every KR links to an Objective
- [ ] Every Objective links to strategy

---

*Last updated: 2026-01-22*
