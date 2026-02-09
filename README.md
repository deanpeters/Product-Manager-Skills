# Product Manager Skills

```text
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ██████╗ ███╗   ███╗    ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
║   ██╔══██╗████╗ ████║    ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
║   ██████╔╝██╔████╔██║    ███████╗█████╔╝ ██║██║     ██║     ███████╗
║   ██╔═══╝ ██║╚██╔╝██║    ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
║   ██║     ██║ ╚═╝ ██║    ███████║██║  ██╗██║███████╗███████╗███████║
║   ╚═╝     ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝
║                                                                    ║
║   41 battle-tested frameworks for AI agents                        ║
║   Claude Code • Cowork • Codex • ChatGPT • Gemini                  ║
║                                                                    ║
║   v0.2 • Feb 8, 2026 • CC BY-NC-SA 4.0                             ║
╚════════════════════════════════════════════════════════════════════╝
```

**Train AI agents to do product management work like a pro.**

Frame problems, hunt opportunities, scaffold validation experiments, and kill bad bets fast. With battle-tested frameworks from Teresa Torres, Geoffrey Moore, Amazon, MITRE, and much more from product management's greatest hits.

---

## 📣 Updates & Announcements

### Feb 8, 2026 — LinkedIn Launch

**Post title:** Product Management Skills for Your Agents  
**Subtitle:** Because "just prompt better" is not a strategy.

Still rewriting PM prompts and getting generic AI output? I built a reusable PM Skills repo to help you make sharper decisions, docs, and outcomes faster.

- Full announcement draft: [`docs/announcements/2026-02-08-linkedin-launch.md`](docs/announcements/2026-02-08-linkedin-launch.md)
- Substack article draft: [`docs/announcements/2026-02-08-substack-savage-launch.md`](docs/announcements/2026-02-08-substack-savage-launch.md)
- Announcements index: [`docs/announcements/README.md`](docs/announcements/README.md)
- Skills repo: [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)
- Prior prompts repo: [Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts)

---

## 🎯 What This Is

**41 ready-to-use PM frameworks** that teach AI agents how to do product management work professionally—without you having to explain your process every time.

Instead of saying *"Write a PRD"* and hoping for the best, the agent already knows:
- ✅ How to structure a PRD
- ✅ What questions to ask stakeholders
- ✅ Which prioritization framework to use (and when)
- ✅ How to run customer discovery interviews
- ✅ How to break down epics using proven patterns

**Result:** You work faster, with better consistency, at a higher strategic level.

**Works with:** Claude Code, Cowork, OpenAI Codex, ChatGPT, Gemini, and any AI agent that can read structured knowledge.

---

## ✅ Safety and Evaluation

Before using any skill:
- Review the skill file and any linked resources. If it includes `scripts/`, read them before running.
- Prefer least privilege. Skills should not require secrets or network access unless explicitly documented.
- Do a quick dry run with a realistic prompt, then refine `name` and `description` for better discoverability.

---

## 🧰 Optional Scripts (Deterministic Helpers)

Some skills include a `scripts/` folder with deterministic helpers for calculations or formatting. These are optional, should be audited before running, and should avoid network calls or external dependencies.

**Examples:**
- `skills/tam-sam-som-calculator/scripts/market-sizing.py`
- `skills/user-story/scripts/user-story-template.py`

---

## 🤖 Skill Creation Utility

**Want to create your own skills?** Choose one of these utilities:

- `scripts/add-a-skill.sh` - Content-first, AI-assisted generation from notes/frameworks.
- `scripts/build-a-skill.sh` - Guided "build-a-bear" wizard that prompts section-by-section.
- `scripts/find-a-skill.sh` - Search skills by name/type/keyword with ranked results.
- `scripts/test-a-skill.sh` - Run strict conformance checks and optional smoke checks.

**What it does:**
1. Analyzes your content and suggests skill types
2. Generates complete skill files with examples
3. Validates metadata for marketplace compliance
4. Updates documentation automatically

**Usage:**
```bash
# From a file
./scripts/add-a-skill.sh research/your-framework.md

# Guided wizard
./scripts/build-a-skill.sh

# Find a skill
./scripts/find-a-skill.sh --keyword pricing --type interactive

# Test one skill
./scripts/test-a-skill.sh --skill finance-based-pricing-advisor --smoke

# From clipboard
pbpaste | ./scripts/add-a-skill.sh

# Check available adapters
./scripts/add-a-skill.sh --list-agents
```

