# Install PM Skills for OpenCode

[OpenCode](https://opencode.ai) is an AI coding agent that natively discovers skills from your home directory or project.

## Global Install (all projects)

```bash
# Copy all skills to OpenCode's global skills directory
cp -r skills/* ~/.config/opencode/skills/

# Or copy individual skills:
cp -r skills/prd-development ~/.config/opencode/skills/
cp -r skills/user-story ~/.config/opencode/skills/
```

## Project-level Install

```bash
# From your project root
cp -r ../Product-Manager-Skills/skills/* .opencode/skills/
```

## How It Works

OpenCode discovers skills from these locations (in order):

1. `.opencode/skills/<name>/SKILL.md` (project)
2. `~/.config/opencode/skills/<name>/SKILL.md` (global)
3. `.claude/skills/<name>/SKILL.md` (project, Claude-compatible fallback)
4. `~/.claude/skills/<name>/SKILL.md` (global, Claude-compatible fallback)

Skills are loaded on-demand via OpenCode's `skill` tool — the agent sees all available skills and loads the full content when needed.

## Per-Agent Permissions (optional)

In your `opencode.json`, scope PM skills to specific agents:

```json
{
  "agent": {
    "plan": {
      "permission": {
        "skill": {
          "pm-*": "allow",
          "user-story*": "allow",
          "prd-*": "allow",
          "stakeholder-*": "allow"
        }
      }
    }
  }
}
```

## OpenCode-Specific Frontmatter

These skills include `compatibility: opencode` and rich fields nested under `metadata:` — OpenCode reads `name` and `description` for skill selection, and agents can read `metadata.*` fields at runtime for additional context.
