"""
Project specific exceptions.
"""

from __future__ import annotations


class BluRayEncoderError(Exception):
    """Base exception for all project specific exceptions."""


class MissingToolError(BluRayEncoderError):
    """Raised when a required external tool is missing."""


class AnalyzerError(BluRayEncoderError):
    """Raised when a movie folder cannot be analyzed."""


class MetadataError(BluRayEncoderError):
    """Raised when movie metadata cannot be retrieved."""