---
name: intelligence-collection-disciplines
description: "Run competitive research like an intelligence agency: eight collection disciplines (OSINT to MASINT), signal-to-inference chains, and fusion. Use when one-source research isn't enough."
intent: >-
  Give product managers the intelligence community's collection playbook: eight independent disciplines,
  each with free and paid sources, signal-to-inference chains, and the PM artifact it feeds — then fuse
  them with confidence stacking so three weak signals become one strong conclusion.
type: component
theme: market-intelligence
best_for:
  - "Choosing which collection channels to run for a competitive or market question"
  - "Turning raw public signals (patents, job posts, filings, web diffs) into defensible inferences"
  - "Cross-validating a suspected competitor move across independent evidence channels"
scenarios:
  - "I think a competitor is building a platform play — how do I confirm it before their launch?"
  - "My TAM slide got shredded — where do I find data that survives scrutiny?"
estimated_time: "reference skill; a single-discipline pass takes 30-60 min"
---

# Intelligence Collection Disciplines

## Purpose

Stop doing competitive research like a term paper. The intelligence community solved this problem
decades ago: they don't collect "data," they run **collection disciplines** — independent channels,
each with its own sources, tradecraft, and blind spots — and then they *fuse* them. This skill gives
product managers that playbook: eight disciplines, each telling you (1) what to collect, (2) where to
collect it, (3) which signal → inference chains to run, and (4) which PM artifact it feeds
(TAM/SAM/SOM, ICPs, personas, battle cards, roadmap bets, win/loss, positioning, pricing). One signal
is an anecdote; three correlated signals from independent disciplines is intelligence.

## Input

**Works best with** the six instantiation variables below — fill them once and every discipline
becomes engagement-specific. Leave them blank and this stays a teaching artifact.

~~~
[TARGET]      = The competitor, partner, or acquirer you're researching
[MARKET]      = The category and its NAICS/SIC/NACE codes (or nearest equivalent)
[GEOGRAPHY]   = Regions in scope, at COUNTRY level, not continent level
[BUYER]       = Who signs the check (drives review sites, job titles, conferences)
[CAPABILITY]  = The strategic move you suspect (platform play, market entry,
                pricing shift, compliance land-grab, etc.)
[DECISION]    = What this research will change (roadmap bet, positioning,
                pricing, market entry, deal defense, ICP refresh)
~~~

**If [DECISION] is blank, stop. Research without a decision is a hobby.**

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as variables already filled. Use it; don't re-ask.

**Arriving empty-handed? That works too.** Read the disciplines as a course in tradecraft, or ask the
agent to walk the instantiation block with you one variable at a time.

**Example invocation:** `Use intelligence-collection-disciplines — [TARGET]: Meridian Freight Systems,
[CAPABILITY]: suspected move into warehouse robotics, [DECISION]: whether we accelerate our own
integration roadmap.`

## Key Concepts

### The Eight Disciplines

| Discipline | Intel Community Name | Plain English | Primary PM Artifact |
|---|---|---|---|
| 1. OSINT | Open Source Intelligence | Press, social, periodicals, analysts | Battle cards, positioning |
| 2. FININT | Financial Intelligence | Filings, earnings calls, procurement | Battle cards, SOM capture rates |
| 3. GEOINT/DEMOINT | Geospatial & Demographic Intelligence | Census, labor, trade, economic statistics | TAM/SAM/SOM, ICPs, personas |
| 4. TECHINT | Technical Intelligence | Patents, technographics, changelogs | Roadmap bets |
| 5. HUMINT | Human Intelligence | Talent moves, employee chatter, win/loss | Roadmap bets, battle cards |
| 6. SIGINT | Signals Intelligence | Web diffs, pricing changes, job posts | Battle cards, pricing strategy |
| 7. MASINT | Measurement & Signature | Supply chain, ops indicators | Threat assessment |
| 8. All-Source Fusion | n/a | Cross-validation and confidence stacking | Everything above |

- **Independence is the design.** The disciplines matter because they fail differently: a press
  release can lie, but a customs record, a patent filing, and thirty job posts are three separate
  bureaucracies that would all have to be lying in the same direction.
