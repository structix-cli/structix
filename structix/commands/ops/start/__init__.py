import click

from .cluster import start_cluster


@click.group()  # type: ignore
def start() -> None:
    """Start infrastructure components."""
    pass


start.add_command(start_cluster)
