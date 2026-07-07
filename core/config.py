from __future__ import annotations

from pathlib import Path

import yaml


class ConfigManager:

    def __init__(self, filename: str = "config.yaml") -> None:

        self.path = Path(filename)

        if not self.path.exists():
            raise FileNotFoundError(filename)

        with self.path.open("r", encoding="utf8") as f:

            self.config = yaml.safe_load(f)

    def get(self, *keys):

        data = self.config

        for key in keys:
            data = data[key]

        return data