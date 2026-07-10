"""
Builds the best search query for a movie folder.
"""

from __future__ import annotations

from models.movie_folder import MovieFolder
from models.search_query import SearchQuery

from services.filename_parser import FilenameParser
from services.folder_name_parser import FolderNameParser


class SearchQueryBuilder:
    """
    Builds the best possible movie search query.
    """

    def __init__(self) -> None:

        self._folder = FolderNameParser()

        self._filename = FilenameParser()

    def build(
        self,
        folder: MovieFolder,
    ) -> SearchQuery:

        folder_query = self._folder.parse(
            folder.name
        )

        if (
            folder_query.year is not None
            or len(folder_query.title) >= 3
        ):
            return folder_query

        if folder.mkv_files:

            return self._filename.parse(
                folder.mkv_files[0]
            )

        return folder_query