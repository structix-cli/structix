import click

from structix.utils.config import load_config
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def start_cluster() -> None:
    """Start a cluster based on the selected provider."""
    config = load_config()
    provider = config.get("cluster", {}).get("provider")

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "start")

    if not command:
        click.echo(f"❌ 'start' is not supported by provider '{provider}'")
        return

    click.echo(f"▶️ Starting cluster with provider: {provider}")
    command()
