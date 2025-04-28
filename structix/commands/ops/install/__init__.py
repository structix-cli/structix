import click

from .ingress import install_ingress
from .prometheus import install_prometheus


@click.group()  # type: ignore
def install() -> None:
    """Install components to your infrastructure."""
    pass


install.add_command(install_ingress)
install.add_command(install_prometheus)
