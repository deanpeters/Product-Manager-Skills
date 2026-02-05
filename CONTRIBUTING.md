# Contributing to Product Manager Skills

Thanks for your interest in contributing! This repository helps product managers work better with AI by providing battle-tested PM frameworks in an agent-ready format.

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

**Where to save:** `/skills/components/`

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

**Where to save:** `/skills/interactive/`

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

**Where to save:** `/skills/workflows/`

---

## 📐 Skill Format (Required Structure)

Every skill **must** follow this format:

~~~markdown
# skill-name.md

## Purpose
One paragraph: What this skill does and when to use it.
(Make it outcome-focused: "build a roadmap that survives exec review," not "learn about roadmaps")

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

## ✅ Quality Checklist (Before Submitting)

Your skill should pass these checks:

- [ ] **Agent-ready:** Could an AI read this and apply it without asking clarifying questions?
- [ ] **Self-contained:** Does it define its own terms? (No unexplained jargon)
- [ ] **Practical:** Does it include at least one concrete example?
- [ ] **Opinionated:** Does it take a stance? (Not just "here are options")
- [ ] **Skimmable:** Can you skim the headings and bullets and get 80% of the value?
- [ ] **Zero fluff:** Did you cut every word that doesn't earn its keep?
- [ ] **Properly categorized:** Is it clearly a component, interactive, or workflow skill?

**For Interactive Skills Only:**
- [ ] **Bounded questions:** 3-5 questions max (not a 20-question survey)
- [ ] **Enumerated options:** 3-5 numbered choices per question
- [ ] **Context-aware:** Options adapt based on previous answers
- [ ] **Handles input gracefully:** User can pick numbers, combine options, or provide custom input

---

## 🎨 Writing Style Guide

### ✅ Do This:
- Write like you're teaching a smart colleague (not a junior intern)
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

By contributing, you agree that your contributions will be licensed under the MIT License (same as this repository).

---

**Thank you for making Product Manager Skills better!** 🙏

Every contribution helps PMs around the world work smarter with AI.
