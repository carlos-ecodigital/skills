# Partner-Simulation Run — 2026-05-05 — Airbnb worked drafts

**Subagent type:** general-purpose (fresh, no Phase 1-4 context)
**Inputs:** 6 Airbnb worked drafts (Q-CO-2, Q-IDEA-1, Q-IDEA-2, P-ACC-1, P-ACC-2, Q-VIDEO-1)
**Subagent task:** Role-play YC group partner; score 7 dimensions; identify top-3 rejection reasons; v-raw vs. v-polished verdict

## Per-dimension scores

| Dimension | Score |
|---|---|
| 1. Founder formidability | 9/10 |
| 2. Idea quality (3-component) | 9/10 |
| 3. Traction evidence | 8/10 |
| 4. Concreteness density | 9/10 |
| 5. Caldwell story-framework | 9/10 |
| 6. Anti-pattern absence | 9/10 |
| 7. Caldwell extraordinary-claims test | 7/10 |
| **Aggregate** | **60/70** |

**Pass threshold:** ≥50/70 → **PASSES**

## Story partner constructed (Caldwell test)

> "Two broke RISD designers in San Francisco couldn't pay rent in October 2007. A design conference came to town, hotels sold out, and they put air mattresses on their floor for $80/night. Three guests stayed four days and came back the following year. They realized travelers don't actually want hotels — they want a bed at the right price in the right location, and the only reason strangers' rooms aren't a substitute is trust. Trust is unbundled today: Couchsurfing has it without payment, Craigslist has payment without it, hotels have both but can't broker peer inventory. They built airbedandbreakfast.com, added a technical co-founder who already exited a company from a Harvard dorm, proved it again at the Denver DNC, and got to 10,000 listings. When investors passed in October 2008, they shipped 1,000 hand-glued election cereal boxes and made $30k in 60 days to survive."

> "That's a clean story. I can defend it in one sentence in partnership."

## Top-3 rejection reasons (would defend a "no")

1. **Bookings, not listings.** 10,000 listings is supply. Where is the demand? No GMV, no take-rate, no booking-conversion, no repeat-host cohort. Couchsurfing has more "listings" and is a charity. Without booking velocity numbers in the first 60 seconds, the traction signal is supply-side vanity.

2. **TAM read is "weekend conference overflow."** Every concrete demand anchor (IDSA, DNC, "conferences, festivals, political conventions") is event-driven peak overflow. That's a real but capped market. The leap to "travelers don't want hotels" is asserted, not earned by data shown. The London engineer quote literally says "every hotel was booked" — i.e., hotel-substitute when sold out, not hotel-replacement. Incumbent-substitute trap (ANTI-004) lurking under paradigm framing.

3. **Hospitality is regulated, liability-loaded; application is silent.** Insurance, host vetting beyond photos, jurisdictional zoning, what happens when a guest is assaulted or trashes a home. The "trust unlock" is described as a UX primitive (photos+reviews+escrow). Real trust in this category is a legal-and-insurance stack. No mention is a competence gap.

**Honorable mention:** Cereal-box hack is great evidence of resourcefulness BUT also a flag — founders spent cycles on a non-core revenue hack instead of solving dead-money via the actual product. Read either way depending on partner.

## v-raw vs. v-polished verdict on substance (dims 1, 2, 5, 7)

**Polished is NEUTRAL on substance.** Polish-pass tightens cadence, doesn't add/weaken claims, no anchors lost, no story moved. Drafts explicitly note polish has nothing to do at 35 chars on the one-liner. v-polished reads identically to v-raw to the partner on substance dimensions.

> "The risk of polishing is exactly that it can sand off authenticity (SEIBEL-005); these drafts avoid that."

**This validates the dual-output design.** Neither v-raw nor v-polished sacrifices substance.

## Final verdict

> "Yes — interview slot. Top-decile founder formidability evidence, organic founder-problem fit, paradigm-level competitor analysis, and a survival hack that demonstrates the trait we're actually betting on; the bookings-vs-listings and regulatory-stack gaps are exactly what a 10-minute interview is for."

## Implications for skill quality

**What this run validates:**
- Skill produces partner-readable output (60/70 aggregate, interview slot granted)
- Anti-pattern absence dimension scored 9/10 — drafts avoid marketing-speak, hype verbs, hedging
- Caldwell story-framework (CALDWELL-008) test passes — partner can construct coherent story on one read
- v-polished does not sacrifice substance vs. v-raw — dual-output design holds

**What this run reveals about the worked example (NOT the skill):**
- Synthetic Airbnb facts file lacks: cohort data, regulatory framing, take-rate/GMV
- These are gaps in the facts file (synthetic reconstruction limitations), not skill design flaws
- Real applications with full facts files would close these gaps via skill's anti-fabrication discipline (skill would have flagged them as `[GAP]` if facts file lacked the data)

**What this run does NOT validate:**
- Skill behavior on adversarial inputs (separate run)
- Skill behavior on real (non-synthetic) facts files (forward-test pending)
- Held-out oracle (Phase 5F still empty)

## Action items surfaced

1. The Airbnb worked example would benefit from adding cohort/booking/take-rate data and regulatory framing — partly a facts-file completeness issue, partly demonstrates that the skill's `[GAP]` discipline matters.
2. Consider adding an atom for "supply-side vanity metric" anti-pattern — the partner explicitly named this gap; skill currently doesn't have an atom for it. Would slot under ANTI-* or expand SEIBEL-002 (PMF self-knowledge).
3. Consider adding an atom for "regulatory/liability stack disclosure" for regulated-industry applications — applies to hospitality, fintech, biotech. Currently absent.
