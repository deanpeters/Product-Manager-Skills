# Install PM Skills in Claude Code

Claude Code users should usually use the existing plugin marketplace path. It keeps terminal workflows clean and preserves the Claude Code installation pattern this repo already supports.

## Install Everything at Once

Want the whole library without picking skills one by one? Install the all-in-one plugin:

```text
/plugin marketplace add deanpeters/Product-Manager-Skills
/plugin install product-manager-skills@pm-skills
/reload-plugins
```

You get all 78 skills and the slash commands in one step.

**Choose one path.** Install the all-in-one plugin, *or* lifecycle bundles, *or* individual skills. Mixing them can load the same skill twice.

## Install One Lifecycle Bundle

The library follows the product lifecycle. Install the bundle for the phase you're in:

| Bundle | Install | Use it for |
|---|---|---|
| Determine | `/plugin install pm-determine@pm-skills` | Strategy, finance, market intelligence, customer context |
| Discover | `/plugin install pm-discover@pm-skills` | Interviews, problem framing, opportunity trees |
| Define | `/plugin install pm-define@pm-skills` | Hypotheses, probes, experiments, positioning |
| Develop | `/plugin install pm-develop@pm-skills` | PRDs, stories, prioritization, roadmaps, AI agents |
| Deliver | `/plugin install pm-deliver@pm-skills` | Pricing, channels, lifecycle and end-of-life |
| Drive | `/plugin install pm-drive@pm-skills` | Stakeholders, influence, career transitions |

```text
/plugin marketplace add deanpeters/Product-Manager-Skills
/plugin install pm-define@pm-skills
/reload-plugins
```

Each bundle includes a few shared helper skills (the facilitation rulebook among them), so it works on its own. If you want several bundles, the all-in-one plugin is simpler: installing multiple bundles repeats those shared helpers once per bundle.

## Install Individual Skills

Prefer to start small? Add the marketplace and install only the skill you need:

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
- You want everything in one step (`product-manager-skills`), one lifecycle bundle, or one skill at a time.
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
