"""
BluRay Encoder

Track models.
"""

from __future__ import annotations

from dataclasses import dataclass

from core.enums import Language


@dataclass(slots=True)
class Track:

    index: int

    codec: str

    language: Language

    title: str | None = None

    default: bool = False

    forced: bool = False

    commentary: bool = False

    def is_primary(self) -> bool:

        return not self.commentary


@dataclass(slots=True)
class VideoTrack(Track):

    width: int = 0

    height: int = 0

    hdr: bool = False


@dataclass(slots=True)
class AudioTrack(Track):

    channels: int = 0


@dataclass(slots=True)
class SubtitleTrack(Track):

    pass