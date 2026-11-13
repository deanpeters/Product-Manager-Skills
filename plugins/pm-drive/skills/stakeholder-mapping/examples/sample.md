# Stakeholder Mapping Example — SaaS

**Initiative:** Fieldlight's customer-facing arrival windows in Next Scheduling — technician ETAs
become visible to the end customer.

Continues from the `stakeholder-identification` SaaS example, which surfaced field technicians as a
priority stakeholder.

---

## Grid 1: Power × Interest

| | **High Interest** | **Low Interest** |
|---|---|---|
| **High Power** | **Manage closely**<br>· Service business owners (the buyer)<br>· Fieldlight CPO | **Keep satisfied**<br>· Legal<br>· Fieldlight CFO |
| **Low Power** | **Keep informed**<br>· Dispatchers<br>· Fieldlight support<br>· CS | **Monitor**<br>· Field technicians<br>· End customers<br>· Notification vendor |

Read alone, this grid says: co-design with business owners, brief Legal, keep dispatchers in the
loop, and largely ignore technicians and end customers.

---

## Grid 2: Impact × Power

| | **High Power** | **Low Power** |
|---|---|---|
| **High Impact** | **Q2**<br>· Service business owners<br>· Dispatchers | **Q1 — elevate deliberately**<br>· **Field technicians**<br>· **End customers** |
| **Low Impact** | **Q4**<br>· Fieldlight CFO<br>· Legal | **Q3**<br>· Notification vendor |

---

## The comparison

| Stakeholder | Power×Interest | Impact×Power | Tension |
|---|---|---|---|
| **Field technicians** | Monitor | **Q1** | Their location becomes visible to a third party. They have no power, low expressed interest — because nobody has told them |
| End customers | Monitor | **Q1** | The feature exists for them; they have no voice in its design |
| Legal | Keep satisfied | Q4 | High power, low impact — a gate, not a participant |
| Dispatchers | Keep informed | Q2 | Higher stakes than grid 1 implies — they field the calls when a window is missed |

**Q1 voices to elevate:**
- **Field technicians** — six interviews across three accounts, conducted without their employer in
  the room. Employer-present interviews on a surveillance-adjacent feature produce agreement, not
  information.
- **End customers** — five interviews recruited through two accounts, asking what window precision
  they'd actually use versus what they'd say they want.

**The mismatch that matters most:** field technicians. Grid 1 says *Monitor.* Grid 2 says
**Q1 — the most affected, least powerful group in the initiative.** Acting on grid 1 alone would
have shipped a location-visibility feature without ever speaking to the people whose location it
makes visible.

---

## Engagement plan

| Stakeholder | Quadrant | Engagement | Cadence | Owner |
|---|---|---|---|---|
| Field technicians | Q1 | Research interviews, then a design review with 3 techs | Twice pre-launch | PM |
| End customers | Q1 | Concept test on window precision | Once pre-launch | Researcher |
| Service business owners | Q2 / Manage closely | Co-design, beta cohort | Biweekly | PM |
| Dispatchers | Q2 | Workflow walkthrough | Monthly | PM |
| Legal | Q4 / Keep satisfied | Disclosure and consent review | At spec and at launch | PM |
| Notification vendor | Q3 | SLA confirmation | Once | Eng lead |

---

## Quadrant migration

| Stakeholder | From | To | Why | How |
|---|---|---|---|---|
| Field technicians | Monitor (P×I) | Keep informed → consulted | They can kill adoption by escalating to their employer; consulting early converts a likely objection into design input | Two design reviews, plus naming their input in launch comms so the change is visible to them |

---

## What to notice

- **The two grids disagreed about the most important stakeholder.** That disagreement is the entire
  reason to run both. One grid would have produced a confident, wrong plan.
- **Low interest was a symptom, not a preference.** Technicians showed low interest because nobody
  had told them. Treating low interest as informed disinterest is how Q1 stakeholders stay invisible
  until launch.
- **The Q1 elevation method is specific and slightly awkward.** "Without their employer in the room"
  is the detail that makes the research worth doing.
- **Legal sits in Q4 and that's correct.** High power, low impact — a gate to satisfy, not a
  participant to co-design with. Not every powerful stakeholder needs deep engagement.
- **The migration names a mechanism.** Two design reviews plus visible credit in launch comms, not
  "build a relationship."
