"""
FFprobe wrapper.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from models.media import (
    AudioStream,
    MainFeature,
    SubtitleStream,
    VideoStream,
)


class FFprobeService:
    """Analyzes a media file using ffprobe."""

    def analyze(self, file: Path) -> MainFeature:

        data = self._run_ffprobe(file)

        return MainFeature(
            path=file,
            duration=float(data["format"]["duration"]),
            file_size=int(data["format"]["size"]),
            chapters=len(data.get("chapters", [])),
            video=self._video(data),
            audio=self._audio(data),
            subtitles=self._subtitles(data),
        )

    @staticmethod
    def _run_ffprobe(file: Path) -> dict:

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

    def _video(self, data: dict) -> VideoStream:

        stream = next(
            s
            for s in data["streams"]
            if s["codec_type"] == "video"
        )

        return VideoStream(
            codec=self._video_codec(stream),
            width=stream.get("width", 0),
            height=stream.get("height", 0),
            profile=stream.get("profile"),
            bit_depth=self._bit_depth(stream),
            frame_rate=self._frame_rate(stream),
            hdr=self._hdr(stream),
        )

    def _audio(self, data: dict) -> list[AudioStream]:

        streams: list[AudioStream] = []

        for stream in data["streams"]:

            if stream["codec_type"] != "audio":
                continue

            tags = stream.get("tags", {})
            disposition = stream.get("disposition", {})

            streams.append(
                AudioStream(
                    index=stream["index"],
                    language=tags.get(
                        "language",
                        "und",
                    ),
                    codec=stream.get(
                        "codec_name",
                        "",
                    ),
                    channels=stream.get(
                        "channels",
                        0,
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

        return streams

    def _subtitles(
        self,
        data: dict,
    ) -> list[SubtitleStream]:

        streams: list[SubtitleStream] = []

        for stream in data["streams"]:

            if stream["codec_type"] != "subtitle":
                continue

            tags = stream.get("tags", {})
            disposition = stream.get("disposition", {})

            streams.append(
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

        return streams

    @staticmethod
    def _frame_rate(stream: dict) -> float | None:

        value = stream.get("avg_frame_rate")

        if not value or value == "0/0":
            return None

        numerator, denominator = value.split("/")

        return float(numerator) / float(denominator)

    @staticmethod
    def _bit_depth(stream: dict) -> int | None:

        value = stream.get("bits_per_raw_sample")

        if not value:
            return None

        return int(value)

    @staticmethod
    def _hdr(stream: dict) -> str | None:

        side_data = stream.get("side_data_list", [])

        for entry in side_data:

            if entry.get("side_data_type") == "DOVI configuration record":
                return "Dolby Vision"

        transfer = stream.get("color_transfer")

        if transfer == "smpte2084":
            return "HDR10"

        if transfer == "arib-std-b67":
            return "HLG"

        return None

     @staticmethod
    def _audio_codec(stream: dict) -> str:

        codec = stream.get("codec_name", "").lower()
        profile = stream.get("profile", "").upper()

        if codec == "dts":

            if "DTS-HD MA" in profile:
                return "DTS-HD MA"

            if "DTS-HD HRA" in profile:
                return "DTS-HD HRA"

            if "DTS EXPRESS" in profile:
                return "DTS Express"

            if "DTS:X" in profile:
                return "DTS:X"

            return "DTS"

        mapping = {
            "truehd": "TrueHD",
            "eac3": "E-AC-3",
            "ac3": "AC-3",
            "aac": "AAC",
            "flac": "FLAC",
            "pcm_bluray": "PCM",
        }

        return mapping.get(codec, codec.upper())


    @staticmethod
    def _video_codec(stream: dict) -> str:

        codec = stream.get("codec_name", "").lower()

        mapping = {
            "h264": "AVC",
            "hevc": "HEVC",
            "mpeg2video": "MPEG-2",
            "vc1": "VC-1",
            "av1": "AV1",
        }

        return mapping.get(codec, codec.upper())