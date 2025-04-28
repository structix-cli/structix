import click

from structix.commands.ops.install.alertmanager import (
    install_alertmanager_resource,
)
from structix.commands.ops.install.grafana import install_grafana_resource
from structix.commands.ops.install.ingress import install_ingress_resource
from structix.commands.ops.install.prometheus import (
    install_prometheus_resource,
)
from structix.utils.config import get_cluster_config_or_fail


@click.command(name="all")  # type: ignore
def install_all() -> None:
    """Install all tools provided by structix."""

    get_cluster_config_or_fail()

    click.echo("🔧 Installing all tools...")
    install_ingress_resource()
    install_prometheus_resource()
    install_alertmanager_resource()
    install_grafana_resource()
    click.echo("✅ All tools installed successfully.")
