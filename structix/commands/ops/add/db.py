# structix/commands/ops/add/db.py

import shutil
from pathlib import Path

import click

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"


def add_db_resource(name: str, db: str | None) -> None:
    chart_path = Path("ops") / "microservices" / name
    templates_path = chart_path / "templates"
    db_template = TEMPLATE_DIR / "templates" / "db-config.yaml.j2"
    output_path = templates_path / "db-config.yaml"

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    if not db_template.exists():
        click.echo("❌ db-config.yaml.j2 template not found in TEMPLATE_DIR.")
        return

    shutil.copyfile(db_template, output_path)
    click.echo(
        f"🌐 DB resource added for microservice '{name}' at {output_path}"
    )


@click.command(name="db")  # type: ignore
@click.argument("name")  # type: ignore
@click.option(
    "--db",
    type=click.Choice(
        ["postgres", "mysql", "mongo", "redis"], case_sensitive=False
    ),
    required=True,
    help="Database type (required)",
)  # type: ignore
def add_db(name: str, db: str | None) -> None:
    """Add an db resource to an existing microservice."""
    add_db_resource(name, db)
