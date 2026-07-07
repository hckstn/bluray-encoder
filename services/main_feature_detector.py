"""
BluRay Encoder

Selects the most likely main feature.
"""

from __future__ import annotations

from pathlib import Path

from models.movie_folder import MovieFolder


class MainFeatureDetector:

    def select(
        self,
        folder: MovieFolder,
    ) -> Path:

        if folder.is_empty:
            raise RuntimeError(
                f"No MKV files found in {folder.path}"
            )

        if len(folder.mkv_files) == 1:
            return folder.mkv_files[0]

        #
        # Temporary implementation.
        #
        # Later versions will use ffprobe and a scoring algorithm.
        #

        return max(
            folder.mkv_files,
            key=lambda p: p.stat().st_size,
        )