# M8: Equity Structure & Capital Round

**Module metadata:**
- Questions: 36 (S11: Q11.1-11.20, S13: Q13.1-13.16)
- Priority: S11 P0 (8) · P1 (8) · P2 (4); S13 P0 (8) · P1 (6) · P2 (2)
- Track: `[SEED]` primary — PF loads only Q11.3 (equity waterfall), Q11.4 (co-investment), Q11.15-11.16 (yield expectation)
- Feeds: `SF` `PF` `LC` `DR` `TO` `OO` `IR`
- Dependencies: M1 (entity structure), M7 S10 (debt structure), M9 S12 (financial model)
- Parallel track: E (Synthesis — depends on Tracks A-D)

**PF mode note:** When loaded for project finance track, only ask Q11.3 (equity waterfall), Q11.4 (co-investment), Q11.15 (dividend preference), Q11.16 (yield expectation). Skip all other equity/round questions — PF raises project debt, not equity.

---

## Section 11: Equity Structure & Investor Terms

### Liquidation & Anti-Dilution

#### 11.1-11.5

**11.1** Liquidation preference structure: participating preferred vs. non-participating preferred. State founder's position and rationale. `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.2** Anti-dilution protection: broad-based weighted average vs. full ratchet. Which is acceptable? Have you modeled the dilution impact of each under a down-round scenario? `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.3** Equity waterfall: define the full return of capital → preferred return (%) → catch-up (%) → carry split structure. Model with realistic exit scenarios (3x, 5x, 10x). `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF` `LC`

**11.4** Co-investment rights at project level: can seed investors co-invest directly in site SPVs? If yes, on what terms? If no, why not? `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `SF` `PF`

**11.5** Share class mechanics: registered shares vs. bearer shares. Transfer restrictions. Impact on secondary sales and future fundraising. `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

---

### Governance & Control

#### 11.6-11.12

**11.6** Board composition post-investment: how many founder seats, investor seats, independent seats? Observer rights offered? `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.7** Reserved matters: which decisions require investor consent? List specific matters (e.g., debt above threshold, key hires, M&A, related-party transactions, ESOP expansion). `ANS` | `P0` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `LC`

**11.8** Information rights: quarterly financial reporting, annual audited accounts, cap table updates, budget approval, access to management. What is committed? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.9** Drag-along / tag-along rights: thresholds (e.g., 75% drag-along), mechanics, tag-along on secondary transfers. `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.10** ROFR (right of first refusal) on share transfers: exists? Scope? Timeline for exercise? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.11** Founder lockup period post-investment: duration (12-24 months typical)? Exceptions (estate planning, partial liquidity)? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.12** Non-compete provisions: scope (geography, sector, duration) for founders post-investment. `ANS` | `P1` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `LC`

---

### Investor Economics & Returns

#### 11.13-11.20

**11.13** Follow-on investment terms for seed lead: automatic participation right at Series A? Pro rata only? Pre-emption? Repriced or flat? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**11.14** Down-round protection and valuation floor: what mechanisms protect early investors? What is the acceptable minimum valuation floor? `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.15** Dividend preference vs. growth reinvestment policy: infrastructure investors expect 6-8% cash yield from Year 3-5. Can your project economics support this? What is the planned dividend policy? `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `SF` `PF`

**11.16** Infrastructure yield expectation: model cash distributions under base case — when does first distribution occur? What annual yield (% of invested capital) from that point? `CAL` | `P1` | `[RANGE]` | `[BOTH]` | Feeds: `SF` `PF`

**11.17** Pro rata rights: all investors or lead investor only? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**11.18** MFN (most favored nation) clause: if running multiple closes, what are the repricing implications if second close is at lower valuation? Can you absorb the MFN adjustment? `ANS` | `P2` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `LC`

**11.19** Governance during downturns: if 18 months in and below plan, what are the equity cure mechanisms? At what point do investors gain enhanced control rights? `ANS` | `P2` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `LC`

**11.20** Syndication capacity: seed lead's known co-investors and typical syndicate partners. Mapped? Approached? `ANS` | `P2` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `TO`

---

