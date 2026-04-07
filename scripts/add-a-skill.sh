#!/usr/bin/env bash
#
# add-a-skill.sh — Agent-agnostic skill distillation utility
#
# Purpose: Convert raw PM content into formalized skills using AI agents
#          Supports Claude Code, manual mode, and custom adapters
#
# Usage:
#   ./scripts/add-a-skill.sh <input-file>
#   ./scripts/add-a-skill.sh --text "content here"
#   cat file.md | ./scripts/add-a-skill.sh
#   ./scripts/add-a-skill.sh --agent manual <input-file>
#   ./scripts/add-a-skill.sh --list-agents
#
# Workflow:
#   1. Intake    → Read content from file/stdin/arg
#   2. Suggest   → AI recommends skill type(s) and structure
#   3. Plan      → Show proposed skills with file structure
#   4. Generate  → Create skill files if approved
#   5. Validate  → Run check-skill-metadata.py
#   6. Review    → User reviews generated skill
#   7. Document  → Update CLAUDE.md, README.md
#   8. Stage     → Stage files for git commit
#

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ADAPTERS_DIR="$SCRIPT_DIR/adapters"
# SECURITY: ADAPTERS_DIR must not be world-writable. Any .sh file placed here
# will be sourced in this script's shell context. Verify with: ls -ld "$ADAPTERS_DIR"
SKILLS_DIR="$PROJECT_ROOT/skills"
DOCS_DIR="$PROJECT_ROOT/docs"

# Global variables
AGENT=""
INPUT_CONTENT=""
INPUT_SOURCE=""
TEMP_DIR=""
DRY_RUN=false

