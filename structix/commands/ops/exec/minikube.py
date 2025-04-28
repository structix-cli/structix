import subprocess

import click


@click.command(name="minikube")  # type: ignore
@click.argument("args", nargs=-1)  # type: ignore
def exec_minikube(args: tuple[str, ...]) -> None:
    """Execute minikube commands with the same arguments."""
    command = ["minikube"] + list(args)

    click.echo(f"📦 Executing: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error executing minikube: {e}")
