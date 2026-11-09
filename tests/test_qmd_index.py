import tempfile
import unittest
from pathlib import Path

from ask_hormozi.captions import TranscriptChunk, render_segment
from ask_hormozi.qmd_index import (
    _bm25_query_candidates,
    _enrich_result,
    _has_substantive_context,
    _rank_search_results,
    _sanitize_bm25_query,
    _select_diverse_results,
    render_markdown_results,
)


class QmdIndexTests(unittest.TestCase):
    def test_enriches_qmd_path_with_local_citation(self) -> None:
        metadata = {
            "episode_id": "abc_123",
            "title": "Pricing that works",
            "published": "2026-07-27",
            "duration_seconds": 600,
            "episode_url": "https://www.youtube.com/watch?v=abc_123",
            "channel": "MoreMozi",
            "channel_id": "channel",
            "transcript_source": "automatic_captions",
        }
        chunk = TranscriptChunk(
            90,
            179,
            (
                "Raise the price only after strengthening the offer so the "
                "customer understands the value, the guarantee, and the "
                "specific outcome the business is promising."
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            data_dir = Path(directory)
            path = data_dir / "segments" / "abc_123" / "000090.md"
            path.parent.mkdir(parents=True)
            path.write_text(render_segment(metadata, chunk), encoding="utf-8")
            result = _enrich_result(
                {
                    "file": "ask-hormozi/segments/abc-123/000090-md",
                    "score": 0.9,
                },
                data_dir=data_dir,
            )

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result["episode_id"], "abc_123")
        self.assertEqual(result["start_seconds"], 90)
        self.assertIn("Raise the price", result["context"])
        self.assertTrue(result["citation_url"].endswith("&t=90s"))

    def test_rejects_non_substantive_stage_direction(self) -> None:
        self.assertFalse(_has_substantive_context("[Music]"))
        self.assertFalse(_has_substantive_context("[Applause] Thanks."))
        self.assertTrue(
            _has_substantive_context(
                "A useful transcript passage explains the underlying idea "
                "with enough detail that an agent can answer the question "
                "accurately and cite the source."
            )
        )

    def test_markdown_results_include_source(self) -> None:
        output = render_markdown_results(
            "pricing",
            [
                {
                    "title": "Pricing that works",
                    "start_seconds": 90,
                    "context": "Strengthen the offer before raising the price.",
                    "citation_url": "https://example.com?t=90s",
                }
            ],
        )
        self.assertIn("Pricing that works — 01:30", output)
        self.assertIn("https://example.com?t=90s", output)

    def test_enriches_catalog_only_result(self) -> None:
        content = """---
episode_id: "AbC123"
title: "Catalog title"
episode_url: "https://www.youtube.com/watch?v=AbC123"
---

# Catalog title
"""
        with tempfile.TemporaryDirectory() as directory:
            data_dir = Path(directory)
            episode_path = data_dir / "episodes" / "abc123.md"
            episode_path.parent.mkdir(parents=True)
            episode_path.write_text(content, encoding="utf-8")
            result = _enrich_result(
                {
                    "file": "ask-hormozi/episodes/abc123-md",
                    "score": 2.0,
                },
                data_dir=data_dir,
            )

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result["episode_id"], "AbC123")
        self.assertEqual(result["transcript_source"], "youtube_catalog")

    def test_sanitizes_natural_language_for_qmd_fts(self) -> None:
        self.assertEqual(
            _sanitize_bm25_query(
                "What's Alex Hormozi's take on pricing offers (in 2026)?"
            ),
            "pricing offers 2026",
        )

    def test_builds_focused_bm25_fallbacks(self) -> None:
        candidates = _bm25_query_candidates(
            "How can a wellness clinic grow from seven million "
            "to twenty five million?"
        )
        self.assertEqual(
            candidates[0],
            "wellness clinic grow seven million twenty five million",
        )
        self.assertIn("wellness clinic", candidates)
        self.assertIn("five million", candidates)

    def test_limits_duplicate_passages_per_episode(self) -> None:
        results = [
            {"episode_id": "a", "context": "a1"},
            {"episode_id": "a", "context": "a2"},
            {"episode_id": "a", "context": "a3"},
            {"episode_id": "b", "context": "b1"},
            {"episode_id": "c", "context": "c1"},
        ]
        selected = _select_diverse_results(results, limit=4)
        self.assertEqual(
            [result["context"] for result in selected],
            ["a1", "a2", "b1", "c1"],
        )

    def test_ranks_repeated_focused_matches_before_single_matches(self) -> None:
        results = [
            {
                "episode_id": "generic",
                "title": "A general business video",
                "context": "This passage mentions a wellness clinic once.",
                "_search_hits": 1,
                "_exact_candidate": False,
                "_rrf_score": 0.02,
            },
            {
                "episode_id": "seed",
                "title": "Helping a Wellness Clinic Get to $25M",
                "context": "The clinic needs to focus before it expands.",
                "_search_hits": 3,
                "_exact_candidate": False,
                "_rrf_score": 0.04,
            },
        ]

        ranked = _rank_search_results(
            results,
            query=(
                "How can a wellness clinic grow from seven million "
                "to twenty five million?"
            ),
        )

        self.assertEqual(ranked[0]["episode_id"], "seed")


if __name__ == "__main__":
    unittest.main()
