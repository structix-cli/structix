from pathlib import Path

import click

from structix.utils.config import load_config
from structix.utils.filesystem import create_nested_folders
from structix.utils.structures.ddd_hexagonal import (
    get_root_structure as get_ddd_hexagonal_structure,
)
from structix.utils.structures.domain_driven_design import (
    get_root_structure as get_ddd_structure,
)
from structix.utils.structures.hexagonal_architecture import (
    get_root_structure as get_hexagonal_structure,
)


@click.command()  # type: ignore
@click.argument("name")  # type: ignore
def add_context(name: str) -> None:
    """Scaffold a new DDD context inside /src."""
    config = load_config()
    root = Path.cwd() / "src" / name

    if root.exists():
        click.echo(f"⚠️ Context '{name}' already exists.")
        return

    click.echo(f"📦 Creating context '{name}'...")

    ddd = config.get("ddd", False)
    hexagonal = config.get("hexagonal", False)
    cqrs = config.get("cqrs", False)

    if ddd and hexagonal:
        create_nested_folders(
            root, get_ddd_hexagonal_structure(), add_gitignore=True
        )
    elif ddd:
        create_nested_folders(root, get_ddd_structure(), add_gitignore=True)
    elif hexagonal:
        create_nested_folders(
            root, get_hexagonal_structure(cqrs), add_gitignore=True
        )
    else:
        click.echo("⚠️ No supported architecture selected.")
        return

    click.echo("✅ Context created successfully.")
