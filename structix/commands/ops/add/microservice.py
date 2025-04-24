from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
@click.argument("image")  # type: ignore
@click.option(
    "--db",
    type=click.Choice(["postgres", "mysql", "mongo"], case_sensitive=False),
    help="Optional database",
)  # type: ignore
def microservice(name: str, image: str, db: str | None) -> None:
    """Add a new Helm chart microservice."""
    click.echo(f"📦 Creating Helm chart for: {name}")
    click.echo(f"🐳 Image: {image}")

    chart_path = Path("infra") / "helm" / name
    templates_path = chart_path / "templates"
    chart_path.mkdir(parents=True, exist_ok=True)
    templates_path.mkdir(parents=True, exist_ok=True)

    image_repo, image_tag = (
        image.split(":") if ":" in image else (image, "latest")
    )

    context = {
        "name": name,
        "image_repo": image_repo,
        "image_tag": image_tag,
        "db": db,
        "db_enabled": db is not None,
    }

    def render(template_name: str, output_path: Path) -> None:
        template = env.get_template(template_name)
        output_path.write_text(template.render(context))

    render("Chart.yaml.j2", chart_path / "Chart.yaml")
    render("values.yaml.j2", chart_path / "values.yaml")
    render("templates/deployment.yaml.j2", templates_path / "deployment.yaml")
    render("templates/service.yaml.j2", templates_path / "service.yaml")

    if db:
        render(
            "templates/db-config.yaml.j2", templates_path / "db-config.yaml"
        )
        click.echo(f"🗃️  Added optional DB config for: {db}")

    click.echo("✅ Helm chart created!")
