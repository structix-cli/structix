import click

from .all import deploy_all
from .microservice import deploy_microservice


@click.group()  # type: ignore
def deploy() -> None:
    """Deploy microservices to the current Kubernetes cluster."""
    pass


deploy.add_command(deploy_microservice)
deploy.add_command(deploy_all)
