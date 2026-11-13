# Jobs-to-be-Done Examples — Industrial

JTBD analysis from **Northfield Automation**, whose retrofit control systems keep aging production
lines running.

**The industrial twist:** the person doing the job and the person paying for it are different
people with different jobs. Analyze the wrong one and you build a product that demos well and gets
worked around on the floor.

---

## Example 1: Retrofit Control Platform (Good JTBD Analysis)

### The job performer: maintenance technician

**Functional Jobs:**
- Get a stopped line running again without making the fault worse
- Determine whether the fault is the controller, a sensor, the wiring, or the machine
- Replace the failed part without re-commissioning everything around it
- Finish the shift without a callback

**Emotional Jobs:**
- Feel competent rather than made to look slow by the tool
- Avoid the exposure of calling the OEM, which reads as "I couldn't fix it"
- Trust the equipment enough to sleep after a night shift

**Social Jobs:**
- Be the person on the crew who can fix anything
- Give the shift supervisor an honest answer to "how long?"
- Pass knowledge to the next tech the way it was passed to them

### The job performer: plant operations manager

**Functional Jobs:**
- Commit to delivery dates the plant can actually hit
- Decide whether to fund a controls refresh or defer it another year
- Attribute downtime to a cause specific enough to act on

**Emotional Jobs:**
- Feel confident defending a capital request with something better than anecdotes
- Stop feeling at the mercy of vendors who all claim the same fix

**Social Jobs:**
- Be seen by the plant manager as someone whose numbers hold up
- Not be the person who approved the upgrade that made things worse

---

### Pains

**Technician:**
- One fault light meaning seventeen things
- Diagnostics requiring software on a laptop that can't come to the panel
- Guessing wrong and losing two hours re-commissioning
- Being blamed for downtime they diagnosed correctly and fast

**Operations manager:**
- Downtime logged as duration and line number, with no cause
- Vendor claims that can't be verified before purchase
- Capital requests judged against anecdote

### Gains

**Technician:**
- Knowing which part failed before touching anything
- Swapping one module instead of a controller
- Not being phoned at 2am for the same fault twice

**Operations manager:**
- Downtime attributable to a cause, in a report
- A refresh decision defensible with plant data

---

## Why this analysis works

- **Two performers, analyzed separately.** They share a product and share almost no jobs. Merging
  them produces "our customer wants reliability," which guides nothing.
- **The emotional jobs are the honest ones.** "Avoid the exposure of calling the OEM" explains
  behavior that functional analysis can't — why a tech spends 40 minutes with a meter rather than
  20 seconds on the phone.
- **The social job predicts adoption.** "Be the person who can fix anything" means a tool that makes
  the tech look replaceable will be resisted no matter how well it performs. Position it as
  amplifying expertise, not substituting for it.
- **The manager's job explains the sale.** Downtime attribution isn't a technician feature at all —
  it's what turns a floor-level improvement into a funded purchase.

---

## Example 2: Bad JTBD Analysis (same product)

**Functional Jobs:**
- Reduce downtime
- Improve efficiency
- Increase productivity

**Emotional Jobs:**
- Feel confident in their equipment

**Social Jobs:**
- Be seen as a modern operation

**What breaks:**
- **"Reduce downtime" is an outcome, not a job.** Nobody wakes up hiring a product to reduce
  downtime — they hire it to *find out which module failed* so the line restarts. The job is the
  work being done; downtime is what improves if you do it well.
- **No performer named.** These could belong to the tech, the manager, the integrator, or the
  plant manager. Since they belong to no one specific, they generate no design constraint.
- **"Feel confident in their equipment"** is a greeting card. Compare to "avoid the exposure of
  calling the OEM," which tells you something you could build for.
- **It fits any industrial product ever sold**, which is the reliable signal that a JTBD analysis
  has said nothing.
