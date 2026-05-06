# Company Facts — Airbnb (synthetic gold standard, reverse-engineered from public 2008-2009 materials)

**Note for skill users:** This is a SYNTHETIC facts file reconstructed from public sources (Founders at Work interview, Brian Chesky's interviews, Paul Graham's "The Airbnbs" retrospective, Crunchbase early-stage data). It is intended as a worked example of what good facts look like AND as a Phase 5 Track B oracle for skill validation. Some details are reconstructed best-effort; this is not a verbatim copy of Airbnb's actual 2009 YC application (which was never publicly released in full).

---

## One-liner
Book rooms with locals, not hotels.

## Detailed description
We've built airbedandbreakfast.com — an online marketplace where travelers book a spot in a stranger's home (couch, air mattress, spare room, or whole apartment) instead of a hotel. Hosts list space; travelers book by date and price. We charge a service fee on each booking. Two sided marketplace; we take liquidity off both sides simultaneously by targeting conferences with sold-out hotels (Democratic National Convention 2008 was our launch).

## Founders

### Brian Chesky — CEO
- **Email:** [redacted]
- **LinkedIn:** [redacted]
- **Equity %:** 33%
- **Time commitment:** 100%
- **Technical founder?** No (industrial designer / RISD)
- **Will commit exclusively to YC for next year?** Yes
- **Education:** Rhode Island School of Design — BFA, Industrial Design, 2004
- **Work history:**
  - Industrial designer, Los Angeles (2004-2007). Small product design projects.
  - Founder, Airbedandbreakfast.com (2008-present)
- **Most impressive thing built/achieved (P-ACC-2):**
  Designed the Pina sport seat for 3DM (200,000 units shipped, sold in 8 countries). Sold the design at age 24.
