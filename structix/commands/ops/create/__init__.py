import click

from .minikube import create_minikube


@click.group()  # type: ignore
def create() -> None:
    """Create infrastructure components."""
    pass


create.add_command(create_minikube)
