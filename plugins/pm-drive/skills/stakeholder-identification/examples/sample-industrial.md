# Stakeholder Identification Example — Industrial

**Initiative:** Northfield Automation is adding remote firmware update to the NFA-500. A controller
in a customer's panel can be updated from a service console hundreds of miles away.

---

## Step 1: Brainstorm (unfiltered)

Field service technicians · plant maintenance staff · plant operations managers · controls
engineers at integrators · the 8 channel partners · plant IT and OT security · Northfield firmware
engineering · Northfield service org · Regulatory (UL/CE) · Legal · insurers of customer plants ·
plant safety officers · customers running validated processes · the tooling vendor · competitors

---

## Step 2: Categorize

| Stakeholder | Ally | Audience | Influencer |
|---|---|---|---|
| Northfield field service | ✓ | ✓ | ✓ |
| Plant maintenance staff | | ✓ | ✓ |
| Plant operations managers | | ✓ | ✓ |
| Plant OT security | | ✓ | ✓ |
| Channel partners (8) | ✓ | ✓ | ✓ |
| Regulatory (UL/CE) | | | ✓ |
| Plant safety officers | | ✓ | ✓ |
| Validated-process customers | | ✓ | ✓ |

**The overlap that mattered:** channel partners are all three. They benefit (fewer support
escalations), they're affected (their service revenue includes site visits this feature removes),
and they influence what their customers adopt. **Ally and threatened party simultaneously.**

---

## Step 3: R/P/D

| Stakeholder | R | P | D | Notes |
|---|---|---|---|---|
| Regulatory body | — | ✓ | — | Listing impact determines whether this ships at all |
| Plant OT security | — | ✓ | — | Can refuse to open the network path, per site |
| Plant operations manager | — | ✓ | ✓ | Decides enrollment for their plant |
| Northfield VP Engineering | ✓ | — | ✓ | Funds and prioritizes |
| Channel partners | — | ✓ | — | Effectively gate adoption at accounts they service |

**Gap found:** **plant OT security** holds P at every single site and appeared eleventh in the
brainstorm. A remote update path is a network ingress into an operational-technology environment —
the exact thing OT security exists to refuse. Missing them wouldn't have delayed launch; it would
have made the feature unadoptable one site at a time, invisibly.

---

## Step 4: Equity lens

- **Who bears cost without power?** **Plant maintenance staff.** A controller on their line can now
  change state initiated by someone off-site. If an update goes wrong at 2am, they are the ones
  standing at the panel — and they have no say in enrollment.
- **Whose perspective is missing because we assumed someone represents them?** We assumed the
  operations manager speaks for maintenance staff. On "who can change my equipment remotely," that's
  not a safe assumption.
- **Third-degree affected?** Plant safety officers, who own the incident review if an update
  contributes to an unplanned stop.

**Added:** plant maintenance staff and safety officers, both promoted from mentions to real
stakeholders.

---

## Step 5: Bias check

- **Who did we default to naming?** People inside Northfield, then the buyer. Seven of the first
  ten names were ours or the person who signs.
- **Who was absent, and why?** OT security and safety officers — because we think of this as a
  product feature and they think of it as a change to a controlled environment.
- **What did we assume?** That "the customer" is the operations manager. On this feature, OT
  security can veto and maintenance staff bear the consequence.

---

## Step 6: Priority targets

| Name | Category | R/P/D | What we need to learn |
|---|---|---|---|
| Plant OT security | Audience + Influencer | P | What network path, authentication, and audit evidence they'd require before permitting ingress — and whether any would refuse outright |
| Plant maintenance staff | Audience + Influencer | — | What they need to trust a remote change: notification, veto, rollback visibility, or something else |
| Channel partners | Ally + Influencer | P | Whether removing site visits threatens their service revenue enough to slow adoption, and what would make it a win for them |

---

## What to notice

- **The gap test found the true blocker.** OT security holds Permission at every site and surfaced
  eleventh. Nothing about the schedule would have flagged it; the R/P/D pass did.
- **The equity lens found the people who absorb the risk.** Maintenance staff live with the
  consequences of a remote change and have no say in whether their plant enrolls.
- **A stakeholder is an ally and a threatened party at once.** Channel partners benefit and lose
  revenue simultaneously. Naming both makes the third priority question honest — "what would make
  this a win for them" rather than "how do we get them on board."
- **The bias pattern matches the SaaS example.** Both teams defaulted to builders and buyers, and
  both missed a Permission-holder who could stop the work. That's the pattern the check exists to
  surface, and it appears to be domain-independent.
