import click

from .microservice import rolling_microservice


@click.group()  # type: ignore
def rolling() -> None:
    """Rolling components in your infrastructure."""
    pass


rolling.add_command(rolling_microservice)
