import subprocess

import click


@click.command(name="minikube")  # type: ignore
def destroy_minikube() -> None:
    """Destroy the local Minikube cluster."""
    click.echo("🔥 Destroying Minikube environment...")
    try:
        subprocess.run(["minikube", "delete"], check=True)
        click.echo("✅ Minikube cluster destroyed.")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to destroy Minikube cluster.")
        click.echo(f"🔍 Error: {e}")
