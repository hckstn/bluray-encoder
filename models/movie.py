"""
BluRay Encoder

Movie model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from core.enums import Language

from .track import (
    AudioTrack,
    SubtitleTrack,
    VideoTrack,
)


@dataclass(slots=True)
class Movie:

    filename: str

    title: str

    year: int | None = None

    tmdb_id: int | None = None

    original_language: Language | None = None

    video: VideoTrack | None = None

    audio: list[AudioTrack] = field(default_factory=list)

    subtitles: list[SubtitleTrack] = field(default_factory=list)

    chapters: bool = False

    @property
    def has_video(self) -> bool:

        return self.video is not None

    def audio_by_language(
        self,
        language: Language,
    ) -> list[AudioTrack]:

        return [
            track
            for track in self.audio
            if track.language == language
        ]

    def subtitle_by_language(
        self,
        language: Language,
    ) -> list[SubtitleTrack]:

        return [
            track
            for track in self.subtitles
            if track.language == language
        ]