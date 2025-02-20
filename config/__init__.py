from typing import TypeVar

from .base import Config as _Config


__all__ = ["Config", "get_config"]

Config = TypeVar("Config", bound=_Config)


def get_config() -> _Config:
    return _Config()
