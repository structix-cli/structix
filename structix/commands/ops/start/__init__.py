import click

from .minikube import start_minikube


@click.group()  # type: ignore
def start() -> None:
    """Start infrastructure components."""
    pass


start.add_command(start_minikube)
