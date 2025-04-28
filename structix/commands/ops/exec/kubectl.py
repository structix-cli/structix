import subprocess

import click


@click.command(name="kubectl")  # type: ignore
@click.argument("args", nargs=-1)  # type: ignore
def exec_kubectl(args: tuple[str, ...]) -> None:
    """Execute kubectl commands with the same arguments."""
    command = ["kubectl"] + list(args)

    click.echo(f"📦 Executing: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error executing kubectl: {e}")
