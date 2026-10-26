# Working in this repo

Source of truth:
- `agents/*.md` – one persona per file (Claude Code subagent format: `name` + quoted `description` frontmatter).
- `commands/*.md` – workflows (Claude Code slash-command format, `$ARGUMENTS` placeholder).
- `skills/consulting-deliverable-standards/SKILL.md` – house style.

Generated, do not edit by hand:
- `skills/senior-consulting-agents/` – portable skill for non-Claude agents. Rebuild after any change to the files above:

```bash
python3 scripts/build-portable-skill.py
```

Keep `version` in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `gemini-extension.json` in sync.
