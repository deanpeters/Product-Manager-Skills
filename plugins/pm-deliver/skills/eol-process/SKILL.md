---
name: eol-process
argument-hint: "[product being retired, and where you are in the process]"
description: "Run a product sunset end to end — decide, align, plan, prepare, announce, close. Use when you need the whole EOL process, not just one artifact."
intent: >-
  Orchestrate a complete product end-of-life from the go/no-go decision through post-retirement
  review, sequencing the decision, stakeholder alignment, operational plan, internal enablement,
  customer announcement, and closure. Right-sized so a feature deprecation runs in a week and a
  regulated hardware retirement runs across quarters. Use this to lose the product without losing
  the customer.
type: workflow
theme: eol-transition
best_for:
  - "Running a full product sunset from decision through post-EOL review"
  - "Knowing what has to happen before you can announce — and in what order"
  - "Rescuing a sunset already in motion by finding which phase got skipped"
scenarios:
  - "We've decided to retire a product and I own the whole thing — walk me through it end to end"
  - "We announced an EOL and it's going badly; what did we skip and what do we do now?"
estimated_time: "30-60 min to plan; weeks to quarters to execute"
---

# EOL Process

## Purpose

Run a product retirement end to end: decide whether to do it, align the people who can stop it,
build the operational plan, ready the teams who will face customers, announce it, and close it out
properly. Six phases with decision points between them.

The governing goal, and the sentence worth keeping in your head the whole way through: **lose the
product without losing the customer.** Most of what follows exists to protect the second half of
that sentence.

This is an orchestration skill. It doesn't replace the artifact skills — it tells you which one to
reach for, when, and what has to be true before you move on.

## Input

**Works best with:** The product being retired and where you currently are — considering it,
decided, mid-plan, or already announced and struggling.

**Also useful:** Scale (customers, revenue, contracts), whether a replacement exists, and who
already knows.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The process opens by establishing what's being retired
and where you are in it, then routes you to the right phase. If you're mid-sunset and something is
going wrong, say so — the diagnostic in "Entering Mid-Stream" finds the skipped phase.

**Example invocations:**
- `Run the full EOL process for our legacy reporting module — decision made, nothing else started.`
- `We announced a sunset three weeks ago and Support is drowning. What did we skip?`

---

## Key Concepts

### The Six Phases

| # | Phase | Question it answers | Primary artifact |
|---|---|---|---|
| 1 | **Decide** | Should we retire this, and how big is this? | Readiness assessment + intensity level |
| 2 | **Align** | Who can stop this, and what do they know that we don't? | Stakeholder sequence |
| 3 | **Plan** | What has to happen, when, and who owns it? | Phase-gated checklist |
| 4 | **Prepare** | Are our people ready before our customers hear? | Internal enablement pack |
| 5 | **Announce** | What do customers hear, and when? | Customer EOL message |
| 6 | **Close** | Did we finish, and what did we learn? | Post-EOL review |

**Phase 6 is the one everyone skips.** It's also the phase that makes your next sunset cheaper.
Budget for it up front, because nobody volunteers for it afterward.

### This Is a Route, Not a Pipeline

Every skill in this suite stands alone. None requires another to have run first. This process is a
**recommended route through independent stops**, not a conveyor belt — which means:

- **You can enter at any phase.** Decision already made and defensible? Start at Phase 2.
- **You can skip phases** when the level justifies it. A Level 1 sunset often collapses 2 through 4
  into a single afternoon.
- **You can go backwards, and sometimes must.** Phase 2 routinely sends you back to Phase 1 — a
  Legal finding or a Sales commitment can invalidate the decision. That's the process working, not
  failing.
- **Nothing hands off a format.** Carrying context between phases means telling the next skill
  "Level 2" and pasting what you have. There's no schema to preserve.

The order earns its keep because each phase surfaces what the next one needs. Deviate deliberately,
not accidentally.

### Right-Size the Whole Process

**Not all EOLs play out the same.** The process compresses or expands with the sunset:

| | **Level 1 — Light** | **Level 2 — Standard** | **Level 3 — Heavy** |
|---|---|---|---|
| Typical scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Elapsed time | Days to weeks | 6-12 months | 12-24 months |
| Phase 2 stops | 3-4 | 7-8 | 10+ |
| Phase 3 gates | 2-3 phases, no gate criteria | 4-5 phases with gates | All 6 phases, gates with approvers |
| Phase 4 output | Support FAQ | + Sales points, objections, escalation | + Channel brief, training |
| Phase 5 message | Brief notice | Standard with phase table | Full, phased, with compliance |
| Phases 2-4 | Often collapse into one sitting | Distinct, sequential | Distinct, with their own workstreams |

