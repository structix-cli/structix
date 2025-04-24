import subprocess
from pathlib import Path

import click


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
def deploy_microservice(name: str) -> None:
    """Deploy a single microservice using Helm."""
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    try:
        click.echo(f"🚀 Deploying microservice: {name}")
        subprocess.run(
            ["helm", "upgrade", "--install", name, str(chart_path)], check=True
        )
        click.echo(f"✅ Deployed '{name}' successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Failed to deploy microservice '{name}'.")
        click.echo(f"🔍 Error: {e}")
