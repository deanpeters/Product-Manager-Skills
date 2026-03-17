---
name: eol-message
description: Write a clear, empathetic EOL announcement with rationale, customer impact, and next steps. Use when retiring a product, feature, or plan without creating avoidable confusion.
intent: >-
  Craft a clear, empathetic End-of-Life (EOL) message that communicates product or feature discontinuation, explains the rationale, addresses customer impact, provides transition support, and positions the replacement solution. Use this to maintain customer trust during difficult transitions and reduce churn by demonstrating care and offering a clear path forward.
type: component
---


## Purpose
Craft a clear, empathetic End-of-Life (EOL) message that communicates product or feature discontinuation, explains the rationale, addresses customer impact, provides transition support, and positions the replacement solution. Use this to maintain customer trust during difficult transitions and reduce churn by demonstrating care and offering a clear path forward.

## Key Concepts

### The EOL Messaging Framework
An effective EOL message balances honesty about the change with empathy for customer impact. It includes:

1. **Company context:** Who you are and your commitment to customers
2. **The announcement:** What's being discontinued and what's replacing it
3. **The rationale:** Why this decision benefits customers (not just the business)
4. **Current product context:** What the product was and who it served
5. **Customer impact:** How this affects users (acknowledge the disruption)
6. **Transition solution:** What the replacement is and how it improves on the old
7. **Support measures:** How you'll help customers migrate
8. **Timeline:** Key dates and milestones
9. **Call to action:** Next steps and contact info

---

## Application

Use `template.md` for the full fill-in structure.

### Step 1: Gather Context
Before drafting, ensure you have:
- **Product being discontinued:** What specifically is ending?
- **Replacement solution:** What's replacing it (if anything)?
- **Timeline:** Key dates (announcement, feature freeze, shutdown, data export deadline)
- **Customer impact:** How many users affected? What workflows disrupted?
- **Support plan:** Migration support, training, discounts, data export tools
- **Rationale:** Why is this happening? (Technology obsolescence, strategic shift, consolidation, etc.)

**If missing context:** Don't send the message until you have a complete transition plan. Customers will ask "What do I do now?"—you must have an answer.

---

### Step 2: Draft the Product Transition Narrative

#### Company Context
Establish who you are and your commitment:

```markdown
### Product Transition Narrative

**We are:** [Describe the company and its relationship to the product being phased out]
- [Key point about company's commitment to customers]
- [Key point about company's product evolution]
- [Key point about company's future vision]
```

**Example:**
```markdown
**We are:** Acme Workflows, a workflow automation platform serving 50,000 small businesses
- We're committed to helping you save time and focus on what matters
- We continuously evolve our product based on your feedback and technological advances
- We're building toward a future where automation is accessible, powerful, and simple
```

---

#### The Announcement
Be clear and direct:

```markdown
**Announcing:**
- [Single sentence that clearly states the EOL of the product and introduces its replacement]
```

**Example:**
- "We are discontinuing Acme Workflows Classic on December 31, 2026, and migrating all customers to Acme Workflows Pro."

---

#### The Rationale (Customer-Benefit-Focused)
Explain *why* this benefits customers:

```markdown
**Because:**
- [Reason 1: e.g., technological advancements]
- [Reason 2: e.g., improved performance]
- [Reason 3: e.g., better alignment with customer needs]

**Which means for you:**
- [Describe the impact and benefits from the customer's perspective]
```

**Example:**
```markdown
**Because:**
- Acme Workflows Classic runs on outdated infrastructure that limits performance and scalability
- Acme Workflows Pro is built on modern technology that enables faster automation, better integrations, and real-time collaboration
- Consolidating to one platform allows us to invest 100% of our engineering resources in features you've requested

**Which means for you:**
- Faster automation execution (3x speed improvement)
- 50+ new integrations with tools you already use
- Access to new features like real-time collaboration and mobile app
```

---

### Step 3: Provide Current Product Context

Acknowledge what's being lost:

```markdown
### Current Product Context

**Our product** [name of the product being discontinued]
- **is a** [brief description of the product and its primary function]
- **that has served** [target customer/user] for [duration or timeframe]
- **by providing** [key benefits or solutions the product offered]
```

**Example:**
```markdown
**Our product** Acme Workflows Classic
- **is a** workflow automation tool that helps small businesses eliminate repetitive tasks
- **that has served** over 20,000 customers for 8 years
- **by providing** reliable, straightforward automation without requiring technical expertise
```

---

### Step 4: Acknowledge Customer Impact

