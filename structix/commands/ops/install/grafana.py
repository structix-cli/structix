import subprocess

import click


@click.command(name="grafana")  # type: ignore
def add_grafana() -> None:
    """Add Grafana dashboard stack using Helm."""
    try:
        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "grafana",
                "https://grafana.github.io/helm-charts",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)
        subprocess.run(
            ["helm", "install", "grafana", "grafana/grafana"], check=True
        )
        click.echo("✅ Grafana installed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Grafana: {e}")
