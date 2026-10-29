# Paidar — User Stories

Stories are written from the roles in the project charter, plus the portfolio reviewer and the developer. Every story traces to the functional requirements in `docs/requirements.md`. Thresholds and delays are named after their configuration parameters in `docs/business_rules.md`, so a default can change without rewriting a story.

FR-13 (Could) has no story yet. It gets one if it moves up in priority.

## Accountant

| ID | Story | Acceptance criteria | Priority | FR |
|---|---|---|---|---|
| US-01 | As the accountant, I want to load the invoice export, bank statement and cash/cheque log in one run, so that I stop copying data between spreadsheets. | Given the three files are in the input folder, when I run the load, then every row is stored with its source file and load time.<br>The run summary shows the rows loaded and the rows rejected, by reason. | Must | FR-01, FR-04 |
| US-02 | As the accountant, I want bad rows rejected with a reason, so that one bad record does not stop the whole load. | Given a row with a missing amount, an unsupported currency or an unparseable date, when the file is loaded, then the row appears in quarantine with a reason code and the run continues.<br>Valid rows in the same file are loaded. | Must | FR-02 |
| US-03 | As the accountant, I want reloading a file to be safe, so that I can rerun after a failure without creating duplicates. | Given a file that was already loaded, when I load it again, then no duplicate invoices or payments are created.<br>A row with an existing invoice number but different data is quarantined as a conflicting duplicate. | Must | FR-03 |
| US-04 | As the accountant, I want payments that quote a valid invoice number matched automatically, so that I do not match them by hand. | Given a payment that references an open invoice, with an amount within the match tolerance of its open balance, when matching runs, then the payment is matched and the invoice is closed.<br>The rule ID, confidence and timestamp are stored. | Must | FR-05, FR-12 |
| US-05 | As the accountant, I want partial payments and overpayments handled correctly, so that balances stay accurate. | Given a payment below the open balance, then the balance is reduced and the invoice stays open as partially paid.<br>Given a payment above the open balance, then the invoice is closed, the excess is recorded as unapplied credit, and the payment is flagged for review. | Must | FR-06 |
| US-06 | As the accountant, I want payments with no reference matched when only one invoice fits, so that less lands in the queue. | Given a known customer with exactly one open invoice whose balance is within the match tolerance of the amount, then the payment is matched with confidence "inferred".<br>Given no candidate or several candidates, then the payment goes to the queue with a reason code. | Must | FR-08 |
| US-07 | As the accountant, I want LBP payments converted at the right rate, so that mixed-currency payments reconcile. | Given an LBP payment, when it is matched, then it is converted at the latest rate on or before the payment date, and the rate and the USD amount are stored.<br>Given no rate on or before that date, then the payment goes to the queue as a missing rate. | Must | FR-09 |
| US-08 | As the accountant, I want one queue of exceptions with the reason and the candidate invoices, so that I only handle what the system could not decide. | Given an unmatched or ambiguous payment, then it appears in the queue with a reason code and any candidate invoices.<br>A payment that was matched automatically never appears in the queue. | Must | FR-10 |
| US-09 | As the accountant, I want to see why any payment was matched the way it was, so that I can trust and audit the system. | Given any matched payment, then I can see which rule applied, the confidence, when it happened, and whether the system or a person decided. | Must | FR-12 |
| US-10 | As the accountant, I want one payment split across several invoices when its narration lists them and the amounts agree, so that multi-invoice payments need no manual work. | Given two or more referenced open invoices of one customer whose open balances add up to the payment within the match tolerance, then each invoice is closed and the payment is allocated to them.<br>If the amounts do not add up, then the payment goes to the queue. An allocation is never guessed. | Should | FR-07 |
| US-11 | As the accountant, I want suggested matches for references with typos, so that near-misses are quick to resolve. | Given a reference that is a close but inexact match for exactly one open invoice, then a suggestion with its similarity score appears in the queue.<br>A suggestion below the automatic threshold is never applied without a person. | Should | FR-11 |

## Collections clerk

