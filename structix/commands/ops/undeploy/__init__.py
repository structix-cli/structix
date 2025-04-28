import click

from .microservice import undeploy_microservice


@click.group()  # type: ignore
def undeploy() -> None:
    """Undeploy components in your infrastructure."""
    pass


undeploy.add_command(undeploy_microservice)
