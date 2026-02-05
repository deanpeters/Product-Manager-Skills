# Product Manager Skills

~~~text
╔══════════════════════════════════════════════════════════════════════╗
║  PRODUCT MANAGER SKILLS  v0.1                                       ║
║  battle-tested PM frameworks for Claude and AI agents               ║
╚══════════════════════════════════════════════════════════════════════╝
~~~

**29 ready-to-use skills** covering everything from writing user stories to running full product strategy sessions.

---

## 🎯 What This Is

A library of **PM skills** that teach AI agents (like Claude) how to do product management work professionally—writing PRDs, running discovery interviews, planning roadmaps, prioritizing backlogs, and more.

Think of it as **training materials for your AI PM partner**. Instead of explaining your process every time, the agent already knows:
- How to structure a PRD
- Which prioritization framework to use (and when)
- How to run customer discovery interviews
- How to break down epics into user stories
- What makes a good positioning statement

**Result:** You work faster, with better consistency, and at a higher strategic level.

---

## 🚫 What This Is NOT

- ❌ A prompt library (see [Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts) for that)
- ❌ A training course for humans
- ❌ Generic "best practices" blog posts

This is **executable PM knowledge** designed for AI agents to read and apply.

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

## 📦 What's Inside (29 Skills)

### 🧱 Component Skills (15)
**Building blocks** — Templates for creating specific PM deliverables.

| Skill | Use When You Need To... |
|-------|-------------------------|
| **positioning-statement** | Define who you serve, what problem you solve, and how you're different (Geoffrey Moore framework) |
| **problem-statement** | Frame a customer problem with evidence before jumping to solutions |
| **user-story** | Write user stories with proper acceptance criteria (Mike Cohn + Gherkin) |
| **jobs-to-be-done** | Understand what customers are trying to accomplish (JTBD framework) |
| **proto-persona** | Create hypothesis-driven personas before doing full research |
| **epic-hypothesis** | Turn vague initiatives into testable hypotheses with success metrics |
| **press-release** | Write a future press release to clarify product vision (Amazon Working Backwards) |
| **user-story-splitting** | Break down large stories using 8 proven patterns |
| **user-story-mapping** | Organize stories by user workflow (Jeff Patton framework) |
| **recommendation-canvas** | Document AI-powered product recommendations |
| **storyboard** | Visualize user journeys with 6-frame narrative storyboards |
| **eol-message** | Communicate product/feature deprecation gracefully |
| **customer-journey-map** | Map customer experience across all touchpoints (NNGroup framework) |
| **pestel-analysis** | Analyze external factors (Political, Economic, Social, Tech, Environmental, Legal) |
| **company-research** | Deep-dive competitor or company analysis |

---

### 🔄 Interactive Skills (10)
**Guided discovery** — AI asks you questions, then offers smart recommendations based on your context.

| Skill | What It Does |
|-------|--------------|
| **positioning-workshop** | Guides you through defining your positioning with adaptive questions |
| **discovery-interview-prep** | Plans customer interviews (Mom Test style) based on your research goals |
| **prioritization-advisor** | Recommends the right prioritization framework (RICE, ICE, Kano, etc.) for your situation |
| **tam-sam-som-calculator** | Projects market size (TAM/SAM/SOM) with real-world data and citations |
| **epic-breakdown-advisor** | Splits epics into user stories using Richard Lawrence's 9 patterns |
| **opportunity-solution-tree** | Generates opportunities and solutions, recommends best proof-of-concept to test |
| **user-story-mapping-workshop** | Walks you through creating story maps with backbone and release slices |
| **customer-journey-mapping-workshop** | Guides journey mapping with pain point identification |
| **problem-framing-canvas** | Leads you through MITRE Problem Framing (Look Inward/Outward/Reframe) |
| **lean-ux-canvas** | Sets up hypothesis-driven planning (Jeff Gothelf Lean UX Canvas v2) |

**How interactive skills work:**
1. AI asks 3-5 questions about your context
2. You answer (or pick from numbered options)
3. AI offers 3-5 tailored recommendations
4. You choose one (or combine approaches)
5. AI executes with the right component skills

**Example:**
~~~
You: "Run the Prioritization Advisor"

AI: "What stage is your product in?
1. Pre-PMF (experimenting rapidly)
2. Early PMF (scaling fast)
3. Mature product (optimizing)
4. Multiple products/platform"

You: "2"

AI: "Based on early PMF stage, I recommend RICE prioritization..."
~~~

---

### 🎭 Workflow Skills (4)
**End-to-end processes** — Complete PM workflows that orchestrate multiple skills.

| Skill | What It Does | Timeline |
|-------|--------------|----------|
| **product-strategy-session** | Full strategy: positioning → problem framing → solution exploration → roadmap | 2-4 weeks |
| **discovery-process** | Complete discovery cycle: frame problem → research → synthesize → validate solutions | 3-4 weeks |
| **roadmap-planning** | Strategic roadmap: gather inputs → define epics → prioritize → sequence → communicate | 1-2 weeks |
| **prd-development** | Structured PRD: problem statement → personas → solution → metrics → user stories | 2-4 days |

**Workflow skills orchestrate everything:**
- `product-strategy-session` references 15+ component and interactive skills
- `discovery-process` walks through interviews, synthesis, experiments
- `roadmap-planning` handles OKRs, prioritization, stakeholder alignment
- `prd-development` produces a complete, professional PRD

---

## 🚀 How to Use (For Product Managers)

### Option 1: Use with Claude Desktop or Claude.ai

