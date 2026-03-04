# Shared Intake Questions

Questions used across ALL ICPs regardless of track. Phase 0 (triage) and Phase 5 (qualification) are fully shared. Phases 1-4 have shared base questions that are extended by ICP-specific modules in `intake-questions-colocation.md` and `intake-questions-site.md`.

---

## Phase 0: Triage + Ingestion (6 Questions)

### Q0.1 -- Lead Identity
**Text:** "Who is this lead? Give me the company name, person's name, and any links you have -- website, email, LinkedIn."
**Why:** Anchor record for CRM lookup and external research. Without a name, nothing else works.
**Feeds:** All deliverables (anchor field), HubSpot contact/company creation
**Source priority:** CRM > founder input > research

### Q0.2 -- Lead Source
**Text:** "How did this lead come to us? Referral, inbound inquiry, event, outbound response, portal signup?"
**Why:** Source quality is a scoring input. Warm referrals convert 3-5x higher than cold inbound. Also determines follow-up urgency and outreach approach.
**Feeds:** Lead Qualification Score (source quality factor), Recommended Next Actions (outreach approach)
**Options:** Referral (who referred?) | Inbound (website/email/phone) | Event (which event?) | Outbound response | Portal/self-service signup | Advisor introduction | Other

### Q0.3 -- Buyer Type (HARD FORK)
**Text:** "What kind of lead is this? Are they looking to buy compute/colocation capacity, or are they a potential site/heat partner?"
**Why:** This is the Level 1 fork that determines the entire intake path. Gets refined to ICP sub-track.
**Feeds:** Track selection, ICP module dispatch, all downstream deliverables
**Options:** Neocloud (GPU cloud provider) | Enterprise (corporate AI/ML) | Institution (research/government) | Grower (greenhouse operator) | District heating (warmtenet) | Industrial heat (factory/process) | Unsure
**If "Unsure":** Ask: "Tell me more about what they do and what they're looking for. Are they looking for data center capacity, or do they have land/heat demand they want to discuss?"

### Q0.4 -- Meeting Status
**Text:** "Is there already a meeting scheduled? If so, when?"
**Why:** Triggers Mode B (meeting prep) if meeting is imminent (<7 days). Changes the intake priority from thoroughness to speed.
**Feeds:** Mode selection (A vs B), Pre-Meeting Prep (if Mode B), urgency scoring
**Conditional:** If meeting within 7 days → switch to Mode B compressed intake

### Q0.5 -- Existing Materials
**Text:** "Do you have anything from them or about them? Emails, their deck, a website, referral notes, anything."
**Why:** Document-first principle (Guidebook Principle 1). Every document processed before asking questions reduces founder burden and increases accuracy.
**Feeds:** Document ingestion (Phase 0A), gap list reduction
**Processing:** Extract structured answers, mark as `[CAPTURED FROM: document name]`, flag dated materials

### Q0.6 -- Founder Context
**Text:** "What do you already know about them? Any impressions, context, or background -- even informal."
**Why:** Founder brain dump captures tribal knowledge that no CRM or research can surface. Relationship context, personal impressions, deal dynamics.
**Feeds:** Opportunity Brief (section 1, 4, 8), Lead Qualification Score (founder assessment factor), Pre-Meeting Prep

---

## Phase 1: Identity & Context -- Shared Base (3 Questions)

These 3 questions apply to ALL ICPs. Each ICP module adds 2-3 more.

### Q1.1 -- Company Overview
**Text:** "What does [Company] actually do? Core business, size, location."
**Why:** Grounds all downstream analysis. Establishes whether this is a real operating entity with the profile to be a DE customer or partner.
**Feeds:** Opportunity Brief (section 1), HubSpot company record, Lead Qualification Score
**Auto-fill from:** CRM company record, website research, Crunchbase/KvK

### Q1.2 -- Key Contact
**Text:** "Who is our main contact? What's their role and decision-making authority?"
**Why:** Determines whether we are talking to a decision-maker, influencer, or end-user. Critical for scoring and for knowing who else we need to reach.
**Feeds:** Opportunity Brief (section 2), HubSpot contact record, Pre-Meeting Prep (attendees)
**Follow-up if unclear:** "Are they the person who can sign, or do we need to reach someone else?"

### Q1.3 -- Relationship History
**Text:** "Have we interacted with them or their company before? Any prior contact?"
**Why:** Existing relationships change the entire approach -- warm vs cold, context continuity, avoiding repeated pitches.
**Feeds:** Opportunity Brief (section 1), CRM enrichment, outreach approach
**Auto-fill from:** HubSpot activity history, associated contacts

---

## Phase 2: Need & Problem -- Shared Base (4 Questions)

### Q2.1 -- Primary Need
**Text (Colocation Track):** "What are they looking for from us? Capacity, specific specs, timeline?"
**Text (Site Track):** "What's their situation? What are they looking to solve or what's the opportunity?"
**Why:** Core need statement. Everything else is context for this answer.
**Feeds:** Opportunity Brief (section 3), Lead Qualification Score (capacity/grid value), Pre-Meeting Prep (their priorities)

### Q2.2 -- Trigger Event
**Text:** "Why now? What triggered them to reach out or become relevant?"
**Why:** Urgency indicator. Real triggers (contract expiry, regulatory deadline, funding round, gas price shock) predict conversion better than stated interest.
**Feeds:** Opportunity Brief (section 4), Lead Qualification Score (timeline match), Pre-Meeting Prep (why now)

