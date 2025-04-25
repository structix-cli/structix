import click

from .cluster import stop_cluster


@click.group()  # type: ignore
def stop() -> None:
    """Stop infrastructure components."""
    pass


stop.add_command(stop_cluster)
