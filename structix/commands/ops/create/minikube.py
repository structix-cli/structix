import subprocess

import click


@click.command(name="minikube")  # type: ignore
def create_minikube() -> None:
    """Create a local Kubernetes cluster using Minikube with Ingress."""
    click.echo("🚀 Creating Minikube environment...")
    try:
        subprocess.run(["minikube", "start"], check=True)
        click.echo("✅ Minikube cluster created successfully.")

        click.echo("🌐 Enabling Ingress controller...")
        subprocess.run(["minikube", "addons", "enable", "ingress"], check=True)
        click.echo("✅ Ingress controller enabled.")

    except subprocess.CalledProcessError as e:
        click.echo(
            "❌ Failed to create Minikube environment or enable Ingress."
        )
        click.echo(f"🔍 Error: {e}")
