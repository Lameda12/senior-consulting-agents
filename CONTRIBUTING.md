# Contributing

## Add or edit a persona
1. Edit `agents/<id>.md`. Frontmatter needs `name: <id>` matching the filename and a quoted `description` stating when to use it.
2. Keep the shared-standards link, core focus, relevant frameworks, deliverables and specialty-specific analytical checks. Do not duplicate shared operating rules or add fictional credentials.
3. Assign the ID exactly once in `scripts/practices.json` and add it to the Agents table in `README.md`.

## Add or edit a workflow
Edit `commands/<name>.md` with description, argument-hint and `$ARGUMENTS`. Link shared standards, name one lead, define conditional specialists, inputs, analysis, output and completion criteria. Bare hyphenated identifiers in backticks must name existing personas, workflows or skills; use ordinary prose for other terms. Preserve unsupported conclusions as gaps.

Shared rules and optional templates live under `skills/consulting-deliverable-standards/`. The router template is `scripts/SKILL.template.md`. The portable skill is generated; never edit it by hand. The generator rewrites shared links, copies references and produces practice indexes.

Native persona and command links to shared rules use `${CLAUDE_PLUGIN_ROOT}/skills/consulting-deliverable-standards/SKILL.md`, so they resolve to the installed plugin rather than the client's working directory. The generator rewrites this to `../deliverable-standards.md` in portable references. Use the generated persona files when copying prompts outside Claude Code.

## Before opening a PR
```bash
python3 scripts/build-portable-skill.py
python3 scripts/build-portable-skill.py --check
python3 -m unittest discover -s tests -v
```

Commit generated files with source changes. Bump the same version in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `gemini-extension.json`. Run relevant behavioral scenarios from `evals/cases.json`; package tests do not prove consulting quality. Record the model, loaded files, outcomes and limitations using `evals/README.md`.

## Content rules
- No real client names, confidential data or copyrighted firm methodology.
- Cite public standards by verified location; do not paste copyrighted text or assume rules are current.
- Keep the unofficial/not-affiliated disclaimer in shared rules and distribution documentation.
- Test behavior, including missing evidence and contradictory requirements, before claiming improved quality or token cost.
