import json
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = REPOSITORY_ROOT / "corpus"


class CorpusContractTests(unittest.TestCase):
    def test_every_catalog_episode_has_complete_source_files(self) -> None:
        catalog = _read_json(CORPUS_ROOT / "catalog.json")
        coverage = _read_json(CORPUS_ROOT / "caption-coverage.json")
        manifest = _read_json(CORPUS_ROOT / "transcript-manifest.json")

        catalog_ids = {
            episode["episode_id"] for episode in catalog["episodes"]
        }
        transcript_ids = {
            path.stem for path in (CORPUS_ROOT / "transcripts").glob("*.md")
        }
        metadata_ids = {
            path.stem for path in (CORPUS_ROOT / "metadata").glob("*.json")
        }
        segment_ids = {
            path.name
            for path in (CORPUS_ROOT / "segments").iterdir()
            if path.is_dir()
        }

        self.assertEqual(catalog["episode_count"], 2_039)
        self.assertEqual(coverage["episode_count"], 2_039)
        self.assertEqual(coverage["captioned_count"], 2_039)
        self.assertEqual(coverage["missing_english_count"], 0)
        self.assertEqual(coverage["failed_count"], 0)
        self.assertEqual(manifest["episode_count"], 2_039)
        self.assertEqual(manifest["transcribed_count"], 2_039)
        self.assertEqual(manifest["missing_caption_count"], 0)
        self.assertEqual(manifest["failed_count"], 0)
        self.assertEqual(catalog_ids, transcript_ids)
        self.assertEqual(catalog_ids, metadata_ids)
        self.assertEqual(
            {episode_id.lower() for episode_id in catalog_ids},
            segment_ids,
        )

    def test_every_segment_has_a_timestamped_source(self) -> None:
        segment_paths = list((CORPUS_ROOT / "segments").glob("*/*.md"))
        self.assertGreater(len(segment_paths), 8_000)

        for path in segment_paths:
            content = path.read_text(encoding="utf-8")
            self.assertIn(
                "timestamp_url: \"https://www.youtube.com/watch?",
                content,
                path,
            )
            self.assertIn("\nSource: [", content, path)
            self.assertGreater(len(content), 300, path)


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
