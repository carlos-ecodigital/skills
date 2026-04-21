# Fireflies Integration — call patterns for legal-assistant

Consumed by `legal-assistant` Phase 3 (systematic source capture) and Phase 4.5 (signatory name cross-check).

## Tools used

Both tools are in the `allowed-tools:` of `legal-assistant/SKILL.md`:

- `fireflies_search` — keyword + participant search across transcribed meetings
- `fireflies_get_transcript` — full transcript body for deep extraction

## Phase 3 standard call pattern

For every LOI, Phase 3 invokes these three searches in parallel, in addition to the rest of the source-capture bundle:

```
fireflies_search keyword:"{counterparty}" limit:10
fireflies_search keyword:"{signatory_last_name}" limit:10
fireflies_search participants:@{counterparty_domain} limit:10
```

`limit:10` is the default. Widen to `limit:25` only when the counterparty is a long-standing partner with heavy meeting history — Phase 3 costs scale linearly with limit.

## Phase 4.5 signatory cross-check pattern

Before writing the intake YAML:

1. `fireflies_search participants:@{counterparty_domain} limit:25` across the last 365 days.
2. For each hit, extract the distinct `{displayName, email}` pairs.
3. Fuzzy-match the user-supplied `signatory_name` against the observed set on surname.
4. If no match → prompt the operator with observed names and require explicit confirmation before writing YAML.

Failure mode to escalate: domain-surname homonyms. When the signatory surname shares letters with the counterparty domain (e.g., `Marin Barrage` vs `Marin Bakša @barrage.net`), the user-supplied name is often a transcription of the domain rather than the person's actual surname. Always escalate.

## `fireflies_get_transcript` — when to fetch

Only fetch full transcript when:

- Phase 3 `search` hit returns a preview that mentions commercial terms (MW, capacity, timing).
- Phase 6 evidence-strength review needs direct-quote corroboration for a pillar at Tier-2 or below.
- Operator explicitly asks to mine a specific meeting.

Never blanket-fetch every hit — transcripts are large (~10k chars) and burn context.

## Caveats

- **Fragmentary transcripts:** noisy calls (low-audio, off-mic participants) produce truncated text. Always cross-reference Fireflies extractions against email threads (Gmail MCP) before treating as canonical.
- **Participant aliasing:** Fireflies records display names as they appear in the meeting title, which may include company suffix (`"Marin Bakša (Barrage)"`). Strip the parenthetical before fuzzy-matching.
- **Rate limits:** `fireflies_search` handles high-fanout well; `fireflies_get_transcript` does not — serialize transcript fetches when pulling more than two.

## Related docs

- `legal-assistant/SKILL.md` — Phase 3 source-capture protocol + Phase 4.5 cross-check
- `_shared/counterpart-description-framework.md` — how Fireflies-observed facts flow into Recital B as categorical descriptors
