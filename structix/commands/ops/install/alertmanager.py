import subprocess

import click


@click.command(name="alertmanager")  # type: ignore
def add_alertmanager() -> None:
    """Add Alertmanager stack using Helm."""
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
                "alertmanager",
                "prometheus-community/alertmanager",
            ],
            check=True,
        )
        click.echo("✅ Alertmanager installed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Alertmanager: {e}")
