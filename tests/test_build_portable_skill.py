"""Integration contracts for the distributable skill, using a tiny source repo."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('scripts/build-portable-skill.py', (SOURCE / 'scripts/build-portable-skill.py').read_text())
        self.write('scripts/SKILL.template.md', '# Router\n{{AGENT_COUNT}} specialists\n{{WORKFLOWS}}\n{{PRACTICES}}\n')
        self.write('scripts/practices.json', json.dumps({'advisory': {'title': 'Advisory', 'use_for': 'Business operations', 'agents': ['alpha']}}))
        self.write('agents/alpha.md', '---\nname: alpha\ndescription: "Use for operations."\n---\n\n# Operations\n\nRead [standards](../skills/consulting-deliverable-standards/SKILL.md).\n')
        self.write('commands/report.md', '---\ndescription: "Prepare report"\nargument-hint: <request>\n---\n\nUse `alpha` for $ARGUMENTS. Read [standards](../skills/consulting-deliverable-standards/SKILL.md).\n')
        self.write('skills/consulting-deliverable-standards/SKILL.md', '---\nname: consulting-deliverable-standards\ndescription: Standards\n---\n\nRead [method](references/engagement-method.md).\n')
        self.write('skills/consulting-deliverable-standards/references/engagement-method.md', '# Method\nRead [context](company-context.md).\n')
        self.write('skills/consulting-deliverable-standards/references/company-context.md', '# Context\n')

    def write(self, path, content):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)

    def run_build(self, *args):
        return subprocess.run([sys.executable, str(self.root / 'scripts/build-portable-skill.py'), *args], capture_output=True, text=True)

    def output(self):
        base = self.root / 'skills/senior-consulting-agents'
        return {str(p.relative_to(base)): p.read_bytes() for p in base.rglob('*') if p.is_file()}

    def test_build_routes_every_persona_and_copies_resolvable_references(self):
        result = self.run_build()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.output()
        self.assertIn('references/practices/advisory.md', output)
        self.assertIn(b'../agents/alpha.md', output['references/practices/advisory.md'])
        self.assertIn(b'../deliverable-standards.md', output['references/agents/alpha.md'])
        self.assertIn(b'the user\'s request', output['references/workflows/report.md'])
        self.assertIn('references/company-context.md', output)
        self.assertIn(b'(engagement-method.md)', output['references/deliverable-standards.md'])
        self.assertNotIn(b'{{', output['SKILL.md'])

    def test_check_detects_drift_without_rewriting(self):
        self.assertEqual(self.run_build().returncode, 0)
        self.write('skills/senior-consulting-agents/references/agents/alpha.md', 'stale')
        before = self.output()
        result = self.run_build('--check')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(before, self.output())

    def test_native_plugin_paths_become_portable_links(self):
        for name in ('agents/alpha.md', 'commands/report.md'):
            path = self.root / name
            path.write_text(path.read_text().replace(
                '../skills/consulting-deliverable-standards/SKILL.md',
                '${CLAUDE_PLUGIN_ROOT}/skills/consulting-deliverable-standards/SKILL.md',
            ))
        result = self.run_build()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.output()
        for name in ('references/agents/alpha.md', 'references/workflows/report.md'):
            self.assertIn(b'(../deliverable-standards.md)', output[name])
            self.assertNotIn(b'${CLAUDE_PLUGIN_ROOT}', output[name])

    def test_invalid_source_preserves_previous_build(self):
        self.assertEqual(self.run_build().returncode, 0)
        before = self.output()
        self.write('agents/alpha.md', 'missing frontmatter')
        self.assertNotEqual(self.run_build().returncode, 0)
        self.assertEqual(before, self.output())

    def test_unmapped_or_duplicate_personas_are_rejected(self):
        for mapping in ({}, {'a': {'title': 'A', 'use_for': 'A', 'agents': ['alpha', 'alpha']}}):
            with self.subTest(mapping=mapping):
                self.write('scripts/practices.json', json.dumps(mapping))
                self.assertNotEqual(self.run_build().returncode, 0)

    def test_unknown_workflow_persona_is_rejected(self):
        self.write('commands/report.md', '---\ndescription: "Report"\n---\nUse `missing-persona` for $ARGUMENTS.\n')
        self.assertNotEqual(self.run_build().returncode, 0)

    def test_rebuild_is_deterministic_and_removes_obsolete_generated_files(self):
        self.assertEqual(self.run_build().returncode, 0)
        before = self.output()
        self.assertEqual(self.run_build().returncode, 0)
        self.assertEqual(before, self.output())
        self.write('skills/senior-consulting-agents/references/obsolete.md', 'old')
        self.assertNotEqual(self.run_build('--check').returncode, 0)
        self.assertEqual(self.run_build().returncode, 0)
        self.assertEqual(before, self.output())
        self.assertEqual(self.run_build('--check').returncode, 0)


if __name__ == '__main__':
    unittest.main()
