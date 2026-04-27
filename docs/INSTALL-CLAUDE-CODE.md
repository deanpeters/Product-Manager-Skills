# Install PM Skills in Claude Code

Claude Code users should usually use the existing plugin marketplace path. It keeps terminal workflows clean and preserves the Claude Code installation pattern this repo already supports.

## Quick Setup

In Claude Code, add the marketplace and install the skill you need:

```text
/plugin marketplace add deanpeters/Product-Manager-Skills
/plugin install jobs-to-be-done@pm-skills
/reload-plugins
```

Then ask for the skill by name:

```text
Use the jobs-to-be-done skill to analyze this customer problem.
```

## Why Not Use the Claude Desktop ZIPs?

The ZIP packs are designed for Claude Desktop and Claude Web skill upload. Claude Code already has a better path: the plugin marketplace.

Use the marketplace when:

- You work primarily in a terminal.
- You want to install one skill at a time.
- You want Claude Code to discover skills through its plugin system.

Use the ZIP packs only when you are setting up Claude Desktop or Claude Web.

## Helpful Commands

```text
/plugin marketplace add deanpeters/Product-Manager-Skills
/plugin install user-story@pm-skills
/plugin install prd-development@pm-skills
/plugin install product-strategy-session@pm-skills
/reload-plugins
```

## More Setup Paths

- Claude Desktop/Web: [`INSTALL-CLAUDE-DESKTOP.md`](INSTALL-CLAUDE-DESKTOP.md)
- Codex: [`INSTALL-CODEX.md`](INSTALL-CODEX.md)
- Maintainer packaging flow: [`RELEASE-PACKAGING.md`](RELEASE-PACKAGING.md)
