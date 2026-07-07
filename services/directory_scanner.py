"""
BluRay Encoder

Scans the Remux directory.
"""

from __future__ import annotations

from pathlib import Path

from models.movie_folder import MovieFolder


class DirectoryScanner:

    def scan(
        self,
        remux_directory: Path,
    ) -> list[MovieFolder]:

        movies: list[MovieFolder] = []

        if not remux_directory.exists():
            return movies

        for directory in sorted(remux_directory.iterdir()):

            if not directory.is_dir():
                continue

            mkvs = sorted(directory.glob("*.mkv"))

            movies.append(
                MovieFolder(
                    path=directory,
                    mkv_files=mkvs,
                )
            )

        return movies