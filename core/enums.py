"""
BluRay Encoder
Version: 0.1.0

Zentrale Enumerationen.
"""

from __future__ import annotations

from enum import Enum


class Language(str, Enum):
    """ISO-639-2 Sprachcodes."""

    GERMAN = "deu"
    ENGLISH = "eng"


class TrackType(str, Enum):
    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLE = "subtitle"


class VideoEncoder(str, Enum):
    LIBX265 = "libx265"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"