# Cleanup on exit
cleanup() {
    if [[ -n "$TEMP_DIR" && -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
}
trap cleanup EXIT

# Helper functions
print_header() {
    echo -e "\n${CYAN}${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}${BOLD}  $1${NC}"
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════════════════════════════${NC}\n"
}

print_step() {
    echo -e "${BLUE}${BOLD}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ Error: $1${NC}" >&2
}

confirm() {
    local prompt="$1"
    local default="${2:-n}"
    local response

    if [[ "$default" == "y" ]]; then
        read -r -p "$(echo -e "${BOLD}$prompt [Y/n]:${NC} ")" response
        response=${response:-y}
    else
        read -r -p "$(echo -e "${BOLD}$prompt [y/N]:${NC} ")" response
        response=${response:-n}
    fi

    [[ "$response" =~ ^[Yy] ]]
}

# Validate an adapter path before sourcing.
# Rejects names that contain path separators or characters outside [a-zA-Z0-9_-].
validate_adapter() {
    local adapter="$1"
    local name
    name="$(basename "$adapter" .sh)"
    if [[ "$name" =~ [^a-zA-Z0-9_-] ]]; then
        print_error "Refusing to source adapter with unsafe name: $name"
        exit 1
    fi
    # Ensure the resolved path is still inside ADAPTERS_DIR (no traversal)
    local real_adapter real_adapters_dir
    real_adapter="$(realpath "$adapter" 2>/dev/null || echo "$adapter")"
    real_adapters_dir="$(realpath "$ADAPTERS_DIR" 2>/dev/null || echo "$ADAPTERS_DIR")"
    if [[ "$real_adapter" != "$real_adapters_dir"/* ]]; then
        print_error "Refusing to source adapter outside adapters directory: $adapter"
        exit 1
    fi
}

# List available adapters
list_agents() {
    print_header "Available Adapters"

    echo "Detected adapters:"
    local found_any=false

    for adapter in "$ADAPTERS_DIR"/*.sh; do
        [[ "$adapter" == *"ADAPTER_TEMPLATE.sh" ]] && continue
        [[ -f "$adapter" ]] || continue

        local adapter_name=$(basename "$adapter" .sh)

        # Validate and source adapter to check if available
        validate_adapter "$adapter"
        # shellcheck source=/dev/null
        source "$adapter"

        if adapter_check_available; then
            echo -e "  ${GREEN}✓${NC} ${BOLD}$adapter_name${NC} (available)"
            found_any=true
        else
            echo -e "  ${RED}✗${NC} $adapter_name (not installed)"
        fi
    done

    if ! $found_any; then
        print_error "No adapters are currently available"
        echo -e "\nCreate an adapter in: $ADAPTERS_DIR"
        echo "Or use manual mode: $0 --agent manual <input-file>"
        exit 1
    fi

    echo -e "\nUsage: $0 --agent <adapter-name> <input-file>"
}

# Detect available adapter
detect_agent() {
    print_step "Detecting available adapters..."

    # Try agents in priority order
    local priority_order=("claude-code" "manual")

    for agent_name in "${priority_order[@]}"; do
        local adapter="$ADAPTERS_DIR/$agent_name.sh"

        if [[ -f "$adapter" ]]; then
            validate_adapter "$adapter"
            # shellcheck source=/dev/null
            source "$adapter"

            if adapter_check_available; then
                AGENT="$agent_name"
                print_success "Using agent: $agent_name"
                return 0
            fi
        fi
    done

    print_error "No supported adapters found."
    echo -e "\nRun '$0 --list-agents' to see installation status."
    exit 1
}

# Load specified agent adapter
load_agent() {
    local agent_name="$1"
    local adapter="$ADAPTERS_DIR/$agent_name.sh"

    if [[ ! -f "$adapter" ]]; then
        print_error "Adapter not found: $agent_name"
        echo "Available adapters:"
        ls -1 "$ADAPTERS_DIR"/*.sh | xargs -n1 basename | sed 's/.sh$//' | sed 's/^/  /'
        exit 1
    fi

    validate_adapter "$adapter"
    # shellcheck source=/dev/null
    source "$adapter"

    if ! adapter_check_available; then
        print_error "Agent '$agent_name' is not installed or not available"
        exit 1
    fi

    AGENT="$agent_name"
    print_success "Loaded agent: $agent_name"
}

# Read input content
read_input() {
    print_step "Reading input content..."

    if [[ -n "${1:-}" ]]; then
        # From file
        if [[ ! -f "$1" ]]; then
            print_error "File not found: $1"
            exit 1
        fi
        INPUT_CONTENT=$(cat "$1")
        INPUT_SOURCE="file: $1"
        print_success "Read content from: $1"
    elif [[ ! -t 0 ]]; then
        # From stdin
        INPUT_CONTENT=$(cat)
        INPUT_SOURCE="stdin"
        print_success "Read content from stdin"
    else
        print_error "No input provided"
        echo "Usage: $0 <input-file> or pipe content via stdin"
        exit 1
    fi

    local word_count=$(echo "$INPUT_CONTENT" | wc -w | tr -d ' ')
    echo "  Content size: $word_count words"
}

# Step 1: Analyze content and suggest skills
analyze_content() {
    print_header "Step 1: Analyzing Content"

    print_step "Asking $AGENT to analyze content and suggest skills..."

    # Call adapter's analyze function
    local analysis
    analysis=$(adapter_analyze_content "$INPUT_CONTENT")

    echo "$analysis"

    echo "$analysis" > "$TEMP_DIR/analysis.txt"

    echo ""
    if ! confirm "Does this analysis look good? Continue with skill generation?"; then
        echo "Exiting. No files were created."
        exit 0
    fi
}

# Step 2: Generate skill plan
generate_plan() {
    print_header "Step 2: Generating Skill Plan"

    print_step "Creating detailed skill plan..."

    local analysis
    analysis=$(cat "$TEMP_DIR/analysis.txt")

    # Call adapter's plan function
    local plan
    plan=$(adapter_generate_plan "$analysis" "$INPUT_CONTENT")

    echo "$plan"

    echo "$plan" > "$TEMP_DIR/plan.txt"

    echo ""
    if ! confirm "Approve this plan and generate skill files?"; then
        echo "Exiting. No files were created."
        exit 0
    fi
}

# Step 3: Generate skill files
generate_skills() {
    print_header "Step 3: Generating Skill Files"

    print_step "Generating skill content..."

    local plan
    plan=$(cat "$TEMP_DIR/plan.txt")

    # Call adapter's generate function
    adapter_generate_skill "$plan" "$INPUT_CONTENT" "$TEMP_DIR/skills"

    print_success "Skill files generated in: $TEMP_DIR/skills"

    # Show what was created
    echo -e "\nGenerated files:"
    find "$TEMP_DIR/skills" -type f | sed 's|^|  |'
}

# Step 4: Validate skills
validate_skills() {
    print_header "Step 4: Validating Skills"

    print_step "Running skill metadata validation..."

    local validation_script="$SCRIPT_DIR/check-skill-metadata.py"

    if [[ ! -f "$validation_script" ]]; then
        print_warning "Validation script not found: $validation_script"
        print_warning "Skipping validation (proceed with caution)"
        return 0
    fi

    local failed=false
    local validated_count=0

    # Validate each SKILL.md file
    for skill_file in "$TEMP_DIR/skills"/*/SKILL.md; do
        [[ -f "$skill_file" ]] || continue

        local skill_name=$(basename "$(dirname "$skill_file")")
        validated_count=$((validated_count + 1))

        echo -e "\nValidating: ${BOLD}$skill_name${NC}"

        if python3 "$validation_script" "$skill_file"; then
            print_success "✓ Passed validation"
        else
            print_error "✗ Failed validation"
            failed=true
        fi
    done

    if [[ "$validated_count" -eq 0 ]]; then
        print_error "No generated SKILL.md files found for validation"
        return 1
    fi

    if $failed; then
        echo ""
        print_error "Some skills failed validation"
        if ! confirm "Continue anyway? (not recommended)"; then
            echo "Exiting. Files are in: $TEMP_DIR/skills"
            exit 1
        fi
    else
        print_success "All skills passed validation"
    fi
}

# Step 5: Review skills
review_skills() {
    print_header "Step 5: Review Generated Skills"

    echo "Generated skills are in: $TEMP_DIR/skills"
    echo ""
    echo "Please review the generated skills before installing."
    echo "You can:"
    echo "  • Read the SKILL.md files"
    echo "  • Check examples and templates"
    echo "  • Verify the structure and content"
    echo ""

    if confirm "Open skills directory in your editor/file browser?" "y"; then
        if command -v code &> /dev/null; then
            code "$TEMP_DIR/skills"
        elif [[ "$(uname)" == "Darwin" ]]; then
            open "$TEMP_DIR/skills"
        else
            xdg-open "$TEMP_DIR/skills" 2>/dev/null || true
        fi
    fi

    echo ""
    if ! confirm "Ready to install these skills?"; then
        echo "Exiting. Files preserved in: $TEMP_DIR/skills"
        trap - EXIT  # Don't cleanup
        exit 0
    fi
}

# Step 6: Install skills
install_skills() {
    print_header "Step 6: Installing Skills"

    print_step "Copying skill files to $SKILLS_DIR..."

    local installed=()

    for skill_dir in "$TEMP_DIR/skills"/*; do
        [[ -d "$skill_dir" ]] || continue

        local skill_name=$(basename "$skill_dir")
        local target_dir="$SKILLS_DIR/$skill_name"

        if [[ -d "$target_dir" ]]; then
            print_warning "Skill already exists: $skill_name"
            if ! confirm "Overwrite existing skill?"; then
                echo "  Skipping $skill_name"
                continue
            fi
            rm -rf "$target_dir"
        fi

        cp -r "$skill_dir" "$target_dir"
        installed+=("$skill_name")
        print_success "Installed: $skill_name"
    done

    printf "%s\n" "${installed[@]}" > "$TEMP_DIR/installed.txt"

    if [[ ${#installed[@]} -eq 0 ]]; then
        print_warning "No skills were installed"
        exit 0
    fi
}

# Step 7: Update documentation
update_documentation() {
    print_header "Step 7: Updating Documentation"

    print_step "Generating documentation updates..."

    local installed
    installed=$(cat "$TEMP_DIR/installed.txt")

    # Call adapter's documentation function
    adapter_update_documentation "$installed" "$TEMP_DIR/doc-updates"

    print_success "Documentation updates generated"

    echo ""
    echo "The following documentation should be updated:"
    echo "  • CLAUDE.md — Project status and skill counts"
    echo "  • README.md — Skill lists and descriptions"
    echo "  • Possibly docs/ files if this is a new suite"
    echo ""

    if [[ -d "$TEMP_DIR/doc-updates" ]]; then
        echo "Suggested updates are in: $TEMP_DIR/doc-updates"
        echo ""
    fi

    if confirm "Generate documentation updates with AI assistance?" "y"; then
        print_step "Asking $AGENT to update documentation..."
        adapter_apply_documentation_updates "$installed"
        print_success "Documentation updated"
    else
        print_warning "Skipping documentation updates"
        echo "You'll need to manually update:"
        echo "  • CLAUDE.md (skill counts)"
        echo "  • README.md (add skills to appropriate sections)"
    fi
}

# Step 8: Stage for commit
stage_files() {
    print_header "Step 8: Staging Files for Commit"

    print_step "Staging new and modified files..."

    cd "$PROJECT_ROOT"

    # Stage only skills installed in this run
    while IFS= read -r skill_name; do
        [[ -n "$skill_name" ]] || continue
        git add "skills/$skill_name" 2>/dev/null || true
    done < "$TEMP_DIR/installed.txt"

    # Stage documentation updates
    git add CLAUDE.md README.md 2>/dev/null || true

    print_success "Files staged for commit"

    echo ""
    echo -e "${BOLD}Git Status:${NC}"
    git status --short

    echo ""
    print_success "Skill creation complete!"
    echo ""
    echo "Next steps:"
    echo "  1. Review staged changes: git diff --staged"
    echo "  2. Commit changes: git commit -m 'Add [skill-name] skill'"
    echo "  3. Push to remote: git push"
}

# Main workflow
main() {
    print_header "PM Skills — Add-a-Skill Utility"

    # Create temp directory
    TEMP_DIR=$(mktemp -d)
    mkdir -p "$TEMP_DIR/skills"

    # Step 1: Analyze content
    analyze_content

    # Step 2: Generate plan
    generate_plan

    # Step 3: Generate skills
    generate_skills

    # Step 4: Validate
    validate_skills

    # Dry run stops before install/docs/staging
    if $DRY_RUN; then
        print_warning "Dry run mode: skipping install, docs updates, and git staging"
        echo "Generated files are preserved in: $TEMP_DIR/skills"
        trap - EXIT  # Don't cleanup
        exit 0
    fi

    # Step 5: Review
    review_skills

    # Step 6: Install
    install_skills

    # Step 7: Update docs
    update_documentation

    # Step 8: Stage for commit
    stage_files
}

# Parse command line arguments
parse_args() {
    require_value() {
        local option="$1"
        local value="${2:-}"
        if [[ -z "$value" || "$value" == -* ]]; then
            print_error "Option '$option' requires a value"
            echo "Run '$0 --help' for usage information."
            exit 1
        fi
    }

    while [[ $# -gt 0 ]]; do
        case $1 in
            --agent)
                require_value "--agent" "${2:-}"
                load_agent "$2"
                shift 2
                ;;
            --list-agents)
                list_agents
                exit 0
                ;;
            --text)
                require_value "--text" "${2:-}"
                INPUT_CONTENT="$2"
                INPUT_SOURCE="command line argument"
                shift 2
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --help|-h)
                cat << EOF
Usage: $0 [OPTIONS] [INPUT_FILE]

Convert raw PM content into formalized skills using AI agents.

Options:
  --agent <name>      Use specific adapter (claude-code, manual, or custom adapter name)
  --list-agents       List available adapters and their installation status
  --text "content"    Provide content directly as argument
  --dry-run           Generate and validate only (skip install/docs/staging)
  --help, -h          Show this help message

Input Methods:
  1. From file:       $0 research/content.md
  2. From stdin:      cat notes.txt | $0
  3. From clipboard:  pbpaste | $0 (macOS) or xclip -o | $0 (Linux)
  4. From argument:   $0 --text "My framework for..."

Examples:
  $0 research/new-framework.md
  $0 --agent manual research/workshop-notes.md
  cat brainstorm.txt | $0
  pbpaste | $0 --agent claude-code

Workflow:
  1. Intake    → Read content from file/stdin/arg
  2. Suggest   → AI recommends skill type(s) and structure
  3. Plan      → Show proposed skills with file structure
  4. Generate  → Create skill files if approved
  5. Validate  → Run check-skill-metadata.py
  6. Review    → User reviews generated skill
  7. Document  → Update CLAUDE.md, README.md
  8. Stage     → Stage files for git commit

EOF
                exit 0
                ;;
            -*)
                print_error "Unknown option: $1"
                echo "Run '$0 --help' for usage information."
                exit 1
                ;;
            *)
                # Positional argument (input file)
                if [[ -n "$INPUT_CONTENT" ]]; then
                    print_error "Multiple input sources provided. Use only one of: file, --text, or stdin."
                    exit 1
                fi
                read_input "$1"
                shift
                ;;
        esac
    done
}

# Entry point
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Ensure we're in the project root
    cd "$PROJECT_ROOT"

    # Parse arguments
    parse_args "$@"

    # Detect or load agent if not specified
    if [[ -z "$AGENT" ]]; then
        detect_agent
    fi

    # Read input if not already read
    if [[ -z "$INPUT_CONTENT" ]]; then
        if [[ ! -t 0 ]]; then
            # Reading from stdin
            read_input
        else
            print_error "No input provided"
            echo "Run '$0 --help' for usage information."
            exit 1
        fi
    fi

    # Run main workflow
    main
fi
