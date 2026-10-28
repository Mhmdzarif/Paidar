# Paidar — Project Charter

| | |
|---|---|
| **Project** | Paidar (pronounced "PAY-dar"): receivables intelligence and collections automation for SMEs |
| **Author / owner** | Mohamad Zarif |
| **Version** | 1.0 (Milestone 0 draft) |
| **Date** | 23 October 2026 |
| **Status** | Draft, to be reviewed at the end of Milestone 1 |
| **Nature of the project** | Portfolio project. Fictional company, synthetic data, simulated results. Not a commercial product. |

## The short version

- **Why Paidar exists:** small and mid-sized businesses that sell on credit often cannot see, quickly and reliably, who has paid, who is late, and whom to chase. Paidar shows how that problem can be fixed with clean data, tested business rules and auditable automation.
- **Who it helps:** the owner (cash visibility), the accountant (less manual reconciliation), the collections clerk (a prioritised worklist and consistent reminders), and sales reps (early warning on their customers).
- **How we will know it works:** by automated tests on synthetic data with known answers (matching accuracy, data-quality checks, rule correctness, failure recovery), by a documented baseline-versus-automated comparison clearly labelled as simulated, and by a demo that anyone can reproduce for $0. Section 7 lists every measure.

---

## 1. Problem Statement

**Problem in one sentence.** Businesses that sell on credit cannot quickly and reliably see who has paid, who is late and whom to chase, because payments arrive through several channels, reconciliation is manual and follow-up is ad hoc.

**What this causes**

- Cash stays tied up in overdue invoices.
- The accountant's time goes on matching payments by hand.
- Mistakes creep in: payments applied to the wrong invoice, or not applied at all.
- Chasing is inconsistent, so some customers are reminded too late and others too often.
- The owner decides on stock, supplier payments and credit limits without a trusted picture of what is owed.

**External evidence (context, not proof).** The QuickBooks 2026 Small Business Late Payments Report found that 59% of surveyed US small businesses had invoices overdue by 30 days or more, up from 47% a year earlier. Businesses with unpaid invoices were owed about $17.7K on average, and 39% said a late payment had made it hard to cover payroll or bills in the past year. Businesses on net-30 terms were more likely to have overdue invoices (55%) than those on immediate terms (26%).
*Caveats:* the sample is US-only, and the survey was commissioned by Intuit QuickBooks, a vendor with a product interest. It is used here as context. It does not prove the problem exists at Atlas Trading or in Lebanon.
*Sources:* https://quickbooks.intuit.com/r/small-business-data/small-business-late-payments-report-2026/ and, for the net-30 comparison, the republished version at https://stacker.com/stories/small-business/report-finds-more-small-businesses-are-carrying-overdue-invoices-last-year

**Local context (assumption to validate in Milestone 1).** In Lebanon, B2B prices are often quoted in USD while part of the payment may be settled in LBP. The exchange rate has been stable near 89,500 LBP per USD (Trading Economics reported 89,502 on 3 April 2026; the World Bank figure for 2025, as republished by statisticsoftheworld.com, is 89,500). Paying USD invoices partly in LBP adds conversion, rounding and partial-payment cases to reconciliation. Paidar treats currency as a generic, configurable multi-currency feature (USD, LBP, EUR) so the design also fits Gulf and remote-employer contexts.
*Sources:* https://tradingeconomics.com/lebanon/currency and https://statisticsoftheworld.com/country/lebanon/PA.NUS.FCRF

**Hypothesised root causes (to be tested in Milestone 1)**

| ID | Hypothesis |
|---|---|
| RC-1 | Invoices, bank statements and the cash/cheque log live in three disconnected sources, so every match is manual. |
| RC-2 | There is no written rule for who is chased, when, by whom and how. |
| RC-3 | Aging and DSO are not defined or calculated consistently, so nobody trusts the numbers. |
| RC-4 | Payment references are missing or malformed in many bank narrations and cash entries. |
| RC-5 | Sales reps have no routine visibility of their customers' overdue balances. |

---

## 2. Fictional Company Profile

> **Atlas Trading is entirely fictional.** All data are synthetic. Any resemblance to a real company is coincidental.

