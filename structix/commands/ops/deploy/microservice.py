import subprocess
from pathlib import Path

import click

from structix.commands.ops.add.microservice import deploy_ingress
from structix.utils.config import get_config, no_cluster_config


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
def deploy_microservice(name: str) -> None:
    """Deploy a single microservice using Helm."""
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    config = get_config()

    if not config.cluster:
        no_cluster_config()
        return

    try:
        click.echo(f"🚀 Deploying microservice: {name}")
        subprocess.run(
            ["helm", "upgrade", "--install", name, str(chart_path)], check=True
        )

        deploy_ingress(name)

        click.echo(f"✅ Deployed '{name}' successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Failed to deploy microservice '{name}'.")
        click.echo(f"🔍 Error: {e}")
