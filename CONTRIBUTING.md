# Contributing

## Add or edit a persona
1. Create or edit `agents/<id>.md`. Frontmatter needs `name: <id>` (same as the filename) and a double-quoted `description` that says what the persona is and when to use it.
2. Keep the body structure used by the other personas: role, core focus, frameworks, deliverables, how you work, default output structure.
3. Add the persona to the Agents table in `README.md`.

## Add or edit a workflow
Create or edit `commands/<name>.md` with `description` and `argument-hint` frontmatter. Use `$ARGUMENTS` for the user's input and name personas by id.

## Before opening a PR
```bash
python3 scripts/build-portable-skill.py
```
Commit the regenerated `skills/senior-consulting-agents/` with your change, and bump the version in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `gemini-extension.json`.

## Content rules
- No real client names, confidential data or copyrighted firm methodology.
- Cite public standards (IFRS, ISA, OECD, etc.) by section, not by pasting text.
- Keep the "unofficial, not affiliated with any professional-services firm" disclaimer.
