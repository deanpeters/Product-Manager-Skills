---
name: agent-orchestration-advisor
description: Design multi-agent AI workflows with clear boundaries, handoffs, and monitoring. Use when a complex PM task should run as parallel specialized agents instead of one linear process.
compatibility: opencode
argument-hint: "[workflow or task to orchestrate]"
metadata:
  best_for:
    - "Breaking a complex PM workflow into parallel, specialized AI agents"
    - "Designing agent boundaries, handoffs, and human review points"
    - "Setting up launch control tower monitoring for agentic workflows"
  estimated_time: "15-25 min"
  intent: >-
    Guide product managers through designing multi-agent workflows — breaking complex, repetitive tasks into parallel, specialized AI agents rather than linear, sequential processes. Covers the 4 dimensions
    of orchestration, agent boundary design, launch control tower monitoring, and evaluation frameworks.
  scenarios:
    - "I spend hours on competitive research every week — help me design agents to run it in parallel"
    - "Our AI workflow is one giant sequential prompt chain — help me re-architect it as an orchestrated system"
  theme: ai-agents
  type: interactive
---

## Purpose

Guide product managers through designing **multi-agent workflows**—breaking complex, repetitive PM tasks into parallel, specialized AI agents rather than linear, sequential processes or manual execution. Use this to transition from "document-heavy administrator" to "systems-level orchestrator" who coordinates a "living system" of AI agents, human teams, and market data interacting continuously.

**Key Shift:** From linear project management (one task at a time) to orchestration (multiple agents working simultaneously, each with clear boundaries and handoffs).

This is not about prompt writing—it's about **architecting workflows where AI agents handle repetitive research, synthesis, and validation while PMs focus on strategy and decision-making**.

## Input

**Works best with:** The workflow or recurring task you want to orchestrate — described in a sentence or two, however manual or messy it is today.
**Also useful:** Where it breaks down now (too slow, too sequential, too dependent on you), the tools your team already uses, and whether you've worked through [context-engineering-advisor](../context-engineering-advisor/SKILL.md) first (it's the prerequisite discipline).

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The advisor opens by asking which PM workflow eats the most of your week, then walks the four orchestration dimensions against it.

**Example invocation:** `Design an orchestration for our weekly competitive intel: today one PM spends 6 hours scraping, summarizing, and briefing — sequentially.`

## Key Concepts

### Orchestration vs. Project Management

| Dimension | Project Management | Orchestration |
|-----------|-------------------|---------------|
| **Approach** | Linear oversight of schedules and human tasks | Managing "living system" where AI agents, humans, and data interact continuously |
| **Task Flow** | Sequential (finish A, then B, then C) | Parallel (A, B, C run simultaneously) |
| **PM Role** | Document-heavy administrator | Systems-level leader coordinating automated systems + human judgment |
| **Focus** | Output (features shipped) | Outcome (business results, learning velocity) |
| **Risk Management** | Manual tracking and mitigation | Real-time monitoring with agentic systems flagging gaps |

**Critical Insight:** Orchestration is not about replacing humans—it's about **force-multiplying human judgment** by automating repetitive, time-consuming tasks.

---

### The Four Dimensions of Orchestration

#### 1. **Coordination of Multi-Agent Workflows**
Breaking complex tasks into specialized agents that run in parallel.

**Example:**
- **Manual (Old):** PM spends 8 hours compiling competitive intel, then 4 hours synthesizing customer feedback, then 3 hours identifying roadmap gaps = 15 hours sequentially
- **Orchestrated (New):** Three agents run simultaneously:
  - Agent A: Competitive intel (research agent)
  - Agent B: Customer synthesis (synthesis agent)
  - Agent C: Roadmap gap analysis (analysis agent)
  - Total time: 8 hours (limited by slowest agent), PM reviews outputs in 2 hours = 10 hours total, 5 hours saved

**Key Principle:** Shift from manual selection to **hypothesis orchestration**—agents generate hypotheses, PM validates and decides.

