# OKR Guidelines

**A framework for moving fast on multi-year infrastructure projects.**

---

## How to Use This Document

**Read first:** Sections 1-3 (Philosophy, Structure, Writing OKRs)
**Reference as needed:** Sections 4-8 (Operations)
**Related documents:**
- TEAMS.md — Team structure and decision rights
- OKR-PROJECT-MANAGEMENT.md — Connecting OKRs to project execution
- OKR-GLOSSARY.md — Terms and definitions
- WAYS-OF-WORKING.md — Culture and communication standards

---

## 1. Philosophy

### 1.1 The Core Tension

We operate at the intersection of two rhythms:

**Startup velocity:** Ship weekly, pivot quickly, bias toward action.
**Infrastructure reality:** Permits take 18 months, sites are irreversible, grid connections require precision.

This is not a contradiction to resolve. It is a duality to master.

OKRs create urgency where speed matters while maintaining discipline where patience is required.

### 1.2 What OKRs Are

- A focus mechanism — what matters most right now
- An alignment tool — how individual work connects to company direction
- A communication system — everyone knows what success looks like
- A learning framework — what we achieved vs. what we attempted

### 1.3 What OKRs Are Not

- A comprehensive task list
- A performance evaluation system
- A replacement for project management
- A way to track everything the company does

### 1.4 The 60/40 Rule

- **60%** of OKRs should be committed (we expect to hit these)
- **40%** of OKRs should be aspirational (stretch goals that push us)

When setting OKRs, explicitly label each as **[Committed]** or **[Aspirational]**.

---

## 2. Structure

### 2.1 Three Levels

```
CONTEXT (Reference — Not Formal OKRs)
├── Vision: Why we exist
├── Strategy: How we win (multi-year thesis)
└── Annual Priorities: This year's strategic bets

COMPANY OKRs (Annual)
├── Owned by: CEO + Leadership
├── Cadence: Set annually, reviewed monthly
├── Maximum: 3-5 Objectives, 2-4 KRs each
│
│   2026-O1: [Objective statement]
│     ├── 2026-O1.KR1: [Key Result]
│     ├── 2026-O1.KR2: [Key Result]
│     └── 2026-O1.KR3: [Key Result]

TEAM OKRs (Quarterly)
├── Owned by: Team Leads (PROJ, GRTH, FIN, PROD)
├── Cadence: Set quarterly, reviewed weekly
├── Maximum: 2-3 Objectives per team, 2-4 KRs each
│
│   GRTH-Q1-O1: [Objective] → Supports 2026-O1
│     ├── GRTH-Q1-O1.KR1 → 2026-O1.KR1
│     └── GRTH-Q1-O1.KR2 → 2026-O1.KR2
```

### 2.2 Naming Convention

**Company OKRs (Annual)**
```
Format: [YEAR]-[O][Number].[KR][Number]

2026-O1       → Company Objective 1
2026-O1.KR1   → Objective 1, Key Result 1
2026-O1.KR2   → Objective 1, Key Result 2
```

**Team OKRs (Quarterly)**
```
Format: [TEAM]-[QUARTER]-[O][Number].[KR][Number]

Teams: PROJ | GRTH | FIN | PROD

GRTH-Q1-O1      → Growth, Q1, Objective 1
GRTH-Q1-O1.KR1  → Growth, Q1, Objective 1, Key Result 1
PROJ-Q2-O1.KR2  → Projects, Q2, Objective 1, Key Result 2
```

**Spoken in conversation:**
- "Twenty-twenty-six O1 KR2"
- "Growth Q1 O1"
- "Projects Q2 KR1"

### 2.3 Alignment Rules

**Every Team KR must link to a Company KR.** Use arrow notation:
```
GRTH-Q1-O1.KR1 → 2026-O1.KR2
```

**Exceptions allowed:** One Team Objective per quarter may be "operational" (team health, process improvement) without direct Company KR linkage. Label these **[Operational]**.

**No orphans:** If you cannot draw a line from work to strategy, either the work should not be prioritized or the strategy is incomplete.

### 2.4 Quarterly Target Interpretation

Quarterly targets are **cumulative**. Q4 target equals the annual target.

**Example:**
- Annual KR: "Increase pipeline from 0 to 500MW"
- Q1 Target: 125MW (cumulative progress)
- Q2 Target: 250MW (cumulative progress)
- Q3 Target: 375MW (cumulative progress)
- Q4 Target: 500MW (annual target achieved)

This approach allows clear progress tracking while maintaining the annual goal.

### 2.5 Transparency

All OKRs are visible to the entire company. No exceptions.

