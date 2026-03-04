# Cap Table Guide -- Seed Round

## 1. Purpose

The cap table is the mathematical backbone of every fundraise. It tracks who owns what, how much dilution each round creates, and what the company is worth. At seed stage, cap table management is about getting the structure right from the start, avoiding errors that compound through later rounds.

## 2. Instrument Selection

| Instrument | Best For | Complexity | Typical Use |
|---|---|---|---|
| SAFE (Simple Agreement for Future Equity) | <EUR 3M rounds, speed, simplicity | Low | 64% of US seed deals (Carta 2025) |
| Convertible Note | Bridge rounds, European structures | Medium | Common in CH/NL for legal familiarity |
| Priced Equity Round | >EUR 5M rounds, institutional investors | High | Required by infrastructure funds / pension funds |
| Hybrid | Mix of instruments across investors | Varies | Common in practice |

### SAFE Mechanics

| Term | Description | Typical Seed Range |
|---|---|---|
| Valuation cap | Maximum pre-money valuation at conversion | EUR 5-20M |
| Discount | Reduction to next-round price | 15-25% |
| Pro rata right | Right to invest in next round | Standard; may exclude angels |
| MFN (Most Favored Nation) | Gets best terms of any subsequent SAFE | Standard |
| Post-money SAFE (YC standard) | Dilution calculated on post-money basis | Increasingly standard |

**Post-money SAFE math:**
```
Ownership % = SAFE Amount / Post-Money Valuation Cap
```
Example: EUR 500K SAFE with EUR 10M post-money cap = 5.0% ownership at conversion.

### Convertible Note Mechanics

| Term | Description | Typical Range |
|---|---|---|
| Principal | Amount invested | Per investor |
| Interest rate | Annual accrual on principal | 2-8% |
| Maturity date | When note becomes due | 18-24 months |
| Valuation cap | Maximum conversion valuation | EUR 5-20M |
| Discount | Reduction to qualified financing price | 15-25% |
| Qualified financing | Minimum raise that triggers conversion | EUR 1-3M |

**Note**: In CH and NL, convertible notes are more legally familiar than SAFEs. Consider local counsel preference.

### Priced Round

| Term | Description | Typical Seed |
|---|---|---|
| Pre-money valuation | Company value before investment | EUR 5-15M |
| Post-money valuation | Pre-money + investment amount | EUR 6-20M |
| Share price | Pre-money / fully diluted shares | Calculated |
| Share class | Preferred vs. ordinary | Series Seed Preferred |
| Liquidation preference | Priority in exit | 1x non-participating |
| Anti-dilution | Protection against down rounds | Broad-based weighted average |
| Board seat | Investor representation | 1 seat typical at seed |
| Pro rata rights | Follow-on investment right | Standard for leads |

## 3. Cap Table Structure

### Pre-Seed (Before This Round)

| Shareholder | Shares | % Ownership | Notes |
|---|---|---|---|
| Founder 1 | {{SHARES}} | {{%}} | |
| Founder 2 | {{SHARES}} | {{%}} | |
| Founder 3 (if any) | {{SHARES}} | {{%}} | |
| Angels / Pre-seed | {{SHARES}} | {{%}} | SAFEs or shares |
| ESOP (reserved) | {{SHARES}} | 10-15% | Unallocated pool |
| **Total** | **{{TOTAL}}** | **100%** | Fully diluted |

### Post-Round (Pro Forma)

| Shareholder | Pre-Round % | Post-Round % | Dilution |
|---|---|---|---|
| Founders (combined) | {{%}} | {{%}} | -{{%}} |
| Pre-seed investors | {{%}} | {{%}} | -{{%}} |
| ESOP pool | {{%}} | {{%}} | May increase |
| **Seed investors** | **0%** | **{{%}}** | New |
| **Total** | **100%** | **100%** | -- |

### Dilution Guidelines (Altman Framework)

| Round | Typical Dilution | Altman Guidance |
|---|---|---|
| Pre-seed / angels | 5-10% | -- |
| Seed | 10-20% | ~10-15% |
| Series A | 15-25% | ~15-25% |
| ESOP pool | 10-15% total | 10% to first 10 employees, 5% to next 20 |

**Target**: Founders should retain >50% after seed round (combined). Below 40% becomes concerning for Series A investors.

