# Firmcraft

<p align="center">
  <img src="assets/firmcraft-mascot.png" width="280" alt="Firmcraft's beaver mascot wearing a navy vest, with a carpenter's pencil behind one ear and an evidence checklist in its paws.">
  <br>
  <sub>Careful craftsmanship. Checked evidence. Practical decisions.</sub>
</p>

**Industry-aware AI workflows for B2B decisions and deliverables.**

Firmcraft helps business teams turn financial data, supplier evidence, buyer requirements and operating documents into reviewable reports, proposals and action plans. Use it inside your existing AI assistant as a **portable skill** or a **Claude Code plugin**.

It is built for the recurring work of B2B companies and the advisors serving them: a distributor reviewing a critical supplier, a SaaS finance team preparing management reports, a services firm responding to an RFP, or an enterprise evaluating risk across subsidiaries.

**54 specialist personas · 13 workflows · 7 sector personas · 2 portable skills · MIT licensed**

> Outputs are AI drafts for qualified review. Firmcraft is not affiliated with any professional-services firm and does not provide professional sign-off.

[Quick start](#quick-start) · [B2B verticals](#b2b-verticals) · [Copy-paste prompts](#copy-paste-prompts) · [All workflows](#all-workflows) · [How it works](#how-it-works) · [Installation](#installation) · [Evaluation](#efficiency-and-evaluation)

## What you can get done

| Business job | What you provide | What Firmcraft prepares |
|---|---|---|
| Monthly management reporting | Actuals, budget, cash movements and metric definitions | Variance analysis, reconciliation exceptions, decision summary and action tracker |
| Supplier-risk review | Criticality, concentration, contracts and supplier evidence | Risk findings, evidence gaps, continuity options and conditions for a decision |
| B2B proposals and RFP responses | Buyer requirements, scope, staffing, effort, rates and budget | Requirement matrix, delivery approach, reconciled fees and unresolved commitments |
| Transaction diligence | Deal perimeter, financial schedules and supporting records | Red flags, adjustment schedules, working-capital questions and decision implications |
| Risk, controls and cyber readiness | Business objectives, policies, test results and incident records | Evidence-linked gaps, prioritized remediation and closure criteria |
| Technical or executive review | A draft, its original brief and supporting evidence | Separate assessments of technical soundness and request fulfillment |

The first three jobs have the most detailed workflow instructions. The broader library supports audit, tax, valuation, ESG, strategy, technology and other advisory work; depth and reliability should be evaluated for your use case.

## Quick start

Choose **one** installation route, then paste a starter prompt. An assistant with access to the installed files is required; a plain chat window does not gain these capabilities just by seeing a skill name.

### Claude Code plugin

From the root of this checkout, run in your terminal:

```bash
claude --plugin-dir .
```

Then paste this into the Claude Code conversation:

```text
/senior-consulting-agents:management-report

Prepare a brief October management report for a 40-person B2B distributor.
Audience: owner and finance lead. All amounts are CAD thousands.

Supplied finance table:
Metric            Actual    Budget
Revenue           120       100
Operating costs    90        80
Operating profit   30        20

Supplied cash table:
Opening cash: 40
Net cash movement: -15
Reported closing cash: 30

Calculate the variances and reconcile cash. Do not invent causes for
unexplained movements. Return a decision summary, editable tables,
evidence gaps and three prioritized actions with proposed owners.
Use only these supplied figures; mark missing context explicitly.
```

### Portable skill in Codex

From this checkout, copy both skill folders to your user skills directory. These commands are for macOS/Linux and update same-named installed files:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/senior-consulting-agents "$HOME/.agents/skills/"
cp -R skills/consulting-deliverable-standards "$HOME/.agents/skills/"
```

Open a new Codex session, select the skill using `$`, and paste:

```text
$senior-consulting-agents

Use the management-report workflow in brief mode for a 40-person B2B
distributor. Audience: owner and finance lead. Period: October.
All amounts are CAD thousands.

Revenue: actual 120, budget 100.
Operating costs: actual 90, budget 80.
Operating profit: actual 30, budget 20.
Opening cash: 40. Net cash movement: -15. Reported closing cash: 30.

Calculate the variances and reconcile cash. Do not invent causes for
unexplained movements. Return a decision summary, editable tables,
evidence gaps and three prioritized actions with proposed owners.
Use only these supplied figures; mark missing context explicitly.
```

**What to look for:** revenue is 20 above budget; costs are 10 above budget; profit is 10 above budget. Expected closing cash is 25, so the reported 30 leaves a difference of 5. A useful report keeps that exception visible instead of making up a balancing item.

The plugin uses namespaced commands; Codex supports explicit `$` skill mentions. See the official [Claude Code command format](https://code.claude.com/docs/en/plugins/components) and [Codex skill discovery and invocation guidance](https://learn.chatgpt.com/docs/build-skills).

### A note about the name

**Firmcraft** is the product name. This version retains the existing technical identifiers:

| Item | Current identifier |
|---|---|
| Repository source | `Lameda12/Firmcraft-skill` |
| Claude Code plugin and marketplace | `senior-consulting-agents` |
| Portable router skill | `senior-consulting-agents` |
| Shared standards skill | `consulting-deliverable-standards` |

The commands in this README use those identifiers. `/firmcraft:proposal` and `$firmcraft` are not registered in this version. Naming the project Firmcraft does not by itself rename its installed commands.

## B2B verticals

Firmcraft combines a **business workflow**, a **practice specialist** and, when it materially changes the analysis, a **sector persona**. Choose the work you need done; you do not need to assemble an agent team yourself.

| Vertical | Typical users | Example B2B work | Relevant sector persona |
|---|---|---|---|
| B2B SaaS, software and telecom | CFOs, revenue operations, deal teams | Recurring-revenue reporting, customer concentration, diligence and enterprise proposals | `sector-tmt` |
| Industrial manufacturing and distribution | Operations, procurement, finance | Critical-supplier reviews, margin analysis, capacity and continuity decisions | `sector-industrial-manufacturing` |
| Financial services and fintech | Risk, compliance, finance and technology teams | Control mapping, third-party risk, regulatory gap analysis and reporting | `sector-financial-services` |
| Healthcare suppliers, medtech and life sciences | Commercial, operations and finance teams | Supplier continuity, operating models, launch dependencies and commercial analysis | `sector-healthcare-life-sciences` |
| Energy, resources and industrial services | Finance, capital-project and procurement teams | Capital allocation, contractor risk and sustainability readiness | `sector-energy-resources` |
| Wholesale, consumer-goods suppliers and retail services | Commercial, supply-chain and finance teams | Customer/channel economics, inventory exposure and supplier reviews | `sector-consumer-retail` |
| Public-sector suppliers and contractors | Bid, delivery and advisory teams | Procurement responses, program delivery and service-performance review | `sector-government` |

Consultancies, accounting practices, agencies and managed-service providers can use the same workflows to serve clients in these verticals. Government procurement also introduces B2G requirements; it should not be treated as an ordinary private-sector sale.

These are configurable use cases supported by the persona library, not separately certified industry products. Healthcare examples concern business operations, not clinical decisions. Jurisdiction-specific or regulated conclusions need current sources and appropriate professional review.

## For small teams, growing companies and enterprises

| Mode | Useful starting point | Expected depth |
|---|---|---|
| **Brief** | A focused decision for an owner or small team | One lead, concise findings, essential evidence gaps and next actions |
| **Standard** | Recurring departmental work or a growing B2B business | Working tables, evidence references, reconciliation and assigned actions |
| **Deep** | Complex, disputed, regulated or multi-entity work | Entity-level analysis, scoped specialist input and additional review where available |

Ask for a mode in ordinary language: “Use brief mode; prioritize the three decisions we need this week.” These are instructions to the agent, not command-line flags or guaranteed token limits. A small company with a critical payroll vendor may need deeper work than a large company buying office stationery.

## Copy-paste prompts

The following examples use synthetic facts or clearly named input files. For file-based examples, supply those files in the assistant's authorized workspace or replace the filenames with your actual attachments. Merely naming a file does not make it accessible.

**Choose your invocation:**

- In **Claude Code**, use `/senior-consulting-agents:<workflow>` as the first line.
- In **Codex**, use `$senior-consulting-agents`, then name the workflow in the request.
- In another **skill-capable assistant**, say “Use the senior-consulting-agents skill and its supplier-risk workflow,” replacing the workflow as needed.

Each prompt below identifies which route it uses. The task body can be reused with the other invocation style.

### 1. Distributor: decide whether to continue with a critical supplier

*Claude Code plugin · supplier-risk · brief*

```text
/senior-consulting-agents:supplier-risk

We are a 25-person B2B distributor deciding whether to continue ordering
from a packaging supplier next month. Use brief mode.

Facts supplied by our operations team:
- This supplier supports 70% of shipments.
- We have no qualified alternative supplier.
- Its questionnaire claims monthly backup tests.
- The only supplied test record is from 2023 and shows a failed restore.
- Current financial statements and switching lead times are unavailable.

Prepare a conditional decision memo and an editable risk/action table.
Separate shipment exposure from revenue exposure. Keep contradictory
and missing evidence visible. State who should decide, what evidence
would change the recommendation, and when we should reassess.
Do not invent risk probabilities or approve the supplier on our behalf.
```

### 2. B2B SaaS: prepare the monthly leadership pack

*Portable skill · management-report · standard*

```text
Use the senior-consulting-agents skill and the management-report workflow.

We are a 120-person B2B SaaS company. Prepare our October leadership
report in standard mode, using only the supplied company-context.md,
actuals.csv, budget.csv, cash-movements.csv and subscription-metrics.csv.

Audience: CEO, CFO and department heads. Currency: CAD.
Use the reporting period and metric definitions in company-context.md.

Reconcile revenue, operating costs, profit and cash. Assess ARR movements
and retention only if the supplied data and definitions support them.
Keep bookings, recognized revenue and cash distinct.

Return an executive summary, editable variance/KPI tables, reconciliation
exceptions and a prioritized action tracker with proposed owners.
Cite source files and rows. Do not attribute a variance to a campaign,
churn or pricing without evidence. List inaccessible or missing inputs.
```

### 3. Professional services: build a proposal that can actually be delivered

*Claude Code plugin · proposal · standard*

```text
/senior-consulting-agents:proposal

Draft a six-week finance-reporting cleanup proposal for a B2B client.
Use standard mode and the following supplied requirements and estimates.

R1: A weekly project progress report throughout the six weeks.
R2: A final report in English and French.
R3: An editable handover checklist for the client's finance team.

Analyst: 80 hours at CAD 100/hour.
Engagement lead: 20 hours at CAD 200/hour.
Buyer budget ceiling: CAD 10,000; tax treatment is unspecified.
Only English-speaking staff are confirmed. No client references approved.

Include a requirement matrix, phased scope, staffing/dependencies,
fee calculation and realistic options for resolving the constraints.
Keep mandatory requirements intact. Label proposed commercial terms.
If the offer is not executable, explain exactly what must be resolved.
Do not invent references, translation capacity or an approved discount.
```

### 4. Fintech: review an enterprise customer's security requirements

*Portable skill · cyber-review · standard*

```text
Use the senior-consulting-agents skill and the cyber-review workflow.

We sell a payments-operations platform to business customers. Review
customer-security-questionnaire.xlsx against the supplied policies,
access-review.csv and recovery-test.pdf. Use standard mode.

Prepare an evidence-linked response matrix for the security team:
requirement, supported response, evidence location, gap, proposed owner
and closure criterion. Distinguish policy design from tested operation.

Do not mark a control effective solely because a policy exists.
Do not invent a certification, test result or maturity score.
Identify any privacy question needing separate specialist input.
Keep unsupported compliance statements provisional; verify applicable
current authority before making a jurisdiction-specific legal claim.
```

### 5. Healthcare supplier: assess a logistics dependency

*Claude Code plugin · supplier-risk · standard*

```text
/senior-consulting-agents:supplier-risk

We are a B2B medical-equipment distributor reviewing a logistics provider.
Use standard mode and healthcare/life-sciences sector context where useful.

Supplied inputs: service-agreement.pdf, delivery-performance.csv,
incident-log.csv and vendor-continuity-plan.pdf.
Decision: renew the service for the next year or require conditions first.

Assess service concentration, delivery exceptions, continuity evidence
and the feasibility of alternatives. Distinguish the contract's service
commitments from observed performance. Do not assume a proposed alternate
provider is qualified or available.

Return a renewal decision memo, evidence gaps and actions with acceptance
criteria. Keep the assessment about business operations; flag any product
quality or regulatory question requiring a qualified specialist.
```

### 6. Industrial group: assess an acquisition target

*Portable skill · due-diligence · deep*

```text
Use the senior-consulting-agents skill and the due-diligence workflow.

We are evaluating a B2B industrial-services acquisition. Use deep mode.
Supplied inputs: deal-brief.md, monthly-financials.csv,
management-adjustments.csv, working-capital.csv and debt-schedule.csv.
Use the perimeter, dates, currencies and jurisdictions in deal-brief.md.

Prepare a red-flag report for our investment committee. Bridge reported
to adjusted EBITDA; check recurrence and duplicate adjustments. Assess
working-capital seasonality and overlap with debt-like items.

Connect each material finding to evidence, a deal decision and a targeted
information request. Separate management assertions from verified facts.
Use additional tax, commercial or technology specialists only for material
questions supported by the scope. Do not manufacture a valuation from
missing data or treat draft deal protections as legal advice.
```

### 7. Energy-services company: prepare sustainability readiness actions

*Claude Code plugin · esg · standard*

```text
/senior-consulting-agents:esg

We supply maintenance services to industrial and energy customers.
Prepare a sustainability-readiness assessment in standard mode.

Use company-context.md, customer-reporting-requirements.pdf,
energy-use.csv and emissions-methodology.md supplied in this workspace.

Separate contractual customer requirements from statutory obligations.
Confirm entity boundaries, reporting period and applicable jurisdiction
before assessing a regime. Verify current authoritative sources when
needed; otherwise state which applicability conclusions remain unverified.

Return an evidence-linked gap table and a 90-day action plan with proposed
owners and closure evidence. Keep missing Scope 1, 2 or 3 data visible.
Do not present readiness work as an assurance opinion.
```

### 8. Enterprise: review a report before it reaches the board

*Portable skill · review · deep*

```text
Use the senior-consulting-agents skill and the review workflow.

Review board-report-draft.md against original-brief.md and the supporting
files in the supplied evidence folder. The report covers three entities.
Use deep mode, preserving entity-level differences in evidence coverage.

Assess two axes separately:
1. Technical soundness: evidence, calculations, applicability and limitations.
2. Request fulfillment: the original brief's requirements and acceptance criteria.

Return a prioritized correction table with finding ID, axis, artifact
location, supporting source, severity and required action. Report each
axis as pass, provisional or blocked. If a required source is inaccessible,
say so; do not infer that the claim is verified.

Review the document rather than rewriting it. Identify decisions requiring
qualified review and do not describe AI review as board approval.
```

### 9. Recurring work: update the decision without losing its history

*Portable skill · management-report · follow-up*

```text
Use the senior-consulting-agents skill and the management-report workflow.

Update the supplied prior-report.md using corrected-cash.csv.
Keep the same scope, currency, period and finding IDs.

List changed inputs, recalculate dependent figures and revise only the
findings affected by those changes. Preserve unaffected conclusions.
For each changed finding, show its previous status, new status, supporting
evidence and remaining action. Include a concise change log.

Do not close an issue merely because management says it is resolved.
If the prior report or corrected file is unavailable, identify that gap
instead of pretending to remember or inspect it.
```

## Give the agent a useful brief

A good request tells Firmcraft what decision the work must support. You can paste this template after a skill mention or plugin command:

```text
Business and vertical:
Decision or deliverable needed:
Audience:
Entities, jurisdictions and reporting period:
Currency and units:
Available files or facts:
Known gaps or conflicting evidence:
Constraints and deadline:
Preferred mode: brief / standard / deep
Output format:
What must be true for this work to be accepted:
```

Fill only the fields relevant to the task. For recurring engagements, use the optional [company-context template](skills/consulting-deliverable-standards/references/company-context.md) to preserve approved definitions, source owners and prior finding IDs. Reconfirm facts that have changed; an old brief is not current evidence.

## All workflows

In Claude Code, prefix each workflow below with `/senior-consulting-agents:`. With the portable skill, name the workflow in your request. The short names in this table are workflow IDs, not universal slash commands in every assistant.

| Workflow | Business purpose | Main output |
|---|---|---|
| [management-report](commands/management-report.md) | Understand financial and operating performance | Reconciled report, variance tables and actions |
| [supplier-risk](commands/supplier-risk.md) | Decide how to manage a supplier dependency | Decision memo, risk register and evidence requests |
| [proposal](commands/proposal.md) | Respond to a buyer with feasible commitments | Proposal, requirements matrix and fee calculation |
| [engage](commands/engage.md) | Route an unfamiliar or cross-practice business request | Scoped engagement and consolidated deliverable |
| [review](commands/review.md) | Challenge a draft against evidence and its brief | Corrections and separate review statuses |
| [risk-assessment](commands/risk-assessment.md) | Map business risks to controls and remediation | Risk register, control gaps and roadmap |
| [cyber-review](commands/cyber-review.md) | Evaluate cyber evidence and readiness | Supported findings and remediation priorities |
| [due-diligence](commands/due-diligence.md) | Assess transaction issues and exposures | Red flags, adjustments and information requests |
| [valuation](commands/valuation.md) | Structure a supported valuation analysis | Approach, model outline and supported sensitivities |
| [audit-plan](commands/audit-plan.md) | Prepare audit scope and planned procedures | Planning memo and evidence-linked risk assessment |
| [tax-memo](commands/tax-memo.md) | Analyze a defined tax question | Jurisdiction-specific draft with verified authority or explicit gaps |
| [esg](commands/esg.md) | Assess sustainability reporting readiness | Applicability assessment, gaps and action plan |
| [interview-prep](commands/interview-prep.md) | Develop professional-services team capability | Targeted practice, case exercises and feedback |

## How it works

1. **Route the job.** A known workflow loads its lead directly. Other requests use the relevant practice index.
2. **Set the scope.** Use available company context, identify decisive gaps and choose an appropriate depth.
3. **Analyze the evidence.** Connect findings to source locations, calculations and applicable criteria. Keep assumptions and contradictory evidence visible.
4. **Bring in specialists when needed.** Additional personas address bounded, material questions. Separate agent execution depends on the host and authorization.
5. **Deliver once.** The lead consolidates findings into a coherent artifact with actions and acceptance evidence.
6. **Review and update.** Assess technical soundness and request fulfillment separately. Preserve finding IDs and explain material changes in follow-ups.

The [shared standards](skills/consulting-deliverable-standards/SKILL.md) and [engagement method](skills/consulting-deliverable-standards/references/engagement-method.md) define this behavior. They are instructions for the model, not a deterministic workflow engine.

### What a review status means

| Status | Meaning |
|---|---|
| **Pass** | The assessed axis meets the stated criteria within the evidence and scope used |
| **Provisional** | Useful work is available, but identified assumptions, gaps or verification remain |
| **Blocked** | A material missing fact or conflicting requirement prevents the requested conclusion or commitment |

A mathematically correct fee schedule can pass a calculation check while a proposal remains blocked because required delivery capability is missing. AI review status never replaces authorized commercial acceptance or professional sign-off.

### Output formats and tools

Firmcraft can instruct an assistant to prepare editable tables, memos, registers, models and other artifacts. Actual file creation depends on the host's tools and any document/spreadsheet skills installed. When the requested format is unavailable, the workflow calls for usable Markdown or CSV-compatible tables and an explicit limitation.

The repo does not include an ERP connector, banking integration, document editor or hosted client portal. Connected data, browsing, calculation tools and file permissions come from the assistant environment. A named framework in a persona is a reference topic, not a bundled authoritative database.

## Installation

### Install the published Claude Code plugin

Inside a Claude Code conversation:

```text
/plugin marketplace add Lameda12/Firmcraft-skill
/plugin install senior-consulting-agents@senior-consulting-agents
```

Open a new session or reload plugins, then use a namespaced command such as `/senior-consulting-agents:proposal`. The plugin packages the personas, commands and both skills. See [Claude Code's installation documentation](https://code.claude.com/docs/en/discover-plugins).

Repository installation downloads the published revision. To try local changes before they are published, use `claude --plugin-dir .` from this checkout as shown in the quick start. See [local plugin loading](https://code.claude.com/docs/en/plugins/create).

### Install portable skills with the Skills CLI

In your terminal:

```bash
npx skills add Lameda12/Firmcraft-skill
```

Select both `senior-consulting-agents` and `consulting-deliverable-standards` and your intended assistant. Installer options and supported hosts are maintained by the [Skills CLI](https://www.skills.sh/docs/cli).

The portable route distributes the workflows as reference files. It does not register Claude Code's 13 command files as native commands in every other assistant.

### Install from a local checkout

For Codex, use the copy commands in the quick start. For a team-scoped installation, place the two complete skill directories under `.agents/skills/` in the target project instead of your user directory. Codex documents both [repository and user skill locations](https://learn.chatgpt.com/docs/build-skills).

For another assistant, copy both folders from `skills/` into its documented skill location, retaining all nested references. Avoid installing the same skill at multiple scopes unless you intend that behavior. Start a fresh session and confirm the skill is visible in the host's selector.

The repository also includes [Gemini extension metadata](gemini-extension.json) and [Gemini context instructions](GEMINI.md). Available features and invocation differ by host; the portable skill is the shared workflow source.

### Use with a model that cannot load skills

Include the selected persona and shared instructions directly in the model's context. For an engagement, include these files from `skills/senior-consulting-agents/`:

```text
references/agents/<persona>.md
references/deliverable-standards.md
references/engagement-method.md
references/workflows/<workflow>.md
```

Replace the placeholders with the selected IDs. Include an optional referenced template only when the task needs it. Supply the actual file contents, not just paths the model cannot access. Then provide the business request and evidence. Execution, calculations and verification still depend on the tools available to that model.

## Specialist coverage

All 54 personas remain available. Practice areas cover audit/accounting, tax, business/technology, risk/cyber, forensic work, deals/valuation, ESG, sector context and engagement/career work.

The titles describe analytical perspectives; they are not real people, verified credentials or a claim that 54 independent agents run on every request.

<details>
<summary>Browse all 54 specialist personas</summary>

| Practice | Agent | Role |
|---|---|---|
| Audit & Assurance | `audit-partner` | Audit Engagement Partner |
| Audit & Assurance | `audit-senior-manager` | Audit Senior Manager (External Audit) |
| Audit / Accounting Advisory | `financial-reporting-ifrs` | IFRS Technical Accounting Director |
| Audit / Accounting Advisory | `us-gaap-sec-reporting` | US GAAP & SEC Reporting Senior Manager |
| Audit / Risk Advisory | `sox-icfr` | SOX / ICFR Controls Director |
| Audit / Technology Assurance | `it-audit-itgc` | IT Audit / ITGC Senior Manager |
| Audit & Assurance | `forensic-data-analytics-audit` | Audit Data & Analytics Lead |
| Audit / ESG | `esg-assurance` | ESG & Sustainability Assurance Director |
| Audit | `public-sector-audit` | Government & Public Sector Audit Senior Manager |
| Tax | `corporate-tax-partner` | Corporate Tax Partner |
| Tax | `international-tax` | International Tax Senior Manager |
| Tax | `transfer-pricing` | Transfer Pricing Director |
| Tax | `indirect-tax` | Indirect Tax (VAT/GST/Sales Tax) Senior Manager |
| Tax / Deal Advisory | `mergers-acquisitions-tax` | M&A Tax Director |
| Tax / People | `global-mobility-tax` | Global Mobility Services Senior Manager |
| Tax | `private-enterprise-tax` | Private Enterprise & Family Office Tax Senior Manager |
| Tax | `tax-technology` | Tax Technology & Transformation Director |
| Tax | `tax-controversy` | Tax Controversy & Dispute Resolution Senior Manager |
| Advisory | `management-consulting-partner` | Management Consulting Partner |
| Advisory / Deal Strategy | `strategy-director` | Strategy Director |
| Advisory | `finance-transformation` | Finance Transformation Senior Manager |
| Advisory | `operations-supply-chain` | Operations & Supply Chain Director |
| Advisory | `people-change` | People & Change Senior Manager |
| Advisory | `customer-advisory` | Customer & Digital Experience Director |
| Advisory / Technology | `technology-consulting-architect` | Technology Consulting Director / Enterprise Architect |
| Advisory / Data & AI | `ai-data-analytics` | AI & Data Analytics Director |
| Advisory / Cyber | `cyber-security` | Cyber Security Director |
| Advisory / Cyber | `privacy-data-protection` | Privacy & Data Protection Senior Manager |
| Risk Advisory | `internal-audit` | Internal Audit Director (Outsourced/Co-sourced) |
| Risk Advisory | `enterprise-risk` | Enterprise Risk Management Senior Manager |
| Risk Advisory / FS | `regulatory-compliance-fs` | Financial Services Regulatory Director |
| Risk Advisory / FS | `financial-risk-quant` | Financial Risk & Quantitative Modeling Senior Manager |
| Forensic | `forensic-investigations` | Forensic Investigations Director |
| Forensic / FS | `anti-financial-crime` | Anti-Money Laundering & Sanctions Senior Manager |
| Forensic | `dispute-expert-witness` | Disputes & Expert Witness Director |
| Deal Advisory | `deal-advisory-partner` | Deal Advisory (M&A) Partner |
| Deal Advisory | `financial-due-diligence` | Financial Due Diligence (Transaction Services) Director |
| Deal Advisory | `valuations` | Valuations Senior Manager |
| Deal Advisory | `corporate-finance-modeling` | Corporate Finance & Financial Modeling Director |
| Deal Advisory | `restructuring` | Restructuring & Turnaround Director |
| Deal Advisory | `integration-separation` | M&A Integration & Separation Senior Manager |
| Deal Advisory / Infra | `infrastructure-advisory` | Infrastructure & Project Finance Director |
| Advisory / ESG | `esg-advisory` | ESG Strategy & Decarbonisation Director |
| Sector | `sector-financial-services` | Financial Services Industry Leader |
| Sector | `sector-energy-resources` | Energy, Natural Resources & Chemicals Industry Leader |
| Sector | `sector-healthcare-life-sciences` | Healthcare & Life Sciences Industry Leader |
| Sector | `sector-tmt` | Technology, Media & Telecom Industry Leader |
| Sector | `sector-government` | Government & Public Sector Advisory Director |
| Sector | `sector-consumer-retail` | Consumer & Retail Industry Leader |
| Sector | `sector-industrial-manufacturing` | Industrial Manufacturing & Automotive Industry Leader |
| Firm Functions | `quality-risk-management` | Risk Management & Professional Practice Partner |
| Firm Functions | `proposal-business-development` | Pursuits & Business Development Director |
| Firm Functions | `engagement-project-manager` | Engagement & PMO Director |
| Firm Functions | `learning-career-coach` | Talent, Learning & Career Coach (Big Four) |

</details>

## Working with client information

Use only the evidence needed for the task, in an approved workspace. Keep different clients' context and artifacts separate, and provide redacted data where sufficient. Store reusable company facts only where the user has authorized them.

Firmcraft's instructions require source traceability, visible limitations and appropriate independence checks. Enterprise identity/access controls, client-data separation, retention, residency and audit logging must be provided and enforced by the host platform. This repository does not implement those controls.

For a team rollout, choose a repeatable job, agree acceptance criteria with its business owner, and test representative inputs before relying on the workflow. Add deeper review for consequential financial, legal, regulatory or assurance conclusions.

## Efficiency and evaluation

Firmcraft reduces unnecessary context through a compact router, shared instructions, selective persona loading and bounded specialist assignments. It asks the lead to produce one consolidated report and to update affected findings when evidence changes.

Initial static measurements recorded a **68% smaller router** and **36–45% smaller loaded-file bundles** for two evaluated workflows. These are character counts from a specific before/after comparison, not measured token bills, latency improvements or guaranteed savings. Details and limitations are in the [validation record](evals/results/2026-10-31.md).

The repository includes [20 synthetic evaluation cases](evals/cases.json) and a [comparison protocol](evals/README.md). The initial behavioral checks covered three candidate scenarios; the full repeated benchmark has not been completed. No superiority over another skills library is claimed.

Judge a rollout by **cost per accepted deliverable**, evidence quality, material errors and human correction time—not just shorter prompts.

## Troubleshooting

| Situation | What to check |
|---|---|
| `/firmcraft:proposal` is not found | This release uses `/senior-consulting-agents:proposal`; see the package identifiers above |
| A Claude Code command is missing | Confirm the plugin is loaded and the command exists in your installed revision; local and published revisions can differ |
| `$senior-consulting-agents` is not available | Confirm the whole skill folder is in a supported location, then open a new session and check the skill selector |
| A copied skill cannot find its references | Copy the complete folder, including `references/`; copying only `SKILL.md` is insufficient |
| An example's files cannot be read | Supply the named inputs in an authorized workspace or attach them through the host; filenames alone grant no access |
| The answer is too long | Request brief mode and a specific decision/output length; essential evidence gaps should remain visible |
| The answer stays provisional or blocked | Review the named missing evidence or conflicting requirements; a polished draft cannot resolve an unsupported fact |
| No spreadsheet or document file was produced | Check the host's artifact tools; request editable Markdown/CSV tables if the required format is unavailable |

## Repository layout and contributing

```text
agents/                                  54 source persona files
commands/                                13 source workflows
skills/consulting-deliverable-standards/  Shared method and optional templates
skills/senior-consulting-agents/          Generated portable distribution
scripts/SKILL.template.md                 Router template
scripts/practices.json                   Practice membership
scripts/build-portable-skill.py          Generator and drift checker
evals/                                   Behavioral cases, protocol and results
tests/                                   Package and generator checks
```

After changing source personas, workflows, shared rules or router inputs:

```bash
python3 scripts/build-portable-skill.py
python3 scripts/build-portable-skill.py --check
python3 -m unittest discover -s tests -v
```

Do not hand-edit the generated portable directory. Keep versions synchronized across the plugin manifest, marketplace entry and Gemini extension. See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for the source-of-truth rules and contribution workflow.

## License

[MIT](LICENSE). Firmcraft is independent and is not affiliated with, endorsed by or representing any professional-services firm. All outputs are AI-generated drafts requiring appropriate qualified review.
