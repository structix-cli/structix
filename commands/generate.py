import click
from pathlib import Path
from utils.config import load_config


@click.group()
def generate():
    """Generate Structix project components."""
    pass


@generate.command("project")
@click.argument("name")
def generate_project(name):
    """Generate project structure in a folder called <name>"""
    config = load_config()
    root = Path.cwd() / name

    if root.exists():
        click.echo("⚠️ Directory already exists.")
        return

    architecture = config.get("architecture")
    ddd = config.get("ddd", False)
    hexagonal = config.get("hexagonal", False)
    cqrs = config.get("cqrs", False)

    root.mkdir(parents=True)
    click.echo(f"📁 Created project: {root}")

    if architecture == "Monolith":
        base = root / "src"
    elif architecture == "Microservices":
        base = root / "services"
    else:
        base = root

    base.mkdir(parents=True)

    if ddd:
        for context in ["example_context"]:
            ctx = base / context
            (ctx / "domain").mkdir(parents=True)
            (ctx / "application").mkdir()
            (ctx / "infrastructure").mkdir()
            if hexagonal:
                (ctx / "interfaces").mkdir()
            if cqrs:
                (ctx / "application/commands").mkdir(parents=True)
                (ctx / "application/queries").mkdir()
            click.echo(f"✅ Generated context: {context}")
    else:
        (base / "example").mkdir(parents=True)
        click.echo("✅ Basic structure generated.")
