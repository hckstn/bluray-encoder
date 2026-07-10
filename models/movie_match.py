"""
Movie search match.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.movie_metadata import MovieMetadata


@dataclass(slots=True, frozen=True)
class MovieMatch:
    """
    Represents one scored TMDb search result.
    """

    metadata: MovieMetadata

    score: float

    title_score: float

    year_score: float