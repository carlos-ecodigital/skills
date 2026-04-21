# LOI Cover Email — Template

Default voice: **short, powerful, collaborative** (Jonathan's Cerebro pattern). Override by supplying different tone-markers.

## Template

```
Subject: {Counterparty} — Letter of Intent

Hi {first_name},

{opening: 1–2 sentences — warm check-in + acknowledge existing joint work. E.g., "Thanks again for the time last week in London — the walk-through of your {site/programme} was genuinely useful." Or, if no recent touchpoint: "Hope things have been moving well on your side since {last_known_milestone}."}

Attached is a Letter of Intent covering {one-sentence purpose — capacity, collaboration scope, programme position}. We see this as supporting the financing required to bring {facilities / capacity / the programme} online alongside a small group of {peer-set — "Neocloud partners" / "enterprise customers" / "strategic suppliers"} we're contracting with in parallel.

It's non-binding aside from confidentiality and non-circumvention. We've placed reasonable [TBC] markers on items we still need to confirm from your side — {2–3 examples, e.g., "the exact entity name and company number, signatory title, and registered address"}.

Let me know if there's anything you'd like to adjust.

Looking forward to building out, contracting, and deploying this capacity for you and our customers.

{signature_block}
```

## Variables

| Variable | Source | Notes |
|---|---|---|
| `{Counterparty}` | Intake YAML `counterparty.name` | Use exact LOI form (no abbreviation) |
| `{first_name}` | Intake YAML `counterparty.contact_name` split on space | Fall back to `signatory_name` if no separate contact |
| `{opening: ...}` | Operator supplies context | If no shared context, default to neutral check-in |
| `{one-sentence purpose}` | Derived from LOI type + Recital A | Strategic Supplier: "our intended supply relationship"; Wholesale: "the colocation capacity we've been scoping"; Distributor: "the GPU-as-a-Service routing we discussed" |
| `{peer-set}` | Context-aware | If counterparty is a Neocloud → "Neocloud partners"; if enterprise → "enterprise customers"; if supplier → "strategic suppliers" |
| `{2–3 examples}` | LOI `[TBC]` items | Pull from the LOI's `[TBC]` markers — show 2–3 that the counterparty actually needs to resolve |
| `{signature_block}` | Operator's standard block | Include title + entity + phone + logo if present |

## What NOT to include

- **Tactical specs** (MW capacity, NVLink generation, specific timing): belongs in the LOI, not the cover. Including them doubles up and reads over-eager.
- **Month-year specifics** ("In March 2026 we…"): ages the email; drop.
- **"Please find attached"**: institutional-cold; replace with a verb that says what the attachment does.
- **Closing with "Best regards / Warm regards"** alone: thin; prefer the "looking forward to building out" line which ties the relationship-future to the instrument.
- **Bulleted lists**: cover emails are prose; bullets break the warmth.
- **Joint announcements at LOI signing**: always frame as deferred to first Designated Site award under MSA. Press at LOI creates premature exposure.

## Iteration guidance

If the operator returns with "shorter" / "tighter" feedback:

1. First cut: the `{2–3 examples}` line (drop to 1 example or remove entirely if the LOI `[TBC]` count is manageable).
2. Second cut: tighten the purpose sentence — remove qualifiers.
3. Third cut: collapse opening + parallel-track frame into one paragraph.

If the operator returns with "warmer" feedback:

1. Expand opening with a personal reference (shared meal, site visit, mutual contact).
2. Add a gratitude line before the close.
3. Use contractions ("we've" not "we have") throughout.

If the operator returns with "more formal" feedback:

1. Remove contractions.
2. Replace "thanks again" opener with "Following our discussion on {date},".
3. Switch closing to "Looking forward to progressing this." (drop the joint-future phrase).

## Related

- `_shared/tone-markers.md` — the voice rules this template assumes
- `templates/loi-cover-email-tone-audit.md` — self-check grid
- `legal-assistant/SKILL.md` Phase 8 — where this template is invoked post-LOI delivery
