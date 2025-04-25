import subprocess
from pathlib import Path

import click

from structix.utils.config import get_cluster_config_or_fail


def deploy_ingress_resource(name: str) -> None:
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    ingress_path = chart_path / "templates" / "ingress.yaml"
    if not ingress_path.exists():
        click.echo(f"❌ Ingress resource not found for microservice '{name}'.")
        return

    get_cluster_config_or_fail()

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


@click.command(name="ingress")  # type: ignore
@click.argument("name")  # type: ignore
def deploy_ingress(name: str) -> None:
    """Deploy an Ingress resource for a microservice."""
    deploy_ingress_resource(name)
