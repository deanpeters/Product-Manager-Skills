# Using PM Skills 101

**Repository:** [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills)
**Skills available:** 95 | **Works with:** Claude, Codex, ChatGPT, Cowork, n8n, LangFlow, Lovable, OpenClaw, Cursor, Windsurf, Bolt, Replit, Make.com, Devin, CrewAI, Gemini

---

## What Is a Skill?

A skill is a structured markdown file (`SKILL.md`) that teaches an AI agent how to do a specific PM task — the right way, every time, without you explaining your process from scratch.

Instead of saying *"Write a PRD"* and hoping for the best, the agent already knows:
- How to structure the document
- What questions to ask stakeholders
- Which framework to apply and when
- What good looks like — and what to avoid

**Skills = Less explaining. More strategic work.**

### Prompts vs. Skills

| Prompts | Skills |
|---|---|
| One-time instructions per task | Reusable frameworks loaded once |
| You repeat yourself constantly | Agent remembers best practices |
| "Write a PRD for X" — hope for the best | Agent knows structure, asks smart questions |
| Inconsistent outputs every time | Consistent, professional results |

---

## Three Skill Types

Skills are organized into three tiers that build on each other.

### 🧱 Component Skills (36) — Templates & Artifacts
**When to use:** You need a standard template for a specific deliverable.
**Time:** 10–30 minutes
**Example:** "Write a user story" → `user-story` skill

### 🔄 Interactive Skills (34) — Guided Discovery
**When to use:** You need help deciding which approach to take before executing.
**Time:** 30–90 minutes
**Example:** "Which prioritization framework should I use?" → `prioritization-advisor` skill asks 3–5 questions about your context, then recommends RICE, ICE, Kano, or others.

### 🎭 Workflow Skills (25) — End-to-End Processes
**When to use:** You need to run a full PM workflow from start to finish.
**Time:** Days to weeks
**Example:** "Align stakeholders on product strategy" → `product-strategy-session` skill guides you through positioning → problem framing → solution exploration → roadmap.

---

## Platform-by-Platform Installation Guide

---

### ◈ Claude.ai / Claude Desktop
*Paste, upload, or ZIP — no CLI needed*

**What "loading a skill" means here:** Claude.ai has no persistent skill memory between conversations by default. Loading a skill means getting the `SKILL.md` content into your active context — by pasting it, attaching it as a file, or uploading a ZIP Claude can read.

#### Option 1 — Paste the skill directly
1. Go to `github.com/deanpeters/Product-Manager-Skills`
2. Open any skill folder (e.g. `skills/user-story/SKILL.md`)
3. Click **Raw** → Select All → Copy
4. Start a Claude conversation and paste: `"Read this skill:"` then paste the content
5. Invoke: `"Using the User Story skill, write stories for our checkout flow"`

#### Option 2 — Upload a skill ZIP
1. Clone the repo locally
2. Run: `./scripts/zip-a-skill.sh --skill user-story`
3. This creates a ZIP in `dist/skill-zips/`
4. Attach the ZIP file to your Claude.ai message
5. Say: `"Read the SKILL.md inside this ZIP and apply it to [your task]"`

#### Option 3 — Core PM starter pack
1. Run: `./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips`
2. This builds a curated ZIP of essential PM skills
3. Upload that one ZIP to Claude.ai
4. All core PM skills are now available for the session

#### Invoking a skill
```
"Using the Prioritization Advisor skill, help me pick a framework for our Q3 roadmap."

"Run the POL Probe skill on this hypothesis:
 Users abandon checkout because shipping cost surprises them."

"Apply the User Story skill to these epics: [paste epics]"
```

> **Pro tip:** Load multiple skills in one conversation. Paste `user-story.md` and `user-story-splitting.md` together, then ask Claude to use both when breaking down an epic. Claude handles the orchestration.

---

### ⌘ Claude Code (CLI)
*Native CLI — the sharpest integration*

**Why this is the cleanest fit:** Claude Code reads your local filesystem. Skills live in the repo. No uploading, no copy-pasting. Discover skills via `npx`, invoke from the CLI, and use `CLAUDE.md` to keep skills loaded across the entire session.

