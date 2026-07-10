"""
TMDb API client.
"""

from __future__ import annotations

import httpx

from models.movie_metadata import MovieMetadata
from models.search_query import SearchQuery

from core.config import ConfigManager


class TMDbClient:

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self) -> None:

        config = ConfigManager()

        self._api_key = config.get(
            "tmdb",
            "api_key",
        )

    def search(
        self,
        query: SearchQuery,
    ) -> MovieMetadata | None:

        params = {
            "api_key": self._api_key,
            "query": query.title,
            "language": "de-DE",
        }

        if query.year:
            params["year"] = query.year

        response = httpx.get(
            f"{self.BASE_URL}/search/movie",
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        results = response.json()["results"]

        if not results:
            return None

        movie = results[0]

        year = None

        if movie.get("release_date"):
            year = int(
                movie["release_date"][:4]
            )

        return MovieMetadata(
            tmdb_id=movie["id"],
            title=movie["title"],
            original_title=movie["original_title"],
            original_language=movie["original_language"],
            release_year=year,
            overview=movie.get("overview"),
            poster_path=movie.get("poster_path"),
        )