import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PROJECT_ROOT / "package.yaml"
WRAPPER_PATH = PROJECT_ROOT / "scripts" / "hq-ask-hormozi"


class HqPackTests(unittest.TestCase):
    def test_manifest_declares_existing_contributions(self) -> None:
        manifest = MANIFEST_PATH.read_text(encoding="utf-8")

        self.assertIn("name: hq-pack-ask-hormozi", manifest)
        self.assertIn("version: 0.2.2", manifest)
        self.assertIn("hqCore: '>=12.0.0'", manifest)
        self.assertIn("    - ask-hormozi", manifest)
        self.assertIn("    - hq-ask-hormozi", manifest)
        self.assertIn("entrypoint: ask-hormozi", manifest)
        self.assertTrue(
            (PROJECT_ROOT / "skills" / "ask-hormozi" / "SKILL.md").is_file()
        )
        self.assertTrue(WRAPPER_PATH.is_file())

    def test_wrapper_indexes_missing_collection_before_search(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            bin_dir = temp_root / "bin"
            bin_dir.mkdir()
            log_path = temp_root / "python.log"
            self._write_executable(
                bin_dir / "qmd",
                "#!/bin/sh\n"
                "if [ \"$1\" = collection ] && [ \"$2\" = list ]; then\n"
                "  printf 'Collections:\\n'\n"
                "fi\n",
            )
            self._write_executable(
                bin_dir / "python3",
                "#!/bin/sh\n"
                "printf '%s\\n' \"$*\" >> \"$ASK_HORMOZI_TEST_LOG\"\n",
            )
            env = os.environ.copy()
            env.update(
                {
                    "ASK_HORMOZI_PACK_ROOT": str(PROJECT_ROOT),
                    "ASK_HORMOZI_TEST_LOG": str(log_path),
                    "PATH": f"{bin_dir}:{env['PATH']}",
                }
            )

            subprocess.run(
                [
                    str(WRAPPER_PATH),
                    "search",
                    "pricing and positioning",
                    "--format",
                    "json",
                    "--limit",
                    "3",
                ],
                check=True,
                env=env,
                capture_output=True,
                text=True,
            )

            calls = log_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(calls), 2)
            self.assertIn("-m ask_hormozi index", calls[0])
            self.assertIn(f"--data-dir {PROJECT_ROOT / 'corpus'}", calls[0])
            self.assertIn(
                "-m ask_hormozi search pricing and positioning "
                "--format json --limit 3",
                calls[1],
            )
            self.assertIn(f"--data-dir {PROJECT_ROOT / 'corpus'}", calls[1])

    def test_wrapper_reuses_existing_collection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            bin_dir = temp_root / "bin"
            bin_dir.mkdir()
            log_path = temp_root / "python.log"
            self._write_executable(
                bin_dir / "qmd",
                "#!/bin/sh\n"
                "if [ \"$1\" = collection ] && [ \"$2\" = list ]; then\n"
                "  printf 'ask-hormozi (qmd://ask-hormozi/)\\n'\n"
                "  i=0\n"
                "  while [ \"$i\" -lt 10000 ]; do\n"
                "    printf 'collection filler output\\n'\n"
                "    i=$((i + 1))\n"
                "  done\n"
                "fi\n",
            )
            self._write_executable(
                bin_dir / "python3",
                "#!/bin/sh\n"
                "printf '%s\\n' \"$*\" >> \"$ASK_HORMOZI_TEST_LOG\"\n",
            )
            env = os.environ.copy()
            env.update(
                {
                    "ASK_HORMOZI_PACK_ROOT": str(PROJECT_ROOT),
                    "ASK_HORMOZI_TEST_LOG": str(log_path),
                    "PATH": f"{bin_dir}:{env['PATH']}",
                }
            )

            subprocess.run(
                [str(WRAPPER_PATH), "search", "offers"],
                check=True,
                env=env,
                capture_output=True,
                text=True,
            )

            calls = log_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(calls), 1)
            self.assertIn("-m ask_hormozi search offers", calls[0])

    def test_wrapper_unpacks_marketplace_corpus_before_indexing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            pack_root = temp_root / "pack"
            (pack_root / "ask_hormozi").mkdir(parents=True)
            corpus_root = pack_root / "corpus"
            corpus_root.mkdir()
            (corpus_root / "segments.tar.xz").touch()
            bin_dir = temp_root / "bin"
            bin_dir.mkdir()
            log_path = temp_root / "runtime.log"
            self._write_executable(
                bin_dir / "qmd",
                "#!/bin/sh\n"
                "if [ \"$1\" = collection ] && [ \"$2\" = list ]; then\n"
                "  printf 'Collections:\\n'\n"
                "fi\n",
            )
            self._write_executable(
                bin_dir / "tar",
                "#!/bin/sh\n"
                "printf 'tar %s\\n' \"$*\" >> \"$ASK_HORMOZI_TEST_LOG\"\n"
                "mkdir -p \"$4/segments\"\n",
            )
            self._write_executable(
                bin_dir / "python3",
                "#!/bin/sh\n"
                "printf 'python %s\\n' \"$*\" >> \"$ASK_HORMOZI_TEST_LOG\"\n",
            )
            env = os.environ.copy()
            env.update(
                {
                    "ASK_HORMOZI_PACK_ROOT": str(pack_root),
                    "ASK_HORMOZI_TEST_LOG": str(log_path),
                    "PATH": f"{bin_dir}:{env['PATH']}",
                }
            )

            subprocess.run(
                [str(WRAPPER_PATH), "setup"],
                check=True,
                env=env,
                capture_output=True,
                text=True,
            )

            calls = log_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(calls), 2)
            self.assertIn("tar -xJf", calls[0])
            self.assertIn("segments.tar.xz", calls[0])
            self.assertIn("python -m ask_hormozi index", calls[1])

    @staticmethod
    def _write_executable(path: Path, content: str) -> None:
        path.write_text(content, encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)


if __name__ == "__main__":
    unittest.main()