If you want one-command shortcuts like `/pm-story` and `/pm-prd`, also see [`Using PM Skills with Slash Commands 101.md`](Using%20PM%20Skills%20with%20Slash%20Commands%20101.md).

#### Setup
```bash
# Clone the repo
git clone https://github.com/deanpeters/Product-Manager-Skills
cd Product-Manager-Skills

# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Discover skills
npx skills find prioritization
npx skills find --type interactive

# Add from this repo
npx skills add deanpeters/Product-Manager-Skills --list
```

#### Invoking skills from the CLI
```bash
# Workflow skill
claude "Using the PRD Development workflow, create a PRD for our mobile notifications feature"

# Interactive skill
claude "Run the Prioritization Advisor — help me rank these 8 features for Q2"

# Component skill
claude "Using the User Story skill, write stories for the checkout epic in JIRA-42"

# Point at a specific skill file
claude --context skills/pol-probe/SKILL.md "Apply this to my hypothesis: [hypothesis]"
```

#### CLAUDE.md — persistent skill loading
1. Create a `CLAUDE.md` file in your project root
2. Reference the skills you want always active
3. Claude Code reads `CLAUDE.md` automatically at session start
4. Skills stay loaded for the entire session — no re-pasting

#### CLAUDE.md example
```markdown
# CLAUDE.md

## Active PM Skills
- skills/user-story/SKILL.md
- skills/prioritization-advisor/SKILL.md
- skills/prd-development/SKILL.md

## Project Context
Product: Checkout redesign
Team: 4 PMs, 2 designers, 8 engineers
Sprint: Epic decomposition for Q2
```

> **Pro tip:** Use `AGENTS.md` (in the repo root) for multi-agent orchestration — it tells Claude Code how to chain skills across a workflow so you can run a discovery-to-PRD pipeline in one session.

---

### ⬡ Cowork
*Knowledge modules + natural language invocation*

**How Cowork handles skills:** Cowork treats skills as knowledge modules — structured documents agents reference when executing tasks. Import them once per workspace, then invoke by name or describe the task and the agent picks the right skill.

#### Importing a skill
1. In your Cowork workspace, open **Knowledge** or **Files**
2. Upload the `SKILL.md` file for any skill you want
3. Or upload a full ZIP package for a skill bundle
4. Name the module clearly (e.g. `PM Skill: User Story`)
5. Enable it for the agents or automations that should use it

#### Invoking a skill
```
"Write a user story for our onboarding flow using the User Story skill"

"Run the Prioritization Advisor and help me rank these 8 features for Q2"

"Apply the POL Probe framework to this hypothesis: [hypothesis text]"
```

#### Using skills in automations
1. Create a new automation in Cowork
2. Add an AI step and select your Claude agent
3. Reference the skill by name in the system prompt
4. Attach the `SKILL.md` as context to that AI step
5. Trigger via task, form, or schedule

#### System prompt pattern for automations
```
You have access to the User Story skill. When asked to write user stories,
apply the framework in your knowledge module 'PM Skill: User Story' exactly.

Always produce: role, action, value, and Gherkin acceptance criteria for each story.
```

> **Pro tip:** Import a skill bundle — component + interactive + workflow for one domain — rather than individual files. Cowork agents learn which tier to use based on task complexity.

---

### ⧉ Codex / ChatGPT
*GitHub connections, Custom GPTs, or Project files*

**Three ways to load skills:** GitHub app connections (best for Codex CLI), Custom GPT Knowledge uploads (best for reusable team GPTs), and Project files (best for ongoing work).

#### Option 1 — GitHub connection (Codex)
1. In ChatGPT, connect GitHub under **Settings → Integrations**
2. Give Codex access to your fork of `Product-Manager-Skills`
3. In a Codex session, reference skills by file path
4. Codex reads the repo directly — no uploads needed

```
"Using skills/user-story/SKILL.md, write user stories for the feature in docs/checkout-epic.md"

"Apply skills/prd-development/SKILL.md to this problem brief: [paste brief]"

"Run skills/prioritization-advisor/SKILL.md and help me rank: [paste backlog items]"
```

