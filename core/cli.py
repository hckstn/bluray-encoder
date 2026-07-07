"""
Command line interface.
"""

from __future__ import annotations

import argparse
from pathlib import Path


class CLI:
    """Builds the command line interface."""

    @staticmethod
    def build() -> argparse.ArgumentParser:

        parser = argparse.ArgumentParser(
            prog="bluray-encoder",
            description="Blu-ray Encoder",
        )

        subparsers = parser.add_subparsers(
            dest="command",
            required=True,
        )

        scan = subparsers.add_parser(
            "scan",
            help="Scan a remux directory.",
        )

        scan.add_argument(
            "path",
            nargs="?",
            type=Path,
            help="Path to the remux directory. Defaults to config.yaml.",
        )

        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Enable verbose logging.",
        )

        return parser