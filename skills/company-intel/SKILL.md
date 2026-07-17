---
name: company-intel
argument-hint: "[company, industry, or competitor set]"
description: Research a company, industry, or competitor set using web search and seven analytical lenses. Use when you need structured intel that feeds downstream PM skills.
intent: >-
  Act as a research engine that builds deep, structured understanding of companies, industries,
  and competitor sets through **seven analytical lenses** — financial landscape, market offer,
  product portfolio, competitive dynamics, rising trends, PM implications, and strategic signals
  (patents, hiring, leadership). Produces a stable, structured output that downstream skills
  consume to generate battlecards, SWOT analyses, positioning statements, PESTEL assessments,
  and market sizing. Supports four entry points: single company, industry/sector, named competitor
  set, or company + "discover my competitors" (researches the company first, identifies likely
  competitors, confirms the list, then runs the full competitor set analysis).
type: workflow
best_for:
  - "Building deep company or industry knowledge before a client engagement or workshop"
  - "Generating structured research that feeds battlecards, SWOT, positioning, or PESTEL"
  - "Running a competitive scan across 3-5 companies with cross-company comparison"
  - "Refreshing intel quarterly on companies you track"
scenarios:
  - "Run company-intel on [company or their domain, e.g. helix-motion.com]"
  - "Give me intel on the clinical data management industry"
  - "Compare [Company A], [Company B], and [Company C]"
  - "Run company-intel on [company] competitors"
  - "Refresh my intel on [company] — what's changed since last quarter?"
---

## Purpose

Research engine that builds deep, structured understanding of companies, industries, and competitor sets. Produces a stable output format that you can hand off to other skills and agents to generate battlecards, SWOT analyses, positioning statements, PESTEL assessments, market sizing, and workshop content.

This is not a generic encyclopedia lookup. Every section pushes toward commercial understanding, product implications, and actionable intelligence. The output is a research primitive — structured data other skills consume — not a final deliverable.

## Input

**Works best with:** The research target: a company, an industry, or a set of competitors.
**Also useful:** The downstream use (battlecard, SWOT, positioning, market sizing) so the research emphasizes the right lenses, plus any constraints on depth or recency.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The workflow opens by asking for the target and what the intel will feed.

**Example invocation:** `Research Figma and its top 3 competitors — output feeds a positioning workshop next week.`

## Key Concepts

### Four Entry Points

The skill auto-detects entry point from the user's input. If ambiguous, ask one clarifying question: "Is this about a specific company, an industry, or a set of competitors?"

**Single Company** — User names a company (e.g., "Helix Motion Systems," "Brightwater Biologics" — or any real company). Produce the full 11-section output for that company.

**Industry/Sector** — User names an industry, sector, or niche (e.g., "clinical data management," "embedded finance," "upstream oil and gas"). Establish broad industry context, narrow into the segment, and connect findings to PM implications. Use the same 11-section structure adapted for sector-level analysis.

**Named Competitor Set** — User names 2-5 companies (e.g., "Compare Helix Motion, Northfield Automation, and Corvid Industrial"). Produce individual 11-section outputs for each company, then add a **Section 12: Cross-Company Comparison** that synthesizes across the set.

**Discover Competitors** — User names a company plus the word "competitors" (e.g., "helix-motion.com competitors" or "Helix Motion Systems competitors"). The skill:
1. Researches the named company first — enough to understand what it does, who it serves, and what market it plays in (a lightweight pass through Lenses 1-4)
2. Identifies 3-5 likely competitors based on that research, citing why each is a competitor (direct, adjacent, substitute, or emerging disruptor)
3. Presents the list for confirmation: "Based on my research, [Company]'s closest competitors appear to be [A, B, C, D, E]. Want me to run the full competitor set on these, or adjust the list first?"
4. Once confirmed, proceeds with the Named Competitor Set flow — full 11-section output for each company plus Section 12 cross-company comparison

The user can also provide a URL instead of a company name (e.g., "helix-motion.com"). The skill should resolve the URL to the company, research accordingly, and proceed.

---

### Seven Research Lenses

