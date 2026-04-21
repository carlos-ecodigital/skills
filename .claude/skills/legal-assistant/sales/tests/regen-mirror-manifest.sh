#!/usr/bin/env bash
# v3.5.8 PRINCIPLES.md tripwire #1 — mirror-edit discipline.
#
# Regenerates tests/mirror-manifest.txt from the current upstream
# checkout. The manifest is the source of truth for staging CI: the
# staging repo's copy of this file MUST be byte-identical to upstream's,
# and every mirrored path's content in staging MUST hash to the listed
# value.
#
# Usage (from the upstream repo root, after mirror-edit):
#   bash .claude/skills/legal-assistant/colocation/tests/regen-mirror-manifest.sh
#
# Then copy the regenerated manifest verbatim to the staging repo at
# skills/de-legal-assistant/colocation/tests/mirror-manifest.txt and
# commit it alongside the mirrored file edits. Staging CI's
# test_mirror_integrity.py will fail if any staging file drifts.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
COLO="$(cd "$HERE/.." && pwd)"

cd "$COLO"

# Files tracked by the mirror — extend as new shared surfaces appear.
# Paths are relative to the colocation/ directory so the manifest is
# layout-agnostic between upstream and staging.
# Scope: test harness only. generate_loi.py is excluded by design —
# staging uses a different document-factory import path (de-document-
# factory), so a byte-level hash would fail on legitimate divergence.
# The test harness has no such divergence; it's where silent mirror-drift
# is most dangerous (tests/ files don't get the same PR-review scrutiny
# as generator edits).
FILES=(
  "tests/_fingerprint.py"
  "tests/conftest.py"
  "tests/test_golden_files.py"
  "tests/test_visual_layout.py"
  "tests/test_intake_structural_shape.py"
)

{
  echo "# v3.5.8 tripwire #1 — mirror integrity manifest."
  echo "# Regenerate with tests/regen-mirror-manifest.sh (upstream repo)."
  echo "# Copy verbatim to staging; staging CI checks each file hashes to"
  echo "# the value listed here. Drift => mirror-edit discipline violation."
  echo "#"
  for f in "${FILES[@]}"; do
    sha256sum "$f"
  done
} > tests/mirror-manifest.txt

echo "Wrote tests/mirror-manifest.txt ($(wc -l < tests/mirror-manifest.txt) lines)"
