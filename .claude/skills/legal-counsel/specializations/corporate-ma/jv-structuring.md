# Joint Venture Structuring

This reference provides clause guidance for joint venture provisions in energy infrastructure and other asset-class JVs. For EPC contract provisions, see `energy-project-finance/epc-contracts.md`.

## 1. JV Structure

- SPV (special purpose vehicle): typically a Norwegian AS, English Ltd, or Dutch BV
- Shareholding: {{PARTY_A_SHARE}}% / {{PARTY_B_SHARE}}%
- Shareholders' agreement governs relationship; company's articles of association aligned

## 2. Governance

- Board composition: {{BOARD_SEATS_A}} directors nominated by Party A; {{BOARD_SEATS_B}} by Party B
- Board chair: alternating or specified party
- Quorum: both parties must be represented
- Voting: simple majority for ordinary matters; unanimous or super-majority for reserved matters

## 3. Reserved Matters

Matters requiring unanimous or super-majority approval:
- Annual budget and business plan
- Capital expenditure above threshold
- Borrowing above threshold
- Changes to scope of business
- Admission of new shareholders
- Dividend policy changes
- Related party transactions
- Material contracts above threshold
- Litigation above threshold
- Insolvency filing
- Amendment to articles of association

## 4. Deadlock Resolution

- Tier 1: escalation to senior executives ({{DEADLOCK_EXEC_DAYS}} days)
- Tier 2: mediation ({{DEADLOCK_MEDIATION_DAYS}} days)
- Tier 3: buy-sell mechanism (Russian roulette, Texas shootout, or sealed bid)
- Alternative Tier 3: independent expert determination for technical deadlocks
- Ongoing obligations during deadlock: status quo; no party may act unilaterally on reserved matters

## 5. Funding Obligations

- Initial equity contributions: proportional to shareholding
- Further funding: pro rata; failure to fund triggers dilution or default buy-out
- Loan funding: shareholder loans on arm's length terms; subordination to third-party lenders
- Cash calls: notice period and mechanism

## 6. Distributions

- Dividend policy: distribute all available cash after debt service, reserves, and capex requirements
- Minimum distribution threshold: {{MIN_DISTRIBUTION}}
- Tax distributions: mandatory distributions to cover shareholders' tax liabilities (if applicable)

## 7. Transfer Restrictions

- Lock-up period: {{LOCK_UP_YEARS}} years from financial close
- Right of first refusal (ROFR): other shareholder has right to match any third-party offer
- Tag-along: minority shareholder can join sale on same terms
- Drag-along: majority shareholder can compel minority to sell on same terms (typically 75%+ threshold)
- Pre-emption: new shares offered first to existing shareholders pro rata

## 8. Exit Mechanisms

- Put option: right of a shareholder to require the other to purchase their shares (trigger events: deadlock, change of control, material breach)
- Call option: right to acquire the other's shares (typically mirror of put)
- Valuation: fair market value determined by independent valuer; methodology specified (DCF, comparable transactions, or agreed formula)
- Payment terms: lump sum or instalments; escrow for disputed amounts

## 9. Non-Compete

- Duration: during JV and {{NON_COMPETE_YEARS}} years after exit
- Scope: same technology, same geography (radius or specified region)
- Exceptions: existing projects, passive investments below threshold

## Drafting Notes

1. **Jurisdiction-specific considerations:** JV structures must comply with local corporate law. See applicable jurisdiction files (`jurisdictions/nl/corporate-law.md`, `jurisdictions/no/corporate-law.md`, etc.) for mandatory governance requirements.

2. **Energy-specific JVs:** For energy asset JVs, align the SHA with the project finance documentation. Lenders will require consent provisions for share transfers, step-in rights, and security over shares. See `energy-project-finance/equity-structures.md`.

3. **50/50 deadlock risk:** Equal JVs require robust deadlock mechanisms. Consider whether the parties genuinely need 50/50 or whether 51/49 with enhanced minority protections would be more functional.
