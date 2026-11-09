import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ask_hormozi.cli import _configure
from ask_hormozi.ingest import default_data_dir


class ConfigTests(unittest.TestCase):
    def test_configure_persists_bundled_corpus(self) -> None:
        with tempfile.TemporaryDirectory() as home_directory:
            home = Path(home_directory)
            corpus = home / "checkout" / "corpus"
            (corpus / "episodes").mkdir(parents=True)
            with patch.object(Path, "home", return_value=home):
                _configure(corpus)
                configured = default_data_dir()
                payload = json.loads(
                    (
                        home / ".config" / "ask-hormozi" / "config.json"
                    ).read_text(encoding="utf-8")
                )

        self.assertEqual(configured, corpus.resolve())
        self.assertEqual(payload["data_dir"], str(corpus.resolve()))

    def test_environment_override_wins(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(
                os.environ, {"ASK_HORMOZI_DATA_DIR": directory}, clear=False
            ):
                self.assertEqual(default_data_dir(), Path(directory).resolve())


if __name__ == "__main__":
    unittest.main()
