import subprocess
import sys
import unittest
from pathlib import Path


class HelloTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(__file__).with_name("hello.py")), *args],
            capture_output=True,
            text=True,
            check=True,
        )

    def test_prints_hello_world(self):
        self.assertEqual(self.run_cli().stdout, "hello world\n")

    def test_help(self):
        output = self.run_cli("--help").stdout
        self.assertIn("--help", output)
        self.assertIn("Print hello world.", output)
        self.assertNotIn("hello world\n", output)


if __name__ == "__main__":
    unittest.main()