These lenses structure all analysis. Apply every lens to every entry point.

**Lens 1 — Financial Landscape and Business Outcomes**
How the entity makes money. Major revenue streams and cost drivers, margin pressures, growth levers, retention and expansion dynamics, capital intensity, seasonal or cyclical patterns, major risks to performance.

**Lens 2 — Market Offer and Business Model**
How the entity creates and captures value. Target markets, buyers, users, influencers, administrators, and blockers. How segments differ. Multi-sided or multi-stakeholder dynamics.

**Lens 3 — Product Portfolio and Product Outcomes**
Major offers, product families, services, platforms, channels. Bundled solutions, ecosystem plays. Digital versus human-assisted components. Legacy versus emerging offers. Distinction between business line, offer, product, feature set, service layer, and enabling platform.

**Lens 4 — Competitive Dynamics**
Direct competitors, adjacent competitors, substitutes, emerging disruptors. Where differentiation is won or lost.

**Lens 5 — Rising Trends and Strategic Concerns**
Market trends, regulatory forces, technology shifts (especially AI and automation), operational constraints, buyer expectation changes, threats from consolidation or commoditization.

**Lens 6 — How Product Management Works Here**
Product-led vs sales-led vs service-led behavior. Centralized vs federated product structures. Platform vs solution orientation. Roadmap and innovation posture. Compliance or governance overhead. Discovery maturity, data maturity, experimentation maturity, AI maturity. Cross-functional friction. Label inferences clearly.

**Lens 7 — Strategic Signals**
Three signal types — always check all three:
- **Patent activity:** Recent filings and grants via patent databases. Technology domains, R&D clusters, gaps between patent activity and public product narrative.
- **Hiring signals:** Roles open in volume, skills and tools in job descriptions, seniority being hired, language that reveals product culture (discovery, outcomes, AI-native, regulatory, experimentation).
- **Leadership changes:** C-suite and product leadership arrivals or departures in the last 12-18 months. Origin of new leaders (platform companies, consulting, competitors). New CPO, CTO, or CDO roles created, eliminated, or restructured. Board-level changes.

Sharp heuristics for reading the product organization specifically:
- **CPO/VP Product tenure:** a new product leader hired in the last 12-18 months almost always means the prior approach failed — read what they were hired *from* (platform company? consultancy? competitor?) as the intended correction.
- **PM job postings as culture documents:** how they define the PM role — outcome language vs. feature/roadmap language, discovery expectations, who PMs report to — reveals how product actually works there better than any About page.
- **Employee-review themes:** clusters around "roadmap chaos," "priorities change weekly," or "product vs. engineering tension" are Lens 6 evidence — community-tier confidence, labeled, but often the earliest honest signal.

**Reading organizational distress (optional deepening, for engagement or partnership prep).** When the
intel supports a conversation with the company — a partnership, a sales motion, a job interview — add
the distress read: what's the most likely **presenting problem** (what they'd say is wrong) versus the
probable **underlying problem** (what the evidence suggests is actually wrong)? Was there a **trigger
event** — missed guidance, a failed launch, a reorg, a new executive inheriting a mess? Calibrate the
distress level: *doing fine and optimizing* → *knows something's wrong* → *in trouble and doesn't know
it yet*. Label the whole read as Inference; it's the most useful and least certain section in the file.

---

### Key Distinctions to Maintain

Always be disciplined about these — collapsing them produces shallow analysis:
- market vs segment
- buyer vs user
- product vs service
- business outcome vs product outcome vs output
- strategy vs tactics
- discovery vs delivery
- platform vs application
- signal vs assumption
- revenue growth vs market share growth vs customer lifetime value improvement vs cost reduction

---

### Tensions Worth Surfacing

Highlight conflicts and tradeoffs wherever they appear:
- growth vs compliance
- scale vs customization
- digital self-service vs high-touch service
- standardization vs domain-specific workflow
- innovation vs legacy burden
- AI ambition vs governance reality
- customer value vs internal efficiency
- short-term revenue vs long-term platform investment

---

### Why This Works

