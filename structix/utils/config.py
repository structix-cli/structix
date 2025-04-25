import json
from pathlib import Path
from typing import Any, Dict, Optional

import click

import structix
from structix.utils.types import (
    ArchitectureType,
    ClusterProviderType,
    StackType,
)

CONFIG_FILE = Path.cwd() / ".structix" / "structix.config.json"


class ClusterConfig:
    def __init__(
        self,
        provider: Optional[ClusterProviderType] = None,
        kubeconfig: Optional[str] = None,
    ) -> None:
        self.provider = provider
        self.kubeconfig = kubeconfig


class Config:
    def __init__(
        self,
        stack: Optional[StackType] = None,
        architecture: Optional[ArchitectureType] = None,
        ddd: Optional[bool] = None,
        hexagonal: Optional[bool] = None,
        cqrs: Optional[bool] = None,
        source_dir: Optional[Path] = None,
        cluster: Optional[ClusterConfig] = None,
    ) -> None:
        self.stack = stack
        self.architecture = architecture
        self.microservice = (
            architecture == "Microservices" if architecture else False
        )
        self.monolith = architecture == "Monolith" if architecture else False
        self.ddd = ddd
        self.hexagonal = hexagonal
        self.cqrs = cqrs
        self.source_dir = source_dir or Path.cwd() / "src"
        self.cluster = cluster


def get_stack_config(stack: str) -> Dict[str, Any]:
    stack_config_path = (
        Path(structix.__file__).parent / f"stacks/{stack}/config.json"
    )
    if stack_config_path.exists():
        with open(stack_config_path) as f:
            return json.load(f)  # type: ignore
    else:
        click.echo(f"⚠️ Error: No configuration found for stack '{stack}'.")
        exit(1)


def get_config() -> Config:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config_data = json.load(f)

            stack = config_data.get("stack")
            stack_config = get_stack_config(stack) if stack else {}

            cluster_data = config_data.get("cluster")
            cluster = ClusterConfig(**cluster_data) if cluster_data else None

            return Config(
                stack=stack,
                architecture=config_data.get("architecture"),
                ddd=config_data.get("ddd"),
                hexagonal=config_data.get("hexagonal"),
                cqrs=config_data.get("cqrs"),
                source_dir=Path(stack_config.get("source_dir", "src")),
                cluster=cluster,
            )
    return Config()


def no_cluster_config() -> None:

    click.echo(
        "❌ No cluster configuration found.\n💡 Run `structix ops init cluster` to set up your cluster provider."
    )


def load_config() -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)  # type: ignore
    return {}


def save_config(new_data: Dict[str, Any]) -> None:
    config = load_config()
    merged = deep_merge(config, new_data)

    if not CONFIG_FILE.exists():
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_FILE, "w") as f:
        json.dump(merged, f, indent=2)


def force_save_config(new_data: Dict[str, Any]) -> None:

    if not CONFIG_FILE.exists():
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_FILE, "w") as f:
        json.dump(new_data, f, indent=2)


def deep_merge(
    original: Dict[str, Any], updates: Dict[str, Any]
) -> Dict[str, Any]:
    for key, value in updates.items():
        if (
            key in original
            and isinstance(original[key], dict)
            and isinstance(value, dict)
        ):
            original[key] = deep_merge(original[key], value)
        else:
            original[key] = value
    return original
