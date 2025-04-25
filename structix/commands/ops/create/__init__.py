import click

from .cluster import create_cluster


@click.group()  # type: ignore
def create() -> None:
    """Create infrastructure components."""
    pass


create.add_command(create_cluster)
