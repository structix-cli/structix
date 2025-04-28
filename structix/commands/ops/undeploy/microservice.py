import subprocess

import click

from structix.utils.config import get_cluster_config_or_fail


def undeploy_microservice_resource(name: str) -> None:
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


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
def undeploy_microservice(name: str) -> None:
    """Undeploy (delete) a deployed microservice using Helm."""
    undeploy_microservice_resource(name)
