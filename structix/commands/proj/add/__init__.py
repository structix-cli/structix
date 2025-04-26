import click

from structix.commands.proj.add.context import add_context
from structix.commands.proj.add.microservice import add_microservice
from structix.commands.proj.add.module import add_module


@click.group()  # type: ignore
def add() -> None:
    """Scaffold architectural structures (e.g. context, service)."""
    pass


add.add_command(add_context)
add.add_command(add_microservice)
add.add_command(add_module)
