# EOL Message Template

Copy the block that matches your size, fill it in, then run the quality checks at the bottom.

## Provenance
Adapted from `prompts/eol-for-a-product-message.md` in the
`https://github.com/deanpeters/product-manager-prompts` repo.

---

## First: pick a size and a path

**Size** — most announcements are Standard:

| | Brief | Standard | Full |
|---|---|---|---|
| Use when | Feature, internal tool, unused option | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Length | 1-3 paragraphs | 1 page with phase table | Multi-part, phased over months |
| Lead time | Weeks | 6-12 months | 12-24 months |

**Path** — determines what the Transition Solution section becomes:

- **Replacement** — another product of yours takes over → positioning statement
- **Migration** — same family, different tier or platform → mechanics and effort
- **Graceful exit** — nothing replaces it → data, alternatives, dignity

---

## Brief template

```markdown
## [Product/Feature] is being retired on [date]

[One sentence: what's ending, when, and what replaces it — or that nothing does.]

**What you need to do:** [The single action, with a link.]

**What happens if you do nothing:** [Plain consequence on the date.]

Questions: [real contact]
```

---

## Standard / Full template

```markdown
## End-of-Life Announcement: [Product Name]

### Product Transition Narrative

**We are:** [Company and relationship to the product]
- [Commitment to customers]
- [Product evolution]
- [Future vision]

**Announcing:**
- [Clear EOL statement, date, and landing place]

**Because:**
- [Reason 1: customer-benefit focused]
- [Reason 2]
- [Reason 3]

**Which means for you:**
- [Customer impact and benefits]

### Current Product Context

**Our product** [name]
- **is a** [brief description]
- **that has served** [target customer] for [timeframe]
- **by providing** [key benefits]

### Customer Impact

**We understand that this may affect you by:**
- [Impact 1 — include how much work it is for them]
- [Impact 2]
- [Impact 3]

### Transition Solution

<!-- REPLACEMENT or MIGRATION path -->
**For** [target customer]
- **that currently use** [old product]
- [replacement product]
- **is a** [category]
- **that** [benefit focused on continuity and improvements]

### Differentiation and Continuity

- **Like** [old product],
- [replacement product]
- **provides** [continuity of key benefits]
- **while also offering** [new benefits]

<!-- GRACEFUL EXIT path — use instead of the two sections above -->
### What Happens to Your Data
- [Export format, how to retrieve it, how long it remains available]

### Alternatives We'd Point You To
- [Option 1, including competitors, with a fit note]
- [Option 2]

### What We're Doing to Help
- [Extended access, export tooling, credits, refunds where owed]

### Support and Next Steps

**To ensure a smooth transition, we will:**
- [Support measure 1]
- [Support measure 2]
- [Support measure 3]

### Timeline

| Gate | Date | What it means for you |
|---|---|---|
| End of Sale | [date] | [No new purchases — plain language] |
| End of Expansion | [date] | [No added seats/capacity] |
| End of Maintenance | [date] | [Still works; no more fixes] |
| End of Life | [date] | [Stops working] |
| End of Service | [date] | [Support and service obligations end] |

<!-- FULL size only -->
### Contractual and Regulatory Notes
- [Contract, SLA, or certification language customers need]
- [Refund, credit, or true-up terms where obligations remain]

### Call to Action
- [Specific next step, with link]
- [How to get help, with real contact info]
```

---

## Quality checks

Run these before sending. Any "no" is a rewrite, not a nitpick.

**Proportion**
- [ ] Size matches blast radius — and if you went smaller, you know which section you dropped
- [ ] The gates you named are the ones that actually apply (naming unused gates adds confusion)

**Clarity**
- [ ] **Sticky-note test:** after one read, a customer can write down what to do and by when
- [ ] Every gate is stated in customer consequences, not internal acronyms
- [ ] The data export deadline is explicit and unmissable
- [ ] No "soon," "in the coming months," or "at a future date"

**Empathy**
- [ ] Impact is acknowledged before benefits are pitched
- [ ] The effort estimate is honest — you'd stand behind it if a customer timed themselves
- [ ] Rationale is framed in customer benefit, not cost savings
- [ ] Nothing in the tone implies customers caused this by not using it enough

**Completeness**
- [ ] The landing place is named — including "there isn't one," said plainly
- [ ] Support measures are specific and real (not "contact support")
- [ ] Contact info is a channel actually staffed for this
- [ ] For graceful exits: alternatives are listed, competitors included where honest

**Obligations**
- [ ] Contract, SLA, and "lifetime" promise language has been checked by someone who can read it
- [ ] Nothing in the message contradicts what customers were sold
