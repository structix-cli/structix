import subprocess

import click


@click.command(name="minikube")  # type: ignore
def start_minikube() -> None:
    """Start the local Minikube cluster."""
    click.echo("🔥 Starting Minikube environment...")
    try:
        subprocess.run(["minikube", "start"], check=True)
        click.echo("✅ Minikube cluster Started.")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to start Minikube cluster.")
        click.echo(f"🔍 Error: {e}")
