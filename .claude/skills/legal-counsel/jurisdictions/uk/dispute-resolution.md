# United Kingdom -- Dispute Resolution

## Court System for Commercial Disputes

### Relevant Courts

| Court | Part of | Jurisdiction | When Used |
|---|---|---|---|
| **Commercial Court** | King's Bench Division, High Court | Complex commercial disputes, arbitration challenges, insurance, banking | Most likely forum for NDA disputes involving substantial commercial interests |
| **Technology and Construction Court (TCC)** | King's Bench Division, High Court | Technology, construction, engineering disputes | EPC/construction disputes; potentially relevant for data centre contracts |
| **Chancery Division** | High Court | IP, trusts, insolvency, company law | IP aspects of NDA disputes; breach of confidence claims |
| **Intellectual Property Enterprise Court (IPEC)** | Part of Chancery Division | Lower-value IP disputes (cap GBP 500,000 damages) | Smaller NDA/breach of confidence claims |
| **County Court** | First instance | Civil claims up to GBP 100,000 | Lower-value NDA disputes |

### Appeal Structure

| Level | Court | Standard |
|---|---|---|
| First appeal | Court of Appeal (Civil Division) | Permission required; real prospect of success or other compelling reason |
| Final appeal | Supreme Court (UKSC) | Permission required; point of general public importance |

---

## Exclusive vs Non-Exclusive Jurisdiction

Most English law NDAs specify jurisdiction of the English courts. The distinction between exclusive and non-exclusive matters.

| Type | Meaning | Effect on DE (Swiss AG) |
|---|---|---|
| **Exclusive** | Only the English courts may hear disputes | DE must litigate in England. Cannot bring proceedings in Switzerland. Counterparty also restricted to England. |
| **Non-exclusive** | English courts have jurisdiction, but parties may also sue elsewhere | DE retains option to sue in Switzerland (subject to Swiss court accepting jurisdiction). Counterparty can choose England or elsewhere. |
| **Asymmetric** | One party restricted to England; the other can sue anywhere | Aggressive — check which party benefits. If counterparty has flexibility but DE does not: flag as AMBER. |

**Practical implications of exclusive English jurisdiction for DE:**
- DE would need to instruct English solicitors (and potentially barristers for trial advocacy).
- English disclosure obligations apply (more extensive than Swiss or Dutch discovery).
- English costs rules apply (loser pays — see below).
- Proceedings conducted in English (no language issue for DE).
- Interim injunctions available from the English court (American Cyanamid test — see contract-law.md).

---

## Costs

### The English Rule: Loser Pays

The general rule under CPR Part 44 is that the unsuccessful party pays the successful party's costs. This is different from many civil law jurisdictions where costs recovery is limited to fixed tariffs.

### Costs Bases

| Basis | Standard | When Ordered | NDA Relevance |
|---|---|---|---|
| **Standard basis** | Costs must be (a) **proportionate** to the matters in issue, and (b) **reasonably incurred** and **reasonable in amount**. Doubt resolved in favour of the paying party. | Default order in most cases | This is what DE should expect in a normal NDA dispute |
| **Indemnity basis** | Costs must be **reasonably incurred** and **reasonable in amount**. No proportionality test. Doubt resolved in favour of the receiving party. | Ordered as a sanction for unreasonable conduct, or when contractually agreed | Directly relevant: Stelia cl.9 specifies "indemnity basis" — DE's policy is to negotiate to "reasonable costs" or "standard basis" |

**The practical difference:** On standard basis, a court will disallow costs that are disproportionate even if reasonably incurred. On indemnity basis, proportionality is irrelevant — the receiving party recovers all reasonable costs. The gap can be significant in complex disputes.

**Contractual costs clauses:** English courts will generally enforce contractual provisions for indemnity basis costs (unlike some jurisdictions that override contractual costs provisions). This is why DE's policy to negotiate away "indemnity basis" in NDAs is commercially sound.

---

## Part 36 Offers

A powerful settlement mechanism unique to English civil procedure (CPR Part 36).

### How It Works

1. A party makes a written "Part 36 offer" to settle all or part of the claim.
2. The other party has at least 21 days to accept or reject.
3. If the offer is rejected and the rejecting party fails to beat the offer at trial, **automatic costs consequences** apply.

### Costs Consequences

| Scenario | Consequence |
|---|---|
| Claimant makes offer, defendant rejects, claimant obtains judgment **at least as advantageous** | Defendant pays claimant's costs on **indemnity basis** from date of expiry + interest uplift (up to 10% above base rate) |
| Defendant makes offer, claimant rejects, claimant fails to obtain judgment **more advantageous** | Claimant pays defendant's costs from date of expiry (on standard basis); claimant gets own costs only up to date of expiry |

**NDA dispute relevance:** If DE has a strong NDA breach claim, making an early Part 36 offer creates significant costs pressure on the counterparty. Conversely, if DE receives a Part 36 offer, rejecting it carries material financial risk if DE does not improve on the offer at trial.

