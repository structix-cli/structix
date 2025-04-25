import subprocess
from pathlib import Path

import click

from structix.commands.ops.deploy.ingress import deploy_ingress_resource
from structix.utils.config import get_cluster_config_or_fail


def deploy_microservice_resource(name: str) -> None:
    """Internal function to deploy a single microservice using Helm."""
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    get_cluster_config_or_fail()

    try:
        click.echo(f"🚀 Deploying microservice: {name}")
        subprocess.run(
            ["helm", "upgrade", "--install", name, str(chart_path)], check=True
        )

        deploy_ingress_resource(name)

        click.echo(f"✅ Deployed '{name}' successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Failed to deploy microservice '{name}'.")
        click.echo(f"🔍 Error: {e}")


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
def deploy_microservice(name: str) -> None:
    """Deploy a single microservice using Helm."""
    deploy_microservice_resource(name)
