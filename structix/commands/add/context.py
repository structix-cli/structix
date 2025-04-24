from pathlib import Path

import click

from structix.utils.config import get_config
from structix.utils.filesystem import create_nested_folders
from structix.utils.structures.ddd_hexagonal import (
    get_module_structure as get_ddd_hexagonal_context_structure,
)
from structix.utils.structures.domain_driven_design import (
    get_module_structure as get_ddd_context_structure,
)


@click.command(name="context")  # type: ignore
@click.argument("name")  # type: ignore
def add_context(name: str) -> None:
    """Scaffold a new DDD context."""
    config = get_config()

    if config.architecture != "Monolith":
        click.echo("⚠️ Contexts are only supported in Monolith architecture.")
        return

    root = Path.cwd() / config.source_dir / name

    if root.exists():
        click.echo(f"⚠️ Context '{name}' already exists.")
        return

    click.echo(f"📦 Creating context '{name}'...")

    if config.ddd and config.hexagonal:
        create_nested_folders(
            root,
            get_ddd_hexagonal_context_structure(config.cqrs),
            add_gitignore=True,
        )
    elif config.ddd:
        create_nested_folders(
            root, get_ddd_context_structure(config.cqrs), add_gitignore=True
        )
    elif config.hexagonal:
        click.echo(
            "⚠️ Contexts are not supported in Hexagonal architecture without DDD."
        )
        return
    else:
        click.echo(
            "⚠️ Contexts are not supported in Monolith architecture without DDD."
        )
        return

    click.echo("✅ Context created successfully.")
