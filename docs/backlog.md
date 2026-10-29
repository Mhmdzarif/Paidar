# Paidar — Project Backlog

This file is the project backlog and progress tracker. Each milestone (M0 to M11) has a goal, planned deliverables and a checklist.
To track progress, change `- [ ]` to `- [x]` when you finish an item, then commit the change.

Every milestone shares the same definition of done:

- Deliverables are committed to the repository.
- Verification steps were run and the evidence saved.
- Documentation is updated (README status).
- I can explain the milestone in 60 seconds, as I would in an interview.

Planned deliverables for Milestones 1 to 11 are drafts. They are refined when each milestone starts.

## M0: Foundation

**Phase:** 1 – Core (weeks 1–5)
**Goal:** Repo, toolchain, cost log, charter
**Tools in use:** Terminal, Git, GitHub, Python, PostgreSQL 17
**Code:** Tiny (database connection check)

### Checklist
- [x] Git installed and configured
- [x] Public repo `paidar` created and cloned (MIT licence, Python `.gitignore`)
- [x] Python 3.12 or 3.13 installed; virtual environment working
- [x] PostgreSQL 17 running; `psql` works
- [x] Database `paidar` owned by role `paidar_user` with a real password (verify with `\du` and `\l`)
- [x] `.env` created; `.env.example` committed; `.env` is not tracked by Git
- [x] `src/check_db.py` prints the PostgreSQL 17 version
- [x] Folder structure and README header committed
- [x] `docs/COST_LOG.md` completed (version, licence link and date checked for every tool)
- [x] `docs/project_charter.md` written, reviewed and committed
- [x] `docs/backlog.md` committed
- [x] At least four meaningful commits pushed; no old project names left in the repo
- [x] README status line changed to "Milestone 0 complete"

### Definition of done
- [x] Deliverables committed to the repo
- [x] Verification steps run and evidence saved
- [x] Docs updated (README status)
- [x] I can explain this milestone in 60 seconds

## M1: Discovery

**Phase:** 1 – Core (weeks 1–5)
**Goal:** Problem, stakeholders, as-is process, root causes, KPIs, baseline
**Tools in use:** Markdown, Mermaid or draw.io
**Code:** No

### Checklist
- [x] `docs/discovery.md` committed (as-is process, root causes, baseline, competitor snapshot, open questions)
- [x] `docs/kpi_definitions.md` committed (nine KPIs)
- [x] Competitor rows checked against the official sites
- [x] Mermaid diagram renders on GitHub
- [x] README status updated

### Definition of done
- [x] Deliverables committed to the repo
- [x] Verification steps run and evidence saved
- [x] Docs updated (README status)
- [x] I can explain this milestone in 60 seconds

## M2: Requirements

**Phase:** 1 – Core (weeks 1–5)
**Goal:** BRD, user stories, acceptance criteria, business rules, backlog, to-be process
**Tools in use:** Markdown (GitHub Issues optional, decided in M2)
**Code:** No

### Checklist
- [x] `docs/requirements.md` committed (gap analysis, to-be map, functional and non-functional requirements)
- [x] `docs/user_stories.md` committed (29 stories with acceptance criteria)
- [x] `docs/business_rules.md` committed (matching, currency, reminders, risk segments)
- [x] Defaults reviewed and changed where I disagree
- [x] README links added

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M3: Data model and generator

**Phase:** 1 – Core (weeks 1–5)
**Goal:** Data model and seeded synthetic-data generator
**Tools in use:** PostgreSQL, SQL, Python (Faker), pytest
**Code:** Yes

### Planned deliverables
- Entity-relationship diagram
- Schema SQL (raw, staging, core)
- Data dictionary
- Seeded generator producing invoices, bank statements and a cash/cheque log, with injected defects
- Generator assumptions documented

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M4: Ingestion and validation

**Phase:** 1 – Core (weeks 1–5)
**Goal:** Load raw files, validate, quarantine bad rows
**Tools in use:** Python, pandas, pandera, SQL
**Code:** Yes

### Planned deliverables
- Ingestion scripts from raw files into the database
- Validation rules and a quarantine table for rejected rows
- Data-quality report
- One automated test for each injected defect type

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M5: Matching engine

**Phase:** 1 – Core (weeks 1–5)
**Goal:** Payment-to-invoice matching engine
**Tools in use:** Python, pytest
**Code:** Yes

### Planned deliverables
- Exact-reference matching, then customer plus amount matching
- Manual-review queue for unmatched or ambiguous payments
- Evaluation against ground-truth labels (precision, recall, review share)
- Unit tests for every matching rule

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M6: SQL marts and dashboard

**Phase:** 1 – Core (weeks 1–5)
**Goal:** KPI marts and a dashboard that answers the owner's five questions
**Tools in use:** SQL, Metabase, Docker Desktop (installed here if needed)
**Code:** SQL

### Planned deliverables
- SQL marts: aging, DSO, overdue rate, customer risk segments (CTEs and window functions)
- Documented query library
- Dashboard answering the five owner questions in three clicks or fewer
- Screenshots for the README

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M7: Core automation

**Phase:** 1 – Core (weeks 1–5)
**Goal:** Decision API and the first automated workflow
**Tools in use:** FastAPI, n8n, Mailpit
**Code:** Yes

### Planned deliverables
- Decision API with the business rules in tested code
- n8n daily reminder workflow (n8n orchestrates, code decides)
- Mailpit as a local inbox for reminder emails
- Reminder log table
- Workflow export committed to the repo, with no credentials inside

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M8: Advanced automation

**Phase:** 2 – Advanced (weeks 6–8)
**Goal:** Escalation, retries, error handling, fuzzy matching
**Tools in use:** n8n, rapidfuzz, Python
**Code:** Yes

### Planned deliverables
- Escalation workflow
- Retries and an error-handling workflow
- Idempotency so no reminder is sent twice
- Fuzzy matching with a review queue
- Fault-injection tests (mail server down, API error, malformed file)

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M9: Impact and analysis

**Phase:** 2 – Advanced (weeks 6–8)
**Goal:** Baseline-versus-automated comparison and analysis notebook
**Tools in use:** Jupyter, pandas, SQL
**Code:** Yes

### Planned deliverables
- Impact simulation with low, base and high assumptions, labelled simulated
- Jupyter notebook: payment-delay distribution and customer segments
- Limitations section

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M10: Hardening

**Phase:** 2 – Advanced (weeks 6–8)
**Goal:** Test hardening, continuous integration, optional Power BI
**Tools in use:** pytest, GitHub Actions, Power BI Desktop (optional)
**Code:** Some

### Planned deliverables
- Coverage report on the matching and rules modules
- GitHub Actions workflow on the public repo, standard runner only
- Test report
- Optional Power BI report on the same SQL marts

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds

## M11: Polish

**Phase:** 3 – Polish (weeks 9–10)
**Goal:** Recruiter-ready repository, case study and interview preparation
**Tools in use:** Markdown, GitHub Pages
**Code:** No

### Planned deliverables
- Polished README with setup instructions that work from a clean clone
- Case-study page on GitHub Pages
- Three-minute demo video and a recruiter demo script
- ATS-friendly CV bullets based on verified results only
- Interview questions with model answers
- List of skills I can confidently claim

### Definition of done
- [ ] Deliverables committed to the repo
- [ ] Verification steps run and evidence saved
- [ ] Docs updated (README status)
- [ ] I can explain this milestone in 60 seconds