Paidar — KPI Definitions

Every KPI here is calculated in SQL in Milestone 6 and shown on the dashboard. The five owner questions are listed in the project charter (section 4).

Shared definitions
As-of date: every KPI is calculated "as of" a date. The default is today.
Open balance (of an invoice): invoice amount − applied payments − credit notes, in USD.
Open invoice: an invoice with an open balance above zero.
Overdue: due date earlier than the as-of date. An invoice due today is not overdue. Days past due = as-of date − due date.
Credit sales: invoices issued on credit terms (net 15, 30 or 45). Cash-on-delivery sales are excluded.
Currency: all KPIs are in USD. LBP payments are converted at the reference rate in effect on the payment date. The rate is configurable (default 89,500 LBP/USD).
Aging buckets (days past due): current (not yet due or due today), 1–30, 31–60, 61–90, 90+. The upper bound is inclusive: 30 days past due is in 1–30, and 31 days is in 31–60.
KPIs
#	KPI	Owner question	Formula	Grain	Better when	Data needed	Caveat
1	Days Sales Outstanding (DSO)	Q3: is DSO improving?	(open receivables at period end ÷ credit sales in the period) × days in the period	Monthly, company (and by customer segment)	Lower	Invoices, applied payments	Swings with end-of-month sales spikes; says nothing about individual customers
2	Total AR outstanding	Q1: how much is owed?	Sum of open balances as of the as-of date	As-of date; company and customer	Lower relative to sales	Invoices, applied payments, credit notes	Includes invoices not yet due, so a large number is not automatically bad
3	Overdue AR percentage	Q1: how much is overdue?	Overdue balance ÷ total AR outstanding × 100 (0 when total AR is 0)	As-of date; company and customer	Lower	Same as KPI 2, plus due dates	A few large invoices can dominate it
4	Aging buckets	Q2: who owes the most overdue money, and for how long?	Open balance grouped by days-past-due bucket	As-of date; customer × bucket	Less in older buckets	Invoices, applied payments, due dates	Unapplied cash inflates the older buckets until it is matched
5	Average days to pay	Q3	Amount-weighted average of (date the balance reached zero − invoice date) for invoices fully paid in the period	Monthly, company and customer	Lower	Invoices, payments with dates	Ignores unpaid invoices, so slow payers appear only after they pay
6	Collection Effectiveness Index (CEI)	Q3	(beginning AR + credit sales − ending total AR) ÷ (beginning AR + credit sales − ending current AR) × 100	Monthly, company	Higher (100 means everything collectable was collected)	Opening and closing AR, credit sales, due dates	"Current" means not yet due; the period must be defined consistently
7	Match rate	Q4: which payments could not be matched?	Payments matched automatically with no human action ÷ all payments received in the period × 100 (by count; also reported by value)	Monthly, company	Higher	Payments, match log	Always read with match precision (SC-2): a high rate with wrong matches is worse than a lower one
8	Manual touches per invoice	Q5: what happened next?	Logged manual actions (manual match, hand-sent reminder, correction) ÷ invoices processed in the period	Monthly, company	Lower	Event log with the actor (system or person)	Counts only logged actions
9	On-time reminder rate	Q5: which reminders were sent?	Reminders sent within 1 business day of their trigger ÷ reminders due × 100	Monthly, company	Higher	Reminder rules (Milestone 2), reminder log	In the demo, "sent" means delivered to a local inbox. It measures process compliance, not whether customers paid.

Owners: finance KPIs (1–7): the owner reviews and the accountant maintains. Process KPIs (8–9): the collections clerk.