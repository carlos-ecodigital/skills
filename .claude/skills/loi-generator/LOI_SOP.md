# How to Request an LOI

## What is this?

Digital Energy has three standard LOI templates for different relationship types. Claude generates the document — you provide the brief and review the output.

## Step 1: Tell Claude what you need

Open Claude and say something like:

> "Generate an LOI for [Company Name]. They are [what they do]. They want [what they want from DE]."

**Examples:**
- "Generate an LOI for Lambda. They're a GPU cloud provider, want 10 MW of colocation capacity."
- "Generate an LOI for TechForce Solutions. They're an SI who wants to integrate their managed services with our DEC platform and sell combined solutions to enterprises."
- "Generate an LOI for Meridian AI. They're a small AI startup, want bare metal colocation for training."
- "Generate an LOI for Nordic Advisors. They'll refer enterprise customers to us — referral arrangement."

**The more detail you give, the better the output.** If you know specifics (capacity, territory, timeline, pricing), include them.

## Step 2: Answer Claude's questions

Claude will ask for any missing information:
- Counterparty details (legal name, address, registration number)
- Contact person and signatory
- Commercial specifics (capacity, term, service model)

If you don't know something, say so. Claude will flag it as [TO BE CONFIRMED] in the document.

## Step 3: Review the output

Claude produces a .docx file. **You must review before sending.** Check:

1. **Recital B** — Does the counterparty description sound right?
2. **Clause 3** — Do the commercial terms match what was discussed?
3. **Signature block** — Correct names and titles?
4. **Any [TO BE CONFIRMED] fields** — Fill these in before sending

## Step 4: Send

- Export to PDF if needed
- Send via DocuSign or email for wet signature
- After signing, rename the file: `YYYYMMDD_DEG_LOI-[Type]_[Company]_(SIGNED).pdf`
- Attach to the HubSpot deal record

## Which type is which?

| If the counterparty... | Claude uses |
|---|---|
| Buys compute for their own use (enterprise, AI lab, startup) | **End User** |
| Packages DE capacity with their services to sell to others (SI, MSP, platform company) | **Distributor** |
| Just introduces customers, doesn't deliver services | **Distributor (Referral)** |
| Buys bulk capacity to resell (neocloud, GPU cloud) | **Wholesale** |

You don't need to specify the type — Claude figures it out from your description.

## Questions?

Ask Carlos or Jelmer. The full technical documentation is in the `loi-ncnda-v3` folder in the CEO vault.
