from pathlib import Path

import click
import questionary

from structix.utils.config import (
    get_project_config_or_fail,
    load_config,
    save_config,
)
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
def init() -> None:
    """Initialize a new Structix project configuration."""
    click.echo("🔧 Welcome to Structix CLI!")

    previous = load_config()
    if previous:
        if questionary.confirm(
            "⚠️  A configuration already exists. Do you want to reinitialize the project?"
        ).ask():
            click.echo("🔄 Reinitializing the project...")
        else:
            click.echo("🚫 Initialization canceled.")
            return

    stack = questionary.select(
        "🧪 Which tech stack are you using?",
        choices=["NestJS"],
    ).ask()

    architecture = questionary.select(
        "📦 What kind of architecture do you want to generate?",
        choices=["Monolith", "Microservices"],
    ).ask()

    ddd = questionary.confirm("🧠 Apply Domain-Driven Design (DDD)?").ask()
    hex_arch = questionary.confirm("🧩 Apply Hexagonal Architecture?").ask()
    cqrs = questionary.confirm("⚡ Apply CQRS?").ask()

    preferences = {
        "project": {
            "stack": stack,
            "architecture": architecture,
            "ddd": ddd,
            "hexagonal": hex_arch,
            "cqrs": cqrs,
        }
    }

    save_config(preferences)
    click.echo("✅ Preferences saved to structix.config.json")

    create_root_structure()


def create_root_structure() -> None:
    """Create the root structure for the project."""

    config = get_project_config_or_fail()

    root = Path.cwd()

    base = root / config.source_dir

    base.mkdir(parents=True, exist_ok=True)

    if config.ddd and config.hexagonal:
        create_nested_folders(
            base, get_ddd_hexagonal_structure(), add_gitignore=True
        )
    elif config.ddd:
        create_nested_folders(base, get_ddd_structure(), add_gitignore=True)
    elif config.hexagonal:
        create_nested_folders(
            base,
            get_hexagonal_structure(config.cqrs, config.microservice),
            add_gitignore=True,
        )

    click.echo("📂 Project structure created successfully!")