#### Option 2 — Custom GPT Knowledge upload
1. Go to **ChatGPT → My GPTs → Create a GPT**
2. Under **Knowledge**, upload the `SKILL.md` files you want
3. Or upload a skill ZIP (ChatGPT extracts it automatically)
4. In GPT instructions, tell it to apply the skill by name
5. Save and share the Custom GPT with your team

#### Option 3 — ChatGPT Projects
1. Create a new Project in ChatGPT
2. Upload `SKILL.md` files to the project's **Files** section
3. All conversations in that project have the skills loaded
4. Best for team projects where everyone uses the same PM frameworks

> **Pro tip:** Don't upload the whole library to one Custom GPT. Build focused GPTs: a "Discovery GPT" with `discovery-process` + `pol-probe` + `opportunity-solution-tree`, and a "Roadmap GPT" with `prioritization-advisor` + `roadmap-planning`.

---

### ⟁ n8n
*AI Agent nodes + skill injected as system prompt*

**How skills work in n8n:** n8n doesn't natively understand skill files — but your AI Agent nodes do. Pass the skill content as a system prompt or inject it into a prompt template. The LLM applies the framework to whatever data flows through.

#### Method 1 — Hardcode skill in system prompt
```
// In your AI Agent node's System Prompt field:

You are a PM assistant. Apply this User Story skill to every request:

---
[Paste the full content of skills/user-story/SKILL.md]
---

When given an epic, generate formatted user stories with Gherkin acceptance criteria.
```

#### Method 2 — HTTP Request to fetch skill dynamically
```
// HTTP Request node:
Method: GET
URL: https://raw.githubusercontent.com/deanpeters/Product-Manager-Skills/main/skills/user-story/SKILL.md

// AI Agent node System Prompt:
"Apply this skill framework: " + {{ $node['FetchSkill'].json.data }}

// User message:
{{ $json.input }}
```

#### Method 3 — Read File node (local clone)
1. Clone the repo to your n8n server or local machine
2. Add a **Read File** node early in your workflow
3. Point it at the `SKILL.md` file path
4. Pass the content as a variable to your AI Agent node
5. Inject via: `{{$node['ReadSkill'].json['data']}}` in the system prompt

#### Recommended workflow pattern
1. **Trigger:** Webhook, form, Jira event, or schedule
2. **Fetch skill:** HTTP Request or Read File node
3. **Prepare input:** format incoming data for the LLM
4. **AI Agent:** inject skill + input, generate structured output
5. **Route output:** Slack, email, Jira, Notion — wherever it belongs

> **Pro tip:** Build a "skill loader" sub-workflow that fetches and caches skill content. Reference it from multiple main workflows via n8n's **Execute Workflow** node — skill updates propagate everywhere automatically.

---

### ⌬ LangFlow
*Document nodes injected into prompt templates*

**How skills work in LangFlow:** LangFlow is a visual LLM pipeline builder. Skills become Text Input or File nodes that feed into your Prompt Template. The LLM applies the skill framework to whatever input hits that chain.

#### Method 1 — Text Input node (simplest)
1. Add a **Text Input** node to your flow
2. Paste the full `SKILL.md` content into the default value field
3. Label it clearly (e.g. `User Story Skill`)
4. Connect it to a **Prompt Template** node
5. In the template, reference it as `{skill_content}`

#### Method 2 — URL Loader node
1. Add a **URL Loader** node to your flow
2. Point it at the raw GitHub URL of the `SKILL.md` file
3. Connect its output to a **Prompt Template** node
4. Skills update automatically when the repo changes

#### Prompt template pattern
```
System: You are a PM assistant. Use the following skill framework to complete all requests:

{skill_content}

---
User request: {user_input}

Apply the skill framework above to complete the request.
```

#### Chaining skills in LangFlow
1. Create separate Text Input nodes for each skill
2. Use a **Merge** node to combine them into one context block
3. Feed the merged context into a single Prompt Template
4. The LLM applies whichever skill is relevant to the request

> **Pro tip:** Skills are short enough to fit in a single context window — no chunking needed. Load 3–5 related skills together and let the LLM decide which to apply based on the request type.

---

### ◇ Lovable
*Attach skills as project knowledge, invoke by name*

