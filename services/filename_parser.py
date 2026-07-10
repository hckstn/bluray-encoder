"""
Filename parser.
"""

from __future__ import annotations

import re
from pathlib import Path

from models.search_query import SearchQuery


_YEAR_PATTERN = re.compile(r"\((\d{4})\)")


class FilenameParser:
    """
    Parses MKV filenames.
    """

    def parse(
        self,
        file: Path,
    ) -> SearchQuery:

        name = file.stem

        year = None

        match = _YEAR_PATTERN.search(name)

        if match:

            year = int(match.group(1))

            name = _YEAR_PATTERN.sub(
                "",
                name,
            )

        name = re.sub(
            r"_t\d+$",
            "",
            name,
        )

        return SearchQuery(
            title=name.strip(),
            year=year,
            source="filename",
        )