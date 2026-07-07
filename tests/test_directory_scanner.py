from pathlib import Path

from services.directory_scanner import DirectoryScanner


def test_empty_directory(tmp_path: Path):

    scanner = DirectoryScanner()

    movies = scanner.scan(tmp_path)

    assert movies == []