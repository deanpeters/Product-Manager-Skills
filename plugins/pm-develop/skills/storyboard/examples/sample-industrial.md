# Storyboard Examples — Industrial

A six-frame storyboard for Northfield Automation's NFA-500, used to align engineering, sales, and
field service before anything was built.

The industrial twist: the "oh crap" moment is usually loud, expensive, and happening at an
inconvenient hour. That makes the narrative easy to feel — and easy to overdramatize. Keep it at
the scale a technician would recognize.

---

## Example 1: Good Storyboard (NFA-500)

```markdown
## 6-Frame Storyboard: NFA-500 Fault Isolation

**Frame 1: Meet Sam**
Sam is a maintenance technician on second shift at a parts plant in Ohio. Fifteen years there. He
knows every machine on his four lines by sound — he can tell you which one is running rough from
the break room.

**Visual:** Sam walking a quiet plant floor at night, coffee in hand, four lines running behind him.

**Frame 2: The Problem**
Line 3 stops at 1:40am. Sam gets to the panel and finds what he always finds: one red fault light.
It means one of seventeen things. He starts pulling the panel and testing points with a meter,
working through them the way he learned from the tech before him.

**Visual:** A single red LED on a control panel. Sam's notebook open beside it, filled with
hand-written fault codes and what they actually meant.

**Frame 3: The 'Oh Crap' Moment**
Forty minutes in, still testing. The shift supervisor comes by to ask how long — the answer is "I
don't know yet," which is the answer Sam hates giving. If he guesses and swaps the controller,
that's two more hours re-commissioning. If he keeps testing, the line stays down. He's not
diagnosing a machine anymore; he's gambling.

**Visual:** Sam mid-test with the meter, supervisor in the doorway, clock reading 2:20am.

**Frame 4: Enter the NFA-500**
Six months later, the same line has an NFA-500 in the panel. Line 3 stops at 1:40am. Sam walks up
and the front panel reads: **Slot 4 — input fault.** No laptop. No software. No network. Just the
answer, at panel height, readable with gloves on.

**Visual:** The NFA-500 front panel, slot 4 indicator lit, the slot number legible from arm's
length.

**Frame 5: The Payoff**
Sam pulls the module from slot 4, drops in a spare from the cabinet, and powers up. The rest of the
configuration is untouched — no re-commissioning. Line 3 is running again at 1:58am. He never
opened the notebook.

**Visual:** Sam sliding a module into place, the line moving behind him, clock reading 1:58am.

**Frame 6: The New Normal**
Three months on, Sam's notebook sits in a drawer. The plant's downtime log now shows fault codes
instead of blank duration entries, so the operations manager can finally tell which lines are
failing for which reasons — and defend a capital request with something better than anecdotes.

**Visual:** The notebook in a drawer; on a desk nearby, a downtime report with fault detail per row.
```

---

**Why this works:**
- **Frame 3 names the real emotion.** "He's not diagnosing a machine anymore; he's gambling" is the
  line that makes engineers understand why the fault light is a design failure and not a minor
  annoyance.
- **The notebook is the through-line.** It appears in Frame 2 as a workaround, is absent in Frame 5,
  and sits in a drawer in Frame 6. One object carries the whole arc without a word of explanation.
- **Frame 4 states constraints as plot.** "No laptop. No software. No network." reads as narrative
  and functions as a requirement.
- **The times are specific.** 1:40 to 2:20 versus 1:40 to 1:58. Anyone can do that subtraction.
- **Frame 6 widens to a second beneficiary.** The operations manager gets something too, which is
  how a technician-facing feature gets funded.

---

## Example 2: Bad Storyboard (same product)

```markdown
**Frame 1:** A manufacturing company struggles with downtime.
**Frame 2:** Their legacy controls lack modern diagnostics.
**Frame 3:** This causes inefficiency and lost productivity.
**Frame 4:** They install the NFA-500.
**Frame 5:** Diagnostics are now faster and easier.
**Frame 6:** Productivity and OEE improve significantly.
```

**What breaks:**
- **No person.** "A manufacturing company" cannot be at a panel at 2am. Without Sam, there is no
  moment anyone can picture, and picturing it is the entire point of a storyboard.
- **No specific moment.** Frames 2 and 3 restate the same abstraction twice.
- **Frame 4 is a purchase, not a scene.** The good version shows the product *being used* at the
  exact moment the old one failed, which is what makes the contrast land.
- **"Faster and easier"** — than what, by how much? No numbers, so no one can check it or feel it.
- **It could be any industrial product.** Swap the name and it still reads the same, which means it
  aligns nobody on anything specific.
- **Nothing was learned by writing it.** The good version surfaced a design constraint — panel-height
  legibility with gloves on. This version could be written without ever meeting a customer.

---

## What the storyboard changed

Sales read Frame 3 and stopped leading demos with the modular-I/O architecture. They started
leading with the 2am scenario, because it's the one every maintenance manager has lived.

Engineering read Frame 4 and moved the fault display from a companion app to the unit itself. The
phrase "no laptop, no software, no network" was in the storyboard three months before it was in a
requirement.
