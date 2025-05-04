import click

from .alertmanager import install_alertmanager
from .all import install_all
from .grafana import install_grafana
from .ingress import install_ingress
from .jaeger import install_jaeger
from .kafka import install_kafka
from .prometheus import install_prometheus


@click.group()  # type: ignore
def install() -> None:
    """Install components to your infrastructure."""
    pass


install.add_command(install_ingress)
install.add_command(install_prometheus)
install.add_command(install_alertmanager)
install.add_command(install_grafana)
install.add_command(install_all)
install.add_command(install_jaeger)
install.add_command(install_kafka)