**Agent support:** Claude Code, Manual mode (works with any CLI), and custom adapters via `scripts/adapters/ADAPTER_TEMPLATE.sh`

**Learn more:** See [`docs/Add-a-Skill Utility Guide.md`](docs/Add-a-Skill%20Utility%20Guide.md) for complete guide.

---

## ✅ Claude Web Upload Checklist

- Keep frontmatter `name` <= 64 chars and `description` <= 200 chars.
- Ensure the skill folder name matches the `name` value.
- Use `scripts/package-claude-skills.sh` to generate upload-ready `Skill.md` files.
- Validate metadata with `scripts/check-skill-metadata.py`.

---

## 🏗️ Three-Tier Architecture (How Skills Work Together)

These 41 skills are organized into **three types** that build on each other:

```text
┌───────────────────────────────────────────────────────────┐
│  WORKFLOW SKILLS (4)                                      │
│  Complete end-to-end PM processes                         │
│  Example: "Run a product strategy session"                │
│  Timeline: 2-4 weeks                                      │
└───────────────────────────────────────────────────────────┘
                         ↓ orchestrates
┌───────────────────────────────────────────────────────────┐
│  INTERACTIVE SKILLS (18)                                  │
│  Guided discovery with adaptive questions                 │
│  Example: "Which prioritization framework should I use?"  │
│  Timeline: 30-90 minutes                                  │
└───────────────────────────────────────────────────────────┘
                         ↓ uses
┌───────────────────────────────────────────────────────────┐
│  COMPONENT SKILLS (19)                                    │
│  Templates for specific PM deliverables                   │
│  Example: "Write a user story"                            │
│  Timeline: 10-30 minutes                                  │
└───────────────────────────────────────────────────────────┘
```

### Component Skills (19) — Templates & Artifacts
**What:** Reusable templates for creating specific PM deliverables (user stories, positioning statements, epics, personas, PRDs, etc.)

**When to use:** You need a standard template or format for a specific deliverable.

**Example:** "Write a user story with acceptance criteria" → Use [`user-story.md`](skills/user-story/SKILL.md)

---

### Interactive Skills (18) — Guided Discovery
**What:** Multi-turn conversational flows where AI asks you 3-5 adaptive questions, then offers smart recommendations based on your context.

**When to use:** You need help deciding which approach to take or gathering context before executing.

**Example:** "Which prioritization framework should I use?" → Run [`prioritization-advisor.md`](skills/prioritization-advisor/SKILL.md), which asks about your product stage, team size, data availability, then recommends RICE, ICE, Kano, or other frameworks.

**How they work:**
1. AI asks 3-5 questions about your context
2. You answer (or pick from numbered options)
3. AI offers 3-5 tailored recommendations
4. You choose one (or combine approaches)
5. AI executes using the right component skills

---

### Workflow Skills (4) — End-to-End Processes
**What:** Complete PM processes that orchestrate multiple component and interactive skills over days/weeks.

**When to use:** You need to run a full PM workflow from start to finish (strategy session, discovery cycle, roadmap planning, PRD creation).

**Example:** "Align stakeholders on product strategy" → Run [`product-strategy-session.md`](skills/product-strategy-session/SKILL.md), which guides you through positioning → problem framing → solution exploration → roadmap planning over 2-4 weeks.

---

## 📦 All 41 Skills (Clickable)

Now that you understand the three types, here's the complete catalog:

### 🧱 Component Skills (19)

