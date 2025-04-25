import click

from structix.utils.config import get_config
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def status_cluster() -> None:
    """Show cluster status across nodes, pods, deployments, etc."""
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

    command = get_provider_command(provider, "status")

    if not command:
        click.echo(f"❌ 'status' is not supported by provider '{provider}'")
        return

    click.echo(f"🔍 Fetching cluster status for provider: {provider}")
    command()