- **Signal → inference chains** are the tradecraft: each observable signal maps to a bounded
  interpretation, labeled per the `autonomous-investigation` protocol (Fact / Inference / Assumption).
- **What this is NOT:** espionage. Every source below is published, filed, posted, or publicly
  observable. See Guardrails in Common Pitfalls.

## Application

### 1. OSINT — The Journalist's Desk

*What a good beat reporter knows before the press release drops.*

| Source Type | Free | Paid |
|---|---|---|
| [TARGET] press & newsroom | Company newsroom pages, Google Alerts, PR Newswire feeds | Meltwater, Cision |
| Industry periodicals | Trade publications, association newsletters, vertical Substacks for [MARKET] | Analyst subscriptions |
| Analyst coverage | Gartner/Forrester press summaries, free webinar replays | Gartner, Forrester, IDC full reports |
| Social & community | LinkedIn exec posts, Reddit, Hacker News, X | Brandwatch, Sprout listening |
| Review sites | Whichever your [BUYER] reads: G2, Capterra, TrustRadius, app stores, Trustpilot | G2 Buyer Intent data |
| Conference footprint | Session titles, sponsor tiers, booth size, speaker rosters at [MARKET] events | n/a |
| Prediction markets | Polymarket, Kalshi, Metaculus, Manifold (crowd-priced odds on regulation, approvals, tech milestones relevant to [MARKET]) | n/a |

**Signal → inference chains:**

- [TARGET] exec suddenly posting about a new problem space → positioning pivot incoming (execs test messaging on social 3-6 months before launch)
- Sponsor tier jump at a [MARKET] conference → market entry or doubling down
- Review complaints clustering on one feature → their roadmap pressure point = your battle card ammo
- Analyst briefing requests (visible via analyst posts) → category creation attempt
- Webinar topics shifting → what they're teaching the market is what they're about to sell
- Sudden silence on a product line → sunset in progress
- Prediction-market odds moving on a regulation or milestone that gates [MARKET] → crowd-priced expectations for scenario planning; treat as a leading indicator of consensus, not ground truth, and check liquidity before trusting the number

**Feeds:** battle cards (objection handling from review mining), positioning (their words vs. customer words gap), win/loss context.

### 2. FININT — The Forensic Accountant

*Follow the money. Companies lie in press releases. They lie less in filings, because lying there is a felony.*

| Source Type | Free | Paid |
|---|---|---|
| Public filings | SEC EDGAR (US), Companies House (UK), BRIS and European e-Justice company search (EU), national securities regulators for [GEOGRAPHY] | AlphaSense, Sentieo |
| Earnings calls | Company IR pages, Seeking Alpha transcripts | AlphaSense (search across calls) |
| Private company signals | Crunchbase free tier, incorporation records, insolvency registers, beneficial-ownership registers where legally accessible | PitchBook, CB Insights |
| Government spend & procurement | USAspending.gov, SAM.gov (US), TED and national procurement portals (EU), country platforms (MENA), development-bank procurement (World Bank, EBRD, AfDB, UNGM) | GovWin |
| Competition & state-aid cases | European Commission merger/antitrust/state-aid databases; national competition authorities | n/a |
| State & sovereign capital | Sovereign wealth fund reports, state-owned enterprise annual reports, PPP pipelines | n/a |

**Signal → inference chains:**

- **Risk Factors section changes year-over-year in an annual filing** → what genuinely scares them (they must disclose it)
- Segment reporting restructure → strategic reprioritization; follow which segment got promoted
- Earnings call Q&A dodges (analysts ask, execs deflect) → soft spot; probe it in your positioning
- New entity registrations or branches in [GEOGRAPHY] → market entry before any announcement
- Deferred revenue trends → actual sales momentum vs. stated momentum
- Merger filings → market definitions and named competitors, straight from [TARGET]'s own lawyers
- Sovereign fund or state-aid money backing [TARGET] → their runway math just changed; discount-pressure plays won't work
- Prior Information Notices and expressions of interest → tenders telegraphed 3-24 months out