Be honest about disruption:

```markdown
### Customer Impact

**We understand that this may affect you by:**
- [Potential impact 1 on customer operations or processes]
- [Potential impact 2 on customer operations or processes]
- [Potential impact 3 on customer operations or processes (if applicable)]
```

**Example:**
```markdown
**We understand that this may affect you by:**
- Requiring time to migrate workflows from Classic to Pro
- Learning new features and interface changes
- Updating integrations or API connections if you've customized workflows
```

---

### Step 5: Present the Transition Solution

Use positioning statement format (reference `skills/positioning-statement/SKILL.md`):

```markdown
### Transition Solution

**For** [target customer/user affected by the EOL]
- **that currently use** [name of the product being phased out]
- [name of the replacement product]
- **is a** [definition of the replacement product category]
- **that** [statement of benefit to the user, focusing on continuity and improvements]

### Differentiation and Continuity

- **Like** [product being phased out],
- [name of the replacement product]
- **provides** [how the replacement maintains key benefits of the old product]
- **while also offering** [new benefits or improvements]
```

**Example:**
```markdown
### Transition Solution

**For** small business owners
- **that currently use** Acme Workflows Classic
- Acme Workflows Pro
- **is a** next-generation workflow automation platform
- **that** maintains all the simplicity and reliability you love while adding 3x faster performance, 50+ new integrations, and real-time collaboration

### Differentiation and Continuity

- **Like** Acme Workflows Classic,
- Acme Workflows Pro
- **provides** easy-to-build automations without coding, reliable execution, and straightforward pricing
- **while also offering** 3x faster workflows, mobile app access, real-time team collaboration, and integrations with tools like Slack, Asana, and Notion
```

---

### Step 6: Outline Support Measures and Timeline

#### Support Measures

```markdown
### Support and Next Steps

**To ensure a smooth transition, we will:**
- [Support measure 1, e.g., "Provide 1-on-1 migration assistance for all customers"]
- [Support measure 2, e.g., "Automatically migrate your workflows (with your approval)"]
- [Support measure 3, e.g., "Offer a 3-month discount on Acme Workflows Pro for existing customers"]
```

---

#### Timeline

```markdown
### Timeline

- [Key date 1 and associated milestone, e.g., "March 1, 2026: Migration tool available"]
- [Key date 2 and associated milestone, e.g., "September 1, 2026: Acme Workflows Classic becomes read-only"]
- [Key date 3 and associated milestone, e.g., "December 31, 2026: Acme Workflows Classic fully discontinued, data export deadline"]
```

**Quality checks:**
- **Sufficient lead time:** Customers need time to plan (6-12 months is typical)
- **Clear milestones:** When does functionality freeze? When does shutdown happen?
- **Data export deadline:** When do they lose access to their data?

---

### Step 7: Provide Clear Next Steps

```markdown
### Call to Action

- [Clear next steps for customers, e.g., "Log in to your account to start the migration wizard"]
- [Contact information for questions or assistance, e.g., "Contact our support team at support@acme.com or call 1-800-ACME-HELP"]
```

---

## Examples

See `examples/sample.md` for a full EOL message example.

Mini example excerpt:

```markdown
**Announcing:** We are discontinuing Acme Classic on Dec 31, 2026
**Because:** Legacy infrastructure limits performance
**Which means for you:** Faster automation + new integrations
```

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Business-Centric Rationale | "Discontinuing to reduce costs" | Frame around customer benefits: "Investing 100% in features you requested" |
| Vague Timeline | "Discontinued soon" | Specific dates: "March 1: Migration tool. December 31: Shutdown" |
| No Support Plan | "Migrate to Product Y. Good luck!" | Offer migration support: 1-on-1 assistance, auto-migration, discounts |
| Ignoring Customer Impact | Jumps from announcement to "Here's the new product!" | Acknowledge impact: "We understand this requires time to migrate" |
| Terse or Defensive Tone | "Low usage forced us to shut down" | Be empathetic: "Consolidating to focus on the future" |

---

## References

### Related Skills
- `skills/positioning-statement/SKILL.md` — Informs the transition solution positioning
- `skills/problem-statement/SKILL.md` — Helps frame the customer impact section
- `skills/proto-persona/SKILL.md` — Defines affected customers

### External Frameworks
- Crisis communication best practices — Transparency, empathy, action
- Customer success playbooks — Retention during product transitions

### Dean's Work
- EOL Messaging Template (created for product lifecycle management)

### Provenance
- Adapted from `prompts/eol-for-a-product-message.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

