---
last-reviewed: 2026-03-30
---

# Promise Tracking SOP

Promise log format, escalation rules, and deadline enforcement.

---

## Promise Types

1. **Promises WE made** — Things Carlos/team committed to sending, scheduling, or doing
   - Examples: "I'll send you our technical spec", "Let me intro you to our CTO", "We'll schedule a site visit"
   - Tracked in: ClickUp (via delegation-engine)
   - Escalation: If overdue → notify owner + Carlos

2. **Promises THEY made** — Things the contact committed to doing
   - Examples: "I'll send our requirements doc", "I'll connect you with our procurement team"
   - Tracked in: HubSpot task/note on contact record
   - Follow-up: If not received by expected date → gentle ping email

---

## Promise Log Format

```
PROMISE LOG: [Source/Event Name] — [Date]

PROMISES WE MADE:
| # | To Whom | Promise | Deadline | Status | Owner | ClickUp Task |
|---|---------|---------|----------|--------|-------|-------------|
| 1 | Jan @ Vattenfall | Send technical spec sheet | 24hr | PENDING | Jelmer | CU-1234 |
| 2 | Lisa @ RWE | Intro to our CTO | 48hr | PENDING | Carlos | CU-1235 |

PROMISES THEY MADE:
| # | From Whom | Promise | Expected By | Status | Follow-up Action |
|---|-----------|---------|-------------|--------|-----------------|
| 1 | Jan @ Vattenfall | Send requirements doc | This week | WAITING | Ping Friday if not received |
| 2 | Erik @ Shell | Connect us with procurement | Next week | WAITING | — |
```

---

## Implied Deadlines

- "I'll send you X" with no date → 24hr deadline (professional standard)
- "Let me intro you to Y" → 48hr deadline
- "We'll schedule Z" → 1 week deadline
- "I'll look into it" → 1 week, then gentle ping

---

## Escalation Protocol

| Situation | Action | When |
|---|---|---|
| Promise-we-made overdue by 1 day | Notify owner via ClickUp | Automatic |
| Promise-we-made overdue by 2 days | Escalate to Carlos | Automatic |
| Promise-they-made overdue by 3 days | Send gentle follow-up email | Manual trigger |
| Promise-they-made overdue by 2 weeks | Move to "unlikely to fulfill" | Manual |

---

## Promise Extraction Rules (During W1)

Look for these patterns in all inputs:
- "I'll", "I will", "let me", "we'll send", "we'll schedule"
- "I promised", "I committed to"
- "They said they would", "they offered to", "they'll"
- Handwritten: circled items, starred items, arrows to action items

---

## Partial Fulfillment States

Beyond the existing PENDING/FULFILLED/OVERDUE:

- **PARTIAL:** Some components of the promise delivered, others outstanding. Example: "Send technical specs" -- specs sent but missing cooling section. Track what's delivered vs remaining.
- **RENEGOTIATED:** Original promise replaced with a revised commitment. Capture: original promise, reason for change, new commitment, new deadline. Both parties must acknowledge.
- **SUPERSEDED:** Promise no longer relevant due to changed circumstances. Example: "Send RFQ" superseded by "They're going with a different vendor." Capture reason.
- **DELEGATED:** Promise ownership transferred from original owner to another team member. Track: original owner, new owner, transfer date, reason.

---

## Owner-Unavailable Protocol

When the assigned promise owner is unreachable (vacation, left company, overloaded):

1. Check if promise is within 48 hours of deadline
2. If yes: escalate to Carlos immediately with full context + suggested alternative owner
3. If no: reassign to backup owner per team structure. Default backup: Jelmer for technical, Carlos for commercial
4. Update ClickUp task with reassignment note
5. Notify original owner when they return

---

## Promise Grouping

- Group promises by contact (not by type) for CEO review -- "everything we owe Pieter" is more useful than "all spec-send promises"
- For multi-threaded companies, also show company-level promise summary
- Integration with ClickUp: promises map to ClickUp tasks with tag `promise-[batch-id]` for batch-level filtering
