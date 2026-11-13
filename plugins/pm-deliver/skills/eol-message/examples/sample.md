# EOL Message Example — SaaS

**Product:** Fieldlight Classic Dispatch (legacy dispatch module, Fieldlight FSM platform)
**Size:** Standard · **Path:** Replacement
**Context:** ~800 accounts, $2.4M ARR, annual contracts, no regulatory constraint. Replaced by
Fieldlight Next Scheduling. About 30 accounts use custom dispatch rules that don't carry over.

---

## The message

```markdown
## End-of-Life Announcement: Fieldlight Classic Dispatch

### Product Transition Narrative

**We are:** Fieldlight, a field service management platform serving 4,000 service businesses
- We're committed to getting your technicians to the right job with the right information
- We continuously evolve the platform based on how crews actually work
- We're building toward scheduling that adapts in real time to what happens in the field

**Announcing:**
- We are retiring Fieldlight Classic Dispatch on December 31, 2026, and moving all accounts to
  Fieldlight Next Scheduling.

**Because:**
- Classic Dispatch runs on infrastructure that recalculates routes once a night and can't respond
  to changes during the day
- Next Scheduling reoptimizes as jobs run long, get cancelled, or get added
- Consolidating lets us put all of our scheduling engineering into one product instead of splitting
  it across two

**Which means for you:**
- Schedules that adjust when the day goes sideways, instead of at 6am only
- Arrival windows your dispatchers can actually promise customers
- Every future scheduling improvement lands in the product you're on

### Current Product Context

**Our product** Fieldlight Classic Dispatch
- **is a** dispatch board that assigns jobs to technicians and builds daily routes
- **that has served** service businesses for nine years
- **by providing** dependable morning route planning that dispatchers could learn in an afternoon

### Customer Impact

**We understand that this may affect you by:**
- Requiring you to rebuild recurring dispatch rules in Next (most accounts: 2-3 hours; we'll do it
  with you if you'd rather)
- Retraining dispatchers on a scheduling board that works differently — it's a real change, not a
  reskin
- Updating any integrations that read the Classic dispatch API (v1 endpoints)

### Transition Solution

**For** service businesses
- **that currently use** Fieldlight Classic Dispatch
- Fieldlight Next Scheduling
- **is a** real-time scheduling and dispatch system
- **that** keeps the dispatch board your team knows while adding schedules that adapt as the day
  actually unfolds

### Differentiation and Continuity

- **Like** Classic Dispatch,
- Next Scheduling
- **provides** drag-and-drop assignment, technician skill matching, and the same daily route view
- **while also offering** mid-day reoptimization, live arrival windows customers can track, and
  overtime warnings before you commit a job

### Support and Next Steps

**To ensure a smooth transition, we will:**
- Migrate your standard dispatch rules automatically, with your approval — no rebuild needed
- Provide a 1-on-1 session for any account using custom rules (we'll reach out to you first; we
  know who you are)
- Run weekly 30-minute Next training sessions for dispatchers through March 2027
- Keep Classic Dispatch fully available until December 31, 2026 — no degradation while you move

### Timeline

| Gate | Date | What it means for you |
|---|---|---|
| End of Sale | March 1, 2026 | Classic Dispatch is no longer available to new accounts. Nothing changes for you. |
| End of Expansion | June 1, 2026 | You can't add new dispatch boards in Classic. Existing boards work normally. |
| End of Maintenance | October 1, 2026 | Classic still runs, but we stop shipping fixes. Move before this if you can. |
| End of Life | December 31, 2026 | Classic Dispatch stops working. Export any data you want to keep by this date. |

### Call to Action

- Start your migration at fieldlight.com/next-migration — the wizard takes about 20 minutes
- Using custom dispatch rules? Book your 1-on-1 at fieldlight.com/next-help
- Questions: support@fieldlight.com, or your account manager directly
```

---

## Why this works

- **Empathy before pitch.** The impact section names the retraining cost and the integration work
  before the benefits get another mention.
- **Honest effort estimate.** "2-3 hours" is falsifiable. A customer who times themselves and finds
  it accurate trusts the next thing you tell them.
- **The hard segment is named, not hidden.** The ~30 custom-rule accounts get a specific commitment
  ("we know who you are") instead of discovering the gap on their own during migration.
- **Gates in customer consequences.** "Classic still runs, but we stop shipping fixes" — nobody has
  to know what EOM means.
- **Lead time proportional to the ask.** Ten months for a change that requires retraining and
  rebuild work.

---

## The same announcement, written badly

```markdown
Subject: Important changes to your Fieldlight account

As part of our ongoing platform modernization, Fieldlight Classic Dispatch will be sunset later
this year. Due to low adoption and rising maintenance costs, we've made the decision to consolidate
our scheduling products.

Customers will be migrated to Fieldlight Next. Please contact support with any questions.
```

**What breaks:**
- **"Later this year"** — fails the sticky-note test outright. No date, no action, no deadline.
- **"Low adoption and rising maintenance costs"** — the rationale is entirely about Fieldlight's
  problems. To the 800 accounts using it daily, "low adoption" reads as *you don't matter*.
- **"Customers will be migrated"** — passive voice hides who does the work. The customer does, and
  they're about to find that out the hard way.
- **No impact acknowledgment** — the dispatch-rule rebuild and retraining go unmentioned, which
  means every one of those 800 accounts discovers them alone.
- **"Contact support"** — no named path for the 30 accounts with custom rules, who are exactly the
  accounts most likely to churn over this.

Same decision, same product, same date. The first version produces migrations; the second produces
a support queue and a churn spike.
