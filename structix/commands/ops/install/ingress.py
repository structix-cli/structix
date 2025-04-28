import subprocess

import click

from structix.utils.config import get_cluster_config_or_fail


def install_ingress_resource() -> None:

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
def install_ingress() -> None:
    """Install an Ingress Controller using Helm."""
    install_ingress_resource()
