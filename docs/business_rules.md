# Paidar — Business Rules

These rules are the single source of truth for the code (Milestones 4–8) and for the tests. Thresholds, delays and schedules are **configuration, not hard-coded values**. The defaults below are scenario choices, not facts about Lebanese business practice.

## 1. Configuration defaults

| Parameter | Default | Used by |
|---|---|---|
| `match_tolerance_usd` | 1.00 | BR-M1 to BR-M5, BR-C4 |
| `min_reminder_balance_usd` | 5.00 | BR-R4 |
| `reminder_delay_days` (days after due date) | stage 1 = 1, stage 2 = 7, stage 3 = 14, stage 4 = 30 | BR-R2 |
| `reminder_run_time` | 08:00, Asia/Beirut | BR-R1 |
| `business_days` | Monday to Friday | BR-R1, BR-R2 |
| `terms_days` by customer | 15, 30 or 45 | BR-A1 |
| `fx_default_rate` | 89,500 LBP per USD | BR-C2 |
| `fuzzy_auto_threshold` | 0.95 | BR-M8 |
| `fuzzy_suggest_threshold` | 0.80 | BR-M8 |
| `retry_attempts` and `retry_delays` | 3 attempts, delays of 1, 5 and 15 minutes | BR-R8 |
| `risk_window_months` | 6 | BR-S1 |
| `risk_min_paid_invoices` | 3 | BR-S1 |
| `risk_avg_delay_days` | green up to 5, amber up to 15 | BR-S2 |
| `risk_overdue_age_days` | green up to 30, amber up to 60 | BR-S2 |

## 2. Validation rules

A row that fails any rule goes to the quarantine table with the reason code shown. The load continues with the remaining rows.

| ID | Rule | Reason code |
|---|---|---|
| BR-V1 | Required fields must be present. Invoices: invoice number, customer, invoice date, terms, amount, currency. Payments: payment date, amount, currency, source. | `missing_field` |
| BR-V2 | Amounts must be numeric and greater than zero. A credit note is a separate record that carries a positive amount and reduces the balance of its linked invoice. | `bad_amount` |
| BR-V3 | Accepted date formats are YYYY-MM-DD and DD/MM/YYYY. Anything else, or a date after the as-of date, is rejected. | `bad_date`, `future_date` |
| BR-V4 | Invoices must be in USD. Payments must be in USD or LBP. Other currencies can be enabled in configuration. | `unsupported_currency` |
| BR-V5 | An exact duplicate row is ignored and counted. A row with an existing invoice number but different data is rejected. | `duplicate` (counted), `conflicting_duplicate` |
| BR-V6 | The customer must exist in the customer list. | `unknown_customer` |
| BR-V7 | Invoice references found in narrations are normalised before matching: upper-case, with spaces and separators removed, so "inv 1023" and "INV-1023" become the same reference. | not applicable |

## 3. Matching rules

Each payment is evaluated in this order. The first rule that applies decides the outcome, and every outcome is logged with the rule ID, a confidence level, a timestamp and the actor (system or person).

1. BR-M1, BR-M2, BR-M3 (a single exact reference)
2. BR-M4 (several references in one payment)
3. BR-M5 (customer and amount)
4. BR-M8 (fuzzy suggestion, Phase 2)
5. BR-M7 (nothing matched: review queue)

BR-M6 (duplicates) is checked first, before anything else.

| ID | Rule | Outcome and confidence |
|---|---|---|
| BR-M1 | **Exact reference, full payment.** The normalised reference equals the number of exactly one open invoice, and the payment amount (in USD) is within `match_tolerance_usd` of its open balance. | Invoice closed. Any difference is logged as a rounding adjustment. Confidence: `exact`. |
| BR-M2 | **Partial payment.** Same reference rule, but the amount is below the open balance by more than the tolerance. | The amount is applied and the invoice stays open as `partially_paid`. Confidence: `exact`. |
| BR-M3 | **Overpayment.** Same reference rule, but the amount is above the open balance by more than the tolerance. | The open balance is applied and the invoice is closed. The excess is recorded as unapplied credit and flagged for review (`overpayment`). |
| BR-M4 | **Several references in one payment.** The narration lists two or more references to open invoices of the same customer, and the amount equals the sum of their open balances within the tolerance. | Each invoice is closed and the payment is split across them. If the sums do not agree, the payment goes to review (`ambiguous_candidates`). An allocation is never guessed. |
| BR-M5 | **Customer and amount, no usable reference.** The payer is a known customer (from the bank account or the cash log), and exactly one of that customer's open invoices has a balance within the tolerance of the amount. | Matched with confidence `inferred`. With no candidate or several, the payment goes to review (`no_reference` or `ambiguous_candidates`). |
| BR-M6 | **Duplicate payment.** A payment identical to an existing one on date, amount, currency, payer and reference. | Rejected and logged. It is never applied twice. |
| BR-M7 | **No match.** No rule applied. | Review queue with one of these reason codes: `no_reference`, `reference_not_found`, `ambiguous_candidates`, `unknown_customer`, `customer_mismatch` (the reference belongs to a different customer than the payer), `overpayment`, `missing_fx_rate`, `low_confidence_fuzzy`. |
| BR-M8 | **Fuzzy match (Phase 2).** The reference is not an exact match, but its similarity to the number of a single open invoice is above the thresholds. | Similarity at or above `fuzzy_auto_threshold`, with the customer consistent and the amount within the tolerance: matched, confidence `fuzzy_high`. Between the two thresholds: a suggestion in the review queue. Below `fuzzy_suggest_threshold`: queue with no suggestion. |