**Level 2 is the default.** Set the level in Phase 1, and let it size everything downstream.
**Never default to Level 3** — process theater on a small sunset teaches everyone to ignore the
process on a big one.

### Entering Mid-Stream

Most people find this skill in the middle of a sunset, often a troubled one. Symptoms map to the
phase that got skipped:

| Symptom | Phase skipped | What to do now |
|---|---|---|
| "Legal just found a contract problem" | 2 (Align) | Stop. Return to Phase 1 — the decision may not survive |
| "Sales says they promised this forever" | 2 (Align) | Inventory field commitments before any further comms |
| "Support is drowning in tickets" | 4 (Prepare) | Ship the FAQ and escalation ladder today; backfill the rest |
| "Customers say they never heard" | 5 (Announce) | Re-announce with dates; the first notice didn't land |
| "Nobody knows who owns what" | 3 (Plan) | Build the checklist; unowned items are the failure |
| "We shut it off and things broke" | 3 (Plan) | Downstream readers were never inventoried |
| "We did it and learned nothing" | 6 (Close) | Run the review now — memory decays fast |

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running any phase conversationally. Give the heads-up, take context dumps, offer numbered choices,
and let people bail to a specific phase.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a project plan.** It sequences decisions and artifacts, not tasks and resources.
- **Not mandatory in full.** Six phases at Level 1 is the ceremony failure this suite exists to
  prevent.
- **Not a substitute for the conversations.** Phase 2 is people talking, not a document.
- **Not one-directional.** Going back to Phase 1 is a success condition, not a rollback.

---

## Application

Use `template.md` as the one-page tracker for a sunset in flight.

This workflow orchestrates **6 phases** with a decision point after each. Elapsed time runs from
days at Level 1 to two years at Level 3 — set the level in Phase 1 and let it size the rest. Each
phase names the skill that produces its artifact, but every one of those skills also runs standalone,
so enter wherever you actually are.

---

## Phase 1: Decide

**Question:** Should we retire this, and how big is this?

### Activities
1. Name the trigger honestly — a metric, a strategy shift, a cost complaint, or an exec remark.
   The trigger predicts the failure mode.
2. Assess retire signals against hold signals. Two or more strong retire signals is a real case;
   an obligation lock or a missing landing place can outweigh all of them.
3. **Set the intensity level.** Recommend from blast radius, then choose deliberately. This sizes
   every phase that follows.
4. Confirm the landing place: replacement, migration, or graceful exit — and whether it's ready.

Run [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) for this phase.

### Outputs
- A verdict: Go, Go-with-conditions, Hold, or Harvest
- An intensity level (1, 2, or 3)
- A named landing place with a readiness status
- A list of obligations to check before announcing

### Decision Point 1: Is this a Go, and is the landing place real?

- **Go** → proceed to Phase 2
- **Go-with-conditions** → proceed to Phase 2, carrying the condition as a gate on Phase 5
- **Hold** → stop. Set a revisit trigger. Consider whether a cheaper move (End of Sale only, a
  price change, a bug fix) satisfies the actual need
- **Harvest** → stop the investment, not the product. Set a review date

**If the landing place isn't ready**, you may proceed through Phases 2-4 but **not** Phase 5. Do
not announce a transition you can't yet support.

---

## Phase 2: Align

**Question:** Who can stop this, and what do they know that we don't?

### Activities
1. Order the stops: Legal, Finance, Sales, Marketing, CS, difficult customers, Engineering,
   Support — filtered by level, plus Executives, Channel, and Regulatory at Level 3.
2. For each stop, prepare what you need **from** them and what you owe **to** them.
3. Hold the conversations in order. Each one informs the next.
4. Capture what surfaced — especially field commitments, contract terms, and hidden dependencies.

Run [`eol-stakeholder-sequence`](../eol-stakeholder-sequence/SKILL.md) for this phase.

### Outputs
- A completed sequence with an output per stop
- An inventory of commitments, obligations, and dependencies discovered
- A revised impact list from your most difficult customers

### Decision Point 2: Did anything invalidate the decision?

This is the most important gate in the process, and the one teams treat as a formality.

- **Nothing blocking** → proceed to Phase 3
- **A contract, regulation, or commitment blocks the timeline** → return to Phase 1. Reassess with
  the new evidence. The date moves, the scope changes, or the verdict flips
- **The landing place turns out to be weaker than believed** → return to Phase 1. This is the
  single most common finding, and it usually arrives from the difficult-customer stop

Returning to Phase 1 here is cheap. Discovering the same thing after Phase 5 is not.

---

## Phase 3: Plan

**Question:** What has to happen, when, and who owns it?

### Activities
1. Select the lifecycle gates in scope — and name the ones you're deliberately not using.
2. Build items per phase, per functional area, at the level you set. Every item: a verb, 4-8 words,
   a named owning function.