- **Wildcard hack story (P-ACC-1):**
  When the company ran out of money in late 2008, designed and shipped two limited-edition cereal boxes (Obama O's and Cap'n McCain's) timed to the 2008 election. Sold them for $40 each, made $30k in 2 months, kept the company alive.
- **Things built with URLs (P-ACC-3):**
  - airbedandbreakfast.com — the company
  - 3DM Pina seat — design portfolio
- **Co-founder relationship:** Joe Gebbia is a college roommate from RISD (2004-2007). Have known each other 4 years; lived together for 3.

### Joe Gebbia — CSO (Chief Stuff Officer / co-founder)
- **Email:** [redacted]
- **Equity %:** 33%
- **Time commitment:** 100%
- **Technical founder?** No (industrial designer / RISD)
- **Will commit exclusively to YC for next year?** Yes
- **Education:** Rhode Island School of Design — BFA, Industrial Design + Graphic Design, 2004
- **Work history:**
  - Critbuns (2007) — designed cushion for art-critique sessions. Featured in MoMA store.
  - Founder, Airbedandbreakfast.com (2008-present)
- **Most impressive thing built/achieved (P-ACC-2):**
  Critbuns cushion (2007) — sold in MoMA Design Store. National retail distribution at age 23.
- **Wildcard hack story (P-ACC-1):**
  Same cereal-box story (co-conceived with Brian).
- **Co-founder relationship:** Brian's college roommate.

### Nathan Blecharczyk — CTO
- **Email:** [redacted]
- **Equity %:** 33%
- **Time commitment:** 100%
- **Technical founder?** Yes (Harvard CS)
- **Will commit exclusively to YC for next year?** Yes
- **Education:** Harvard — BSc Computer Science, 2005
- **Work history:**
  - Founded Datamine (2002, while at Harvard) — referral-marketing platform. Sold for "low millions" (per public reports).
  - Engineer, OPNET Technologies (2005-2007).
  - Co-founder, Airbedandbreakfast.com (2008-present)
- **Most impressive thing built/achieved (P-ACC-2):**
  Founded and exited Datamine (referral-marketing platform built while at Harvard) for an undisclosed sum. Built and operated profitably from college dorm room.
- **Wildcard hack story (P-ACC-1):** [GAP: needs founder input]
- **Things built with URLs (P-ACC-3):**
  - airbedandbreakfast.com
  - Datamine (acquired, no longer active)
- **Co-founder relationship:** Joined Brian and Joe in early 2008 after Joe's outreach.

## What's been built
- airbedandbreakfast.com — live marketplace (Rails + AWS)
- Mobile-friendly listing and booking flow
- Payment processing via PayPal
- Listed: ~10,000 listings across major US cities (early 2009)

## Customers / users
- **Active users (current):** ~10,000 listings; thousands of bookings to date
- **Paying customers:** travelers who pay listing-prices + service fee
- **Highest-paying customer:** [aggregate marketplace, no single dominant customer]
- **Named user love-evidence:** "We are not going to slow down" — actual founder line; verbatim user quotes available from early DNC bookings.

## Business model & monetization
- **Category:** Marketplace (two-sided)
- **Pricing:** ~3% guest fee + ~3% host fee on each booking
- **Sales cycle:** instant (transactional)
- **ACV:** highly variable — $20-$300/night

## Market & why now
- **Specific market:** US travel accommodation; ~$120B/yr in 2008
- **Why now (the unrealized shift):** Hotel inventory cannot scale to event-driven demand spikes (conferences, festivals, political conventions). Same-period internet penetration + PayPal-style trust infrastructure makes peer-to-peer rentals feasible for the first time.
- **Why incumbents structurally cannot address:** Business-model conflict — hotels cannot list private homes without cannibalizing inventory pricing. Hotel-room marketplaces (Hotwire, Expedia) cannot list non-hotel inventory without changing their entire supplier-relationship model.
- **Why this team noticed first:** Demographic insider + heavy-user — Brian and Joe were broke RISD grads who rented out their air mattresses to designers visiting San Francisco for an industrial-design conference (October 2007), discovered the demand directly.

## Competitors
- **Couchsurfing:** free, community-led, no payment infrastructure. We charge — which lets hosts professionalize. Couchsurfing actively rejects monetization; that's their organizational conflict.
- **Craigslist:** has a "vacation rentals" section. Unsearchable, unmoderated, no payment trust. Craigslist's structural conflict: their philosophy rejects vertical optimization.
- **VRBO / HomeAway:** vacation-home rentals only (whole-home, multi-day). We do nights. Different inventory.

## Insight (what we understand others don't)
Travelers don't fundamentally want hotels — they want a place to sleep at the right price in the right location. When hotels are sold out, travelers will accept stranger-with-an-air-mattress IF trust infrastructure exists. The trust unlock comes from photos + reviews + payment escrow, all 3 simultaneously. Couchsurfing has trust without payment; Craigslist has payment without trust; the gap is profitable.

## Traction (concrete numbers + dates)
- **Bookings to date:** 10,000+ (early 2009)
- **Major launches:** DNC 2008 (Denver, sold-out hotels) — proved the model under conference demand
- **Cereal box revenue:** $30k in 2 months (Oct-Nov 2008) — bridge financing while building
- **Revenue (from bookings):** [GAP: monthly numbers needed for Q-PROG-8 6-month breakdown]
- **Press coverage:** [GAP: needs specific list]

## Cap table / equity structure
- Brian Chesky 33%, Joe Gebbia 33%, Nathan Blecharczyk 33%, options pool 1%
- Prior investors: none at YC application time (cereal boxes were the only outside money — and that's customer revenue, not investment)
- Total raised: $0
- Cash in bank: $30k (cereal-box revenue residual)
- Monthly burn: ~$5-8k (3 founders living frugally)
- Runway: ~4 months
- Currently fundraising: applying to YC

## Use of proceeds
- Product: continued marketplace development (search, payment trust, mobile)
- Customer acquisition: SF + NYC + Boston launches
- Reserve: 6-month runway extension
- **Specific milestones unlocked:** SF launch, hire 1 engineer, expand to non-conference inventory

## Anything unusual
- Two industrial designers + one CS founder is an unusual team composition for an internet startup
- Cereal box revenue is the most-cited founder anecdote — it's the resourcefulness signal embedded in the company's origin

## Other ideas considered (Q-IDEA-5)
1. **Snooth** — wine-discovery platform (Brian's idea pre-Airbnb). Decided against because the team wasn't wine-experts and wine commerce required regulatory navigation we didn't want.
2. **Conference-scoped travel marketplace** — early version of Airbnb but ONLY for conference attendees. Decided against because it was too narrow; the same trust infrastructure could serve broader travel.

## Re-applicant info
- **Prior YC application:** Yes — applied to W08 with a different idea (Snooth), rejected. Re-applying W09 with Airbnb.
- **What changed since:** completely different idea, different team (added Nathan), shipped product with bookings, cereal-box demonstration of resourcefulness.

## Other accelerators
- None.

## How heard about YC / why applying (Q-CUR)
- **What convinced you to apply:** PG essay "Be Good" + the realization that Airbnb's model fits PG's "schlep blindness" framing — payment trust + photo verification is the schlep that competitors avoid.
- **Have you been to YC events:** No.
- **How did you hear:** PG essays.

## Coding agent session (Q-PROG-4)
N/A — not a Summer 2026 application; coding-agent question didn't exist in 2009. Included only as worked-example reference.
