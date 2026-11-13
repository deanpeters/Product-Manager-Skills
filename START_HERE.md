# Start Here

If you are new here, you are in the right place. This library gives your AI assistant ready-made PM skills: short instruction files that teach it how to do one PM job well.

You do **not** need to be a programmer to use PM Skills well.

## Find your place in the lifecycle

The skills are grouped by where they fit in product work, in the order it tends to unfold:

1. **Determine**: set the outcome and read the market
2. **Discover**: find the real problem
3. **Define**: shape a solution and test the bet
4. **Develop**: turn it into buildable work
5. **Deliver**: price it, take it to market, retire it well

A sixth group, **Drive**, runs underneath all five: your stakeholders and your career.

It's a cycle, not a line, so loop back whenever the evidence says to. Not sure where you are? Pick the phase that sounds like your week. The full map, with a "start with" skill for each, is in the [README](README.md#browse-by-lifecycle).

Setup guides, if you want them:
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

### B) "I am comfortable in a terminal" (higher control)

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

*These commands need a terminal. In a chat app, skip to the next section and just ask in plain words, for example "Write user stories for a new account settings page."*

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

*Terminal only. In chat, ask: "Which PM skill fits this situation?" and describe it.*

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
- `Claude Desktop`: `docs/Using PM Skills with Claude Desktop.md`
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
