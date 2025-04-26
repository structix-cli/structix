import click

from structix.commands.proj.add import add
from structix.commands.proj.init import init


@click.group()  # type: ignore
def proj() -> None:
    """Project-related commands."""
    pass


proj.add_command(add)
proj.add_command(init)
