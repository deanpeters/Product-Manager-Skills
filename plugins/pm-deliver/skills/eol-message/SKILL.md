---
name: eol-message
argument-hint: "[product or feature being retired]"
description: "Write a right-sized EOL announcement — brief notice through full phased comms — with rationale, customer impact, and next steps. Use when retiring a product, feature, or plan."
intent: >-
  Craft a clear, empathetic End-of-Life (EOL) message that communicates product or feature
  discontinuation, explains the rationale, addresses customer impact, provides transition support,
  and positions the replacement solution — sized to the blast radius. Use this to maintain customer
  trust during difficult transitions and reduce churn by demonstrating care and offering a clear
  path forward.
type: component
theme: eol-transition
best_for:
  - "Announcing a product, feature, or plan retirement without creating a support incident"
  - "Sizing the announcement to the change — a notice, not an opus, when the change is small"
  - "Handling the hard case: retiring something with no replacement"
scenarios:
  - "We're sunsetting our legacy module in December and I need to tell 800 accounts"
  - "We're discontinuing a hardware line with service contracts and channel partners — what do we send?"
estimated_time: "20-40 min"
---

# EOL Message

## Purpose

Craft a clear, empathetic End-of-Life (EOL) message that communicates discontinuation, explains the
rationale, addresses customer impact, provides transition support, and positions what comes next.
Use this to maintain customer trust during a difficult transition and reduce the churn that comes
from customers feeling abandoned.

This is not a generic sunset announcement — it's a customer-centric communication that acknowledges
loss while framing the change as progress. And it is **sized to the change**: a deprecated toggle
gets a paragraph, a flagship retirement gets phased communications across months.

## Input

**Works best with:** What's being retired (product, feature, or plan) and roughly when.

**Also useful:** The rationale, affected customer segments, migration or replacement path, support
commitments, and any contract or regulatory language that constrains what you can say.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks for the what/when/why and the landing
place before drafting, then recommends a message size you can override. An EOL message without a
stated rationale and a next step reads as abandonment — so those two get asked for either way.

**Example invocations:**
- `Draft an EOL message: retiring our legacy reporting module Dec 31, replaced by the new analytics dashboard; 400 accounts affected.`
- `We're killing a feature nobody uses. Give me the brief version — no replacement, 3 weeks notice.`

---

## Key Concepts

### Size the Message to the Change

The most common EOL messaging failure isn't tone — it's proportion. A six-section announcement for
a deprecated checkbox trains customers to ignore your notices. A one-line notice for a product
carrying real workflows creates a support incident.

| | **Brief** | **Standard** | **Full** |
|---|---|---|---|
| Use when | Feature, internal tool, unused option | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Length | 1-3 paragraphs | 1 page with phase table | Multi-part, phased over months |
| Sections used | Announcement, timeline, CTA | All 9, lightly | All 9 + compliance and obligations |
| Lead time | Weeks | 6-12 months | 12-24 months |
| Channels | In-app or changelog | Email + in-app + docs | Email + account teams + partners + press |

**Most announcements are Standard.** Recommend a size, explain why in one line, and let the user
move it. If they choose Brief for something you'd have sized Standard, note the single thing that
gets lost — usually the phase table, which is what prevents "wait, when does it stop working?"
tickets.

### The Three Transition Paths

What you're really telling customers is where they land. There are three answers, and they produce
genuinely different messages:

1. **Replacement** — another product of yours takes over. The message leans on continuity: what
   carries forward, what improves. Positioning matters most here.
2. **Migration** — same product family, different tier, configuration, or platform. The message
   leans on mechanics: what customers must do, by when, and how much work it is. Be honest about
   effort; understating it is the fastest route to distrust.
3. **Graceful exit** — nothing replaces it. The message leans on dignity: honest reasoning, data
   export, generous notice, and real alternatives *including competitors*. Naming a competitor
   costs less than the reputation damage of stranding people.

The graceful exit is the one teams write badly, because it's the one they feel worst about. It is
also the one customers judge you on hardest.

### Lifecycle Gates (shared vocabulary)

EOL is not one date, and collapsing the gates into a single announcement is what generates the
"but I thought it still worked" support wave:

- **GA (General Availability):** Actively sold and fully supported
- **NSC (Notice of Status Change):** The decision is communicated; planning begins
- **EOS (End of Sale):** No new customers can purchase
- **EOE (End of Expansion):** Existing customers cannot add capacity or seats
- **EOR (End of Renewal):** Existing contracts will not be renewed
- **EOM (End of Maintenance):** Bug fixes and patches stop
- **EOL (End of Life):** The product is retired
- **EOSRV (End of Service):** All support and service obligations end

Brief messages name two or three gates. Full messages name all eight in a table. **Whichever gates
you use, define them in the customer's terms** — "you can keep using it, but we won't ship fixes"
beats "EOM: 3/2027."

### The EOL Messaging Framework

An effective EOL message balances honesty about the change with empathy for customer impact:

1. **Company context:** Who you are and your commitment to customers
2. **The announcement:** What's ending and what's replacing it
3. **The rationale:** Why this benefits customers (not just the business)
4. **Current product context:** What the product was and who it served
5. **Customer impact:** How this affects users (acknowledge the disruption)
6. **Transition solution:** The landing place and how it compares
7. **Support measures:** How you'll help them get there
8. **Timeline:** Key dates and gates
9. **Call to action:** Next steps and contact info

### Why This Works
- **Empathy-first:** Acknowledges disruption before justifying the decision
- **Clarity:** No ambiguity about what's changing and when
- **Support-focused:** Shows you're not abandoning customers mid-transition
- **Future-oriented:** Frames change as progress, not loss

### The Sticky-Note Rule

A customer should be able to write what they must do, and by when, on a sticky note after one read.
If they can't, the message is decoration. Test every draft against this before sending.

### Anti-Patterns (What This Is NOT)
- **Not a terse shutdown notice:** "We're discontinuing Product X. Goodbye."
- **Not business-centric:** Don't lead with "This reduces our costs"
- **Not vague:** "Soon" is not a timeline
- **Not defensive:** Don't blame customers ("low usage forced us to shut down")
- **Not uniform:** The same template at the same length for every sunset is the proportion failure

### When to Use This
- Discontinuing a product, feature, or service
- Migrating customers from legacy to new platform
- Sunsetting an acquired product
- Deprecating a technology stack or API