3. Write gate criteria with approvers for each phase transition (Level 2+).
4. Cover the four things sunsets strand: **data, contracts, access, money.**
5. Put the Phase 4 "enablement complete" date on the plan, **before** the Phase 5 announcement date.

Run [`eol-checklist`](../eol-checklist/SKILL.md) for this phase.

### Outputs
- A phase-gated checklist with owners and dates
- Gate criteria with named approvers
- Post-EOL actions, including the Phase 6 review, owned
- Assumptions to validate

### Decision Point 3: Is every item owned, and is every date real?

- **Unowned items** → that's the finding. Escalate rather than papering over it
- **A date you can't defend** → write `TBD`, or `Not scheduled` with the precondition. An invented
  EOL date is a promise you will break in public
- **Enablement date not before announcement date** → fix it now; in practice they collapse

---

## Phase 4: Prepare

**Question:** Are our people ready before our customers hear?

### Activities
1. Build the support FAQ, organized by what customers actually ask, highest call volume first.
2. Build sales talking points with an honest comparison table — **including the gaps.**
3. Write objection handling using Acknowledge-Reframe-Offer, with **every offer pre-approved.**
4. Name the escalation ladder — four rungs, real people.
5. At Level 3, add the channel partner brief and run live training with role-play.

Run [`eol-internal-enablement`](../eol-internal-enablement/SKILL.md) for this phase.

### Outputs
- An enablement pack sized to the level
- An escalation ladder a rep could use at 4pm on a Friday
- Partners briefed ahead of the public notice (Level 3)

### Decision Point 4: Is enablement actually complete?

**This gates the announcement.** The cardinal sin of EOL communication is handing Support and Sales
the announcement five minutes before customers get it.

Test it: ask a rep who they'd call about a churn threat, and ask them to answer the hardest
objection out loud. If either answer is a shrug, you are not ready to announce.

---

## Phase 5: Announce

**Question:** What do customers hear, and when?

### Activities
1. Size the message: Brief, Standard, or Full.
2. Choose the path: replacement, migration, or graceful exit — each produces a different message.
3. Draft against the nine-section framework, acknowledging impact before pitching benefits.
4. State the gates in customer consequences, not internal acronyms.
5. Apply the **sticky-note test**: after one read, can a customer write down what to do and by when?
6. Segment where it matters — enterprise, SMB, at-risk accounts, and partners need different things.

Run [`eol-message`](../eol-message/SKILL.md) for this phase.

### Outputs
- The customer announcement, sized and pathed
- Segment variants where warranted
- A comms calendar across the gates, not a single send

### Decision Point 5: Does the announcement survive contact?

Before sending, check three things:
- **Legal has read it** — especially anything about contracts, refunds, or certification
- **It doesn't contradict what customers were sold** — check against the field commitments from
  Phase 2
- **Support has it first** — with enough lead time to have read it

---

## Phase 6: Close

**Question:** Did we finish, and what did we learn?

### Activities
1. Walk the gates as they arrive. Each transition needs its criteria met and its approver's sign-off
   — gates are commitments, not calendar entries.
2. Track migration or transition progress against the Phase 3 targets. Escalate accounts with zero
   movement early, not at the last gate.
3. Complete the closure items: data export windows honored, deletion scheduled, contracts closed,
   revenue recognition ended, infrastructure decommissioned, documentation archived.
4. **Run the lessons-learned review.** What surprised you, which phase you under-invested in, what
   the difficult customers found that you'd missed, and what the retention actually was against
   forecast.
5. Where an EOL date was left unscheduled, hand off the precondition to a named owner with a
   review date.

### Outputs
- Gates closed with sign-offs
- Final retention or transition numbers against forecast
- A written lessons-learned review
- Any deferred decisions explicitly owned

### Decision Point 6: Is this actually closed?

Closure is not the shutdown date. It's when the data is gone or delivered, the contracts are
settled, the money is recognized, and someone has written down what happened. If the review hasn't
been run, the sunset isn't finished — it's just quiet.

---

## Complete Workflow: End-to-End Summary

