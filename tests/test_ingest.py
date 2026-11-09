import tempfile
import unittest
from pathlib import Path

from ask_hormozi.ingest import _select_caption


class IngestTests(unittest.TestCase):
    def test_manual_caption_is_preferred(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manual = root / "video.en.json3"
            automatic = root / "video.en-orig.json3"
            manual.write_text("{}", encoding="utf-8")
            automatic.write_text("{}", encoding="utf-8")
            selected, source = _select_caption(
                root,
                {
                    "id": "video",
                    "subtitles": {"en": [{}]},
                    "automatic_captions": {"en-orig": [{}]},
                },
            )

        self.assertEqual(selected, manual)
        self.assertEqual(source, "manual_captions")

    def test_automatic_caption_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            automatic = root / "video.en-orig.json3"
            automatic.write_text("{}", encoding="utf-8")
            selected, source = _select_caption(
                root,
                {
                    "id": "video",
                    "subtitles": {},
                    "automatic_captions": {"en-orig": [{}]},
                },
            )

        self.assertEqual(selected, automatic)
        self.assertEqual(source, "automatic_captions")


if __name__ == "__main__":
    unittest.main()
