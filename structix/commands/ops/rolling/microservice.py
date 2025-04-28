import subprocess
from pathlib import Path

import click

from structix.utils.config import get_cluster_config_or_fail


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
@click.option("--image", required=True, help="Image in repository:tag format")  # type: ignore
def rolling_microservice(name: str, image: str) -> None:
    """Perform a rolling update on a microservice with a new image."""
    chart_path = Path("ops") / "microservices" / name

    if not chart_path.exists():
        click.echo(f"❌ Microservice '{name}' does not exist at {chart_path}")
        return

    get_cluster_config_or_fail()

    if ":" not in image:
        click.echo(
            f"❌ Invalid image format '{image}'. Use repository:tag format."
        )
        return

    repository, tag = image.split(":", 1)

    try:
        click.echo(
            f"🔄 Rolling update microservice '{name}' with image {repository}:{tag} (force pull once)..."
        )

        subprocess.run(
            [
                "helm",
                "upgrade",
                name,
                str(chart_path),
                "--set",
                f"image.repository={repository}",
                "--set",
                f"image.tag={tag}",
                "--set",
                "image.pullPolicy=Always",
            ],
            check=True,
        )

        click.echo(
            f"✅ Rolled '{name}' to image {repository}:{tag} successfully."
        )
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Failed to roll microservice '{name}'.")
        click.echo(f"🔍 Error: {e}")
