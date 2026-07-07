"""
BluRay Encoder

Result returned by the MovieSourceResolver.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MovieMatch:

    source_name: str

    normalized_title: str

    year: int | None

    confidence: float