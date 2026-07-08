# Start Here

If you are new to this repo, you are in the right place.

You do **not** need to be a programmer to use PM Skills well.

## New in v0.65

You asked, we listened. We took a moment to create comprehensive instructions on how to install, integrate, or otherwise use any one or all of these skills.

Start here:
- `docs/Using PM Skills 101.md`
- `docs/Platform Guides for PMs.md`
- `docs/Using PM Skills with Slash Commands 101.md`

## 0) Read This First (2 Minutes)

- Beginner guide: `docs/Using PM Skills 101.md`
- Platform chooser: `docs/Platform Guides for PMs.md`

If you only remember one thing:
- Pick **one skill**
- Give **one real business problem**
- Ask for **clarifying questions first**

## 1) Choose Your Comfort Level

### A) "I just want results in chat" (non-technical)

Start with:
- `Claude Desktop`: `docs/Using PM Skills with Claude Desktop.md`
- `ChatGPT Desktop`: `docs/Using PM Skills with ChatGPT Desktop.md`

Copy/paste starter prompt:

```text
Use the uploaded PM skill as my framework.
Ask up to 3 clarifying questions first.
Then produce the final output in markdown.
End with assumptions, risks, and next steps.
```

### B) "I can use a terminal" (higher control)

Start with:
- `Claude Code`: `docs/Using PM Skills with Claude Code.md`
- `Claude /slash commands`: `docs/Using PM Skills with Slash Commands 101.md`
- `Codex`: `docs/Using PM Skills with Codex.md`
- `OpenCode`: `docs/INSTALL-OPENCODE.md`

Copy/paste starter prompt:

```text
Using skills/prioritization-advisor/SKILL.md, help me choose a framework for 12 requests and one sprint.
Ask questions one at a time, then give numbered recommendations.
```

### C) "I need repeatable workflows" (automation)

Start with:
- `n8n`: `docs/Using PM Skills with n8n.md`
- `LangFlow`: `docs/Using PM Skills with LangFlow.md`
- `Python agents`: `docs/Using PM Skills with Python Agents.md`

### D) "I’m experimenting with alternative agent stacks"

Start with:
- `OpenClaw`: `docs/Using PM Skills with OpenClaw.md`
- `Claude Cowork`: `docs/Using PM Skills with Claude Cowork.md`

## 2) Pick Your First Outcome

### I need a PM artifact

```bash
./scripts/run-pm.sh skill user-story "Write stories for a new account settings page"
```

### I need help deciding

```bash
./scripts/run-pm.sh skill prioritization-advisor "We have 12 requests and one sprint"
```

### I need end-to-end guidance

```bash
./scripts/run-pm.sh command discover "Reduce onboarding drop-off for self-serve users"
```

## 3) Find The Right Skill Fast

```bash
./scripts/find-a-skill.sh --keyword onboarding
./scripts/find-a-command.sh --keyword roadmap
./scripts/find-a-command.sh --list-all
```

## 4) If You Feel Stuck

- Start with one simple request and one skill file.
- Use real context (segment, KPI, timeline).
- Ask the assistant to explain assumptions before drafting.
- Use `docs/Using PM Skills 101.md` as your baseline guide.

## 5) Full Guides

- Beginner onboarding: `docs/Using PM Skills 101.md`
- Platform index for PMs: `docs/Platform Guides for PMs.md`
- Claude Code: `docs/Using PM Skills with Claude Code.md`
- Claude /slash commands: `docs/Using PM Skills with Slash Commands 101.md`
- Codex: `docs/Using PM Skills with Codex.md`
- OpenClaw: `docs/Using PM Skills with OpenClaw.md`
- Claude Cowork: `docs/Using PM Skills with Claude Cowork.md`
- Claude Desktop: `docs/Using PM Skills with Claude Desktop.md`
- ChatGPT Desktop: `docs/Using PM Skills with ChatGPT Desktop.md`
- n8n: `docs/Using PM Skills with n8n.md`
- LangFlow: `docs/Using PM Skills with LangFlow.md`
- Python agents: `docs/Using PM Skills with Python Agents.md`
- Cursor: `docs/Using PM Skills with Cursor.md`
- Windsurf: `docs/Using PM Skills with Windsurf.md`
- Bolt: `docs/Using PM Skills with Bolt.md`
- Replit Agent: `docs/Using PM Skills with Replit Agent.md`
- Make.com: `docs/Using PM Skills with Make.com.md`
- Devin: `docs/Using PM Skills with Devin.md`
- CrewAI: `docs/Using PM Skills with CrewAI.md`
- Gemini: `docs/Using PM Skills with Gemini.md`
- ChatGPT (all options): `docs/Using PM Skills with ChatGPT.md`
- Claude (all options): `docs/Using PM Skills with Claude.md`
- Non-technical setup chooser: `docs/PM Skills Rule-of-Thumb Guide.md`
- Multi-tool operating model: `docs/PM Tooling Operations Charter.md`
