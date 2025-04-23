DDD_STRUCTURE = {
    "context_template": {
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
        "infrastructure": [
            "repositories",
            "services",
            "mappers",
            "external_services",
        ],
    },
    "shared": [
        "value_objects",
        "types",
        "utils",
        "exceptions",
    ],
}


HEXAGONAL_STRUCTURE = {
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

DDD_HEXAGONAL_STRUCTURE = {
    "context_template": {
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
    },
    "shared": [
        "value_objects",
        "types",
        "utils",
        "exceptions",
    ],
}


DDD_CQRS_STRUCTURE = {
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

HEXAGONAL_CQRS_STRUCTURE = {
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