**No first-in-first-out allocation.** Without a usable reference, a payment is never applied to the oldest invoice by default. Guessing causes wrong matches, and a wrong match is worse than an exception in the queue.

## 4. Currency rules

| ID | Rule |
|---|---|
| BR-C1 | Invoices are in USD. Payments can be in USD or LBP. |
| BR-C2 | An LBP payment is converted at the latest rate on or before the payment date: USD amount = LBP amount ÷ rate. The rate comes from the `fx_rates` table, seeded with `fx_default_rate`. |
| BR-C3 | The rate and the USD amount are stored on the payment and are never recalculated afterwards. |
| BR-C4 | If no rate exists on or before the payment date, the payment goes to review (`missing_fx_rate`). The tolerance is applied to the USD amount. |

## 5. Invoice status and aging rules

| ID | Rule |
|---|---|
| BR-A1 | Due date = invoice date + the customer's terms in days. |
| BR-A2 | Status is derived from the open balance: `open` (nothing applied), `partially_paid` (some applied, balance above the tolerance) or `paid` (balance within the tolerance). Overdue is a flag calculated from the as-of date, not a status. |
| BR-A3 | Overdue, days past due and aging buckets follow `docs/kpi_definitions.md`. Cash-on-delivery invoices are excluded from receivables. |
| BR-A4 | A credit note reduces the open balance but never takes it below zero. Any excess becomes unapplied credit. |

## 6. Reminder rules

### Reminder ladder

| Stage | Trigger | Recipient | Action | Phase |
|---|---|---|---|---|
| 1 | Stage-1 delay after the due date | Customer billing contact | Friendly reminder | 1 |
| 2 | Stage-2 delay after the due date | Customer billing contact | Firm reminder that states the open balance | 1 |
| 3 | Stage-3 delay after the due date | Sales rep and collections clerk | Escalation notice and a follow-up task | 2 |
| 4 | Stage-4 delay after the due date | Owner | Credit-review recommendation | 2 |

Stages 1 and 2 are customer-facing. Stages 3 and 4 are internal.

### Rules

| ID | Rule |
|---|---|
| BR-R1 | Reminders are evaluated once per business day at `reminder_run_time`, after loading and matching have finished, so payments received are applied first. |
| BR-R2 | A stage is due when the days past due reach its delay and no reminder exists for that invoice and stage. A stage that falls on a non-business day is sent on the next business day. |
| BR-R3 | **Idempotency.** There is at most one reminder per invoice and stage, enforced by a unique key. A stage that is already sent or pending is never sent again. |
| BR-R4 | **Check at send time.** Before sending, the invoice must still have an open balance of at least `min_reminder_balance_usd`. Otherwise the reminder is skipped and the reason (`paid_before_send` or `below_minimum`) is logged. |
| BR-R5 | **Consolidation (Phase 2).** Customer-facing reminders for one customer due on the same day are combined into one message that lists each invoice. The log keeps one row per invoice, with a shared message ID. |
| BR-R6 | **Superseded stages.** If an invoice crosses several customer-facing thresholds at once, only the highest applicable stage is sent. The lower stages are marked `skipped_superseded`. This highest applicable stage is the "correct stage" that success criterion SC-8 measures. |
| BR-R7 | If a customer has no billing contact, nothing is sent and a follow-up task is created for the clerk (`missing_contact`). |
| BR-R8 | **Retries (Phase 2).** A failed send is retried up to `retry_attempts` times, with the configured delays. After the last failure the reminder is marked `failed`, a task is created for the clerk, and the owner is notified by the error workflow. |
| BR-R9 | Every customer message states the invoice number, invoice date, due date, original amount, open balance in USD and the payment reference to quote. It makes no threats. |
| BR-R10 | Stage 3 and 4 notices are recommendations only. Paidar never blocks sales or changes credit limits. |
| BR-R11 | Every attempt is logged with the invoice or invoices, stage, channel, recipient, timestamp, status, attempt number and message ID. |

## 7. Customer risk segments

Segments describe payment behaviour to help prioritise follow-up. They are not credit decisions.

| ID | Rule |
|---|---|
| BR-S1 | History = invoices fully paid within the last `risk_window_months` months. A customer with fewer than `risk_min_paid_invoices` such invoices is **Insufficient history**. Days late for an invoice = the larger of zero and (the date its balance reached zero − its due date). |
| BR-S2 | **Green:** average days late up to the green limit, and no open invoice past the green age limit. **Amber:** average days late up to the amber limit, or an open invoice past the green age limit but within the amber limit. **Red:** average days late above the amber limit, or any open invoice past the amber age limit. Red takes precedence over amber, and amber over green. |
