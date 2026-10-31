---
description: "Prepare a reconciled management report"
argument-hint: <client / topic / document>
---

Read [shared standards](${CLAUDE_PLUGIN_ROOT}/skills/consulting-deliverable-standards/SKILL.md) and the linked engagement method once per context.

Prepare a management report for: $ARGUMENTS
Lead: `finance-transformation`. Use `corporate-finance-modeling` only for material model/reconciliation issues, or a sector persona for industry-specific metrics.

## Inputs
Use the company brief if supplied. Identify audience, entities, period, currency/units, actuals, budget or prior-period comparator, cash balances, KPI definitions and prior report. Ask only for facts that change the decision; mark missing comparators and unverified totals explicitly.

## Analysis
1. Check period, entity, unit and currency alignment; retain source locations. Do not aggregate incompatible currencies or mix year-to-date with monthly figures. Reconcile source totals before interpreting performance; show unresolved differences.
2. Calculate actual minus comparator and percentage variance using the comparator as denominator. Show the convention; a zero or negative comparator needs an explicit interpretation, not an unexplained percentage. For expenses, distinguish numeric increase from favorable performance.
3. Explain material movements using supplied driver evidence. Separate observed variance from hypothesized cause. Reconcile opening cash plus net cash movement to closing cash; profit is not cash flow. Do not create a cash bridge when inputs are absent.
4. Prioritize decisions and assign actions. For a follow-up, keep finding IDs, update dependent calculations and show what changed; don't silently replace prior conclusions.

## Deliverable and acceptance
Return an answer-first report, an editable KPI/variance table (metric, period, actual, comparator, difference, percentage, source, explanation), reconciliation exceptions and an action tracker. Use a workbook only when supported/requested; otherwise provide editable tables and disclose that format.

Complete when material numbers reconcile or differences are explicitly open, drivers are evidenced or labeled hypotheses, and each recommendation has a proposed/confirmed owner, timing and acceptance evidence. State technical soundness and request fulfillment separately. Brief mode keeps the key decisions and exceptions; deep mode adds entity and scenario detail without hiding unresolved evidence.
