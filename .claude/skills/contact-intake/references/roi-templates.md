# ROI Templates

Report formats for conference/batch ROI tracking (W6).

---

## T+1 Week: Activity Report

```
═══ BATCH STATUS: [Source/Event] — [Date] ═══

INTAKE METRICS:
  Total inputs processed: [N] across [M] formats
  Unique contacts extracted: [X]
  Existing contacts updated: [Y]
  New contacts created: [Z]

TIER DISTRIBUTION:
  Tier A (Hot):      [N] ([%])
  Tier B (Warm):     [N] ([%])
  Tier C (Cool):     [N] ([%])
  Vendor:            [N]
  Competitor:        [N]
  Non-sales:         [N]
  No action:         [N]

MULTI-THREADED COMPANIES: [N] companies with 2+ contacts

FOLLOW-UP STATUS:
  Follow-ups sent:     [X] of [Y] target
  Responses received:  [N]
  Meetings scheduled:  [N]

PROMISE TRACKER:
  Promises we made:    [X] total, [Y] fulfilled, [Z] overdue
  Promises they made:  [X] total, [Y] received, [Z] pending

COMPLETION: [X]% — [N] contacts still unprocessed
```

---

## T+1 Month: Pipeline Report

```
═══ PIPELINE IMPACT: [Source/Event] — [Date] ═══

CONVERSION FUNNEL:
  Contact captured → Follow-up sent:     [X]%
  Follow-up sent → Response received:    [X]%
  Response → Meeting booked:             [X]%
  Meeting → Qualified opportunity:       [X]%

PIPELINE GENERATED:
  New qualified opportunities:  [N] (value: EUR [X])
  Deals advanced to next stage: [N]
  Vendor RFQs initiated:        [N]

RELATIONSHIP VALUE:
  Second meetings held:          [N]
  Introductions received:        [N]
  Intro chains activated:        [N]

TOP PERFORMERS: (contacts that generated most pipeline value)
  1. [Name] @ [Company] — EUR [X] pipeline, [stage]
  2. ...
```

---

## T+3 Month: Revenue Attribution Report

```
═══ REVENUE ATTRIBUTION: [Source/Event] — [Date] ═══

FINANCIAL:
  Pipeline generated:              EUR [X]
  Pipeline weighted:               EUR [X]
  Closed-won attributable:         EUR [X]
  Total investment (travel/booth):  EUR [X]
  Cost per qualified lead:         EUR [X]
  ROI multiple:                    [X]x

STRATEGIC VALUE (non-pipeline):
  Key relationships established:    [list]
  Market intelligence gathered:     [summary]
  Competitive intelligence:         [summary]
  Brand visibility:                 [qualitative]

CROSS-EVENT COMPARISON (if available):
  | Event | Contacts | Tier A | Pipeline | ROI |
  |-------|----------|--------|----------|-----|
  | [Event 1] | [N] | [N] | EUR [X] | [X]x |
  | [Event 2] | [N] | [N] | EUR [X] | [X]x |

RECOMMENDATION: [Attend again / Skip / Change format]
  Rationale: [1-2 sentences]
```

---

## Running CSV Log Format (for small batches of 5 or fewer)

The general-purpose `contacts_log_YYYY.csv` that accumulates all contacts year-round:

```csv
Date Added,Full Name,Company,Position,Email,Phone,LinkedIn,Source Type,Source Detail,Conversation Summary,ICP Track,Tier,Follow-up Status,HubSpot Contact ID,Notes
```

This is a lightweight record of all contacts processed — not a review file, just an audit trail.
