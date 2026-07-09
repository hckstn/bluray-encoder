"""
Detection of required external tools.
"""

from __future__ import annotations

import shutil

from core.exceptions import MissingToolError


class ToolDetector:

REQUIRED_TOOLS = (
    "ffmpeg",
    "ffprobe",
    "mkvmerge",
    "mkvpropedit",
    "mkvextract",
)

    def detect(self) -> dict[str, str]:

        result: dict[str, str] = {}

        missing: list[str] = []

        for tool in self.REQUIRED_TOOLS:

            executable = shutil.which(tool)

            if executable is None:
                missing.append(tool)
            else:
                result[tool] = executable

        if missing:
            raise MissingToolError(
                "Missing external tools: "
                + ", ".join(missing)
            )

        return result