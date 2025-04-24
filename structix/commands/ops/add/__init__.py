import click

from .microservice import microservice


@click.group()  # type: ignore
def add() -> None:
    """Add new components to your infrastructure."""
    pass


add.add_command(microservice)
