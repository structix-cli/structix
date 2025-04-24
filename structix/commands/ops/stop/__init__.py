import click

from .minikube import stop_minikube


@click.group()  # type: ignore
def stop() -> None:
    """Stop infrastructure components."""
    pass


stop.add_command(stop_minikube)
