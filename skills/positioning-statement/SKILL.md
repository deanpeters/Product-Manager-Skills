---
name: positioning-statement
description: Create a Geoffrey Moore-style positioning statement. Use when clarifying who you serve, what problem you solve, your category, and why you're different from alternatives.
intent: >-
  Create a Geoffrey Moore-style positioning statement that clearly articulates who your product serves, what need it addresses, how it's categorized, what benefit it delivers, and how it differs from alternatives. Use this when you need to align stakeholders on product strategy, guide messaging, or test if your value proposition is crisp and defensible.
type: component
theme: strategy-positioning
best_for:
  - "Defining your product's market position clearly for the first time"
  - "Differentiating from specific competitors in your messaging"
  - "Aligning your team on who you serve, what problem you solve, and why you're different"
scenarios:
  - "I need to write a positioning statement for a new B2B SaaS product targeting mid-market HR teams"
  - "Our positioning feels generic and I need to sharpen it against two specific competitors"
estimated_time: "10-15 min"
---


## Purpose
Create a Geoffrey Moore-style positioning statement that clearly articulates who your product serves, what need it addresses, how it's categorized, what benefit it delivers, and how it differs from alternatives. Use this when you need to align stakeholders on product strategy, guide messaging, or test if your value proposition is crisp and defensible.

## Key Concepts

### The Geoffrey Moore Framework
From *Crossing the Chasm*, Moore's framework splits positioning into two parts:

**Value Proposition:**
- **For** [target customer]
- **that need** [underserved need]
- [product name]
- **is a** [product category]
- **that** [benefit statement]

**Differentiation Statement:**
- **Unlike** [primary competitor or competitive alternative]
- [product name]
- **provides** [unique differentiation]

### Anti-Patterns (What This Is NOT)
- **Not a tagline:** "Positioning" ≠ "Nike: Just Do It"
- **Not a feature list:** Don't say "that provides AI, automation, and integrations"
- **Not generic:** "For businesses that need efficiency" = positioning theater
- **Not aspirational fluff:** "That revolutionizes productivity" without specifics is noise

---

## Application

Use `template.md` for the full fill-in structure.

### Step 1: Gather Context
Before drafting, ensure you have:
- **Target customer segment:** Demographics, behaviors, role (not just "SMBs" or "developers")
- **Underserved need:** Pains, gains, jobs-to-be-done (reference `skills/jobs-to-be-done/SKILL.md` if needed)
- **Product category:** How buyers mentally file your solution (CRM, analytics platform, etc.)
- **Competitive landscape:** Direct competitors AND substitute behaviors (e.g., "Excel" is often the real competitor)

**If missing context:** Use discovery interviews, market research, or customer interviews to fill gaps. Don't guess.

---

### Step 2: Draft the Value Proposition

Fill in the template:

```markdown
## Value Proposition

**For** [specific target customer/persona]
- **that need** [statement of underserved need—focus on pains, gains, JTBD]
- [product or service name]
- **is a** [product category]
- **that** [benefit statement—focus on outcomes, not features]
```

**Quality checks:**
- **Target specificity:** Could you describe this person to a recruiter? If not, narrow it.
- **Need clarity:** Does this need resonate emotionally? Or is it generic ("need efficiency")?
- **Category fit:** Does this category help or hurt you? (Sometimes creating a new category is strategic, but risky.)
- **Outcome focus:** Are you saying what the user *gets*, not what the product *has*?

---

### Step 3: Draft the Differentiation Statement

Fill in the template:

```markdown
## Differentiation Statement

- **Unlike** [primary competitor or competitive alternative]
- [product or service name]
- **provides** [unique differentiation—outcomes, not features]
```

**Quality checks:**
- **Competitor honesty:** Is this the *real* alternative buyers consider? (Not just who you wish they compared you to.)
- **Differentiation substance:** Could a competitor copy this in 6 months? If yes, it's not durable differentiation.
- **Outcome framing:** Are you saying what users *achieve* differently, not just what you *do* differently?

---

### Step 4: Stress-Test the Positioning

Ask these questions:
1. **Would a customer recognize themselves?** Read the "For [target]" aloud. Does it feel specific or generic?
2. **Is the need defensible?** Can you point to research, interviews, or data that validates this need?
3. **Does the category help or hurt?** Does it anchor you against the right competitors? Or does it box you in?
4. **Is differentiation believable?** Could you prove this claim with a demo, case study, or data?
5. **Does this guide decisions?** If someone asked "Should we build feature X?" would this positioning help answer it?

If any answer is "no" or "sort of," revise.

---

### Step 5: Socialize and Iterate

- **Share with stakeholders:** Founders, execs, product, marketing, sales
- **Test with customers:** Read it aloud. Do they nod or look confused?
- **Refine ruthlessly:** Positioning is never done on the first draft. Cut words, sharpen specificity, test alternatives.

---

## Examples

See `examples/sample.md` for full positioning examples.

Mini example excerpt:

```markdown
**For** software development teams
- **that need** to reduce email overload and improve real-time collaboration
- Slack
- **is a** team messaging platform
- **that** centralizes communication and makes conversations searchable
```

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| "For everyone" | "For businesses that want to grow" or "For anyone who uses software" | Pick the *first* customer segment. Positioning works when it's narrow. |
| Feature creep in benefit | "That provides AI, automation, analytics, and integrations" | Lead with the outcome: "That reduces churn by 30% through predictive analytics" |
| Imaginary competitor | "Unlike outdated legacy systems" or "Unlike traditional approaches" | Name the *actual* competitor. If buyers use Excel, say "Unlike Excel." |
| Differentiation without proof | "Provides revolutionary AI" or "Delivers unmatched speed" | Make it falsifiable: "10x faster query performance than Snowflake on datasets under 1TB" |
| Category confusion | "Is a next-generation platform for digital transformation" | Pick a category buyers understand, or commit to category creation (requires $$$ and time) |

---

## References

### Related Skills
- `skills/problem-statement/SKILL.md` — Defines the problem positioning addresses
- `skills/jobs-to-be-done/SKILL.md` — Informs the "that need" statement
- `skills/proto-persona/SKILL.md` — Defines the "For [target]" segment
- `skills/press-release/SKILL.md` — Positioning informs press release messaging

### External Frameworks
- Geoffrey Moore, *Crossing the Chasm* (1991) — Origin of this framework
- April Dunford, *Obviously Awesome* (2019) — Modern positioning playbook
- Al Ries & Jack Trout, *Positioning: The Battle for Your Mind* (1981) — Foundational positioning theory

### Dean's Work
- [Link to relevant Dean Peters' Substack articles if applicable]

### Provenance
- Adapted from `prompts/positioning-statement.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

---

**Skill type:** Component
**Suggested filename:** `positioning-statement.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** References `skills/problem-statement/SKILL.md`, `skills/jobs-to-be-done/SKILL.md`, `skills/proto-persona/SKILL.md`
