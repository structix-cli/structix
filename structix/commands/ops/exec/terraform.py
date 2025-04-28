import subprocess

import click


@click.command(name="terraform")  # type: ignore
@click.argument("args", nargs=-1)  # type: ignore
def exec_terraform(args: tuple[str, ...]) -> None:
    """Execute terraform commands with the same arguments."""
    command = ["terraform"] + list(args)

    click.echo(f"📦 Executing: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error executing terraform: {e}")