## 4. ESOP / Option Pool

| Element | Recommendation |
|---|---|
| Pool size at seed | 10-15% of fully diluted shares |
| Vesting schedule | 4-year vest, 1-year cliff, monthly thereafter |
| Exercise price | Fair market value at grant date (409A / independent valuation) |
| Swiss considerations | ESOP under Swiss Code of Obligations; tax at exercise |
| Dutch considerations | SAR (Stock Appreciation Right) or Option plan; wage tax at exercise |

## 5. Swiss AG Cap Table Specifics

| Element | Swiss AG Rules | Notes |
|---|---|---|
| Minimum share capital | CHF 100,000 (20% paid-in at formation) | Art. 621 CO |
| Par value minimum | CHF 0.01 per share | Art. 622 CO |
| Share classes | Allowed: ordinary + preference | Statuten define rights |
| Share register | Maintained by board | Registered shares (Namenaktien) |
| Transfer restrictions | Possible via Statuten (Vinkulierung) | Board can restrict transfers |
| Capital increase | Requires notarized GM resolution | Handelsregister filing required |
| Conditional capital | For options/warrants (up to 50% of existing capital) | Art. 653a CO |
| Authorized capital | Board can issue new shares (up to 50%, 2-year limit) | Art. 651 CO |

## 6. Dutch BV Cap Table Specifics

| Element | Dutch BV Rules | Notes |
|---|---|---|
| Minimum share capital | EUR 0.01 (Flex-BV) | Art. 2:178 BW |
| Share classes | Letteraandelen (A/B/C classes) | Customizable rights per class |
| Share register | Maintained by bestuur | Not public |
| Transfer | Notariele akte required | Art. 2:196 BW |
| Pre-emption rights | Statutory (Art. 2:206a BW) | 4-week exercise period |
| Distribution test | Balanstest + liquiditeitstest | Art. 2:216 BW |

See `_shared/equity-structures.md` for comprehensive Dutch BV and Swiss AG share structuring, anti-dilution mechanisms, SHA provisions, and distribution waterfalls.

## 7. Dual-Entity Structure (CH Holding + NL Operating)

For Digital Energy Group AG structure:

```
Digital Energy Group AG (Zug, CH) -- Holding
  |
  |-- [Seed investors invest here]
  |-- ESOP at AG level
  |
  +-- Project BV 1 (NL) -- Site 1 operations
  +-- Project BV 2 (NL) -- Site 2 operations
  +-- Project BV 3 (NL) -- Site 3 operations
```

| Consideration | Guidance |
|---|---|
| Where do investors buy shares? | Swiss AG level (holding) |
| Tax on dividends CH -> investors | Swiss WHT 35% (reclaimable under treaty for qualifying investors) |
| Participation exemption | CH: Beteiligungsabzug on dividends from BV to AG |
| NL -> CH dividend | NL WHT 15% (reduced to 0% under EU PSD or CH-NL treaty) |
| ESOP jurisdiction | Swiss AG options (conditional capital) |
| Project-level investors | If needed, co-invest at BV level alongside AG |

## 8. Common Mistakes

| Mistake | Impact | Fix |
|---|---|---|
| No ESOP pool created | Seed investors force it at Series A, diluting founders | Create 10-15% pool before seed |
| Unclear share classes | Disputes at exit | Define rights in Statuten/articles at formation |
| Missing pro rata rights | Early investors can't protect position | Include in SAFE/note/SHA |
| Over-promising board seats | Governance gridlock | 1 investor seat maximum at seed |
| Ignoring WHT in dual-entity | Unexpected tax leakage | Structure with treaty benefits from Day 1 |
| Cap table kept in head | Errors compound | Use a spreadsheet from Day 1. Consider Carta/Ledgy/Pulley. |

---

## Cross-References

| Topic | Reference |
|---|---|
| Equity structures, anti-dilution, SHA, waterfalls | `_shared/equity-structures.md` |
| Institutional investor requirements | `_shared/investor-landscape.md` |
| Swiss tax considerations | [references/jurisdiction-guide.md](jurisdiction-guide.md) |
| Financial model integration | [references/financial-projections.md](financial-projections.md) |
| Investment memo structure section | [references/investment-memo-guide.md](investment-memo-guide.md) |
