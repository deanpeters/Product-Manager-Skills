---
name: eol-stakeholder-sequence
argument-hint: "[product being sunset, and who already knows]"
description: "Plan who to talk to about a sunset, in what order, and what each conversation must cover. Use when an EOL decision is made and you want the landmines found before the announcement."
intent: >-
  Plan the order and content of stakeholder conversations for an EOL decision. Encodes the
  hard-won lesson that EOL engagement has a specific sequence — legal exposure first, financial
  impact second, then revenue-facing teams, then customer-facing teams — and that getting the order
  wrong means discovering landmines after the announcement instead of before.
type: component
theme: eol-transition
best_for:
  - "Sequencing EOL conversations so each one informs the next"
  - "Knowing what to ask for and what to commit to at every stop"
  - "Finding the objection that would have blown up six months after the announcement"
scenarios:
  - "We're retiring a product and I don't know who to talk to first or what to bring them"
  - "Last sunset blew up because Sales had promised things we didn't know about — sequence this one properly"
estimated_time: "20-35 min"
---

# EOL Stakeholder Sequence

## Purpose

Plan the order of EOL conversations, and what each one must cover. The output is a sequenced list of
stops — each with what you need **from** them, what you owe **to** them, the red flags to listen
for, and what the conversation must produce.

EOL is not a broadcast. It is a series of conversations where each one informs the next, and each
one surfaces something the last one missed. Sequenced well, the awkward discoveries happen in a
conference room. Sequenced badly, they happen in public, after the announcement, in front of
customers.

## Input

**Works best with:** The product being sunset and who already knows about it.

**Also useful:** Scale (customers, revenue, contracts), whether channel partners or regulators are
involved, and any political sensitivities, strained relationships, or past surprises worth planning
around.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks up to three questions — what's being
sunset and who knows, how big the blast radius is, and whether there's history to plan around —
then builds the sequence. Political sensitivities are optional; the sequence works without them and
sharpens with them.

**Example invocations:**
- `Sequence the stakeholder conversations for retiring our legacy reporting module.`
- `Who do I talk to, in what order, about sunsetting a hardware line with 8 resellers?`

---

## Key Concepts

### The Sequencing Principle

**Talk to the people who can kill the plan before you talk to the people who have to execute it.**

Each conversation should inform the next. Legal exposure first, because a contract term can end the
discussion. Financial impact second, because it sizes everything downstream. Then revenue-facing
teams, then customer-facing teams, then the technical teams who will carry it out.

Get this backwards — brief Support first, Legal last — and you will have told forty people about a
plan that a single contract clause invalidates.

### Right-Size the Sequence

**Not all EOLs play out the same.** Most land in the middle:

| | **Level 1 — Light** | **Level 2 — Standard** | **Level 3 — Heavy** |
|---|---|---|---|
| Typical scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Stops | 3-4 | 7-8 | 10+ |
| Includes | Engineering, Support, affected users | + Legal, Finance, Sales, Marketing, CS, difficult customers | + Executives, Channel, Regulatory, key accounts |
| Skip unless there's a reason | Legal, Finance, Sales, Channel | Channel, Regulatory | — |

**Level 2 is the default.** Recommend a level, say why, then let the user move it. **Never default
to the heaviest sequence** — a ten-stop tour for a feature deprecation burns credibility you'll
want for the sunset that actually needs it.

If someone dials down, name the stop they're dropping and what it typically catches. Dropping Legal
on a product with contracts is the one worth pushing back on once — then honoring their call.

### The Canonical Order

Filtered by level, but the relative order holds:

**Level 1+**
1. **Engineering** — what depends on this technically
2. **Support** — what changes for support operations
3. **Affected users or internal teams** — who feels it first

**Level 2+ (inserted ahead of the above)**
1. **Legal** — contractual and regulatory exposure
2. **Finance** — revenue impact and forecast changes
3. **Sales** — pipeline, bundles, and *promises made in the field that never found their way into
   a contract or a ticket*
4. **Marketing** — you do not want to discover they just bought a quarter's worth of demand gen for
   the thing you killed
5. **Customer Success** — they will bear the brunt of this; work with them, not around them
6. **Your most difficult customers** — they will find the three things you forgot that would have
   blown up six months later

**Level 3+**
- **Executive leadership** — strategic approval
- **Channel partners** — inventory, commitments, and their own customer relationships
- **Regulatory bodies** — filings and compliance
- **Key accounts** — individual transition conversations

### Why Your Most Difficult Customers Belong in the Sequence

Counterintuitive, and the stop teams skip most often. The customer who files the most tickets and
pushes hardest in QBRs has, by construction, the deepest and weirdest usage of your product. They
will find the integration you forgot, the contract term nobody read, and the workflow that has no
equivalent in the replacement.

You can learn that from them in a scheduled call now, or from them on a public forum later.

### What You Need / What You Owe

Every stop has two directions. Skipping the second turns stakeholders into an audience:

- **What you need FROM them** — the input, approval, or knowledge only they have
- **What you owe TO them** — the context, commitment, or lead time they need to do their job

A conversation that is all extraction gets you compliance. A conversation that runs both ways gets
you the thing they weren't asked about.

### The Sticky-Note Rule

