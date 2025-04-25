# structix/core/providers.py
import os
import subprocess
from typing import Callable, Dict, List

import click

from structix.utils.config import force_save_config, get_config, load_config

PROVIDER_ACTIONS: Dict[str, List[str]] = {
    "minikube": [
        "init",
        "create",
        "start",
        "stop",
        "destroy",
        "remove",
        "status",
        "expose",
    ],
    "kubeconfig": ["init", "remove", "status"],
}


def is_action_supported(provider: str, action: str) -> bool:
    return action in PROVIDER_ACTIONS.get(provider, [])


def remove_cluster() -> None:
    config = get_config()
    if not config.cluster:
        click.echo("⚠️ No cluster configuration found.")
        return

    raw_config = load_config()
    raw_config.pop("cluster", None)
    force_save_config(raw_config)
    click.echo("🗑️ Cluster config removed from structix.config.json")


def status_cluster() -> None:
    config = get_config()

    if not config.cluster or not config.cluster.provider:
        click.echo("❌ Cluster not configured. Run: structix ops init cluster")
        raise SystemExit(1)

    provider = config.cluster.provider
    env = os.environ.copy()
    if config.cluster.kubeconfig:
        env["KUBECONFIG"] = config.cluster.kubeconfig

    click.echo(f"🔍 Cluster Provider: {provider}")

    try:
        subprocess.run(["kubectl", "get", "nodes"], check=True, env=env)
        click.echo()
        subprocess.run(["kubectl", "get", "pods", "-A"], check=True, env=env)
        click.echo()
        subprocess.run(
            ["kubectl", "get", "deployments", "-A"], check=True, env=env
        )
        click.echo()
        subprocess.run(
            ["kubectl", "get", "ingress", "-A"], check=True, env=env
        )
        click.echo()
        subprocess.run(["helm", "list", "-A"], check=True, env=env)
    except subprocess.CalledProcessError as e:
        click.echo("❌ Could not retrieve full cluster status.")
        click.echo(f"🔍 Error: {e}")


def expose_cluster() -> None:
    config = get_config()

    if not config.cluster or config.cluster.provider != "minikube":
        click.echo("⚠️  Expose is only supported for Minikube right now.")
        return

    try:
        click.echo(
            "🔌 Starting 'minikube tunnel' to expose LoadBalancer services..."
        )
        subprocess.run(["minikube", "tunnel"], check=True)
        click.echo(
            "✅ Minikube tunnel started successfully. Your ingress should now be exposed."
        )
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to start minikube tunnel.")
        click.echo(f"🔍 Error: {e}")


PROVIDER_COMMANDS: Dict[str, Dict[str, Callable[[], None]]] = {
    "minikube": {
        "create": lambda: (
            subprocess.run(["minikube", "start"], check=True),
            None,
        )[1],
        "start": lambda: (
            subprocess.run(["minikube", "start"], check=True),
            None,
        )[1],
        "stop": lambda: (
            subprocess.run(["minikube", "stop"], check=True),
            None,
        )[1],
        "destroy": lambda: (
            subprocess.run(["minikube", "delete"], check=True),
            None,
        )[1],
        "remove": remove_cluster,
        "status": status_cluster,
        "expose": expose_cluster,
    },
    "kubeconfig": {
        "remove": remove_cluster,
        "status": status_cluster,
    },
}


def get_provider_command(
    provider: str, action: str
) -> Callable[[], None] | None:
    return PROVIDER_COMMANDS.get(provider, {}).get(action)
