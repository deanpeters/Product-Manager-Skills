---
name: lifecycle-play-advisor
argument-hint: "[product that's fading, and what makes you think so]"
description: "Diagnose where a product sits in its lifecycle and which play fits — extend, replace, or retire. Use when a product is fading and you need the call, not just the worry."
intent: >-
  Guided triage for a product at the mature-to-decline inflection. Establishes the lifecycle stage
  from the transition questions, identifies what is actually driving the pressure, tests the
  extension play before conceding to replacement or retirement, and routes to the skill that
  executes the chosen play.
type: interactive
theme: product-lifecycle
best_for:
  - "Settling an extend-versus-replace-versus-retire argument with a diagnosis instead of volume"
  - "Checking whether a product is really in decline or just badly distributed"
  - "Finding the cheapest play that actually addresses the pressure"
scenarios:
  - "Revenue's been flat for a year and half the team wants a rewrite and half wants to kill it"
  - "Leadership says this product is dying — is it, and what should we actually do about it?"
estimated_time: "15-25 min"
---

# Lifecycle Play Advisor

## Purpose

Work out what to do with a product that has stopped growing. Three plays are available — **extend**,
**replace**, **retire** — and this skill gets you to the right one through diagnosis rather than
debate, then hands you to whichever skill executes it.

Most teams argue the play before establishing the stage. The argument is unwinnable that way,
because nobody has agreed on what's actually happening to the product. Four questions fixes that.

This skill is deliberately willing to say **"nothing yet."** A mature product throwing off margin
with manageable support cost doesn't need a play; it needs to be left alone and watched.

## Input

**Works best with:** The product, and what makes you think something needs to change.

**Also useful:** Revenue trend and over how long, support load, what customers say, whether an
internal driver (cost, capacity, strategy) is really behind the question, and what investment
appetite exists.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The diagnosis runs on questions a PM can answer from
what they already know — no report-pulling required. "I don't know" is a valid answer and becomes a
labeled assumption in the recommendation.

**Example invocations:**
- `Our reporting module has been flat six quarters and people want to rebuild it. Extend, replace, or retire?`
- `Leadership wants to kill our parts module. Walk me through whether that's right.`

---

## Key Concepts

### The Three Plays

- **Extend** — add a variant or capability to the existing line. The product keeps running; you add
  alongside. Cheapest, lowest risk, most often skipped because it isn't exciting.
- **Replace** — ship a successor and phase the old one out. **GTM and EOL run simultaneously**, for
  two products that compete with each other. The expensive play.
- **Retire** — phase out with no successor of your own. Customers land elsewhere, possibly with a
  competitor. The goal becomes losing the product without losing the customer.

And the fourth answer that isn't a play: **harvest** — stop investing, keep running, set a review
date.

### Diagnosis Before Play

The seven transition questions establish stage; the pressure source discriminates the plays. Run
both before recommending anything, and show your work — a recommendation the user can audit is one
they can defend to someone else.

### The Extension Bias

**Default toward the cheapest play that addresses the actual pressure.** Extension is
under-considered in almost every room, because replacement is more interesting to build and
retirement is more decisive to announce. Test extension explicitly, and record why it failed when
it does.

### Anti-Patterns (what this is NOT)
- **Not a growth strategy tool.** Where the next tranche of growth comes from is a different
  question — see `ansoff-matrix` and `organic-growth-advisor`.
- **Not a kill switch.** "Nothing yet" and "harvest" are real outcomes.
- **Not the execution.** It routes to the skill that runs the chosen play.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol. Give
the heads-up at the start — four questions, about fifteen minutes — and let the user dump context
to skip ahead.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

---

## Application

This skill asks **up to 4 adaptive questions**, then recommends a play with its reasoning, its
hazards, and a route out.

---

### Question 1 of 4 — What product, and what makes you think something's wrong?

**Agent asks:**

"Which product are we looking at, and what prompted the question? The prompt matters as much as the
product — flat revenue, rising support costs, a competitor move, and an exec remark lead to very
different diagnoses."

**Listen for whether the trigger is internal or external.** An internal trigger — manufacturing
wants the line, engineering wants to rewrite, finance wants the cost out — is legitimate, but it
means the customer-facing case for change is weak and the transition has to be carried entirely by
you. Name that early; it changes what the play costs.

---

### Question 2 of 4 — Where is it actually in the lifecycle?

**Agent asks:**

"Let's establish the stage. Seven quick reads — yes or no, gut answers are fine:

1. Is defending market share still profitable?
2. Are loyalty efforts no longer retaining users?
3. Are legacy support costs becoming unsustainable?
4. Should we be running migration campaigns instead of loyalty ones?
5. Are we losing money on certain distribution channels?
6. Are our value-add bundles losing effectiveness?
7. Is our data shifting from predictive to transitional?"

**Score it:**

| Yes count | Stage | Implication |
|---|---|---|
| 0-1 | Mature and healthy | No play needed. Invest or leave alone |
| 2-3 | Mature and softening | Extension territory; watch quarterly |
| 4-5 | Crossing into decline | Pick a play deliberately, now |
| 6-7 | In decline | Replace or retire; extension likely just delays |

