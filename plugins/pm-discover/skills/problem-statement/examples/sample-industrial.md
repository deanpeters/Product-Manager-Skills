# Problem Statement Examples — Industrial

Northfield Automation builds retrofit control systems for legacy production lines. These statements
were written during NFA-500 discovery.

The industrial twist: the person who feels the pain is rarely the person who signs. A problem
statement written from the buyer's chair produces a cost-reduction pitch; written from the
technician's chair it produces something a team can actually design against.

---

## Example 1: Good Problem Statement (NFA-500 discovery)

**Problem Framing Narrative:**

**I am:** A maintenance technician at a mid-sized parts manufacturer
- Responsible for keeping four production lines running across two buildings
- On call nights and weekends; I am the person who gets phoned at 2am
- Comfortable with wiring and mechanics, less so with software and network configuration

**Trying to:**
- Get a stopped line running again as fast as possible, without making it worse
- Know whether the fault is the controller, a sensor, the wiring, or the machine itself

**But:**
- The controller shows a single fault light with no indication of which input tripped
- Diagnosing means pulling the panel and testing points one at a time with a meter
- If I guess wrong and swap the controller, I lose two hours re-commissioning it

**Because:**
- The controller was designed when a fault light was the state of the art
- Diagnostic information exists inside the device but was never surfaced anywhere a person can see
- Nobody who designed it has ever stood at a panel at 2am with production waiting

**Which makes me feel:**
- Anxious — every minute of guessing is a minute the line isn't producing
- Undermined — I am good at this job and the tool makes me look slow
- Resentful of the "upgrade" that made diagnosis harder than the machine it replaced

---

**Why this works:**
- **The "because" names a design failure, not a user failure.** "Nobody who designed it has stood
  at a panel at 2am" is the whole insight, and it points directly at what to change.
- **The feeling is specific and true to the role.** "Undermined" is the one that matters — a tool
  that makes a competent person look slow gets worked around, then blamed.
- **It doesn't smuggle in a solution.** No mention of a display, an app, or an LED. The team stays
  free to solve it.
- **It gives you a testable success condition** without stating one: the tech knows which input
  tripped without pulling the panel.

---

## Example 2: Bad Problem Statement (same situation)

**Problem Framing Narrative:**

**I am:** A plant operations manager

**Trying to:**
- Reduce unplanned downtime costs

**But:**
- Our controllers lack modern diagnostics

**Because:**
- The technology is outdated

**Which makes me feel:**
- Frustrated

---

**What breaks:**
- **Wrong person.** The operations manager experiences downtime as a number on a report. The
  technician experiences it as a 2am phone call and a meter in their hand. Only one of those
  produces design insight.
- **"Lack modern diagnostics" is a solution wearing a problem's clothes.** It names an absent
  feature rather than a blocked job, so the team builds "diagnostics" without knowing what question
  the tech is actually trying to answer.
- **"The technology is outdated" explains nothing.** Outdated how? The mechanical design is fine.
  It's the information design that fails.
- **"Frustrated"** is the default emotion nobody learns anything from.
- The whole thing could describe any industrial product from the last forty years — which means it
  describes none of them well enough to act on.

---

## Example 3: Good Problem Statement (the buyer's problem, stated honestly)

The operations manager *does* have a real problem — it's just a different one, and worth writing
separately rather than blending in.

**I am:** A plant operations manager responsible for output on four lines

**Trying to:**
- Commit to delivery dates I can actually hit
- Decide whether to fund a controls refresh this year or defer it again

**But:**
- I can't tell whether our downtime is a controls problem, a maintenance-staffing problem, or a
  machine-age problem
- Every vendor tells me their box will fix it, and I have no way to check

**Because:**
- Downtime is logged as a duration and a line number, with no fault-level detail
- The people who know what actually happened fix it and move on — the knowledge never reaches a
  system

**Which makes me feel:**
- Exposed — I'm defending a capital request with anecdotes
- Skeptical of vendors, including the ones telling the truth

---

**Why keeping these separate matters:**
Blending them produces a mushy statement serving neither. Separated, they point at two different
things to build — fault-level diagnostics on the unit for the technician, and downtime
attribution the manager can take to a budget meeting. The second is what actually sells the first.
