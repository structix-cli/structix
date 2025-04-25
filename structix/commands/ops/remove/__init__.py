import click

from .cluster import remove_cluster


@click.group()  # type: ignore
def remove() -> None:
    """Remove infrastructure components."""
    pass


remove.add_command(remove_cluster)
