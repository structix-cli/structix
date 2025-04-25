import shutil
import subprocess
from pathlib import Path

import click


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
@click.option(
    "--purge",
    is_flag=True,
    default=False,
    help="Also uninstall the Helm release associated with this microservice",
)  # type: ignore
def remove_microservice(name: str, purge: bool) -> None:
    """Remove an existing Helm chart microservice."""
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    if purge:
        click.echo(f"🗑️ Uninstalling Helm release: {name}")
        try:
            subprocess.run(["helm", "uninstall", name], check=True)
            click.echo("✅ Helm release removed.")
        except subprocess.CalledProcessError as e:
            click.echo("⚠️ Failed to uninstall Helm release.")
            click.echo(f"🔍 Error: {e}")

    click.echo(f"🧹 Deleting files for microservice: {name}")
    shutil.rmtree(chart_path)
    click.echo("✅ Microservice directory removed.")
