import click

from structix.utils.config import load_config
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def destroy_cluster() -> None:
    """Destroy a cluster based on the selected provider."""
    config = load_config()
    provider = config.get("cluster", {}).get("provider")

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "destroy")

    if not command:
        click.echo(f"❌ 'destroy' is not supported by provider '{provider}'")
        return

    click.echo(f"💣 Destroying cluster with provider: {provider}")
    command()
