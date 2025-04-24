import click
import questionary

from structix.utils.config import save_config


@click.command(name="cluster")  # type: ignore
def init_cluster() -> None:
    """Initialize cluster provider configuration using an interactive selector."""
    provider = questionary.select(
        "Select cluster provider:", choices=["minikube", "kubeconfig"]
    ).ask()

    if not provider:
        click.echo("❌ Cancelled. No provider selected.")
        return

    save_config({"cluster": {"provider": provider}})
    click.echo(f"✅ Provider '{provider}' saved to structix.config.json")
