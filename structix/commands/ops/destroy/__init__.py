import click

from .cluster import destroy_cluster


@click.group()  # type: ignore
def destroy() -> None:
    """Destroy infrastructure components."""
    pass


destroy.add_command(destroy_cluster)
