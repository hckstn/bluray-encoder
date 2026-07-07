"""
Application entry point.
"""

from __future__ import annotations

from pathlib import Path

from rich.console import Console

from core.cli import CLI
from core.config import ConfigManager
from services.directory_scanner import DirectoryScanner


class Application:

    VERSION = "0.2.0"

    def __init__(self) -> None:

        self.console = Console()
        self.config = ConfigManager()

    def run(self) -> int:

        args = CLI.build().parse_args()

        self.console.print(
            f"[bold cyan]BluRay Encoder[/] {self.VERSION}"
        )

        match args.command:

            case "scan":
                return self.scan(args.path)

        return 0

    def scan(
        self,
        path: Path | None,
    ) -> int:

        if path is None:

            path = Path(
                self.config.get(
                    "paths",
                    "remux",
                )
            )

        path = path.expanduser().resolve()

        self.console.print()
        self.console.print(
            f"Scanning [cyan]{path}[/]..."
        )

        scanner = DirectoryScanner()

        movies = scanner.scan(path)

        self.console.print()

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