| Attribute | Profile |
|---|---|
| Business | Wholesale distributor of packaged food and household goods, based in Beirut |
| Size | About 25 employees: 1 owner/GM, 1 accountant, 1 collections/admin clerk, 4 sales reps, about 18 warehouse and delivery staff |
| Customers | About 180 active B2B accounts (mini-markets, supermarkets, restaurants, cafés) |
| Volume | About 3,000 invoices over 18 months (about 170 per month); average invoice about $450, with a few large accounts dominating |
| Currency | Invoices issued in USD; payments received in USD or LBP, converted at a configurable reference rate (starting value 89,500 LBP/USD) |
| Credit terms | Net 15 for new customers, net 30 for most, net 45 for the largest accounts |
| Payment methods | Bank transfer (USD or LBP), cash collected by sales reps, cheque |
| Current tools | Accounting package that exports invoices to CSV/Excel; bank portal that exports statements to CSV; a cash-and-cheque log in Excel; phone and WhatsApp for chasing |
| Receivables team | The accountant (reconciliation, part of their week) and the collections clerk (chasing) |

**Current process (summary; mapped in detail in Milestone 1)**

1. An invoice is issued in the accounting system.
2. The customer pays by bank transfer, cash or cheque.
3. The accountant downloads the bank statement weekly, copies it into Excel and matches payments to invoices by hand.
4. Cash and cheques are recorded in a separate log.
5. The clerk phones or messages overdue customers when time allows.
6. When the owner asks "who owes us money?", someone builds an ad hoc spreadsheet.

**Data problems the generator will simulate**

Duplicate rows, mixed date formats, typos in invoice references, missing references, partial payments, one payment covering several invoices, overpayments, credit notes, unapplied cash, and USD/LBP mixing.

---

## 3. Objectives

All business objectives apply to the fictional scenario and are **simulated**. They are targets to be tested, not results.

### Business objectives (Atlas Trading, simulated)

| ID | Objective | Measure | Target |
|---|---|---|---|
| BO-1 | Cut the time spent on payment reconciliation | Modelled manual minutes (baseline from Milestone 1) versus automated runtime plus manual-review minutes | At least 70% reduction, reported with low/base/high assumptions |
| BO-2 | Give the owner a trusted, current picture of receivables | Wall-clock time for one full pipeline run on the demo dataset | Under 5 minutes |
| BO-3 | Make follow-up consistent | Reminder log compared with the business-rules catalogue | 100% of overdue invoices receive the correct reminder stage within 1 business day of crossing the threshold |
| BO-4 | Estimate the effect on days to collect (DSO) | Simulation with documented assumptions | A low/base/high range, never a single-point claim |

### Project objectives (portfolio)

| ID | Objective | Target |
|---|---|---|
| PO-1 | Deliver on schedule | Phase 1 by week 5, Phase 2 by week 8, Phase 3 by week 10 (± 1 week) |
| PO-2 | Produce the full business-analysis document set | Complete by the end of Milestone 2 |
| PO-3 | Make the project reproducible | A clean clone reaches a working demo in 15 minutes or less |
| PO-4 | Stay within budget | $0 spent, no payment details entered anywhere |

---

## 4. Scope

### In scope

**Phase 1 (core, weeks 1–5)**

- Seeded synthetic-data generator with injected defects
- Ingestion and validation, with a quarantine table for rejected rows
- PostgreSQL schema (raw, staging, core)
- Matching engine: exact reference, then customer plus amount
- SQL marts: aging, DSO, overdue rate, customer risk segments
- Dashboard that answers the owner's five questions (below)
- One automated daily reminder workflow, with a local inbox
- Business-analysis documents, tests, README

**Phase 2 (advanced, weeks 6–8)**

- Fuzzy matching with a manual-review queue
- Escalation workflow, retries, an error-handling workflow and idempotency
- Baseline-versus-automated impact simulation and a Jupyter analysis
- Continuous integration, test report, optional Power BI report

### Out of scope

