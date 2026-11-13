---
name: release-readiness
argument-hint: "[what is shipping, to whom, and how reversible it is]"
description: "Check a release is safe to ship: tests, rollout, monitoring, rollback, support. Use when a build is about to go out and you need to know what could hurt, and how you'd undo it."
intent: >-
  A right-sized readiness check for shipping a release (a deploy, a firmware update, a configuration
  change), distinct from the business launch. Confirms what changed, how it's tested, how it rolls
  out, how it's watched, how it is undone, and who is ready to support it, with a go / hold decision
  made on criteria agreed before looking at status. Sized to the blast radius and reversibility.
type: component
theme: pm-artifacts
best_for:
  - "Deciding go or hold on a release with criteria agreed beforehand"
  - "Making rollback, monitoring, and support ready before shipping, not after"
  - "Sizing the check to what a failure would cost and how reversible it is"
  - "Separating the technical release from the business launch"
scenarios:
  - "We ship Thursday. What do we need to confirm before we hit go?"
  - "Release is a pricing-engine change that touches billing. How careful should we be?"
  - "Firmware update to 2,000 field units. What does 'ready' mean?"
  - "Write the go/hold criteria for a low-risk UI change"
estimated_time: "20-30 min"
---

# Release Readiness

## Purpose

Decide whether a release is **safe to ship**, with a check sized to what a failure would cost. The
output is a short readiness record: what is changing, how it was tested, how it rolls out, how it is
watched, how it is undone, who will support it, and a **go / hold** decision made against criteria
the team agreed *before* looking at the status.

The sentence to keep in your head: **before you ship, know how you'd undo it.** A release you can't
reverse needs a higher bar than one you can undo in a minute.

This is the **technical** release check. The **business** launch (sales, support, marketing,
partners) is [`launch-plan`](../launch-plan/SKILL.md). A feature can release quietly many times
before it launches, and a launch can sit on one release.

## Input

**Works best with:** What is shipping, who it reaches, and how reversible it is.

**Also useful:** The test results, the rollout plan, the monitoring in place, the rollback method,
and who is on call or in support.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what's shipping and how bad a failure
would be, picks a level, and builds the check from your answers. Anything unknown becomes a labeled
blank (`[NEEDS SOURCE]`), never an assumed yes.

**Example invocations:**
- `Release: a change to how overage is billed. Reaches all paying accounts. Rollback is a flag.`
- `Firmware 2.1 to 2,000 field units over the air. No physical rollback once flashed.`

---

## Key Concepts

### Right-Size the Check (the Level Dial)

**Not every release needs the same care.** Pick a level, say why in one line, and let the team move it:

| | **Level 1: Light** | **Level 2: Standard** | **Level 3: Heavy** |
|---|---|---|---|
| Typical release | Small, reversible, narrow (copy, minor UI, internal tool) | A normal feature or fix to real customers | Billing, security, data migrations, firmware or hardware in the field, regulated |
| Checks | Tested, rollback known, one owner | + staged rollout, monitoring, support briefed | + formal go/hold, rehearsed rollback, incident owner, comms ready |
| Output feel | A few lines | One-page record | Full record with sign-offs |

**Level 2 is the default. Never default to Level 3.** A heavy ritual for a copy change teaches the
team that readiness is ceremony, and they'll skip it on the day it matters. If they go lighter,
name what is left uncovered.

### Blast Radius and Reversibility Set the Level

Two questions decide: **how many people (or units) does it reach**, and **how fast and cleanly can
it be undone**? A feature flag on 1% of accounts is cheap to reverse. A database migration or an
over-the-air flash with no physical rollback is not. High reach plus hard reversal is Level 3.

### The Seven Checks

1. **What changes.** A plain description, and what does not change (so nobody assumes).
2. **How it was tested.** What was tested, in what environment, and what was *not* tested.
3. **Rollout.** Staged (a small share first, then more) rather than all at once, and the
   criteria for moving to the next stage.
4. **Monitoring.** The signals that say it's working or failing (errors, latency, support volume,
   failure rates), who watches them, and for how long.
5. **Rollback.** The exact way to undo it, how long it takes, and whether it's been tried. "We
   would revert" is not a rollback plan.
6. **Support and communication.** Who is ready to take the calls, what they know, and what customers
   are told if something breaks.
