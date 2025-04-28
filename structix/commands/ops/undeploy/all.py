from pathlib import Path

import click

from structix.commands.ops.undeploy.microservice import (
    undeploy_microservice_resource,
)
from structix.utils.config import get_cluster_config_or_fail


@click.command(name="all")  # type: ignore
def undeploy_all() -> None:
    """Undeploy all microservices found in ops/microservices."""

    base_path = Path("ops") / "microservices"
    if not base_path.exists():
        click.echo("❌ No microservices directory found.")
        return

    get_cluster_config_or_fail()

    found = False
    for chart in base_path.iterdir():
        if (chart / "Chart.yaml").exists():
            found = True
            undeploy_microservice_resource(chart.name)

    if not found:
        click.echo("ℹ️ No Helm charts found in ops/microservices.")
