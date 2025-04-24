import click

from structix.commands.ops.add import add
from structix.commands.ops.init import init


@click.group()  # type: ignore
def ops() -> None:
    """DevOps-related commands."""
    pass


ops.add_command(init)
ops.add_command(add)
