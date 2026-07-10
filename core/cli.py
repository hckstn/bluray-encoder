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

        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Enable verbose logging.",
        )

        subparsers = parser.add_subparsers(
            dest="command",
            required=True,
        )

        #
        # scan
        #

        scan = subparsers.add_parser(
            "scan",
            help="Scan movie folders.",
        )

        scan.add_argument(
            "path",
            nargs="?",
            type=Path,
            help="Remux directory. Defaults to config.yaml.",
        )

        #
        # search
        #

        search = subparsers.add_parser(
            "search",
            help="Search TMDb for the first movie folder.",
        )

        search.add_argument(
            "path",
            nargs="?",
            type=Path,
            help="Remux directory. Defaults to config.yaml.",
        )

        #
        # analyze
        #

        analyze = subparsers.add_parser(
            "analyze",
            help="Analyze the first movie folder.",
        )

        analyze.add_argument(
            "path",
            nargs="?",
            type=Path,
            help="Remux directory. Defaults to config.yaml.",
        )

        #
        # encode
        #

        encode = subparsers.add_parser(
            "encode",
            help="Encode one or more movie folders.",
        )

        encode.add_argument(
            "path",
            nargs="?",
            type=Path,
            help="Remux directory. Defaults to config.yaml.",
        )

        return parser