- **Web-grounded:** Uses live search, not training-data recall — output includes citations
- **PM-native:** Every section connects to product management implications, not just business facts
- **Composable:** Stable output format that downstream skills can parse and consume
- **Repeatable:** Same input next quarter produces fresh intel — the delta is the story
- **Signal-driven:** Strategic signals (patents, hiring, leadership) are often the most honest data available — they reveal what a company is actually doing, not what it says it's doing

---

### Anti-Patterns

- **Not a Wikipedia summary:** Push past "what they do" to "what this means for product decisions"
- **Not financial analysis:** Focus is product strategy and commercial dynamics, not valuation or stock picks
- **Not a prompt generator:** The output is actual research with citations, not prompts for a future session
- **Not a one-time exercise:** Design for quarterly refresh — run it again, compare the delta

---

### Research Expectations

**Use web search actively.** This skill requires live data gathering, not recall from training data. Search for and cite:
- Investor relations materials, annual reports, earnings transcripts
- Company product pages and official strategy pages
- Regulatory disclosures and filings
- Patent databases (Google Patents, USPTO)
- Company careers pages and job aggregators (LinkedIn, Indeed, Glassdoor)
- Executive appointment announcements and leadership change coverage
- Industry analysts (Gartner, Forrester, IDC) and reputable news coverage

**Cite sources.** Every factual claim should include a source. Use the library's canonical evidence
labels from [`autonomous-investigation`](../autonomous-investigation/SKILL.md): **Fact**
(source-supported), **Inference** (evidence-based interpretation), **Assumption** (working guess).
When you're inferring — especially on Lens 6 (PM culture) and Lens 7 (strategic signals) — show the
basis: "Inference based on [evidence]."

**Source priority ladder.** Primary (filings, earnings calls, investor docs) → credible secondary
(major business press, trade publications) → community (Glassdoor, review sites, forums — lower
confidence) → inferred signals (job postings, announcements). State where each claim sits.

**Recency matters.** Prioritize sources from the last 12-24 months. Flag anything older than 18
months explicitly.

**Do not sanitize.** Brutal product reviews, public criticism of leadership, employee accounts of
roadmap chaos — it all belongs in the file, labeled and sourced. Intelligence that flatters the
subject is marketing; the reader needs the real picture.

## Application

### Step 1: Detect Entry Point

Determine from user input:
- **Single company** → proceed to Step 2 with one entity
- **Industry/sector** → proceed to Step 2, adapt sections for sector-level analysis
- **Named competitor set** (2-5 companies listed) → proceed to Step 2 for each company, then Step 3
- **Discover competitors** (one company + "competitors") → proceed to Step 1b, then Step 2 for each, then Step 3
- **URL provided** (e.g., "helix-motion.com") → resolve to company name, then detect entry point from any additional context

If ambiguous, ask one question: "Is this about a specific company, an industry, or a set of competitors?"

If the user provides additional context (e.g., "I'm preparing for a client engagement with them" or "we compete with them in the SMB segment"), use that context to weight which lenses get deeper treatment.

---

### Step 1b: Discover Competitors (when entry point is "discover competitors")

1. **Research the named company** using web search. Do a lightweight pass through Lenses 1-4 — enough to understand what the company does, who it serves, what market it plays in, and how it creates value.

2. **Identify 3-5 likely competitors** based on that research. For each, state:
   - Company name
   - Why it's a competitor (direct, adjacent, substitute, or emerging disruptor)
   - One-sentence description of how it competes

3. **Present the list for confirmation:**

   "Based on my research, [Company] is [brief description — what it does and who it serves].

   Its closest competitors appear to be:
   1. **[Competitor A]** — [relationship: direct/adjacent/substitute/disruptor]. [Why.]
   2. **[Competitor B]** — [relationship]. [Why.]
   3. **[Competitor C]** — [relationship]. [Why.]
   4. **[Competitor D]** — [relationship]. [Why.]
   5. **[Competitor E]** — [relationship]. [Why.]

   Want me to run the full competitor set analysis on these? You can also add, remove, or swap any before I proceed."

4. **Once confirmed,** proceed to Step 2 for each company (including the original), then Step 3 (cross-company comparison).

