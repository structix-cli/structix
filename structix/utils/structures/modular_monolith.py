from typing import Any, Dict

MODULE_STRUCTURE: Dict[str, Any] = {
    "controllers": [],
    "services": [],
    "repositories": [],
    "dto": [],
    "entities": [],
}

ROOT_STRUCTURE = {
    "shared": [
        "value_objects",
        "types",
        "utils",
        "exceptions",
    ],
}


CQRS_STRUCTURE = {
    "commands": [
        "handlers",
        "dto",
    ],
    "queries": [
        "handlers",
        "dto",
    ],
}


def get_root_structure() -> Dict[str, Any]:
    """Get the root structure for the project."""
    return ROOT_STRUCTURE


def get_module_structure(cqrs: bool) -> Dict[str, Any]:
    """Get the context structure for the project."""
    if cqrs:
        module_structure = MODULE_STRUCTURE.copy()
        module_structure.pop("dto", None)
        module_structure.pop("services", None)
        module_structure.update(CQRS_STRUCTURE)
        return module_structure
    return MODULE_STRUCTURE
