> Pattern: Decision | See meeting-pattern-decision.md

# Procurement Decisions — Run of Show
**Weekly | 30-60 minutes | 6 attendees max**

**Attendees:** Yoni, Jelmer, Jeroen, Jochem, DJ, + 1 as needed
**Carlos:** Attends only when a CAPEX gate decision or strategic vendor choice is on the agenda.

---

## [0:00 - 0:05] STATUS DASHBOARD (Jeroen reads)

**Vendor Response Tracker:**
| Vendor | RFQ Sent | Response | Status | Next Action |
|--------|----------|----------|--------|-------------|
| [name] | [date] | YES/NO | [status] | [action + deadline] |

**CAPEX Tracker:**
| Category | Budget | Current Estimate | Delta | Flag |
|----------|--------|-----------------|-------|------|
| [category] | [amount] | [amount] | [+/-] | GREEN/YELLOW/RED |

**Timeline Tracker:**
| Milestone | Target Date | Status | Risk |
|-----------|------------|--------|------|
| [milestone] | [date] | On Track / At Risk / Delayed | [1 sentence] |

*No discussion during dashboard read. Questions after.*

---

## [0:05 - 0:40] DECISION BLOCKS (3-4 items, 8 min each)

**Decision 1: [Topic]** — Owner: [name]
```
[0:00-0:01] CONTEXT: What's the decision? (1 sentence)
[0:01-0:03] OPTIONS: A, B, or C (1 sentence each, with cost/timeline impact)
[0:03-0:06] DISCUSSION: Input from relevant people
[0:06-0:08] DECISION: Owner decides. Group commits. Yoni records.
```

**Decision 2: [Topic]** — Owner: [name]
*(Same 8-min format)*

**Decision 3: [Topic]** — Owner: [name]
*(Same 8-min format)*

**Decision 4: [Topic]** — Owner: [name]
*(Same 8-min format)*

---

## [0:40 - 0:45] WORKSHOP SCHEDULING

Items that need >8 minutes of technical discussion do NOT belong in this meeting. Schedule them as separate Procurement Workshops (see `meeting-pattern-workshop.md`).

| Topic | Required Attendees (max 6) | Proposed Time | Output Artifact |
|-------|---------------------------|---------------|-----------------|
| [topic] | [names] | [day/time] | [document / decision brief / design] |

*Workshops are scheduled on demand, not recurring. Each needs a defined output artifact.*

---

## [0:45 - 0:50] CLOSE (Yoni or Jeroen)

- Read back all decisions made
- Read back all action items with owners + deadlines
- Confirm scheduled Workshops with attendees and output expectations
- Preview next week's expected decision items

---

## Rules

- **This is a Decision meeting, not a Workshop.** If a topic needs exploration, brainstorming, or technical deep-dive, schedule a Procurement Workshop. The test: "Do we have options to choose between?" If yes, decide here. If no, it's not ready.
- **8 minutes per item, enforced.** If it needs more time, it needs a Workshop first to produce the options.
- **Bring options, not problems.** If you have a blocker, bring 2 solutions.
- **Vendor follow-ups are async.** Don't spend meeting time composing emails.
- **If it's not on the agenda, it waits.** Add it to next week's decision queue.

---

## When to Schedule a Procurement Workshop

A Workshop is needed when:
- A technical comparison requires >8 minutes (e.g., N+1 vs 3+1 redundancy analysis)
- A vendor evaluation needs detailed spec-by-spec scoring
- A design decision affects multiple downstream systems
- The team needs to produce a document (RFQ, evaluation matrix, decision brief)

Workshop rules: max 6 people, defined output artifact, no time limit but substance checked. See `meeting-pattern-workshop.md`.