---

### Step 2: Research and Produce Output

Use web search to gather data across all seven lenses. Produce the following 11-section output:

```markdown
## 1. What This Entity Is
[Business definition, founding, market position, scale. What makes it distinct.]

## 2. How It Makes Money
[Revenue streams, cost structure, margin dynamics, financial logic.
Seasonal or cyclical patterns. Growth levers and risks.]

## 3. Who It Serves
[Buyers, users, influencers, administrators, blockers.
Segment differences. Multi-stakeholder complexity.]

## 4. What It Sells or Delivers
[Core value propositions. Key offers in plain language.
How the offer creates value for the customer.]

## 5. Key Product Lines or Offers
[Mapped by product family, platform, service, channel.
Digital vs human-assisted. Legacy vs emerging.
Distinguish: business line, offer, product, feature set,
service layer, enabling platform.]

## 6. Business and Market Pressures
[Competitive forces, regulatory pressure, technology shifts,
operational constraints. Name the tensions.]

## 7. Competitors and Alternatives
[Direct competitors, adjacent competitors, substitutes,
emerging disruptors. Where differentiation is won or lost.]

## 8. Important Trends and Risks
[Macro forces, buyer expectation shifts, AI and automation impact,
consolidation or commoditization threats.]

## 9. Strategic Signals
[Patent activity: recent filings, technology domains, R&D bets.
Hiring signals: volume roles, skills language, seniority patterns.
Leadership changes: arrivals, departures, origins, new roles created.
Include sources for each signal.]

## 10. What This Means for Product Management
[PM implications: org dynamics, discovery maturity, delivery model,
cross-functional friction, AI readiness. Product-led vs sales-led.
Likely PM challenges. Domain-specific skills PMs would need.
Label inferences.]

## 11. Sources and Confidence
[List all sources used, organized by section.
Flag assumptions and inferences explicitly.
Note any sections where data was thin or unavailable.]
```

**Quality checks for every section:**
- Does it push past description to implication?
- Does it name specific tensions, not just facts?
- Are sources cited?
- Is inference labeled?

---

### Step 3: Cross-Company Comparison (Competitor Set Only)

When the entry point is a competitor set, produce individual Section 1-11 outputs for each company, then add:

```markdown
## 12. Cross-Company Comparison

### Where They're Betting Differently
[Patent clusters, hiring patterns, leadership hires that diverge.
Which companies are investing in AI, which in services,
which in platform plays.]

### Where They're Converging
[Same platform moves, same market pivots, same talent profiles.
When everyone zigs together, that's table stakes — not differentiation.]

### Gaps and White Space
[What none of them are covering. Segments underserved.
Capabilities nobody is building. Buyer needs unaddressed.]

### Tensions That Play Out Differently
[e.g., Company A chose scale over customization;
Company B chose the opposite. Who's winning, and for whom?]

### PM Implications Across the Set
[What a PM at each company would face differently.
Which org is better set up for discovery?
Which is most constrained by legacy?]
```

---

### Step 4: Handoff Menu

After producing the output, offer the user a handoff menu. Each option names what gets built and which skill or agent consumes the research:

"Your research is ready. What do you want to build from it?

1. **Competitive battlecard** — I'll structure a head-to-head comparison for your sales or strategy team
2. **SWOT analysis** — I'll run strengths, weaknesses, opportunities, and threats using the research as input
3. **Positioning statement** — Use `positioning-statement` skill with this company/market context loaded
4. **PESTEL assessment** — Use `pestel-analysis` skill with the trends and pressures from Sections 6 and 8
5. **Market sizing (TAM/SAM/SOM)** — Use `tam-sam-som-calculator` skill with the market and segment data from Sections 2-3
6. **Research prompts for deeper investigation** — Generate 3-5 targeted research prompts per lens for a follow-up session
7. **PM briefing memo** — Condense the 11 sections into a 1-page executive summary for a PM audience
8. **Workshop discussion guide** — Extract teachable tensions and case study angles for training use

Select a number, combine them (e.g., '1 and 4'), or describe what you need."

