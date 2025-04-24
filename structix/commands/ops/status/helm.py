import subprocess

import click


@click.command(name="helm")  # type: ignore
def status_helm() -> None:
    """List Helm releases currently installed."""
    click.echo("📦 Listing Helm releases...")
    try:
        subprocess.run(["helm", "list"], check=True)
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to list Helm releases.")
        click.echo(f"🔍 Error: {e}")
