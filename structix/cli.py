import click

from structix.commands import add, config, init, ops


@click.group()  # type: ignore
def cli() -> None:
    """Structix CLI - Scaffold clean backend projects."""
    pass


cli.add_command(init.init)
cli.add_command(config.config)
cli.add_command(add.add)
cli.add_command(ops.ops)


cli()
