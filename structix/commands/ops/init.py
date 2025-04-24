from pathlib import Path

import click
import questionary


@click.command(name="init")  # type: ignore
def init() -> None:
    """Initialize infrastructure (Kubernetes, Terraform, etc.)"""
    print("🚀 Initializing Infrastructure Setup!")

    if (
        Path("ops").exists()
        and not questionary.confirm(
            "⚠️ 'ops' folder already exists. Overwrite?"
        ).ask()
    ):
        click.echo("🚫 Infrastructure setup canceled.")
        return

    include_k8s = questionary.confirm("☸️  Include Kubernetes manifests?").ask()
    include_helm = questionary.confirm("📦 Include Helm charts?").ask()
    include_tf = questionary.confirm("🌍 Include Terraform configs?").ask()
    include_ci = questionary.confirm(
        "⚙️  Include GitHub Actions workflow?"
    ).ask()

    ops_path = Path("ops")
    ops_path.mkdir(exist_ok=True)

    if include_k8s:
        (ops_path / "k8s").mkdir(parents=True, exist_ok=True)
    if include_helm:
        (ops_path / "helm").mkdir(parents=True, exist_ok=True)
    if include_tf:
        (ops_path / "terraform").mkdir(parents=True, exist_ok=True)
    if include_ci:
        (Path(".github") / "workflows").mkdir(parents=True, exist_ok=True)

    click.echo("✅ Infrastructure scaffold complete.")