**How skills work in Lovable:** Lovable (the AI app builder) accepts knowledge files and instructions alongside your build requests. Load a PM skill to shape how the AI frames the product problem before generating the app or feature.

#### Attaching a skill
1. In Lovable, open your project or start a new one
2. Use the attachment or knowledge feature to upload the `SKILL.md` file
3. Or paste the skill content directly into your opening prompt
4. Reference the skill by name in your build request

#### Invoking a skill in a build prompt
```
"Before we start building, apply the Problem Statement skill to frame this:
 [describe the problem]"

"Using the User Story skill I've attached, define the user stories for this feature,
 then build a UI prototype that satisfies story #1"

"Apply the POL Probe skill to my hypothesis, then build a lightweight prototype
 we can use to test it"
```

#### Best use case: skills before the build
1. Frame the problem with `problem-statement` or `pol-probe` skill first
2. Let Lovable generate the prototype
3. Use the `user-story` skill to define acceptance criteria for the next iteration
4. This turns Lovable from vibe-coding into structured, hypothesis-driven prototyping

> **Pro tip:** Most PMs skip straight to "build me X." Loading a `problem-statement` or `pol-probe` skill forces the right conversation before any code gets generated — and the prototype you get back is actually testing something.

---

### ⚙ OpenClaw
*Load via system prompt or runtime skill router*

**How skills work in OpenClaw:** OpenClaw is a Claude-compatible agent framework. Load skills by injecting `SKILL.md` content into the system prompt at agent initialization, or build a skill router that selects and loads the right skill per request.

#### Option 1 — System prompt injection
```json
{
  "system_prompt": "You are a PM assistant with access to the following skills. Apply the relevant skill based on the task type:\n\n[paste SKILL.md content here]",
  "model": "claude-sonnet-4-20250514"
}
```

#### Option 2 — Runtime skill loader (Python)
```python
# skills_loader.py
def load_skill(skill_name: str) -> str:
    path = f"skills/{skill_name}/SKILL.md"
    with open(path, "r") as f:
        return f.read()

def build_prompt(skill_name: str, user_input: str) -> str:
    skill = load_skill(skill_name)
    return f"Apply this skill:\n{skill}\n\nTask: {user_input}"
```

#### Skill routing by task type
```python
SKILL_ROUTER = {
    "user story":   "user-story",
    "prioritize":   "prioritization-advisor",
    "prd":          "prd-development",
    "discovery":    "discovery-process",
    "hypothesis":   "pol-probe",
    "roadmap":      "roadmap-planning",
}

# Match request keywords -> load skill -> execute
```

> **Pro tip:** Pair the skill router with `AGENTS.md` in the repo root for multi-skill orchestration patterns — it documents how skills are meant to chain across a full workflow.

---

## Quick Reference

### Most Common Skills to Start With

| Task | Skill | Type |
|---|---|---|
| Write a user story | `user-story` | Component |
| Break down a large epic | `epic-breakdown-advisor` | Interactive |
| Pick a prioritization framework | `prioritization-advisor` | Interactive |
| Test a hypothesis before building | `pol-probe` + `pol-probe-advisor` | Component + Interactive |
| Frame a customer problem | `problem-statement` | Component |
| Write a full PRD | `prd-development` | Workflow |
| Plan a quarterly roadmap | `roadmap-planning` | Workflow |
| Run customer discovery | `discovery-process` | Workflow |
| Assess your AI readiness | `ai-shaped-readiness-advisor` | Interactive |

### Useful Scripts (from local clone)

```bash
# Find a skill by keyword or type
./scripts/find-a-skill.sh --keyword pricing --type interactive

# Build a ZIP for one skill
./scripts/zip-a-skill.sh --skill user-story

# Build ZIPs for all skills
./scripts/zip-a-skill.sh --all --output dist/skill-zips

# Build a curated starter pack
./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips

# Test a skill for conformance
./scripts/test-a-skill.sh --skill user-story --smoke
```

---

### ✦ Cursor
*Rules files + `@` file references — no slash commands, same outcome*

Detailed guide: [`Using PM Skills with Cursor.md`](Using%20PM%20Skills%20with%20Cursor.md)

