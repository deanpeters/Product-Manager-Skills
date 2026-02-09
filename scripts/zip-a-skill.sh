#!/usr/bin/env bash
#
# zip-a-skill.sh - Build upload-ready ZIP artifacts for Claude custom skills.
#
# This script:
#   1) Runs scripts/package-claude-skills.sh into a temp folder
#   2) Zips one or more packaged skill folders into an output directory
#
# Usage:
#   ./scripts/zip-a-skill.sh --skill user-story
#   ./scripts/zip-a-skill.sh --skill user-story --skill prd-development --output dist/skill-zips
#   ./scripts/zip-a-skill.sh --all
#   ./scripts/zip-a-skill.sh --type workflow
#   ./scripts/zip-a-skill.sh --preset core-pm
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PACKAGER="$SCRIPT_DIR/package-claude-skills.sh"

ALL=false
OUTPUT_DIR="$ROOT/dist/skill-zips"
SKILL_ARGS=()
TYPE_FILTER=""
PRESET=""
LIST_PRESETS=false

print_help() {
  cat <<EOF
Usage: $0 [OPTIONS]

Build upload-ready ZIP files for Claude custom skills.

Options:
  --skill <name|path>  Zip one skill (repeatable)
  --all                Zip all skills
  --type <type>        Zip by skill type: component|interactive|workflow
  --preset <name>      Zip a curated preset (see --list-presets)
  --list-presets       Show available preset names and descriptions
  --output <dir>       Output directory for zip files (default: dist/skill-zips)
  -h, --help           Show this help

Examples:
  $0 --skill user-story
  $0 --skill skills/user-story/SKILL.md --output dist/skill-zips
  $0 --skill user-story --skill prd-development
  $0 --all
  $0 --type interactive
  $0 --all --type workflow
  $0 --preset core-pm
  $0 --list-presets
EOF
}

print_presets() {
  cat <<'EOF'
Available presets:
  core-pm           Core PM starter set across component/interactive/workflow
  finance-suite     All finance-focused skills
  workflow-pack     All workflow skills
  interactive-pack  High-leverage interactive advisors/workshops
  component-pack    Common component templates for PM artifacts
EOF
}

preset_skills() {
  local preset="$1"
  case "$preset" in
    core-pm)
      cat <<'EOF'
problem-statement
user-story
epic-hypothesis
positioning-statement
prioritization-advisor
discovery-interview-prep
problem-framing-canvas
opportunity-solution-tree
prd-development
roadmap-planning
product-strategy-session
skill-authoring-workflow
EOF
      ;;
    finance-suite)
      cat <<'EOF'
finance-metrics-quickref
saas-revenue-growth-metrics
saas-economics-efficiency-metrics
feature-investment-advisor
acquisition-channel-advisor
finance-based-pricing-advisor
business-health-diagnostic
EOF
      ;;
    workflow-pack)
      cat <<'EOF'
discovery-process
prd-development
product-strategy-session
roadmap-planning
skill-authoring-workflow
EOF
      ;;
    interactive-pack)
      cat <<'EOF'
prioritization-advisor
feature-investment-advisor
finance-based-pricing-advisor
business-health-diagnostic
context-engineering-advisor
ai-shaped-readiness-advisor
agent-orchestration-advisor
opportunity-solution-tree
EOF
      ;;
    component-pack)
      cat <<'EOF'
user-story
problem-statement
positioning-statement
epic-hypothesis
proto-persona
press-release
user-story-splitting
recommendation-canvas
EOF
      ;;
    *)
      echo "Error: Unknown preset '$preset'." >&2
      echo "Run '$0 --list-presets' to see valid names." >&2
      return 1
      ;;
  esac
}

require_value() {
  local opt="$1"
  local value="${2:-}"
  if [[ -z "$value" || "$value" == -* ]]; then
    echo "Error: Option '$opt' requires a value." >&2
    exit 1
  fi
}

resolve_skill_name() {
  local input="$1"
  local value="${input%/}"

  if [[ "$value" == */SKILL.md ]]; then
    basename "$(dirname "$value")"
    return 0
  fi

  if [[ "$value" == */skills/* ]]; then
    basename "$value"
    return 0
  fi

  basename "$value"
}

skill_type_for_name() {
  local skill_name="$1"
  local skill_file="$ROOT/skills/$skill_name/SKILL.md"

  if [[ ! -f "$skill_file" ]]; then
    return 1
  fi

  awk '
    BEGIN { in_frontmatter = 0 }
    NR == 1 && $0 == "---" { in_frontmatter = 1; next }
    in_frontmatter && $0 == "---" { exit }
    in_frontmatter && $0 ~ /^type:[[:space:]]*/ {
      sub(/^type:[[:space:]]*/, "", $0)
      print $0
      exit
    }
  ' "$skill_file"
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --skill)
        require_value "--skill" "${2:-}"
        SKILL_ARGS+=("$2")
        shift 2
        ;;
      --all)
        ALL=true
        shift
        ;;
      --type)
        require_value "--type" "${2:-}"
        TYPE_FILTER="$2"
        shift 2
        ;;
      --output)
        require_value "--output" "${2:-}"
        OUTPUT_DIR="$2"
        shift 2
        ;;
      --preset)
        require_value "--preset" "${2:-}"
        PRESET="$2"
        shift 2
        ;;
      --list-presets)
        LIST_PRESETS=true
        shift
        ;;
      -h|--help)
        print_help
        exit 0
        ;;
      *)
        echo "Error: Unknown option '$1'." >&2
        echo "Run '$0 --help' for usage." >&2
        exit 1
        ;;
    esac
  done
}

