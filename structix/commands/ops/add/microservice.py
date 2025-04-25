import subprocess
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

import structix

TEMPLATE_DIR = Path(structix.__file__).parent / "utils" / "templates" / "helm"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


@click.command(name="microservice")  # type: ignore
@click.argument("name")  # type: ignore
@click.argument("image")  # type: ignore
@click.option(
    "--db",
    type=click.Choice(["postgres", "mysql", "mongo"], case_sensitive=False),
    help="Optional database",
)  # type: ignore
@click.option(
    "--deploy",
    is_flag=True,
    default=False,
    help="Deploy the Helm chart into your current K8s cluster",
)  # type: ignore
@click.option(
    "--with-ingress",
    is_flag=True,
    default=False,
    help="Include an Ingress resource for the microservice",
)  # type: ignore
def microservice(
    name: str, image: str, db: str | None, deploy: bool, with_ingress: bool
) -> None:
    """Add a new Helm chart microservice."""

    chart_path = Path("ops") / "microservices" / name
    templates_path = chart_path / "templates"

    if chart_path.exists():
        click.echo(
            f"❌ Microservice '{name}' already exists at {chart_path}\n💡 Use a different name or remove the existing one."
        )
        return

    chart_path.mkdir(parents=True, exist_ok=True)
    templates_path.mkdir(parents=True, exist_ok=True)

    click.echo(f"📦 Creating Helm chart for: {name}")
    click.echo(f"🐳 Image: {image}")

    image_repo, image_tag = (
        image.split(":") if ":" in image else (image, "latest")
    )

    context = {
        "name": name,
        "image_repo": image_repo,
        "image_tag": image_tag,
        "db": db,
        "db_enabled": db is not None,
    }

    def render(template_name: str, output_path: Path) -> None:
        template = env.get_template(template_name)
        output_path.write_text(template.render(context))

    render("Chart.yaml.j2", chart_path / "Chart.yaml")
    render("values.yaml.j2", chart_path / "values.yaml")
    render("deployment.yaml.j2", templates_path / "deployment.yaml")
    render("service.yaml.j2", templates_path / "service.yaml")

    if db:
        render("db-config.yaml.j2", templates_path / "db-config.yaml")
        click.echo(f"🗃️  Added optional DB config for: {db}")

    if with_ingress:
        render("ingress.yaml.j2", templates_path / "ingress.yaml")
        click.echo("🌐 Added optional Ingress config.")

        deploy_ingress(templates_path, apply_standalone=not deploy)

    click.echo("✅ Helm chart created!")

    if deploy:
        try:
            click.echo("🚀 Deploying Helm chart...")
            subprocess.run(
                ["helm", "upgrade", "--install", name, str(chart_path)],
                check=True,
            )
            click.echo("✅ Helm chart deployed successfully!")
        except subprocess.CalledProcessError as e:
            click.echo("❌ Failed to deploy Helm chart.")
            click.echo(f"🔍 Error: {e}")


def deploy_ingress(templates_path: Path, apply_standalone: bool) -> None:
    try:
        result = subprocess.run(
            ["helm", "status", "ingress-nginx", "-n", "ingress-nginx"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode != 0:
            click.echo(
                "🔧 Ingress controller not found. Installing via Helm..."
            )

            subprocess.run(
                [
                    "helm",
                    "repo",
                    "add",
                    "ingress-nginx",
                    "https://kubernetes.github.io/ingress-nginx",
                ],
                check=True,
            )
            subprocess.run(["helm", "repo", "update"], check=True)

            subprocess.run(
                [
                    "helm",
                    "install",
                    "ingress-nginx",
                    "ingress-nginx/ingress-nginx",
                    "--namespace",
                    "ingress-nginx",
                    "--create-namespace",
                    "--version",
                    "4.6.0",
                    "--set",
                    "controller.admissionWebhooks.enabled=false",
                    "--set",
                    "controller.admissionWebhooks.patch.enabled=false",
                    "--set",
                    "controller.service.enableHttps=false",
                ],
                check=True,
            )
            click.echo("✅ Ingress controller installed successfully.")
        else:
            click.echo("✅ Ingress controller already installed.")

        if apply_standalone:
            click.echo("🚀 Deploying Ingress resource...")
            subprocess.run(
                [
                    "minikube",
                    "kubectl",
                    "--",
                    "apply",
                    "-f",
                    str(templates_path / "ingress.yaml"),
                ],
                check=True,
            )
            click.echo("✅ Ingress resource deployed successfully.")

    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to deploy Ingress controller or resource.")
        click.echo(f"🔍 Error: {e}")