---

## Arbitration

### London Court of International Arbitration (LCIA)

| Feature | Detail |
|---|---|
| Seat | London |
| Rules | LCIA Arbitration Rules (current version) |
| Language | English (default) |
| Typical duration | 12-18 months |
| Costs | Registration fee GBP 1,750 + hourly-rate arbitrator fees (not ad valorem) |
| Confidentiality | Proceedings confidential by default under LCIA Rules |
| Appeal | Very limited grounds for challenge (Arbitration Act 1996, s.67-69) |

### ICC Arbitration (London Seat)

- International Chamber of Commerce arbitration with London as seat.
- Common in cross-border commercial contracts.
- Ad valorem fee structure (based on amount in dispute).
- Less confidential than LCIA by default (but parties can agree confidentiality).

### When NDAs Specify Arbitration

Some NDAs specify arbitration instead of court proceedings. Advantages and disadvantages for DE:

| Factor | Court | Arbitration |
|---|---|---|
| **Confidentiality** | Public proceedings (hearings, judgments) | Confidential by default |
| **Speed** | Slower (English court backlog) | Potentially faster (LCIA targets 12-18 months) |
| **Enforcement** | Domestic enforcement straightforward; cross-border depends on treaties | New York Convention: enforceable in 170+ jurisdictions |
| **Interim relief** | Full range of interim remedies available | Limited — may need to apply to court for interim injunction |
| **Cost** | Potentially lower (no arbitrator fees) but English litigation is expensive | Arbitrator fees add cost; but discovery more limited |
| **Appeal** | Full appeal on law and fact | Very limited appeal rights |

**NDA preference for DE:** For NDA disputes, **court proceedings are generally preferable** because:
1. Interim injunctions (the primary NDA remedy) are more effectively obtained from courts.
2. The deterrent effect of public proceedings may be valuable.
3. English courts are experienced with confidentiality and breach of confidence claims.

---

## Enforcement of Swiss Judgments in England

### Post-Brexit Framework

Since 1 January 2021, EU instruments (Brussels Ia Regulation) no longer apply between the UK and Switzerland. The applicable framework depends on the jurisdiction clause:

| Jurisdiction Clause | Applicable Instrument | Enforcement |
|---|---|---|
| **Exclusive** jurisdiction clause designating England | Hague Convention on Choice of Court Agreements 2005 | Recognition and enforcement under the Hague Convention (both UK and Switzerland are parties) |
| **Exclusive** jurisdiction clause designating Switzerland | Hague Convention 2005 | Swiss judgment enforceable in England under the Hague Convention |
| **Non-exclusive** jurisdiction clause | Common law | No automatic recognition. DE would need to bring fresh proceedings in England and rely on the Swiss judgment as evidence (common law rules: Dicey Rule 43) |
| **No jurisdiction clause** | Common law | Same as non-exclusive — no automatic recognition |

**Key point:** If DE obtains a Swiss court judgment against a UK counterparty, enforcement in England is **only straightforward if there is an exclusive jurisdiction clause** (covered by the Hague Convention). For non-exclusive clauses, enforcement requires fresh English proceedings — adding significant cost and delay.

**Practical implication for NDA review:** When reviewing an English law NDA with an English jurisdiction clause, DE should understand that it is committing to the English court system for disputes. If DE wants to preserve Swiss court access, it should negotiate non-exclusive jurisdiction or a Swiss law/jurisdiction clause (per nda-policy-positions.md Section 10.4 governing law stance).

---

## Practical Implications for DE

### Summary: What DE Should Know When Signing an English Law NDA

| Issue | Impact | Action |
|---|---|---|
| **Exclusive English jurisdiction** | DE must litigate in England if dispute arises | Accept for high-stakes counterparties with leverage; push for non-exclusive if possible |
| **Loser pays costs** | Financial risk if DE brings a weak claim (or defends poorly) | Factor into decision to litigate; use Part 36 strategically |
| **Indemnity basis costs** | Higher costs exposure than standard basis | Always negotiate to "reasonable costs" or "standard basis" per DE policy |
| **Interim injunctions available** | DE can seek urgent relief to prevent ongoing disclosure | Positive — the English injunction regime is effective for NDA enforcement |
| **No good faith defence** | Counterparty cannot argue they acted in good faith to excuse breach | Positive for enforcement — clear terms are enforced as written |
| **6-year limitation** | Must bring breach claim within 6 years of breach | Monitor for breaches; do not delay proceedings |
| **Swiss judgment enforcement** | Not automatic unless exclusive jurisdiction clause + Hague Convention | If DE obtains a Swiss judgment, enforcement in England may require fresh proceedings |
| **English solicitors required** | Must instruct English lawyers for High Court proceedings | Budget for this if signing an NDA with exclusive English jurisdiction |
