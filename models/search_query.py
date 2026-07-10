"""
Movie search query.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SearchQuery:
    """
    Represents the information required to search a movie database.
    """

    title: str

    year: int | None = None

    source: str = "unknown"