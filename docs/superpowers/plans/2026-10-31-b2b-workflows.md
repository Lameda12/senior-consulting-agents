# B2B workflow implementation plan

**Goal:** Turn the approved consulting persona library into economical, evidence-led business workflows while retaining all 54 personas and portable distribution.

**Approved design:** Shared instructions; compact practice routing; one lead with conditional specialists; reusable company context; traceable findings; editable deliverables; updates limited to affected findings. Develop management reporting, supplier-risk review, and proposal preparation first. Brief/standard/deep modes depend on risk as well as company size. Enterprise enforcement belongs to the host application.

**Architecture:** Markdown remains the source. Shared operating rules and optional context templates live in the deliverable-standards skill. The Python generator copies them, rewrites package-relative links, and builds practice indexes from a maintained registry. No new runtime dependencies.

## Constraints and review focus

- Preserve persona IDs, existing command IDs, `$ARGUMENTS` in sources, and standalone persona access to shared rules.
- Never edit portable generated files directly; synchronize all three versions.
- Missing or contradictory evidence must remain visible even in brief mode.
- Separate technical soundness from fulfillment of the user's request.
- Scoped subagents receive the necessary rules and evidence; no recursive delegation.
- Check portable links, source failures without output destruction, and deterministic regeneration.
- Measure prompt characters separately from actual token cost or output quality.

## Tasks

- [x] 1. Capture baseline behavior on incomplete supplier evidence and an infeasible proposal; add failing generator integration tests for routing, copied references, drift detection and invalid input preservation.
- [x] 2. Implement shared standards/method, concise specialist cards, practice routing, and generator `--check` validation. Preserve all specialties and make review conditional on consequence.
- [x] 3. Add management-report and supplier-risk workflows; strengthen proposal and adapt existing workflows to bounded roles, evidence and completion criteria.
- [x] 4. Update installation/contribution documentation and synchronized versions. Add a repeatable 20-case behavioral evaluation set and scoring protocol.
- [x] 5. Regenerate, run the full tests and package checks, perform fresh behavioral checks and a final review, and report measured prompt-size changes with limitations.

## Execution notes

Implementation stays in the user's current checkout; no publishing, installation, or automatic commits. User approval already covers the design above. Independent agents are limited to behavioral evaluation and final review under the skill-authoring guidance.

Validation: seven package tests passed; all generated links resolve; three candidate behavioral scenarios checked, with a follow-up proposal check after clarifying ambiguous requirements. Independent review found no important issues. See `evals/results/2026-10-31.md` for static measurements, unrun cases and missing provider usage data.
