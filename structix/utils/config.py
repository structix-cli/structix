import json
from pathlib import Path
from typing import Any, Dict

import click

from structix.utils.types import ArchitectureType, StackType

CONFIG_FILE = Path.cwd() / "structix.config.json"


class Config:
    stack: StackType
    architecture: ArchitectureType
    ddd: bool
    hexagonal: bool
    cqrs: bool

    def __init__(
        self,
        stack: StackType,
        architecture: ArchitectureType,
        ddd: bool,
        hexagonal: bool,
        cqrs: bool,
    ) -> None:
        self.stack = stack
        self.architecture = architecture
        self.ddd = ddd
        self.hexagonal = hexagonal
        self.cqrs = cqrs


def get_config() -> Config:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config_data = json.load(f)
            return Config(
                stack=config_data.get("stack", "NestJS"),
                architecture=config_data.get("architecture", "Monolith"),
                ddd=config_data.get("ddd", False),
                hexagonal=config_data.get("hexagonal", False),
                cqrs=config_data.get("cqrs", False),
            )

    click.echo("⚠️ Error: No configuration found.")
    exit(1)


def load_config() -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)  # type: ignore
    return {}


def save_config(config: Dict[str, Any]) -> None:
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