| Skill | Use When You Need To... |
|-------|-------------------------|
| **[company-research](skills/company-research/SKILL.md)** | Deep-dive competitor or company analysis |
| **[customer-journey-map](skills/customer-journey-map/SKILL.md)** | Map customer experience across all touchpoints (NNGroup framework) |
| **[eol-message](skills/eol-message/SKILL.md)** | Communicate product/feature deprecation gracefully |
| **[epic-hypothesis](skills/epic-hypothesis/SKILL.md)** | Turn vague initiatives into testable hypotheses with success metrics |
| **[finance-metrics-quickref](skills/finance-metrics-quickref/SKILL.md)** | Fast lookup table for 32+ SaaS finance metrics with formulas, benchmarks, and when to use each |
| **[jobs-to-be-done](skills/jobs-to-be-done/SKILL.md)** | Understand what customers are trying to accomplish (JTBD framework) |
| **[pestel-analysis](skills/pestel-analysis/SKILL.md)** | Analyze external factors (Political, Economic, Social, Tech, Environmental, Legal) |
| **[pol-probe](skills/pol-probe/SKILL.md)** | Define lightweight, disposable validation experiments to test hypotheses before building (Dean Peters PoL framework) |
| **[positioning-statement](skills/positioning-statement/SKILL.md)** | Define who you serve, what problem you solve, and how you're different (Geoffrey Moore framework) |
| **[press-release](skills/press-release/SKILL.md)** | Write a future press release to clarify product vision (Amazon Working Backwards) |
| **[problem-statement](skills/problem-statement/SKILL.md)** | Frame a customer problem with evidence before jumping to solutions |
| **[proto-persona](skills/proto-persona/SKILL.md)** | Create hypothesis-driven personas before doing full research |
| **[recommendation-canvas](skills/recommendation-canvas/SKILL.md)** | Document AI-powered product recommendations |
| **[saas-economics-efficiency-metrics](skills/saas-economics-efficiency-metrics/SKILL.md)** | Evaluate unit economics and capital efficiency (CAC, LTV, payback, margins, burn rate, Rule of 40, magic number) |
| **[saas-revenue-growth-metrics](skills/saas-revenue-growth-metrics/SKILL.md)** | Calculate and interpret revenue, retention, and growth metrics (revenue, ARPU, MRR/ARR, churn, NRR, expansion) |
| **[storyboard](skills/storyboard/SKILL.md)** | Visualize user journeys with 6-frame narrative storyboards |
| **[user-story](skills/user-story/SKILL.md)** | Write user stories with proper acceptance criteria (Mike Cohn + Gherkin) |
| **[user-story-mapping](skills/user-story-mapping/SKILL.md)** | Organize stories by user workflow (Jeff Patton framework) |
| **[user-story-splitting](skills/user-story-splitting/SKILL.md)** | Break down large stories using 8 proven patterns |

---

### 🔄 Interactive Skills (18)

| Skill | What It Does |
|-------|--------------|
| **[acquisition-channel-advisor](skills/acquisition-channel-advisor/SKILL.md)** | Evaluate acquisition channels using unit economics, customer quality, and scalability. Recommends scale/test/kill decisions |
| **[agent-orchestration-advisor](skills/agent-orchestration-advisor/SKILL.md)** | Design multi-agent workflows—break complex tasks into parallel, specialized AI agents. Covers 4 dimensions of orchestration, agent boundary design, launch control tower monitoring, and evaluation frameworks |
| **[ai-shaped-readiness-advisor](skills/ai-shaped-readiness-advisor/SKILL.md)** | Assess if you're "AI-first" (automating tasks) or "AI-shaped" (redesigning how you work). Evaluates 5 competencies and recommends which to build first |
| **[business-health-diagnostic](skills/business-health-diagnostic/SKILL.md)** | Diagnose SaaS business health using key metrics, identify red flags, and prioritize actions. Analyzes growth, retention, efficiency, and capital health |
| **[context-engineering-advisor](skills/context-engineering-advisor/SKILL.md)** | Diagnose context stuffing (volume without intent) vs. context engineering (structure for attention). Guides memory architecture, retrieval strategies, and Research→Plan→Reset→Implement cycle |
| **[customer-journey-mapping-workshop](skills/customer-journey-mapping-workshop/SKILL.md)** | Guides journey mapping with pain point identification |
| **[discovery-interview-prep](skills/discovery-interview-prep/SKILL.md)** | Plans customer interviews (Mom Test style) based on your research goals |
| **[epic-breakdown-advisor](skills/epic-breakdown-advisor/SKILL.md)** | Splits epics into user stories using Richard Lawrence's 9 patterns |
| **[feature-investment-advisor](skills/feature-investment-advisor/SKILL.md)** | Evaluate feature investments using revenue impact, cost structure, ROI, and strategic value. Delivers build/don't build recommendations |
| **[finance-based-pricing-advisor](skills/finance-based-pricing-advisor/SKILL.md)** | Evaluate pricing changes using financial impact analysis (ARPU/ARPA, conversion, churn risk, NRR, payback) |
| **[lean-ux-canvas](skills/lean-ux-canvas/SKILL.md)** | Sets up hypothesis-driven planning (Jeff Gothelf Lean UX Canvas v2) |
| **[opportunity-solution-tree](skills/opportunity-solution-tree/SKILL.md)** | Generates opportunities and solutions, recommends best proof-of-concept to test |
| **[pol-probe-advisor](skills/pol-probe-advisor/SKILL.md)** | Recommends which of 5 prototype types to use based on your hypothesis and risk (Feasibility, Task-Focused, Narrative, Synthetic Data, Vibe-Coded) |
| **[positioning-workshop](skills/positioning-workshop/SKILL.md)** | Guides you through defining your positioning with adaptive questions |
| **[prioritization-advisor](skills/prioritization-advisor/SKILL.md)** | Recommends the right prioritization framework (RICE, ICE, Kano, etc.) for your situation |
| **[problem-framing-canvas](skills/problem-framing-canvas/SKILL.md)** | Leads you through MITRE Problem Framing (Look Inward/Outward/Reframe) |
| **[tam-sam-som-calculator](skills/tam-sam-som-calculator/SKILL.md)** | Projects market size (TAM/SAM/SOM) with real-world data and citations |
| **[user-story-mapping-workshop](skills/user-story-mapping-workshop/SKILL.md)** | Walks you through creating story maps with backbone and release slices |
| **[workshop-facilitation](skills/workshop-facilitation/SKILL.md)** | Adds one-step-at-a-time facilitation with numbered recommendations for workshop skills |

