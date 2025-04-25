from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix
from structix.utils.config import get_config
from structix.utils.helm import deploy_ingress, deploy_microservice

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
@click.option(
    "--port",
    type=int,
    default=80,
    help="Port the service will expose",
)  # type: ignore
@click.option(
    "--replicas",
    type=int,
    default=1,
    help="Number of replicas for the deployment",
)  # type: ignore
@click.option(
    "--deploy",
    is_flag=True,
    default=False,
    help="Deploy the Helm chart into your current K8s cluster",
)  # type: ignore
@click.option(
    "--with-ingress",
    is_flag=True,
    default=False,
    help="Include an Ingress resource for the microservice",
)  # type: ignore
def microservice(
    name: str,
    image: str,
    db: str | None,
    port: int,
    replicas: int,
    deploy: bool,
    with_ingress: bool,
) -> None:
    """Add a new Helm chart microservice."""

    config = get_config()

    if deploy:
        if not config.cluster:
            click.echo(
                "❌ The '--deploy' option requires a cluster to be set up.\n"
                "💡 Please set up a cluster using 'structix ops init cluster' before deploying."
            )
            return

    chart_path = Path("ops") / "microservices" / name
    templates_path = chart_path / "templates"

    if chart_path.exists():
        click.echo(
            f"❌ Microservice '{name}' already exists at {chart_path}\n💡 Use a different name or remove the existing one."
        )
        return

    chart_path.mkdir(parents=True, exist_ok=True)
    templates_path.mkdir(parents=True, exist_ok=True)

    click.echo(f"📦 Creating Helm chart for: {name}")
    click.echo(f"🐳 Image: {image}")

    image_repo, image_tag = (
        image.split(":") if ":" in image else (image, "latest")
    )

    context = {
        "name": name,
        "image_repo": image_repo,
        "image_tag": image_tag,
        "db": db,
        "db_enabled": db is not None,
        "port": port,
        "replica_count": replicas,
    }

    def render(template_name: str | Path, output_path: Path) -> None:
        relative_template = (
            template_name.relative_to(TEMPLATE_DIR)
            if isinstance(template_name, Path)
            else Path(template_name)
        )
        template = env.get_template(str(relative_template))
        output_path.write_text(template.render(context))

    render(TEMPLATE_DIR / "Chart.yaml.j2", chart_path / "Chart.yaml")
    render(TEMPLATE_DIR / "values.yaml.j2", chart_path / "values.yaml")
    render(
        TEMPLATE_DIR / "templates" / "deployment.yaml.j2",
        templates_path / "deployment.yaml",
    )
    render(
        TEMPLATE_DIR / "templates" / "service.yaml.j2",
        templates_path / "service.yaml",
    )

    if db:
        render(
            TEMPLATE_DIR / "templates" / "db-config.yaml.j2",
            templates_path / "db-config.yaml",
        )
        click.echo(f"🗃️  Added optional DB config for: {db}")

    if with_ingress:
        render(
            TEMPLATE_DIR / "templates" / "ingress.yaml.j2",
            templates_path / "ingress.yaml",
        )
        click.echo("🌐 Added optional Ingress config.")

        if deploy:

            deploy_ingress()

    click.echo("✅ Helm chart created!")

    if deploy:
        deploy_microservice(name)
