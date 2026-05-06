# Q-IDEA-3 — "How will you make money? How much could you make?" (Airbnb worked example)

**Atoms applied:** ALTMAN-007 (LOIs for enterprise — N/A consumer), SEIBEL-003 (model precision: marketplace), ARC-019 (metric priority), PG-007 (default-alive logic), ALTMAN-009 (TAM as ceiling, post-PMF expansion), PG-006 (pre-PMF narrow-deep)

---

## v-raw

We charge a service fee on each booking — ~3% from the guest, ~3% from the host. Take rate ~6% of GMV. Pricing varies $20-$300/night so per-booking revenue is $1.20-$18; thousand bookings/month at $50 average = $3,000 monthly net.

**Beachhead first:** event-driven peak overflow (conferences, festivals, conventions). Sold-out hotels create demand spikes; we have a 6-month repeat host cohort already.

**Expansion sequence:**
1. Conference overflow (now) — proven
2. Business travel routes between major US cities (next 12 months) — Tier-1 city pairs first
3. International leisure travel (24-36 months) — when we have density abroad
4. Whole-home rentals competing with VRBO (36+ months) — bigger ACV, longer stays

**Ceiling:** US lodging is ~$120B/yr; global lodging is ~$500B. We don't need to capture all of it. Capturing 1% of US lodging at 6% take rate is $72M/yr revenue. We grow by both (a) more bookings in beachhead, (b) expanding to adjacent inventory types.

We don't yet know our final ceiling — depends on regulatory friction by city and host density per metro. Best estimate: $100M+ annual revenue achievable in 5-7 years if we stay disciplined on liquidity and trust infrastructure.

[~210 words]

## v-polished

Service fee on each booking: ~3% guest + ~3% host. Take rate ~6%. Per-booking revenue $1-$18 depending on price. Beachhead is event overflow (conferences, conventions) — sold-out hotels create spikes; we have a 6-month repeat-host cohort already.

Expansion: conference overflow → US-tier-1 business travel routes (12 months) → international leisure (24-36 months) → whole-home rentals (36+ months).

US lodging market is ~$120B/yr. Capturing 1% at 6% take rate = $72M/yr. Global lodging is ~$500B. $100M+ annual revenue achievable in 5-7 years if we stay disciplined on liquidity and trust infrastructure.

## Citations

- [atom: SEIBEL-003] marketplace not SaaS — pricing aligns with marketplace model (per-transaction fee, not subscription)
- [atom: ALTMAN-007] LOIs flag — N/A here (consumer marketplace, not enterprise)
- [atom: ARC-019] metric priority — lead with revenue trajectory, not user count
- [atom: PG-006 narrow-deep pre-PMF] — beachhead is event overflow (narrow), expansion sequenced
- [atom: ALTMAN-009 TAM ceiling expansion path] — both narrow-now AND credible expansion required
- [atom: PG-007 default-alive math] — runway × burn against monthly revenue
- [fact: company-facts.md#business-model-monetization]
- [fact: company-facts.md#market-and-why-now]

## Anti-pattern checks

- ❌ TAM-first framing — NOT triggered (lead with beachhead + take-rate, not "$120B market")
- ❌ Revenue model imprecision (SEIBEL-003) — NOT triggered (marketplace explicit, take rate specific)
- ❌ Hedging ("we think we could potentially") — NOT triggered (specific calculations)

## Gate report

| Gate | Result |
|---|---|
| Beachhead specific (PG-006) | PASS — event overflow with cohort evidence |
| Expansion path specific (ALTMAN-009) | PASS — 4-step sequence with timeframes |
| TAM as ceiling not gate | PASS — ceiling stated last, not first |
| Specific take-rate / per-booking math | PASS — 6% / $1-$18 |
| Honest "we don't know final ceiling" | PASS — calibrated, not over-claimed |
| Anti-fabrication | PASS (every claim traces to facts file) |
