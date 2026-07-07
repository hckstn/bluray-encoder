"""
Custom project exceptions.
"""

from __future__ import annotations


class BlurayEncoderError(Exception):
    """Base class for all project exceptions."""


class MissingToolError(BlurayEncoderError):
    """Raised when a required external tool cannot be found."""


class ConfigurationError(BlurayEncoderError):
    """Raised when configuration is invalid."""