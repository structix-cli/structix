import click

from structix.commands.ops.add import add
from structix.commands.ops.create import create
from structix.commands.ops.deploy import deploy
from structix.commands.ops.destroy import destroy
from structix.commands.ops.exec import exec
from structix.commands.ops.expose import expose
from structix.commands.ops.remove import remove
from structix.commands.ops.rolling import rolling
from structix.commands.ops.scale import scale
from structix.commands.ops.setup import setup
from structix.commands.ops.start import start
from structix.commands.ops.status import status
from structix.commands.ops.stop import stop
from structix.commands.ops.undeploy import undeploy


@click.group()  # type: ignore
def ops() -> None:
    """DevOps-related commands."""
    pass


ops.add_command(add)
ops.add_command(create)
ops.add_command(deploy)
ops.add_command(destroy)
ops.add_command(exec)
ops.add_command(expose)
ops.add_command(setup)
ops.add_command(remove)
ops.add_command(rolling)
ops.add_command(scale)
ops.add_command(start)
ops.add_command(status)
ops.add_command(stop)
ops.add_command(undeploy)
