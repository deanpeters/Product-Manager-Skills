#!/usr/bin/env bash
#
# build-codex-skills.sh - Build a Codex-friendly .agents/skills package.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
OUT_DIR="$ROOT/dist/codex"
OUT_SKILLS="$OUT_DIR/.agents/skills"
ZIP_PATH="$OUT_DIR/codex-product-manager-skills.zip"

if ! command -v zip >/dev/null 2>&1; then
  echo "Error: 'zip' command not found. Install zip and retry." >&2
  exit 1
fi

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "Error: skills directory not found at: $SKILLS_DIR" >&2
  exit 1
fi

if [[ ! -f "$ROOT/AGENTS.md" ]]; then
  echo "Error: AGENTS.md not found at repo root." >&2
  exit 1
fi

rm -rf "$OUT_DIR"
mkdir -p "$OUT_SKILLS"

count=0
for skill_dir in "$SKILLS_DIR"/*; do
  [[ -d "$skill_dir" ]] || continue
  skill_name="$(basename "$skill_dir")"
  cp -R "$skill_dir" "$OUT_SKILLS/$skill_name"
  count=$((count + 1))
done

cp "$ROOT/AGENTS.md" "$OUT_DIR/AGENTS.md"

if [[ "$count" -eq 0 ]]; then
  echo "Error: No skills copied for Codex package." >&2
  exit 1
fi

find "$OUT_DIR" -name .DS_Store -type f -delete

rm -f "$ZIP_PATH"
(cd "$OUT_DIR" && zip -qr "$ZIP_PATH" .agents AGENTS.md)

echo "Copied $count skills to: ${OUT_SKILLS#$ROOT/}"
echo "Created: ${ZIP_PATH#$ROOT/}"
