# structix/core/providers.py
import os
import subprocess
from typing import Callable, Dict, List

import click

from structix.utils.config import load_config, save_config

PROVIDER_ACTIONS: Dict[str, List[str]] = {
    "minikube": [
        "init",
        "create",
        "start",
        "stop",
        "destroy",
        "remove",
        "status",
    ],
    "kubeconfig": ["init", "remove", "status"],
}


def is_action_supported(provider: str, action: str) -> bool:
    return action in PROVIDER_ACTIONS.get(provider, [])


# Define the actual command implementations


def remove_cluster() -> None:
    config = load_config()
    if "cluster" not in config:
        click.echo("⚠️ No cluster configuration found.")
        return
    config.pop("cluster")
    save_config(config)
    click.echo("🗑️ Cluster config removed from structix.config.json")


def status_cluster() -> None:
    config = load_config()
    provider = config.get("cluster", {}).get("provider")

    env = os.environ.copy()
    kubeconfig_path = config.get("cluster", {}).get("kubeconfig")
    if kubeconfig_path:
        env["KUBECONFIG"] = kubeconfig_path

    click.echo(f"🔍 Cluster Provider: {provider}")

    try:
        subprocess.run(["kubectl", "get", "nodes"], check=True, env=env)
        subprocess.run(["kubectl", "get", "pods", "-A"], check=True, env=env)
        subprocess.run(
            ["kubectl", "get", "deployments", "-A"], check=True, env=env
        )
        subprocess.run(["helm", "list", "-A"], check=True, env=env)
    except subprocess.CalledProcessError as e:
        click.echo("❌ Could not retrieve full cluster status.")
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
