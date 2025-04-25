import click

from .cluster import remove_cluster
from .microservice import remove_microservice


@click.group()  # type: ignore
def remove() -> None:
    """Remove infrastructure components."""
    pass


remove.add_command(remove_cluster)
remove.add_command(remove_microservice)