**Say the count back and name the pattern**, not just the number. Yeses clustered on 5 and 6
(channel and price) point somewhere very different from yeses on 3 and 7 (support cost and data) —
the first pattern is a distribution problem wearing a product costume.

---

### Question 3 of 4 — What's actually driving the pressure?

**Agent asks:**

"Three sources. Which is loudest?

1. **Demand-side** — customer needs shifted, segments moved, a competitor differentiated
2. **Supply/cost-side** — components, production cost, support load, or a strategy change
3. **Capability-side** — the technology is obsolete or the architecture has hit its limit

Pick one as primary, even if two apply."

**Why this discriminates:**

| Pressure | Points toward | Because |
|---|---|---|
| Demand-side | **Extend** | The core still solves a real problem for someone — find them |
| Supply/cost-side | **Replace** | The problem is your economics, not the customer's need |
| Capability-side | **Replace** or **Retire** | Depends on whether the need survives the technology |

**Name the trap out loud:** supply-side pressure arrives at the roadmap disguised as a customer
problem. "We need to rebuild this" often means "our costs are bad." That's a legitimate reason for a
replacement — but saying it plainly changes what success looks like and who has to carry the
transition.

---

### Question 4 of 4 — Test the extension play

**Agent asks:**

"Before I recommend anything more expensive, four questions on extending what you have:

1. Is there a **segment** a variant could serve?
2. Is there a **capability** you could add without re-architecting?
3. Would a **repackage or rebrand** reach a different buyer?
4. Is the decline in the **product**, or in the **channel or price** around it?"

Question 4 catches the most expensive misdiagnosis in the set: a healthy product condemned because
the distribution channel stopped working or the bundle lost its edge. Fixing the lever is far
cheaper than replacing the product — and the broken lever carries straight over to the successor if
you don't.

**If all four are no**, extension is genuinely off the table, and now the user has the "no, because…"
on record for when someone asks in three months.

---

### Final Step: Recommend the play

Deliver this structure:

```markdown
## Lifecycle Play Recommendation: [Product]

**Stage:** [stage] — [n]/7 transition questions, clustered on [which]
**Primary pressure:** [demand / supply-cost / capability] — [evidence]
**Trigger was:** [internal / external] — [what that means for the transition]

### Recommended Play: [Extend / Replace / Retire / Harvest / Nothing yet]

**Because:** [two or three specifics from their answers]

**Extension test:** [passed and how, or failed and why — always state it]

**What this play costs:** [rough shape]

**What you're accepting by choosing it:** [the tradeoff, plainly]

### Hazards to plan for
- [The 2-3 hazards that apply to this play, from the seven]

### Assumptions I made
- [Anything answered "I don't know"]
```

Then offer numbered next steps:

"Where next?

1. **Run the retirement properly** — [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md)
   for the go/no-go, or [`eol-process`](../eol-process/SKILL.md) for the whole thing
2. **Build the replacement risk register** — see
   [`product-lifecycle-plays`](../product-lifecycle-plays/SKILL.md), especially the seven hazards
