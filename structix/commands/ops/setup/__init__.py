import click

from .cluster import setup_cluster


@click.group()  # type: ignore
def setup() -> None:
    """Setup infrastructure components."""
    pass


setup.add_command(setup_cluster)
