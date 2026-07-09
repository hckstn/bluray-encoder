from pathlib import Path

from models.media import MainFeature
from models.media import VideoStream


def test_main_feature():

    feature = MainFeature(
        path=Path("movie.mkv"),
        duration=120.0,
        file_size=123,
        chapters=12,
        video=VideoStream(
            codec="hevc",
            width=3840,
            height=2160,
        ),
    )

    assert feature.video.width == 3840