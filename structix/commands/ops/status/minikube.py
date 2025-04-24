import subprocess

import click


@click.command(name="minikube")  # type: ignore
def status_minikube() -> None:
    """Show status of Minikube cluster."""
    click.echo("🔍 Checking Minikube status...")
    try:
        subprocess.run(["minikube", "status"], check=True)
    except subprocess.CalledProcessError as e:
        click.echo("❌ Could not get Minikube status.")
        click.echo(f"🔍 Error: {e}")
