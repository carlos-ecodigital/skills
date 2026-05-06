# Secondary Questions — Airbnb worked example (Q-FOUND-2/3, Q-CO-7/8/9, Q-PROG-1/2/3/9/11/12)

These questions are moderate-leverage. Drafts are tighter (50-100 words each) but follow the same atom-citation discipline.

---

## Q-FOUND-2 — Technical work attribution

**Form text:** "Have any of you written code, or done other technical work on your product? If you have, which of [it] was done by a non-founder? Please explain."

### v-raw
Yes. Nathan (CTO) has written all production code for airbedandbreakfast.com — payment integration (PayPal), listing flow, search, booking system, host/guest profiles. No non-founder has written any production code. Joe and Brian designed the UI/UX (industrial design backgrounds — they sketch and prototype, then Nathan builds). Hosting infrastructure (AWS) configured by Nathan. No outsourced engineering, no contractors.

### Citations
- [atom: ALTMAN-006] ≥1 builder requirement — Nathan satisfies; explicit
- [atom: FAQ-002] outsourcing-product anti-pattern — explicitly NOT us
- [atom: PG-009b] internal-language register — describing what each founder actually did, not "leveraging cross-functional capabilities"
- [fact: company-facts.md#what-built]

### Gates: PASS — explicit Yes, named builder, no outsourcing, internal-language register.

---

## Q-FOUND-3 — Looking for co-founder

**Form text:** "Are you looking for a co-founder?"

### v-raw
No. Brian, Joe, and Nathan are the founding team — three founders, balanced (two designers + one engineer per ALTMAN-006 builder + seller split). Brian and Joe are college roommates (4 years pre-founding); Nathan joined early 2008 from his Datamine exit. We met Nathan via mutual networks; we'd known of his Datamine work for 2 years before approaching him.

### Citations
- [atom: ALTMAN-005] pre-existing relationship — Brian/Joe = 4 years; Nathan via mutual networks (qualified, not random)
- [atom: ALTMAN-006] skills split satisfied
- [atom: CALDWELL-016] co-founder matching N/A — already have technical talent
- [fact: company-facts.md#co-founder-relationship]

### Gates: PASS — explicit No with rationale, relationship duration named.

---

## Q-CO-7 — What your company is going to make

**Form text:** "What is your company going to make? Please describe your product and what it does or will do."

### v-raw
We've built airbedandbreakfast.com — an online marketplace where travelers book a spot in a stranger's home (couch, air mattress, spare room, or whole apartment) for a night or longer, instead of a hotel. Hosts list their space with photos, set price, define availability. Travelers search by destination + date + price, view reviews, book via PayPal. We hold payment in escrow until check-in. Service fee: 3% guest, 3% host. Currently US-only; ~10,000 listings.

### Citations
- [atom: HALE-002] lead with what — opens with "marketplace where travelers book"
- [atom: HALE-006] noun-verb-object — "marketplace [for] travelers [to] book rooms"
- [atom: HALE-005] no marketing-speak — concrete mechanics, no "platform/empower/transform"
- [atom: ARC-022] flaws acknowledged — "currently US-only" (limitation, not hidden)
- [fact: company-facts.md#detailed-description] [fact: company-facts.md#business-model-monetization]

### Gates: PASS — concrete, partner-readable, mechanics specific, geographic limitation acknowledged.

---

## Q-CO-8 / Q-CO-9 — Location

**Form text:** "Where do you live now, and where would the company be based after YC? (City A, Country A / City B, Country B)" + "Explain your decision regarding location."

### v-raw
**Currently:** San Francisco, USA / San Francisco, USA / San Francisco, USA. **After YC:** all three founders stay in San Francisco. We chose SF before YC because hosts and travelers in SF are early adopters; the network effects of a marketplace require dense early geography. Post-YC we expand inventory beyond SF but founder location stays SF — partners we want to work with, technical talent we want to hire, and the customer-discovery loop all live here.

### Citations
- [atom: ARC-016] PG SV advice — superior investor experience and specialized resources
- [atom: PG-004 multi-path live-in-future] — demographic-insider in target city; SF already part of the founders' lived experience
- [fact: company-facts.md#location]

### Gates: PASS — explicit SF commitment, mechanism named (network effects + talent + investors), no hedging.

---

## Q-PROG-1 — How far along

**Form text:** "How far along are you?"

### v-raw
Production marketplace live for 14 months. ~10,000 listings, ~3,000 active hosts (booking in last 60 days). $13.4k April 2009 net revenue, ~33% mo/mo growth. Major launches: SF (origin Oct 2007), DNC Denver (Aug 2008 — proved event-overflow model). Cereal-box bridge financing kept us alive through investor "no" period (Oct-Nov 2008, $30k revenue from limited-edition Obama O's / Cap'n McCain's). Three founders full-time since early 2008; living frugally; ~4 months runway.

### Citations
- [atom: ARC-019] metric priority — revenue (highest tier we have) leads
- [atom: ALTMAN-008] do things that don't scale — cereal boxes are the canonical hand-rolled hack
- [atom: ARC-013] show what you've done — concrete shipped artifacts named
- [atom: SEIBEL-002] PMF self-knowledge — implicit in honest figures, not over-claimed
- [fact: company-facts.md#traction] [fact: company-facts.md#revenue-trajectory]

### Gates: PASS — concrete dates, specific dollar figures, named launches, runway honest.

---

## Q-PROG-2 — Full-time / time spent

**Form text:** "How long have each of you been working on this? How much of that has been full-time? Please explain."

### v-raw
Brian and Joe: 19 months total (since October 2007), full-time since January 2008. Nathan: 16 months, full-time since joining in early 2008. All three have been 100% Airbnb since respective full-time start dates — no side projects, no part-time consulting, no other jobs. Living frugally to extend runway; the cereal-box hack was funded by personal credit and lived inventory in our apartment, not by other paid work.

### Citations
- [atom: FAQ-003] full-time commitment expected
- [atom: ANTI-008] day-job hedging — NOT triggered (explicit zero side-work)
- [fact: company-facts.md#time-commitment]

### Gates: PASS — explicit dates, explicit "no side-work," clean commitment signal.

---

## Q-PROG-3 — Tech stack

**Form text:** "Which tech stack are you using, or planning to use, to build this product? Include AI models and AI scaling tools you use."

### v-raw
Rails on AWS EC2. PostgreSQL for relational data. PayPal for payment processing. S3 for listing photos. Memcached for search caching. AI/ML: none currently — search ranking is rule-based (recency + price + reviews). Roadmap: image-quality scoring for listings (likely a vision model in 2009-10 once accessible). Front-end: jQuery + custom CSS. Mobile: not yet (mobile usage was minimal in 2008-9). Repository: private GitHub.

### Citations
- [atom: PG-009b] internal-language register — engineering vocabulary, not marketing
- [atom: ARC-021] specificity — named tech components rather than "modern stack"
- [fact: company-facts.md#tech-stack]

### Gates: PASS — concrete tech named, honest about what's not built (mobile, ML), no buzzword padding.

(Note: 2009 application; Q-PROG-4 coding-agent-session N/A — that question is Summer 2026+ specific.)

---

## Q-PROG-9 — Revenue source breakdown

**Form text:** "Where does your revenue come from? If your revenue comes from multiple sources..."

### v-raw
100% from marketplace take rate (3% guest fee + 3% host fee on each booking). No subscription, no advertising, no consulting, no service revenue. Cereal-box revenue ($30k Oct-Nov 2008) was non-recurring bridge — not counted in this monthly trajectory.

### Citations
- [atom: SEIBEL-003] business-model precision — marketplace not SaaS
- [atom: CALDWELL-013] no misrepresentation — cereal box explicitly excluded
- [fact: company-facts.md#revenue-source]

### Gates: PASS — clean source attribution, non-recurring excluded explicitly.

---

## Q-PROG-11 — Re-applicant

**Form text:** "If you are applying with the same idea as a previous batch, did anything change?"

### v-raw
N/A — first-time application.

(Anti-pattern check: founders who try to manufacture a "we're improving" narrative when they haven't applied before fail trust. Honest "first-time" is correct.)

### Gates: PASS — accurate first-time status.

---

## Q-PROG-12 — Other accelerators

**Form text:** "If you have already participated or committed to participate in an incubator, accelerator or pre-accelerator program..."

### v-raw
None.

### Citations
- [atom: PG-011] address head-on — N/A here (no prior to address)
- [atom: CALDWELL-007] predatory-advisor caution — we have NOT given equity for "YC access" promises
- [fact: company-facts.md#other-accelerators]

### Gates: PASS — accurate status.

---

## Summary

10 secondary-question drafts complete. All pass anti-fabrication + concreteness + brevity gates. Combined with the 6 high-leverage drafts (Q-CO-2, Q-IDEA-1, Q-IDEA-2, Q-IDEA-3, Q-IDEA-5, Q-PROG-5/6, Q-PROG-7/8, Q-VIDEO-1, P-ACC-1, P-ACC-2), total: **16 question drafts** for the Airbnb worked example.

Remaining: factual fills (Q-EQ-1 to Q-EQ-11, Q-CUR-1/2, Q-BATCH-1, P-BASICS-1 to P-BASICS-6, P-ROLE-1 to P-ROLE-5, P-BG-1/2/3, P-SOCIAL-1/2/3, P-ACC-3, P-ACC-4) — see `factual-fills.md`.