- Company OKRs published to all staff at annual kickoff
- Team OKRs published at start of each quarter
- Weekly status updates visible to everyone
- Scores published at end of each period

---

## 3. Writing Effective OKRs

### 3.1 Objectives

**Format:** [Action verb] + [Qualitative direction] + [Scope]

**Characteristics:**
- Inspirational and memorable
- Directional (clear about what success looks like)
- Achievable but ambitious

**Strong:**
- "Establish ourselves as the partner of choice for hyperscalers"
- "Build a world-class project delivery organization"
- "Achieve financial sustainability"

**Weak:**
- "Grow revenue" — too vague
- "Complete Phase 1 construction" — this is a KR, not an O
- "Improve collaboration" — not measurable

### 3.2 Key Results

**Format:** [Metric] from [Baseline X] to [Target Y]

**Every KR must have:**

- **Baseline** — Where are we today? (Verified number)
- **Target** — Where do we need to be? (Specific number)
- **Owner** — Single accountable person (not a team)
- **Source** — Where does the data come from?

**The newspaper test:** Could an outsider verify this KR was achieved? If not, it is not measurable enough.

### 3.3 KR Quality Checklist

Before finalizing any KR:

- [ ] Measurable by third party
- [ ] "From X to Y" format with baseline and target
- [ ] Outcome, not activity
- [ ] Single owner assigned
- [ ] Data source identified
- [ ] Ambitious but achievable (60-70% confidence)

### 3.4 Confidence Calibration

"60-70% confidence" is abstract. Use this heuristic:

- If you would bet your own money 2:1 that you will hit it → ~65% confidence ✓
- If you would only bet even odds → too easy, stretch further
- If you would not bet at all → too hard, reduce target

### 3.5 Common Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Activity as outcome | "Hold 20 customer meetings" | "Generate €10M qualified pipeline" |
| Missing baseline | "Reach 200MW contracted" | "Increase from 50MW to 200MW" |
| Unverifiable | "Improve satisfaction" | "Increase NPS from 32 to 45" |
| Outside our control | "Customer signs contract" | "Deliver signed proposal to customer" |
| Task list | "Complete 15 items" | "Reduce cycle time from 90 to 60 days" |

---

## 4. Scoring

### 4.1 Scale

| Score | Status | Meaning |
|-------|--------|---------|
| 0.0-0.3 | Failed | Little to no progress |
| 0.4-0.6 | Partial | Made progress, missed target |
| 0.7-0.9 | Achieved | Hit or nearly hit target — **THIS IS SUCCESS** |
| 1.0 | Exceeded | Surpassed target (consider if we aimed too low) |

### 4.2 Calculation

**For spectrum KRs:**
```
Score = (Actual - Baseline) / (Target - Baseline)

Example:
Baseline: 50MW, Target: 200MW, Actual: 150MW
Score = (150 - 50) / (200 - 50) = 0.67 ✓
```

**For binary KRs:**
- 0.0 = not achieved
- 1.0 = achieved
- Use binary sparingly (permits, regulatory approvals)

### 4.3 Aggregation

**Objective score:** Average of its KR scores
**Company score:** Weighted average of Objectives (weights assigned by CEO at start of year)

### 4.4 Scoring and Performance

OKR scores are not directly tied to individual performance reviews.

- Ambitious targets should be safe to set
- Team success matters more than individual scoring
- We evaluate individuals on contribution, initiative, and growth
- We celebrate learning from ambitious misses

---

## 5. Operating Rhythm

### 5.1 Annual Cycle

| When | Activity | Who |
|------|----------|-----|
| November | Strategic review | CEO + Leadership |
| December W1-2 | Draft Company OKRs | CEO |
| December W3 | Leadership alignment | Leadership |
| December W4 | Publish Company OKRs | CEO |
| January W1 | Teams draft Q1 OKRs | Team Leads |
| January W2 | Alignment and publish | All |

### 5.2 Quarterly Cycle

| When | Activity | Who |
|------|----------|-----|
| Q-2 weeks | Draft next quarter Team OKRs | Team Leads |
| Q-1 week | Alignment review | Leadership |
| Q Week 1 | Publish and kickoff | All |
| End of Q | Score and retrospective | All |

### 5.3 Monthly Review

First Monday of each month:

**Format:** 60-minute leadership meeting

**Agenda:**
1. **Scorecard review** (15 min) — Current status of all Company KRs
2. **Red/Yellow deep-dive** (30 min) — What is off track, why, what is needed
3. **Decisions** (15 min) — Resolve blockers, reallocate resources if needed

**Output:** Updated status, documented decisions, actions assigned.

### 5.4 Weekly Rhythm

