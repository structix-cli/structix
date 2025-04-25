# structix/ops/create/cluster.py

import click

from structix.utils.config import get_config
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def create_cluster() -> None:
    """Create a cluster based on the selected provider."""
    config = get_config()

    if not config.cluster:
        click.echo(
            "❌ No cluster configuration found.\n💡 Run `structix ops init cluster` to set up your cluster provider."
        )

        return

    provider = config.cluster.provider

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "create")

    if not command:
        click.echo(f"❌ 'create' is not supported by provider '{provider}'")
        return

    click.echo(f"🚀 Creating cluster with provider: {provider}")
    command()
