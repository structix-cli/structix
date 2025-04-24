import subprocess

import click


@click.command(name="minikube")  # type: ignore
def stop_minikube() -> None:
    """Stop the local Minikube cluster."""
    click.echo("🔥 Stopping Minikube environment...")
    try:
        subprocess.run(["minikube", "stop"], check=True)
        click.echo("✅ Minikube cluster stopped.")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to stop Minikube cluster.")
        click.echo(f"🔍 Error: {e}")
