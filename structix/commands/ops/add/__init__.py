import click

from .db import add_db
from .ingress import add_ingress
from .microservice import add_microservice


@click.group()  # type: ignore
def add() -> None:
    """Add new components to your infrastructure."""
    pass


add.add_command(add_microservice)
add.add_command(add_ingress)
add.add_command(add_db)
