import click
from commands import init as init_cmd
from commands import config as config_cmd


@click.group()
def cli():
    """Structix CLI - Scaffold clean backend projects."""
    pass


cli.add_command(init_cmd.init)
cli.add_command(config_cmd.config)


cli()
