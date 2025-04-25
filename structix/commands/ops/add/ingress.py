import shutil
from pathlib import Path

import click

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"


@click.command(name="ingress")  # type: ignore
@click.argument("name")  # type: ignore
def add_ingress(name: str) -> None:
    """Add an Ingress resource to an existing microservice."""
    chart_path = Path("ops") / "microservices" / name
    templates_path = chart_path / "templates"
    ingress_template = TEMPLATE_DIR / "templates" / "ingress.yaml.j2"
    output_path = templates_path / "ingress.yaml"

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    if not ingress_template.exists():
        click.echo("❌ ingress.yaml.j2 template not found in TEMPLATE_DIR.")
        return

    shutil.copyfile(ingress_template, output_path)
    click.echo(
        f"🌐 Ingress resource added for microservice '{name}' at {output_path}"
    )
