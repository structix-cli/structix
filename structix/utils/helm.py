import subprocess
from pathlib import Path

import click


def deploy_microservice(service: str) -> None:
    path = Path("ops") / "microservices" / service
    try:
        click.echo("🚀 Deploying Helm chart...")
        subprocess.run(
            ["helm", "upgrade", "--install", service, str(path)],
            check=True,
        )
        click.echo("✅ Helm chart deployed successfully!")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to deploy Helm chart.")
        click.echo(f"🔍 Error: {e}")


def deploy_ingress() -> None:
    """Install ingress-nginx controller if not present."""
    result = subprocess.run(
        ["helm", "status", "ingress-nginx", "-n", "ingress-nginx"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode == 0:
        click.echo("✅ Ingress controller already installed.")
        return

    click.echo("🔧 Ingress controller not found. Installing via Helm...")
    try:
        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "ingress-nginx",
                "https://kubernetes.github.io/ingress-nginx",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)
        subprocess.run(
            [
                "helm",
                "install",
                "ingress-nginx",
                "ingress-nginx/ingress-nginx",
                "--namespace",
                "ingress-nginx",
                "--create-namespace",
                "--version",
                "4.6.0",
                "--set",
                "controller.admissionWebhooks.enabled=false",
                "--set",
                "controller.admissionWebhooks.patch.enabled=false",
                "--set",
                "controller.service.enableHttps=false",
            ],
            check=True,
        )
        click.echo("✅ Ingress controller installed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to install ingress controller.")
        click.echo(f"🔍 Error: {e}")
