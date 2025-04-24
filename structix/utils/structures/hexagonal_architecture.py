from typing import Any, Dict

ROOT_STRUCTURE = {
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


def get_root_structure(cqrs: bool) -> Dict[str, Any]:
    """Get the root structure for the project."""
    if cqrs:
        root_structure = ROOT_STRUCTURE.copy()
        root_structure["application"] = CQRS_STRUCTURE["application"]
        return root_structure
    return ROOT_STRUCTURE
