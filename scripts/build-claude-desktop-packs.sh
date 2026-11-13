#!/usr/bin/env bash
#
# build-claude-desktop-packs.sh - Build easy-button ZIP packs for Claude Desktop/Web.
#
# Each pack contains individual upload-ready skill ZIPs from dist/skill-zips.
# Users download one pack, unzip it, then upload the skill ZIPs inside to Claude.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUT_DIR="$ROOT/dist/claude-desktop"
SKILL_ZIPS_DIR="$ROOT/dist/skill-zips"

require_zip() {
  if ! command -v zip >/dev/null 2>&1; then
    echo "Error: 'zip' command not found. Install zip and retry." >&2
    exit 1
  fi
}

pack_skills() {
  local zip_name="$1"
  shift 1

  local tmp_pack
  tmp_pack="$(mktemp -d)"
  local count=0
  local skill

  for skill in "$@"; do
    if [[ -f "$SKILL_ZIPS_DIR/$skill.zip" ]]; then
      cp "$SKILL_ZIPS_DIR/$skill.zip" "$tmp_pack/"
      count=$((count + 1))
    else
      echo "Warning: Skill '$skill' not found; skipping for $zip_name." >&2
    fi
  done

  if [[ "$count" -eq 0 ]]; then
    rm -rf "$tmp_pack"
    echo "Error: Pack '$zip_name' would be empty." >&2
    exit 1
  fi

  rm -f "$OUT_DIR/$zip_name"
  (cd "$tmp_pack" && zip -qr "$OUT_DIR/$zip_name" .)
  rm -rf "$tmp_pack"
  echo "Created: ${OUT_DIR#$ROOT/}/$zip_name ($count skill ZIPs)"
}

pack_all_skills() {
  local zip_name="$1"
  local count

  count="$(find "$SKILL_ZIPS_DIR" -mindepth 1 -maxdepth 1 -type f -name '*.zip' | wc -l | tr -d ' ')"
  if [[ "$count" -eq 0 ]]; then
    echo "Error: No individual skill ZIPs found for $zip_name." >&2
    exit 1
  fi

  rm -f "$OUT_DIR/$zip_name"
  (cd "$SKILL_ZIPS_DIR" && zip -qr "$OUT_DIR/$zip_name" .)
  echo "Created: ${OUT_DIR#$ROOT/}/$zip_name ($count skill ZIPs)"
}

main() {
  require_zip

  if [[ ! -f "$SCRIPT_DIR/zip-a-skill.sh" ]]; then
    echo "Error: Skill ZIP builder not found at: $SCRIPT_DIR/zip-a-skill.sh" >&2
    exit 1
  fi

  rm -rf "$OUT_DIR"
  mkdir -p "$OUT_DIR"

  rm -rf "$SKILL_ZIPS_DIR"
  bash "$SCRIPT_DIR/zip-a-skill.sh" --all --output "$SKILL_ZIPS_DIR" >/dev/null

  pack_skills "01-core-pm-starter-pack.zip" \
    user-story \
    jobs-to-be-done \
    prioritization-advisor \
    product-strategy-session \
    roadmap-planning \
    discovery-process
  cp "$OUT_DIR/01-core-pm-starter-pack.zip" "$OUT_DIR/pm-skills-starter-pack.zip"
  echo "Created alias: ${OUT_DIR#$ROOT/}/pm-skills-starter-pack.zip"

  pack_skills "02-discovery-pack.zip" \
    discovery-process \
    discovery-interview-prep \
    jobs-to-be-done \
    proto-persona \
    problem-statement \
    opportunity-solution-tree \
    customer-journey-map

  pack_skills "03-strategy-pack.zip" \
    product-strategy-session \
    positioning-statement \
    positioning-workshop \
    tam-sam-som-calculator \
    pestel-analysis \
    recommendation-canvas \
    lean-ux-canvas

  pack_skills "04-delivery-pack.zip" \
    user-story \
    user-story-splitting \
    epic-breakdown-advisor \
    epic-hypothesis \
    prd-development \
    roadmap-planning

  pack_skills "05-ai-pm-pack.zip" \
    ai-shaped-readiness-advisor \
    context-engineering-advisor \
    recommendation-canvas \
    pol-probe \
    pol-probe-advisor \
    company-research

  pack_skills "06-market-intel-pack.zip" \
    intel-discipline-advisor \
    intelligence-collection-disciplines \
    autonomous-investigation \
    competitive-analysis-process \
    market-landscape-scan \
    competitive-research-snapshot \
    competitive-intel-watch \
    battle-card-builder \
    voice-of-customer-miner \
    pricing-packaging-tracker \
    swot-analysis \
    porters-five-forces \
    ansoff-matrix \
    pestel-delta-monitor \
    tam-sam-som-calculator \
    company-intel

  pack_skills "07-lifecycle-eol-pack.zip" \
    lifecycle-play-advisor \
    product-lifecycle-plays \
    eol-readiness-advisor \
    eol-process \
    eol-checklist \
    eol-stakeholder-sequence \
    eol-internal-enablement \
    eol-message

  # Lifecycle bundle packs, generated from the bundles: mapping in
  # pm-skills.config.yaml (each carries the Core helper skills). Same grouping
  # as the Claude Code plugins in plugins/.
  local bundle
  while read -r bundle; do
    local bundle_skills=()
    while read -r skill_name; do bundle_skills+=("$skill_name"); done \
      < <(python3 "$SCRIPT_DIR/bundle-skills.py" "$bundle")
    pack_skills "pm-${bundle}-pack.zip" "${bundle_skills[@]}"
  done < <(python3 "$SCRIPT_DIR/bundle-skills.py" --list)

  pack_all_skills "99-all-skills-pack.zip"

  echo "Claude Desktop/Web packs ready in: ${OUT_DIR#$ROOT/}"
}

main "$@"