### Q2.3 -- Current Solution
**Text (Colocation Track):** "How are they handling this today? Own infrastructure, cloud, existing colo?"
**Text (Site Track):** "What's their current setup? How are they getting heat/energy today?"
**Why:** Competitive context. Determines switching cost, reference frame, and objection landscape.
**Feeds:** Opportunity Brief (section 7), Pre-Meeting Prep (competitive positioning), icp-profiles.md reference

### Q2.4 -- Pain Severity
**Text:** "How urgent is this for them? Is it a nice-to-have or a must-solve?"
**Why:** Separates tire-kickers from real opportunities. Feeds directly into timeline scoring.
**Feeds:** Lead Qualification Score (timeline match), Opportunity Brief (section 4), prioritization

---

## Phase 3: Technical / Operational -- Shared Base (3 Questions)

### Q3.1 -- Scale
**Text (Colocation Track):** "How much capacity do they need? MW, racks, GPU count -- whatever they've specified."
**Text (Site Track):** "What's the scale? Land area, grid connection size, heat demand -- whatever is known."
**Why:** Scale determines feasibility, site matching, and deal economics. Sub-minimum scale is a disqualification trigger.
**Feeds:** Lead Qualification Score (capacity/grid value), Opportunity Brief (section 3, 5, 9), Validation (benchmark check)

### Q3.2 -- Timeline
**Text:** "When do they need this? What's their deployment or decision timeline?"
**Why:** Timeline match is a top-3 scoring factor for every ICP. Mismatched timelines waste everyone's time.
**Feeds:** Lead Qualification Score (timeline match), Opportunity Brief (section 9), Recommended Next Actions (urgency)

### Q3.3 -- Location Preference
**Text (Colocation Track):** "Do they have a location preference within the Netherlands? Or is geography flexible?"
**Text (Site Track):** "Where are they located? Specific address or region if known."
**Why:** Site matching. DE operates in specific Dutch regions with specific grid availability. Location determines which sites are viable.
**Feeds:** Opportunity Brief (section 5), site matching, grid congestion check, Validation (geography)

---

## Phase 4: Commercial / Financial -- Shared Base (3 Questions)

### Q4.1 -- Budget / Price Sensitivity
**Text (Colocation Track):** "Do they have a budget range or price expectation? What are they paying today?"
**Text (Site Track):** "What are their current energy/heat costs? Any budget constraints?"
**Why:** Price fit is essential. DE must be competitive vs alternatives (hyperscalers, gas, geothermal) for the opportunity to be viable.
**Feeds:** Lead Qualification Score (budget/price fit), Opportunity Brief (section 9), Validation (benchmark)

### Q4.2 -- Decision Process
**Text:** "How do they make decisions like this? Who else is involved? Is there a formal procurement process?"
**Why:** Maps the decision-making unit. Enterprise/institutional/municipal decisions involve multiple stakeholders and longer cycles.
**Feeds:** Lead Qualification Score (decision authority), Opportunity Brief (section 2, 9), Pre-Meeting Prep (stakeholder map)

### Q4.3 -- Contract Expectations
**Text (Colocation Track):** "What contract term are they thinking? Any specific commercial requirements?"
**Text (Site Track):** "What kind of arrangement are they open to? Land lease, partnership, specific terms?"
**Why:** Determines commercial compatibility. DE's model requires long-term commitments (particularly for Site Track partners).
**Feeds:** Opportunity Brief (section 9), Lead Qualification Score, legal routing

---

## Phase 5: Qualification & Fit (4 Questions)

### Q5.1 -- Competitive Landscape
**Text:** "Who else are they talking to? Do we know about other options they're evaluating?"
**Why:** Competitive intelligence drives positioning strategy. Knowing the alternative helps us frame our value correctly.
**Feeds:** Opportunity Brief (section 7), Pre-Meeting Prep (competitive positioning), Lead Qualification Score

### Q5.2 -- Strategic Alignment
**Text (Colocation Track):** "Beyond the immediate need, is there a strategic angle -- EU sovereignty, sustainability reporting, long-term infrastructure planning?"
**Text (Site Track):** "Beyond the immediate economics, is there a strategic driver -- energy transition, ESG, regulatory compliance, business model evolution?"
**Why:** Strategic drivers make deals stickier and less price-sensitive. They also determine which messaging pillar leads.
**Feeds:** Lead Qualification Score (strategic driver), Opportunity Brief (section 6), positioning angle

### Q5.3 -- Obstacles & Concerns
**Text:** "What could kill this? Any red flags, concerns, or blockers you're aware of?"
**Why:** Founder intuition about deal-breakers is often the most accurate signal. Also surfaces hidden constraints.
**Feeds:** Opportunity Brief (section 8), Lead Qualification Score (red flags), Validation (red flag scan)

### Q5.4 -- Founder Confidence
**Text:** "Gut feel, 1 to 5 -- how likely is this to become a real deal?"
**Why:** The founder assessment factor in scoring. Captures all the intangibles that structured questions miss.
**Feeds:** Lead Qualification Score (founder assessment, 5-10% weight), Opportunity Brief (recommendation)
**Scale:** 1 = unlikely, 2 = possible, 3 = decent chance, 4 = strong, 5 = near-certain
