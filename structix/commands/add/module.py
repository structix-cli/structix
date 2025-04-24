from pathlib import Path

import click

from structix.utils.config import get_config
from structix.utils.filesystem import create_nested_folders
from structix.utils.structures.modular_monolith import (
    get_module_structure as get_modular_monolith_module_structure,
)


@click.command()  # type: ignore
@click.argument("name")  # type: ignore
def add_module(name: str) -> None:
    """Scaffold a new module."""
    config = get_config()

    if config.architecture != "Monolith":
        click.echo("⚠️ Modules are only supported in Monolith architecture.")
        return

    root = Path.cwd() / config.source_dir / name

    if root.exists():
        click.echo(f"⚠️ Module '{name}' already exists.")
        return

    click.echo(f"📦 Creating module '{name}'...")

    if config.ddd and config.hexagonal:
        click.echo(
            "⚠️ Modules are only supported in simple architecture without DDD or Hexagonal."
        )
    elif config.ddd:
        click.echo(
            "⚠️ Modules are only supported in simple architecture without DDD or Hexagonal."
        )
    elif config.hexagonal:
        click.echo(
            "⚠️ Modules are only supported in simple architecture without DDD or Hexagonal."
        )
    else:
        create_nested_folders(
            root,
            get_modular_monolith_module_structure(config.cqrs),
            add_gitignore=True,
        )
        return

    click.echo("✅ Context created successfully.")
