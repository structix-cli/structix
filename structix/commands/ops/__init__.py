import click

from structix.commands.ops.add import add
from structix.commands.ops.create import create
from structix.commands.ops.deploy import deploy
from structix.commands.ops.destroy import destroy
from structix.commands.ops.init import init
from structix.commands.ops.start import start
from structix.commands.ops.status import status
from structix.commands.ops.stop import stop


@click.group()  # type: ignore
def ops() -> None:
    """DevOps-related commands."""
    pass


ops.add_command(init)
ops.add_command(add)
ops.add_command(destroy)
ops.add_command(create)
ops.add_command(deploy)
ops.add_command(status)
ops.add_command(start)
ops.add_command(stop)