---

### Rerun Pattern (Executive Signal Refresh)

When the user reruns the skill on a previously researched entity — or asks for a quarterly refresh —
run it as a delta investigation, not a regeneration:

- **Read the prior output fully before searching**; diff against it. Focus web search on the period
  since (typically the last 90 days), prioritizing primary sources: earnings transcripts, filings,
  investor days, direct executive interviews. Quote executives *exactly* — never fabricate quotes,
  figures, or guidance.
- Lead with a **"What's Changed"** summary before any full sections. For each material shift, use the
  Then/Now form:
  - **Then:** what the prior run recorded
  - **Now:** the new signal — "exact quote or observation" (source, date, URL)
  - **Reading:** what this suggests for strategy or product (labeled Inference)
  - **Confidence:** high / medium / low
- Include a **Dropped Language** subsection: initiatives, phrases, or metrics the company *stopped*
  mentioning quarter over quarter. What leaders stop saying is often the strongest signal — a
  transformation program that vanishes from the earnings script died without a press release. Read
  earnings materials as strategy documents, not finance rituals: separating narrative shifts from
  metric shifts is the skill.
- In Section 9 (Strategic Signals), highlight delta from prior run: new hires, new patents, leadership moves
- Flag sections where nothing material changed: "No significant change since [prior date]" — and if
  the quiet is sustained across runs, note the quiet as its own signal.

The user does not need to say "refresh" — if the agent has prior output in context, it should default
to delta-first reporting. For monitoring a whole competitor *set* at lower depth, hand off to
[`competitive-intel-watch`](../competitive-intel-watch/SKILL.md); this refresh goes deep on one company.

## Examples

### Example: Single Company — Helix Motion Systems *(fictional, as are all companies in these examples)*

**Trigger:** "Run company-intel on Helix Motion Systems"

**Entry point:** Single Company

**Section 1 excerpt:**
Helix Motion Systems is a large diversified industrial manufacturer specializing in motion and control technologies. A century-old firm, it operates across two segments: Diversified Industrial (~85% of revenue) and Aerospace Systems (~15%). A recent multi-billion-dollar aerospace acquisition significantly expanded that second segment.

**Section 9 excerpt:**
- **Patents:** Clustering in electro-hydraulic controls and hydrogen fuel cell components. R&D investment in electrification outpacing public product announcements — signals a bet on industrial decarbonization. *(Source: Google Patents, 2024-2025 filings)*
- **Hiring:** Volume hiring for "digital twin" engineers and IoT platform architects in the Diversified Industrial segment. Job descriptions reference AWS IoT and Azure Digital Twins. *(Source: LinkedIn, Indeed — June 2026)*
- **Leadership:** New VP of Digital Transformation hired from a platform-oriented automation rival (2025). New Group President for Engineered Materials from a diversified conglomerate (2024). Pattern: importing talent from platform-first industrials. *(Source: company press releases)*

**Section 10 excerpt:**
PMs at Helix face the classic industrial tension: long product lifecycles (10-20 years) vs. pressure to digitize and create recurring-revenue service layers. Product management is historically engineering-led, not customer-led. Discovery is constrained by the fact that customers (OEMs, utilities, defense contractors) have long procurement cycles and low tolerance for experimentation. The hiring signals suggest a push toward platform thinking, but the org structure (segment-based P&Ls) creates incentives to optimize locally rather than build horizontal platforms. *Inference: the digital twin hiring is likely ahead of organizational readiness to consume it.*

---

### Example: Competitor Set — Industrial Motion Control

**Trigger:** "Compare Helix Motion, Northfield Automation, and Corvid Industrial on company-intel"

**Entry point:** Competitor Set (3 companies)

**Section 12 excerpt (Cross-Company Comparison):**

**Where They're Betting Differently:**
- Helix is investing heavily in electrification and hydrogen (patent evidence). Northfield is betting on software-defined automation (a major industrial-software acquisition). Corvid is splitting into three companies and doubling down on aerospace autonomy.

