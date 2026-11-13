# User Story Examples — Industrial

Northfield Automation builds retrofit control systems for legacy production lines. These stories
come from the NFA-500 platform, the modular successor to the NFA-200.

The domain differs from SaaS in ways that change the story: users are often **not** the buyer, the
cost of a defect is measured in line downtime rather than churn, and "I want to" frequently means
"I want to avoid a two-hour drive to a plant at 3am."

---

## Example 1: Good User Story

```markdown
### User Story 118:

- **Summary:** Push firmware to NFA-500 units remotely so techs stop driving to sites for patches

#### Use Case:
- **As a** field service technician supporting 40+ NFA-500 installations across three states
- **I want to** apply a firmware update to a controller without traveling to the site
- **so that** a 20-minute patch stops costing a full day of windshield time

#### Acceptance Criteria:

**Scenario 1: Update applies during a planned maintenance window**
- **Given** a controller is enrolled in remote management and the line is in a scheduled
  maintenance window
- **When** I push a firmware update from the service console
- **Then** the controller applies the update, restarts, and reports its new version within 5 minutes
- **And** the console logs the operator, timestamp, and prior version for the audit trail

**Scenario 2: Line is running**
- **Given** a controller is enrolled and the line is actively running
- **When** I push a firmware update
- **Then** the console refuses the push and shows the next scheduled maintenance window
- **And** offers to queue the update for that window

**Scenario 3: Update fails mid-apply**
- **Given** a firmware update has begun
- **When** the update fails or the connection drops
- **Then** the controller rolls back to the previous firmware and resumes normal operation
- **And** raises an alert to the service console naming the failure point
```

**Why this works:**
- **The user is the technician, not the buyer.** The plant manager pays; the tech lives with it.
  Writing the story from the buyer's seat would have produced "as a plant manager I want lower
  service costs" — true, and useless to a developer.
- **The "so that" is concrete.** "A full day of windshield time" is a number someone can check.
- **Scenario 3 is the real story.** In industrial control, the failure path *is* the requirement — a
  controller that bricks mid-update stops a production line. Rollback isn't an edge case, it's the
  reason the feature is safe to ship.
- **Scenario 2 encodes a safety rule as behavior.** "Refuses the push" is testable; "should be
  careful about running lines" is not.

---

## Example 2: Bad User Story (same feature)

```markdown
### User Story 118:

- **Summary:** Remote firmware updates

#### Use Case:
- **As a** user
- **I want to** update firmware remotely
- **so that** it's more efficient

#### Acceptance Criteria:
- Firmware can be updated over the network
- Should be secure
- Must not break anything
```

**What breaks:**
- **"As a user"** — which one? The technician who applies it, the controls engineer who approves it,
  and the operations manager who schedules the window need different things.
- **"So that it's more efficient"** — for whom, and by how much? Nothing here tells you whether the
  feature succeeded.
- **"Must not break anything"** is the entire hard problem, waved at. Compare to Scenario 3, which
  says exactly what happens when it does break.
- **"Should be secure"** — an unfalsifiable phrase attached to a device that can stop a production
  line. Either specify the control or write a separate story for it.

---

## Example 3: Good User Story (a different user, same platform)

```markdown
### User Story 124:

- **Summary:** Show which I/O module failed so techs stop swapping the whole controller

#### Use Case:
- **As a** plant maintenance technician responding to a line stoppage
- **I want to** see which specific I/O module has faulted, on the unit itself
- **so that** I can swap one module instead of replacing the controller and re-commissioning

#### Acceptance Criteria:

**Scenario 1: Single module fault**
- **Given** an I/O module has faulted
- **When** I look at the controller's front panel
- **Then** the faulted module's indicator shows a fault state and the display names the slot number
- **And** the same information is readable from the service console

**Scenario 2: Fault clears after module swap**
- **Given** a faulted module has been replaced with a known-good module
- **When** the controller powers up
- **Then** the fault clears without requiring re-commissioning of the other modules
```

**Why this works:**
- **The value is in what it prevents.** Re-commissioning a controller is hours of work; the story
  buys a module swap instead.
- **"On the unit itself"** matters. The tech is standing at a panel on a plant floor, often without
  a laptop and sometimes without connectivity. A SaaS-shaped story would have assumed a dashboard.
- **Scenario 2 protects the value.** Without it, you could pass Scenario 1 and still force a
  re-commission — technically correct, practically worthless.
