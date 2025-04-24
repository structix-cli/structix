import click

from .helm import status_helm
from .minikube import status_minikube


@click.group()  # type: ignore
def status() -> None:
    """Show status of DevOps components."""
    pass


status.add_command(status_minikube)
status.add_command(status_helm)
