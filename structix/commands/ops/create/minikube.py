import subprocess

import click


@click.command(name="minikube")  # type: ignore
def create_minikube() -> None:
    """Create a local Kubernetes cluster using Minikube."""
    click.echo("🚀 Creating Minikube environment...")
    try:
        subprocess.run(["minikube", "start"], check=True)
        click.echo("✅ Minikube cluster created successfully.")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to create Minikube cluster.")
        click.echo(f"🔍 Error: {e}")
