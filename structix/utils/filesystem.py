from pathlib import Path
from typing import Any, Dict


def create_nested_folders(base: Path, structure: Dict[str, Any]) -> None:
    for key, value in structure.items():
        subpath = base / key
        if isinstance(value, list):
            for folder in value:
                (subpath / folder).mkdir(parents=True, exist_ok=True)
        elif isinstance(value, dict):
            (subpath).mkdir(parents=True, exist_ok=True)
            create_nested_folders(subpath, value)
        else:
            (subpath / value).mkdir(parents=True, exist_ok=True)
