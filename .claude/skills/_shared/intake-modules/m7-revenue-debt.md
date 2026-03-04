# M7: Revenue Model, Unit Economics & Debt Structure

**Module metadata:**
- Questions: 55 (S9: Q9.1-9.20, S10: Q10.1-10.35)
- Priority: S9 all P0; S10 P1 (Q10.1-10.16), P0 (Q10.17-10.21), P1 (Q10.22-10.28), P2 (Q10.29-10.35)
- Track: `[BOTH]` — Seed loads S9 full + S10 light (Q10.17-10.21 only); PF loads full
- Feeds: `SF` `PF` `PE` `CS` `DR` `LC`
- Dependencies: M4 (BESS revenue), M5 (DC revenue), M6 (site data)
- Parallel track: C (Site/Technical)
- Mini-deliverable trigger: After M7 → **Financial Overview Draft** (revenue model + projections summary)

**Seed mode note:** For seed track, ask all S9 questions (revenue model) but only S10 Q10.17-10.21 (cash waterfall + security — 5 of 35 debt questions). Skip S10.1-10.16 and S10.22-10.35 — seed investors need revenue certainty proof, not debt covenant detail.

---

## Section 9: Revenue Model & Unit Economics

### 9.1-9.10 Revenue Model

**9.1** Revenue streams: list all revenue streams with annual revenue estimate per site. `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**9.2** Heat revenue: price per GJ/MWh, volume per year, contract structure (fixed/indexed), customer(s). `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**9.3** DC colocation revenue: price per kW/month or per rack/month, contract duration, escalation mechanism. `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**9.4** BESS grid services revenue: FCR per MW/year, aFRR per MW/year, arbitrage per MW/year (P50 and P90). `CAL` | `P0` | `[RANGE]` | `[BOTH]` | Feeds: `PF` `SF`

**9.5** Revenue phasing: Year 1 (ramp-up), Year 2 (stabilized), Year 3-5 (growth). `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**9.6** Revenue concentration: top customer as % of total revenue? Top 3? `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**9.7** Pricing benchmarks: how does your pricing compare to market? For each stream, provide market reference price. `VAL` | `P0` | `[RANGE]` | `[BOTH]` | Feeds: `SF` `PE`

**9.8** Revenue escalation: annual price escalation assumption per stream (CPI-linked? Fixed %? Market-based?) `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**9.9** Churn and renewal risk: contract expiry dates, renewal assumptions, customer switching risk. `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

**9.10** Revenue sensitivity: top 3 variables driving revenue variance (price, volume, utilization). ±10% sensitivity for each. `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

---

### 9.11-9.20 Unit Economics

**9.11** Per-site unit economics table: Revenue, OPEX, EBITDA, CAPEX, equity IRR, payback period — for each site. `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**9.12** OPEX breakdown per site: O&M, insurance, land lease, grid charges, personnel, other — annualized. `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**9.13** OPEX escalation assumptions: which costs are fixed, which are CPI-linked, which are variable? `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**9.14** Gross margin per revenue stream: heat, DC, BESS — what's the gross margin for each? `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**9.15** Platform overhead: holding company costs (management, legal, audit, corporate) allocated across sites. `CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**9.16** Breakeven analysis: at what utilization/occupancy rate does each site break even? `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**9.17** Unit economics comparison: per-site economics vs. standalone BESS, standalone DC, standalone heat supply. Integration value quantified. `CAL` | `P1` | `[RANGE]` | `[BOTH]` | Feeds: `SF` `PE`

**9.18** Economies of scale: how do unit economics improve from site 1 → site 3 → site 10? What drives the improvement? `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `SF` `PE`

**9.19** Working capital requirements: construction-phase cash flow timing, VAT recovery delays, customer payment terms. `CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**9.20** Cash conversion: time from service delivery to cash receipt per revenue stream. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

---

### Section 9 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| All revenue streams identified with annual estimate | P0 | [ ] |
| Per-site unit economics table complete | P0 | [ ] |
| OPEX breakdown per site | P0 | [ ] |
| Gross margin per revenue stream | P0 | [ ] |
| Breakeven utilization calculated | P0 | [ ] |
| Revenue sensitivity (top 3 variables) | P0 | [ ] |
| Pricing benchmarked against market | P0 | [ ] |

---

## Section 10: Debt Structure & Bankability

**Section metadata:**
- Questions: 35 (Q10.1-10.35)
- Priority: P1 (Q10.1-10.16) · P0 (Q10.17-10.21) · P1 (Q10.22-10.28) · P2 (Q10.29-10.35)
- Track: `[PF]` primary — Seed loads only Q10.17-10.21 (cash waterfall + security)
- Feeds: `PF` `SF` `DR` `LC`
- Dependencies: M4 (BESS DSCR), M5 (DC DSCR), M6 (site data), S9 (revenue model)

**Critical insight:** The investment case template was written as if equity is the only capital source. Project financing has reference knowledge about debt topics but no structured way to surface them during IM production.

---

### Debt Instrument Design

#### 10.1-10.8 Debt Structure

**10.1** Senior debt target: gearing (%), tenor (years), amortization profile (sculpted/annuity/bullet). `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF` `SF`

