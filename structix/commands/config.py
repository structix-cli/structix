from typing import Any

import click

from structix.utils.config import load_config, save_config


@click.group()  # type: ignore
def config() -> None:
    """Manage Structix configuration."""
    pass


@config.command("set")  # type: ignore
@click.argument("key")  # type: ignore
@click.argument("value")  # type: ignore
def config_set(key: Any, value: Any) -> None:
    config_data = load_config()
    if value.lower() == "true":
        value = True  # type: ignore
    elif value.lower() == "false":
        value = False  # type: ignore

    config_data[key] = value
    save_config(config_data)
    click.echo(f"🔧 Set '{key}' to '{value}'")


@config.command("show")  # type: ignore
def config_show() -> None:
    config_data = load_config()
    click.echo("📋 Current configuration:")
    for k, v in config_data.items():
        click.echo(f"  {k}: {v}")