1. **Open a conversation** with Claude
2. **Share the skill file** you need (e.g., "Read user-story.md")
3. **Ask Claude to apply it:**
   - "Using the User Story skill, write stories for our checkout flow"
   - "Run the Prioritization Advisor for our Q2 backlog"
   - "Follow the Discovery Process workflow to validate this problem"

**That's it.** Claude reads the skill and applies the framework.

---

### Option 2: Use with Claude Code (CLI)

If you're using Claude Code command-line tool:

1. **Navigate to this repo:**
   ```bash
   cd product-manager-skills
   ```

2. **Reference skills in your prompts:**
   ```bash
   claude "Using the PRD Development workflow, create a PRD for our new mobile feature"
   ```

3. **For interactive skills:**
   ```bash
   claude "Run the Epic Breakdown Advisor to split our onboarding epic"
   ```

Claude Code will read the skill files automatically from the `/skills/` directory.

---

### Option 3: Copy-Paste into Any AI Chat

1. **Open the skill file** (e.g., `skills/components/user-story.md`)
2. **Copy the contents**
3. **Paste into ChatGPT, Gemini, or any AI chat**
4. **Ask the AI to apply it:**
   - "Using this framework, write user stories for our new feature"

Works with any AI that accepts long context.

---

## 📚 Skill Structure (What's Inside Each File)

Every skill follows the same format:

~~~
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
~~~

**Clean. Practical. Zero fluff.**

Each skill is:
- ✅ **Self-contained** (no external dependencies)
- ✅ **Actionable** (step-by-step guidance)
- ✅ **Example-rich** (shows good and bad cases)
- ✅ **Pitfall-aware** (warns about common mistakes)

---

## 🏗️ Three-Tier Architecture

Skills build on each other:

~~~
┌─────────────────────────────────────────┐
│   Workflow Skills (4)                   │
│   End-to-end processes                  │
│   Example: "product-strategy-session"   │
└─────────────────────────────────────────┘
              ↓ orchestrates
┌─────────────────────────────────────────┐
│   Interactive Skills (10)               │
│   Guided discovery with questions       │
│   Example: "positioning-workshop"       │
└─────────────────────────────────────────┘
              ↓ uses
┌─────────────────────────────────────────┐
│   Component Skills (15)                 │
│   Templates and artifacts               │
│   Example: "user-story"                 │
└─────────────────────────────────────────┘
~~~

**How they work together:**

**Example 1: Writing User Stories**
1. Use `user-story-splitting` (component) to break down a large epic
2. Use `user-story` (component) to write each story with acceptance criteria

**Example 2: Running Product Strategy**
1. Use `product-strategy-session` (workflow) which:
   - Calls `positioning-workshop` (interactive) to define positioning
   - Calls `problem-framing-canvas` (interactive) to frame the problem
   - Calls `opportunity-solution-tree` (interactive) to explore solutions
   - Calls `roadmap-planning` (workflow) to sequence initiatives
   - Uses 15+ component skills throughout

---

## 💼 Real-World Use Cases

### "I need to align stakeholders on product strategy"
→ **Workflow:** `product-strategy-session` (2-4 weeks, orchestrates positioning → roadmap)

### "I need to validate a customer problem before building"
→ **Workflow:** `discovery-process` (3-4 weeks, interviews → synthesis → validation)

### "I need to write a PRD for a new feature"
→ **Workflow:** `prd-development` (2-4 days, problem → solution → stories)

### "I need to create a Q2 roadmap"
→ **Workflow:** `roadmap-planning` (1-2 weeks, epics → prioritization → sequencing)

### "I need to choose a prioritization framework"
→ **Interactive:** `prioritization-advisor` (asks questions, recommends RICE/ICE/Kano)

### "I need to split a large epic"
→ **Interactive:** `epic-breakdown-advisor` (Richard Lawrence's 9 patterns)

### "I need to write a user story"
→ **Component:** `user-story` (template + examples)

---

## 🌟 What Makes These Skills Different

### ✅ Battle-Tested Frameworks
Built on proven methods from:
- Geoffrey Moore (Crossing the Chasm)
- Jeff Patton (User Story Mapping)
- Teresa Torres (Continuous Discovery)
- Amazon (Working Backwards)
- Richard Lawrence (Story Splitting)
- MITRE (Problem Framing)
- And more...

### ✅ Real Client Work
Based on decades of PM consulting across healthcare, finance, manufacturing, and tech.

### ✅ Agent-Ready Format
Optimized for AI comprehension—not blog posts, not books, not courses. These are **executable frameworks**.

### ✅ Zero Fluff
Every word earns its keep. No filler, no buzzwords, no generic advice.

### ✅ Example-Rich
Shows both "good" and "bad" examples so you know what works and what to avoid.

---

## 🤝 Contributing

Found a gap? Have a PM framework you'd like to see included?

**Ways to contribute:**
- **Open an issue** with your suggestion
- **Submit a pull request** with a new skill (we'll help you format it)
- **Share feedback** on what's working or what's missing

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

MIT License — use it, remix it, make it better.

See [LICENSE](LICENSE) for full details.

---

## 📞 Questions?

- **GitHub Issues:** [Report bugs or suggest features](https://github.com/deanpeters/Product-Manager-Skills/issues)
- **LinkedIn:** [Connect with Dean Peters](https://linkedin.com/in/deanpeters)
- **Productside:** [Learn more about AI PM consulting](https://productside.com)

---

**v0.1 — February 2026**

Built by Dean Peters (Productside) with Claude (Anthropic).

*Helping product managers work smarter with AI.*
