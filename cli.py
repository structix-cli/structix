import click

from commands import config as config_cmd
from commands import generate as generate_cmd
from commands import init as init_cmd


@click.group()  # type: ignore
def cli() -> None:
    """Structix CLI - Scaffold clean backend projects."""
    pass


cli.add_command(init_cmd.init)
cli.add_command(config_cmd.config)
cli.add_command(generate_cmd.generate)


cli()
