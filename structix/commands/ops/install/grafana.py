import shutil
import subprocess
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


def install_grafana_resource() -> None:
    try:
        tool_path = Path(".") / "ops" / "tools" / "grafana"
        tool_path.mkdir(parents=True, exist_ok=True)
        tmp_values_path = tool_path / "values-grafana.yaml"
        templates_path = tool_path / "templates"
        templates_path.mkdir(parents=True, exist_ok=True)
        ingress_path = templates_path / "ingress.yaml"
        dashboard_path = templates_path / "dashboard.yaml"

        context = {
            "prometheus_datasource_url": "http://prometheus-server.monitoring.svc.cluster.local",
        }

        values_template = env.get_template("values-grafana.yaml.j2")
        tmp_values_path.write_text(values_template.render(context))

        grafana_template_dir = TEMPLATE_DIR / "templates" / "tools" / "grafana"
        for file in grafana_template_dir.glob("*"):
            if file.is_file():
                target_name = file.name
                if file.suffix == ".j2":
                    target_name = file.with_suffix("").name
                shutil.copy(file, tool_path / "templates" / target_name)

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
                "upgrade",
                "--install",
                "grafana",
                "grafana/grafana",
                "-f",
                str(tmp_values_path),
                "--set",
                "adminUser=admin",
                "--set",
                "adminPassword=changeme123",
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

        subprocess.run(
            [
                "kubectl",
                "apply",
                "-f",
                str(dashboard_path),
            ],
            check=True,
        )

        click.echo("✅ Grafana installed and ingress configured successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Grafana: {e}")


@click.command(name="grafana")  # type: ignore
def install_grafana() -> None:
    """Install Grafana dashboard stack using Helm and configure ingress."""
    install_grafana_resource()