zip_one_skill() {
  local packaged_root="$1"
  local skill_name="$2"
  local skill_dir="$packaged_root/$skill_name"
  local zip_path="$OUTPUT_DIR/$skill_name.zip"

  if [[ ! -d "$skill_dir" ]]; then
    echo "Error: Skill '$skill_name' not found in packaged output." >&2
    return 1
  fi

  rm -f "$zip_path"
  (cd "$packaged_root" && zip -qr "$zip_path" "$skill_name")
  echo "Created: ${zip_path#$ROOT/}"
}

main() {
  parse_args "$@"

  if [[ "$LIST_PRESETS" == true ]]; then
    print_presets
    exit 0
  fi

  if ! command -v zip >/dev/null 2>&1; then
    echo "Error: 'zip' command not found. Install zip and retry." >&2
    exit 1
  fi

  if [[ -n "$PRESET" && ( "$ALL" == true || -n "$TYPE_FILTER" || "${#SKILL_ARGS[@]}" -gt 0 ) ]]; then
    echo "Error: --preset cannot be combined with --all, --type, or --skill." >&2
    exit 1
  fi

  if [[ -n "$PRESET" ]]; then
    preset_skills "$PRESET" >/dev/null
  fi

  if [[ "$ALL" == false && "${#SKILL_ARGS[@]}" -eq 0 ]]; then
    if [[ -z "$TYPE_FILTER" && -z "$PRESET" ]]; then
      echo "Error: Provide --skill <name|path>, --type <type>, --preset <name>, or --all." >&2
      echo "Run '$0 --help' for usage." >&2
      exit 1
    fi
  fi

  if [[ -n "$TYPE_FILTER" && "$TYPE_FILTER" != "component" && "$TYPE_FILTER" != "interactive" && "$TYPE_FILTER" != "workflow" ]]; then
    echo "Error: --type must be one of: component, interactive, workflow." >&2
    exit 1
  fi

  if [[ "$ALL" == true && "${#SKILL_ARGS[@]}" -gt 0 ]]; then
    echo "Error: Use either --all or --skill, not both." >&2
    exit 1
  fi

  if [[ -n "$TYPE_FILTER" && "${#SKILL_ARGS[@]}" -gt 0 ]]; then
    echo "Error: Use either --skill or --type, not both." >&2
    exit 1
  fi

  if [[ "$OUTPUT_DIR" != /* ]]; then
    OUTPUT_DIR="$ROOT/$OUTPUT_DIR"
  fi

  mkdir -p "$OUTPUT_DIR"

  local tmp_dir=""
  tmp_dir="$(mktemp -d)"
  trap 'rm -rf "${tmp_dir:-}"' EXIT

  bash "$PACKAGER" "$tmp_dir/claude-skills" >/dev/null
  local packaged_root="$tmp_dir/claude-skills"

  local created=0
  if [[ -n "$PRESET" ]]; then
    local skill_name
    while IFS= read -r skill_name; do
      [[ -n "$skill_name" ]] || continue
      zip_one_skill "$packaged_root" "$skill_name"
      created=$((created + 1))
    done < <(preset_skills "$PRESET")
  elif [[ "$ALL" == true ]]; then
    local skill_dir
    for skill_dir in "$packaged_root"/*; do
      [[ -d "$skill_dir" ]] || continue
      local skill_name
      skill_name="$(basename "$skill_dir")"

      if [[ -n "$TYPE_FILTER" ]]; then
        local skill_type
        skill_type="$(skill_type_for_name "$skill_name" || true)"
        [[ "$skill_type" == "$TYPE_FILTER" ]] || continue
      fi

      zip_one_skill "$packaged_root" "$skill_name"
      created=$((created + 1))
    done
  elif [[ -n "$TYPE_FILTER" ]]; then
    local skill_dir
    for skill_dir in "$packaged_root"/*; do
      [[ -d "$skill_dir" ]] || continue
      local skill_name
      local skill_type
      skill_name="$(basename "$skill_dir")"
      skill_type="$(skill_type_for_name "$skill_name" || true)"
      [[ "$skill_type" == "$TYPE_FILTER" ]] || continue
      zip_one_skill "$packaged_root" "$skill_name"
      created=$((created + 1))
    done
  else
    local raw
    for raw in "${SKILL_ARGS[@]}"; do
      local skill_name
      skill_name="$(resolve_skill_name "$raw")"
      zip_one_skill "$packaged_root" "$skill_name"
      created=$((created + 1))
    done
  fi

  if [[ "$created" -eq 0 ]]; then
    echo "Error: No skills matched the requested selection." >&2
    exit 1
  fi

  echo "Done. Created $created zip file(s) in: ${OUTPUT_DIR#$ROOT/}"
}

main "$@"
