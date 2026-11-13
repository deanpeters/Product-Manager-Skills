# Discovery Process Example — Life Sciences

**Brightwater Biologics** is a clinical-stage biotech running multi-site trials. Its internal
product team builds **Trialpath**, the platform study coordinators, CRA monitors, and CRO partners
use to run those studies.

**Why this domain changes discovery:** you cannot run an experiment on patients to test a product
idea. Your users work for someone else — sites are independent organizations with their own
priorities. Access is scarce and scheduled weeks out. And the cost of being wrong isn't churn, it's
a protocol deviation in a regulatory file.

That doesn't make discovery optional. It makes each interview more expensive, which raises the
value of framing the problem properly before you spend one.

---

## Example: Discovery on slow protocol amendment adoption

**Context:** When a study protocol is amended, every participating site must acknowledge it,
retrain staff, and update procedures. Brightwater's data showed a median of 31 days from amendment
release to full site adoption, with a long tail past 60 days. Sites running outdated procedures are
a compliance exposure. The initial hypothesis: *sites aren't reading the notifications.*

---

**Phase 1 — Frame the Problem**

- Ran `problem-framing-canvas`: the assumed problem was "coordinators miss amendment notifications"
- Reframed after looking at the data: **93% of amendments were opened within 48 hours.** Sites were
  reading them. The delay was somewhere after reading
- Revised problem statement: "Coordinators acknowledge amendments quickly but take a median of 31
  days to operationalize them, and we don't know what happens in between"
- **Decision Point 1:** enough context to research? Yes — but the original hypothesis was already
  dead, which was worth knowing before booking a single interview

**Phase 2 — Research Planning**

- Target: study coordinators at 6 sites, spanning fast adopters (under 10 days) and slow ones
  (over 45 days). Sampling the *variance* rather than the average
- Constraint: coordinators are not Brightwater employees. Interviews had to be scheduled through
  site leadership, capped at 30 minutes, and could not ask anything touching patient specifics
- Added two CRA monitors, who see multiple sites and can compare
- Ethics check: no patient data, no protocol content — process questions only

**Phase 3 — Conduct Research**

- 6 coordinator interviews + 2 monitor interviews over three weeks
- The pattern surfaced by interview 3 and held: **acknowledgment is one click; operationalizing
  requires a training session that has to be scheduled around patient visits.** Sites with a
  standing weekly staff meeting adopted in days. Sites without one waited for a gap that kept not
  appearing
- Unprompted from four of six: coordinators didn't know which parts of an amendment actually
  changed. They re-read the whole protocol because the diff wasn't given to them
- **Decision Point 2:** saturation reached at interview 5; interview 6 confirmed and added nothing

**Phase 4 — Synthesize Insights**

- Root cause was **not** attention or tooling adoption. It was that amendments arrive as complete
  replacement documents, so every one triggers a full re-read and a scheduled retraining
- Opportunity 1: show what changed, so a minor amendment stops costing a full retraining slot
- Opportunity 2: let sites schedule retraining from inside the workflow rather than around it
- Opportunity 3 (out of scope, escalated): amendment volume itself — 40% originated from a single
  protocol-authoring team

**Phase 5 — Generate and Validate Solutions**

- **The constraint:** no live experiment. You cannot randomize sites into "sees the diff" and
  "doesn't" when the outcome is regulatory compliance
- So: a **retrospective test.** Took six historical amendments, generated diffs by hand, and asked
  four coordinators to estimate retraining time with and without the diff. Median estimate dropped
  from 45 minutes to 10 for minor amendments
- Then a **paper pilot** at two sites: for the next real amendment, Brightwater's team supplied a
  hand-made diff. Both sites operationalized in under 7 days, against a 31-day baseline
- **Decision Point 3:** validated enough to build. The pilot was two sites and one amendment — small,
  and stated as small

**Phase 6 — Decide and Document**

- Decision: build amendment diffs into Trialpath; defer in-workflow retraining scheduling to a later
  cycle
- Metric: median amendment-to-adoption from 31 days to under 14, measured across all sites over two
  quarters
- Assumptions logged: hand-made diffs matched what automated diffs would produce; two sites may not
  represent the network; the 40% authoring concentration is a separate problem now owned by clinical
  operations

---

## What this example teaches that the SaaS one can't

- **The first hypothesis died in Phase 1, from data the team already had.** "Sites aren't reading
  notifications" was wrong, and one query answered it before any interview was booked. When access
  is expensive, framing pays for itself immediately.
- **Sampling the variance beat sampling the average.** The fast sites explained the slow ones —
  a standing weekly meeting was the whole difference. Interviewing six typical sites would have
  produced six descriptions of being busy.
- **Your users don't work for you.** Interviews routed through site leadership, capped at 30
  minutes, bounded by what could ethically be asked. That shapes the research plan, not just the
  calendar.
- **When you can't experiment, you can still test.** A retrospective estimate and a two-site paper
  pilot are weaker than a randomized trial and far stronger than shipping on conviction. Naming the
  weakness — "two sites, one amendment" — is what keeps the evidence honest.
- **The biggest finding was out of scope, and got escalated rather than absorbed.** 40% of
  amendments coming from one authoring team is a process problem, not a product one. Discovery's job
  was to name it and hand it to the right owner.