**Feeds:** battle cards (financial stress = "they'll be desperate at quarter-end" plays), SOM capture
rates (their revenue ÷ claimed customer count = deal size reality check, feeding the GEOINT/DEMOINT
sizing recipe), account targeting (procurement award patterns).

### 3. GEOINT/DEMOINT — The Cartographer

*The terrain map, not troop movement. Government statistics are free intelligence most PMs never open —
and the backbone of every ICP, persona, and TAM that survives scrutiny.*

| Source Type | Free | Paid |
|---|---|---|
| US market structure | Census Bureau (County Business Patterns, Economic Census, NAICS establishment counts), BEA | IBISWorld, Statista, Grand View Research |
| US labor & buyers | BLS (occupation counts, wages, industry employment), FRED (macro conditions gating budgets) | TalentNeuron |
| EU market structure | Eurostat, PRODCOM manufacturing statistics, national statistical institutes, ECB data | national data resellers |
| EU trade flows | Eurostat COMEXT, Access2Markets, TARIC (tariffs, quotas, rules of origin) | Panjiva, S&P Global |
| MENA regional | GCC-Stat, Arab Development Portal, ESCWA, Arab Monetary Fund, SESRIC | n/a |
| MENA national | GASTAT (Saudi), FCSC (UAE), CAPMAS (Egypt), HCP (Morocco), and peers | n/a |
| Global cross-check | World Bank Data and Enterprise Surveys, IMF country reports, OECD.Stat, UN Comtrade, ITC Trade Map | n/a |

**Signal → inference chains:**

- Establishment counts by industry code and employee band → the denominator for bottom-up TAM
- Regional industry concentration → where your SOM actually lives, and where field sales should live
- Occupation growth curves for your [BUYER] roles → is the population you sell to growing or shrinking
- Wage trends in buyer roles → willingness-to-pay ceiling shifts; pricing corridor validation
- Firmographic distributions (size bands, legal forms, sectors) → ICP boundaries drawn from data, not vibes
- Buyer-title prevalence by [GEOGRAPHY] → persona localization; the "VP of Product" you message in Boston is a "Head of Digital" in Frankfurt and may not exist in Riyadh
- Trade-flow shifts in product-specific codes → market entry or supply relocation before any announcement

