DDD_STRUCTURE = {
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
        "interfaces",
    ],
    "infrastructure": [
        "repositories",
        "persistence",
        "services",
        "mappers",
        "external_services",
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
        "persistence",
        "services",
        "mappers",
        "external_services",
    ],
}


CQRS_STRUCTURE = {"application": {"commands", "queries"}}
