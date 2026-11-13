# Lifecycle & EOL Suite Summary

**8 skills** across two themes, covering what to do with a product that has stopped growing — and
how to retire one without losing the customer.

- **`product-lifecycle`** (2 skills) — the play decision: extend, replace, or retire
- **`eol-transition`** (6 skills) — executing the retirement play

**Governing idea:** *lose the product without losing the customer.*

---

## Which skill do I need?

| If you're... | Start with |
|---|---|
| Not sure the product should change at all | [`lifecycle-play-advisor`](../skills/lifecycle-play-advisor/SKILL.md) |
| Arguing extend vs. rebuild vs. kill | [`lifecycle-play-advisor`](../skills/lifecycle-play-advisor/SKILL.md) |
| Deciding across a whole product line | [`product-lifecycle-plays`](../skills/product-lifecycle-plays/SKILL.md) (portfolio worksheet) |
| Planning a replacement and want the hazards | [`product-lifecycle-plays`](../skills/product-lifecycle-plays/SKILL.md) (risk register) |
| Told to kill something and unsure it's right | [`eol-readiness-advisor`](../skills/eol-readiness-advisor/SKILL.md) |
| Decided, and need the whole process | [`eol-process`](../skills/eol-process/SKILL.md) |
| Wondering who to tell and when | [`eol-stakeholder-sequence`](../skills/eol-stakeholder-sequence/SKILL.md) |
| Needing the operational plan | [`eol-checklist`](../skills/eol-checklist/SKILL.md) |
| Announcing in three weeks with nothing ready | [`eol-internal-enablement`](../skills/eol-internal-enablement/SKILL.md) |
| Just needing to write the announcement | [`eol-message`](../skills/eol-message/SKILL.md) |
| **Mid-sunset and it's going badly** | [`eol-process`](../skills/eol-process/SKILL.md) → "Entering Mid-Stream" |

---

## The suite

### Upstream: the play decision (`product-lifecycle`)

| Skill | Type | What it produces |
|---|---|---|
| [`lifecycle-play-advisor`](../skills/lifecycle-play-advisor/SKILL.md) | Interactive | A recommended play with its reasoning, hazards, and a route out |
| [`product-lifecycle-plays`](../skills/product-lifecycle-plays/SKILL.md) | Component | Stage diagnosis, portfolio worksheet, replacement risk register |

**The three plays:**

- **Extend** — add a variant or capability to the existing line. Cheapest, lowest risk, most often
  skipped because it isn't exciting.
- **Replace** — ship a successor and phase the old one out. **GTM and EOL run simultaneously** for
  two products that compete with each other. The expensive play.
- **Retire** — phase out with no successor of your own. Customers land elsewhere, possibly with a
  competitor.

Plus the answer that isn't a play: **harvest** — stop investing, keep running, set a review date.

### Executing the retirement (`eol-transition`)

| Skill | Type | What it produces |
|---|---|---|
| [`eol-readiness-advisor`](../skills/eol-readiness-advisor/SKILL.md) | Interactive | Verdict + intensity level + obligations to check |
| [`eol-stakeholder-sequence`](../skills/eol-stakeholder-sequence/SKILL.md) | Component | Ordered conversation plan, five fields per stop |
| [`eol-checklist`](../skills/eol-checklist/SKILL.md) | Component | Phase-gated plan, owners, gate criteria |
| [`eol-internal-enablement`](../skills/eol-internal-enablement/SKILL.md) | Component | Support FAQ, sales points, objections, escalation |
| [`eol-message`](../skills/eol-message/SKILL.md) | Component | The customer announcement, sized and pathed |
| [`eol-process`](../skills/eol-process/SKILL.md) | Workflow | The six-phase orchestration |

---

## The six phases

| # | Phase | Question | Skill |
|---|---|---|---|
| 1 | Decide | Should we retire this, and how big is this? | `eol-readiness-advisor` |
| 2 | Align | Who can stop this, and what do they know that we don't? | `eol-stakeholder-sequence` |
| 3 | Plan | What has to happen, when, and who owns it? | `eol-checklist` |
| 4 | Prepare | Are our people ready before customers hear? | `eol-internal-enablement` |
| 5 | Announce | What do customers hear, and when? | `eol-message` |
| 6 | Close | Did we finish, and what did we learn? | `eol-process` |

**Two gates carry most of the value:**

- **DP2 (after Align)** — did anything invalidate the decision? Returning to Phase 1 here is cheap;
  discovering the same thing after Phase 5 is not.
- **DP4 (after Prepare)** — is enablement actually complete? **This gates the announcement.** Test
  it by asking a rep who they'd call about a churn threat.

---

## Two conventions that run through everything

### The right-sizing dial

Every skill offers three levels, recommends one, and lets you override:

| | Level 1 — Light | Level 2 — Standard | Level 3 — Heavy |
|---|---|---|---|
| Scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Elapsed | Days to weeks | 6-12 months | 12-24 months |
| Stakeholder stops | 3-4 | 7-8 | 10+ |
| Lifecycle gates | 2-3 | 4-5 | All 6 |
| Enablement | Support FAQ | + Sales, objections, escalation | + Channel, training |
| Message | Brief notice | Standard with phase table | Full with compliance |

**Level 2 is the default. Never default to Level 3.** Choosing lighter is legitimate — the skills
name what a lighter level leaves uncovered so the choice is informed.

### The lifecycle gates

- **GA** — actively sold and fully supported (a *state*, not a phase of work)
- **NSC** — Notice of Status Change; the decision is communicated
- **EOS** — End of Sale; no new customers can purchase
- **EOE** — End of Expansion; no added capacity or seats
- **EOR** — End of Renewal; contracts will not renew *(contract-driven; include only when needed)*
- **EOM** — End of Maintenance; fixes stop
- **EOL** — End of Life; the product is retired
- **EOSRV** — End of Service; all support and service obligations end

Working checklists usually span **NSC → EOSRV**. Naming the gates you're *not* using is as useful as
naming the ones you are. And `Not scheduled` — paired with the precondition that would let you
schedule it — beats an invented EOL date you'll break in public.

---

## Independence

**Every skill in this suite runs standalone.** None requires another to have run first, and there
is no handoff format between them. Carrying context means saying "Level 2" and pasting what you
have.

`eol-process` recommends a route through them; it does not sequence them mechanically. That's
deliberate — the repo's mandate is that skills teach and stand on their own, not that they chain
into a pipeline you must enter at the top.

---

## Worked examples

Every Component and Workflow skill ships two domains that interlock into continuous stories:

**Fieldlight** (field service SaaS) — retiring Classic Dispatch. Begins as one row in a
four-product portfolio worksheet, runs all six phases, closes at 94% retention against a 90% target
with a review that names what went wrong.

**Northfield Automation** (industrial retrofit controllers) — planning to retire the NFA-200 and
discovering it can't. A risk register that named the right hazard and mis-rated it, a Phase 2 that
broke the plan, and an outcome of End of Sale with **no EOL date** and the retrofit path funded as
the precondition.

---

## Download

The whole suite in one pack:
[`pm-deliver-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-deliver-pack.zip) (the Deliver bundle, which holds the end-of-life skills)

Release note:
[v0.84 — The Lifecycle & End-of-Life Suite](announcements/2026-08-10-v0-84-lifecycle-and-eol-suite.md)
