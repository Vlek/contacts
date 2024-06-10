"""
Configuration manager

We need to be able to save configurations to a file in a user-friendly
way that will be retrievable later.

If people wish to then save these settings and use them across different
PCs, they should have that option.
"""

import logging
from pathlib import Path

import yaml


DEFAULT_CONFIG_FOLDER: str = "~/.config/contacts"
DEFAULT_CONFIG_FILE_NAME: str = "contacts.yaml"


class Config:
    def __init__(
        self,
        config_file_path: str = f"{DEFAULT_CONFIG_FOLDER}/{DEFAULT_CONFIG_FILE_NAME}",
    ) -> None:
        self._load(config_file_path)

    def _load(self, config_file_path: str) -> None:
        self.config_file_path: Path = Path(config_file_path).expanduser()

        self.config_folder_path: Path = self.config_file_path.parent

        if not self.config_folder_path.exists():
            self.config_folder_path.mkdir()

        if self.config_file_path.exists():
            with self.config_file_path.open() as config_file:
                self.config: dict[str, object] = yaml.safe_load(config_file)
        else:
            self.config: dict[str, object] = {}

    def write(self) -> None:
        """Writes the configuration to the config file."""

        with open(self.config_file_path, "w") as config_file:
            config_file.write(yaml.dump(self.config))
