---
name: eol-checklist
argument-hint: "[product being sunset, and any hard dates]"
description: "Build a phase-gated EOL checklist sized to the sunset, with a named owner on every item. Use when the decision to retire is made and you need the operational plan."
intent: >-
  Generate a phase-gated EOL checklist tailored to the complexity of the sunset. Covers up to 15
  functional areas across the lifecycle gates, but right-sizes the output so a minor feature
  deprecation gets a short punch list while a flagship product retirement gets the full
  cross-functional playbook. Every item names a verb and an owner.
type: component
theme: eol-transition
best_for:
  - "Turning a sunset decision into an operational plan with owners and dates"
  - "Making sure a retirement doesn't strand data, contracts, or inventory"
  - "Right-sizing process so a feature deprecation doesn't get a flagship playbook"
scenarios:
  - "We've decided to retire the legacy module in December — what actually has to happen between now and then?"
  - "Hardware line with channel partners and service contracts; I need the full cross-functional checklist"
estimated_time: "20-40 min"
---

# EOL Checklist

## Purpose

Turn a sunset decision into a phase-gated operational plan: what must happen, in which lifecycle
phase, and who owns it. The output is a working checklist — sticky-note-sized items, each with a
verb and a named function — not a strategy document.

The checklist is **sized to the sunset**. A deprecated internal tool gets a dozen items across
three phases. A regulated hardware line gets a cross-functional playbook across six phases with
gate criteria between them. Both are correct; using the wrong one is the failure.

## Input

**Works best with:** The product being sunset and any dates you're already committed to.

**Also useful:** Customer and revenue scale, whether a replacement exists and how ready it is,
contract or regulatory obligations, and whether hardware, inventory, or channel partners are in
play.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks up to three questions — what's being
sunset and at what scale, whether there's a replacement, and what hard deadlines exist — then picks
a level and builds. Unknowns become labeled assumptions rather than blockers.

**Example invocations:**
- `EOL checklist for our legacy reporting module, shutting down Dec 31, ~400 accounts.`
- `Build the heavy checklist for a hardware retirement — service contracts, 8 resellers, UL certified.`

---

## Key Concepts

### Right-Size Before You Build

**Not all EOLs play out the same.** Most land in the middle. Pick the level deliberately:

| | **Level 1 — Light** | **Level 2 — Standard** | **Level 3 — Heavy** |
|---|---|---|---|
| Typical scope | Feature, internal tool, unversioned API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Phases used | 2-3 (NSC, EOS, EOL) | 4-5 (NSC, EOS, EOE, EOM, EOL) | All 6 (NSC through EOSRV) |
| Functional areas | 4 | 11 | 15 |
| Gate criteria | Not needed | Between major phases | Between every phase, with approvers |
| Output feel | Punch list | Working checklist with owners and dates | Cross-functional playbook |

**Level 2 is the default.** Recommend a level, say why in one line, and let the user move it. If
they go lighter, name the specific area that drops out so the choice is informed. **Never default
to Level 3** — a heavy checklist applied to a light sunset teaches teams that EOL process is
ceremony, and they'll skip it next time when it matters.

The level is yours to change mid-build. "Actually make this heavier" is a normal thing to hear
after the Legal row surfaces something.

### The Lifecycle Gates

- **GA (General Availability):** Actively sold and fully supported
- **NSC (Notice of Status Change):** The decision is communicated; planning begins
- **EOS (End of Sale):** No new customers can purchase
- **EOE (End of Expansion):** Existing customers cannot add capacity or seats
- **EOR (End of Renewal):** Existing contracts will not be renewed
- **EOM (End of Maintenance):** Bug fixes and patches stop
- **EOL (End of Life):** The product is retired
- **EOSRV (End of Service):** All support and service obligations end

**Which of these become checklist phases:** GA is a *state*, not a phase of work — nothing is
checklisted there. EOR is contract-driven and only appears when renewals are in play. So working
checklists usually span the six actionable phases: **NSC, EOS, EOE, EOM, EOL, EOSRV**, with EOR
inserted when subscription or service contracts run past EOS.

**Naming the gates you're not using is as useful as naming the ones you are.** A Level 1 checklist
should say "EOE and EOSRV don't apply — nothing to expand, nothing to service."

### The Fifteen Functional Areas

Filtered by level. The parenthetical marks the lowest level where each appears:

| Area | Level |
|---|---|
| Product and Strategy | 1 |
| Engineering and Technical | 1 |
| Support | 1 |
| Documentation and Training | 1 |
| Legal and Contractual | 2 |
| Financial Planning | 2 |
| Sales | 2 |
| Marketing | 2 |
| Customer Success | 2 |
| IT Systems | 2 |
| Data Management | 2 |
| Inventory and Supply Chain | 3 |
| Channel and Partner Management | 3 |
| Regulatory and Compliance | 3 |
| Internal Organizational Alignment | 3 |

### The Sticky-Note Rule

