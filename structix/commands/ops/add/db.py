import shutil
from pathlib import Path

import click
import yaml  # type: ignore

import structix

TEMPLATE_DIR = (
    Path(structix.__file__).parent
    / "utils"
    / "templates"
    / "helm"
    / "templates"
)


def add_db_resource(name: str, db: str) -> None:
    chart_path = Path("ops") / "microservices" / name
    templates_path = chart_path / "templates"
    values_path = chart_path / "values.yaml"

    db_templates = [
        TEMPLATE_DIR / "db" / "db-secret.yaml.j2",
        TEMPLATE_DIR / "db" / "db-service.yaml.j2",
        TEMPLATE_DIR / "db" / f"db-{db}.yaml.j2",
    ]

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    templates_path.mkdir(parents=True, exist_ok=True)

    for template_file in db_templates:
        if not template_file.exists():
            click.echo(f"❌ Template not found: {template_file}")
            return
        destination = templates_path / template_file.name.replace(".j2", "")
        shutil.copyfile(template_file, destination)
        click.echo(f"📄 Copied template: {destination}")

    if values_path.exists():
        with open(values_path) as f:
            values = yaml.safe_load(f) or {}
    else:
        values = {}

    db_defaults = {
        "postgres": {"port": 5432},
        "mysql": {"port": 3306},
        "mongo": {"port": 27017},
        "redis": {"port": 6379},
    }

    values["db"] = {
        "enabled": True,
        "type": db,
        "username": "admin",
        "password": "changeme",
        "database": "appdb",
        "port": db_defaults.get(db, {}).get("port", 5432),
        "storage": "1Gi",
    }

    with open(values_path, "w") as f:
        yaml.dump(values, f, default_flow_style=False, sort_keys=False)

    click.echo(f"📝 Updated values.yaml at {values_path}")


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
def add_db(name: str, db: str) -> None:
    """Add a db resource to an existing microservice."""
    add_db_resource(name, db)
