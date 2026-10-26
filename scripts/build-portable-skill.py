#!/usr/bin/env python3
"""Regenerate skills/senior-consulting-agents/ from agents/, commands/ and the
deliverable-standards skill, so non-Claude agents (Codex, Gemini CLI, OpenCode,
Cursor, Cline, ...) get every persona and workflow through one portable SKILL.md.

Run after editing anything in agents/ or commands/:
    python3 scripts/build-portable-skill.py
"""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "senior-consulting-agents"
REFS = SKILL / "references"


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise SystemExit("missing frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        meta[key.strip()] = value
    return meta, m.group(2).lstrip()


def main():
    if REFS.exists():
        shutil.rmtree(REFS)
    (REFS / "agents").mkdir(parents=True)
    (REFS / "workflows").mkdir(parents=True)

    agent_rows = []
    for path in sorted((ROOT / "agents").glob("*.md")):
        meta, body = split_frontmatter(path.read_text())
        role = re.search(r"^# (.+)$", body, re.M).group(1)
        use_for = re.search(r"Use for (.+?)\.", meta["description"])
        use_for = use_for.group(1) if use_for else meta["description"]
        (REFS / "agents" / path.name).write_text(body)
        agent_rows.append(f"| `{path.stem}` | {role} | {use_for} | `references/agents/{path.name}` |")

    workflow_rows = []
    for path in sorted((ROOT / "commands").glob("*.md")):
        meta, body = split_frontmatter(path.read_text())
        body = body.replace("$ARGUMENTS", "the user's request")
        (REFS / "workflows" / path.name).write_text(f"# {meta['description']}\n\n{body}")
        workflow_rows.append(f"| {path.stem} | {meta['description']} | `references/workflows/{path.name}` |")

    _, standards = split_frontmatter((ROOT / "skills" / "consulting-deliverable-standards" / "SKILL.md").read_text())
    (REFS / "deliverable-standards.md").write_text(standards)

    template = (ROOT / "scripts" / "SKILL.template.md").read_text()
    out = template.replace("{{AGENTS}}", "\n".join(agent_rows)).replace("{{WORKFLOWS}}", "\n".join(workflow_rows))
    (SKILL / "SKILL.md").write_text(out)
    print(f"wrote {len(agent_rows)} personas, {len(workflow_rows)} workflows to {SKILL.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