#### 2. **Leadership of Cross-Functional AI Pods**
Governing diverse teams (data scientists, ML engineers, compliance, ethicists) to ensure solutions are scalable, ethical, and aligned.

**What it includes:**
- Embedding diversity-aware workflows
- Risk management (not afterthought)
- Ethical orchestration (ensuring AI doesn't "go rogue")
- Cross-functional alignment (engineering, compliance, design)

**PM Role:** Guardian of Governance—ensures AI systems reflect company values.

#### 3. **Launch Control Tower Function**
Real-time monitoring of organizational readiness across functions using agentic systems to flag gaps before critical failures.

**What it monitors:**
- Support readiness (docs, training, escalation paths)
- Marketing readiness (messaging, assets, GTM plan)
- Operations readiness (infrastructure, scaling, monitoring)

**Key Principle:** Agentic systems act as early warning system—flag gaps before they become blockers.

#### 4. **Strategic Intent Alignment (Context Engineering Applied)**
Feeding AI agents the correct mix of mission, constraints, and priorities to ensure automated decisions reflect company values.

**Connection:** This is **context engineering at the orchestration layer**. See `context-engineering-advisor` for foundations.

**What agents need:**
- Product constraints (what we will/won't build)
- Strategic priorities (what matters most right now)
- Operational definitions (shared glossary)
- Evidence standards (what counts as validation)

---

### The Four AI Management Workflows (Productside Blueprint)

Every PM must master these workflows to move fast while staying grounded:

1. **Context Engineering** ✅ (Foundation)
   - Create AI workspace that remembers product domain, research, JTBD, personas, constraints
   - **Skill:** `context-engineering-advisor`

2. **Synthetic Evals** 📋 (Quality Assurance)
   - Automated validation tests for AI reasoning
   - Generate synthetic data, run workflows against traces
   - Eliminates 80% of hallucination risk

3. **Agentic Workflows** ← **We're here**
   - Agents handle repetitive tasks (competitive intel, customer synthesis, roadmap gaps)
   - PM focuses on strategy

4. **Vibe Coding** 📋 (Rapid Prototyping)
   - Generate clickable prototypes from context workspace
   - Collapse feedback loops from weeks to hours
   - **Connection:** `pol-probe-advisor` (Vibe-Coded PoL Probes)

---

### AI-Shaped Problems (Teresa Torres)

**What makes a problem "AI-shaped"?**
- Previously difficult to scale due to human involvement (e.g., synthesizing 50 user interviews)
- Falls short with current non-AI solutions (e.g., manual competitive tracking)
- Requires consistency at scale (e.g., risk analysis across 100 features)

**Key Insight:** "While AI makes building easier, choosing *what* to build remains the primary challenge." Orchestration helps with the "building" part so PMs can focus on "choosing."

---

### The Four Big Risks (Marty Cagan, AI Era)

The orchestrator manages these risks across the organization:

| Risk | Standard Definition | AI Era Layer | Orchestrator's Role |
|------|---------------------|--------------|---------------------|
| **Value Risk** | Will customers pay? | Does AI provide enough incremental benefit vs. cost? | Validate value with PoL probes before orchestrating |
| **Usability Risk** | Can users figure it out? | Is the UX right? (Chat often isn't!) | Test workflows with real users |
| **Feasibility Risk** | Can we build it? | Do we understand "physics of AI"? Token budget? | Design within technical constraints |
| **Viability Risk** | Can we sell/support? | Legal limits? Data privacy? Sustainable OpEx? | Monitor costs, compliance, scalability |

---

### Anti-Patterns (What This Is NOT)

- **Not about replacing PMs:** Orchestration amplifies judgment, doesn't eliminate it
- **Not about automating everything:** Some tasks require human empathy and context
- **Not about complexity for its own sake:** Only orchestrate when it saves significant time or improves quality
- **Not about "set it and forget it":** Orchestrated workflows require monitoring and maintenance

---

### When to Use This Skill

✅ **Use this when:**
- You have repetitive PM tasks that take 5+ hours per week (competitive analysis, customer synthesis, roadmap maintenance)
- You're doing sequential work that could be parallelized (research, then synthesis, then analysis)
- You need consistency at scale (analyze 50 features for risk, synthesize 100 customer interviews)
- You're spending time on execution instead of strategy

❌ **Don't use this when:**
- The task is one-time or infrequent (not worth orchestration overhead)
- Human judgment is critical at every step (empathy-driven work)
- The task is already fast enough (don't over-engineer)
- You haven't built context engineering foundations first (see `context-engineering-advisor`)

---

## Application

This interactive skill uses **adaptive questioning** to design multi-agent workflows step-by-step.

---

### Step 0: Gather Context

**Agent asks:**

Before we design your orchestrated workflow, let's gather context:

**Current PM Work:**
- What repetitive tasks take the most time each week? (competitive analysis, customer synthesis, roadmap updates, etc.)
- How much time do you spend on these tasks? (hours per week)
- Are these tasks sequential (one after another) or could they run in parallel?

**Desired Outcome:**
- What would "good enough" automation look like? (80% reduction in manual work? Higher consistency?)
- What parts require human judgment? (final decisions, empathy, ethical considerations)

**Technical Context:**
- Do you have context engineering foundations? (constraints registry, operational glossary—see `context-engineering-advisor`)
- What AI tools do you currently use? (Claude Projects, ChatGPT, custom agents)

**You can describe briefly or paste examples.**

---

### Step 1: Assess if Task is AI-Shaped

**Agent asks:**

Let's determine if your task is suited for orchestration. **Which statement best describes your situation?**

**Select one:**

1. **"I spend 10+ hours per week on repetitive research/synthesis tasks"**
   - Examples: Compiling competitive intelligence, synthesizing customer feedback, tracking feature requests
   - Assessment: High potential for orchestration

2. **"I have a task that requires multiple sequential steps, and each step is time-consuming"**
   - Examples: Research competitors → Synthesize findings → Identify gaps → Update roadmap (15 hours total, done sequentially)
   - Assessment: Good candidate for parallelization

3. **"I need consistency at scale—analyzing many similar items"**
   - Examples: Risk analysis for 50 features, synthesizing 100 user interviews, tracking 20 competitors
   - Assessment: Perfect for orchestration (agents ensure consistency)

4. **"I have a task that's mostly human judgment and empathy"**
   - Examples: Stakeholder negotiation, team coaching, ethical trade-offs
   - Assessment: Not a good candidate for orchestration (keep human-driven)

**User response:** [Selection]

**Agent analyzes:**

Based on your selection:
- **Options 1-3:** Proceed to workflow design
- **Option 4:** Recommend keeping task human-driven; suggest alternative approaches (e.g., use AI for research, but keep decision-making human)

---

### Step 2: Decompose Task into Agent-Specific Subtasks

**Agent asks:**

Let's break your task into **discrete subtasks**, each handled by a specialized agent.

**For the task you selected, what are the distinct steps?**

**Example Decomposition (Competitive Intelligence):**

**Manual Process (Old):**
1. Research 10 competitors' product pages (3 hours)
2. Track recent feature launches (2 hours)
3. Analyze pricing changes (2 hours)
4. Synthesize into competitive landscape doc (3 hours)
5. Identify strategic gaps (2 hours)
**Total:** 12 hours, done sequentially

**Orchestrated Process (New):**
- **Agent A (Research):** Scrape competitors' product pages, extract features
- **Agent B (Launch Tracker):** Monitor competitors' release notes, blog posts, social media
- **Agent C (Pricing Analyzer):** Track pricing pages, identify changes
- **Agent D (Synthesis):** Compile findings from A, B, C into structured report
- **Agent E (Gap Analysis):** Compare our roadmap vs. competitor features, flag gaps
**Total:** Agents A-C run in parallel (3 hours), then D and E run sequentially (2 hours) = 5 hours + 1 hour PM review = 6 hours total (50% time saved)

**Agent offers:**

I'll help you decompose your task. **Describe your current process step-by-step**, and I'll identify:
- Which steps can be agent-handled
- Which steps can run in parallel
- Which steps require human judgment

**User response:** [Describe process]

**Agent provides:** Decomposed workflow with agent assignments.

---

### Step 3: Design Parallel vs. Sequential Flows

**Agent asks:**

Now let's design the **workflow topology**—which agents run in parallel vs. sequentially.

**Three Flow Patterns:**

**Pattern 1: Full Parallel (Fastest)**
```
[Agent A] ─┐
[Agent B] ─┼─→ [PM Review] → [Decision]
[Agent C] ─┘
```
- All agents run simultaneously
- PM reviews all outputs together
- **Use when:** Agents are independent (no dependencies between them)

**Pattern 2: Pipeline (Sequential with Handoffs)**
```
[Agent A] → [Agent B] → [Agent C] → [PM Review] → [Decision]
```
- Each agent depends on previous agent's output
- **Use when:** Later agents need earlier agents' results

**Pattern 3: Hybrid (Parallel + Sequential)**
```
[Agent A] ─┐
[Agent B] ─┼─→ [Agent D] → [Agent E] → [PM Review] → [Decision]
[Agent C] ─┘
```
- Some agents run in parallel, feed into sequential agents
- **Use when:** Early steps are independent, later steps synthesize

**For your task, which pattern fits best?**

**Options:**
1. **Full Parallel** — All agents are independent
2. **Pipeline** — Each agent needs the previous one's output
3. **Hybrid** — Mix of parallel and sequential
4. **Not sure** — [Agent analyzes your decomposition and recommends]

**User response:** [Selection]

**Agent provides:** Visual workflow diagram with agent dependencies.

---

### Step 4: Define Agent Boundaries and Handoffs

**Agent asks:**

Now let's define **what each agent knows** (context boundaries) and **how agents hand off to each other**.

**For each agent, define:**

1. **Agent Name & Purpose** (What's its job?)
2. **Context Needed** (What information does it need?)
   - Always-available (from context engineering)
   - Retrieved on-demand (specific to this run)
3. **Output Format** (What does it produce?)
4. **Handoff to Next Agent** (What gets passed? What gets filtered?)

**Example (Competitive Intelligence Orchestration):**

**Agent A: Competitor Research Agent**
- **Purpose:** Scrape 10 competitors' product pages, extract features
- **Context Needed:**
  - Always-available: List of competitors (from constraints registry)
  - Retrieved: Competitor URLs (from database)
- **Output Format:** Structured JSON: `{competitor, features[], last_updated}`
- **Handoff:** Passes JSON to Agent D (Synthesis Agent)

**Agent D: Synthesis Agent**
- **Purpose:** Compile findings from Agents A, B, C into structured report
- **Context Needed:**
  - Always-available: Report template, writing tone (from context workspace)
  - Retrieved: Outputs from Agents A, B, C
- **Output Format:** Markdown document with sections: Overview, Key Features, Pricing, Launch Activity
- **Handoff:** Passes report to Agent E (Gap Analysis Agent)

**Agent offers:**

I'll help you define boundaries for each agent. **For your workflow, let's define:**
- What context each agent needs (always-available vs. retrieved)
- What format each agent produces (JSON, Markdown, structured data)
- How agents hand off (what's passed vs. filtered)

**User response:** [Describe agent needs]

**Agent provides:** Complete agent boundary definitions + handoff specifications.

---

### Step 5: Implement Strategic Intent Alignment

**Agent asks:**

To prevent agents from "going rogue," we need to feed them the correct mix of **mission, constraints, and priorities**.

**Strategic Intent Checklist (Per Agent):**

1. **Mission:** What is this agent's primary goal?
   - Example: "Identify competitive threats that could impact Q2 roadmap"

2. **Constraints:** What must the agent NOT do?
   - Example: "Do not recommend features outside our strategic focus areas"
   - Example: "Do not scrape data from sites that prohibit it (check robots.txt)"

3. **Priorities:** If the agent must choose, what matters most?
   - Example: "Prioritize features launched in last 30 days over older features"

4. **Evidence Standards:** What counts as valid information?
   - Example: "Only cite information from official product pages, release notes, or verified blog posts"

**Connection:** This is **context engineering applied to orchestration**. See `context-engineering-advisor` for deeper guidance.

**Agent offers:**

For each agent in your workflow, let's define:
- Mission (what's the goal?)
- Constraints (what's out of bounds?)
- Priorities (what matters most?)
- Evidence standards (what counts as valid?)

**User response:** [Define strategic intent per agent]

**Agent provides:** Strategic intent document for each agent.

---

### Step 6: Set Up Launch Control Tower Monitoring

**Agent asks:**

The **Launch Control Tower** provides real-time monitoring to flag gaps before they become critical failures.

**What to Monitor (Three Dimensions):**

**1. Agent Performance:**
- Are agents completing tasks on time?
- Are outputs meeting quality standards?
- Are agents staying within token/cost budgets?

**2. Organizational Readiness (If Launching a Feature):**
- Support readiness: Docs updated? Training complete? Escalation paths defined?
- Marketing readiness: Messaging finalized? Assets created? GTM plan locked?
- Operations readiness: Infrastructure scaled? Monitoring in place? Rollback plan ready?

**3. Risk Flags:**
- Are agents producing unexpected outputs? (potential hallucination)
- Are agents violating constraints? (ethical/compliance issues)
- Are handoffs failing? (Agent B not receiving Agent A's output correctly)

**Monitoring Approach:**

**Option 1: Manual Dashboard**
- Weekly PM review of agent outputs
- Spot-check quality, compare to golden datasets
- Manual risk flag identification

**Option 2: Automated Monitoring**
- Agents log outputs to central dashboard
- Automated evals run on each output (see Step 7)
- Alerts triggered when quality drops below threshold

**Option 3: Hybrid**
- Automated evals + weekly PM review
- Alerts for critical issues, PM spot-checks others

**Which monitoring approach fits your team's maturity?**

**Options:**
1. **Manual Dashboard** (Lower maturity, smaller scale)
2. **Automated Monitoring** (Higher maturity, larger scale)
3. **Hybrid** (Recommended for most teams)

**User response:** [Selection]

**Agent provides:** Monitoring plan with specific metrics and alert thresholds.

---

### Step 7: Create Evaluation Plan

**Agent asks:**

To ensure orchestrated workflows produce high-quality outputs, we need an **evaluation framework**.

**The Four Eval Types (From Research):**

| Eval Type | Method | When to Use |
|-----------|--------|-------------|
| **Golden Datasets** | 20-100 examples of real inputs + expected outputs | Baseline quality measurement |
| **Code Assertions** | Rules output must follow (e.g., must contain valid JSON) | Structural validation |
| **LLM-as-Judge** | Powerful model (GPT-4o) grades agent output | Rapid automated feedback |
| **Human Evals** | PM manually reviews traces | Ultimate check for "taste" and "product sense" |

**Evaluation Process:**

1. **Collect Traces:** Log inputs and outputs for each agent run
2. **Review Weekly:** Annotate traces to categorize failure modes
3. **Build Failure Mode Taxonomy:** Common errors (hallucination, constraint violation, low quality)
4. **Create Automated Evals:** Target common failure modes with Golden Datasets or Code Assertions
5. **Iterate:** Refine agent prompts/context based on eval results

**For your workflow, which evals make sense?**

**Options:**
1. **Start with Golden Datasets** — Create 20 examples of good outputs for each agent
2. **Start with Code Assertions** — Define structural rules (e.g., output must be valid JSON with required fields)
3. **Start with Human Evals** — PM reviews every output for first 2 weeks, identifies patterns
4. **All three** — Comprehensive eval strategy (recommended for critical workflows)

**User response:** [Selection]

**Agent provides:** Evaluation plan with specific eval types, frequencies, and success criteria.

---

### Step 8: Implementation Plan & Next Steps

**Agent synthesizes:**

Here's your complete orchestrated workflow plan:

```
┌─────────────────────────────────────────────────────────────┐
│ ORCHESTRATED WORKFLOW: [Your Task Name]                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ TOPOLOGY: [Full Parallel / Pipeline / Hybrid]              │
│                                                             │
│ AGENTS:                                                     │
│ • Agent A: [Name] - [Purpose]                              │
│ • Agent B: [Name] - [Purpose]                              │
│ • Agent C: [Name] - [Purpose]                              │
│                                                             │
│ FLOW:                                                       │
│ [Agent A] ─┐                                                │
│ [Agent B] ─┼─→ [Agent D] → [PM Review] → [Decision]        │
│ [Agent C] ─┘                                                │
│                                                             │
│ CONTEXT BOUNDARIES:                                         │
│ • Always-available: [List]                                  │
│ • Retrieved on-demand: [List]                               │
│                                                             │
│ STRATEGIC INTENT:                                           │
│ • Mission: [Per agent]                                      │
│ • Constraints: [Per agent]                                  │
│ • Priorities: [Per agent]                                   │
│                                                             │
│ MONITORING:                                                 │
│ • Approach: [Manual / Automated / Hybrid]                   │
│ • Metrics: [List]                                           │
│ • Alert thresholds: [List]                                  │
│                                                             │
│ EVALUATION:                                                 │
│ • Golden Datasets: [Y/N]                                    │
│ • Code Assertions: [Y/N]                                    │
│ • Human Evals: [Frequency]                                  │
│                                                             │
│ TIME SAVINGS:                                               │
│ • Manual (old): [X hours]                                   │
│ • Orchestrated (new): [Y hours]                             │
│ • Savings: [X-Y hours per week]                             │
└─────────────────────────────────────────────────────────────┘
```

**Implementation Roadmap:**

**Week 1: Build Context Foundations**
- If not already done, complete `context-engineering-advisor`
- Create constraints registry, operational glossary
- Document strategic intent for each agent

**Week 2: Implement First Agent**
- Start with simplest agent (usually research or data collection)
- Test with 5 real examples
- Validate output quality

**Week 3: Add Remaining Agents**
- Implement agents 2-5 (depending on your workflow)
- Test handoffs between agents
- Validate full workflow end-to-end

**Week 4: Set Up Monitoring & Evals**
- Implement chosen monitoring approach
- Create Golden Datasets (if selected)
- Run first week of human evals, identify failure modes

**Week 5+: Iterate & Scale**
- Refine agent prompts based on eval results
- Add automated evals targeting common failures
- Scale to more use cases

**Success Criteria:**
- ✅ Time savings: 30%+ reduction in manual work
- ✅ Quality: Agent outputs meet quality bar 80%+ of time
- ✅ Consistency: Outputs follow template/format 95%+ of time
- ✅ Monitoring: Alerts catch issues before PM notices
- ✅ Evaluation: Failure mode taxonomy documented, automated evals in place

**Agent offers:**

Would you like me to:
1. **Export this workflow plan** as a Markdown document?
2. **Provide implementation templates** (agent prompt templates, monitoring dashboard, eval checklists)?
3. **Recommend tools** for building this orchestration (Claude Projects, custom APIs, orchestration platforms)?

---

## Examples

### Example 1: Competitive Intelligence Orchestration

**Context:**
- PM at B2B SaaS company
- Tracks 10 competitors
- Manual process: 12 hours per week (research, synthesis, gap analysis)

**Goal:** Reduce to 6 hours with orchestrated workflow

**Workflow Design:**

**Agents:**
- **Agent A (Research):** Scrapes competitors' product pages, extracts features
- **Agent B (Launch Tracker):** Monitors release notes, blogs, social media for new launches
- **Agent C (Pricing Analyzer):** Tracks pricing pages, identifies changes
- **Agent D (Synthesis):** Compiles findings from A, B, C into structured report
- **Agent E (Gap Analysis):** Compares our roadmap vs. competitors, flags strategic gaps

**Topology:** Hybrid (A, B, C in parallel → D → E → PM Review)

**Strategic Intent:**
- Mission (Agent E): "Identify competitive threats that could impact Q2 roadmap"
- Constraint (Agent E): "Do not recommend features outside our strategic focus areas (enterprise security, AI-powered analytics)"
- Priority (Agent B): "Prioritize features launched in last 30 days"

**Monitoring:**
- Hybrid approach: Automated evals + weekly PM review
- Metrics: Agent completion time, output quality score (LLM-as-Judge)
- Alert: If Agent E flags >5 critical gaps (potential strategic threat)

**Evaluation:**
- Golden Datasets: 20 examples of well-synthesized competitive reports
- Code Assertions: Output must be valid JSON with required fields (competitor, features[], pricing[], launch_date)
- Human Evals: PM reviews one full workflow run per week

**Result:**
- Time: 12 hours → 6 hours (50% savings)
- Quality: Consistent format, no missed competitors
- Strategic value: Gap analysis flags threats 2 weeks earlier than manual process

---

### Example 2: Customer Feedback Synthesis

**Context:**
- PM at consumer app
- Receives 200+ pieces of feedback per week (app reviews, support tickets, NPS comments)
- Manual process: 8 hours per week (reading, tagging, synthesizing themes)

**Goal:** Reduce to 2 hours with orchestrated workflow

**Workflow Design:**

**Agents:**
- **Agent A (Ingestion):** Collects feedback from App Store, Google Play, Zendesk, NPS surveys
- **Agent B (Tagging):** Tags feedback by category (bug, feature request, usability, performance)
- **Agent C (Sentiment):** Classifies sentiment (positive, neutral, negative, critical)
- **Agent D (Theme Extraction):** Identifies recurring themes across feedback
- **Agent E (Prioritization):** Scores themes by frequency + sentiment intensity
- **Agent F (Synthesis):** Generates weekly synthesis report with top 5 themes + example quotes

**Topology:** Pipeline (A → B → C → D → E → F → PM Review)

**Strategic Intent:**
- Mission (Agent D): "Identify unmet customer needs that could become roadmap opportunities"
- Constraint (Agent E): "Do not deprioritize critical bugs, even if infrequent"
- Priority (Agent F): "Focus on themes affecting 10+ users in last 7 days"

**Monitoring:**
- Automated: Dashboard shows agent completion status, error rate
- Alerts: If Agent C flags >10 "critical" sentiment items (escalate to PM immediately)

**Evaluation:**
- Golden Datasets: 50 examples of well-tagged, well-synthesized feedback
- LLM-as-Judge: Weekly eval of Agent D's theme extraction quality
- Human Evals: PM spot-checks 10% of tagged feedback

**Result:**
- Time: 8 hours → 2 hours (75% savings)
- Quality: Themes now backed by quantitative data (frequency, sentiment)
- Strategic value: Identified 3 high-impact themes that became Q2 roadmap features

---

### Example 3: Risk Analysis at Scale

**Context:**
- PM at enterprise platform
- Needs to analyze 50 features for risk (security, compliance, performance, usability)
- Manual process: 15 hours (30 minutes per feature)

**Goal:** Reduce to 5 hours with orchestrated workflow

**Workflow Design:**

**Agents:**
- **Agent A (Security Risk):** Analyzes feature for security vulnerabilities (data exposure, auth issues)
- **Agent B (Compliance Risk):** Checks feature against regulatory requirements (GDPR, HIPAA, SOC2)
- **Agent C (Performance Risk):** Estimates load impact, identifies scaling concerns
- **Agent D (Usability Risk):** Flags complex workflows, accessibility issues
- **Agent E (Synthesis):** Compiles risk scores, generates risk matrix

**Topology:** Full Parallel (A, B, C, D run simultaneously → E → PM Review)

**Strategic Intent:**
- Mission (All agents): "Flag risks that could delay launch or harm customers"
- Constraint (Agent B): "Must cite specific regulatory requirements (not vague warnings)"
- Priority (Agent E): "Prioritize risks by impact × likelihood (standard risk matrix)"

**Monitoring:**
- Automated: Dashboard shows risk distribution (low/medium/high/critical)
- Alerts: If any feature scores "critical" risk (escalate to PM + leadership)

**Evaluation:**
- Golden Datasets: 30 examples of well-analyzed features with known risks
- Code Assertions: Risk scores must be {low, medium, high, critical}—no other values
- Human Evals: Security team reviews Agent A outputs monthly

**Result:**
- Time: 15 hours → 5 hours (67% savings)
- Quality: Consistent risk scoring across all 50 features
- Strategic value: Identified 3 critical risks that would have been missed in manual review

---

## Common Pitfalls

### 1. **Orchestrating Before Context Engineering**
**Failure Mode:** Building agent workflows without context foundations (constraints, glossary, evidence standards).

**Consequence:** Agents produce inconsistent outputs, violate constraints, hallucinate.

**Fix:** Complete `context-engineering-advisor` first. Build constraints registry, operational glossary, strategic intent documents.

---

### 2. **Over-Orchestrating Simple Tasks**
**Failure Mode:** Creating complex multi-agent workflows for tasks that take <2 hours per week.

**Consequence:** Orchestration overhead (setup, monitoring, maintenance) exceeds time saved.

**Fix:** Only orchestrate tasks that take 5+ hours per week or require consistency at scale.

---

### 3. **No Evaluation Plan**
**Failure Mode:** "Set it and forget it"—agents run without quality checks.

**Consequence:** Quality drift over time, unnoticed hallucinations, constraint violations.

**Fix:** Implement Golden Datasets + weekly Human Evals at minimum. Build failure mode taxonomy, create automated evals.

---

### 4. **Ignoring Handoff Failures**
**Failure Mode:** Assuming agents will correctly pass data to each other without testing.

**Consequence:** Agent B receives malformed data from Agent A, produces garbage output.

**Fix:** Test handoffs explicitly. Validate data format at each handoff. Use Code Assertions to enforce structure.

---

### 5. **Forgetting the "PM Review" Step**
**Failure Mode:** Treating orchestrated workflows as fully autonomous—no human oversight.

**Consequence:** Agents make decisions that lack context, empathy, or strategic alignment.

**Fix:** Always include PM Review step. Agents generate hypotheses/recommendations; PM validates and decides.

---

## References

### Related Skills
- **[context-engineering-advisor](../context-engineering-advisor/SKILL.md)** (Interactive) — **Prerequisite:** Build context foundations before orchestration
- **[ai-shaped-readiness-advisor](../ai-shaped-readiness-advisor/SKILL.md)** (Interactive) — Assesses Agent Orchestration maturity (Competency #2)
- **[pol-probe-advisor](../pol-probe-advisor/SKILL.md)** (Interactive) — Vibe Coding connection (rapid prototyping)
- **[discovery-process](../discovery-process/SKILL.md)** (Workflow) — Use orchestrated agents in discovery phase

### External Frameworks
- **Dean Peters** — *The Product Manager as an Orchestrator* (Productside research)
- **Dean Peters** — *Productside Blueprint* (Four AI Management Workflows: Context Engineering, Synthetic Evals, Agentic Workflows, Vibe Coding)
- **Teresa Torres** — *Continuous Discovery Habits* (5 AI PM disciplines: Context Engineering, Orchestration, Observability, Evals, Maintenance)
- **Marty Cagan** — *Empowered* (4 big risks: Value, Usability, Feasibility, Viability)

### Tools & Platforms
- **Claude Projects** — Simple orchestration with multiple agents in one project
- **LangChain** — Framework for building agent chains
- **LangGraph** — State machine orchestration for complex workflows
- **n8n / Zapier** — No-code workflow automation (simpler orchestrations)
