"""
BluRay Encoder

Represents one movie source directory.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class MovieFolder:
    """
    A directory containing one movie and one or more MKV files.
    """

    path: Path

    mkv_files: list[Path] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def has_multiple_titles(self) -> bool:
        return len(self.mkv_files) > 1

    @property
    def is_empty(self) -> bool:
        return len(self.mkv_files) == 0