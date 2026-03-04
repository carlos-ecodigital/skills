#!/bin/bash
# package-for-web.sh — Generate ZIP packages for Claude.ai org provisioning
# Usage: ./scripts/package-for-web.sh
# Output: web-packages/ directory with one ZIP per skill + de-org-foundations

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/.claude/skills"
OUTPUT_DIR="$REPO_ROOT/web-packages"
STAGING_DIR="$REPO_ROOT/.staging"

# Skills to exclude from web packaging
EXCLUDE_DIRS=("_shared" "_archived")
EXCLUDE_FILES=("_retrieval-rules.yaml")

# Shared reference bundling map
# Format: "skill-name:relative/path/to/shared/file/or/dir"
declare -a BUNDLE_MAP=(
  "seed-fundraising:intake-modules"
  "seed-fundraising:equity-structures.md"
  "seed-fundraising:intake-design-guidebook.md"
  "project-financing:intake-modules/m1-entity-tax.md"
  "project-financing:intake-modules/m4-bess-technical.md"
  "project-financing:intake-modules/m5-dc-ai-technical.md"
  "project-financing:intake-modules/m6-sites-assets.md"
  "project-financing:intake-modules/m7-revenue-debt.md"
  "ops-targetops:market-data.md"
  "ops-targetops:investor-landscape.md"
)

# Clean previous output
rm -rf "$OUTPUT_DIR" "$STAGING_DIR"
mkdir -p "$OUTPUT_DIR" "$STAGING_DIR"

echo "=== Digital Energy Skills Web Packager ==="
echo "Source: $SKILLS_DIR"
echo "Output: $OUTPUT_DIR"
echo ""

count=0

# Package each skill directory
for skill_path in "$SKILLS_DIR"/*/; do
  skill_name=$(basename "$skill_path")

  # Skip excluded directories
  skip=false
  for exclude in "${EXCLUDE_DIRS[@]}"; do
    if [ "$skill_name" = "$exclude" ]; then
      skip=true
      break
    fi
  done
  $skip && continue

  echo "Packaging: $skill_name"

  # Create staging copy
  stage="$STAGING_DIR/$skill_name"
  cp -R "$skill_path" "$stage"

  # Remove .git directory if present (e.g., humanizer submodule)
  rm -rf "$stage/.git"

  # Remove Excel files (binary, not useful in web skills)
  find "$stage" -name "*.xlsx" -delete 2>/dev/null || true

  # Bundle shared references if mapped
  for mapping in "${BUNDLE_MAP[@]}"; do
    map_skill="${mapping%%:*}"
    map_ref="${mapping#*:}"

    if [ "$skill_name" = "$map_skill" ]; then
      shared_source="$SKILLS_DIR/_shared/$map_ref"
      shared_dest="$stage/_shared/$(dirname "$map_ref")"

      if [ -e "$shared_source" ]; then
        mkdir -p "$shared_dest"
        cp -R "$shared_source" "$shared_dest/"
        echo "  + bundled _shared/$map_ref"
      else
        echo "  ! WARNING: _shared/$map_ref not found"
      fi
    fi
  done

  # Create ZIP (from within staging dir so paths are relative)
  (cd "$STAGING_DIR" && zip -r "$OUTPUT_DIR/$skill_name.zip" "$skill_name" -x "*/.DS_Store" "*/.*") > /dev/null
  count=$((count + 1))
done

# Create de-org-foundations skill (web-only)
echo ""
echo "Creating: de-org-foundations (web-only foundation skill)"
foundations_stage="$STAGING_DIR/de-org-foundations"
mkdir -p "$foundations_stage/org"

# Write SKILL.md
cat > "$foundations_stage/SKILL.md" << 'SKILL_EOF'
---
name: de-org-foundations
description: >
  Digital Energy organizational context — team structure, ways of working,
  OKR framework, project management methodology. Background knowledge that
  Claude loads when organizational context is relevant.
user-invocable: false
---

# Digital Energy Organization Foundation

This skill provides organizational context for Digital Energy.
Claude loads this automatically when team structure, decision-making,
OKR, or project management context is needed.

## Contents

- See org/TEAMS.md for team structure and responsibilities
- See org/WAYS-OF-WORKING.md for communication standards and BLUF format
- See org/OKR-GUIDELINES.md for OKR framework (setting, scoring, reviewing)
- See org/OKR-PROJECT-MANAGEMENT.md for project execution (stage-gate, sprints)
- See org/OKR-GLOSSARY.md for terminology definitions
- See ops-playbook.md for operational playbook
- See marketing-ops-guide.md for marketing operations guide
SKILL_EOF

# Bundle org docs
for doc in TEAMS.md WAYS-OF-WORKING.md OKR-GUIDELINES.md OKR-PROJECT-MANAGEMENT.md OKR-GLOSSARY.md; do
  if [ -f "$SKILLS_DIR/_shared/org/$doc" ]; then
    cp "$SKILLS_DIR/_shared/org/$doc" "$foundations_stage/org/"
    echo "  + org/$doc"
  fi
done

# Bundle operational guides
for doc in ops-playbook.md marketing-ops-guide.md; do
  if [ -f "$SKILLS_DIR/_shared/$doc" ]; then
    cp "$SKILLS_DIR/_shared/$doc" "$foundations_stage/"
    echo "  + $doc"
  fi
done

(cd "$STAGING_DIR" && zip -r "$OUTPUT_DIR/de-org-foundations.zip" "de-org-foundations" -x "*/.DS_Store" "*/.*") > /dev/null
count=$((count + 1))

# Clean staging
rm -rf "$STAGING_DIR"

# Summary
echo ""
echo "=== Done ==="
echo "Generated $count ZIPs in $OUTPUT_DIR/"
echo ""
total_size=$(du -sh "$OUTPUT_DIR" | cut -f1)
echo "Total size: $total_size"
echo ""
echo "ZIPs:"
ls -lh "$OUTPUT_DIR"/*.zip | awk '{print "  " $NF " (" $5 ")"}'
echo ""
echo "Next: upload these ZIPs to Claude.ai Organization settings > Skills"
