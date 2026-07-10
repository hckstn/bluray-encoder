"""
Folder name parser.
"""

from __future__ import annotations

import re

from models.search_query import SearchQuery


_YEAR_PATTERN = re.compile(r"\((\d{4})\)$")


class FolderNameParser:
    """
    Parses a movie folder name.
    """

    def parse(
        self,
        folder_name: str,
    ) -> SearchQuery:

        folder_name = folder_name.strip()

        year = None

        match = _YEAR_PATTERN.search(folder_name)

        if match:

            year = int(match.group(1))

            folder_name = _YEAR_PATTERN.sub(
                "",
                folder_name,
            ).strip()

        return SearchQuery(
            title=folder_name,
            year=year,
            source="folder",
        )