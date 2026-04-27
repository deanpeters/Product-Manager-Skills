#!/usr/bin/env bash
#
# validate-skills.sh - Check canonical skill folders before packaging.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$ROOT/skills"

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "Error: skills directory not found at: $SKILLS_DIR" >&2
  exit 1
fi

found=0
valid=0
failures=0

echo "Validating skills in: ${SKILLS_DIR#$ROOT/}"

for skill_dir in "$SKILLS_DIR"/*; do
  [[ -d "$skill_dir" ]] || continue

  found=$((found + 1))
  skill_name="$(basename "$skill_dir")"
  skill_file="$skill_dir/SKILL.md"
  skill_ok=true

  if [[ ! -f "$skill_file" ]]; then
    echo "Missing SKILL.md: skills/$skill_name"
    skill_ok=false
  else
    first_line="$(sed -n '1p' "$skill_file")"
    if [[ "$first_line" != "---" ]]; then
      echo "Missing YAML front matter: skills/$skill_name/SKILL.md"
      skill_ok=false
    else
      if ! awk '
        NR == 1 && $0 == "---" { in_frontmatter = 1; next }
        in_frontmatter && $0 == "---" { exit }
        in_frontmatter && $0 ~ /^name:[[:space:]]*[^[:space:]]/ { found = 1 }
        END { exit(found ? 0 : 1) }
      ' "$skill_file"; then
        echo "Missing front matter field 'name': skills/$skill_name/SKILL.md"
        skill_ok=false
      fi

      if ! awk '
        NR == 1 && $0 == "---" { in_frontmatter = 1; next }
        in_frontmatter && $0 == "---" { exit }
        in_frontmatter && $0 ~ /^description:[[:space:]]*[^[:space:]]/ { found = 1 }
        END { exit(found ? 0 : 1) }
      ' "$skill_file"; then
        echo "Missing front matter field 'description': skills/$skill_name/SKILL.md"
        skill_ok=false
      fi
    fi
  fi

  if [[ "$skill_ok" == true ]]; then
    valid=$((valid + 1))
  else
    failures=$((failures + 1))
  fi
done

echo
echo "Skills found: $found"
echo "Valid skills:  $valid"
echo "Failures:      $failures"

if [[ "$found" -eq 0 ]]; then
  echo "Error: No skill directories found." >&2
  exit 1
fi

if [[ "$failures" -gt 0 ]]; then
  echo "Validation failed." >&2
  exit 1
fi

echo "Validation passed."
