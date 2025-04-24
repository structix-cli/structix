import click

from structix.commands.add.context import add_context
from structix.commands.add.service import add_service


@click.group()  # type: ignore
def add() -> None:
    """Scaffold architectural structures (e.g. context, service)."""
    pass


add.add_command(add_context, name="context")
add.add_command(add_service, name="service")
