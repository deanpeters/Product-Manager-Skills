# Stakeholder Identification Example — SaaS

**Initiative:** Fieldlight is adding a customer-facing arrival-window feature to Next Scheduling —
technicians' ETAs become visible to the end customer whose home or site they're visiting.

---

## Step 1: Brainstorm (unfiltered)

Dispatchers · field technicians · service business owners (our buyer) · the end customer receiving
the service · Fieldlight support · Fieldlight sales · CS · engineering · SMS/notification vendor ·
Legal · the technicians' union at two enterprise accounts · competitors · app store reviewers ·
insurance carriers for our customers · integrators who resell Fieldlight

---

## Step 2: Categorize

| Stakeholder | Ally | Audience | Influencer |
|---|---|---|---|
| Service business owners (buyer) | ✓ | ✓ | ✓ |
| Dispatchers | ✓ | ✓ | |
| Field technicians | | ✓ | ✓ |
| End customers | | ✓ | ✓ |
| Fieldlight support | | ✓ | ✓ |
| Legal | | | ✓ |
| Technicians' union (2 accounts) | | ✓ | ✓ |
| Notification vendor | | | ✓ |

**The overlap that mattered:** field technicians are an audience *and* an influencer. They don't buy
Fieldlight, but they tell their employer what's unusable — and a tracked-location feature is exactly
the kind of thing they escalate.

---

## Step 3: R/P/D

| Stakeholder | R | P | D | Notes |
|---|---|---|---|---|
| Service business owner | — | ✓ | ✓ | Decides adoption per account |
| Fieldlight CPO | ✓ | — | ✓ | Funds and prioritizes |
| Legal | — | ✓ | — | Location-data disclosure review |
| Notification vendor | ✓ | — | — | Delivery infrastructure |
| Technicians' union | — | ✓ | — | Effectively holds P at two enterprise accounts |

**Gap found:** Legal and the union both hold **P** and neither appeared in the first two minutes of
Step 1. They were added late — which is the finding. The team's default is to name people who build
and buy, not people who can stop it.

---

## Step 4: Equity lens

- **Who bears cost without power?** **Field technicians.** The feature makes their location visible
  to a third party. They don't buy the product, can't opt out, and weren't consulted.
- **Whose perspective is missing because we assumed someone represents them?** We assumed the
  business owner speaks for technicians. On a surveillance-adjacent feature, that assumption is
  clearly wrong.
- **Third-degree affected?** End customers' household members, who may be home when a tracked
  technician arrives.

**Added:** field technicians promoted from a passing mention to a priority stakeholder.

---

## Step 5: Bias check

- **Who did we default to naming?** Buyers and builders. The first eight names were all people who
  pay us or work here.
- **Who was absent, and why?** Technicians and Legal. Technicians because they're not the buyer;
  Legal because we think of them as a late gate rather than a stakeholder.
- **What did we assume?** That "the customer" means the business owner. Three different people in
  this initiative could be called the customer.

---

## Step 6: Priority targets

| Name | Category | R/P/D | What we need to learn |
|---|---|---|---|
| Field technicians | Audience + Influencer | — | Where the line sits between "customer knows when I'll arrive" and "my employer tracks me all day" |
| Legal | Influencer | P | What disclosure and consent are required, and whether consent must come from the technician or the employer |
| Service business owners | Ally + Influencer | P, D | Whether they'd adopt if technicians push back, and whether they've promised customers this already |

---

## What to notice

- **The equity lens changed the plan.** Field technicians went from a footnote to a priority target,
  and that single move probably prevented shipping a feature that gets escalated as surveillance.
- **The gap test earned its place.** Two P-holders were missed in the initial brainstorm. Both could
  have blocked launch after build.
- **The bias check was specific.** "We default to buyers and builders" is actionable; "we should be
  more inclusive" isn't.
- **Three priority targets, each with a real question.** "Where the line sits between knowing an ETA
  and being tracked all day" is a research question. "Understand technician needs" is not.
