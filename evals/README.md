# Behavioral evaluation

Use `cases.json` to compare a baseline commit with a candidate. These are synthetic fixtures, not client advice. The suite is a protocol and dataset; it does not run a model or claim a score by itself.

## Run protocol

1. Pin both revisions, the model/version, reasoning setting, host, tools and output limits. Keep user inputs and evidence identical. Use a fresh context per case and revision. Do not expose `checks` to the responding agent; give it only `request` and the appropriate revision's skill.
2. Follow the skill's actual routing. Record every loaded file, delegated assignment, retrieval and output. Supply only fixture evidence; do not browse unless a case explicitly needs it. Where tools are unavailable, record that constraint equally on both versions.
3. Run all 20 cases with at least three repetitions per revision for a release comparison. Randomize/blind the outputs for grading. Use a qualified domain reviewer for consequential professional claims. Small smoke checks identify regressions; they cannot establish comparative quality.
4. Grade correctness, evidence support, calculations, request fulfillment and actionability on 0–2 each (0 materially deficient, 1 usable with corrections, 2 meets case requirements). Apply each case's checks. Fabricated facts, unsupported definitive compliance conclusions, hidden mandatory gaps or falsely claimed actions are hard failures regardless of total score.
5. Record provider-reported input, cached-input, output and reasoning tokens where available; include every agent, tool-result context and retry. Record actual cost, latency, correction time and acceptance. Missing usage is unknown, never zero. Character counts are only a static prompt-size proxy.
6. Compare paired cases and report simple versus complex work separately. Target 50% lower median total tokens with no quality regression, but do not claim this until measured. Also report cost per accepted deliverable and rejection rate; lower cost achieved by omitting necessary work fails.

## Results record

For each run: case ID, revision, model/settings, loaded files, output/artifact location, five rubric scores, hard failures, reviewer corrections, token breakdown, cost, latency and acceptance. Include tool limitations and unresolved verification. Keep client data out of this repository.

A release report should state which cases were actually run. The initial smoke evaluation and static measurements are documented in `results/2026-10-31.md`; unrun cases remain unmeasured.
