import click

from .alertmanager import install_alertmanager
from .grafana import install_grafana
from .ingress import install_ingress
from .prometheus import install_prometheus


@click.group()  # type: ignore
def install() -> None:
    """Install components to your infrastructure."""
    pass


install.add_command(install_ingress)
install.add_command(install_prometheus)
install.add_command(install_alertmanager)
install.add_command(install_grafana)
