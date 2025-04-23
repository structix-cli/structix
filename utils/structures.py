DDD_STRUCTURE = {
    "domain": [
        "entities",
        "value_objects",
        "aggregates",
        "repositories",
        "services",
        "events",
    ],
    "application": ["use_cases", "dto", "services"],
    "infrastructure": ["repositories", "persistence", "services"],
}


HEXAGONAL_STRUCTURE = {
    "interfaces": ["controllers", "routes", "graphql", "listeners"],
    "adapters": ["inbound", "outbound"],
}


CQRS_STRUCTURE = {"application": {"commands", "queries"}}
