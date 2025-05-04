import re
import shutil
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix
from structix.commands.ops.add.db import add_db_resource
from structix.commands.ops.add.ingress import add_ingress_resource
from structix.commands.ops.deploy.microservice import (
    deploy_microservice_resource,
)
from structix.utils.config import get_config

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
@click.argument("image")  # type: ignore
@click.option(
    "--db",
    type=click.Choice(
        ["postgres", "mysql", "mongo", "redis"], case_sensitive=False
    ),
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
    "--cpu",
    type=str,
    help="CPU request and limit for the container (e.g., 200m)",
)  # type: ignore
@click.option(
    "--memory",
    type=str,
    help="Memory request and limit for the container (e.g., 256Mi)",
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
@click.option(
    "--with-prometheus",
    is_flag=True,
    default=False,
    help="Enable Prometheus annotations and monitoring label",
)  # type: ignore
@click.option(
    "--metrics-port",
    type=int,
    help="Port where metrics are exposed (defaults to container port)",
)  # type: ignore
@click.option(
    "--metrics-path",
    type=str,
    default="/metrics",
    help="Path for the Prometheus scrape endpoint (default: /metrics)",
)  # type: ignore
def add_microservice(
    name: str,
    image: str,
    db: str | None,
    port: int,
    replicas: int,
    cpu: str | None,
    memory: str | None,
    deploy: bool,
    with_ingress: bool,
    with_prometheus: bool,
    metrics_port: int | None,
    metrics_path: str,
) -> None:
    """Add a new Helm chart microservice."""

    config = get_config()

    cpu_regex = re.compile(r"^([0-9]+m|[0-9]+(\.[0-9]+)?)$")
    memory_regex = re.compile(r"^[0-9]+(Ei|Pi|Ti|Gi|Mi|Ki|E|P|T|G|M|K)?$")

    if cpu:
        if not cpu_regex.match(cpu):
            click.echo(
                f"❌ Invalid CPU format: '{cpu}'.\n"
                "💡 Example of valid formats: '100m', '0.5', '1'\n"
                "✅ Allowed units:\n"
                "   - m: milliCPU (1/1000 CPU core)\n"
                "   - 0.5: half of a CPU core\n"
                "   - 1: one CPU core\n"
            )
            return

    if memory:
        if not memory_regex.match(memory):
            click.echo(
                f"❌ Invalid Memory format: '{memory}'.\n"
                "💡 Example of valid formats: '256Mi', '512Mi', '1Gi'\n"
                "✅ Allowed units:\n"
                "   - Ki: kibibytes (1024 bytes)\n"
                "   - Mi: mebibytes (1024 Ki)\n"
                "   - Gi: gibibytes (1024 Mi)\n"
                "   - Ti: tebibytes (1024 Gi)\n"
                "   - Pi: pebibytes (1024 Ti)\n"
                "   - Ei: exbibytes (1024 Pi)\n"
                "   - K: kilobytes (1000 bytes)\n"
                "   - M: megabytes (1000 K)\n"
                "   - G: gigabytes (1000 M)\n"
                "   - T: terabytes (1000 G)\n"
                "   - P: petabytes (1000 T)\n"
                "   - E: exabytes (1000 P)"
            )
            return

    if deploy:
        if not config.cluster:
            click.echo(
                "❌ The '--deploy' option requires a cluster to be set up.\n"
                "💡 Please set up a cluster using 'structix ops init cluster' before deploying."
            )
            return

    ctx = click.get_current_context()
    port_source = ctx.get_parameter_source("metrics_port")
    path_source = ctx.get_parameter_source("metrics_path")

    if not with_prometheus and (
        port_source == click.core.ParameterSource.COMMANDLINE
        or path_source == click.core.ParameterSource.COMMANDLINE
    ):
        click.echo(
            "❌ You must pass '--with-prometheus' to use '--metrics-port' or '--metrics-path'.\n"
            "💡 Example: --with-prometheus --metrics-port=9100 --metrics-path=/custom"
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
        "db_enabled": db is not None,
        "container_port": port,
        "replica_count": replicas,
        "cpu": cpu,
        "memory": memory,
        "expose_metrics": with_prometheus,
        "metrics_port": metrics_port or port,
        "metrics_path": metrics_path,
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

    shutil.copyfile(
        TEMPLATE_DIR / "templates" / "deployment.yaml.j2",
        templates_path / "deployment.yaml",
    )
    shutil.copyfile(
        TEMPLATE_DIR / "templates" / "service.yaml.j2",
        templates_path / "service.yaml",
    )

    if db:
        add_db_resource(name, db)

    if with_ingress:
        add_ingress_resource(name)

    click.echo("✅ Helm chart created!")

    if deploy:
        deploy_microservice_resource(name)
