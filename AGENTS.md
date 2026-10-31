# Working in this repo

Source of truth:
- `agents/*.md` – one persona per file (Claude Code subagent format: `name` + quoted `description` frontmatter).
- `commands/*.md` – workflows (Claude Code slash-command format, `$ARGUMENTS` placeholder).
- `skills/consulting-deliverable-standards/SKILL.md` – house style.
- `skills/consulting-deliverable-standards/references/` – shared engagement method and optional templates.
- `scripts/SKILL.template.md` and `scripts/practices.json` – portable router and practice membership.

Generated, do not edit by hand:
- `skills/senior-consulting-agents/` – portable skill for non-Claude agents. Rebuild after any change to the files above:

```bash
python3 scripts/build-portable-skill.py
python3 scripts/build-portable-skill.py --check
python3 -m unittest discover -s tests -v
```

Keep `version` in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `gemini-extension.json` in sync.
