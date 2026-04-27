#!/usr/bin/env bash
#
# build-claude-desktop-packs.sh - Build multi-skill ZIP packs for Claude Desktop/Web.
#
# Uses the same Claude-compatible packaging path as zip-a-skill.sh:
# scripts/package-claude-skills.sh converts canonical SKILL.md files to Skill.md.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PACKAGER="$SCRIPT_DIR/package-claude-skills.sh"
OUT_DIR="$ROOT/dist/claude-desktop"

require_zip() {
  if ! command -v zip >/dev/null 2>&1; then
    echo "Error: 'zip' command not found. Install zip and retry." >&2
    exit 1
  fi
}

pack_skills() {
  local packaged_root="$1"
  local zip_name="$2"
  shift 2

  local tmp_pack
  tmp_pack="$(mktemp -d)"
  local count=0
  local skill

  for skill in "$@"; do
    if [[ -d "$packaged_root/$skill" ]]; then
      cp -R "$packaged_root/$skill" "$tmp_pack/"
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
  echo "Created: ${OUT_DIR#$ROOT/}/$zip_name ($count skills)"
}

pack_all_skills() {
  local packaged_root="$1"
  local zip_name="$2"
  local count

  count="$(find "$packaged_root" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
  if [[ "$count" -eq 0 ]]; then
    echo "Error: No packaged skills found for $zip_name." >&2
    exit 1
  fi

  rm -f "$OUT_DIR/$zip_name"
  (cd "$packaged_root" && zip -qr "$OUT_DIR/$zip_name" .)
  echo "Created: ${OUT_DIR#$ROOT/}/$zip_name ($count skills)"
}

main() {
  require_zip

  if [[ ! -x "$PACKAGER" && ! -f "$PACKAGER" ]]; then
    echo "Error: Claude packager not found at: $PACKAGER" >&2
    exit 1
  fi

  rm -rf "$OUT_DIR"
  mkdir -p "$OUT_DIR"

  local tmp_dir
  tmp_dir="$(mktemp -d)"
  trap 'rm -rf "${tmp_dir:-}"' EXIT

  bash "$PACKAGER" "$tmp_dir/claude-skills" >/dev/null
  local packaged_root="$tmp_dir/claude-skills"

  pack_skills "$packaged_root" "01-core-pm-starter-pack.zip" \
    user-story \
    jobs-to-be-done \
    prioritization-advisor \
    product-strategy-session \
    roadmap-planning \
    discovery-process

  pack_skills "$packaged_root" "02-discovery-pack.zip" \
    discovery-process \
    discovery-interview-prep \
    jobs-to-be-done \
    proto-persona \
    problem-statement \
    opportunity-solution-tree \
    customer-journey-map

  pack_skills "$packaged_root" "03-strategy-pack.zip" \
    product-strategy-session \
    positioning-statement \
    positioning-workshop \
    tam-sam-som-calculator \
    pestel-analysis \
    recommendation-canvas \
    lean-ux-canvas

  pack_skills "$packaged_root" "04-delivery-pack.zip" \
    user-story \
    user-story-splitting \
    epic-breakdown-advisor \
    epic-hypothesis \
    prd-development \
    roadmap-planning

  pack_skills "$packaged_root" "05-ai-pm-pack.zip" \
    ai-shaped-readiness-advisor \
    context-engineering-advisor \
    recommendation-canvas \
    pol-probe \
    pol-probe-advisor \
    company-research

  pack_all_skills "$packaged_root" "99-all-skills-pack.zip"

  echo "Claude Desktop/Web packs ready in: ${OUT_DIR#$ROOT/}"
}

main "$@"
