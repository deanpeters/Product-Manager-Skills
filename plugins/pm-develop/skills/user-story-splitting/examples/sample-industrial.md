# User Story Splitting Examples — Industrial

Splitting oversized stories on **Northfield Automation's** NFA-500 platform.

**The industrial twist:** the usual tempting split — frontend/backend, or firmware/console — is
especially wrong here, because a firmware-only slice ships nothing a customer can use and a
console-only slice has nothing to talk to. Worse, firmware releases are expensive and infrequent, so
a bad split can strand a half-feature in the field for a quarter.

---

## Example 1: Splitting by Workflow Steps

**Original Story:**
```markdown
As a field service technician, I want to manage firmware across my installed base
so that units stay current without site visits.
```
Too big: spans enrollment, visibility, updating, and rollback.

**Split:**
1. **See firmware version** for each enrolled unit in the service console
2. **Enroll a unit** in remote management during commissioning
3. **Push an update** to one enrolled unit during a maintenance window
4. **Push to a group** of units on the same schedule
5. **Roll back automatically** when an update fails mid-apply

**Why this works:** each slice is independently useful. Slice 1 alone answers "which units are
behind?" — a question techs ask weekly — and it ships without touching firmware at all.

**The sequencing trap:** slice 5 looks like error handling to defer. It cannot be. Slice 3 must not
ship without it, because a failed update on an un-rolled-back controller stops a production line.
**In this domain the failure path is part of the walking skeleton, not a follow-up.**

---

## Example 2: Splitting by Business Rule

**Original Story:**
```markdown
As a technician, I want the controller to refuse unsafe operations
so that I cannot accidentally stop a running line.
```

**Split by rule:**
1. Refuse firmware push when the line is **running**
2. Refuse firmware push when the unit reports an **active fault**
3. Refuse configuration change when the unit is in a **safety-interlocked state**
4. Allow **override with explicit confirmation** for units in maintenance mode

**Why this works:** each rule is independently testable and independently valuable. Rule 1 alone
prevents the most likely accident.

**Note on rule 4:** an override is a separate story on purpose. Bundled into rules 1-3, "refuse
unless overridden" gets built as one permissive path and the refusal becomes advisory. Split out,
the refusal ships strict first and the override arrives as a deliberate decision with its own
review.

---

## Example 3: Splitting by Hardware Variant

A split that has no clean SaaS equivalent.

**Original Story:**
```markdown
As a technician, I want fault isolation on the front panel
so that I know which module failed.
```

**Split by variant:**
1. Fault isolation on the **4-slot base unit** (the highest-volume configuration)
2. Fault isolation on the **8-slot expanded unit**
3. Fault isolation for **third-party modules** in a mixed configuration

**Why this works:** slice 1 covers the majority of the installed base and can ship on the existing
panel hardware. Slice 2 needs a display change. Slice 3 depends on data third parties may not
expose — genuinely risky, and worth isolating so it can't sink the first two.

**The trap this avoids:** "support all configurations" as one story means the hardest variant sets
the timeline for the easiest, and the highest-volume customers wait on an edge case.

---

## ❌ The Split to Avoid: By Component

**Tempting split:**
1. Firmware: detect and report slot-level faults
2. Console: display fault data
3. Panel: add slot indicators

**Why this is wrong:**
- **No slice delivers anything alone.** Firmware that reports to nothing, a console with no data,
  indicators with nothing driving them
- **Nothing is demonstrable** until all three land, so you learn nothing until you've spent
  everything
- **It's especially costly here.** Firmware release windows are infrequent; shipping slice 1 alone
  means a firmware revision in the field that does nothing observable, and you'll need another
  revision to make it useful
- It splits by **who does the work**, not by what a user gets — the most common splitting mistake in
  any domain, and the most expensive one in this one

**The fix:** Example 3's variant split. Every slice crosses firmware, console, and panel together
for a narrower set of hardware — thin in scope, complete in function.
