import subprocess

import click

from structix.utils.config import get_cluster_config_or_fail


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
def undeploy_microservice(name: str) -> None:
    """Undeploy (delete) a deployed microservice using Helm."""
    get_cluster_config_or_fail()

    try:
        click.echo(f"🧹 Undeploying microservice '{name}'...")

        subprocess.run(
            ["helm", "uninstall", name],
            check=True,
        )

        click.echo(f"✅ Undeployed '{name}' successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Failed to undeploy microservice '{name}'.")
        click.echo(f"🔍 Error: {e}")