---

### 🎭 Workflow Skills (4)

| Skill | What It Does | Timeline |
|-------|--------------|----------|
| **[discovery-process](skills/discovery-process/SKILL.md)** | Complete discovery cycle: frame problem → research → synthesize → validate solutions | 3-4 weeks |
| **[prd-development](skills/prd-development/SKILL.md)** | Structured PRD: problem statement → personas → solution → metrics → user stories | 2-4 days |
| **[product-strategy-session](skills/product-strategy-session/SKILL.md)** | Full strategy: positioning → problem framing → solution exploration → roadmap | 2-4 weeks |
| **[roadmap-planning](skills/roadmap-planning/SKILL.md)** | Strategic roadmap: gather inputs → define epics → prioritize → sequence → communicate | 1-2 weeks |

---

## 🚀 How to Use

### With Claude Desktop or Claude.ai

1. Open a conversation with Claude
2. Share the skill file: "Read user-story.md"
3. Ask Claude to apply it: "Using the User Story skill, write stories for our checkout flow"

### With Claude Code (CLI)

```bash
cd product-manager-skills
claude "Using the PRD Development workflow, create a PRD for our mobile feature"
```

### With OpenAI Codex, Cowork, or Other Agents

**Codex:** Load skill files into your workspace, reference by name. See [Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md).
**Cowork:** Import skills as knowledge modules, invoke via natural language
**Other agents:** Follow your agent's docs for loading custom knowledge

### With ChatGPT, Gemini, or Any AI Chat

1. Open the skill file (e.g., `skills/user-story/SKILL.md`)
2. Copy the contents
3. Paste into ChatGPT/Gemini
4. Ask: "Using this framework, write user stories for my feature"

---

## 📄 Docs

- **[Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md)** — How to apply these skills in the Codex workspace.
- **[Building PM Skills](docs/Building%20PM%20Skills.md)** — How we distill sources into agent-ready PM skills.

---

## 💼 Real-World Use Cases

### "I need to align stakeholders on product strategy"
→ **Workflow:** [`product-strategy-session`](skills/product-strategy-session/SKILL.md) (2-4 weeks, orchestrates positioning → roadmap)

### "I need to validate a customer problem before building"
→ **Workflow:** [`discovery-process`](skills/discovery-process/SKILL.md) (3-4 weeks, interviews → synthesis → validation)

### "I need to test a hypothesis quickly before investing in development"
→ **Interactive:** [`pol-probe-advisor`](skills/pol-probe-advisor/SKILL.md) (recommends which prototype type: Feasibility, Task-Focused, Narrative, Synthetic Data, or Vibe-Coded)
→ **Component:** [`pol-probe`](skills/pol-probe/SKILL.md) (template for documenting validation experiments)

### "I want to know if I'm using AI strategically or just for efficiency"
→ **Interactive:** [`ai-shaped-readiness-advisor`](skills/ai-shaped-readiness-advisor/SKILL.md) (assesses 5 competencies: Context Design, Agent Orchestration, Outcome Acceleration, Team-AI Facilitation, Strategic Differentiation)

