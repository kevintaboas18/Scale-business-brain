import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ask_hormozi.catalog import (
    CaptionAuditResult,
    _english_languages,
    audit_caption_coverage,
    inspect_caption_coverage,
    render_catalog_episode,
    write_catalog,
)


class CatalogTests(unittest.TestCase):
    def test_writes_catalog_and_episode_markdown(self) -> None:
        episodes = [
            {
                "id": "AbC123",
                "title": "A useful episode",
                "duration": 3_661,
            }
        ]
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            catalog = write_catalog(
                output_dir,
                episodes=episodes,
                channel_url="https://example.com/channel",
            )
            episode_path = output_dir / "episodes" / "abc123.md"
            episode_text = episode_path.read_text(encoding="utf-8")
            stored = json.loads(
                (output_dir / "catalog.json").read_text(encoding="utf-8")
            )

        self.assertEqual(catalog["episode_count"], 1)
        self.assertEqual(stored["episodes"][0]["episode_id"], "AbC123")
        self.assertIn("https://www.youtube.com/watch?v=AbC123", episode_text)
        self.assertIn("Duration: 01:01:01", episode_text)

    def test_catalog_markdown_has_source_boundary(self) -> None:
        rendered = render_catalog_episode(
            {
                "episode_id": "abc",
                "title": "Episode title",
                "episode_url": "https://example.com/watch",
                "duration_seconds": 60,
            }
        )
        self.assertIn("source: \"youtube_catalog\"", rendered)
        self.assertIn("authorized transcript corpus", rendered)

    def test_english_language_detection(self) -> None:
        languages = _english_languages(
            {"en": [], "en-orig": [], "es": [], "en-US": []}
        )
        self.assertEqual(languages, ["en", "en-US", "en-orig"])

    def test_caption_inspection_falls_back_when_first_client_has_no_english(
        self,
    ) -> None:
        without_captions = {
            "id": "video",
            "title": "Video",
            "duration": 60,
            "subtitles": {},
            "automatic_captions": {},
        }
        with_captions = {
            **without_captions,
            "automatic_captions": {"en-orig": []},
        }
        with patch(
            "ask_hormozi.catalog.subprocess.run",
            side_effect=[
                subprocess.CompletedProcess(
                    args=[],
                    returncode=0,
                    stdout=json.dumps(without_captions),
                    stderr="",
                ),
                subprocess.CompletedProcess(
                    args=[],
                    returncode=0,
                    stdout=json.dumps(with_captions),
                    stderr="",
                ),
            ],
        ) as run:
            result = inspect_caption_coverage(
                {"id": "video", "title": "Video"}
            )

        self.assertEqual(result.status, "captioned")
        self.assertEqual(result.automatic_english, ["en-orig"])
        self.assertEqual(run.call_count, 2)
        self.assertIn("web_embedded", " ".join(run.call_args_list[0].args[0]))
        self.assertIn("player_client=tv", " ".join(run.call_args_list[1].args[0]))

    def test_caption_audit_resumes_only_failed_entries(self) -> None:
        episodes = [
            {"id": "verified", "title": "Verified", "duration": 60},
            {"id": "retry", "title": "Retry", "duration": 60},
        ]
        with tempfile.TemporaryDirectory() as directory:
            output_file = Path(directory) / "coverage.json"
            output_file.write_text(
                json.dumps(
                    {
                        "episodes": [
                            {
                                "episode_id": "verified",
                                "title": "Verified",
                                "episode_url": "https://example.com/verified",
                                "published": "",
                                "duration_seconds": 60,
                                "manual_english": [],
                                "automatic_english": ["en"],
                                "status": "captioned",
                                "error": None,
                            },
                            {
                                "episode_id": "retry",
                                "title": "Retry",
                                "episode_url": "https://example.com/retry",
                                "published": "",
                                "duration_seconds": 60,
                                "manual_english": [],
                                "automatic_english": [],
                                "status": "failed",
                                "error": "throttled",
                            },
                        ]
                    }
                ),
                encoding="utf-8",
            )
            retried = CaptionAuditResult(
                episode_id="retry",
                title="Retry",
                episode_url="https://example.com/retry",
                published="",
                duration_seconds=60,
                manual_english=[],
                automatic_english=["en-orig"],
                status="captioned",
            )
            with (
                patch(
                    "ask_hormozi.catalog.list_episodes",
                    return_value=episodes,
                ),
                patch(
                    "ask_hormozi.catalog.inspect_caption_coverage",
                    return_value=retried,
                ) as inspect,
            ):
                payload = audit_caption_coverage(
                    output_file=output_file,
                    jobs=1,
                )

        inspect.assert_called_once()
        self.assertEqual(
            inspect.call_args.args[0]["id"],
            "retry",
        )
        self.assertEqual(payload["captioned_count"], 2)
        self.assertEqual(payload["failed_count"], 0)


if __name__ == "__main__":
    unittest.main()
