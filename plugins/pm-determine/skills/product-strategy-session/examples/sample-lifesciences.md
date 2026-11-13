# Product Strategy Session Example — Life Sciences

**Brightwater Biologics** runs multi-site clinical trials. Its internal product team built
**Trialpath**, the platform its coordinators, monitors, and CRO partners use to run those studies.

**The strategy question:** two CRO partners have asked to license Trialpath for studies that have
nothing to do with Brightwater. Should an internal tool become a product?

**Why this domain changes strategy work:** revenue arrives years after the evidence that justifies
it, the buyer is rarely the user, and the option you're comparing against isn't a competitor — it's
"keep spending that engineering capacity on the therapy program that is the actual company."

---

## Example: Should Trialpath become a product?

---

**Phase 1 — Positioning**

- Ran `positioning-workshop`. First attempt targeted "clinical trial sponsors," which collapsed
  immediately — a 40-person biotech and a global CRO buy nothing alike
- Segmented to three candidates: small sponsors without a platform, CROs running studies for
  others, and large sponsors already on incumbent systems
- Third segment eliminated in the session: displacing an incumbent validated system means the
  customer re-validates everything. Nobody does that for a feature advantage
- Proto-personas built for the two survivors: **"First-Study Farrah"** (ops lead at a small sponsor
  running her first multi-site trial) and **"Margin-Watch Marcus"** (CRO operations director whose
  economics are staffing ratios)
- JTBD split sharply. Farrah: *"help me run a compliant study without hiring a systems team."*
  Marcus: *"help me run more studies per coordinator."*
- Draft positioning, small-sponsor segment: *For clinical-stage sponsors running their first
  multi-site studies, who need a compliant trial platform without an internal systems team,
  Trialpath is a trial operations platform that ships preconfigured to the workflows a study
  actually runs on — unlike enterprise systems that assume a validation team you don't have.*

**Phase 2 — Problem Framing**

- Ran `problem-framing-canvas` on the internal question, not the customer's
- **Look inward:** Trialpath is built for Brightwater's protocols. Two CROs asking is not a market.
  Every hour on it is an hour off the therapy program
- **Look outward:** small sponsors genuinely lack good options, and the incumbents price for
  enterprise. The pull is real
- **Reframe:** the question isn't "is there demand." It's *"can we serve it without taxing the
  program that is the actual company?"*
- Named the strategic risk plainly: Brightwater is a biotech. A software line competes for the same
  scarce engineering, and its revenue arrives on a slower clock than the trials it would fund

**Phase 3 — Discovery**

- Six interviews: 4 small-sponsor ops leads, 2 CRO directors
- Small sponsors confirmed the pain and revealed the blocker: **they need a validated system**, and
  validation documentation was the first question in every conversation. Brightwater had validated
  Trialpath *for its own use* — not as a vendor-supplied system
- CROs wanted the opposite: deep configurability per client, which is a services business wearing a
  software costume
- Killed the CRO segment. Marcus's job needs staffing leverage; that's consulting, not licensing
- Sized it honestly: roughly 300 addressable small sponsors, realistic reach far lower. **Not a
  business that changes Brightwater's trajectory.** Possibly one that funds a team

**Phase 4 — Roadmap and Decision**

- Ran `roadmap-planning` against a deliberately narrow bet
- **Decision: a limited pilot, not a product line.** License to three small sponsors at cost, for
  eighteen months, with a named exit
- Sequenced: vendor-grade validation documentation → multi-tenant isolation → configuration for
  non-Brightwater protocols. The first item is the gate; the other two don't matter if it fails
- **The kill criterion, written before starting:** if vendor-grade validation documentation takes
  more than two engineer-quarters, stop. That is the cost that would begin taxing the therapy
  program
- Explicit non-goals: no CRO segment, no incumbent displacement, no sales hires
- Review at 18 months against one question — *did this fund itself without slowing a trial?*

---

## What this example teaches that the SaaS one can't

- **The strategy question was internal, not competitive.** The real alternative wasn't a rival
  platform; it was spending the same engineers on the drug. Phase 2 named that instead of assuming
  growth is always good.
- **A segment died on regulatory mechanics, not on demand.** Large sponsors want it and will never
  buy, because switching means re-validating. Constraints, not preferences, eliminated that segment
  in one session.
- **Validation documentation was the whole gate.** Every small-sponsor interview opened with it, and
  it became the first roadmap item and the kill criterion. In a regulated market the compliance
  artifact often *is* the product decision.
- **A segment was killed for being services in disguise.** CRO configurability sounds like product
  demand and behaves like consulting revenue. Naming it early avoided years of building bespoke
  configuration for two accounts.
- **The honest sizing was "this doesn't change our trajectory."** ~300 addressable sponsors. That
  didn't stop the bet — it right-sized it into an eighteen-month pilot with a written exit, rather
  than a product line with a hiring plan.
