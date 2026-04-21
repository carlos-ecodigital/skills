# LOI Cover Email — Tone Audit

Self-check grid applied to any draft before delivery. Operator can run this against their own edits; skill runs it against generated drafts.

## Grid

| # | Check | How to verify | Pass/Fail |
|---|---|---|---|
| 1 | **Word count ≤ 200** (Short) | `wc -w` the body; exclude signature | ☐ |
| 2 | **Paragraph count ≤ 5** (Short) | Count paragraphs (blank-line-separated blocks) | ☐ |
| 3 | **No tactical specs** (Short) | Grep body for MW / NVLink / GPU model names / specific dates beyond validity | ☐ |
| 4 | **Active-verb ratio ≥ 80%** (Powerful) | Scan main verbs; passive ("was done by", "will be") should be <20% | ☐ |
| 5 | **Zero hedging words** (Powerful) | Grep for "I think", "we believe", "perhaps", "maybe", "might" — should be 0 | ☐ |
| 6 | **First-person-plural opener** (Collaborative) | First sentence uses "we", "our", "us" not "I", "me", "my" | ☐ |
| 7 | **Joint-future close** (Collaborative) | Final sentence names shared outcome ("for you and our customers" / "together" / "our joint programme") | ☐ |
| 8 | **No generic openers** | No "I hope this finds you well" / "As per our discussion" | ☐ |
| 9 | **No bulleted lists** | Body is prose; no `- ` or `• ` lines | ☐ |
| 10 | **No "Please find attached"** | Attachment verb is specific ("I've attached", "attached is") | ☐ |

## How to run

From the de-executive-comms skill's output, scroll to the bottom — every draft includes an auto-generated audit block. Operator reviews before copying to Gmail.

When operating without the skill (editing a draft manually), run this grid as a mental checklist. If more than two fail, re-apply the relevant tone markers from `_shared/tone-markers.md` and re-draft.

## Common failure patterns

- **#1 (Word count)**: longest offender is usually the parallel-track paragraph. Tighten or collapse with the purpose sentence.
- **#4 (Active-verb ratio)**: legal register bleeds into cover copy. Replace "This LOI has been drafted to…" with "I've drafted this LOI to…" or "This LOI covers…"
- **#5 (Hedging)**: hedging is natural when the operator is unsure about a claim. If true, remove the claim; if false, remove the hedge.
- **#6 (First-person-plural opener)**: "I'd like to follow up…" fails. Replace with "We've appreciated the progress on…" or similar.
- **#7 (Joint-future close)**: "Looking forward to hearing from you" fails — it's ball-in-your-court. Replace with joint-outcome phrasing.
