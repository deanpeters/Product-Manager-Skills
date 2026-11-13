# Altitude & Horizon Example — Hardware Org

The `sample.md` example follows a Director in a SaaS company. This one follows the same transition
in a **hardware organization** — Northfield Automation, which builds retrofit control systems.

**Why the org shape matters more than the industry:** altitude and horizon are shaped by how far
ahead your organization is forced to think. In SaaS a Director's horizon is quarterly because
releases are continuous. In hardware, tooling lead times and certification windows push the
planning horizon out to eighteen months *whether or not the Director is ready for it* — and the
most common failure is a newly promoted Director still operating on a release-cycle horizon.

---

## Example 1: Cascading Context Map in a hardware org

### Scenario

Priya was promoted from PM to Director of Product at Northfield six months ago. Company leadership
has stated a priority: *"Consolidate onto one control platform by 2028."* Her three teams — platform
firmware, I/O modules, and service tooling — have been asking what that means for their work.
Nobody above her has translated it.

### Completed Context Cascade

```markdown
## Context Cascade: Control Platform Group — FY2027

**Company Priority:** "Consolidate onto one control platform by 2028."

**Business Unit Translation:** Controls BU stops investing in NFA-200 capability and
moves the installed base to NFA-500 without losing service revenue during the wind-down.

**Product Portfolio Translation:** NFA-500 must cover the full range the NFA-200 covered —
including the high-channel-count jobs it currently can't — before we can stop selling
the 200.

**Team Accountabilities:**
- Platform firmware: remote update and fault isolation, so a growing installed base is
  serviceable without a growing field team
- I/O modules: close the high-channel-count gap. This is the gate on End of Sale.
- Service tooling: migration and commissioning tooling so integrators can move without
  re-learning everything

**Why this matters:** the End of Sale date is not ours to move — manufacturing needs the
line. What IS ours is whether customers have somewhere to land when it happens.

**What I'm still unsure about:** whether "one platform by 2028" includes the SmartLink
gateway or only controllers. I've asked; I don't have an answer. Planning as if it's
controllers only, and I'll say so if that changes.
```

### Why this is strong

- **It translates a slogan into three team accountabilities**, each traceable to the company line.
- **It names the gate.** "This is the gate on End of Sale" tells the I/O module team their work
  paces everyone else's — the single most useful sentence for a team that would otherwise optimize
  locally.
- **It names what's fixed and what's theirs.** The EOS date is immovable; the landing place is
  theirs. That's the difference between a team feeling steamrolled and a team feeling accountable.
- **The unresolved question is stated, with a working assumption.** Priya didn't wait for clarity
  and didn't manufacture it. Both are Director behaviors; waiting is the PM habit.
- **It fits on one page** for a group spanning three teams and an eighteen-month horizon.

---

## Example 2: Anti-Pattern — the horizon that didn't move

### Scenario

Six weeks earlier, Priya's I/O module team hit a supplier problem on a component for the
high-channel-count module. Her instinct — a good PM instinct — was to dig in: get on calls with the
supplier, evaluate substitutes, rebuild the schedule.

### Director response (weak)

She spent three weeks largely inside that problem. She was effective; the substitute part was
found and the schedule was rebuilt.

**What it cost:** during those three weeks, the tooling decision for the module housing went
unmade. The tooling vendor's August slot was given to another customer. The module — the gate on
End of Sale — slipped a full quarter, which pushed the EOS date the company had already committed
to manufacturing.

### What the framework says

- **Altitude:** she operated at feature/team level on a component sourcing problem her senior PM
  could have run with support
- **Horizon:** she spent a sprint-shaped three weeks while the decision that mattered lived on a
  14-week lead time. **The horizon failure is the expensive one.** In SaaS, three weeks of Director
  attention in the weeds costs three weeks. Here it cost a year, because the thing she wasn't
  watching had a lead time.
- **Hero Syndrome trigger:** a hard, concrete, solvable problem — exactly the kind that feels like
  contribution — appearing while the important decision was ambiguous and slow.

### Stronger response

Assign the supplier problem to the senior PM with a clear escalation trigger. Spend her own time on
the tooling decision, because it is the one with an external clock she can't restart and no one
below her has the authority to make.

---

## What this example teaches that the SaaS one can't

- **Horizon is set by your supply chain, not your calendar.** A Director's planning horizon in
  hardware is defined by the longest external lead time in the portfolio, and it doesn't wait for
  the Director to grow into it.
- **Hero Syndrome is more expensive when lead times are long.** The same three weeks of misplaced
  attention costs three weeks in SaaS and a year here.
- **"What's fixed vs. what's ours" is the most valuable line in the cascade.** When a date is
  genuinely immovable, saying so — and naming what the team *does* control — is what keeps a team
  accountable rather than resentful.
