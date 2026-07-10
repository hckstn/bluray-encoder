"""
Application entry point.
"""

from __future__ import annotations

from pathlib import Path

from rich.console import Console

from core.cli import CLI
from core.config import ConfigManager
from core.exceptions import MissingToolError
from core.tool_detector import ToolDetector

from pipeline.analyzer import Analyzer
from services.directory_scanner import DirectoryScanner
from services.search_query_builder import SearchQueryBuilder
from services.tmdb_service import TMDbService


class Application:
    """Main application."""

    VERSION = "0.5.0"

    def __init__(self) -> None:

        self.console = Console()
        self.config = ConfigManager()

        self.scanner = DirectoryScanner()
        self.analyzer = Analyzer()
        self.query_builder = SearchQueryBuilder()
        self.tmdb = TMDbService()

    def run(self) -> int:

        args = CLI.build().parse_args()

        self.console.print(
            f"[bold cyan]BluRay Encoder[/] {self.VERSION}"
        )
        self.console.print()

        if not self._check_tools():
            return 1

        match args.command:

            case "scan":
                return self.scan(args.path)

            case "search":
                return self.search(args.path)

        return 0

    def _check_tools(self) -> bool:

        self.console.print("Checking required tools...")

        try:

            tools = ToolDetector().detect()

            for tool in tools:

                self.console.print(
                    f"[green]✓[/] {tool}"
                )

            self.console.print()

            return True

        except MissingToolError as exc:

            self.console.print()
            self.console.print(f"[red]{exc}[/]")

            return False

    def _resolve_path(
        self,
        path: Path | None,
    ) -> Path:

        if path is None:

            path = Path(
                self.config.get(
                    "paths",
                    "remux",
                )
            )

        return path.expanduser().resolve()

    def scan(
        self,
        path: Path | None,
    ) -> int:

        path = self._resolve_path(path)

        self.console.print(
            f"Scanning [cyan]{path}[/]"
        )
        self.console.print()

        movies = self.scanner.scan(path)

        if not movies:

            self.console.print(
                "[yellow]No movie folders found.[/]"
            )

            return 0

        for movie in movies:

            self.console.print(
                f"[green]✓[/] {movie.name}"
            )

        self.console.print()
        self.console.print(
            f"Found {len(movies)} movie folder(s)."
        )

        return 0

    def search(
        self,
        path: Path | None,
    ) -> int:

        path = self._resolve_path(path)

        folders = self.scanner.scan(path)

        if not folders:

            self.console.print(
                "[yellow]No movie folders found.[/]"
            )

            return 0

        folder = folders[0]

        feature = self.analyzer.analyze(folder)

        query = self.query_builder.build(folder)

        metadata = self.tmdb.search(query)

        self.console.print()

        self.console.print(
            f"[bold]{folder.name}[/]"
        )

        self.console.print(
            f"Main feature : {feature.path.name}"
        )

        self.console.print(
            f"Runtime      : {feature.duration:.1f} s"
        )

        self.console.print(
            f"Search title : {query.title}"
        )

        if query.year:

            self.console.print(
                f"Search year  : {query.year}"
            )

        self.console.print()

        if metadata is None:

            self.console.print(
                "[red]No TMDb match found.[/]"
            )

            return 0

        self.console.print(
            "[green]TMDb match[/]"
        )

        self.console.print(
            f"Title        : {metadata.title}"
        )

        self.console.print(
            f"Original     : {metadata.original_title}"
        )

        self.console.print(
            f"Language     : {metadata.original_language}"
        )

        self.console.print(
            f"Year         : {metadata.release_year}"
        )

        self.console.print(
            f"TMDb ID      : {metadata.tmdb_id}"
        )

        return 0