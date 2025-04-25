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
        provider: ClusterProviderType,
        kubeconfig: str,
    ) -> None:
        self.provider = provider
        self.kubeconfig = kubeconfig


class ProjectConfig:
    def __init__(
        self,
        stack: StackType,
        architecture: ArchitectureType,
        ddd: bool,
        hexagonal: bool,
        cqrs: bool,
        source_dir: Path,
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
        self.source_dir = source_dir


class Config:
    def __init__(
        self,
        project_config: Optional[ProjectConfig] = None,
        cluster: Optional[ClusterConfig] = None,
    ) -> None:
        self.project_config = project_config
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


def get_cluster_config_or_fail() -> ClusterConfig:
    config = get_config()
    if not config.cluster:
        click.echo(
            "❌ No cluster configuration found.\n💡 Run `structix ops init cluster` to set up your cluster provider."
        )
        exit(1)
    return config.cluster


def get_project_config_or_fail() -> ProjectConfig:
    config = get_config()
    if not config.project_config:
        click.echo(
            "❌ No project configuration found.\n💡 Run `structix init` to set up your project."
        )
        exit(1)
    return config.project_config


def get_config() -> Config:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config_data = json.load(f)

            project_data = config_data.get("project")
            project = None

            if project_data:
                stack = project_data.get("stack")
                stack_data = get_stack_config(stack)
                project = ProjectConfig(
                    stack=stack,
                    architecture=project_data.get("architecture", "Monolith"),
                    ddd=project_data.get("ddd", False),
                    hexagonal=project_data.get("hexagonal", False),
                    cqrs=config_data.get("cqrs", False),
                    source_dir=Path(stack_data.get("source_dir", "src")),
                )

            cluster_data = config_data.get("cluster")
            cluster = None

            if cluster_data:
                cluster = (
                    ClusterConfig(**cluster_data) if cluster_data else None
                )

            return Config(
                project_config=project,
                cluster=cluster,
            )
    return Config()


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
