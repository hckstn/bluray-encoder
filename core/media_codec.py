"""
Media codec normalization.

Converts raw FFprobe codec names into normalized names used by the
application.
"""

from __future__ import annotations

from typing import Any


_VIDEO_CODECS = {
    "h264": "AVC",
    "hevc": "HEVC",
    "mpeg2video": "MPEG-2",
    "vc1": "VC-1",
    "av1": "AV1",
}

_AUDIO_CODECS = {
    "ac3": "AC-3",
    "eac3": "E-AC-3",
    "truehd": "TrueHD",
    "aac": "AAC",
    "flac": "FLAC",
    "pcm_bluray": "PCM",
}


def normalize_video_codec(codec: str) -> str:
    """Return a normalized video codec name."""

    return _VIDEO_CODECS.get(codec.lower(), codec.upper())


def normalize_audio_codec(codec: str, profile: str | None) -> str:
    """Return a normalized audio codec name."""

    codec = codec.lower()
    profile = (profile or "").upper()

    if codec == "dts":

        if profile.startswith("DTS-HD MA"):
            return "DTS-HD MA"

        if profile.startswith("DTS-HD HRA"):
            return "DTS-HD HRA"

        if profile.startswith("DTS:X"):
            return "DTS:X"

        if profile.startswith("DTS EXPRESS"):
            return "DTS Express"

        return "DTS"

    return _AUDIO_CODECS.get(codec, codec.upper())


def detect_hdr(video_stream: dict[str, Any]) -> str | None:
    """
    Detect HDR type from FFprobe JSON.
    """

    for entry in video_stream.get("side_data_list", []):

        if (
            entry.get("side_data_type")
            == "DOVI configuration record"
        ):
            return "Dolby Vision"

    transfer = video_stream.get("color_transfer")

    if transfer == "smpte2084":
        return "HDR10"

    if transfer == "arib-std-b67":
        return "HLG"

    return None