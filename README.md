# Product Manager Skills

**Product Management skills framework built on battle-tested methods for Claude Code, Cowork, Codex, and AI agents.**

---

## What This Is

A collection of **skills** (structured knowledge modules) that teach AI agents how to perform product management work at a professional level.

Think of these as "specialty training" for AI agents — the PM equivalent of teaching an assistant your company's style guide, decision frameworks, and workflow patterns.

---

## What This Is Not

- ❌ A prompt library (see [Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts) for that)
- ❌ A course or certification program
- ❌ Generic "best practices" fluff

This is **executable PM knowledge** designed to be read and applied by AI agents.

---

## Why Skills > Prompts

**Prompts** are instructions you give per-task.
**Skills** are reusable frameworks the agent learns once and applies across tasks.

Example:
- **Prompt:** "Write a PRD for feature X"
- **Skill:** The agent already knows PRD structure, what questions to ask, how to handle ambiguity, and what good looks like

Skills reduce repetition, improve consistency, and let you work at a higher level of abstraction.

---

## How to Use

### 1. Choose Your Agent
These skills work with:
- **Claude Code** (command-line coding agent)
- **Cowork** (desktop automation agent)
- **OpenAI Codex** (code generation)
- Any AI agent that supports skill/knowledge injection

### 2. Load the Skill
Each skill is a standalone `.md` file in `/skills/`. Load it into your agent's context per the agent's documentation.

### 3. Reference It in Your Work
Once loaded, reference the skill by name in your prompts:

```
Using the Roadmap Planning skill, build a Q2 roadmap for our payments platform.
```

The agent will apply the framework automatically.

---

## Skill Structure

Each skill follows this format:

```
# Skill Name

## Purpose
What this skill does and when to use it.

## Key Concepts
Core frameworks, definitions, and mental models.

## Application
Step-by-step guidance for common scenarios.

## Examples
Real-world cases showing the skill in action.

## Common Pitfalls
What to avoid and why.
```

Clean. Practical. Zero fluff.

---

## Example of Future Skills

| Skill | What It Does |
|-------|--------------|
| `roadmap-planning.md` | Strategic roadmap development and prioritization |
| `prd-authoring.md` | Writing clear, decision-ready product requirements |
| `stakeholder-mapping.md` | Identifying influence, interests, and communication strategies |
| `discovery-interviews.md` | Running effective customer discovery and synthesis |
| `metrics-frameworks.md` | Choosing and interpreting product metrics |
| `market-research.md` | Capturing and distilling market and competitive signals |
| *(more coming)* | |

---

## Contributing

Found a gap? Have a battle-tested PM method you want formalized?

**Open an issue** or **submit a PR** with:
- Skill name
- Use case (when would a PM need this?)
- Your proposed framework (doesn't need to be polished)

We'll collaborate to get it agent-ready.

---

## Philosophy

These skills are built on **25+ years of Productside IP** and real client work across healthcare, finance, manufacturing, and technology.

**Principles:**
- Outcome-driven over output-driven
- Evidence over vibes
- Clarity beats completeness
- Examples beat explanations

No hype. No buzzwords. Just frameworks that work.

---

## Related Resources

- **[Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts)** — Task-specific prompts for ChatGPT, Claude, Gemini
- **[Productside](https://productside.com)** — AI Product Management training and consulting
- **Dean's Substack** — Essays on AI-amplified product work

---

## License

MIT — use it, remix it, make it better.

---

**Questions?** Open an issue or reach out on [LinkedIn](https://linkedin.com/in/deanpeters).
