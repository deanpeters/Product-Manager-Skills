# PoL Probe Examples — Industrial

Proof-of-Life probes from **Northfield Automation** during NFA-500 development.

**The industrial twist:** you can't ship a fake door to a plant floor. There's no feature flag, no
5% rollout, no "we'll revert if it goes badly." That makes cheap physical probes *more* valuable —
because the real experiment costs a tooling cycle and takes a year.

---

## ✅ Good: Task-Focused PoL Probe

**Hypothesis:** "A technician can identify which I/O slot faulted from the front panel in under 30
seconds, wearing work gloves, in plant lighting."

**Probe:** A printed card mounted at panel height showing the proposed front-panel layout. Nine
technicians at three sites were given a simulated fault ("slot 4 has failed — show me how you'd
know") and timed.

**Cost:** Two days, a color printer, and site visits already scheduled for other work.

**What we learned:**
- 7 of 9 identified the slot in under 20 seconds. Two took over a minute — both at the site with
  the dimmest panel lighting
- All nine reached for the card with a gloved hand and none attempted a precise touch
- Four asked "does it tell me *what* failed or just *where*?" — a question nobody on the team had
  thought to answer

**What changed:** The touchscreen concept was dropped. Indicator height increased for low-light
legibility. A fault-type code was added beside the slot number, from a question we hadn't known to
ask.

**Why this is a good probe:**
- **It tested the riskiest assumption** — legibility under real conditions — not the easiest one
- **It cost nothing and could fail cheaply.** Two of nine failing was a finding, not a setback
- **It ran where the work happens.** The same card tested in an office would have passed easily and
  taught nothing
- **It surfaced an unknown unknown.** The "what failed, not just where" question came from putting a
  real artifact in front of a real user

---

## ✅ Good: Feasibility PoL Probe

**Hypothesis:** "Module failures show a detectable precursor signal in I/O data before they fail."

**Probe:** Pulled signal logs preceding 50 known module failures from the service database. One
engineer, one week, no new code.

**What we learned:** Precursor patterns appeared in **9 of 50**.

**What changed:** The predictive-maintenance epic was killed after three weeks and roughly zero
engineering cost.

**Why this is a good probe:** it used data that already existed to answer a question that would
otherwise have consumed two quarters. In a domain where a false "your line is about to stop" alert
destroys trust faster than no alert at all, being wrong 80% of the time was disqualifying — and the
probe found that out before anyone wrote firmware.

---

## ❌ Bad: The Probe That Couldn't Fail

**Hypothesis:** "Customers want better diagnostics."

**Probe:** Showed twelve customers a slide deck of the proposed NFA-500 diagnostics and asked
whether they'd find it valuable.

**Result:** Twelve of twelve said yes.

**Why this is a bad probe:**
- **Nobody says no to "would you like a better version of a thing you complain about."** The result
  was determined before the probe ran
- **It tested enthusiasm, not behavior.** A tech saying "that'd be great" in a conference room tells
  you nothing about whether they can read it at panel height with gloves on
- **It had no failure condition.** A probe that cannot come back negative isn't a probe, it's a
  presentation
- **It confirmed a decision already made**, which is the most expensive form of research — it buys
  false confidence at the price of real learning

**The fix:** the printed-card probe above. Same question, four days, and two of nine failed — which
is exactly what made it worth running.

---

## What hardware changes about probing

| | Software | Hardware / industrial |
|---|---|---|
| Cheapest real test | Ship to 5% and measure | Paper, cardboard, or existing data |
| Failure cost | Revert the flag | Tooling cycle, possibly a year |
| Where to test | Wherever users are | **Where the work physically happens** |
| Riskiest assumption | Usually demand | Often physical: legibility, reach, environment |

The discipline is identical; the artifacts are cheaper and more physical, and the site visit is
non-negotiable. A probe run in an office tests an office.