```
PHASE 1: DECIDE                          -> eol-readiness-advisor
  Trigger -> signals -> intensity level -> landing place
  DP1: Go / Go-with-conditions / Hold / Harvest
       Landing place not ready? Phases 2-4 OK, Phase 5 blocked
       |
PHASE 2: ALIGN                           -> eol-stakeholder-sequence
  Legal -> Finance -> Sales -> Marketing -> CS -> difficult customers
  -> Engineering -> Support  (+ Execs, Channel, Regulatory at L3)
  DP2: Did anything invalidate the decision?  --[yes]--> back to Phase 1
       |
PHASE 3: PLAN                            -> eol-checklist
  Gates in scope -> items with owners -> gate criteria -> data,
  contracts, access, money -> enablement date BEFORE announce date
  DP3: Every item owned? Every date real?
       |
PHASE 4: PREPARE                         -> eol-internal-enablement
  Support FAQ -> sales points with gaps -> objections (offers
  pre-approved) -> escalation ladder -> channel brief + training (L3)
  DP4: Enablement complete?  --[no]--> DO NOT ANNOUNCE
       |
PHASE 5: ANNOUNCE                        -> eol-message
  Size -> path -> draft -> sticky-note test -> segment -> comms calendar
  DP5: Legal read it? Consistent with field promises? Support has it?
       |
PHASE 6: CLOSE                           -> (this skill)
  Walk gates -> track progress -> close data/contracts/money ->
  LESSONS-LEARNED REVIEW -> own any deferred decisions
  DP6: Data settled, contracts closed, review written?
```

**Level 1 compression:** Phases 2, 3, and 4 often collapse into one sitting — a short stakeholder
list, a punch list, and a support FAQ. Phases 1, 5, and 6 still happen. Especially 6.

---

## Examples

- `examples/sample.md` — Fieldlight Classic Dispatch (SaaS, Level 2, all six phases across ten
  months)
- `examples/sample-industrial.md` — NFA-200 controller line (industrial, Level 3, where Phase 2
  sends the process back to Phase 1 and changes the outcome)

---

## Common Pitfalls

### Pitfall 1: Starting at Phase 5
**Symptom:** The first artifact anyone builds is the customer announcement.

**Consequence:** You announce, then discover the contract terms, the field promises, and the
missing migration path — in public, with a date already committed.

**Fix:** The announcement is the fifth phase for a reason. Everything before it exists to make it
survivable.

---

### Pitfall 2: Treating Decision Point 2 as a Formality
**Symptom:** Stakeholder conversations happen, findings get noted, the plan proceeds unchanged.

**Consequence:** You held the conversations and ignored them, which is worse than skipping them —
you now have witnesses who warned you.

**Fix:** DP2 is a real gate. If Legal or your difficult customers surfaced something material,
return to Phase 1 and reassess. That loop is the process working.

---

### Pitfall 3: Announcing Before Enablement
**Symptom:** Phase 4 and Phase 5 land in the same week, or Phase 4 slips and Phase 5 doesn't.

**Consequence:** Support improvises for three days and their improvisations become your de facto
policy — inconsistently.

**Fix:** DP4 gates DP5 on the plan, with separate dates. If enablement slips, the announcement
slips.

---

### Pitfall 4: Process Theater on a Small Sunset
**Symptom:** A deprecated feature gets ten stakeholder stops and a training program.

**Consequence:** Everyone learns EOL process is bureaucracy and skips it next time — and next time
is the one with the contracts.

**Fix:** Set the level in Phase 1 honestly. A Level 1 sunset that runs in an afternoon and closes
properly is a success.

---

### Pitfall 5: Skipping Phase 6
**Symptom:** The product shuts off, the team moves on, nobody writes anything down.

**Consequence:** The next sunset repeats every mistake, and the data-deletion and contract-closure
items quietly go undone.

**Fix:** Put the review on the Phase 3 checklist with a named owner while people still care.
Closure is not the shutdown date.

---

### Pitfall 6: Losing the Customer With the Product
**Symptom:** Every phase is executed competently, measured entirely in internal completion.

**Consequence:** A clean retirement and a churn spike. You ran a good process and still lost the
relationship.

**Fix:** Track retention as the outcome measure, not checklist completion. The goal is losing the
product without losing the customer — if the second half didn't happen, the process didn't succeed.

---

## References

### Related Skills

Every skill below stands alone. This process recommends a route through them; none of them requires
this skill, and this skill doesn't require you to run all of them. Carry context between phases by
saying "Level 2" and pasting what you have.

- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — Phase 1
- [`eol-stakeholder-sequence`](../eol-stakeholder-sequence/SKILL.md) — Phase 2
- [`eol-checklist`](../eol-checklist/SKILL.md) — Phase 3
- [`eol-internal-enablement`](../eol-internal-enablement/SKILL.md) — Phase 4
- [`eol-message`](../eol-message/SKILL.md) — Phase 5
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) — interaction protocol throughout
- [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md) — for the Phase 5 transition solution
- [`stakeholder-mapping`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/stakeholder-mapping/SKILL.md) — general mapping, if Phase 2 needs breadth first

### External Frameworks
- Product Life Cycle (PLC) — EOL lives in the decline stage
- Industry EOL lifecycle practice (GA/NSC/EOS/EOE/EOR/EOM/EOL/EOSRV)
- Acknowledge-Reframe-Offer — objection handling in Phase 4

### Provenance
- Orchestrates the EOL prompt series in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
