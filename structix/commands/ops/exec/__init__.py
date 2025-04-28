import click

from .kubectl import exec_kubectl
from .minikube import exec_minikube
from .terraform import exec_terraform


@click.group()  # type: ignore
def exec() -> None:
    """Execute commands in external tools."""
    pass


exec.add_command(exec_kubectl)
exec.add_command(exec_minikube)
exec.add_command(exec_terraform)