| ID | Story | Acceptance criteria | Priority | FR |
|---|---|---|---|---|
| US-12 | As the clerk, I want a daily worklist of overdue invoices by priority, so that I know whom to follow up first. | Given the daily run has finished, then overdue invoices are listed by days past due and amount, with the last reminder stage and its date.<br>The list reflects payments received before the run. | Must | FR-15 |
| US-13 | As the clerk, I want reminders sent automatically on the agreed schedule, so that none are forgotten or inconsistent. | Given an invoice that has reached the stage-1 delay, then a stage-1 reminder is sent; given the stage-2 delay, a stage-2 reminder.<br>Reminders are sent by the scheduled run on business days and delivered to the local inbox. | Must | FR-19, FR-20 |
| US-14 | As the clerk, I want no pointless or duplicate reminders, so that customers are not annoyed. | Given an invoice that was paid before sending, a balance below the minimum reminder balance, or a stage already sent, then no reminder is sent and the skip reason is logged.<br>Given an invoice first seen past several thresholds, then only the highest applicable customer-facing stage is sent. | Must | FR-20, FR-21 |
| US-15 | As the clerk, I want every reminder recorded, so that I can see what was sent and what happened next. | Given any send attempt, then the log shows the invoice or invoices, the stage, the recipient, the time, the status and the attempt number. | Must | FR-22 |
| US-16 | As the clerk, I want one message per customer per day, so that a customer with several overdue invoices gets one email. | Given two invoices of one customer that reach a stage on the same day, then one message lists both.<br>The log keeps one row per invoice. | Should | FR-23 |
| US-17 | As the clerk, I want failed sends retried and persistent failures flagged, so that nothing is lost silently. | Given the mail server is down, then the send is retried with the configured delays, then marked failed, and a follow-up task is created.<br>The owner's inbox receives a failure notice. | Should | FR-25, FR-26 |

## Owner

| ID | Story | Acceptance criteria | Priority | FR |
|---|---|---|---|---|
| US-18 | As the owner, I want total AR, the overdue percentage and DSO at a glance, so that I know how much cash is stuck. | Given an as-of date, then the dashboard shows these three values using the definitions in `docs/kpi_definitions.md`, and displays the as-of date. | Must | FR-14, FR-17 |
| US-19 | As the owner, I want to see who owes the most overdue money and for how long, so that I know whom to call. | Then I can see customers ranked by overdue amount, with aging buckets and the age of the oldest invoice, in three clicks or fewer. | Must | FR-15, FR-17 |
| US-20 | As the owner, I want the DSO trend by month, so that I can tell whether collection is improving. | Then a monthly DSO trend is shown, with its formula one click away, and it matches the KPI definition. | Must | FR-14, FR-17 |
| US-21 | As the owner, I want to see unmatched payments and reminder activity, so that I know what needs attention and what the system did. | Then the dashboard shows the count and value of payments awaiting review, and the reminders sent per day with their outcome. | Must | FR-10, FR-17, FR-22 |
| US-22 | As the owner, I want a notice when an invoice reaches the stage-4 delay, with a credit-review recommendation, so that I can decide on credit terms. | Given an invoice reaches that delay, then I receive one notice. Nothing is blocked automatically. | Should | FR-24 |
| US-23 | As the owner, I want customers grouped into risk segments, so that follow-up goes where it matters. | Given enough payment history, then each customer is Green, Amber or Red according to the segment rules. Others show as "Insufficient history". | Should | FR-16 |

## Sales rep

| ID | Story | Acceptance criteria | Priority | FR |
|---|---|---|---|---|
| US-24 | As a sales rep, I want to see my customers' overdue balances, so that I am not surprised on a visit. | Given I filter by my name, then I see overdue balances and aging for my customers only. | Should | FR-18 |
| US-25 | As a sales rep, I want a notice when one of my customers reaches the stage-3 delay, so that I can step in early. | Given an invoice reaches that delay, then I receive one notice, and a follow-up task exists for the clerk. | Should | FR-24 |

## Reviewer and developer

| ID | Story | Acceptance criteria | Priority | FR |
|---|---|---|---|---|
| US-26 | As a portfolio reviewer, I want to run the demo from a documented sequence of steps with no paid accounts, so that I can evaluate the project quickly. | Given a clean clone and the README, then a working dashboard with sample data is reachable in the time set by NFR-02, with no accounts, credentials or payment. | Must | FR-28 |
| US-27 | As the developer, I want a seeded generator with configurable defect rates, so that results are repeatable. | Given the same seed and configuration, then identical files are produced.<br>A manifest counts each injected defect type, so tests can check that every type is detected. | Must | FR-27 |
| US-28 | As the developer, I want proof that the automation survives failures, so that I can show it is reliable. | Given a stopped mail server, an API error or a malformed input file, then the failure is logged, retried or quarantined, and no duplicate reminder is produced. | Should | FR-21, FR-25, FR-26 |
| US-29 | As the developer, I want a baseline-versus-automated comparison with low, base and high cases, so that I can report the impact honestly. | Then the comparison uses the assumptions in `docs/discovery.md` and labels every result as simulated. | Should | FR-29 |
