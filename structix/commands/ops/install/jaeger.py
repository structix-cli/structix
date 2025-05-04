import subprocess
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


def install_jaeger_resource() -> None:
    try:
        tool_path = Path(".") / "ops" / "tools" / "jaeger"
        tmp_values_path = tool_path / "values-jaeger.yaml"
        ingress_path = tool_path / "templates" / "ingress.yaml"

        tool_path.mkdir(parents=True, exist_ok=True)
        templates_path = tool_path / "templates"
        templates_path.mkdir(parents=True, exist_ok=True)

        context = {"namespace": "observability"}

        values_template = env.get_template("values-jaeger.yaml.j2")
        tmp_values_path.write_text(values_template.render(context))

        ingress_template = env.get_template(
            str(
                Path(".")
                / "templates"
                / "tools"
                / "jaeger"
                / "ingress.yaml.j2"
            )
        )
        ingress_path.write_text(ingress_template.render(context))

        subprocess.run(
            [
                "helm",
                "repo",
                "add",
                "jaegertracing",
                "https://jaegertracing.github.io/helm-charts",
            ],
            check=True,
        )
        subprocess.run(["helm", "repo", "update"], check=True)

        subprocess.run(
            [
                "helm",
                "upgrade",
                "--install",
                "jaeger",
                "jaegertracing/jaeger",
                "-n",
                context["namespace"],
                "--create-namespace",
                "-f",
                str(tmp_values_path),
                "--force",
            ],
            check=True,
        )

        subprocess.run(
            [
                "kubectl",
                "apply",
                "-f",
                str(ingress_path),
                "-n",
                context["namespace"],
            ],
            check=True,
        )

        click.echo("✅ Jaeger installed and ingress configured successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing Jaeger: {e}")


@click.command(name="jaeger")  # type: ignore
def install_jaeger() -> None:
    """Install Jaeger tracing stack using Helm and configure ingress."""
    install_jaeger_resource()
