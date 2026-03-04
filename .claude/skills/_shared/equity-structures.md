# Shared Reference: Equity Structures

*Canonical reference for equity structuring across skills. Used by `seed-fundraising` and `project-financing`.*

---

## 1. Dutch BV Equity Framework

### 1.1 Flex-BV Share Capital

| Parameter | Requirement | Source |
|---|---|---|
| Minimum nominal value | EUR 0.01 per share | Art. 2:178 BW |
| Share type | Aandelen op naam (registered only) | Art. 2:194 BW |
| Share register | Maintained by bestuur; not public | Art. 2:194 BW |
| Share transfer | Notariele akte required | Art. 2:196 BW |
| Multi-class shares | Letteraandelen (A/B/C) permitted | Art. 2:178 BW |
| Pre-emption rights | Statutory voorkeursrecht; 4-week exercise | Art. 2:206a BW |

### 1.2 Share Classes in Infrastructure SPVs

| Class | Dutch Term | Typical Use | Rights |
|---|---|---|---|
| Ordinary | Gewone aandelen | Base equity | Voting + economic |
| Preference | Preferente aandelen | Priority return | Preferred dividend; limited voting |
| Lettered (A/B/C) | Letteraandelen | Investor tranches | Customized per class |
| Profit-sharing certificates | Winstbewijzen | Management incentive | Economic only; no voting |
| Priority shares | Prioriteitsaandelen | Governance control | Enhanced voting |

### 1.3 Distribution Tests (Art. 2:216 BW)

| Test | Description | Responsible |
|---|---|---|
| Balanstest | Distribution may not exceed equity minus legal/statutory reserves | Algemene vergadering |
| Liquiditeitstest | Company must be able to pay debts after distribution | Bestuur |
| Director refusal | Bestuur may refuse even if balanstest passed | Bestuur |
| Clawback | Recipients who knew distribution was improper must repay | Shareholders |

---

## 2. Swiss AG Equity Framework

### 2.1 AG Capital Mechanics

| Feature | Detail | Source |
|---|---|---|
| Minimum capital | CHF 100,000 | Art. 621 CO |
| Paid-in at formation | 20% (min CHF 50,000) | Art. 632 CO |
| Par value minimum | CHF 0.01 | Art. 622 CO |
| Share classes | Ordinary + preference allowed | Statuten |
| Transfer restrictions | Vinkulierung possible | Board approval |
| Conditional capital | For options/warrants (up to 50%) | Art. 653a CO |
| Authorized capital | Board issues new shares (up to 50%, 2-year) | Art. 651 CO |
| Capital band (2023) | Board can adjust within band for 5 years | New reform |

### 2.2 AG vs GmbH

| Feature | AG | GmbH |
|---|---|---|
| VC preference | Strongly preferred | Less common |
| Minimum capital | CHF 100,000 | CHF 20,000 |
| Shareholder register | Private (Namenaktien) | Public at Handelsregister |
| Transfer | Vinkulierung (board) | GM approval required |

---

## 3. Anti-Dilution and Transfer Mechanisms

| Mechanism | Type | Application |
|---|---|---|
| Voorkeursrecht (NL) | Statutory | 4-week exercise on new issuance |
| Full ratchet | Contractual (SHA) | Aggressive; rare in infrastructure |
| Weighted average (broad-based) | Contractual (SHA) | Standard institutional protection |
| Pay-to-play | Contractual (SHA) | Lose protection if decline |
| Tag-along | Contractual (SHA) | Minority follows majority on sale |
| Drag-along | Contractual (SHA) | Majority can compel sale (75%+ typical) |

---

## 4. SHA Key Provisions

| Provision | Dutch Term | Description |
|---|---|---|
| Board composition | Bestuurssamenstelling | Nomination rights per share class |
| Reserved matters | Goedkeuringsbesluiten | Supermajority for key decisions |
| Information rights | Informatierechten | Quarterly + annual reporting |
| Transfer restrictions | Overdrachtsbeperkingen | Lock-up, ROFR, tag/drag |
| Deadlock resolution | Geschillenregeling | Escalation -> mediation -> NAI arbitration |
| Non-compete | Concurrentiebeding | 2-3 years post-exit |
| Distribution waterfall | Uitkeringswaterval | IRR hurdles with promote |
| Funding obligations | Financieringsverplichtingen | Pro rata capital calls |

---

## 5. Distribution Waterfall (Standard Infrastructure)

| Priority | Distribution | Rate | Recipient |
|---|---|---|---|
| 1 | Return of capital | 100% contributed equity | All pro rata |
| 2 | Preferred return | 8-10% IRR compounding | All pro rata |
| 3 | Catch-up | 100% to sponsor | GP/sponsor |
| 4 | Residual split | 80/20 or 70/30 | Investors / sponsor |

### Multi-Tier Waterfall

| Tier | IRR Hurdle | LP Share | GP Share |
|---|---|---|---|
| 1 | 0-8% | 100% | 0% |
| 2 | 8-12% | 80% | 20% |
| 3 | 12-15% | 70% | 30% |
| 4 | >15% | 60% | 40% |

---

## 6. Institutional Investor Requirements

### 6.1 Dutch Pension Funds

| Fund | AUM | Infrastructure Allocation | Source |
|---|---|---|---|
| APG (ABP) | EUR 552B | Target 10% by 2030 | IPE |
| PGGM (PFZW) | EUR 251B | EUR 15B infrastructure | PGGM |
| MN (PMT/PME) | -- | EUR 2.5B infra debt | IPE Real Assets |

### 6.2 Requirements by Type

| Requirement | Pension Funds | Insurers | Infrastructure Funds |
|---|---|---|---|
| SFDR | Art. 8 min; Art. 9 preferred | Art. 8 or 9 | Art. 8 minimum |
| Minimum ticket | EUR 10-50M | EUR 5-25M | EUR 5-100M |
| Return (net) | 6-10% core; 10-15% value-add | 4-7% debt; 8-12% equity | 8-15% equity |
| Duration | 15-30 years | 10-20 years | 7-12 year fund |

---

## 7. Exit Mechanisms

| Route | Timing | Considerations |
|---|---|---|
| Trade sale | 3-7 years post-COD | EV/EBITDA multiples |
| Secondary sale | 5-10 years | Fund lifecycle; LP secondaries |
| Refinancing + recap | 2-5 years post-stabilization | Partial exit via dividend recap |
| IPO | Platform-level | Rare for single asset |
| Put/call options | Per SHA triggers | Pre-agreed valuation |

### Valuation Multiples (NL Infrastructure)

| Asset Class | EV/EBITDA Range | Notes |
|---|---|---|
| Data center (operational) | 18-25x | Location + power premium |
| BESS (operational) | 8-14x | Revenue model dependent |
| Onshore wind | 10-14x | SDE++ value |
| Solar PV | 10-14x | SDE++ value |

---

## Cross-References

| Topic | Reference |
|---|---|
| Full Dutch BV equity structures | `project-financing/references/equity-structures.md` |
| Seed-round cap table mechanics | `seed-fundraising/references/cap-table-guide.md` |
| Swiss AG fundraising specifics | `seed-fundraising/references/jurisdiction-guide.md` |
| SHA drafting | `legal-counsel` skill |

---

*Shared reference -- used by multiple skills. Last updated: February 2026.*
