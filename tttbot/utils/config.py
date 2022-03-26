import yaml
from pathlib import Path

import logging

logger = logging.getLogger(__name__)

from typing import *


class Config:
    """
    Loads a yaml config file and provides access to the config dictionary through class methods.

    :param path: Path to the config file.
    :param default_config_path: Path to the default config file. Default is "data/default_config.yml".
    :return: None
    """

    def __init__(
        self,
        path: Union[Path, str],
        default_config_path: Union[Path, str] = Path("data", "default_config.yml"),
    ):

        self.default_config_path: Path = Path(default_config_path)
        self._config: Dict[str, Any] = load_yaml(self.default_config_path)
        self.path: Path = Path(path)
        self.update_config(
            load_yaml(self.path)
        )  # replace the default config with user config

    def update_config(self, config_dict: Dict[str, Any]):
        """
        Updates the config dictionary with the given config_dict. Will only update keys that already exist.

        :param config_dict: The config dictionary to update the config with.
        """

        for key, val in config_dict.items():
            if key in self:
                self[key] = val
            else:
                logger.warning(f"Config key {key} not found in default config.")

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __setitem__(self, key: str, value: Any):
        self._config[key] = value

    def __iter__(self) -> Iterator[str]:
        return iter(self._config)

    def __contains__(self, key: str) -> bool:
        return key in self._config

    def get(self, key: str, default: Any) -> Any:
        return self._config.get(key, default)


def load_yaml(path: Path):

    if not path.exists():
        raise FileNotFoundError(f"Config file {path} not found.")

    with open(path, "r") as stream:
        return yaml.safe_load(stream)
