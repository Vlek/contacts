"""
Configuration manager

We need to be able to save configurations to a file in a user-friendly
way that will be retrievable later.

If people wish to then save these settings and use them across different
PCs, they should have that option.
"""

from pathlib import Path

import yaml


DEFAULT_CONFIG_FOLDER: str = "~/.config/contacts"
DEFAULT_CONFIG_FILE_NAME: str = "contacts.yaml"


class Config:
    def __init__(self, config_folder: str = DEFAULT_CONFIG_FOLDER) -> None:
        config_file_name: str = DEFAULT_CONFIG_FILE_NAME

        self.folder: Path = Path(config_folder)

        if not self.folder.exists:
            self.folder.mkdir()

        self.config_file_path: Path = self.folder / config_file_name

        with open(self.config_file_path, "a+") as config_file:
            self.config: dict[str, object] = yaml.safe_load(config_file)

    def write(self) -> None:
        """Writes the configuration to the config file."""

        with open(self.config_file_path, "w") as config_file:
            config_file.write(yaml.dump(self.config))
