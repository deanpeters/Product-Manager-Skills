# Commands

Commands are reusable workflow wrappers over one or more local PM skills.

- Skills remain the source of truth for frameworks and pedagogy.
- Commands are lightweight orchestration for fast execution.
- Commands are written as markdown with frontmatter and can be used in any agent by referencing the file path.

## Command Format

Each command file should include frontmatter:

```yaml
---
name: command-name
description: What this command does
argument-hint: "<what the user should provide>"
uses:
  - skill-name
  - another-skill
outputs:
  - Output artifact 1
  - Output artifact 2
---
```

## Available Commands (v1)

- `discover`
- `strategy`
- `write-prd`
- `plan-roadmap`
- `prioritize`
- `leadership-transition`

## Validation

```bash
python3 scripts/check-command-metadata.py
```

## Discovery

```bash
./scripts/find-a-command.sh --list-all
./scripts/find-a-command.sh --keyword roadmap
```
