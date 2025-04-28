import subprocess
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


def install_grafana_resource() -> None:
    try:
        tmp_values_path = Path(".") / "ops" / "tools" / "values-grafana.yaml"

        tmp_values_path.parent.mkdir(parents=True, exist_ok=True)

        context = {
            "prometheus_datasource_url": "http://prometheus-server.monitoring.svc.cluster.local",
        }

        values_template = env.get_template("values-grafana.yaml.j2")
        tmp_values_path.write_text(values_template.render(context))

        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "grafana",
                "https://grafana.github.io/helm-charts",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)
        subprocess.run(
            [
                "helm",
                "install",
                "grafana",
                "grafana/grafana",
                "-f",
                str(tmp_values_path),
            ],
            check=True,
        )
        click.echo("✅ Grafana installed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Grafana: {e}")


@click.command(name="grafana")  # type: ignore
def install_grafana() -> None:
    """Install Grafana dashboard stack using Helm."""
    install_grafana_resource()
