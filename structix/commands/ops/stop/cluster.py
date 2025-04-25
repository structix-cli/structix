import click

from structix.utils.config import get_cluster_config_or_fail
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def stop_cluster() -> None:
    """Stop a cluster based on the selected provider."""
    cluster_config = get_cluster_config_or_fail()

    provider = cluster_config.provider

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "stop")

    if not command:
        click.echo(f"❌ 'stop' is not supported by provider '{provider}'")
        return

    click.echo(f"⏹️  Stopping cluster with provider: {provider}")
    command()