| Item | Reason |
|---|---|
| Predictive ML or LLM features | Models trained on synthetic data only learn the generator's rules, so they would prove nothing. Risk scoring stays rule-based and explainable. |
| WhatsApp, SMS or real email sending | Needs paid or credentialed services; reminders are demonstrated in a local inbox. |
| Connectors to real accounting software | Needs real accounts or sandboxes; the project uses file exports. |
| Cloud deployment | Billing risk; the demo is local and reproducible. |
| Logins, roles and a custom web interface | No added value for the central problem; the dashboard tool is enough. |
| Mobile app | Not relevant to the problem. |
| Real customer data | Privacy; all data are synthetic. |
| Tax, legal or accounting-compliance advice | Not a compliance product; Paidar does not move money or issue legal invoices. |

**The owner's five questions (the dashboard's job)**

1. How much is owed in total, and how much of it is overdue?
2. Which customers owe the most overdue money, and for how long?
3. Is DSO improving or getting worse month by month?
4. Which payments could not be matched to an invoice?
5. Which reminders were sent, to whom, and what happened next?

**Scope control.** Phase 1 scope is frozen after Milestone 2. Any change is written into the change log at the end of this charter before work starts. New ideas go to a parking-lot list in the backlog.

---

## 5. Stakeholders

These are role-based personas inside the fictional company, plus the secondary audience of the portfolio. They are drafts, to be deepened with a power/interest analysis in Milestone 1.

| Stakeholder | Role | What they need | Influence | Interest |
|---|---|---|---|---|
| Owner / General Manager | Decision-maker, sponsor | A trusted view of cash owed and overdue; early warning on risky customers | High | High |
| Accountant | Primary user | Fast, accurate reconciliation; fewer spreadsheet errors; an audit trail | Medium | High |
| Collections / admin clerk | Primary user | A prioritised daily worklist; reminders that go out consistently; a record of every contact | Medium | High |
| Sales reps (4) | Secondary user | To know when their customers are overdue before a visit, and to avoid awkward surprises | Medium | Medium |
| Customers (B2B accounts) | Indirectly affected | Clear, correct, polite reminders; no reminders for invoices already paid | Low | Medium |
| Bank / accounting-system exports | Data sources | Stable file formats (an assumption) | Low | Low |
| Developer (Mohamad Zarif) | Project owner and builder | A finished, honest, reproducible project | High | High |
| Portfolio reviewers (recruiters, hiring managers) | Secondary audience | Evidence of analysis, engineering and clear communication, and a demo they can run for free | Medium | Medium |

---

## 6. Assumptions and Constraints

### Assumptions

Every assumption below is **unvalidated** until Milestone 1. Each will be given a range and tested for sensitivity.

| ID | Assumption | How it will be handled |
|---|---|---|
| A-01 | Manual reconciliation takes about 3–5 minutes per payment. | Used for the manual baseline; range tested in sensitivity analysis. |
| A-02 | Chasing one overdue invoice manually takes about 5 minutes (lookup, call or message, note). | Same. |
| A-03 | In the baseline period, about 10–15% of invoices are paid more than 30 days late. | Generator parameter, documented and varied. |
| A-04 | A meaningful share of bank narrations (about 20–30%) have missing or malformed invoice references. | Generator parameter, documented and varied. |
| A-05 | Customers pay in USD and LBP; the reference rate is configurable (starting value 89,500 LBP/USD). | Stored in an `fx_rates` table; open question Q-01 below. |
| A-06 | The company's systems can export invoices and statements as CSV/Excel. | Stated in the data dictionary. |
| A-07 | Standard aging buckets apply: current, 1–30, 31–60, 61–90, 90+ days past due. | Confirmed against common accounting practice; documented in KPI definitions. |
| A-08 | One developer works about 10–12 hours per week for about 10 weeks. | Drives the phasing in section 4. |

### Constraints

- **Budget: $0.** No paid software, APIs, trials, cloud services or courses, and no payment details entered anywhere.
- **Local-first and reproducible.** Everything runs on one Windows 11 machine (16 GB RAM, 6 cores), and recruiters can reproduce it without accounts or credentials.
- **Synthetic data only.** No real people, companies or transactions.
- **Deterministic rules.** No paid or metered AI services.
- **Licences.** Every tool is recorded in `docs/COST_LOG.md` with its licence, version and date checked. Any change in licence or pricing triggers a replacement before work continues.
- **Public repository,** so recruiters can read the work.

### Open questions

