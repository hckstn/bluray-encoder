"""
Media models used throughout the analysis pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class VideoStream:
    """Video stream information."""

    codec: str
    width: int
    height: int

    hdr: str | None = None

    profile: str | None = None

    bit_depth: int | None = None

    frame_rate: float | None = None


@dataclass(slots=True)
class AudioStream:
    """Audio stream information."""

    index: int

    language: str

    codec: str

    channels: int

    title: str | None = None

    default: bool = False

    forced: bool = False


@dataclass(slots=True)
class SubtitleStream:
    """Subtitle stream information."""

    index: int

    language: str

    title: str | None = None

    default: bool = False

    forced: bool = False


@dataclass(slots=True)
class MainFeature:
    """Represents one analyzed MKV."""

    path: Path

    duration: float

    file_size: int

    chapters: int

    video: VideoStream

    audio: list[AudioStream] = field(default_factory=list)

    subtitles: list[SubtitleStream] = field(default_factory=list)