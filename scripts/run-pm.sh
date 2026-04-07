#!/usr/bin/env bash
#
# run-pm.sh - Fast runner for PM skills and commands
# NOTE: This is a local development tool. Do not expose it as a service.
#
# Usage:
#   ./scripts/run-pm.sh skill prd-development "Create a PRD for ..."
#   ./scripts/run-pm.sh command discover "Improve activation for SMBs"
#   ./scripts/run-pm.sh command strategy "..." --agent claude
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

AGENT="print"
MODE=""
TARGET=""
INPUT=""

print_help() {
    cat <<EOF_HELP
Usage: $0 <skill|command> <name> <input> [--agent print|claude|codex]

Examples:
  $0 skill prd-development "Create a PRD for mobile onboarding redesign"
  $0 command discover "Reduce onboarding drop-off"
  $0 command strategy "B2B analytics add-on" --agent claude

Behavior:
  - agent=print  Prints the generated prompt (default)
  - agent=claude Runs: claude "<prompt>"
  - agent=codex  Runs: codex "<prompt>"
EOF_HELP
}

require_value() {
    local option="$1"
    local value="${2:-}"
    if [[ -z "$value" || "$value" == -* ]]; then
        echo "Error: Option '$option' requires a value." >&2
        exit 1
    fi
}

parse_args() {
    if [[ $# -lt 3 ]]; then
        print_help
        exit 1
    fi

    MODE="$1"
    TARGET="$2"
    INPUT="$3"

    # Guard: reject inputs over 2000 characters to prevent runaway prompts
    if [[ ${#INPUT} -gt 2000 ]]; then
        echo "Error: Input exceeds 2000 characters (got ${#INPUT}). Truncate your input and retry." >&2
        exit 1
    fi

    shift 3

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --agent)
                require_value "--agent" "${2:-}"
                AGENT="$2"
                shift 2
                ;;
            --help|-h)
                print_help
                exit 0
                ;;
            *)
                echo "Error: Unknown option '$1'." >&2
                print_help
                exit 1
                ;;
        esac
    done

    if [[ "$MODE" != "skill" && "$MODE" != "command" ]]; then
        echo "Error: Mode must be 'skill' or 'command'." >&2
        exit 1
    fi

    if [[ "$AGENT" != "print" && "$AGENT" != "claude" && "$AGENT" != "codex" ]]; then
        echo "Error: --agent must be one of: print, claude, codex." >&2
        exit 1
    fi
}

build_prompt() {
    local path
    if [[ "$MODE" == "skill" ]]; then
        path="$PROJECT_ROOT/skills/$TARGET/SKILL.md"
        if [[ ! -f "$path" ]]; then
            echo "Error: Skill not found: $TARGET" >&2
            exit 1
        fi
        printf "Using the skill at %s, help with: %s" "${path#$PROJECT_ROOT/}" "$INPUT"
    else
        path="$PROJECT_ROOT/commands/$TARGET.md"
        if [[ ! -f "$path" ]]; then
            echo "Error: Command not found: $TARGET" >&2
            exit 1
        fi
        printf "Run the workflow command at %s for this request: %s" "${path#$PROJECT_ROOT/}" "$INPUT"
    fi
}

run_prompt() {
    local prompt="$1"

    if [[ "$AGENT" == "print" ]]; then
        echo "$prompt"
        exit 0
    fi

    if [[ "$AGENT" == "claude" ]]; then
        if ! command -v claude >/dev/null 2>&1; then
            echo "Error: 'claude' command not found. Use --agent print or install Claude Code CLI." >&2
            exit 1
        fi
        claude "$prompt"
        exit 0
    fi

    if ! command -v codex >/dev/null 2>&1; then
        echo "Error: 'codex' command not found. Use --agent print or install Codex CLI." >&2
        exit 1
    fi
    codex "$prompt"
}

main() {
    parse_args "$@"
    PROMPT="$(build_prompt)"
    run_prompt "$PROMPT"
}

main "$@"
