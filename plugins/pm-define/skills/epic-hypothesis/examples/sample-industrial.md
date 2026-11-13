# Epic Hypothesis Examples — Industrial

Epics framed as testable bets during NFA-500 development at Northfield Automation.

The industrial twist: you cannot A/B test a control panel, and the feedback loop is measured in
quarters, not days. That makes the hypothesis discipline *more* valuable, not less — the discovery
experiments have to be cheap and physical, because the real experiment is expensive and slow.

---

## Example 1: Good Epic Hypothesis

```markdown
### Epic Hypothesis: On-Unit Fault Isolation for the NFA-500

#### If/Then Hypothesis

**If we** display fault information down to the individual I/O slot on the controller's front
panel, readable without a laptop or network connection
**for** maintenance technicians diagnosing a stopped line at the panel
**Then we will** reduce median time-from-stop-to-first-corrective-action from 52 minutes to under
15 minutes across pilot sites

#### Tiny Acts of Discovery Experiments

1. **Notebook audit** (1 week, ~0 cost) — collect the personal fault-code notebooks technicians
   keep. If most techs maintain one, the information gap is real and we can see exactly which codes
   matter. If few do, our premise is wrong.
2. **Paper-panel test** (2 weeks) — mock the front panel on printed card at three pilot sites. Give
   techs a simulated fault and time how long to correct diagnosis. No hardware required.
3. **Glove-and-lighting check** (3 days) — verify legibility at panel height, in plant lighting,
   with work gloves on. Kills or confirms the touchscreen option before tooling.
4. **Downtime attribution pull** (2 weeks) — get three plants to split logged downtime into
   diagnosis versus repair. Establishes the 52-minute baseline, which we currently believe but have
   not measured.

#### Success Metrics

- **Primary:** median stop-to-first-corrective-action under 15 min at pilot sites (baseline 52)
- **Secondary:** controller swaps per 100 faults drops below 10 (baseline 34) — techs stop
  replacing the whole unit when they can see which module failed
- **Guardrail:** no increase in incorrect module replacements. Faster wrong answers are worse than
  slower right ones.

#### Kill Criteria

- If the notebook audit shows fewer than a third of techs track codes themselves, the information
  gap isn't what we think — stop and re-frame
- If the paper-panel test doesn't beat 25 minutes, the panel UI isn't the lever; the constraint is
  somewhere else
- If guardrail rises above baseline, stop regardless of the primary metric
```

**Why this works:**
- **The baseline is named as unmeasured.** "52 minutes" appears in the hypothesis and experiment 4
  exists to verify it. Stating a number you haven't confirmed, and then confirming it, is honest
  sequencing.
- **The experiments are physical and cheap.** Printed card and a stopwatch. No firmware, no tooling,
  no capital — which is the only way to run discovery on hardware timelines.
- **Experiment 3 can kill a design in three days.** Gloves and plant lighting versus a touchscreen
  is a five-minute question that saves a tooling cycle.
- **The guardrail names the real risk.** Faster diagnosis that's wrong more often is a worse product
  — and it's exactly what "make the fault light more informative" could produce if done carelessly.
- **Kill criteria are pre-committed.** Written before the team fell in love with the panel design.

---

## Example 2: Bad Epic Hypothesis

```markdown
### Epic: Improve NFA-500 Diagnostics

**Goal:** Deliver best-in-class diagnostics for the NFA-500 platform to improve customer
satisfaction and differentiate from competitors.

**Success:** Positive customer feedback, improved NPS, competitive win rate.

**Approach:** Work with engineering to scope and deliver enhanced diagnostic capabilities in H2.
```

**What breaks:**
- **Nothing here can be wrong.** "Improve diagnostics" has no condition under which the team would
  stop, change course, or admit the premise failed. That's the definition of an untestable epic.
- **No user.** Technician, controls engineer, and operations manager need different diagnostics.
  The epic doesn't say which, so engineering will pick — probably the one easiest to build.
- **"Positive customer feedback" and "improved NPS"** are lagging by quarters in this market and
  confounded by everything else in the release. Neither can steer a decision mid-build.
- **No baseline**, so "improved" is unmeasurable even after the fact.
- **"Best-in-class"** invites scope with no ceiling. Compare to "under 15 minutes," which tells you
  precisely when to stop building.

---

## Example 3: Good Epic Hypothesis (a bet that got killed)

Worth showing, because a killed epic is the discipline paying off.

```markdown
### Epic Hypothesis: Predictive Failure Alerts

**If we** analyze I/O signal patterns to predict module failures before they occur
**for** plant operations managers planning maintenance windows
**Then we will** convert at least 30% of unplanned line stops into planned maintenance at pilot sites

#### Tiny Acts of Discovery Experiments

1. **Historical data pull** (3 weeks) — collect signal logs preceding 50 known module failures.
   Do failures show a detectable precursor pattern at all?
2. **Blind classification** (1 week) — have an engineer attempt to identify pre-failure windows
   from logs without knowing the outcomes.

#### Kill Criteria
- If fewer than half of failures show any precursor signal, prediction isn't feasible with the
  data we have — stop.
```

**Outcome:** Experiment 1 found precursor patterns in **9 of 50** failures. The epic was killed
after three weeks and roughly zero engineering cost.

**Why this is a success:** the alternative was a two-quarter build landing on a feature that would
have been wrong 80% of the time — in a domain where a false "your line is about to stop" alert
destroys trust faster than no alert at all. The hypothesis format is what made the cheap test
obvious and the kill decision uncontroversial.
