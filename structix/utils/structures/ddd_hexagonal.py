from typing import Any, Dict

MODULE_STRUCTURE = {
    "domain": [
        "entities",
        "value_objects",
        "aggregates",
        "repositories",
        "services",
        "events",
        "exceptions",
    ],
    "application": [
        "use_cases",
        "dto",
        "services",
        "ports",
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
    "infrastructure": [
        "repositories",
        "services",
        "mappers",
        "external_services",
    ],
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
        ],
        "queries": [
            "handlers",
            "ports",
        ],
        "dto": [],
        "services": [],
    }
}


def get_root_structure() -> Dict[str, Any]:
    """Get the root structure for the project."""
    return ROOT_STRUCTURE


def get_module_structure(cqrs: bool) -> Dict[str, Any]:
    """Get the context structure for the project."""
    if cqrs:
        module_structure = MODULE_STRUCTURE.copy()
        module_structure["application"] = CQRS_STRUCTURE["application"]
        return module_structure
    return MODULE_STRUCTURE
