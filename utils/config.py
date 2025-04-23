import json
from pathlib import Path
from typing import Any, Dict

CONFIG_FILE = Path.cwd() / "structix.config.json"


def load_config() -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)  # type: ignore
    return {}


def save_config(config: Dict[str, Any]) -> None:
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
