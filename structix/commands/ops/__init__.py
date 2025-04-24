import click

from structix.commands.ops.init import init


@click.group()  # type: ignore
def ops() -> None:
    """DevOps-related commands."""
    pass


ops.add_command(init, name="init")
