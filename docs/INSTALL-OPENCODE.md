# Install PM Skills in OpenCode

[OpenCode](https://opencode.ai) is an open-source AI coding agent. It reads skills in the same `SKILL.md` format this library uses, so **there is nothing to convert**. You only need to put the skill folders where OpenCode looks.

> Contributed by [@dNzZiz](https://github.com/dNzZiz) (PR #20). Thank you for pushing OpenCode support forward.

## Why no changes to the skills are needed

OpenCode needs only a `description` to advertise a skill, and it ignores frontmatter fields it doesn't use. Our extra fields (`type`, `intent`, `best_for`, `scenarios`, and so on) are harmless there. That's why this library stays runtime-agnostic: one format, every agent.

## Option 1: Install globally (every project)

From a clone of this repo:

```bash
mkdir -p ~/.config/opencode/skills
cp -r skills/* ~/.config/opencode/skills/
```

Want only a few? Copy the folders you want:

```bash
cp -r skills/user-story skills/prd-development ~/.config/opencode/skills/
```

## Option 2: Install in one project

From your project root, with this repo cloned alongside it:

```bash
mkdir -p .opencode/skills
cp -r ../Product-Manager-Skills/skills/* .opencode/skills/
```

## Option 3: Reuse the Codex ZIP

OpenCode also reads `.agents/skills/` natively. If you already use the [Codex ZIP](INSTALL-CODEX.md) (`pm-skills-codex.zip`), unzip it into your project root and OpenCode will find the skills with no further setup.

## Where OpenCode looks

| Scope | Folders it reads |
|---|---|
| Global | `~/.config/opencode/skills`, plus `~/.claude/skills` and `~/.agents/skills` |
| Project | `.opencode/skills`, plus `.claude/skills` and `.agents/skills` |

If you already installed these skills for Claude Code in `~/.claude/skills`, OpenCode will pick them up without a second copy. When the same skill name appears in more than one place, the more specific folder wins: project `.opencode/skills` beats global `~/.config/opencode/skills`, which beats the `.claude` and `.agents` folders.

## Use a skill

OpenCode shows the agent each skill's name and description, and the agent loads the full skill when it's relevant. You can also ask for one directly:

```text
Use the jobs-to-be-done skill to analyze this customer problem.
```

Or mention it by name with `@`, for example `@user-story`.

**Not sure which skill?** Ask: "Which PM skill fits this situation?" and describe what you're trying to do. The skill descriptions are written as "use when..." triggers, so the agent can match them.

## Limiting which skills an agent can load (optional)

OpenCode lets you allow, ask, or deny skills per agent. The configuration syntax has changed between OpenCode versions, so use [OpenCode's skills documentation](https://opencode.ai/docs/skills/) as the source of truth rather than copying a snippet from here.

## Troubleshooting

- **A skill doesn't show up:** confirm the folder contains `SKILL.md` (uppercase), for example `~/.config/opencode/skills/user-story/SKILL.md`, and restart OpenCode.
- **You see an old version:** a copy in a higher-precedence folder is overriding the one you just installed. Check the project `.opencode/skills` folder first.
- **Updating:** pull the latest repo and copy the folders again.

## Notes

- Treat `skills/` as the source library.
- For Claude Desktop/Web, use the Claude ZIP packs. See [`INSTALL-CLAUDE-DESKTOP.md`](INSTALL-CLAUDE-DESKTOP.md).
- For Claude Code, use the plugin marketplace. See [`INSTALL-CLAUDE-CODE.md`](INSTALL-CLAUDE-CODE.md).
