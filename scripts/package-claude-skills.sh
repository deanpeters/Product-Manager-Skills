#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${1:-"$ROOT/dist/claude-skills"}"

sanitize_frontmatter_for_claude() {
  local src="$1"
  local dst="$2"

  awk '
    BEGIN { in_frontmatter = 0; keep_key = 0 }
    NR == 1 && $0 == "---" { in_frontmatter = 1; print; next }
    in_frontmatter && $0 == "---" { in_frontmatter = 0; print; next }
    in_frontmatter {
      if ($0 ~ /^[A-Za-z0-9_-]+:[[:space:]]*/) {
        key = $0
        sub(/:.*/, "", key)
        if (key == "name" || key == "description" || key == "license" || key == "allowed-tools" || key == "compatibility" || key == "metadata") {
          keep_key = 1
          print
        } else {
          keep_key = 0
        }
        next
      }
      if (keep_key == 1) {
        print
      }
      next
    }
    { print }
  ' "$src" > "$dst"
}

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

for skill_dir in "$ROOT"/skills/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  target_dir="$OUT_DIR/$skill_name"
  mkdir -p "$target_dir"

  if [ -f "$skill_dir/SKILL.md" ]; then
    sanitize_frontmatter_for_claude "$skill_dir/SKILL.md" "$target_dir/Skill.md"
  fi

  for extra in template.md examples scripts; do
    if [ -e "$skill_dir/$extra" ]; then
      cp -R "$skill_dir/$extra" "$target_dir/"
    fi
  done

done

echo "Prepared Claude skills folder at: $OUT_DIR"
