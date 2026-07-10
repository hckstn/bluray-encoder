"""
TMDb service.

Searches movies on The Movie Database (TMDb) and returns normalized
movie metadata.
"""

from __future__ import annotations

from difflib import SequenceMatcher

import httpx

from core.config import ConfigManager
from core.exceptions import MetadataError
from models.movie_match import MovieMatch
from models.movie_metadata import MovieMetadata
from models.search_query import SearchQuery


class TMDbService:
    """Search movies using TMDb."""

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self) -> None:

        config = ConfigManager()

        token = config.get(
            "tmdb",
            "bearer_token",
        )

        self._client = httpx.Client(
            timeout=20.0,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            },
        )

    def search(
        self,
        query: SearchQuery,
    ) -> MovieMetadata | None:
        """
        Return the best matching movie or None.
        """

        matches = self.search_all(query)

        if not matches:
            return None

        return matches[0].metadata

    def search_all(
        self,
        query: SearchQuery,
    ) -> list[MovieMatch]:
        """
        Search TMDb and return all scored matches.
        """

        try:

            response = self._client.get(
                f"{self.BASE_URL}/search/movie",
                params=self._build_params(query),
            )

            response.raise_for_status()

        except httpx.HTTPError as exc:

            raise MetadataError(
                f"TMDb request failed: {exc}"
            ) from exc

        payload = response.json()

        matches: list[MovieMatch] = []

        for item in payload.get("results", []):

            metadata = self._create_metadata(item)

            title_score = self._title_score(
                query.title,
                metadata.title,
                metadata.original_title,
            )

            year_score = self._year_score(
                query.year,
                metadata.release_year,
            )

            score = (
                title_score * 0.70
                + year_score * 0.30
            )

            matches.append(
                MovieMatch(
                    metadata=metadata,
                    score=score,
                    title_score=title_score,
                    year_score=year_score,
                )
            )

        matches.sort(
            key=lambda match: match.score,
            reverse=True,
        )

        return matches

    @staticmethod
    def _build_params(
        query: SearchQuery,
    ) -> dict[str, str | int]:

        params: dict[str, str | int] = {
            "query": query.title,
            "language": "de-DE",
        }

        if query.year is not None:
            params["year"] = query.year

        return params

    @staticmethod
    def _create_metadata(
        movie: dict,
    ) -> MovieMetadata:

        release_year = None

        release_date = movie.get(
            "release_date",
            "",
        )

        if len(release_date) >= 4:

            try:
                release_year = int(
                    release_date[:4]
                )
            except ValueError:
                pass

        return MovieMetadata(
            tmdb_id=movie["id"],
            imdb_id=None,
            title=movie.get("title", ""),
            original_title=movie.get(
                "original_title",
                "",
            ),
            original_language=movie.get(
                "original_language",
                "",
            ),
            release_year=release_year,
            runtime=None,
            overview=movie.get("overview"),
            tagline=None,
            poster_path=movie.get("poster_path"),
            genres=(),
        )

    @staticmethod
    def _title_score(
        query: str,
        title: str,
        original_title: str,
    ) -> float:

        query = query.lower()

        score_title = SequenceMatcher(
            None,
            query,
            title.lower(),
        ).ratio()

        score_original = SequenceMatcher(
            None,
            query,
            original_title.lower(),
        ).ratio()

        return max(
            score_title,
            score_original,
        )

    @staticmethod
    def _year_score(
        query_year: int | None,
        result_year: int | None,
    ) -> float:

        if query_year is None:
            return 1.0

        if result_year is None:
            return 0.0

        if query_year == result_year:
            return 1.0

        difference = abs(
            query_year - result_year
        )

        return max(
            0.0,
            1.0 - difference / 10.0,
        )

    def close(self) -> None:
        """Release HTTP resources."""

        self._client.close()