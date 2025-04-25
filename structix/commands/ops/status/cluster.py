import click

from structix.utils.config import get_cluster_config_or_fail
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def status_cluster() -> None:
    """Show cluster status across nodes, pods, deployments, etc."""
    cluster_config = get_cluster_config_or_fail()

    provider = cluster_config.provider

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "status")

    if not command:
        click.echo(f"❌ 'status' is not supported by provider '{provider}'")
        return

    click.echo(f"🔍 Fetching cluster status for provider: {provider}")
    command()
