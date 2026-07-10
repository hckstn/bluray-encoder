"""
Project specific exceptions.
"""

from __future__ import annotations


class BluRayEncoderError(Exception):
    """Base exception for the application."""


class AnalyzerError(BluRayEncoderError):
    """Raised when a movie folder cannot be analyzed."""