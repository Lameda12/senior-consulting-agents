#!/usr/bin/env python3
"""Build the portable skill from maintained Markdown; --check detects drift without writes."""
import argparse
from collections import Counter
import json
from pathlib import Path
import posixpath
import re

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'skills' / 'senior-consulting-agents'
SHARED = '../skills/consulting-deliverable-standards/SKILL.md'
PLUGIN_SHARED = '${CLAUDE_PLUGIN_ROOT}/skills/consulting-deliverable-standards/SKILL.md'


def split_frontmatter(text):
    """Parse this repo's single-line scalar frontmatter."""
    match = re.match(r'^---\n(.*?)\n---\n?(.*)$', text, re.S)
    if not match:
        raise ValueError('missing frontmatter')
    meta = {}
    for line in match[1].splitlines():
        key, separator, value = line.partition(':')
        if not separator or key in meta or not value.strip():
            raise ValueError(f'invalid frontmatter: {line}')
        value = value.strip()
        meta[key] = json.loads(value) if value.startswith('"') else value
    if not isinstance(meta.get('description'), str):
        raise ValueError('missing description')
    return meta, match[2].lstrip()


def render_files(root):
    """Validate and render the whole package before changing existing output."""
    files, agents = {}, {}
    for path in sorted((root / 'agents').glob('*.md')):
        meta, body = split_frontmatter(path.read_text(encoding='utf-8'))
        role = re.search(r'^# (.+)$', body, re.M)
        if meta.get('name') != path.stem or not role:
            raise ValueError(f'{path}: name must match filename and body needs a title')
        use_for = re.search(r'Use for (.+?)\.', meta['description'])
        agents[path.stem] = (role[1], use_for[1] if use_for else meta['description'])
        files[f'references/agents/{path.name}'] = body.replace(PLUGIN_SHARED, SHARED).replace(SHARED, '../deliverable-standards.md')
    practices = json.loads((root / 'scripts/practices.json').read_text(encoding='utf-8'))
    assigned = [agent for group in practices.values() for agent in group['agents']]
    if set(assigned) != set(agents) or any(n != 1 for n in Counter(assigned).values()):
        raise ValueError('practice registry must assign every persona exactly once, with no unknown IDs')
    practice_rows = []
    for slug, group in practices.items():
        if not re.fullmatch(r'[a-z][a-z0-9-]*', slug):
            raise ValueError(f'invalid practice ID: {slug}')
        rows = [f'| [{agent}](../agents/{agent}.md) | {agents[agent][1]} |' for agent in group['agents']]
        files[f'references/practices/{slug}.md'] = f"# {group['title']}\n\nSelect one lead; load another persona only for a distinct material question.\n\n| Persona | Use for |\n|---|---|\n" + '\n'.join(rows) + '\n'
        practice_rows.append(f"| [{group['title']}](references/practices/{slug}.md) | {group['use_for']} |")
    command_paths = sorted((root / 'commands').glob('*.md'))
    known_ids = set(agents) | {p.stem for p in command_paths} | {'senior-consulting-agents', 'consulting-deliverable-standards'}
    workflow_rows = []
    for path in command_paths:
        meta, body = split_frontmatter(path.read_text(encoding='utf-8'))
        if '$ARGUMENTS' not in body:
            raise ValueError(f'{path}: missing $ARGUMENTS')
        # Bare hyphenated code identifiers in commands name personas, workflows or skills.
        unknown = set(re.findall(r'`([a-z]+(?:-[a-z0-9]+)+)`', body)) - known_ids
        if unknown:
            raise ValueError(f'{path}: unknown references: {sorted(unknown)}')
        body = body.replace('$ARGUMENTS', "the user's request").replace(PLUGIN_SHARED, SHARED).replace(SHARED, '../deliverable-standards.md')
        files[f'references/workflows/{path.name}'] = f"# {meta['description']}\n\n{body}"
        workflow_rows.append(f"| [{path.stem}](references/workflows/{path.name}) | {meta['description']} |")
    source = root / 'skills/consulting-deliverable-standards'
    _, standards = split_frontmatter((source / 'SKILL.md').read_text(encoding='utf-8'))
    files['references/deliverable-standards.md'] = standards.replace('(references/', '(')
    for path in sorted((source / 'references').rglob('*.md')):
        files[f'references/{path.relative_to(source / "references").as_posix()}'] = path.read_text(encoding='utf-8')
    template = (root / 'scripts/SKILL.template.md').read_text(encoding='utf-8')
    for key, value in {'AGENT_COUNT': str(len(agents)), 'WORKFLOW_COUNT': str(len(command_paths)), 'PRACTICES': '\n'.join(practice_rows), 'WORKFLOWS': '\n'.join(workflow_rows)}.items():
        template = template.replace('{{' + key + '}}', value)
    if '{{' in template:
        raise ValueError('unresolved template placeholder')
    files['SKILL.md'] = template
    for name, body in files.items():
        for target in re.findall(r'\]\(([^)]+)\)', body):
            if '://' in target or target.startswith('#'):
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), target.split('#')[0]))
            if resolved not in files:
                raise ValueError(f'{name}: broken package link {target}')
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='report stale, missing or extra generated files without writing')
    args = parser.parse_args()
    try:
        files = render_files(ROOT)
    except (ValueError, KeyError, OSError, TypeError) as exc:
        parser.exit(1, f'Invalid source: {exc}\n')
    existing = {p.relative_to(SKILL).as_posix(): p for p in SKILL.rglob('*') if p.is_file()}
    changed = sorted(name for name, body in files.items() if name not in existing or existing[name].read_bytes() != body.encode('utf-8'))
    extra = sorted(set(existing) - set(files))
    if args.check:
        if changed or extra:
            parser.exit(1, 'Generated skill is stale:\n' + '\n'.join(changed + extra) + '\n')
        print(f'Portable skill is current ({len(files)} files); all package links resolve.')
        return
    for name, body in files.items():
        path = SKILL / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding='utf-8')
    for name in extra:
        existing[name].unlink()
    print(f'Wrote {len(files)} files to {SKILL.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
