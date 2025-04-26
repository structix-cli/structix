import click

import structix
from structix.commands import ops, proj


@click.group()  # type: ignore
@click.version_option(structix.__version__, prog_name="Structix")  # type: ignore
def cli() -> None:
    """Structix CLI - Scaffold clean backend projects."""
    pass


cli.add_command(proj.proj)
cli.add_command(ops.ops)


cli()
