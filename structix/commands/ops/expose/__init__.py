import click

from .cluster import expose_cluster


@click.group()  # type: ignore
def expose() -> None:
    """Expose infrastructure components."""
    pass


expose.add_command(expose_cluster)