**How Cursor handles skills:** Cursor doesn't have a native slash command system for custom prompts. Instead it uses `.cursorrules` for persistent instructions and `@filename` references to pull specific files into the prompt context on demand. Both routes work well for PM skills.

#### Option 1 — `.cursorrules` (persistent, session-wide)
1. Create a `.cursorrules` file in your project root
2. Paste the contents of the skill(s) you want always active
3. Or reference the skill file path and instruct Cursor to load it at start
4. Every Cursor prompt in that project will have the skill in context

#### `.cursorrules` example
```
## Active PM Skills

You have access to the following PM frameworks. Apply the relevant one
based on the task type without being asked.

### User Story Skill
[Paste contents of skills/user-story/SKILL.md here]

### Prioritization Advisor Skill
[Paste contents of skills/prioritization-advisor/SKILL.md here]
```

#### Option 2 — `@file` reference (on demand)
```
# In the Cursor prompt bar, reference the skill directly:

@skills/user-story/SKILL.md
Write user stories for our checkout abandonment epic.

@skills/pol-probe/SKILL.md
Design a validation experiment for this hypothesis: [hypothesis]
```

#### Option 3 — Store skills in a `prompts/` folder
1. Create a `prompts/` folder in your project root
2. Copy `SKILL.md` files there with descriptive names (e.g. `prompts/user-story.md`)
3. Reference with `@prompts/user-story.md` in any Cursor prompt
4. Easier to manage than pasting into `.cursorrules` for large skill sets

> **Pro tip:** Put your highest-frequency skills (user-story, prioritization-advisor) in `.cursorrules` so they're always available. Put situational skills (prd-development, discovery-process) in `prompts/` and pull them with `@` only when needed.

---

### ✦ Windsurf
*Cascade rules + `@` file references — nearly identical to Cursor*

Detailed guide: [`Using PM Skills with Windsurf.md`](Using%20PM%20Skills%20with%20Windsurf.md)

**How Windsurf handles skills:** Windsurf uses a `WINDSURF_RULES` file (or `.windsurfrules`) for persistent Cascade instructions — the functional equivalent of Cursor's `.cursorrules`. The `@` file reference pattern works the same way.

#### Setup
1. Create `.windsurfrules` in your project root
2. Paste skill content or add instructions referencing skill files
3. Windsurf's Cascade agent reads it at session start

#### `.windsurfrules` example
```
## PM Skills Active in This Project

You are a PM assistant with access to the following frameworks.
Apply them without being explicitly asked when the task context matches.

### User Story Skill
[Paste contents of skills/user-story/SKILL.md]

### Problem Statement Skill
[Paste contents of skills/problem-statement/SKILL.md]
```

#### On-demand via `@` reference
```
@skills/prioritization-advisor/SKILL.md
Help me rank these 10 features for Q2 — we're post-PMF, 3 squads, hard June date.

@skills/epic-breakdown-advisor/SKILL.md
Split this epic: [paste epic description]
```

> **Pro tip:** Windsurf's Cascade is strong at multi-step agentic tasks. Workflow skills (`prd-development`, `discovery-process`) shine here — paste the full workflow skill into `.windsurfrules` and let Cascade run the phases autonomously.

---

### ◇ Bolt.new
*Paste skill into the opening prompt — frame before you build*

Detailed guide: [`Using PM Skills with Bolt.md`](Using%20PM%20Skills%20with%20Bolt.md)

**How Bolt handles skills:** Bolt.new is a prompt-to-app builder. It doesn't have a persistent knowledge layer, so skills go directly into your opening prompt. The key insight: use skills to frame the product problem *before* Bolt generates any code.

#### The PM-first pattern
```
# Step 1 — Frame with a skill before building:

I'm going to build [feature]. Before you generate any code, apply this
Problem Statement skill to make sure we're solving the right problem:

[Paste contents of skills/problem-statement/SKILL.md]

Problem context: [describe the problem]

Ask me what you need, then we'll move to building.
```

#### Invoking skills inline
```
"Apply the User Story skill below to define what we're building,
 then generate a prototype that satisfies story #1:

[Paste skills/user-story/SKILL.md]

Feature: self-serve seat management for enterprise admins"
```