Every item is **4 to 8 words**, names a **verb**, and carries a **named owner** (a function, not a
person's calendar). "Legal reviews contracts" is an item. "Ensure appropriate review of all
relevant contractual obligations across the customer base" is a paragraph wearing a checkbox.

**Why the owner is mandatory:** an unowned item is a wish. Forcing a function onto every line
surfaces cross-functional gaps early — when you can't name who owns "notify channel partners," you
have just discovered that nobody does.

### Phase Gates Are Commitments, Not Dates

A phase gate is what must be **true** before you advance, with an approver. "EOS to EOE: last-time-buy
orders closed — Approver: Sales VP." This is what stops an EOL from being one announcement followed
six months later by somebody quietly pulling a plug.

### Anti-Patterns (what this is NOT)
- **Not a project plan.** No Gantt, no dependencies graph, no resource loading.
- **Not exhaustive by default.** Coverage proportional to risk, not maximum ceremony.
- **Not the decision.** If the sunset itself is still in question, this is premature.
- **Not a substitute for the conversations.** A checklist item saying "align with Legal" is not
  alignment with Legal.

---

## Application

### Step 1: Set the level

Recommend from blast radius — customers, revenue, contracts, hardware, partners — then present all
three and let the user choose. If the level is genuinely unclear, ask:

"How complex is this sunset?
1. **Light** — a feature, internal tool, or unversioned API. Few users, all reachable.
2. **Standard** — a commercial product with paying customers and contracts.
3. **Heavy** — revenue-critical, hardware in the field, channel partners, or regulated.

Most sunsets are Standard. Which sounds like yours?"

### Step 2: Select phases in scope

Map the level to phases, then check for the two overrides:
- **Contracts running past EOS?** Insert EOR.
- **No service obligations at all?** Drop EOSRV and say so.

If a date is genuinely unknown, write `TBD` — and if a date *shouldn't* be set yet (no migration
path exists), write `Not scheduled` and add an item naming the precondition. An invented EOL date
is a promise you will break in public.

### Step 3: Build items per phase, per area

For each phase in scope, walk the functional areas warranted by the level. Each item:
- Starts with a verb
- Is 4 to 8 words
- Names an owning function
- Belongs to exactly one phase — the phase where the work happens, not where it's announced

Cover, at minimum, the four things sunsets most often strand:
1. **Data** — export format, availability window, deletion schedule
2. **Contracts** — renewal language, SLA terms, refunds or credits owed
3. **Access** — API keys, integrations, SSO, downstream systems that read from it
4. **Money** — forecast adjustment, revenue recognition, cost of the sunset itself

### Step 4: Write gate criteria (Level 2+)

For each phase transition, list what must be true and who signs. Three to five criteria per gate is
plenty. If you can't name an approver, the gate isn't real.

### Step 5: Post-EOL actions and assumptions

Always include a short post-EOL block — archival, final report, and a lessons-learned review.
**The review is the item teams cut first and regret most**; the next sunset is always easier when
someone wrote down what surprised you in this one.

Close with assumptions to validate — every unknown from Step 1, stated plainly.

### Final Step: Offer what comes next

"Where next?

1. **Map the stakeholder conversations** — who to talk to, in what order (Recommended)
2. **Draft the customer announcement** — see [`eol-message`](../eol-message/SKILL.md)
3. **Build the internal enablement pack** — support FAQ, sales talking points, objections
4. **Convert this to a dated timeline** — calendar dates against each phase

Reply with a number, a combination ('1 & 3'), or your own path."

---

## Examples

- `examples/sample.md` — Fieldlight Classic Dispatch (SaaS, Level 2, five phases)
- `examples/sample-industrial.md` — NFA-200 controller line (industrial, Level 3, six phases with
  a deliberately undated EOL)

---

## Common Pitfalls

### Pitfall 1: Ceremony Inflation
**Symptom:** Every sunset gets the 15-area, six-phase playbook because it's "more thorough."

**Consequence:** Teams learn EOL process is theater, skip it entirely on the next one — and the
next one is the one with the contracts.

**Fix:** Right-size deliberately. A Level 1 checklist that gets *used* beats a Level 3 that gets
ignored.

---

### Pitfall 2: Unowned Items
**Symptom:** "Ensure customer data is exported." Owner: blank, or "the team."

**Consequence:** Everyone assumes someone else has it. On shutdown day, nobody did.

**Fix:** Every item names a function. If you can't name one, that's the finding — escalate it
rather than papering over it.

---

### Pitfall 3: The Invented Date
**Symptom:** An EOL date gets written down because the checklist template had a blank for it.

**Consequence:** You announce a date, discover the migration path doesn't exist, and move it.
Customers who planned around the first date stop believing the second.

**Fix:** `Not scheduled` is a legitimate entry. Pair it with the precondition that would let you
schedule it.

---

### Pitfall 4: Phase Collapse
**Symptom:** Everything lands in one phase called "EOL."

**Consequence:** You stop sales, stop support, and shut down on the same day. Customers experience
it as an outage with advance notice.

**Fix:** Separate the gates. Stopping sales is cheap and early; stopping service is expensive and
last.

---

### Pitfall 5: Forgetting the Downstream Readers
**Symptom:** The checklist covers the product and its customers, but not the four internal systems
that quietly query its API.

**Consequence:** The product retires on schedule and three dashboards, a billing job, and a partner
integration break the next morning.

**Fix:** The IT Systems and Data Management areas exist for this. At Level 1, still ask once: what
reads from this?

---

## References

### Related Skills

These stand on their own — none is a prerequisite for this skill, and this skill isn't a
prerequisite for them. If you already picked a level elsewhere, just say "Level 2" and this skill
will build to it; there's no handoff artifact to carry.

- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — if the decision itself still needs
  a case, or you want the level recommended for you
- [`eol-stakeholder-sequence`](../eol-stakeholder-sequence/SKILL.md) — who to talk to and when
- [`eol-internal-enablement`](../eol-internal-enablement/SKILL.md) — readying customer-facing teams
- [`eol-message`](../eol-message/SKILL.md) — the customer-facing announcement

### External Frameworks
- Industry EOL lifecycle practice (GA/NSC/EOS/EOE/EOM/EOL/EOSRV)
- RACI — for assigning the owner on each item

### Provenance
- Adapted from `prompts/eol-checklist.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
