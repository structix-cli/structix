import shutil
import subprocess
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


def install_kafka_resource() -> None:
    try:
        tool_path = Path(".") / "ops" / "tools" / "kafka"
        tool_path.mkdir(parents=True, exist_ok=True)
        tmp_values_path = tool_path / "values-kafka.yaml"
        templates_path = tool_path / "templates"
        templates_path.mkdir(parents=True, exist_ok=True)

        context = {
            "replica_count": 1,
            "zookeeper_enabled": True,
            "kraft_enabled": False,
        }

        values_template = env.get_template("values-kafka.yaml.j2")
        tmp_values_path.write_text(values_template.render(context))

        kafka_template_dir = TEMPLATE_DIR / "templates" / "tools" / "kafka"
        for file in kafka_template_dir.glob("*"):
            if file.is_file():
                target_name = file.name
                if file.suffix == ".j2":
                    target_name = file.with_suffix("").name
                shutil.copy(file, templates_path / target_name)

        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "bitnami",
                "https://charts.bitnami.com/bitnami",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)

        subprocess.run(
            [
                "helm",
                "upgrade",
                "--install",
                "kafka",
                "bitnami/kafka",
                "-f",
                str(tmp_values_path),
                "--namespace",
                "kafka",
                "--create-namespace",
            ],
            check=True,
        )

        click.echo("✅ Kafka installed successfully in the 'kafka' namespace.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Kafka: {e}")


@click.command(name="kafka")  # type: ignore
def install_kafka() -> None:
    """Install Apache Kafka using Helm and Bitnami charts."""
    install_kafka_resource()