#### Best skills for Bolt
| Skill | Why It Works in Bolt |
|---|---|
| `problem-statement` | Prevents building the wrong thing from the first prompt |
| `pol-probe` | Turns the Bolt prototype into a real validation experiment |
| `user-story` | Gives Bolt acceptance criteria to build against, not just vibes |
| `proto-persona` | Gets a real user archetype in context before UI decisions are made |

> **Pro tip:** Bolt's sweet spot is rapid prototyping. Skills make those prototypes *testable* rather than just impressive. The `pol-probe` skill is particularly powerful here — it defines what the prototype needs to prove before a single component gets generated.

---

### ◇ Replit (Replit Agent)
*System prompt injection or inline pasting — best for iterative builds*

Detailed guide: [`Using PM Skills with Replit Agent.md`](Using%20PM%20Skills%20with%20Replit%20Agent.md)

**How Replit Agent handles skills:** Replit Agent supports persistent instructions via a system prompt field in Agent settings. You can also paste skills inline per prompt. For PM work, the system prompt route is cleaner since it keeps the framework active across the entire build session.

#### Option 1 — Agent system prompt (persistent)
1. Open Replit Agent for your project
2. Go to **Agent Settings → System Prompt**
3. Paste the skill content you want active for the session
4. Every Agent prompt in that session applies the skill framework

#### System prompt example
```
You are a PM assistant and developer. Before generating any code or UI,
apply the following User Story skill to define what you're building:

[Paste skills/user-story/SKILL.md]

Do not generate code until the user has confirmed the user stories
and acceptance criteria are correct.
```

#### Option 2 — Inline per prompt
```
"Apply this skill to define the stories before building:

[Paste skills/user-story/SKILL.md]

Feature: push notification preferences for mobile users"
```

#### Replit-specific workflow
1. Use `problem-statement` or `pol-probe` skill to frame the problem
2. Use `user-story` skill to define what the Agent should build
3. Let Agent build the prototype
4. Use `epic-breakdown-advisor` to plan the next iteration

> **Pro tip:** Replit Agent is especially useful in training contexts with non-technical PMs who want to prototype fast. Skills prevent "just build something cool" from replacing actual product thinking.

---

### ⟁ Make.com
*HTTP modules + skill content piped into AI modules*

Detailed guide: [`Using PM Skills with Make.com.md`](Using%20PM%20Skills%20with%20Make.com.md)

**How Make.com handles skills:** Make.com (formerly Integromat) is a no-code automation platform. Like n8n, it doesn't natively understand skill files — but its **OpenAI**, **Anthropic Claude**, or **HTTP** modules accept prompt text, which is where skill content goes.

#### Method 1 — Hardcode skill in the AI module's system prompt
1. Add a **Claude** or **OpenAI** module to your scenario
2. In the **System Prompt** field, paste the full `SKILL.md` content
3. In the **User Message** field, pass the incoming data: `{{1.text}}` or similar
4. The AI applies the skill framework to every item that flows through

#### Method 2 — Fetch skill dynamically via HTTP module
1. Add an **HTTP → Make a Request** module at the start of your scenario
2. Set Method: `GET`
3. URL: `https://raw.githubusercontent.com/deanpeters/Product-Manager-Skills/main/skills/user-story/SKILL.md`
4. Store the response body as a variable
5. In your AI module's System Prompt: `Apply this skill: {{skill_content}}`

#### Recommended Make.com scenario pattern
```
Trigger (webhook / form / Google Sheets row)
  ↓
HTTP module — fetch SKILL.md from GitHub
  ↓
Claude/OpenAI module — skill + input → structured output
  ↓
Route output to Slack / Notion / Jira / email
```

#### Best use cases for Make.com + skills
| Trigger | Skill | Output Destination |
|---|---|---|
| New Jira epic created | `user-story` | Post draft stories back to Jira |
| Form submission (feature request) | `problem-statement` | Notion database |
| Weekly schedule | `prioritization-advisor` | Slack digest |
| Stakeholder email received | `pol-probe` | Draft validation experiment doc |

> **Pro tip:** Make.com's visual interface makes it easy to show PMs how skills plug into existing workflows. It's a strong training demo platform — the scenario is self-documenting and the flow is legible without any code.

