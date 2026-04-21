# Image Ingest — HEIC → JPG tooling protocol

Field-collected artefacts from iPhone operators default to HEIC format. Claude's `Read` tool cannot ingest HEIC directly. Convert first, then read. Document source of truth for this workflow.

## When this fires

- Counterparty sends a brochure, deck, or one-pager as HEIC images (iPhone screenshots or photos).
- Operator provides site photos (DEC site visits, prefab module inspections).
- Any `~/Downloads/*.HEIC` or `~/Downloads/*.heic` that needs to feed Phase 3 source-capture.

Case example: Cerebro Cloud GTC 2026 brochure arrived as 9 HEIC pages from Jonathan's phone (2026-04-17). Converted via `sips`, Read'd each page, extracted 12+ proof points into Recital B.

## One-liner — single file

```bash
sips -s format jpeg input.HEIC --out output.jpg
```

## One-liner — batch

```bash
cd ~/Downloads
for f in *.HEIC; do
  sips -s format jpeg "$f" --out "${f%.HEIC}.jpg" > /dev/null 2>&1
done
```

Lowercase `.heic`:

```bash
for f in *.heic; do
  sips -s format jpeg "$f" --out "${f%.heic}.jpg" > /dev/null 2>&1
done
```

## Post-conversion archival

After conversion + Read:

1. Move originals to Drive: `Fundraise DE/02_Analysis/Counterparty_Research/{slug}/originals/`
2. Move JPGs to Drive: `Fundraise DE/02_Analysis/Counterparty_Research/{slug}/`
3. Reference Drive path in the LOI intake YAML `source_map[pillar_N]: internal:brochure_{YYYYMMDD}_{slug}` (engine accepts this token as tier-2; R-24 warns that tier-1 corroboration is still needed before signing).

## When NOT to convert

- Original metadata is needed (location GPS, EXIF timestamp, device) — `sips` strips most metadata. Use `exiftool` first to preserve, or convert a copy.
- Video files (`.MOV`, `.mp4` from iPhone) — `sips` handles still images only. Use `ffmpeg` or split into frames.
- HEIC is already archived in a format that the downstream consumer can use — unnecessary conversion.

## Related

- `_shared/counterpart-description-framework.md` — brochure-as-tier-2 source handling
- `_shared/fireflies-integration.md` — companion protocol for meeting transcripts
- `legal-assistant/SKILL.md` Phase 3 — source-capture workflow where this fits
