"""
Movie analyzer.

Analyzes all MKV files inside one movie folder and returns the
main feature (longest runtime).
"""

from __future__ import annotations

from models.media import MainFeature
from models.movie_folder import MovieFolder
from services.ffprobe_service import FFprobeService

from core.exceptions import AnalyzerError


class Analyzer:
    """Analyze one movie folder."""

    def __init__(
        self,
        ffprobe: FFprobeService | None = None,
    ) -> None:

        self._ffprobe = ffprobe or FFprobeService()

    def analyze(
        self,
        folder: MovieFolder,
    ) -> MainFeature:
        """
        Analyze all MKV files inside a movie folder and
        return the longest title.
        """

        features: list[MainFeature] = [
            self._ffprobe.analyze(file)
            for file in folder.mkv_files
        ]

        if not features:
            raise AnalyzerError(
                f"No MKV files found in '{folder.path}'."
            )

        return max(
            features,
            key=lambda feature: feature.duration,
        )