**10.2** Cost of debt: base rate + spread assumption, benchmark source, comparison to market benchmarks. `CAL` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.3** Interest rate hedging: strategy (swap, cap, collar), % of exposure hedged, tenor of hedge, cost. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.4** Construction financing: separate facility or equity-funded? Drawdown schedule? Commitment fee? `ANS` | `P1` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

**10.5** Bridge-to-term: how does construction facility convert to term loan? Conditions precedent for conversion? `ANS` | `P1` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

**10.6** Mezzanine / subordinated debt: planned? Terms? Provider? Intercreditor arrangement? `ANS` | `P1` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

**10.7** Green bond / sustainability-linked loan: eligibility assessment, potential pricing benefit (greenium). `ANS` | `P2` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

**10.8** Lender landscape: which lenders approached? Status of conversations? `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF` `SF`

---

### Covenants & Reserves

#### 10.9-10.16 Covenant Package

**10.9** DSCR lock-up covenant: target level (1.10-1.15x). Consequence of breach (distribution lock-up). `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.10** DSCR default covenant: target level (1.05x). Consequence of breach (event of default). `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.11** LLCR minimum covenant: target level (1.15-1.20x). Calculation methodology. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.12** DSRA: months of debt service coverage (typically 6). Funding source. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.13** MRA: adequacy calculation methodology, initial funding, annual contribution. `CAL` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.14** Cash sweep: trigger level, sweep percentage, equity floor. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.15** Distribution lock-up conditions: minimum DSRA balance, DSCR above lock-up, no outstanding defaults. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.16** Financial reporting covenants: frequency (quarterly/semi-annual), content requirements, auditor requirements. `ANS` | `P2` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

---

### Cash Waterfall

#### 10.17-10.21 Cash Waterfall & Security

**10.17** Revenue waterfall order: Revenue → OPEX → Senior debt service → DSRA top-up → MRA top-up → Tax → Equity distributions. Confirm or modify. `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**10.18** Trapped cash: where does cash accumulate during distribution lock-up? Interest-bearing? `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

**10.19** Equity cure mechanism: if DSCR breaches covenant, can equity inject cash to cure? Amount limits? Frequency limits? `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**10.20** Step-in rights: lender step-in trigger conditions, direct agreement framework with counterparties. `ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `LC`

**10.21** SPV ring-fencing security package: share pledge, asset pledge, account pledge, assignment of material contracts. `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

---

### Construction Risk for Lenders

#### 10.22-10.28 Construction Questions

**10.22** EPC contract structure: lump-sum turnkey, fixed price, cost-plus? LDs for delay and underperformance? `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF` `LC`

**10.23** EPC contractor: name, credit quality, parent guarantee availability. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.24** Construction contingency: % of CAPEX (lenders typically require 5-10%). Amount. `CAL` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.25** IDC (interest during construction): calculation, funding source (equity or capitalized from facility). `CAL` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.26** Commissioning tests: what tests are required for COD certification? Who certifies? `ANS` | `P1` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

**10.27** Defects liability period: duration (typically 12-24 months), coverage, alignment with performance guarantee. `ANS` | `P2` | `[EXACT]` | `[PF]` | Feeds: `PF` `LC`

**10.28** Construction insurance: CAR/EAR coverage, DSU (delay in start-up) coverage, insurance broker. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

---

### Insurance for Lenders

#### 10.29-10.35 Insurance Questions

**10.29** Insurance broker: appointed? Name? Specialization in energy storage / DC? `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF` `DR`

**10.30** Preliminary insurance quote: obtained? Key terms and conditions? Annual premium? `DOC` | `P2` | `[DOC-REQUIRED]` | `[PF]` | Feeds: `PF` `DR`

**10.31** Coverage scope: construction (CAR/EAR) + operational (PAR/ISR/All-Risk) + machinery breakdown + third-party liability. `ANS` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.32** Key exclusions: degradation, new/unproven chemistries, cybersecurity incidents, terrorism. Document each. `ANS` | `P2` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

**10.33** UL9540A results: available for insurance underwriter? Impact on premium and coverage terms? `ANS` | `P1` | `[BINARY]` | `[PF]` | Feeds: `PF`

**10.34** Annual insurance cost: total, as % of insured value, budgeted in OPEX? `CAL` | `P1` | `[EXACT]` | `[PF]` | Feeds: `PF`

**10.35** Manufacturer warranty insurance: if manufacturer is not investment grade, is warranty insurance available? Cost? `ANS` | `P2` | `[NARRATIVE]` | `[PF]` | Feeds: `PF`

---

### Section 10 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| Cash waterfall specified | P0 | [ ] |
| Security package outlined | P0 | [ ] |
| Step-in rights framework defined | P0 | [ ] |
| DSCR ≥ 1.20x in base case | P1 | [ ] |
| Covenant package defined (lock-up + default levels) | P1 | [ ] |
| EPC lump-sum turnkey or equivalent | P1 | [ ] |
| Insurance broker appointed | P1 | [ ] |
| Insurance programme ≥80% defined | P1 | [ ] |
| Construction contingency ≥5% of CAPEX | P1 | [ ] |

**Critical flag:** If any P0/P1 gate item is missing → **"Not bankable — address before approaching project debt lenders."**
