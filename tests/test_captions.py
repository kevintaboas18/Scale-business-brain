import json
import tempfile
import unittest
from pathlib import Path

from ask_hormozi.captions import (
    CaptionEvent,
    chunk_events,
    episode_metadata,
    format_timestamp,
    parse_frontmatter,
    parse_json3,
    render_segment,
    timestamp_url,
)


class CaptionTests(unittest.TestCase):
    def test_parse_and_chunk_json3(self) -> None:
        payload = {
            "events": [
                {"tStartMs": 0, "dDurationMs": 10_000},
                {
                    "tStartMs": 1_000,
                    "dDurationMs": 2_000,
                    "segs": [{"utf8": "Build"}, {"utf8": " the system."}],
                },
                {
                    "tStartMs": 3_000,
                    "dDurationMs": 500,
                    "segs": [{"utf8": "\n"}],
                },
                {
                    "tStartMs": 91_000,
                    "dDurationMs": 3_000,
                    "segs": [{"utf8": "Measure"}, {"utf8": " incrementality."}],
                },
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "captions.json3"
            path.write_text(json.dumps(payload), encoding="utf-8")
            events = parse_json3(path)

        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].text, "Build the system.")
        chunks = chunk_events(events, chunk_seconds=90)
        self.assertEqual([chunk.start_seconds for chunk in chunks], [0, 90])
        self.assertEqual(chunks[1].text, "Measure incrementality.")

    def test_segment_metadata_round_trip(self) -> None:
        info = {
            "id": "abc123",
            "title": "A useful episode",
            "upload_date": "20260727",
            "duration": 200,
            "channel": "MoreMozi",
        }
        metadata = episode_metadata(info, "automatic_captions")
        chunk = chunk_events(
            [CaptionEvent(90_000, 93_000, "A useful passage.")]
        )[0]
        rendered = render_segment(metadata, chunk)
        parsed = parse_frontmatter(rendered)

        self.assertEqual(parsed["episode_id"], "abc123")
        self.assertEqual(parsed["published"], "2026-07-27")
        self.assertEqual(parsed["start_seconds"], 90)
        self.assertIn("A useful passage.", rendered)

    def test_timestamp_helpers(self) -> None:
        self.assertEqual(format_timestamp(61), "01:01")
        self.assertEqual(format_timestamp(3_661), "01:01:01")
        self.assertEqual(
            timestamp_url("https://www.youtube.com/watch?v=abc", 61),
            "https://www.youtube.com/watch?v=abc&t=61s",
        )


if __name__ == "__main__":
    unittest.main()
