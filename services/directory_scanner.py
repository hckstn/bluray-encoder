"""
Directory scanner.
"""

from __future__ import annotations

from pathlib import Path

from models.movie_folder import MovieFolder


class DirectoryScanner:

    def scan(
        self,
        root: Path,
    ) -> list[MovieFolder]:

        if not root.exists():
            return []

        folders: list[MovieFolder] = []

        for directory in sorted(root.iterdir()):

            if not directory.is_dir():
                continue

            mkvs = sorted(directory.glob("*.mkv"))

            if not mkvs:
                continue

            folders.append(
                MovieFolder(
                    path=directory,
                    mkv_files=mkvs,
                )
            )

        return folders