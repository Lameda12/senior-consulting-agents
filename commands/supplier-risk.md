---
description: "Assess supplier risk and continuity decisions"
argument-hint: <client / topic / document>
---

Read [shared standards](${CLAUDE_PLUGIN_ROOT}/skills/consulting-deliverable-standards/SKILL.md) and the linked engagement method once per context.

Assess the supplier decision for: $ARGUMENTS
Lead: `operations-supply-chain`. Add `cyber-security` for material systems/data dependence, `privacy-data-protection` for personal-data obligations, or `financial-due-diligence` for financial resilience questions. Do not automatically load SOX or internal-audit personas.

## Inputs
Identify service/product, decision horizon, spend or shipment exposure, critical dependencies, switching lead time, substitutes, incident/performance records and supplied financial/control evidence. Keep shipment, spend and revenue exposure distinct. Company size does not lower evidence requirements for critical suppliers.

## Analysis
1. Map concentration and realistic business impact. Verify whether proposed alternatives are qualified and available; an untested substitute is not mitigation already in place.
2. Compare supplier assertions with dated evidence, scope and exceptions. Record contradictions; an old failed test cannot support a current claim of effective recovery. Missing financials mean resilience is unknown, not insolvency.
3. Use the client's approved rating rubric. Otherwise use provisional priorities: high = plausible critical disruption with no evidenced recovery/substitute; medium = material but contained disruption with supported mitigations; low = limited impact with evidenced recovery. Label likelihood unknown where unsupported. Unknown evidence cannot justify low risk or a numerical score.
4. Recommend proceed, conditional proceed, defer or alternative sourcing, explaining operational tradeoffs. Conditional continuation is a recommendation for the authorized owner's risk decision, never an approval granted by the agent.

## Deliverable and acceptance
Return a decision memo, risk register with stable IDs/source references, targeted evidence requests and an action tracker (proposed owner, deadline, closure evidence). Define conditions, escalation triggers and reassessment timing for any provisional continuation. Avoid unsupported fixed top-ten lists.

Complete when material dependencies and contradictory/missing evidence are visible, ratings have rationale, and actions state what evidence changes the decision. Report technical soundness and request fulfillment separately; never claim controls were tested or supplier approval granted without evidence.
