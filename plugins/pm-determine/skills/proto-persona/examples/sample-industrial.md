# Proto-Persona Examples — Industrial

Proto-personas built during NFA-500 discovery at Northfield Automation, before any formal research
had been funded.

The industrial twist: **the user, the buyer, and the specifier are three different people**, and
they often disagree. A single persona covering "the customer" hides the disagreement that decides
whether you win.

---

## Example 1: "Second-Shift Sam" (Good Proto-Persona — the user)

```markdown
### Name
- Second-Shift Sam

### Bio & Demographics
- 38-52, works at a parts manufacturer in a small city; often 15+ years at the same plant
- Maintenance technician, second shift; on call for nights and weekends
- Trade school or apprenticeship background; strong mechanical and electrical skills
- Learned the controls side on the job, from manuals and whoever came before
- Does not carry a laptop onto the floor. Has a phone with a cracked screen and gloves on

### Needs & Goals
- Get a stopped line running again without making the fault worse
- Know which part failed before touching anything
- Avoid calling the OEM, which means admitting he couldn't fix it
- Finish the shift without a callback at 2am

### Frustrations & Pain Points
- A single fault light that means seventeen possible things
- Diagnostics that require software he doesn't have on a machine he can't bring to the panel
- Vendors who assume network connectivity on a floor with none
- Being blamed for downtime he diagnosed correctly and quickly

### Behaviors & Habits
- Keeps a personal notebook of fault codes and what they actually meant
- Asks the plant's most experienced tech before he asks the manual
- Trusts equipment he has personally taken apart
- Will work around a tool that slows him down, permanently, without telling anyone

### Assumptions to Validate
- ASSUMPTION: he wants slot-level fault detail on the unit, not on a screen elsewhere
- ASSUMPTION: no connectivity at the panel in most plants — needs confirming per site
- ASSUMPTION: the personal notebook is common, not just one tech's habit
- ASSUMPTION: he has real influence on repurchase through the "what do you want to work on"
  conversation with his manager
```

**Why this works:**
- **The assumptions are labeled and falsifiable.** "No connectivity at the panel" is checkable in
  one site visit, and the whole diagnostics design hinges on it.
- **"Gloves on. Cracked screen."** Two details that kill a touchscreen-first concept before it's
  drawn.
- **The behavior section predicts failure modes.** "Will work around a tool that slows him down,
  permanently, without telling anyone" is the most important line — it explains why usage data
  would look fine while adoption quietly died.
- **The last assumption is about influence, not usage.** Sam doesn't sign the PO, but he answers
  when the manager asks what to buy. That's a research question worth its own interview.

---

## Example 2: "Spec-Sheet Priya" (Good Proto-Persona — the specifier)

```markdown
### Name
- Spec-Sheet Priya

### Bio & Demographics
- 29-40, controls engineer at a systems integrator that bids retrofit projects
- Engineering degree; fluent in ladder logic and three vendors' toolchains
- Specifies the controller, commissions it, and never sees it again
- Judged on projects delivered on time and on bid

### Needs & Goals
- Specify a controller she can commission predictably, with no surprises on site
- Reuse configuration across jobs instead of rebuilding each time
- Avoid the vendor call that starts "it worked in the shop"

### Frustrations & Pain Points
- Documentation that describes the happy path and nothing else
- Toolchains that require a specific old Windows version
- Discovering at commissioning that a feature works differently than the datasheet implied
- Carrying spares and training for three controller families because no one family covers her range

### Behaviors & Habits
- Reads the manual before the sales deck; distrusts anything not in the manual
- Builds a personal library of working configurations
- Will standardize on one vendor if the range covers her jobs — and then defends that choice

### Assumptions to Validate
- ASSUMPTION: range coverage matters more to her than any individual feature
- ASSUMPTION: she has veto power on the controller choice, not just input
- ASSUMPTION: commissioning time is the metric she'd trade other things for
```

---

## Why two personas, not one

Sam and Priya want different things from the same box.

Sam wants **fault detail at the panel, with gloves on, offline.** Priya wants **range coverage and
predictable commissioning.** Neither is wrong; neither is the buyer.

A single "industrial customer" persona would have averaged them into someone who wants "reliability
and ease of use" — a description that fits every product ever made and guides no decision. The
disagreement between the two is the useful part: it tells you the roadmap needs both an on-unit
diagnostic story *and* a platform-range story, and that pitching one to the other's audience will
fall flat.

**What makes these proto- rather than real personas:** every assumption is labeled, and none has
been tested yet. Their job is to make the team's guesses explicit and arguable, then get replaced
by evidence — not to be defended once someone gets attached to Sam.