3. **Plan the extension** — [`organic-growth-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/organic-growth-advisor/SKILL.md) for which
   growth path the variant serves
4. **Run this across the whole line** — the portfolio worksheet in
   [`product-lifecycle-plays`](../product-lifecycle-plays/SKILL.md)

Pick a number, combine them, or tell me what you'd rather do."

**On a Replace recommendation, always add one line:** "A replacement is two funded workstreams — a
launch and a retirement. If the retirement isn't funded, you've chosen an extension with extra
steps."

---

## Examples

### Example A — SaaS, the answer is "your channel is broken, not your product"

**PM:** "Our Parts module has been flat for five quarters. Leadership wants to fold it into the core
platform and stop selling it separately."

**Agent (Q1):** "What prompted it — a customer signal, or an internal one?"

**PM:** "Internal. It's the smallest line item and someone noticed."

**Agent:** "Noted — that's an internal trigger, which means there's no customer pressure to help
carry a transition. Let's see whether the product agrees with leadership."

**Agent (Q2):** *runs the seven questions.* Yeses on 5 (losing money on certain channels) and 6
(bundles losing effectiveness). Everything else no.

**Agent:** "2 out of 7 — mature and softening, not declining. And the pattern is the interesting
part: both of your yeses are on channel and price. Nothing about the product itself came back
negative. Support cost is fine, retention is fine."

**Agent (Q3):** "What's driving the pressure?"

**PM:** "Honestly? We sell it through the same motion as everything else and it doesn't fit. Reps
don't lead with it."

**Agent (Q4):** *extension test.* Segment — yes, distributors have asked for a read-only tier.
Capability — yes, a read-only view is minor work. Repackage — yes, that's exactly the ask. Channel
or product — **channel.**

**Recommendation: Extend, and fix the channel.** Stage says mature-softening. Both decline signals
sit on distribution and pricing, not the product. A read-only distributor tier addresses a segment
that has actively asked, and it's small work. Folding it into the core would have retired a healthy
product to solve a sales-motion problem — and the sales-motion problem would have survived the
merge.

*What you're accepting:* a distributor tier means supporting a new buyer type. Small, but not zero.

---

### Example B — Industrial, the answer is "replace, and fund the retirement"

**PM:** "Manufacturing wants the NFA-200 line for NFA-500 capacity. So we're retiring the NFA-200."

**Agent (Q1):** "That's an internal trigger — a capacity constraint, not a customer need. Worth
flagging up front: the customer-facing case for change is weak here, so your organization carries
the entire transition. What's the revenue trend?"

**PM:** "Flat four quarters. Service revenue's actually growing."

**Agent (Q2):** *runs the seven.* Yeses on 4, 6, 7, and a soft 1. Support costs fine, retention
strong, channels profitable.

**Agent:** "4 out of 7 — mature and softening, not in decline. Your installed base is loyal, under
contract, and service margin is healthy. That matters, because it means this isn't a product
failing. It's a factory floor you want back."

**Agent (Q3):** "Primary pressure?"

**PM:** "Supply side. Manufacturing capacity."

**Agent (Q4):** *extension test.* Segment — partially; a modular I/O variant would open bigger jobs.
Capability without re-architecture — no, needs a new backplane. Repackage — no, industrial buyers
specify on capability. Channel or product — neither.

**Agent:** "Here's the thing worth saying out loud: the extension your customers would want *is*
the NFA-500. That's a strong signal the replacement play is right — and it raises the question you
need to answer before committing. **Is the NFA-500 a drop-in for the installed base?**"

**PM:** "...I'd assumed so. I don't actually know."

**Recommendation: Replace — with that question as a gate.**

*Hazards to plan for:* internal misalignment (medium), cannibalization (deliberate, low impact),
and **poor EOL management (high impact)** — which is entirely gated on the drop-in question. If the
NFA-500 needs different mounting or site work, you don't have a migration path, you have a project,
and an EOL date would be a promise you can't keep.

*Assumption labeled:* drop-in compatibility unverified.

**And the line that always goes on a Replace:** a replacement is two funded workstreams — a launch
and a retirement. Retrofit engineering unfunded means you've chosen an extension with extra steps.

---

## Common Pitfalls

### Pitfall 1: Recommending a Play Before the Stage Is Established
**Symptom:** The user names a play in their first message and the conversation optimizes it.

**Consequence:** You've validated an opinion rather than run a diagnosis, and the expensive
assumption inside it goes unexamined.

**Fix:** Run Q2 even when the user arrives certain. It takes two minutes and it either confirms
them or saves them a year.

---

### Pitfall 2: Letting the Count Replace the Pattern
**Symptom:** "4 out of 7, so you're in decline."

**Consequence:** Four yeses clustered on channel and price mean something completely different from
four on support cost and architecture. The count alone routes people wrong.

**Fix:** Always name which questions came back yes, and say what that cluster means.

---

### Pitfall 3: Accepting the Internal Trigger at Face Value
**Symptom:** "Manufacturing wants the line" becomes "the product should be retired."

**Consequence:** You run a full retirement when an End of Sale, a price change, or a repackage
would have satisfied the actual need more cheaply.

**Fix:** Name the trigger as internal, then ask what specifically it needs. Often the cheaper move
delivers it.

---

### Pitfall 4: Skipping the Extension Test on an Obvious Case
**Symptom:** The product is clearly dying, so Q4 gets waved through.

**Consequence:** No written record of why extension failed. In three months someone asks, and the
answer is a shrug.

**Fix:** Ask all four regardless. On a genuinely dead product it takes ninety seconds and produces
a defensible "no, because…"

---

### Pitfall 5: Treating "Nothing Yet" as a Non-Answer
**Symptom:** Every run produces a play, because producing a play feels like producing value.

**Consequence:** Healthy mature products get projects they didn't need, funded from budget that had
somewhere better to be.

**Fix:** 0-1 yeses means no play. Say so, set a review date, and stop.

---

## References

### Related Skills

These stand on their own — none is a prerequisite for this skill, and this skill isn't a
prerequisite for them.

- [`product-lifecycle-plays`](../product-lifecycle-plays/SKILL.md) — the framework behind this
  triage: the strategy grid, the seven hazards, the risk register, the portfolio worksheet
- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — the retirement play's go/no-go
- [`eol-process`](../eol-process/SKILL.md) — running a retirement end to end
- [`organic-growth-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/organic-growth-advisor/SKILL.md) — which growth path an extension
  serves
- [`ansoff-matrix`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/ansoff-matrix/SKILL.md) — where the next tranche of growth comes from
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) — the interaction protocol

### External Frameworks
- Product Life Cycle (PLC) — the five-stage economic model
- PLC strategy grid — marketing-mix levers by stage

### Provenance
- Distilled from practitioner experience running product lifecycle transitions and product
  retirements across software, hardware, and regulated industries.