**Gaps and White Space:**
- None of the three have a credible PLG motion for their digital products — all rely on enterprise sales. A startup that cracks self-serve industrial IoT tooling could undercut all three on adoption speed.

**PM Implications Across the Set:**
- Helix PM = engineer-first, platform-curious but segment-siloed
- Northfield PM = software-led post-acquisition, navigating legacy OT culture
- Corvid PM = post-split identity crisis, aerospace PMs and industrial PMs now in different companies

---

### Anti-Pattern Example

**Weak:** "Helix Motion Systems makes industrial equipment and has strong financials."

**Strong:** Identifies the tension between Helix's motion-and-control platform business (recurring revenue, long service cycles) and its push into intelligent manufacturing and IIoT — and explains why that tension creates specific PM challenges around build-vs-partner decisions, aftermarket monetization, and the pace of digital product adoption in asset-intensive industries.

## Common Pitfalls

### Pitfall 1: Surface-Level Description Without Implications
**Symptom:** Summary reads like a Wikipedia article or press release.
**Consequence:** No actionable intelligence. Downstream skills get nothing useful.
**Fix:** Push every section toward "what does this mean for product decisions?" If a fact doesn't connect to a tension, tradeoff, or PM implication, it's not pulling its weight.

### Pitfall 2: Skipping Strategic Signals
**Symptom:** Analysis draws only from press releases and About pages. Sections 1-8 are solid; Section 9 is empty or generic.
**Consequence:** You're seeing what the company *says* it's doing, not what it's *actually* doing. Patents, hiring, and leadership changes are often the most honest signals available.
**Fix:** Always search patents, hiring, and leadership as a required step — even if the results are thin. "No significant patent activity found" is a signal too.

### Pitfall 3: Confusing Outputs With Outcomes
**Symptom:** Listing features or products without explaining what results they produce for customers or the business.
**Consequence:** Section 5 becomes a product catalog instead of strategic intelligence.
**Fix:** For every offer, answer: what problem does it solve, for whom, what outcome does it improve, and what behavioral change does it create?

### Pitfall 4: No Citations
**Symptom:** "The CEO said the company is focused on AI." No source, no date, no context.
**Consequence:** Unverifiable claims. Downstream consumers can't trust the research.
**Fix:** Cite source and date. "CEO Jane Doe stated X in Q1 2026 earnings call (Source: Seeking Alpha transcript, Feb 2026)."

### Pitfall 5: Treating All Industries as Identical
**Symptom:** Generic PM frameworks applied without domain calibration. "They should do more discovery" without acknowledging that discovery in defense contracting looks nothing like discovery in consumer SaaS.
**Consequence:** Section 10 is useless to anyone who actually works in the domain.
**Fix:** Identify what makes PM *different* in this specific domain — regulatory overhead, buyer/user separation, capital intensity, sales cycle length, service dependency.

### Pitfall 6: One-Time Exercise, Never Refreshed
**Symptom:** Intel gathered once, never updated. Decisions made on 18-month-old hiring signals.
**Consequence:** Stale intelligence is worse than no intelligence — it creates false confidence.
**Fix:** Set a rerun cadence (quarterly for active competitors, annually for industry context). When rerunning, lead with "What's Changed."

## Downstream Composition Guide

This section is for other skill authors and agent builders who want to consume company-intel output.

### What This Skill Produces

A structured markdown document with 11 numbered sections (12 for competitor sets). Each section has a stable heading and defined content type:

