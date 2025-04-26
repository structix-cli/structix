from pathlib import Path

import click
import questionary
import yaml  # type: ignore

from structix.utils.config import get_config, save_config

STRUCTIX_DIR = Path.cwd() / ".structix"
KUBECONFIG_PATH = STRUCTIX_DIR / "kubeconfig.yaml"


@click.command(name="cluster")  # type: ignore
def setup_cluster() -> None:
    """Setup cluster provider configuration using an interactive selector."""

    config = get_config()

    if config.cluster:
        click.echo(
            "❌ Cluster configuration already exists.\n💡 Run `structix ops remove cluster` to remove the existing configuration."
        )
        return

    provider = questionary.select(
        "Select cluster provider:", choices=["minikube", "kubeconfig"]
    ).ask()

    if not provider:
        click.echo("❌ Cancelled. No provider selected.")
        return

    config_data = {"cluster": {"provider": provider}}

    if provider == "kubeconfig":
        method = questionary.select(
            "How do you want to provide the kubeconfig?",
            choices=[
                "Enter a path to an existing kubeconfig file",
                "Paste kubeconfig content directly",
            ],
        ).ask()

        STRUCTIX_DIR.mkdir(exist_ok=True)

        if method == "Enter a path to an existing kubeconfig file":
            path = questionary.path(
                "Enter the full path to your kubeconfig file"
            ).ask()
            if path and Path(path).exists():
                content = Path(path).read_text()
            else:
                click.echo("❌ Invalid path provided.")
                return

        elif method == "Paste kubeconfig content directly":
            content = questionary.text(
                "Paste your kubeconfig content here:"
            ).ask()
            if not content:
                click.echo("❌ No content provided.")
                return

        try:
            parsed = yaml.safe_load(content)
            if (
                not isinstance(parsed, dict)
                or "clusters" not in parsed
                or "contexts" not in parsed
            ):
                raise ValueError("Missing required keys: clusters or contexts")
        except Exception as e:
            click.echo(f"❌ Invalid kubeconfig: {e}")
            return

        KUBECONFIG_PATH.write_text(content)
        config_data["cluster"]["kubeconfig"] = str(KUBECONFIG_PATH)
        click.echo(f"✅ Kubeconfig saved to {KUBECONFIG_PATH}")

    save_config(config_data)
    click.echo(f"✅ Provider '{provider}' configuration saved.")