| ID | Question | To be answered in |
|---|---|---|
| Q-01 | Which exchange rate applies to which transaction (market rate, central-bank rate, customer-agreed rate)? | Milestone 1 |
| Q-02 | Are the credit terms and aging buckets above typical for Lebanese distributors? | Milestone 1 (optional practitioner conversations) |
| Q-03 | How common are cheques and cash compared with bank transfers? | Milestone 1 |

---

## 7. Success Criteria

"Works" means **verified on synthetic data with documented assumptions**. These criteria demonstrate engineering correctness and method. They do not claim real-world performance or real company results.

| ID | Criterion | How it is measured | Target | Phase |
|---|---|---|---|---|
| SC-1 | Reproducible demo | Timed run from a clean clone, following only the README | 15 minutes or less; zero paid accounts | 3 |
| SC-2 | Matching accuracy | Automatic matches compared with the generator's ground-truth labels | Precision of at least 95%; recall and share sent to manual review reported honestly | 1–2 |
| SC-3 | Data-quality coverage | One automated test for each injected defect type | 100% of defect types detected | 1 |
| SC-4 | Rule correctness | Business-rules catalogue checked against tests; coverage report on matching and rules modules | Every rule has at least one passing test; coverage of at least 80% on those modules | 1–2 |
| SC-5 | Automation reliability | Fault-injection tests: mail server down, API returns an error, malformed input file | Failures logged and retried; zero duplicate reminders; recovery without manual database edits | 2 |
| SC-6 | Dashboard usefulness | Walk-through of the owner's five questions | Each answered in three clicks or fewer | 1 |
| SC-7 | Reconciliation effort | Modelled manual minutes versus automated runtime plus manual review (BO-1) | At least 70% reduction, as a low/base/high range, labelled simulated | 2 |
| SC-8 | Reminder consistency | Reminder log versus the rules catalogue over the simulated period (BO-3) | 100% of overdue invoices get the correct stage within 1 business day | 1–2 |
| SC-9 | Documentation | Checklist of: requirements document, 20 or more user stories with acceptance criteria, as-is and to-be process maps, ERD, data dictionary, architecture diagram, KPI definitions, test report, case study, 3-minute demo video | All present and linked from the README | 1–3 |
| SC-10 | Cost | Review of `docs/COST_LOG.md` | $0 spent; every tool shows "Payment details: No" | All |
| SC-11 | Schedule | Dates on closed milestone issues | Phase 1 by week 5, Phase 2 by week 8, Phase 3 by week 10 (± 1 week) | All |

---

## 8. Top Three Risks

| # | Risk | Likelihood | Impact | Early warning sign | Mitigation |
|---|---|---|---|---|---|
| R-1 | **Scope creep** (adding tools and features that delay a finished project) | High | High | A milestone takes more than 1.5 times its planned time; new tools appear that are not in the plan | Freeze Phase 1 after Milestone 2; record changes in the change log; keep a parking-lot list; use a definition of done for every milestone |
| R-2 | **Synthetic-data credibility** ("you built the data to fit your solution") | Medium | High | Results look too good, such as 100% matching | Document generator assumptions and randomness; inject noise and hard cases (partial, multi-invoice and over-payments); keep a hard-case set that is not used for tuning; report recall and manual-review share honestly; never claim real-world accuracy or ROI; optionally check the analytics on the CC BY 4.0 Online Retail II dataset for realistic invoice patterns |
| R-3 | **Domain-knowledge gap and unvalidated assumptions** about receivables practice and Lebanese payment habits | Medium | High | I cannot explain a KPI or rule in plain language; assumptions have no source | Do an accounts-receivable primer and a competitor scan in Milestone 1; keep an assumption log with ranges and a sensitivity analysis; optionally talk to one or two accountants and report them only as discovery input; label anything unvalidated |

**Watch list (not top three):** a tool changing its licence or pricing (mitigated by the dated cost log and a fallback for each tool); fragile automation workflows (logic lives in tested code, the workflow tool only orchestrates); machine resource limits (monitor memory as services are added); time and motivation (public commit history and small milestones).

---

## Document control

| Version | Date | Change |
|---|---|---|
| 1.0 | 23 October 2026 | Initial draft for Milestone 0 |

**Next review:** end of Milestone 1. Charter changes are recorded in the change log above.