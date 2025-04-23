DDD_STRUCTURE = {
    "domain": [
        "entities",
        "value_objects",
        "aggregates",
        "repositories",
        "events",
    ],
    "application": ["use_cases", "dto"],
    "infrastructure": ["repositories", "persistence", "services"],
}

HEXAGONAL_STRUCTURE = {
    "interfaces": ["controllers", "routes", "graphql", "listeners"],
    "adapters": ["inbound", "outbound"],
}

CQRS_STRUCTURE = {"application": {"commands", "queries"}}
