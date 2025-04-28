import subprocess
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


def install_alertmanager_resource() -> None:
    try:
        tool_path = Path(".") / "ops" / "tools" / "alertmanager"
        tmp_values_path = tool_path / "values-alertmanager.yaml"
        ingress_path = tool_path / "templates" / "ingress-alertmanager.yaml"

        tool_path.mkdir(parents=True, exist_ok=True)
        templates_path = tool_path / "templates"
        templates_path.mkdir(parents=True, exist_ok=True)

        context = {
            "alertmanager_replicas": 1,
        }

        values_template = env.get_template("values-alertmanager.yaml.j2")
        tmp_values_path.write_text(values_template.render(context))

        ingress_template = env.get_template(
            str(
                Path(".")
                / "templates"
                / "tools"
                / "ingress-alertmanager.yaml.j2"
            )
        )
        ingress_path.write_text(ingress_template.render({}))

        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "prometheus-community",
                "https://prometheus-community.github.io/helm-charts",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)

        subprocess.run(
            [
                "helm",
                "upgrade",
                "--install",
                "alertmanager",
                "prometheus-community/alertmanager",
                "-f",
                str(tmp_values_path),
            ],
            check=True,
        )

        subprocess.run(
            [
                "kubectl",
                "apply",
                "-f",
                str(ingress_path),
            ],
            check=True,
        )

        click.echo(
            "✅ Alertmanager installed and ingress configured successfully."
        )
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Alertmanager: {e}")


@click.command(name="alertmanager")  # type: ignore
def install_alertmanager() -> None:
    """Install Alertmanager stack using Helm and configure ingress."""
    install_alertmanager_resource()
