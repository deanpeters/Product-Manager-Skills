# PM Skills Rule-of-Thumb Guide (For Non-Technical PMs)

If this all feels messy, use this page first.

---

## 30-Second Decision

1. **I do not code and just want results in chat**  
Use **ChatGPT Projects** (upload a few skill files) or **Claude skill ZIP upload**.

2. **I can use a terminal and want the best quality/control**  
Use **Claude Code** or **Codex** against the local repo.

3. **My company is Microsoft-first**  
Use **M365 Copilot** with approved connectors and governance.

4. **I need automation across tools**  
Use **n8n** with this repo's scripts.

---

## Simple Rule

- **Local repo** = best control and highest quality  
- **ZIP upload** = easiest for non-technical users (Claude skills)  
- **Apps/Connectors/MCP** = best for enterprise integrations and automation

---

## Which Method Should I Pick?

| Situation | Best Choice | Why |
|---|---|---|
| "I just need one PM output today" | ChatGPT Project + upload skill file(s) | Fast start, no code |
| "I use Claude app and want reusable skills" | Claude custom skill ZIP upload | Works with Claude Skills UI |
| "I want best quality and repeatable workflows" | Claude Code or Codex on local repo | Full file access + tight iteration |
| "My org requires enterprise controls" | M365 Copilot (+ approved connectors) | Governance and tenant boundaries |
| "I need pipelines, not one-off chats" | n8n + repo scripts | Repeatable automation |

---

## Beginner Defaults (Use These First)

### Default A: ChatGPT (non-technical)

1. Create a ChatGPT Project.
2. Upload 1-3 skills from `skills/<skill-name>/SKILL.md`.
3. Paste this instruction in Project instructions:

```text
Use uploaded skill files as operating standards.
Follow sections in order: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References.
Ask up to 3 clarifying questions when context is missing.
```

### Default B: Claude (non-technical)

1. Run `./scripts/zip-a-skill.sh --preset core-pm` (or `--skill <skill-name>`).
2. Open `dist/skill-zips/`.
3. Upload the ZIP in Claude Skills settings.

---

## Common Confusions (And Fixes)

- **"Can I sync a local folder straight into chat apps?"**  
Usually no. Use local coding tools, file uploads, or app connections.

- **"Do I need MCP?"**  
No, not to start. MCP is an advanced integration path.

- **"Do I need ZIP files for everything?"**  
No. ZIP is mostly a Claude custom-skills workflow.

- **"Should I use one huge all-in-one skill file?"**  
No. Start with 1-3 focused skills for better output quality.

---

## Where To Go Next

- Claude setup: [`docs/Using PM Skills with Claude.md`](Using%20PM%20Skills%20with%20Claude.md)
- Codex setup: [`docs/Using PM Skills with Codex.md`](Using%20PM%20Skills%20with%20Codex.md)
- ChatGPT setup: [`docs/Using PM Skills with ChatGPT.md`](Using%20PM%20Skills%20with%20ChatGPT.md)
- Build your own skills: [`docs/Building PM Skills.md`](Building%20PM%20Skills.md)
