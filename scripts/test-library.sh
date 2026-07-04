#!/usr/bin/env bash
#
# test-library.sh - Validate the full PM skills library surface.
#
# Runs:
#   1) skill metadata checks
#   2) skill trigger-readiness audit
#   3) command metadata/reference checks
#   4) library drift check (marketplace entries + doc links vs skills/)
#   5) optional skill smoke tests
#   6) catalog generation freshness check
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

RUN_SMOKE=false

print_help() {
    cat <<EOF_HELP
Usage: $0 [--smoke]

Options:
  --smoke   Run additional skill smoke tests via scripts/test-a-skill.sh --smoke
  --help    Show this help
EOF_HELP
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --smoke)
                RUN_SMOKE=true
                shift
                ;;
            --help|-h)
                print_help
                exit 0
                ;;
            *)
                echo "Error: Unknown option '$1'" >&2
                print_help
                exit 1
                ;;
        esac
    done
}

main() {
    parse_args "$@"
    cd "$PROJECT_ROOT"

    echo "[1/6] Validating skills"
    python3 "$SCRIPT_DIR/check-skill-metadata.py"

    echo "[2/6] Auditing trigger metadata"
    python3 "$SCRIPT_DIR/check-skill-triggers.py"

    echo "[3/6] Validating commands"
    python3 "$SCRIPT_DIR/check-command-metadata.py"

    echo "[4/6] Checking library drift (marketplace + doc links)"
    python3 "$SCRIPT_DIR/check-library-drift.py"

    if $RUN_SMOKE; then
        echo "[5/6] Running skill smoke tests"
        "$SCRIPT_DIR/test-a-skill.sh" --smoke
    else
        echo "[5/6] Skipping smoke tests (use --smoke to enable)"
    fi

    echo "[6/6] Regenerating catalogs"
    python3 "$SCRIPT_DIR/generate-catalog.py"

    echo "Library checks complete."
}

main "$@"
