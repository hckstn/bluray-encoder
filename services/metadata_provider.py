from abc import ABC, abstractmethod

from models.movie_metadata import MovieMetadata
from models.search_query import SearchQuery


class MetadataProvider(ABC):

    @abstractmethod
    def search(
        self,
        query: SearchQuery,
    ) -> MovieMetadata | None:
        ...