| Section | Content Type | Downstream Use |
|---------|-------------|----------------|
| 1. What This Entity Is | Entity definition, scale, market position | Context setting for any downstream skill |
| 2. How It Makes Money | Revenue, costs, margins, financial logic | `business-health-diagnostic`, `feature-investment-advisor` |
| 3. Who It Serves | Buyers, users, segments, stakeholder map | `proto-persona`, `jobs-to-be-done`, `positioning-statement` |
| 4. What It Sells or Delivers | Value propositions, core offers | `positioning-statement`, battlecards |
| 5. Key Product Lines | Product families, platforms, services | Competitive analysis, portfolio mapping |
| 6. Business and Market Pressures | Competitive, regulatory, technology forces | `pestel-analysis`, `derisk-measurement-advisor` |
| 7. Competitors and Alternatives | Direct, adjacent, substitutes, disruptors | Battlecards, competitive positioning |
| 8. Important Trends and Risks | Macro forces, AI impact, consolidation | `pestel-analysis`, `derisk-measurement-advisor` |
| 9. Strategic Signals | Patents, hiring, leadership changes | Competitive intelligence, trend analysis |
| 10. What This Means for PM | Org dynamics, discovery maturity, PM challenges | Workshop content, coaching, engagement prep |
| 11. Sources and Confidence | Citations, assumptions, data quality flags | Quality assurance for all downstream use |
| 12. Cross-Company Comparison | Divergence, convergence, gaps, tensions | Battlecards, SWOT, competitive strategy |

### How to Reference This Skill

In your skill's References section:
```markdown
- **[company-intel](../company-intel/SKILL.md)** (Workflow) — Run first to generate structured company/industry research; this skill consumes Sections [X, Y, Z] as input
```

### Passing Output to Downstream Skills

When handing off to a downstream skill, pass the relevant sections explicitly:
- **Battlecard** → Sections 4, 5, 7, 9, 12
- **SWOT** → Sections 2, 6, 7, 8, 9
- **Positioning** → Sections 3, 4, 7
- **PESTEL** → Sections 6, 8, 9
- **TAM/SAM/SOM** → Sections 2, 3, 5
- **Business health** → Sections 2, 5, 8
- **PM briefing** → Sections 1, 5, 9, 10
- **Workshop guide** → Sections 6, 9, 10 (tensions and PM implications)

## References

### Related Skills
- **[company-research](../company-research/SKILL.md)** (Component) — Lighter-weight company profile focused on executive quotes and product strategy; `company-intel` is deeper and broader, producing structured output for downstream consumption
- **[autonomous-investigation](../autonomous-investigation/SKILL.md)** (Workflow) — The evidence-label and confidence protocol this skill's research follows
- **[intelligence-collection-disciplines](../intelligence-collection-disciplines/SKILL.md)** (Component) — OSINT/FININT/HUMINT source tables and signal chains behind Lenses 1, 6, and 7
- **[competitive-intel-watch](../competitive-intel-watch/SKILL.md)** (Workflow) — Breadth sibling: monitors the whole competitor set on a cadence while this skill goes deep on one entity
- **[pestel-analysis](../pestel-analysis/SKILL.md)** (Component) — Deep PESTEL template; consumes Sections 6 and 8 from company-intel
- **[derisk-measurement-advisor](../derisk-measurement-advisor/SKILL.md)** (Interactive) — Risk scan that benefits from Sections 6 and 8 as context input
- **[tam-sam-som-calculator](../tam-sam-som-calculator/SKILL.md)** (Component) — Market sizing; consumes Sections 2, 3, 5
- **[business-health-diagnostic](../business-health-diagnostic/SKILL.md)** (Interactive) — SaaS health diagnosis; consumes Section 2
- **[positioning-statement](../positioning-statement/SKILL.md)** (Component) — Positioning; consumes Sections 3, 4, 7
- **[acquisition-channel-advisor](../acquisition-channel-advisor/SKILL.md)** (Interactive) — Go-to-market analysis; consumes Sections 2, 3, 7
- **[proto-persona](../proto-persona/SKILL.md)** (Component) — Persona creation; consumes Section 3

### Research Sources
- Company investor relations pages — Annual reports, earnings transcripts, forward-looking statements
- Patent databases — Google Patents, USPTO
- Job aggregators — LinkedIn, Indeed, Glassdoor (hiring signals)
- Industry analysts — Gartner, Forrester, IDC
- Regulatory filings — SEC (US), Companies House (UK), relevant sector regulators
- News coverage — Reuters, Bloomberg, industry-specific publications

### Provenance
- Adapted from Dean Peters' company-profile-executive-insights-research prompt and TAM-SAM-SOM prompt generator in the product-manager-prompts repo
- Incorporates the Seven Research Lenses framework developed for Productside enterprise PM training
