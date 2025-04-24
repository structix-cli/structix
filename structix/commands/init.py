from pathlib import Path

import click
import questionary

from structix.utils.config import load_config, save_config
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
    print("🔧 Welcome to Structix CLI!")

    previous = load_config()
    if previous:
        if questionary.confirm(
            "⚠️ A configuration already exists. Do you want to reinitialize the project?"
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
        "stack": stack,
        "architecture": architecture,
        "ddd": ddd,
        "hexagonal": hex_arch,
        "cqrs": cqrs,
    }

    save_config(preferences)
    click.echo("✅ Preferences saved to structix.config.json")


def create_root_structure() -> None:
    """Create the root structure for the project."""

    config = load_config()
    root = Path.cwd() / "src"

    if root.exists():
        click.echo("⚠️ Directory already exists.")
        return

    architecture = str(config.get("architecture"))
    ddd = config.get("ddd", False)
    hexagonal = config.get("hexagonal", False)
    cqrs = config.get("cqrs", False)

    root.mkdir(parents=True)
    click.echo(f"📁 Created project: {root}")

    base = {"Monolith": root / "src", "Microservices": root / "services"}.get(
        architecture, root
    )

    base.mkdir(parents=True)

    if ddd and hexagonal:
        create_nested_folders(base, get_ddd_hexagonal_structure())
    elif ddd:
        create_nested_folders(base, get_ddd_structure())
    elif hexagonal:
        create_nested_folders(base, get_hexagonal_structure(cqrs))
