import subprocess
from pathlib import Path

import click


@click.command(name="all")  # type: ignore
def deploy_all() -> None:
    """Deploy all microservices found in ops/microservices."""
    base_path = Path("ops") / "microservices"
    if not base_path.exists():
        click.echo("❌ No microservices directory found.")
        return

    found = False
    for chart in base_path.iterdir():
        if (chart / "Chart.yaml").exists():
            found = True
            try:
                click.echo(f"🚀 Deploying microservice: {chart.name}")
                subprocess.run(
                    ["helm", "upgrade", "--install", chart.name, str(chart)],
                    check=True,
                )
                click.echo(f"✅ Deployed '{chart.name}' successfully.")
            except subprocess.CalledProcessError as e:
                click.echo(f"❌ Failed to deploy '{chart.name}'.")
                click.echo(f"🔍 Error: {e}")

    if not found:
        click.echo("ℹ️ No Helm charts found in ops/microservices.")
