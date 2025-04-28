import subprocess

import click


@click.command(name="prometheus")  # type: ignore
def install_prometheus() -> None:
    """Install Prometheus monitoring stack using Helm."""
    try:
        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "prometheus-community",
                "https://prometheus-community.github.io/helm-charts",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)
        subprocess.run(
            [
                "helm",
                "install",
                "prometheus",
                "prometheus-community/prometheus",
            ],
            check=True,
        )
        click.echo("✅ Prometheus installed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Prometheus: {e}")
