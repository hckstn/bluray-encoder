from __future__ import annotations

import logging

from rich.logging import RichHandler


class Logger:

    @staticmethod
    def create(level: str = "INFO") -> logging.Logger:

        logger = logging.getLogger("bluray_encoder")

        if logger.handlers:
            return logger

        logger.setLevel(level)

        handler = RichHandler(
            rich_tracebacks=True,
            show_time=True,
            show_path=False,
        )

        formatter = logging.Formatter("%(message)s")

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger