"""
Movie metadata.

Normalized metadata returned by TMDb.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class MovieMetadata:
    """Normalized movie metadata."""

    tmdb_id: int

    imdb_id: str | None

    title: str

    original_title: str

    original_language: str

    release_year: int | None

    runtime: int | None

    overview: str | None = None

    tagline: str | None = None

    poster_path: str | None = None

    genres: tuple[str, ...] = field(default_factory=tuple)