Every bullet is **4 to 8 words**. Sequences get read in hallways, before meetings, on phones.

### Anti-Patterns (what this is NOT)
- **Not a stakeholder map.** No power/interest grid. This is an ordered itinerary.
- **Not a broadcast plan.** The customer announcement is a different artifact.
- **Not parallelizable by default.** The order is the value; parallelize only where noted.
- **Not a RACI.** Decision rights are a separate question from conversation order.

---

## Application

### Step 1: Set the level

Recommend from blast radius, present all three, let the user choose. If unclear, ask:

"How complex is this sunset?
1. **Light** — a feature or internal tool. Few users, all reachable.
2. **Standard** — a commercial product with paying customers and contracts.
3. **Heavy** — revenue-critical, hardware, channel partners, or regulated.

Most are Standard. Which sounds like yours?"

### Step 2: Order the stops

Apply the canonical order, filtered by level. Two adjustments worth making:

- **Move a stop earlier** when history demands it. If Sales was blindsided last time, brief Sales
  earlier than the template says and note why.
- **Split a stop** when one function holds two different conversations. "Legal (contracts)" and
  "Legal (regulatory)" are often different people with different answers.

### Step 3: Build each stop

For every stop, fill five fields:

1. **When** — before or after which milestone or other stop
2. **Why this stop matters for EOL** — in 4-8 words
3. **What you need FROM them** — specific questions, not "input"
4. **What you owe TO them** — context, lead time, commitments
5. **Red flags to watch for** — the signals that this stop just surfaced a blocker

Then state the **output**: the decision, approval, or artifact the conversation must produce. A stop
with no output is a status update, not a stop.

### Step 4: Mark parallel vs. sequential

Say which stops must be strictly sequential and why, and which can safely run in parallel. Being
explicit here is what lets a team compress a ten-stop sequence into three weeks without breaking
the dependency that mattered.

### Step 5: Assumptions

Close with what you assumed — who you think knows, what you think the contracts say, which
relationships you think are intact.

### Final Step: Offer what comes next

"Where next?

1. **Build the phase-gated checklist** — the operational plan (Recommended)
2. **Draft talking points for the three most sensitive stops**
3. **Build the internal enablement pack** — support FAQ, sales talking points, objections
4. **Draft the customer announcement** — see [`eol-message`](../eol-message/SKILL.md)

Reply with a number, a combination ('1 & 3'), or your own path."

---

## Examples

- `examples/sample.md` — Fieldlight Classic Dispatch (SaaS, Level 2, eight stops)
- `examples/sample-industrial.md` — NFA-200 controller line (industrial, Level 3, eleven stops)

---

## Common Pitfalls

### Pitfall 1: Announcing Before Asking
**Symptom:** The sequence starts with a company-wide email.

**Consequence:** Every subsequent conversation is a negotiation with someone who found out the
wrong way and is now defending their turf instead of helping you.

**Fix:** The announcement is the *end* of the internal sequence, not the beginning.

---

### Pitfall 2: Legal Last
**Symptom:** Legal gets looped in once the plan is built, "to review."

**Consequence:** A contract term or regulatory obligation invalidates a plan forty people have
already committed to. Now you're relitigating instead of executing.

**Fix:** Legal is the first Level 2+ stop. A five-minute "are there commitments here?" beats a
five-week replan.

---

### Pitfall 3: Treating Sales as Recipients
**Symptom:** Sales is informed of the EOL date rather than asked what they've promised.

**Consequence:** Field commitments that never made it into a contract surface after the
announcement, from the customer's side, as accusations of bad faith.

**Fix:** Ask Sales explicitly: what has anyone promised about this product's future? Ask before you
tell.

---

### Pitfall 4: Skipping the Difficult Customers
**Symptom:** The sequence covers internal functions and stops.

**Consequence:** Your edge cases are discovered by the people least inclined to be quiet about them.

**Fix:** Two or three of your hardest customers, under NDA if needed, before the public
announcement. Budget for what they'll find.

---

### Pitfall 5: Extraction-Only Conversations
**Symptom:** Every stop is a list of things you need. Nothing is offered.

**Consequence:** Stakeholders answer the questions asked and volunteer nothing. The thing that
sinks you was the thing nobody thought to ask about.

**Fix:** Fill "what you owe them" for every stop before you hold it.

---

## References

### Related Skills

These stand on their own — none is a prerequisite for this skill, and this skill isn't a
prerequisite for them. If you already chose a level elsewhere, say "Level 2" and this skill builds
to it.

- [`eol-checklist`](../eol-checklist/SKILL.md) — the phase-gated operational plan
- [`eol-internal-enablement`](../eol-internal-enablement/SKILL.md) — what customer-facing teams get
  after these conversations
- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — if the decision still needs a case
- [`eol-message`](../eol-message/SKILL.md) — the customer-facing announcement
- [`stakeholder-mapping`](../stakeholder-mapping/SKILL.md) — general power/interest mapping for non-EOL work

### External Frameworks
- Mendelow's Matrix — power/interest prioritization, useful for choosing depth per stop
- DACI / RACI — decision rights, a separate question from conversation order

### Provenance
- Adapted from `prompts/eol-stakeholder-sequence.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
