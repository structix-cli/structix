import click

from .minikube import destroy_minikube


@click.group()  # type: ignore
def destroy() -> None:
    """Destroy infrastructure components."""
    pass


destroy.add_command(destroy_minikube)
