from typing import Any, Dict

MODULE_STRUCTURE = {
    "domain": [
        "models",
        "services",
        "events",
        "exceptions",
    ],
    "application": [
        "ports",
        "services",
    ],
    "adapters": {
        "inbound": [
            "rest",
            "graphql",
            "cli",
            "events",
        ],
        "outbound": [
            "persistence",
            "http_clients",
            "messaging",
            "external_services",
        ],
    },
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
    "application": {
        "commands": [
            "handlers",
            "ports",
            "services",
        ],
        "queries": [
            "handlers",
            "ports",
            "services",
        ],
    }
}


def get_root_structure(cqrs: bool, microservice: bool) -> Dict[str, Any]:
    """Get the root structure for the project."""
    if cqrs:
        root_structure = ROOT_STRUCTURE.copy()
        if not microservice:
            module_structure = MODULE_STRUCTURE.copy()
            module_structure["application"] = CQRS_STRUCTURE["application"]
            root_structure.update(
                {k: list(v) for k, v in module_structure.items()}
            )
        return root_structure
    return ROOT_STRUCTURE


def get_module_structure(cqrs: bool) -> Dict[str, Any]:
    """Get the module structure for the project."""
    if cqrs:
        module_structure = MODULE_STRUCTURE.copy()
        module_structure["application"] = CQRS_STRUCTURE["application"]
        return module_structure
    return MODULE_STRUCTURE