### When NOT to Use This
- For minor tweaks that don't change what customers can do (don't over-communicate)
- Before you have a transition plan (communicate *after* you know how you'll support customers)
- If you're secretly hoping customers won't notice (be transparent)

---

## Application

Use `template.md` for the full fill-in structure.

### Step 1: Establish size and path

Before drafting, settle two things:

**Size:** Brief, Standard, or Full. Recommend one from the blast radius — customer count, revenue,
contracts, whether hardware or partners are involved — then let the user override. Say in one line
what a smaller size leaves out.

**Path:** Replacement, Migration, or Graceful exit. This determines what the message emphasizes and
whether the Transition Solution section is a positioning statement or an exit plan.

### Step 2: Gather context

- **Product being discontinued:** What specifically is ending?
- **Landing place:** What's replacing it, if anything?
- **Timeline:** Which gates apply, and what date does each land on?
- **Customer impact:** How many users? What workflows disrupted?
- **Support plan:** Migration help, training, discounts, data export tools
- **Rationale:** Why is this happening?
- **Constraints:** Contract language, regulatory requirements, "lifetime" promises made

**If missing context:** Don't send until you have a transition plan. Customers will ask "What do I
do now?" — you must have an answer. Drafting is fine; sending is not.

---

### Step 3: Draft the transition narrative

#### Company Context

```markdown
**We are:** [Company and its relationship to the product being phased out]
- [Commitment to customers]
- [How the product line evolves]
- [Where you're headed]
```

**Example:**
```markdown
**We are:** Fieldlight, a field service management platform serving 4,000 service businesses
- We're committed to getting your technicians to the right job with the right information
- We continuously evolve the platform based on how crews actually work
- We're building toward scheduling that adapts in real time to what happens in the field
```

#### The Announcement

```markdown
**Announcing:**
- [Single sentence stating the EOL clearly and naming the landing place]
```

**Example:** "We are retiring Fieldlight Classic Dispatch on December 31, 2026, and moving all
accounts to Fieldlight Next Scheduling."

**Graceful exit variant:** "We are retiring Fieldlight Route Optimizer on June 30, 2027. We do not
have a replacement, and we want to be direct about that."

#### The Rationale (customer-benefit-focused)

```markdown
**Because:**
- [Reason 1]
- [Reason 2]
- [Reason 3]

**Which means for you:**
- [Impact and benefits from the customer's perspective]
```

**Example:**
```markdown
**Because:**
- Classic Dispatch runs on infrastructure that can't support real-time schedule changes
- Next Scheduling reoptimizes routes as jobs run long or get cancelled
- Consolidating lets us put all engineering effort into one scheduler instead of two

**Which means for you:**
- Schedules that adjust when the day goes sideways, instead of at 6am only
- Technician arrival windows you can actually promise customers
- Every future scheduling improvement lands in the product you're on
```

---

### Step 4: Provide current product context

Acknowledge what's being lost. Skip this section in Brief messages.

```markdown
**Our product** [name]
- **is a** [description and primary function]
- **that has served** [customer type] for [duration]
- **by providing** [key benefits it delivered]
```

---

### Step 5: Acknowledge customer impact

Be honest about disruption. Understating effort here is the most damaging shortcut in the whole
message.

```markdown
**We understand that this may affect you by:**
- [Impact 1 on operations or process]
- [Impact 2]
- [Impact 3]
```

**Example:**
```markdown
**We understand that this may affect you by:**
- Requiring you to rebuild recurring dispatch rules (most accounts: 2-3 hours)
- Retraining dispatchers on a different scheduling board
- Updating any integrations that read the Classic dispatch API
```

---

### Step 6: Present the transition solution

**Replacement or Migration path** — use positioning statement format (see
[`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md)):

```markdown
**For** [affected customer]
- **that currently use** [old product]
- [replacement]
- **is a** [category]
- **that** [benefit, focused on continuity and improvement]

### Differentiation and Continuity
- **Like** [old product],
- [replacement]
- **provides** [what carries forward]
- **while also offering** [what's new]
```

**Graceful exit path** — replace the above with an honest exit plan:

```markdown
### What Happens to Your Data
- [Export format, how to get it, how long it stays available]

### Alternatives We'd Point You To
- [Option 1, including competitors, with a note on fit]
- [Option 2]

### What We're Doing to Help
- [Extended access, export tooling, migration credits, refunds where owed]
```

---

### Step 7: Outline support measures and timeline

```markdown
**To ensure a smooth transition, we will:**
- [Support measure 1]
- [Support measure 2]
- [Support measure 3]

### Timeline
| Gate | Date | What it means for you |
|---|---|---|
| [Gate] | [Date] | [Plain-language consequence] |
```

**Quality checks:**
- **Sufficient lead time:** 6-12 months is typical for Standard; longer for contracts and hardware
- **Gates in customer language:** "stops receiving fixes," not "EOM"
- **Data export deadline stated explicitly:** when do they lose access to their own data?

---

### Step 8: Provide clear next steps

```markdown
### Call to Action
- [Specific first action, with the link or path]
- [How to get help, with real contact info]
```

---

### Final Step: Offer what comes next

After delivering the draft, offer numbered options:

"Here's where you might go next:

1. **Pressure-test it** — I'll read it back as a skeptical customer and flag what's unclear
2. **Resize it** — produce the Brief or Full version of this same message
3. **Segment it** — variants for enterprise accounts, SMB, and partners, who need different things
4. **Check the readiness case** — see [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md)
   if the decision itself still needs defending

Pick a number, combine them, or tell me what you need."

---

## Examples

- `examples/sample.md` — Fieldlight Classic Dispatch (SaaS, Standard size, Replacement path)
- `examples/sample-industrial.md` — NFA-200 controller line (industrial, Full size, Replacement
  plus channel and regulatory obligations)

Mini excerpt:

```markdown
**Announcing:** We are retiring Fieldlight Classic Dispatch on December 31, 2026
**Because:** Classic can't support real-time schedule changes
**Which means for you:** Schedules that adjust when the day goes sideways
```

---

## Common Pitfalls

### Pitfall 1: Business-Centric Rationale
**Symptom:** "We're discontinuing Product X to reduce costs and consolidate our portfolio."

**Consequence:** Customers feel like collateral damage in a business decision.

**Fix:** Frame rationale around customer benefit: "We're consolidating to Product Y so we can
invest all our engineering in the features you've asked for."

---

### Pitfall 2: Vague Timeline
**Symptom:** "Product X will be discontinued soon."

**Consequence:** Customers can't plan. Anxiety and churn increase.

**Fix:** Specific dates against named gates: "March 1: no new purchases. December 31: full
shutdown, data export deadline."

---

### Pitfall 3: No Support Plan
**Symptom:** "You'll need to migrate to Product Y. Good luck!"

**Consequence:** Customers feel abandoned. High churn risk.

**Fix:** Offer real help: 1-on-1 assistance, auto-migration tooling, transition pricing, training.

---

### Pitfall 4: Ignoring Customer Impact
**Symptom:** The message jumps from announcement to "Here's the new product!"

**Consequence:** Customers feel their concerns aren't acknowledged.

**Fix:** Explicitly name the disruption, including how long the work will take them.

---

### Pitfall 5: Terse or Defensive Tone
**Symptom:** "Due to low usage, we're shutting down Product X."

**Consequence:** Sounds like you're blaming the customers who did use it.

**Fix:** Be empathetic and forward-looking. Low usage is your business context, not their fault.

---

### Pitfall 6: One Size For Every Sunset
**Symptom:** Every retirement gets the same full-length template, or every one gets a changelog line.

**Consequence:** Full-length notices for trivial changes train customers to ignore you — so the one
that matters gets ignored too. Changelog lines for real retirements become support incidents.

**Fix:** Choose Brief, Standard, or Full deliberately, and say why. When you go smaller, know which
section you dropped.

---

## References

### Related Skills

These stand on their own — none is a prerequisite for this skill, and this skill isn't a
prerequisite for them. If you ran a readiness assessment and landed on an intensity level, just
mention it ("Level 2") and this skill will size the message accordingly.

- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — the go/no-go decision and
  intensity dial, if the retirement itself still needs a case
- [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md) — informs the transition solution
- [`problem-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/problem-statement/SKILL.md) — helps frame the customer impact section
- [`proto-persona`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/proto-persona/SKILL.md) — defines the affected customers for segmented
  variants

### External Frameworks
- Crisis communication best practices — transparency, empathy, action
- Customer success playbooks — retention during product transitions

### Provenance
- Adapted from `prompts/eol-for-a-product-message.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
