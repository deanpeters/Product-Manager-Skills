# Install PM Skills in Codex

Codex can use these skills from a project-local `.agents/skills` folder, or directly from a clone of this repo.

## Quick Setup with the Codex ZIP

1. Go to the GitHub Releases page for this repo.
2. Download `codex-product-manager-skills.zip`.
3. Unzip it into your project or repo root.
4. Confirm your project now has:

```text
.agents/
  skills/
    <skill-name>/
      SKILL.md
AGENTS.md
```

5. Open Codex in that repo.
6. Ask Codex to use a named skill.

Example:

```text
Use the jobs-to-be-done skill to analyze this customer problem.
```

## Advanced Setup: Clone the Whole Repo

Advanced users can clone this repo and run Codex from the repo root. That gives Codex access to:

- `skills/`
- `commands/`
- `catalog/`
- repo scripts and docs

This is the best path if you want to contribute back, inspect the full library, or use the command workflows.

## Notes

- Treat `skills/` as the source library.
- Treat generated `dist/` artifacts as downloadable packages.
- For Claude Desktop/Web, use the Claude ZIP packs instead. See [`INSTALL-CLAUDE-DESKTOP.md`](INSTALL-CLAUDE-DESKTOP.md).
- For Claude Code, use the plugin marketplace. See [`INSTALL-CLAUDE-CODE.md`](INSTALL-CLAUDE-CODE.md).
