import click

from structix.utils.config import get_config, no_cluster_config
from structix.utils.ops.providers import get_provider_command


@click.command(name="cluster")  # type: ignore
def expose_cluster() -> None:
    """Expose the cluster using the configured provider (e.g., minikube tunnel)."""
    config = get_config()

    if not config.cluster:
        no_cluster_config()
        return

    provider = config.cluster.provider

    if not provider:
        click.echo("❌ No cluster provider configured.")
        return

    command = get_provider_command(provider, "expose")

    if not command:
        click.echo(f"❌ 'expose' is not supported by provider '{provider}'")
        return

    click.echo(f"🌍 Exposing cluster with provider: {provider}")
    command()
