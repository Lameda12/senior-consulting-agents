---
description: "Review evidence and request fulfillment separately"
argument-hint: <client / topic / document>
---

Read [shared standards](${CLAUDE_PLUGIN_ROOT}/skills/consulting-deliverable-standards/SKILL.md) and the linked engagement method once per context.

Review: $ARGUMENTS
Lead: `quality-risk-management`. Add the relevant practice reviewer for consequential technical judgments; keep the reviewer independent of authoring context when available. Workers review directly and must not delegate.
Use the artifact, source evidence and original request/requirements. If requirements are unavailable, request them or explicitly mark that axis unassessed; never infer compliance from the artifact alone.
Assess separately (1) technical soundness: support, calculations, applicability, consistency and contradictory evidence, and (2) request fulfillment: required scope, format, acceptance criteria and actions.
Return corrections in a table: finding ID, axis, artifact location, source/rule, issue, severity, required action. Check specialist claims against evidence; do not treat their output as verification. Give pass/provisional/blocked per axis and open items; an unassessed axis remains provisional. Provide a readiness recommendation, not professional sign-off. Do not rewrite the entire artifact unless requested.
