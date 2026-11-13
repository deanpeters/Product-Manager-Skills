# User Story Map Example — Industrial

A story map for **Northfield Automation's** NFA-500 commissioning experience — the work a systems
integrator does to get a controller installed, configured, and running on a customer's line.

**The industrial twist:** the backbone spans days and sites, not minutes and screens. Some steps
happen in a shop, some in a plant, and some at 2am. And release slices are constrained by physical
delivery — you can't ship half a controller.

---

```markdown
## User Story Map: NFA-500 Commissioning

### Backbone (integrator's workflow, left to right)

Specify  ->  Configure in shop  ->  Install on site  ->  Commission  ->  Hand off  ->  Support

### Walking Skeleton (release 1 — the thinnest path that works end to end)

| Specify | Configure | Install | Commission | Hand off | Support |
|---|---|---|---|---|---|
| Select I/O modules for channel count | Build config on a laptop | Mount in panel with standard kit | Verify each I/O point | Print point list for plant | Read fault codes at panel |

### Release 2 — reduce rework

| Specify | Configure | Install | Commission | Hand off | Support |
|---|---|---|---|---|---|
| Validate module mix against panel space | Import config from a previous job | Verify wiring before power-up | Auto-test all points in sequence | Generate handoff doc | Export fault history |

### Release 3 — scale across jobs

| Specify | Configure | Install | Commission | Hand off | Support |
|---|---|---|---|---|---|
| Quote generator from line survey | Config templates by machine type | Guided install checklist | Remote witness for sign-off | Plant training mode | Remote firmware update |

---

### Detail under one backbone step: Commission

**Verify each I/O point** (R1)
- Toggle output and confirm at the device
- Trigger input and confirm at the controller
- Record pass/fail per point

**Auto-test all points in sequence** (R2)
- Run the full point list unattended
- Flag failures with slot and point number
- Produce a signed test record

**Remote witness for sign-off** (R3)
- Customer engineer observes the test remotely
- Test record signed without a second site visit
```

---

## What this map teaches that the SaaS one can't

- **The walking skeleton is genuinely thin, and it's still a real job.** Release 1 commissions a
  controller manually, point by point, with a printed list. Slow, and it works end to end — which
  is the test of a walking skeleton. A SaaS map can slice thinner; here the floor is "the line runs."
- **Release slices follow economics, not screens.** R2 targets rework (the expensive failure in
  commissioning), R3 targets scale across jobs. Neither is a feature grouping.
- **One backbone step spans two locations and two organizations.** "Commission" happens on the
  customer's floor, performed by an integrator, witnessed by a plant engineer. Mapping it as a
  single actor's task would have hidden the sign-off step entirely — which is where R3's value is.
- **The last column is where the product lives longest.** Support runs for a decade after
  commissioning ends. Story maps that stop at "hand off" systematically under-serve the phase with
  the most cumulative user-hours.
- **Remote witness (R3) is a workflow change disguised as a feature.** It removes a site visit from
  the customer's engineer, not the integrator's. Mapping across both actors is what made that
  visible.
