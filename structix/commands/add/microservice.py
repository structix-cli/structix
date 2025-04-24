from pathlib import Path

import click

from structix.utils.config import get_config
from structix.utils.filesystem import create_nested_folders
from structix.utils.structures.ddd_hexagonal import (
    get_module_structure as get_ddd_hexagonal_microservice_structure,
)
from structix.utils.structures.domain_driven_design import (
    get_module_structure as get_ddd_microservice_structure,
)
from structix.utils.structures.hexagonal_architecture import (
    get_module_structure as get_hexagonal_microservice_structure,
)
from structix.utils.structures.modular_monolith import (
    get_module_structure as get_modular_monolith_microservice_structure,
)


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
def add_microservice(name: str) -> None:
    """Scaffold a new microservice."""
    config = get_config()

    if config.architecture != "Microservices":
        click.echo(
            "⚠️ Microservice are only supported in Microservices architecture."
        )
        return

    root = Path.cwd() / config.source_dir / name

    if root.exists():
        click.echo(f"⚠️ Microservice '{name}' already exists.")
        return

    root.mkdir(parents=True, exist_ok=True)

    click.echo(f"🚀 Creating microservice '{name}'...")

    if config.ddd and config.hexagonal:
        create_nested_folders(
            root,
            get_ddd_hexagonal_microservice_structure(config.cqrs),
            add_gitignore=True,
        )
    elif config.ddd:
        create_nested_folders(
            root,
            get_ddd_microservice_structure(config.cqrs),
            add_gitignore=True,
        )
    elif config.hexagonal:
        create_nested_folders(
            root,
            get_hexagonal_microservice_structure(config.cqrs),
            add_gitignore=True,
        )
    else:
        create_nested_folders(
            root,
            get_modular_monolith_microservice_structure(config.cqrs),
            add_gitignore=True,
        )

    click.echo("✅ Microservice created successfully.")