### "I'm pasting entire docs into AI and getting vague responses"
→ **Interactive:** [`context-engineering-advisor`](skills/context-engineering-advisor/SKILL.md) (diagnose context stuffing vs. engineering, define boundaries, implement Research→Plan→Reset→Implement cycle)

### "I need to write a PRD for a new feature"
→ **Workflow:** [`prd-development`](skills/prd-development/SKILL.md) (2-4 days, problem → solution → stories)

### "I need to create a Q2 roadmap"
→ **Workflow:** [`roadmap-planning`](skills/roadmap-planning/SKILL.md) (1-2 weeks, epics → prioritization → sequencing)

### "I need to choose a prioritization framework"
→ **Interactive:** [`prioritization-advisor`](skills/prioritization-advisor/SKILL.md) (asks questions, recommends RICE/ICE/Kano)

### "I need to split a large epic"
→ **Interactive:** [`epic-breakdown-advisor`](skills/epic-breakdown-advisor/SKILL.md) (Richard Lawrence's 9 patterns)

### "I need to write a user story"
→ **Component:** [`user-story`](skills/user-story/SKILL.md) (template + examples)

---

## 💡 Why Skills Beat Prompts

| Prompts | Skills |
|---------|--------|
| One-time instructions per task | Reusable frameworks learned once |
| "Write a PRD for X" | Agent knows PRD structure, asks smart questions, handles edge cases |
| You repeat yourself constantly | Agent remembers best practices |
| Inconsistent outputs | Consistent, professional results |

**Skills = Less explaining, more strategic work.**

---

## 🌟 What Makes These Skills Different

### ✅ Battle-Tested Frameworks
Built on proven methods from Geoffrey Moore, Jeff Patton, Teresa Torres, Amazon, Richard Lawrence, MITRE, and more.

### ✅ Real Client Work
Based on decades of PM consulting across healthcare, finance, manufacturing, and tech.

### ✅ Agent-Ready Format
Optimized for AI comprehension—not blog posts, not books, not courses. **Executable frameworks.**

### ✅ Zero Fluff
Every word earns its keep. No filler, no buzzwords, no generic advice.

### ✅ Example-Rich
Shows both "good" and "bad" examples so you know what works and what to avoid.

---

## 📚 Skill Structure (What's Inside Each File)

Every skill follows the same format:

```
## Purpose
What this skill does and when to use it.

## Key Concepts
Core frameworks, definitions, anti-patterns.

## Application
Step-by-step instructions (with examples).

## Examples
Real-world cases (good and bad).

## Common Pitfalls
What to avoid and why.

## References
Related skills and external frameworks.
```

**Clean. Practical. Zero fluff.**

---

## 🤝 Contributing

Found a gap? Have a PM framework you'd like to see included?

**Ways to contribute:**
- Open an issue with your suggestion
- Submit a pull request (we'll help you format it)
- Share feedback on what's working or missing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🎓 Philosophy

**Principles:**
- **Outcome-driven** over output-driven (solve problems, don't just ship features)
- **Evidence over vibes** (validate with data, not opinions)
- **Clarity beats completeness** (simple and usable beats comprehensive and confusing)
- **Examples beat explanations** (show, don't just tell)

**No hype. No buzzwords. Just frameworks that work.**

---

## 📖 Related Resources

- **[Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts)** — Task-specific prompts for ChatGPT, Claude, Gemini
- **[Productside](https://productside.com)** — AI-powered product management training and consulting
- **[Dean's LinkedIn](https://linkedin.com/in/deanpeters)** — Essays on AI-amplified product work

---

## 📜 License

CC BY-NC-SA 4.0 — non-commercial use with share-alike.

See [LICENSE](LICENSE) for full details.

---

## 📞 Questions?

- **GitHub Issues:** [Report bugs or suggest features](https://github.com/deanpeters/Product-Manager-Skills/issues)
- **LinkedIn:** [Connect with Dean Peters](https://linkedin.com/in/deanpeters)
- **Productside:** [Learn more about AI PM consulting](https://productside.com)

---

**v0.2 — February 8, 2026**

Highlights in this release:
- 41 total skills, including Phase 7 finance skills
- New skill tooling: `add-a-skill`, `build-a-skill`, `find-a-skill`, `test-a-skill`
- Stricter skill conformance validation and documentation updates

Built by Dean Peters (Principal Consultant and Trainer at Productside.com) with Anthropic Claude and OpenAI Codex.

*Helping product managers work smarter with AI.*
