# Contributing to Product Manager Skills

Thanks for your interest in contributing! This repository helps product managers work better with AI by providing battle-tested PM frameworks in an agent-ready format.

---

## 🎓 Design Philosophy — Read This First

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously: they equip AI agents to do PM work at a professional level, and they teach the human PM the *why* behind the framework so they can explain it, adapt it, and pass it on.

**ABC — Always Be Coaching** is a key governing principle.

Every skill should:
- Explain the *why*, not just the *what*
- Name failure modes so the reader recognizes them in the wild
- Show reasoning in examples, not just outputs
- Leave the user with better judgment, not just a filled-in template

**The most common contribution mistake:** trimming explanation to tighten copy. Brevity that strips learning scaffolding is a defect, not an improvement. If you're shortening a skill, check that you're cutting fluff — not cutting the lesson.

### Commercial Neutrality and Provider Boundaries

This is a shared library of durable product-management practice, not a channel for
promoting or integrating commercial products.

- Canonical skills must complete their promised job without a named vendor,
  account, API key, or paid service.
- Do not add provider-specific setup instructions, API calls, model identifiers,
  paid-request workflows, tracking links, referral links, or promotional calls to
  action.
- A named tool may appear only as a non-preferred example or comparison when it
  materially helps the reader make a decision. State any cost, data-sharing,
  account, or vendor-lock-in implications plainly.
- Provider-specific integrations belong in a separately approved integrations
  area or companion repository. They require an explicit maintainer request; do
  not introduce them speculatively through a contribution.

The test is simple: does this teach a reusable practice, or does it steer a reader
toward a product? If it is the latter, it does not belong in a canonical skill.

### Why We Don't Use `$ARGUMENTS`

Other skill libraries lean on Claude Code's `$ARGUMENTS` substitution to accept input. We deliberately don't — and it's a differentiator, not an omission:

1. **Portability.** Substitution only happens in Claude Code. In the Claude Desktop/Web packs, Codex, and the Streamlit playground, `$ARGUMENTS` renders as literal, unexplained template syntax — broken scaffolding in front of the reader.
2. **Pedagogy.** These skills teach human PMs as much as they instruct agents. A plain-language `## Input` section shows a PM what a well-formed request looks like — and, just as important, tells them they can arrive with nothing and be walked through it. `$ARGUMENTS` teaches them nothing.
3. **It's unnecessary.** Claude Code already appends typed arguments to the skill content when you invoke `/skill-name your context`. A skill that says "treat inline input as answers already given" gets the same behavior on every runtime, without the syntax.

Every skill declares its inputs in a required `## Input` section instead — that's the contract, on every runtime. Input sections are invitations, not gates: they must make clear that partial or zero input is fine and the guided flow (Guided / Context dump / Best guess entry modes) covers whatever's missing. PRs that "modernize" skills by introducing `$ARGUMENTS` or other runtime-specific template syntax will be asked to convert to the `## Input` convention — and `scripts/check-skill-metadata.py` fails any skill body containing bare `$ARGUMENTS`, so validation catches it before review does. (The `argument-hint` frontmatter field is the one sanctioned exception — it powers Claude Code autocomplete and is ignored everywhere else.)

---

## 🎯 Who Can Contribute?

**Anyone!** You don't need to be technical. If you:
- Have a PM framework that works consistently
- Spotted an error or gap in an existing skill
- Want to improve examples or clarity
- Have feedback on what's missing

...then you can contribute.

---

## 🤔 What Can You Contribute?

### 1. **New Skills**
Have a PM framework that should be included? Submit it!

**Examples of good candidates:**
- A template you use repeatedly (like OKR writing, stakeholder mapping, etc.)
- A process you follow consistently (like feature launches, go-to-market planning)
- A decision framework that helps you choose between options

**Not a good fit:**
- One-off advice or tips (these should be prompts, not skills)
- Company-specific processes (skills should be universally applicable)
- Overly complex frameworks (skills should be actionable, not academic)

---

### 2. **Improvements to Existing Skills**
Found something unclear? Missing examples? Outdated advice?