**Monday 10:00**
- All KR owners update status in ClickUp
- Status: 🟢 Green (on track) | 🟡 Yellow (at risk) | 🔴 Red (off track)

**Monday (same day) for any Red status:**
- Document: What is the issue?
- Propose: What is the solution?
- Request: What do you need?

**Friday**
- Weekly memo summarizing key updates
- Celebrate progress, flag concerns

### 5.5 The 15-Minute Weekly Update

Each team lead answers:
1. **What moved?** — Which KRs progressed?
2. **What is stuck?** — Which KRs are at risk?
3. **What is needed?** — What decisions or resources required?

No deep-dive project discussions. Those belong in project meetings.

---

## 6. Conflict Resolution

### 6.1 Process

When teams have competing priorities or resource conflicts:

1. **DRI decides** — The owner of the relevant Company KR makes the call
2. **48-hour limit** — Resolution must happen within 48 hours
3. **Appeal to CEO** — If DRI decision is contested, CEO makes final call

### 6.2 Escalation Criteria

Escalate to CEO when:
- DRI decision is formally appealed
- Conflict involves irreversible commitments
- Resolution not reached within 48 hours
- Cross-team impact exceeds €1K

---

## 7. Failure Protocol

### 7.1 Early Warning

When a KR falls to Red status:
- Same-day documentation of issue, solution, and ask
- Escalation to leadership if blocking other work
- Weekly tracking until resolved

### 7.2 Zombie KRs

When a KR is clearly going to miss significantly (Month 2+, <50% of target):

**Step 1: KR Owner documents (one paragraph)**
- What happened?
- Planning failure or execution failure?
- Is the outcome still strategically relevant?

**Step 2: CEO decides**

| Option | When to Use |
|--------|-------------|
| **Close** | KR no longer relevant. Score it, document lesson, move on. |
| **Carry Forward** | Still relevant, needs more time. Set adjusted target for next period. Original scored as-is. |
| **Restructure** | Goal is right, KR was wrong measure. Replace with better KR next period. |

**Principle:** Never let a KR quietly die. Force an explicit decision.

### 7.3 Abandonment

All formal abandonment decisions require CEO approval.

To request abandonment:
1. Document why the KR should be abandoned
2. Confirm it cannot be restructured or carried forward
3. Submit to CEO for decision
4. If approved, mark as "Abandoned" with reason documented

---

## 8. Board Reporting

### 8.1 Cadence

Quarterly board meetings receive OKR updates.

### 8.2 Format

**One-page memo + metrics dashboard**

```
BOARD UPDATE — Q[X] 2026

HEADLINES
• [Biggest win this quarter]
• [Biggest challenge or risk]
• [Key decision made or needed]

KEY METRICS
                        Target    Actual    Trend
Pipeline (MW)           [X]       [X]       ↑/↓/→
Contracted Revenue      [X]       [X]       ↑/↓/→
Cash Position           [X]       [X]       ↑/↓/→
Runway (months)         [X]       [X]       ↑/↓/→
Team Size               [X]       [X]       ↑/↓/→

OKR SCORECARD (Company OKRs only)
2026-O1: [Name]
  KR1: [X] → Score: 0.X — [One-line commentary]
  KR2: [X] → Score: 0.X — [One-line commentary]

2026-O2: [Name]
  KR1: [X] → Score: 0.X — [One-line commentary]

ASKS
• [Specific introduction, advice, or approval needed]
• [Maximum 3 items]

NEXT QUARTER PRIORITIES
• [Priority 1]
• [Priority 2]
• [Priority 3]
```

**Rules:**
- Maximum 2 pages
- BLUF: Headlines first, details available if asked
- No surprises: If something is Red, board should know before the meeting

---

## 9. Quick Reference

### 9.1 Anatomy

```
Objective = Qualitative + Inspirational + Directional
Key Result = Baseline → Target + Owner + Source
```

### 9.2 Weekly Checklist

- [ ] Monday 10:00: Update KR status (🟢/🟡/🔴)
- [ ] Red items: Same-day issue + solution + ask
- [ ] Friday: Review weekly memo

### 9.3 Scoring

| Score | Meaning |
|-------|---------|
| 0.0-0.3 | Failed |
| 0.4-0.6 | Partial |
| 0.7-0.9 | **Success** |
| 1.0 | Exceeded |

### 9.4 Golden Rules

1. OKRs focus on change; KPIs track health
2. Measure outcomes, not activities
3. One owner per KR, no exceptions
4. 0.7 is success, not failure
5. If you hit 1.0 every time, you are not stretching

---

*Last updated: 2026-01-22*
