from typing import Any, Dict

CONTEXT_STRUCTURE = {
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


def get_context_structure(cqrs: bool) -> Dict[str, Any]:
    """Get the context structure for the project."""
    if cqrs:
        context_structure = CONTEXT_STRUCTURE.copy()
        context_structure["application"] = CQRS_STRUCTURE["application"]
        return context_structure
    return CONTEXT_STRUCTURE
