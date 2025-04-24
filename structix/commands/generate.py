# === Refactor of generate_project using imported structures ===

from pathlib import Path
from typing import Any, Dict

import click

from structix.utils.config import load_config
from structix.utils.structures import (
    DDD_CQRS_STRUCTURE,
    DDD_STRUCTURE,
    HEXAGONAL_STRUCTURE,
)


@click.group()  # type: ignore
def generate() -> None:
    """Generate Structix project components."""
    pass


def create_nested_folders(base: Path, structure: Dict[str, Any]) -> None:
    for key, value in structure.items():
        subpath = base / key
        if isinstance(value, list):
            for folder in value:
                (subpath / folder).mkdir(parents=True, exist_ok=True)
        elif isinstance(value, dict):
            (subpath).mkdir(parents=True, exist_ok=True)
            create_nested_folders(subpath, value)
        else:
            (subpath / value).mkdir(parents=True, exist_ok=True)


@generate.command("project")  # type: ignore
@click.argument("name")  # type: ignore
def generate_project(name: Any) -> None:
    """Generate project structure in a folder called <name>"""
    config = load_config()
    root = Path.cwd() / name

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

    if ddd:
        for context in ["example_context"]:
            ctx = base / context
            ctx.mkdir(parents=True, exist_ok=True)

            create_nested_folders(ctx, DDD_STRUCTURE)
            if hexagonal:
                create_nested_folders(ctx, HEXAGONAL_STRUCTURE)
            if cqrs:
                create_nested_folders(ctx, DDD_CQRS_STRUCTURE)

            click.echo(f"✅ Generated DDD context: {context}")
    else:
        (base / "example").mkdir(parents=True)
        click.echo("✅ Basic structure generated.")
