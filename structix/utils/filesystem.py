from pathlib import Path
from typing import Any, Dict


def create_nested_folders(
    base: Path, structure: Dict[str, Any], add_gitignore: bool = False
) -> None:
    def ensure_folder(path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)
        if add_gitignore:
            gitignore = path / ".gitignore"
            gitignore.touch(exist_ok=True)

    for key, value in structure.items():
        subpath = base / key
        subpath.mkdir(parents=True, exist_ok=True)
        if isinstance(value, list):
            if len(value) == 0:
                ensure_folder(subpath)
            else:
                for folder in value:
                    folder_path = subpath / folder
                    ensure_folder(folder_path)
        elif isinstance(value, dict):
            create_nested_folders(subpath, value, add_gitignore=add_gitignore)
        else:
            folder_path = subpath / value
            ensure_folder(folder_path)
