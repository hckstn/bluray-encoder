"""
BluRay Encoder
Version: 0.1.0

Globale Konstanten.
"""

from pathlib import Path

PROJECT_NAME = "BluRay Encoder"

VERSION = "0.1.0"

REMUX_DIR = Path("remux")
ENCODED_DIR = Path("encoded")
LOG_DIR = Path("logs")

SUPPORTED_VIDEO_ENCODERS = (
    "libx265",
)