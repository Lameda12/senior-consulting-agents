"""Cross-platform release invariants."""
import json
from pathlib import Path
import unittest


class PackageTests(unittest.TestCase):
    def test_all_distribution_manifests_use_the_same_version(self):
        root = Path(__file__).resolve().parents[1]
        plugin = json.loads((root / '.claude-plugin/plugin.json').read_text())
        marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
        gemini = json.loads((root / 'gemini-extension.json').read_text())
        self.assertEqual(plugin['version'], marketplace['plugins'][0]['version'])
        self.assertEqual(plugin['version'], gemini['version'])