---

### ⚙ Devin
*Skills as background context — load via file access or session instructions*

Detailed guide: [`Using PM Skills with Devin.md`](Using%20PM%20Skills%20with%20Devin.md)

**How Devin handles skills:** Devin is an autonomous software engineering agent from Cognition. It operates with access to your codebase and can read files directly. For PM work, the most effective pattern is giving Devin access to skill files as reference documents it consults when completing PM-adjacent tasks (writing specs, creating docs, defining acceptance criteria).

#### Option 1 — Include skills in the repo Devin accesses
1. Clone or add `Product-Manager-Skills` as a submodule in your project repo
2. Give Devin access to the repo as you normally would
3. In your Devin session prompt, reference the skill file explicitly
4. Devin reads and applies it as part of its task execution

#### Session prompt pattern
```
Before writing any code for this feature, read the skill file at
skills/user-story/SKILL.md and generate user stories with acceptance
criteria. Get my confirmation before proceeding to implementation.

Feature: [describe feature]
```

#### Option 2 — Paste skill into session instructions
```
You have access to the following User Story framework. Apply it to
define acceptance criteria for any feature before writing tests or code:

[Paste skills/user-story/SKILL.md]

Current task: implement seat management for enterprise accounts.
Start by generating the user stories. Wait for approval before coding.
```

#### Where skills add the most value with Devin
| Task | Skill | Why |
|---|---|---|
| Pre-implementation spec | `user-story` + `epic-breakdown-advisor` | Ensures Devin builds the right thing at the right scope |
| Problem framing before sprint | `problem-statement` | Stops Devin from optimizing a solution to the wrong problem |
| Hypothesis validation prototype | `pol-probe` | Tells Devin what the prototype needs to prove, not just what to build |
| PRD-as-code generation | `prd-development` | Gives Devin a structured output format, not a blank page |

> **Pro tip:** Devin is powerful but autonomous. Skills act as guardrails — they inject the PM's framework into Devin's task context so it operates within a structured process, not just toward a vague output.

---

### ⬡ CrewAI
*Skills as agent role definitions or task context — load via crew config*

Detailed guide: [`Using PM Skills with CrewAI.md`](Using%20PM%20Skills%20with%20CrewAI.md)

**How CrewAI handles skills:** CrewAI is a multi-agent orchestration framework. Each agent in a crew has a role, goal, and backstory. Skills map cleanly to agent roles — a skill *is* the framework an agent uses to complete its assigned task. The repo's `AGENTS.md` file documents orchestration patterns designed with CrewAI-style flows in mind.

#### Mapping skills to agents

| CrewAI Agent | PM Skill | Role Assignment |
|---|---|---|
| Discovery Agent | `discovery-process` | Runs customer research and synthesizes findings |
| Story Writer Agent | `user-story` | Converts epics and research into sprint-ready stories |
| Prioritization Agent | `prioritization-advisor` | Ranks backlog items using the recommended framework |
| Validation Agent | `pol-probe` | Designs experiments to test assumptions before build |
| Strategy Agent | `product-strategy-session` | Aligns positioning, problem framing, and roadmap |

#### Agent definition with skill as backstory
```python
from crewai import Agent

story_writer = Agent(
    role="PM Story Writer",
    goal="Convert epics and feature briefs into sprint-ready user stories with acceptance criteria",
    backstory=open("skills/user-story/SKILL.md").read(),
    verbose=True,
    llm=your_llm
)

validation_agent = Agent(
    role="PM Validation Specialist",
    goal="Design lightweight experiments to test product hypotheses before committing to build",
    backstory=open("skills/pol-probe/SKILL.md").read(),
    verbose=True,
    llm=your_llm
)
```

#### Task definition
```python
from crewai import Task

write_stories_task = Task(
    description="Using your User Story framework, write user stories for: {epic_description}",
    agent=story_writer,
    expected_output="User stories in As a/I want/So that format with Gherkin acceptance criteria"
)
```