### Section 11 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| Cap table sums to 100% | P0 | [ ] |
| Liquidation preference defined (participating / non-participating) | P0 | [ ] |
| Equity waterfall modeled with 3x/5x/10x scenarios | P0 | [ ] |
| Board composition defined | P0 | [ ] |
| Reserved matters listed | P0 | [ ] |
| Anti-dilution mechanism chosen | P0 | [ ] |
| Dividend policy articulated for infrastructure investors | P0 | [ ] |

**Critical flag:** If founder has not decided on participating vs. non-participating preference → **"Negotiation prep gap — define position before first term sheet conversation."**

---

## Section 13: Capital Structure & Round

### Round Parameters

#### 13.1-13.8

**13.1** Target raise amount: [amount]. What is the minimum viable raise (floor)? What is the maximum (ceiling)? `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**13.2** Pre-money valuation: [amount]. Methodology used (DCF-implied, comparable anchoring, infrastructure fund vs. VC pricing)? `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**13.3** Instrument type: priced equity round, SAFE, convertible note, or hybrid? Rationale for chosen instrument. `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**13.4** Post-money ownership table: founders %, ESOP %, existing SAFEs/notes %, new investors %. Must sum to 100%. `CAL` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC` `DR`

**13.5** Use of proceeds: line-item breakdown of how raised capital will be deployed. Must align with milestones that trigger next round. `ANS` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `DR`

**13.6** Runway from this raise: months of runway at planned burn rate. What milestones are achieved within this runway? `CAL` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**13.7** Existing capitalization: current SAFEs, convertible notes, grants — detail each with terms (cap, discount, MFN, conversion triggers). `DOC` | `P0` | `[DOC-REQUIRED]` | `[SEED]` | Feeds: `SF` `LC` `DR`

**13.8** SAFE/note conversion modeling: at proposed round terms, what is the fully diluted cap table post-conversion? Model all SAFEs converting at their caps. `CAL` | `P0` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

---

### Round Mechanics & Strategy

#### 13.9-13.16

**13.9** Round structure: single close or rolling close? If rolling, what is the timeline? First close minimum? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**13.10** Lead investor: identified? In discussions? What is the lead's typical check size and expected terms? `ANS` | `P1` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF` `TO` `OO`

**13.11** Allocation strategy: how much reserved for lead, how much for followers, strategic allocation for advisors/angels? `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**13.12** Next round trigger milestones: what specific, measurable milestones will make this company ready for the next funding round? Map each milestone to use-of-proceeds line item. `ANS` | `P1` | `[EXACT]` | `[SEED]` | Feeds: `SF`

**13.13** Bridge scenario: if next round is delayed 6 months, what is the bridge plan? Existing investors? New bridge investors? Terms? `ANS` | `P1` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF`

**13.14** Valuation support: if an investor challenges the pre-money valuation, what is your defense? Prepare 3 supporting arguments (comparable transactions, DCF, strategic value). `ANS` | `P1` | `[NARRATIVE]` | `[SEED]` | Feeds: `SF`

**13.15** Legal counsel for round: engaged? Name? Experience with cross-border seed rounds in your jurisdictions? `ANS` | `P2` | `[EXACT]` | `[SEED]` | Feeds: `SF` `LC`

**13.16** Closing timeline: target first close date, final close date. Key dependencies that could delay (regulatory, co-investor timing, document preparation). `ANS` | `P2` | `[EXACT]` | `[SEED]` | Feeds: `SF`

---

### Section 13 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| Target raise amount with floor and ceiling | P0 | [ ] |
| Pre-money valuation with methodology | P0 | [ ] |
| Instrument type decided | P0 | [ ] |
| Post-money ownership table sums to 100% | P0 | [ ] |
| Use of proceeds aligns with milestones | P0 | [ ] |
| Existing SAFEs/notes documented | P0 | [ ] |
| SAFE conversion modeled at proposed terms | P0 | [ ] |
| Next round trigger milestones defined | P1 | [ ] |

**Critical flag:** If use of proceeds does not clearly fund milestones that trigger the next round → **"Raise amount may be insufficient — investors will ask 'what does this money buy you?'"**
