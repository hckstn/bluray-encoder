"""
Media models.

These dataclasses represent the normalized media information used
throughout the application.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class VideoStream:
    """Video stream."""

    codec: str
    width: int
    height: int

    profile: str | None = None
    hdr: str | None = None

    bit_depth: int | None = None

    frame_rate: float | None = None


@dataclass(slots=True)
class AudioStream:
    """Audio stream."""

    index: int

    language: str

    codec: str

    channels: int

    layout: str | None = None

    title: str | None = None

    default: bool = False

    forced: bool = False


@dataclass(slots=True)
class SubtitleStream:
    """Subtitle stream."""

    index: int

    language: str

    title: str | None = None

    default: bool = False

    forced: bool = False


@dataclass(slots=True)
class MainFeature:
    """
    Represents the analyzed main feature of a movie.
    """

    path: Path

    duration: float

    file_size: int

    chapters: int

    video: VideoStream

    audio: list[AudioStream] = field(default_factory=list)

    subtitles: list[SubtitleStream] = field(default_factory=list)