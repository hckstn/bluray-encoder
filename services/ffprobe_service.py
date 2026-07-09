"""
FFprobe service.

Reads media information from FFprobe and converts it into the project's
normalized data model.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from core.media_codec import (
    detect_hdr,
    normalize_audio_codec,
    normalize_video_codec,
)
from models.media import (
    AudioStream,
    MainFeature,
    SubtitleStream,
    VideoStream,
)


class FFprobeService:
    """Analyze MKV files using FFprobe."""

    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLE = "subtitle"

    def analyze(self, file: Path) -> MainFeature:
        """Analyze one MKV file."""

        data = self._run_ffprobe(file)

        return MainFeature(
            path=file,
            duration=float(data["format"]["duration"]),
            file_size=int(data["format"]["size"]),
            chapters=len(data.get("chapters", [])),
            video=self._parse_video(data),
            audio=self._parse_audio(data),
            subtitles=self._parse_subtitles(data),
        )

    @staticmethod
    def _run_ffprobe(file: Path) -> dict[str, Any]:

        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-print_format",
                "json",
                "-show_format",
                "-show_streams",
                "-show_chapters",
                str(file),
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        return json.loads(result.stdout)

    def _parse_video(
        self,
        data: dict[str, Any],
    ) -> VideoStream:

        stream = next(
            s
            for s in data["streams"]
            if s["codec_type"] == self.VIDEO
        )

        return VideoStream(
            codec=normalize_video_codec(
                stream.get("codec_name", "")
            ),
            width=stream.get("width", 0),
            height=stream.get("height", 0),
            profile=stream.get("profile"),
            hdr=detect_hdr(stream),
            bit_depth=self._bit_depth(stream),
            frame_rate=self._frame_rate(stream),
        )

    def _parse_audio(
        self,
        data: dict[str, Any],
    ) -> list[AudioStream]:

        audio: list[AudioStream] = []

        for stream in data["streams"]:

            if stream["codec_type"] != self.AUDIO:
                continue

            tags = stream.get("tags", {})
            disposition = stream.get("disposition", {})

            audio.append(
                AudioStream(
                    index=stream["index"],
                    language=tags.get(
                        "language",
                        "und",
                    ),
                    codec=normalize_audio_codec(
                        stream.get("codec_name", ""),
                        stream.get("profile"),
                    ),
                    channels=stream.get(
                        "channels",
                        0,
                    ),
                    layout=stream.get(
                        "channel_layout"
                    ),
                    title=tags.get("title"),
                    default=bool(
                        disposition.get("default")
                    ),
                    forced=bool(
                        disposition.get("forced")
                    ),
                )
            )

        return audio

    def _parse_subtitles(
        self,
        data: dict[str, Any],
    ) -> list[SubtitleStream]:

        subtitles: list[SubtitleStream] = []

        for stream in data["streams"]:

            if stream["codec_type"] != self.SUBTITLE:
                continue

            tags = stream.get("tags", {})
            disposition = stream.get("disposition", {})

            subtitles.append(
                SubtitleStream(
                    index=stream["index"],
                    language=tags.get(
                        "language",
                        "und",
                    ),
                    title=tags.get("title"),
                    default=bool(
                        disposition.get("default")
                    ),
                    forced=bool(
                        disposition.get("forced")
                    ),
                )
            )

        return subtitles

    @staticmethod
    def _frame_rate(
        stream: dict[str, Any],
    ) -> float | None:

        value = stream.get("avg_frame_rate")

        if not value or value == "0/0":
            return None

        numerator, denominator = value.split("/")

        return float(numerator) / float(denominator)

    @staticmethod
    def _bit_depth(
        stream: dict[str, Any],
    ) -> int | None:

        value = stream.get("bits_per_raw_sample")

        if not value:
            return None

        return int(value)