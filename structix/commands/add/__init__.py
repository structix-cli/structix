import click

from structix.commands.add.context import add_context
from structix.commands.add.microservice import add_microservice
from structix.commands.add.module import add_module


@click.group()  # type: ignore
def add() -> None:
    """Scaffold architectural structures (e.g. context, service)."""
    pass


add.add_command(add_context)
add.add_command(add_microservice)
add.add_command(add_module)
