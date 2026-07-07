from pathlib import Path

from services.ffprobe_service import FFprobeService


def test_ffprobe_missing_file():

    service = FFprobeService()

    try:
        service.analyze(Path("does_not_exist.mkv"))
    except Exception:
        return

    assert False