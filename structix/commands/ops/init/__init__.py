# structix/ops/init/__init__.py
import click

from .cluster import init_cluster


@click.group()  # type: ignore
def init() -> None:
    """Initialize infrastructure components."""
    pass


init.add_command(init_cluster)
