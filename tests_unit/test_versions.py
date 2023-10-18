import os
import unittest
import pkgutil
import importlib

class TestVersions(unittest.TestCase):
    def test(self):
        versions_module = importlib.import_module("imagenet_utils.versions")
        version_names = [fname[:-3] for fname in os.listdir("imagenet_utils/versions") if not fname.startswith("__")]
        for version_name in version_names:
            # assert CLASSES is imported in __init__
            self.assertTrue(
                hasattr(versions_module, f"{version_name.upper()}_CLASSES"),
                f"'{version_name.upper()}_CLASSES' not imported in __init__.py"
            )
            # assert CLASSES is sorted
            classes = getattr(versions_module, f"{version_name.upper()}_CLASSES")
            self.assertEqual(sorted(classes), classes, f"{version_name} is not sorted")
