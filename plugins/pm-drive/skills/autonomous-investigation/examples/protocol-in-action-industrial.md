# Autonomous Investigation Protocol — In Action (Industrial)

All companies, products, URLs, and figures are **fictional**. Industrial sibling of
[`protocol-in-action.md`](protocol-in-action.md). The SaaS run showed the gate revision and the
gaps list; this one shows two clauses the SaaS run couldn't stress as hard: **confidence stacking
across physical-world channels** (customs, registries, permits) and the **conflict case** — when
two disciplines disagree and the protocol says *dig* instead of average.

---

## 1. Invocation, budget, and one surgical question

> **User:** Investigate whether Meridian Freight Systems is entering plant-floor automation —
> this supports how much of Northfield's 2027 roadmap we fence off for a defensive play.

Target and decision arrived inline. The skill spends one question:

> **Agent:** One question: does "entering" mean shipping a product, or building the capability?
> The evidence bars differ — capability shows up in filings and hiring years before a product
> shows up in a catalog.

> **User:** Capability. If it's real, 2027 planning has to know.

## 2. The search-plan gate

> **Agent:** **Search plan** (say "revise" to change it):
> - Sweep certification registries, customs/trade data, and facility/permit records for
>   commitment-side signals (money and atoms, not words)
> - Cross-check with hiring patterns, API/docs changes, and their public solutions pages
> - Facts get URLs and dates; interpretations get labeled Inference; unknowables go to the gaps
>   list, not the estimate mill

Continue unless revised — the user lets it run.

## 3. Findings — a stack, and a conflict

> **Key findings:**
> - Certification filing "in process" for a plant-floor equipment class, via a Meridian
>   subsidiary — **Fact** ([registry entry, Oct 2026](https://example.com/certregistry/meridian))
> - Component import volumes rising two consecutive quarters — **Fact** ([trade records](https://example.com/tradedata/meridian))
> - "Manufacturing early access" signup on their solutions page — **Fact** ([page diff, Nov 2026](https://example.com/archive/meridian-solutions))
> - API docs already model generic asset classes — **Fact** ([docs](https://example.com/meridian/docs))
>
> **The stack (4 channels agree):** registry (MASINT-adjacent) + customs (MASINT) + web
> staging (SIGINT) + architecture (TECHINT) → capability build is real — **actionable
> intelligence**, not a watch item.
>
> **The conflict:** HUMINT disagrees. Their careers page shows **no** manufacturing-domain
> hires — no controls engineers, no plant-floor sales, no channel roles — **Fact** (job boards,
> checked Nov 2026). Four channels say "building"; the people channel says "not staffing it."
> Per the protocol: channels in conflict means someone is bluffing — dig, don't average.
>
> **The dig (one more pass, scoped to the conflict):** the certification filing lists a
> *partner engineering firm* as the responsible party — **Fact** (registry detail page).
> Resolution hypothesis: they're building through partners, not headcount — which changes the
> defensive read entirely: a partner-led entry can be slowed by winning the partners —
> **Inference**, confidence: medium.
>
> **Gaps (couldn't find, not guessed):**
> - No way to see the partner agreement's exclusivity terms from public record
> - Import volumes can't be allocated between warehouse (their core) and plant-floor (the bet)
>
> **Reading for your decision:** capability build confirmed, product 12-36 months out
> (certification clock), and the entry vector is partner-led. Fence off a *partner-program*
> response in 2027, not a product-defense sprint — **Inference**.
>
> **Final Step — reply 1, 2, 3, 4, a combination, or "Verbose Mode":**
> 1. Map their likely partner-firm candidates (the integrator roll-ups first)
> 2. Set tripwires: registry progress, distributor listings, domain hiring
> 3. Trace the partner-led scenario into 2027 roadmap assumptions
> 4. Brief leadership with the stack + conflict resolution as-is

---

## Why this example works

- **The conflict case is the star.** Four agreeing channels would have shipped a tidy
  "they're coming" brief; the disagreeing fifth channel forced a dig that changed the
  *strategic response* (win the partners vs. race the product). Averaging the signals — "80%
  confident" — would have buried the most decision-relevant fact in the whole run.
- **Commitment-side evidence led the plan.** Registries, customs, permits — money and atoms.
  The announcement layer (their marketing site) appears only as staging corroboration, exactly
  the "ambition is OSINT; commitment shows up elsewhere" corollary.
- **The gaps list stayed honest under pressure** — import allocation and partner terms are
  unknowable from outside, and the report says so instead of estimating, even though both
  numbers would have made the brief more satisfying.
- **Read the two siblings together:** SaaS run = gate revision + graceful unattended rerun;
  industrial run = stacking + conflict resolution. Between them, all seven clauses appear under
  load in two different physics.