#### Full PM crew pattern
```python
from crewai import Crew

pm_crew = Crew(
    agents=[story_writer, validation_agent, prioritization_agent],
    tasks=[write_stories_task, validate_hypothesis_task, prioritize_backlog_task],
    verbose=True,
    process=Process.sequential  # or hierarchical with a PM Lead agent
)

result = pm_crew.kickoff(inputs={"epic_description": "seat management for enterprise admins"})
```

#### AGENTS.md
The repo root includes an `AGENTS.md` file that documents multi-agent orchestration patterns for this exact use case. Read it before configuring your crew — it maps which skills chain together and in what order for common PM workflows.

> **Pro tip:** Use `Process.hierarchical` with a "PM Lead" agent whose backstory is the `product-strategy-session` workflow skill. The Lead delegates to specialist agents (Story Writer, Validation, etc.) using their individual component and interactive skills. This mirrors how a real PM team operates.

---

### ◈ Gemini / Gemini CLI
*`GEMINI.md` for persistent context · `@file` for on-demand · `gemini` CLI for scripted invocation*

Detailed guide: [`Using PM Skills with Gemini.md`](Using%20PM%20Skills%20with%20Gemini.md)

**How Gemini handles skills:** Gemini (and the Gemini CLI) mirrors Claude's approach closely. `GEMINI.md` is the equivalent of `CLAUDE.md` — it loads persistent context at session start. The `gemini` CLI supports file context via flags. Google AI Studio supports file uploads for persistent knowledge.

#### Option 1 — `GEMINI.md` (persistent, session-wide)
1. Create a `GEMINI.md` file in your project root
2. Add skill references or paste skill content directly
3. The Gemini CLI reads it automatically at session start

#### `GEMINI.md` example
```markdown
# GEMINI.md

## Active PM Skills
You have access to the following PM frameworks. Apply the relevant one
based on the task without being asked.

### User Story Skill
[Paste contents of skills/user-story/SKILL.md]

### Prioritization Advisor Skill
[Paste contents of skills/prioritization-advisor/SKILL.md]

## Project Context
Product: [your product]
Team: [your team size and structure]
Current focus: [current sprint or initiative]
```

#### Option 2 — Gemini CLI with file flag
```bash
# Pass a skill file directly as context
gemini --context skills/user-story/SKILL.md \
       "Write user stories for our checkout abandonment epic"

# Pass multiple skill files
gemini --context skills/user-story/SKILL.md \
       --context skills/prioritization-advisor/SKILL.md \
       "Help me prioritize and then write stories for these 6 features"

# Pipe a skill file in
cat skills/pol-probe/SKILL.md | gemini "Apply this to my hypothesis: [hypothesis]"
```

#### Option 3 — Google AI Studio (web)
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. In **System Instructions**, paste the skill content
3. Skills stay active for the entire Studio session
4. For multi-skill sessions, paste all relevant skills into System Instructions at the start

#### Option 4 — Gemini in Google Workspace (Docs, Sheets, Gmail)
Skills can be referenced via the Gemini sidebar in Google Workspace apps:
1. Open Gemini sidebar in Google Docs or Sheets
2. Paste the skill content at the top of your prompt
3. Then describe the task: `"Using the skill above, write stories for this epic: [paste epic]"`
4. Best for PMs who live in Google Workspace and want skills without leaving their tools

> **Pro tip:** If you're already using Claude Code and want Gemini CLI parity, the `GEMINI.md` pattern is a near-direct port of your `CLAUDE.md` setup. Clone the skills repo once, point both CLIs at the same `skills/` directory, and maintain one source of truth.

---

## More Resources

- **Full docs:** `github.com/deanpeters/Product-Manager-Skills/docs/`
- **Platform-specific guide index:** `docs/Platform Guides for PMs.md`
- **Slash command guide (Claude Code):** `docs/Using PM Skills with Slash Commands 101.md`
- **Core platform guides:** `docs/Using PM Skills with Claude.md`, `docs/Using PM Skills with Codex.md`, `docs/Using PM Skills with ChatGPT.md`
- **Non-technical setup guide:** `docs/PM Skills Rule-of-Thumb Guide.md`
- **Build your own skill:** `./scripts/build-a-skill.sh` (guided wizard)
- **Streamlit playground:** `streamlit run app/main.py` (local test-drive, multi-provider)
