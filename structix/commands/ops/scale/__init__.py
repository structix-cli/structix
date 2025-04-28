import click

from .microservice import scale_microservice


@click.group()  # type: ignore
def scale() -> None:
    """Scale components in your infrastructure."""
    pass


scale.add_command(scale_microservice)
