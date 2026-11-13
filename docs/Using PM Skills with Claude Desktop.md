# Using PM Skills with Claude Desktop

Claude Desktop is a strong non-technical path: upload packaged skills, then use them in normal chat.

If this is your first time here, read [`Using PM Skills 101.md`](Using%20PM%20Skills%20101.md) first.

## Best For

- PMs who want point-and-click setup
- Teams that prefer app-based workflows over terminals
- Reusing a small set of core PM skills

## 10-Minute Setup

1. Build a zip for one skill:

```bash
./scripts/zip-a-skill.sh --skill user-story
```

2. In Claude Desktop, open **Settings → Capabilities → Skills**.
3. Upload the zip from `dist/skill-zips/`.
4. Start with a practical prompt:

```text
Use the user-story skill to write stories for improving account setup completion.
```

## Good Starter Packs

- Single skill for focused work:

```bash
./scripts/zip-a-skill.sh --skill prioritization-advisor
```

- Curated starter set:

```bash
./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips
```

## How To Keep Output Quality High

- Upload 1-3 skills first, not the whole library.
- For interactive skills, let the assistant ask its questions before forcing output.
- Give specific constraints (segment, KPI, deadline, dependencies).

## Common Pitfalls

- Uploading source folders directly instead of packaged zip files.
- Expecting GitHub auto-sync after upload.
- Using vague prompts without business context.

## Learn More (Official)

- Using Skills in Claude: [https://support.claude.com/en/articles/12512180-using-skills-in-claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Claude desktop app download: [https://claude.ai/download](https://claude.ai/download)
- Anthropic MCP docs (advanced integration): [https://docs.anthropic.com/en/docs/mcp](https://docs.anthropic.com/en/docs/mcp)

## PM Skills Links

- Claude umbrella guide: [`Using PM Skills with Claude.md`](Using%20PM%20Skills%20with%20Claude.md)
- Packaging helper details: [`../scripts/package-claude-skills.sh`](../scripts/package-claude-skills.sh)
