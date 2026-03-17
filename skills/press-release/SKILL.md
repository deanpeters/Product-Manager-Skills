---
name: press-release
description: Write an Amazon-style press release that defines customer value before building. Use when aligning stakeholders on a new product, feature, or strategic bet.
intent: >-
  Create a visionary press release following Amazon's "Working Backwards" methodology to define and communicate a product or feature before building it. Use this to align stakeholders on the customer value proposition, clarify the problem being solved, and test if the product story resonates—treating the press release as a forcing function for clarity and customer-centricity.
type: component
---


## Purpose
Create a visionary press release following Amazon's "Working Backwards" methodology to define and communicate a product or feature before building it. Use this to align stakeholders on the customer value proposition, clarify the problem being solved, and test if the product story resonates—treating the press release as a forcing function for clarity and customer-centricity.

## Key Concepts

### Press Release Structure
A standard press release follows this format:

1. **Headline:** Clear, benefit-focused product announcement
2. **Dateline:** City, state, date
3. **Introduction paragraph:** What's being launched, who it's for, key benefit
4. **Problem paragraph:** Customer problem the product solves
5. **Solution paragraph:** How the product addresses the problem (outcomes, not features)
6. **Quote from company leader:** Vision, customer commitment
7. **Additional details:** Supporting benefits or data
8. **Boilerplate:** Company background
9. **Call to action:** How to learn more
10. **Media contact:** Press contact information

### Anti-Patterns (What This Is NOT)
- **Not feature-centric:** Don't list specs—focus on customer outcomes
- **Not internal jargon:** Write for customers, not engineers
- **Not vague:** "Revolutionizes productivity" is fluff; "Reduces report generation time from 8 hours to 10 minutes" is real
- **Not marketing spin:** Be honest about what the product does

---

## Application

Use `template.md` for the full fill-in structure.

### Step 1: Gather Context
Before drafting, ensure you have:
- **Product/feature description:** What are you building?
- **Target customer/persona:** Who is this for? (reference `skills/proto-persona/SKILL.md`)
- **Problem statement:** What customer problem does this solve? (reference `skills/problem-statement/SKILL.md`)
- **Key benefits:** What outcomes does it deliver?
- **Competitive context:** How is this different from alternatives? (reference `skills/positioning-statement/SKILL.md`)
- **Company mission/values:** How does this fit the company's vision?

**If missing context:** Run discovery, define the problem statement, or clarify positioning first.

---

### Step 2: Draft the Headline

Create a clear, benefit-focused headline:

```markdown
"[Product/Feature Name] by [Company] Aims to [Main Benefit/Goal]"
```

**Quality checks:**
- **Benefit-focused:** Does it say what the customer gets, not just what you built?
- **Specific:** "Aims to simplify workflows" is vague; "Aims to cut invoice processing time by 60%" is specific
- **Memorable:** Can someone repeat this headline in a conversation?

**Examples:**
- ✅ "Acme Workflows Launches Invoice Automation to Cut Processing Time by 60% for Small Businesses"
- ❌ "Acme Launches New Product with AI Features"

---

### Step 3: Write the Dateline and Introduction

```markdown
[City], [State], [Country], [Date] —

Today, [Company], a [type of organization], announced [key news], a [brief description]. This [product/feature] is set to [main benefit], addressing [key customer problem].
```

**Quality checks:**
- **Concise:** 2-3 sentences max
- **Customer problem mentioned:** Don't jump to solution—name the problem first

---

### Step 4: Explain the Problem

```markdown
[Product/feature] solves [specific customer problem]. According to [source or customer insight], [supporting data or quote that validates the problem].
```

**Quality checks:**
- **Specific problem:** Not "inefficiency" but "manual invoice processing takes 8 hours per month"
- **Validated:** Include data, customer quotes, or research to prove the problem is real

---

### Step 5: Describe the Solution (Outcome-Focused)

```markdown
[Product/feature] addresses this by [how it solves the problem—focus on outcomes]. [Quote from company leader]: "[Insert quote that emphasizes customer value, not features]."
```

**Quality checks:**
- **Outcome-first:** "Reduces processing time" not "includes OCR technology"
- **Quote is visionary:** Should reflect customer empathy and company values

---

### Step 6: Add Supporting Details

```markdown
In addition to [key benefit], [product/feature] also [additional benefits]. According to [statistic or source], [supporting data].
```

**Quality checks:**
- **Data-driven:** Use numbers where possible (time savings, cost reduction, etc.)
- **Customer-centric:** Still focused on "what they get," not "what we built"

---

### Step 7: Include Boilerplate

```markdown
[Company], founded in [year], is a [type of company] known for [main products/services]. With a focus on [company mission or values], [Company] has [achievements or milestones].
```

---

### Step 8: Add Call to Action and Media Contact

```markdown
For more information about [product/feature], visit [website] or contact [media contact name] at [contact info].

**Media Contact Information:**
[Name]
Title: [Title]
Phone: [Phone]
Email: [Email]
```

---

### Step 9: Test the Press Release

Ask these questions:
1. **Would a customer care?** If you sent this to a target customer, would they want to learn more?
2. **Is the problem clear?** Can someone who's never heard of your product understand the pain point?
3. **Are benefits measurable?** Can you prove the claims (time savings, cost reduction, etc.)?
4. **Is it jargon-free?** Could your mom understand it?
5. **Does it pass the "so what?" test?** If someone reads this and says "so what?" you haven't articulated value.

If any answer is "no," revise.

---

## Examples

See `examples/sample.md` for full press release examples.

Mini example excerpt:

```markdown
**Headline:** "Acme Launches SmartInvoice to Cut Processing Time by 60%"
**Problem:** Small businesses spend 8 hours/month on manual invoices
**Solution:** Automates extraction and approvals to save time
```

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Feature list instead of benefits | "Includes AI, ML, OCR, NLP, and real-time sync" | Translate to outcomes: "AI-powered automation reduces processing time by 60%" |
| Vague problem statement | "Solves inefficiency in workflows" | Be specific: "Small business owners spend 8 hours/month manually entering invoice data" |
| Jargon-heavy language | "Leverages cutting-edge ML models to optimize enterprise-grade workflows" | Write plainly: "Automatically handles invoices so you don't have to" |
| Generic executive quote | "We're excited to bring innovation to market" | Make it customer-focused: "Business owners shouldn't spend weekends processing invoices" |
| No data or validation | "Customers will love this revolutionary new solution" | Add data: "Beta users saved an average of 5 hours per month" |

---

## References

### Related Skills
- `skills/problem-statement/SKILL.md` — Defines the customer problem the press release highlights
- `skills/positioning-statement/SKILL.md` — Informs the differentiation and value proposition
- `skills/proto-persona/SKILL.md` — Defines the target customer mentioned in the press release
- `skills/jobs-to-be-done/SKILL.md` — Informs the customer benefits and outcomes

### External Frameworks
- Amazon's Working Backwards process — Origin of the press release-first methodology
- Ian McAllister's Quora answer on Amazon's press release template (2012) — Widely cited explanation
- Colin Bryar & Bill Carr, *Working Backwards* (2021) — Book on Amazon's product development process

### Dean's Work
- Visionary Press Release Prompt (inspired by Amazon's Working Backwards methodology)

### Provenance
- Adapted from `prompts/visionary-press-release.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

---

**Skill type:** Component
**Suggested filename:** `press-release.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** References `skills/problem-statement/SKILL.md`, `skills/positioning-statement/SKILL.md`, `skills/proto-persona/SKILL.md`, `skills/jobs-to-be-done/SKILL.md`
