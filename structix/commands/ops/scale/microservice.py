import subprocess
from pathlib import Path

import click

from structix.utils.config import get_cluster_config_or_fail


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
@click.option(
    "--replicas",
    type=int,
    required=True,
    help="Number of replicas to scale to.",
)  # type: ignore
def scale_microservice(name: str, replicas: int) -> None:
    """Scale a deployed microservice to the desired number of replicas."""
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    get_cluster_config_or_fail()

    try:
        click.echo(
            f"📈 Scaling microservice '{name}' to {replicas} replicas..."
        )

        subprocess.run(
            [
                "helm",
                "upgrade",
                name,
                str(chart_path),
                "--set",
                f"replicaCount={replicas}",
            ],
            check=True,
        )

        click.echo(f"✅ Scaled '{name}' to {replicas} replicas successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Failed to scale microservice '{name}'.")
        click.echo(f"🔍 Error: {e}")
