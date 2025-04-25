import click

from .cluster import status_cluster
from .helm import status_helm


@click.group()  # type: ignore
def status() -> None:
    """Show status of DevOps components."""
    pass


status.add_command(status_cluster)
status.add_command(status_helm)
