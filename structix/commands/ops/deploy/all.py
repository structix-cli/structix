from pathlib import Path

import click

from structix.commands.ops.deploy.microservice import (
    deploy_microservice_resource,
)
from structix.utils.config import get_cluster_config_or_fail


@click.command(name="all")  # type: ignore
def deploy_all() -> None:
    """Deploy all microservices found in ops/microservices."""

    base_path = Path("ops") / "microservices"
    if not base_path.exists():
        click.echo("❌ No microservices directory found.")
        return

    get_cluster_config_or_fail()

    found = False
    for chart in base_path.iterdir():
        if (chart / "Chart.yaml").exists():
            found = True
            deploy_microservice_resource(chart.name)

    if not found:
        click.echo("ℹ️ No Helm charts found in ops/microservices.")