**Good improvements:**
- Add a "bad example" showing what NOT to do
- Clarify ambiguous instructions
- Add references to related skills
- Fix errors or typos
- Improve formatting for readability

**Please avoid:**
- Removing opinionated guidance (we take stances, not just list options)
- Adding fluff or unnecessary explanations (every word should earn its keep)
- Changing the standard structure (all skills follow the same format)

---

### 3. **Feedback & Suggestions**
Not ready to write? That's fine—share ideas:
- What PM tasks do you struggle with?
- Which existing skills are most/least useful?
- What frameworks do you wish existed?

**Open an issue** and we'll discuss.

---

## 📝 How to Contribute (Step-by-Step)

### For Non-Technical PMs (No GitHub Experience Required)

**Option 1: Email Your Suggestion**
1. Write up your idea in a doc (Google Docs, Word, etc.)
2. Email it to [Dean's email - add if you want]
3. We'll review and format it for you

**Option 2: Open a GitHub Issue**
1. Go to the [Issues tab](https://github.com/deanpeters/Product-Manager-Skills/issues)
2. Click "New Issue"
3. Describe your suggestion:
   - **For new skills:** What's the framework? When would a PM use it?
   - **For improvements:** Which skill? What section? What's unclear or wrong?
4. Submit—we'll follow up

---

### For Technical PMs (Comfortable with GitHub)

**Option 1: Fork & Pull Request**
1. **Fork this repository** (button in top-right)
2. **Clone your fork** to your computer:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Product-Manager-Skills.git
   cd Product-Manager-Skills
   ```
3. **Create a new branch:**
   ```bash
   git checkout -b add-skill-name
   ```
4. **Make your changes** (add a skill, improve existing content)
5. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add [skill-name] skill"
   ```
6. **Push to your fork:**
   ```bash
   git push origin add-skill-name
   ```
7. **Submit a pull request** on GitHub

**We'll review within a week and provide feedback.**

---

**Option 2: Use the Add-a-Skill Utility (Automated)**

For faster skill creation, use the `add-a-skill.sh` utility to automatically generate skills from raw PM content:

```bash
# From a file
./scripts/add-a-skill.sh research/your-framework.md

# From clipboard
pbpaste | ./scripts/add-a-skill.sh

# Check available adapters
./scripts/add-a-skill.sh --list-agents
```

**What it does:**
1. Analyzes your content and suggests skill types
2. Generates complete skill files with proper structure
3. Validates metadata for marketplace compliance
4. Updates documentation automatically
5. Stages files for git commit

**Supported adapters:** Claude Code, Manual mode (`--agent manual`), and custom adapters

**Learn more:** See [`docs/Add-a-Skill Utility Guide.md`](docs/Add-a-Skill%20Utility%20Guide.md)

**Want a guided wizard instead?**
```bash
./scripts/build-a-skill.sh
```

**Find and test before opening a PR:**
```bash
# Find related skills by keyword/type
./scripts/find-a-skill.sh --keyword discovery --type interactive

# Test your new/updated skill
./scripts/test-a-skill.sh --skill your-skill-name --smoke
```

---

## Using AI Agents (Optional)
If you use OpenAI Codex while drafting or validating skills, open this repo in your Codex workspace and reference the skill file path directly (e.g., `skills/user-story/SKILL.md`). For a quick walkthrough, see [Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md).

For guidance on how to manually distill frameworks and source material into new skills, see [Building PM Skills](docs/Building%20PM%20Skills.md).

---

## 🔒 Security, Safety, and Evaluation

- Review any source material and scripts for unsafe or destructive actions. Skills should not request secrets or run risky commands.
- If you add a script, place it in `skills/<skill-name>/scripts/`, keep it deterministic, avoid network calls, and document usage in the skill file.
- Before opening a pull request, confirm that the change does not introduce a commercial dependency, provider-specific integration, affiliate or referral path, tracking link, or paid external request. If a named tool is essential to a comparison, keep the skill usable without it and disclose its implications.
- Run a quick dry run using the skill questions or template and refine `name`, `description`, and steps until outputs are consistent and specific.

---

## 🧩 Skill Types: Which One to Create?

Before adding a new skill, determine which type it should be:

### **Component Skills** (Templates & Artifacts)
**Use when:** You need a reusable template for creating a specific PM deliverable.

**Examples:**
- User story template
- Positioning statement format
- Epic hypothesis structure
- PRD section (problem statement, success metrics)

**Structure:**
- Focused on "how to create X well"
- Includes template + quality criteria + examples + pitfalls

**Where to save:** `/skills/skill-name/SKILL.md` with `type: component` in frontmatter

---

### **Interactive Skills** (Guided Discovery)
**Use when:** You need adaptive questioning that gathers context and offers recommendations.

**Examples:**
- "Which prioritization framework should I use?" (asks about stage, data, constraints → recommends RICE/ICE/Kano)
- "Help me prep discovery interviews" (asks about research goals → generates interview guide)

**Structure:**
- Asks 3-5 adaptive questions
- Offers 3-5 numbered options based on context
- Allows user to pick by number or provide custom input
- Applies component skills at the end

**Where to save:** `/skills/skill-name/SKILL.md` with `type: interactive` in frontmatter

---

### **Workflow Skills** (End-to-End Processes)
**Use when:** You need a complete PM process that orchestrates multiple skills.

**Examples:**
- Product strategy session (positioning → problem framing → roadmap)
- Discovery process (frame problem → research → validate solutions)
- PRD development (problem statement → solution → user stories)

**Structure:**
- Multi-phase process (typically 4-8 phases)
- References component and interactive skills
- Includes decision points ("If X, then do Y")

**Where to save:** `/skills/skill-name/SKILL.md` with `type: workflow` in frontmatter

---

## 📐 Skill Format (Required Structure)

### Naming Conventions

Skill names must be **generic and universal** — they describe what the skill does, not who built it. No contributor handles, company names, or personal prefixes.

- ✅ `pm-skill-creator`
- ✅ `discovery-interview-prep`
- ❌ `acme-pm-skill-creator`
- ❌ `yourhandle-discovery-prep`

The skill belongs to the community once merged. The name should reflect that.

Every skill **must** follow this format:

~~~markdown
---
name: skill-name
description: Brief one-line description of what this skill does (≤ 200 chars for Claude web uploads)
type: component
---

## Purpose
One paragraph: What this skill does and when to use it.
(Make it outcome-focused: "build a roadmap that survives exec review," not "learn about roadmaps")

## Input
What the user can bring, in plain language — no template syntax (see "Why We Don't Use `$ARGUMENTS`" above). Frame it as an invitation, not a gate: nothing here is a prerequisite.
- **Works best with:** The subject the skill operates on (e.g., "the feature or problem you're writing a story for")
- **Also useful:** Context that sharpens the output (constraints, audience, prior research)
- **Inline input rule:** Tell the agent that anything supplied with the invocation (text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line) counts as answers already given — use it, don't re-ask
- **Arriving empty-handed?** Say what the skill does instead — open with the first guided question, offer entry modes, etc. The reader must finish this section knowing the skill will walk them through what they don't have
- Include 1–2 example invocations so humans learn what a well-formed request looks like

## Key Concepts
Core frameworks, definitions, mental models.
- Use bullets or tables
- Define PM jargon (don't assume everyone knows "JTBD" or "RICE")
- Include "Anti-Patterns" (what this is NOT)

## Application
Step-by-step guidance.
- Write as instructions anyone can follow
- Use numbered steps when sequence matters
- Call out decision points ("If X, do Y; if Z, do Q")
- **For component skills:** Focus on template + quality criteria
- **For interactive skills:** Map question sequence with numbered options
- **For workflow skills:** Show phases with decision branches

## Examples
Real-world cases showing the skill in action.
- Show both "good" and "bad" examples
- Make examples specific, not generic ("SaaS onboarding," not "product feature")
- **For interactive skills:** Show sample conversation flows

## Common Pitfalls
What to avoid and why.
- Name the failure mode ("Solution-First Thinking")
- Explain the consequence ("Build wrong thing, waste time")
- Provide the fix ("Frame problem first with customer evidence")

## References
- Related skills (link to component/interactive/workflow skills this uses or is used by)
- External frameworks (cite sources: Jeff Patton, Teresa Torres, etc.)
- Original authors/books
~~~

**Non-negotiable sections:**
- Purpose
- Input
- Key Concepts
- Application
- Examples
- Common Pitfalls
- References

**Optional sections:**
- Decision trees
- Templates
- Checklists

---

## 🔐 Provenance and Attribution

Skills earn trust by citing their sources. But an attribution can itself disclose something it
shouldn't, so there is one rule:

**Cite public, linkable work by name. For unpublished internal or client-delivered material, cite
the framework or the practice — not the artifact.**

**Cite freely, with a link:**
- Published repos, blog posts, Substack articles, podcast episodes, public talks and webinars
- Third-party frameworks and their authors — Moore, Cohn, Patton, Torres, Porter, Ansoff, HBR

**Never name:**
- Private training decks, client workshops, internal playbooks, or unpublished compendia
- Client names and pseudonyms alike — a placeholder like "XYZ Co" still signals a real engagement
- Local file paths on anyone's machine

Write `Distilled from practitioner experience running <the practice>` instead. It is true, useful,
and points at nothing.

**Two traps worth naming, because both have bitten this repo:**

1. **A named deliverable plus a date plus an author is findable**, even with the client scrubbed.
   "Company X's Q3 Strategy Workshop" identifies the engagement on its own.
2. **A denylist is a disclosure.** Never write "do not create examples about <specific topic>" into
   a committed file — that points a reader straight at the sensitive material. Keep exclusions in
   private notes and state the constraint positively: which domain to stay *inside*.

---

## ✅ Quality Checklist (Before Submitting)

Your skill should pass these checks:

- [ ] **Pedagogic:** Does it explain the *why*, not just the *what*? Would a PM finish this knowing more than when they started?
- [ ] **Agent-ready:** Could an AI read this and apply it without asking clarifying questions?
- [ ] **Self-contained:** Does it define its own terms? (No unexplained jargon)
- [ ] **Practical:** Does it include at least one concrete example?
- [ ] **Fully adorned:** Does the skill ship a `template.md` plus worked examples from two business domains (one SaaS, one industrial/non-SaaS)? *Why:* a skill demonstrated only in a SaaS market quietly narrows who it teaches — PMs in industrial, hardware, and regulated businesses deserve to see their own business on the page, and a second domain proves the framework generalizes. Reuse the repo's fictional universes (Fieldlight/Wrenchline for SaaS; Helix/Northfield/Corvid for industrial); suffix added files with the domain (`sample-industrial.md`). Quality bar, not hard gate: interactive skills may substitute per-domain conversation-flow examples, and definitionally single-domain skills are exempt.
- [ ] **Input-aware:** Does the Input section show an example invocation, tell the agent to use inline input instead of re-asking, and make clear the user can arrive with nothing and be guided through it? (Invitation, not gate — and no `$ARGUMENTS` syntax.)
- [ ] **Opinionated:** Does it take a stance? (Not just "here are options")
- [ ] **Skimmable:** Can you skim the headings and bullets and get 80% of the value?
- [ ] **Zero fluff:** Did you cut every word that doesn't earn its keep? (But not the lesson — see Design Philosophy above)
- [ ] **Properly categorized:** Is it clearly a component, interactive, or workflow skill?
- [ ] **If you removed existing content:** Can you confirm nothing pedagogic was lost? "Why This Works," Anti-Patterns, consequence explanations in Common Pitfalls, and educational preambles are load-bearing. "The agent already knows this" is not a valid reason to remove them — the human reader may not.

**For Interactive Skills Only:**
- [ ] **Bounded questions:** 3-5 questions max (not a 20-question survey)
- [ ] **Enumerated options:** 3-5 numbered choices per question
- [ ] **Context-aware:** Options adapt based on previous answers
- [ ] **Handles input gracefully:** User can pick numbers, combine options, or provide custom input
- [ ] **Uses the facilitation protocol:** Links [`workshop-facilitation`](skills/workshop-facilitation/SKILL.md) as its interaction protocol *and* carries the `**Default entry mode:**` line (copy both from any advisor, e.g. `prioritization-advisor`). *Why:* the line is how the library-wide setting in `pm-skills.config.yaml` reaches a skill installed on its own. `validate-skills.sh` fails without it. See [Guided Context Capture](docs/guided-context-capture.md)

---

## 🎨 Writing Style Guide

This section covers skill content. For reader-facing docs (README, install guides, the "Using PM Skills with…" guides), follow [Writing for Our Readers](docs/writing-for-our-readers.md): three readers, layered docs, and the first screen belongs to the least technical one.

### ✅ Do This:
- Write like you're teaching a smart, less experienced or emerging PM: explain the *why*, and never condescend
- Use short sentences and active voice
- Name tradeoffs (not just "best practices")
- Include vivid labels when helpful ("feature factory," "HiPPO decision-making")
- Make it copy/paste ready for AI agents
- Show real examples (anonymize if needed)

### ❌ Don't Do This:
- Use filler phrases ("Well, let's explore..." / "It's important to note...")
- Moralize or preach ("You MUST always..." / "It's critical that...")
- Hedge excessively ("This might potentially help in some cases...")
- Write academic essays (this isn't a journal article)
- Assume everyone has context (define terms, explain frameworks)
- Dump 10 questions at once (interactive skills ask 3-5 max)

**Tone:** Professional but conversational. Clear over clever.

---

## 🔄 Review Process

**A note on external scoring tools:**
Tools that score or grade skills can be useful for surfacing structural issues. If you use one, share the results — that's helpful context. Just note that most tools optimize for agent execution efficiency, which is only half this repo's mission. A score improvement that comes from removing pedagogic content will be sent back for revision.

**What happens after you submit:**

1. **We review within 7 days**
   - Check quality (does it pass the checklist?)
   - Check fit (does it align with repository goals?)
   - Check clarity (can AI and PMs both follow it?)

2. **We provide feedback**
   - If approved: Merge and publish
   - If changes needed: Suggest edits
   - If not a fit: Explain why (and suggest alternatives)

3. **You get credit**
   - Your name in the skill file
   - Mentioned in release notes
   - Added to contributors list

---

## 🙏 What We're Looking For

**High-priority contributions:**
- **Missing PM frameworks** (OKRs, go-to-market planning, feature launches, A/B testing)
- **Better examples** (especially "bad" examples showing common mistakes)
- **Clearer instructions** (where existing skills are confusing)

**Medium-priority:**
- Additional references to external frameworks
- Cross-references between related skills
- Alternative approaches (e.g., different prioritization frameworks)

**Low-priority:**
- Reformatting (skills already follow standard format)
- Style tweaks (unless clarity is significantly improved)

---

## 🚫 What We Won't Accept

**Out of scope:**
- Company-specific processes (skills should be universal)
- Generic advice ("communicate with stakeholders") without a specific framework
- Duplicate content (check existing skills first)
- Sales or marketing content (this is a PM skill library)
- Overly academic or theoretical frameworks (skills must be actionable)
- **Efficiency edits that strip pedagogic value** — trimming explanation, removing anti-patterns, or cutting examples to make a skill shorter is a defect. The teaching is the point. Specifically protected: "Why This Works" sections, Anti-Patterns, consequence chains in Common Pitfalls, and educational preambles that explain why a framework exists.
- **Content removal justified only by a score from an external tool** — external skill scoring tools may optimize for agent execution efficiency, which is only half this repo's mission. Score improvements are useful signal, but content removal requires explicit justification beyond a score change.

---

## 💬 Questions?

**Not sure if your idea fits?**
- Open an issue and describe it
- We'll let you know if it's a good candidate

**Need help formatting?**
- Submit a rough draft
- We'll help you polish it

**Want to brainstorm?**
- Reach out to Dean on [LinkedIn](https://linkedin.com/in/deanpeters)

---

## 📜 License Note

By contributing, you agree that your contributions will be licensed under the CC BY-NC-SA 4.0 license (same as this repository).

---

**Thank you for making Product Manager Skills better!** 🙏

Every contribution helps PMs around the world work smarter with AI.