7. **Dependencies and timing.** Other systems or teams affected, and why now (not a Friday afternoon
   or a customer's peak week).

### Go / Hold Criteria Are Agreed First

Decide before the status is known what counts as must-pass (tests green, rollback rehearsed) and
what is watch-only. A go/hold made after looking at a mixed picture gets talked into "go." Hold is a
legitimate and cheap outcome compared to a bad release.

### Not Only Software

For firmware, hardware, or service changes the same seven checks apply, with physical specifics:
which units, which firmware versions, whether a field rollback exists, whether certification is
affected, and who handles units that fail mid-update.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not the business launch.** See [`launch-plan`](../launch-plan/SKILL.md).
- **Not a code review or QA plan.** It checks that testing and rollback exist, not how to test.
- **Not a gate the PM owns.** The release owner decides; this skill makes the criteria visible.
- **Not heavy by default.** Light is a legitimate level.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the level and why, the seven checks, the go/hold criteria
and result, and the open items. Commentary short, after. Every unconfirmed check is `[NEEDS SOURCE]`
or "not confirmed", never assumed done.

**If the PM brings a plan, critique first.** Is the level justified by reach and reversibility? Is
there a rollback that has been tried? Is monitoring tied to named signals and a watcher? Is
rollout staged with criteria? Were go/hold criteria written before the status? Name gaps; offer
rewrites last.

### Step 1: Describe the Release
What changes, what doesn't, who or what it reaches, and how reversible it is.

### Step 2: Set the Level
Recommend Light, Standard, or Heavy from reach and reversibility; say why; honor an override and
name what a lighter level leaves uncovered.

### Step 3: Walk the Seven Checks
For each, record the state and mark anything unconfirmed. Press on rollback: has it been tried?

### Step 4: Set Go / Hold Criteria
Must-pass and watch, with thresholds, agreed before reading the status.

### Step 5: Decide and Hand Back
State go, hold, or go with conditions, and the open items with owners. Short summary (supplied,
inferred, unknown), then a numbered ladder, evidence-favored first, labeled `(Recommended)`: hold
until the rollback is rehearsed; ship to a small share first; ship as planned with a named watcher
for 48 hours; or reschedule off the peak window.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight billing change, SaaS, Level 3) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield firmware update,
industrial, Level 3, ending in a hold).

---

## Common Pitfalls

### Pitfall 1: "We'd Just Revert"
**Symptom:** Rollback is an intention.
**Consequence:** The first time it's tried is during the incident.
**Fix:** Name the method, the time it takes, and whether it was rehearsed.

### Pitfall 2: Everything at Once
**Symptom:** A full rollout on day one.
**Consequence:** Any defect reaches every customer.
**Fix:** Stage it with criteria for moving on.

### Pitfall 3: Nobody Watching
**Symptom:** Monitoring exists; no one is assigned.
**Consequence:** Failure is found by customers.
**Fix:** Name the signals, the watcher, and the duration.

### Pitfall 4: Criteria Written After the Status
**Symptom:** "It's mostly green, let's go."
**Consequence:** Real risks are rationalized.
**Fix:** Agree must-pass and watch criteria first.

### Pitfall 5: Heavy by Default
**Symptom:** A copy change gets a full sign-off.
**Consequence:** The team learns to skip the process.
**Fix:** Size to reach and reversibility.

### Pitfall 6: Releasing at the Worst Time
**Symptom:** A Friday afternoon or a customer's peak week.
**Consequence:** Slow response when it matters.
**Fix:** Name why now, and choose a window when people can respond.

---

## References

### Skill Files
- [`template.md`](template.md): the seven checks, go/hold criteria, and open items
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`launch-plan`](../launch-plan/SKILL.md): the business launch around a release
- [`sprint-planning`](../sprint-planning/SKILL.md): upstream; what was committed
- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md): the same go/no-go discipline at the end of life
- [`launch-metrics`](../launch-metrics/SKILL.md): what to watch after launch
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Staged rollouts, feature flags, and rollback:** standard release-engineering practice.
- **Production readiness reviews:** common site-reliability practice (for example *Site Reliability Engineering*, Google).

### Provenance
Distilled from practitioner experience preparing product releases for software and connected hardware.