**The TAM/SAM/SOM Recipe (this discipline's signature dish):**

~~~
TAM: Establishment counts for [MARKET] (Census/NAICS, Eurostat/NACE,
     or national equivalent for [GEOGRAPHY])
     × employment/spend benchmarks (BLS, Eurostat, trade associations)
     (validate against two independent analyst reports; if they disagree by 3x, say so)

SAM: TAM filtered by your actual constraints: [GEOGRAPHY], segment, compliance
     requirements, tech prerequisites (see TECHINT technographics),
     local-content and vendor-registration eligibility where applicable

SOM: SAM × realistic capture rate derived from [TARGET] public filings via FININT
     (their revenue ÷ their claimed customer count = deal size reality check)
~~~

**Feeds:** TAM/SAM/SOM (the backbone — see `tam-sam-som-calculator`), ICP definition, personas,
messaging localization, market entry prioritization, pricing corridor validation.

### 4. TECHINT — The Patent Examiner

*R&D leaves fingerprints 12-18 months before products ship.*

| Source Type | Free | Paid |
|---|---|---|
| Patents | patents.google.com, USPTO Patent Center, EPO Espacenet, WIPO PatentScope | Clarivate, LexisNexis PatentSight+ |
| Technographics | BuiltWith free lookups, Wappalyzer | HG Insights, BuiltWith Pro, 6sense |
| Product telemetry | Public changelogs, API docs diffs, status pages, GitHub org activity | n/a |
| Standards bodies | Whichever govern [MARKET]: IETF, W3C, ISO committees, CEN/CENELEC/ETSI work programs, industry consortia | n/a |
| Funded research | CORDIS and Horizon Europe project databases, university project repositories | n/a |
| Academic & preprints | arXiv, Google Scholar, Semantic Scholar, SSRN, the conferences that matter to [MARKET] | Dimensions, Scopus |
| Trademark filings | USPTO TESS, EUIPO, WIPO Global Brand Database | Corsearch |

**Signal → inference chains:**

- Patent **clusters** (5+ filings in one classification in 12 months) → committed bet on [CAPABILITY], not exploration
- Inventor names repeating across filings → the actual product team behind the initiative; track their conference talks and LinkedIn
- Trademark filing for a product-sounding name → launch inside 6-12 months (trademarks are cheap; companies file close to launch)
- [TARGET] repeatedly appearing in funded consortia → their long-range bet, 12-48 months of lead time
- Research pilot sites → likely launch customers, named in public deliverables
- [TARGET] chairing a standards committee → they intend to shape the rules of [MARKET], not just play by them
- [TARGET]-affiliated authors publishing preprints → R&D direction 6-24 months before patents; a paper cluster plus a hiring surge in the same specialty is one of the strongest fusion pairs available
- Author affiliations shifting from university to [TARGET] on successive papers → they hired the lab, not just the idea
- API docs adding endpoints for an unreleased capability → beta program running now
- Your prospects' tech stacks (technographics) → your SAM refinement: who *can* actually buy you

**Feeds:** roadmap bets (where to accelerate vs. concede), SAM refinement, battle cards (feature-gap
countdown clocks), build/buy/partner decisions.

### 5. HUMINT — The Sports Scout

*Organizations announce strategy through job boards long before press releases. People are the tell.*

| Source Type | Free | Paid |
|---|---|---|
| Job postings | LinkedIn Jobs, [TARGET] careers pages, Indeed | JobsPikr, TalentNeuron, Revelio Labs |
| Employee sentiment | Glassdoor, Blind, Reddit communities for [MARKET] | n/a |
| Leadership moves | LinkedIn announcements, press | BoardEx, The Org |
| Win/Loss | Your own sales team debriefs, churned-customer interviews | Clozd, DoubleCheck |
| Conference hallway | Your field team's ears at [MARKET] trade shows | n/a |

**Signal → inference chains:**

- Hiring surge in one specialty (30+ postings in a quarter) → building [CAPABILITY], not a feature
- Regional specialist roles appearing for a [GEOGRAPHY] you haven't seen them in → expansion pre-announcement
- Job posts naming specific technologies → confirmed stack choices → integration roadmap intel
- Senior product/tech leader exits within 6 months of a strategy announcement → the strategy is in trouble
- Your own alumni landing at [TARGET] → assume they know your playbook
- Employee reviews mentioning "pivot," "reorg," "leadership churn" → 2 quarters of internal distraction = your window
- Win/Loss interviews: the only source that tells you *why* deals actually close (everything else is inference)

**Feeds:** roadmap bets (their build signals), battle cards (org instability plays), win/loss program
(ground truth for everything).

### 6. SIGINT — The Wiretap You're Allowed to Have

*Companies broadcast constantly through what they change on the public internet. Most competitors never listen.*

| Source Type | Free | Paid |
|---|---|---|
| Website diffs | Wayback Machine, Visualping free tier | Visualping, Klue, Crayon (auto-monitoring) |
| Pricing pages | Manual snapshots + Wayback | Klue, Crayon, Kompyte |
| SEO/SEM moves | Google "site:" queries, free Semrush lookups | Semrush, Ahrefs, SpyFu |
| App store metadata | Version notes, screenshot changes, keyword shifts | Sensor Tower, data.ai |
| DNS/infrastructure | crt.sh (new SSL certs reveal new subdomains), DNS records | n/a |
| Webinar/event cadence | [TARGET] events pages, registration platforms | n/a |

**Signal → inference chains:**

- New subdomain SSL cert (e.g., `[capability].[target].com`) → product launch staging, often weeks ahead
- Pricing page removes a tier → packaging overhaul, usually toward enterprise
- Sudden SEM bidding on *your* brand terms → they consider you the threat now (congratulations)
- Case study page pattern shifts (new vertical or [GEOGRAPHY] appearing) → segment push
- Messaging A/B visible via Wayback diffs → they're unsure of positioning; hit the wound

**Feeds:** battle cards (the freshest layer — this is what keeps cards from going stale), pricing
strategy, positioning counter-moves.

### 7. MASINT — The Satellite Photo

*Measure the physical and operational exhaust. Abnormal resource allocation never lies.*

| Source Type | Free | Paid |
|---|---|---|
| Supply chain | Import/export records via ImportYeti (free tier), Eurostat COMEXT and customs codes, UN Comtrade | S&P Global Supply Chain Intelligence, Panjiva, ImportGenius |
| Facilities & projects | Commercial real estate news, local business journals, permits in [GEOGRAPHY]; industrial-zone tenant announcements, environmental permits, EPC contract awards; satellite imagery | CoStar |
| Ops capacity | Support response time sampling, status page incident frequency | n/a |
| Certifications & safety | Whichever gate [MARKET]: ISO, SOC 2, FedRAMP, CE marks; notified-body designations and safety recalls (EU); sector registries | n/a |

**Signal → inference chains:**

- 20%+ volume change in critical inputs → pre-launch or demand collapse (check which via FININT)
- New supplier geographies or country-of-origin shifts → market entry, tariff hedging, or resilience play
- Compliance certification "in process" listings → 12-36 month runway into a regulated segment, visible to anyone who checks the registry
- Product recalls or repeated safety-alert patterns → quality strain; battle card ammunition with a public citation
- Land allocation, power/water capacity reservations, or engineering-design contracts preceding equipment procurement → facility buildout 6-36 months before any launch announcement
- Support response times stretching + hiring freeze in support roles → cash constraint or overwhelmed by growth (disambiguate via employee sentiment)
- Office consolidations → cost compression; expect pricing aggression to follow

**Note:** supply chain and facility signals are strongest for hardware and industrial players. The
software equivalent is ops capacity plus infrastructure-scale language in job postings.

**Feeds:** threat assessment, launch prediction and capacity estimates, battle cards (capacity-stretch
objections: "ask them about their support SLAs lately").

### 8. All-Source Fusion — The Situation Room

*One signal is an anecdote. Three correlated signals from independent disciplines is intelligence.*

Apply the **Confidence Stacking Rule** from the `autonomous-investigation` protocol: 1 discipline =
watch item; 2 = working hypothesis; 3+ = actionable intelligence; conflicting disciplines = someone is
bluffing — dig. And treat announcements as intent until funding, procurement, land, permits, hiring,
or contracts corroborate them: **ambition is OSINT; commitment shows up in FININT, MASINT, and HUMINT.**

**Fusion template — detecting [TARGET]'s [CAPABILITY] play:**

| Discipline | Signal (fill in what you found) |
|---|---|
| MASINT | Resource/input anomaly: ____ |
| TECHINT | Patent cluster or repo activity: ____ |
| HUMINT | Hiring pattern: ____ |
| SIGINT | Infrastructure or web change: ____ |
| FININT | Filing language, procurement award, or earnings dodge: ____ |
| GEOINT/DEMOINT | Terrain check: does the market they'd enter actually exist at the size the move implies? ____ |

**Fusion verdict:** ____ disciplines, one story → confidence level → recommended response.

**The fusion cadence:**

- **Weekly:** SIGINT sweep (site diffs, pricing, job posts). 30 minutes.
- **Monthly:** OSINT + HUMINT digest. Review mining, employee sentiment, conference intel.
- **Quarterly:** FININT + TECHINT deep pass. Filings, patents, procurement awards.
- **Annual + every TAM refresh:** GEOINT/DEMOINT pass. Statistics releases lag; sizing rot is slow but real.
- **Event-driven:** MASINT alerts, material filings, leadership exits. React within 48 hours.

### Mapping disciplines to PM artifacts

| Artifact | Primary Disciplines | Refresh Cadence |
|---|---|---|
| TAM/SAM/SOM | GEOINT/DEMOINT + FININT (capture rates) + TECHINT (technographics) | Annual, plus event-driven |
| ICPs & Personas | GEOINT/DEMOINT + HUMINT (win/loss ground truth) | Semi-annual |
| Messaging & localization | GEOINT/DEMOINT + OSINT | Semi-annual |
| Battle cards | SIGINT + OSINT + HUMINT (win/loss) | Weekly SIGINT layer, monthly rebuild |
| Roadmap bets | TECHINT + HUMINT | Quarterly |
| Positioning | OSINT + FININT (earnings language) | Semi-annual |
| Pricing strategy | SIGINT + FININT + GEOINT/DEMOINT (wage/WTP corridors) | Event-driven |
| Threat assessment | All-Source Fusion | Quarterly brief + event-driven |

### Regional note

The disciplines do not change across markets; the sources do, and so does the evidentiary burden. Two
lessons that generalize: in rich-disclosure systems (EU), the challenge is finding the right record in
a fragmented landscape — no single portal holds it all. In announcement-heavy markets (MENA), the
challenge is separating national ambition from funded, procured, permitted commitment — and an
announced budget, an approved budget, committed financing, a tender value, and an awarded contract are
five different numbers wearing the same headline. Search in local languages; never assume the English
portal contains every notice.

## Examples

**Illustrative fusion fill (all names fictional):** you suspect [TARGET] = Meridian Freight Systems is
building a warehouse-robotics platform. The sweep finds: +20% specialized component orders in customs
records (**MASINT**, Fact), 15 new filings in one robotics patent class (**TECHINT**, Fact), 30+
platform engineers hired in a quarter (**HUMINT**, Fact), a new `robotics.meridianfreight.com` SSL
cert (**SIGINT**, Fact), the CFO dodging an analyst's capex question (**FININT**, Inference), and
establishment counts confirming the addressable segment supports the investment math
(**GEOINT/DEMOINT**, Fact). Six disciplines, one story: high-confidence platform threat. Response:
accelerate your own platform roadmap and arm sales with a maturity battle card *before* their launch,
not after.

**Single-discipline quick win:** your battle card claims a competitor is "financially strong." One
FININT pass finds deferred revenue declining three quarters straight while claimed customer count grew
— **Inference:** deal sizes are shrinking. The card gains a quarter-end discount-pressure play, with
the filing URL attached.

## Common Pitfalls

- **Feature-matching theater.** The goal is never "they shipped X so we ship X." Signals inform
  decisions about *outcomes* — "this changes which customer problem wins the next investment."
- **Single-discipline conviction.** A hiring surge alone is a watch item, not a strategy brief.
  Escalate confidence only as independent disciplines corroborate — that's the stacking rule.
- **Announcement inflation.** Re-planning your roadmap around a press release. Ambition is OSINT;
  wait for the money, the permits, or the hires.
- **Unsourced claims.** A battle card assertion without a source and date is an opinion wearing a
  badge. Document provenance on every claim; archive source documents at collection time, because
  portals restructure and files get replaced.
- **Crossing the line.** Pretexting, soliciting NDA-protected information, hiring someone specifically
  to extract their former employer's secrets, scraping against terms you agreed to — all off-limits.
  Everything in this skill is published, filed, posted, or publicly observable. The stage test: if
  you'd be uncomfortable explaining your method at [TARGET]'s user conference, don't use it.
- **Running every discipline on every question.** The artifact-mapping table exists so you run the two
  or three disciplines that feed your [DECISION], on the cadence that matches how fast that evidence
  actually changes.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the protocol that
  labels and stacks what these disciplines collect
- [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md) (Component) — consumes the
  GEOINT/DEMOINT sizing recipe
- [`company-research`](../company-research/SKILL.md) and [`company-intel`](../company-intel/SKILL.md)
  — single-company deep dives built largely on OSINT + FININT + HUMINT
- Investigation skills that run these disciplines: `market-landscape-scan`,
  `competitive-research-snapshot`, `competitive-intel-watch`, `battle-card-builder`
- SCIP Code of Ethics — the competitive-intelligence profession's reference standard
- Regional Source Overlays (EU/MENA companion; planned as a future component skill)
- Adapted from Dean Peters' "Competitive Research on Steroids" compendium and the Competitive Analysis
  Playbook (Productside).
