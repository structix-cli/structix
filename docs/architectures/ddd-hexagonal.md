# Domain-Driven Design with Hexagonal Architecture

The **Domain-Driven Design with Hexagonal Architecture** combines the domain-driven modeling of DDD with the structural separation of Hexagonal (Ports and Adapters) architecture.

This hybrid approach maintains a strong, clear domain layer while allowing flexible external communication through ports and adapters.

It is ideal for large systems where domain complexity is high and system boundaries need to remain flexible.

---

## Root Structure

At the root level, a `shared` folder contains common components accessible by all modules:

```bash
shared/
├── value_objects/
├── types/
├── utils/
├── exceptions/
```

### Shared Components

-   **value_objects/**: Reusable immutable types for different domains.
-   **types/**: Global type definitions and type aliases.
-   **utils/**: Helper utilities for the entire application.
-   **exceptions/**: Common exception classes used across modules.

---

## Module Structure

Each module follows a layered structure reflecting DDD principles and Hexagonal separation:

```bash
module-name/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── aggregates/
│   ├── repositories/
│   ├── services/
│   ├── events/
│   ├── exceptions/
├── application/
│   ├── use_cases/
│   ├── dto/
│   ├── services/
│   ├── ports/
├── adapters/
│   ├── inbound/
│   │   ├── rest/
│   │   ├── graphql/
│   │   ├── cli/
│   │   ├── events/
│   ├── outbound/
│       ├── persistence/
│       ├── http_clients/
│       ├── messaging/
│       ├── external_services/
├── infrastructure/
│   ├── repositories/
│   ├── services/
│   ├── mappers/
│   ├── external_services/
```

### Module Components

-   **domain/**:

    -   **entities/**: Core domain entities with business rules.
    -   **value_objects/**: Immutable domain-specific value types.
    -   **aggregates/**: Aggregate roots managing domain consistency boundaries.
    -   **repositories/**: Abstract interfaces for persistence operations.
    -   **services/**: Business services encapsulating complex domain logic.
    -   **events/**: Events triggered by domain changes.
    -   **exceptions/**: Domain-specific exceptions.

-   **application/**:

    -   **use_cases/**: Application-specific tasks that orchestrate domain logic.
    -   **dto/**: Data Transfer Objects to move data across boundaries.
    -   **services/**: Application services implementing orchestration logic.
    -   **ports/**: Input/output ports defining how the application interacts internally and externally.

-   **adapters/**:

    -   **inbound/**: Interfaces allowing external actors (e.g., REST APIs, CLI, events) to call into the system.
    -   **outbound/**: Interfaces through which the system interacts with databases, external APIs, messaging systems, etc.

-   **infrastructure/**:
    -   Provides implementations for the outbound ports such as repositories, services, and mappers.

---

## CQRS Mode (Optional)

When **CQRS (Command Query Responsibility Segregation)** is enabled, the `application/` layer is split into command and query responsibilities:

```bash
module-name/
├── application/
│   ├── commands/
│   │   ├── handlers/
│   │   ├── ports/
│   ├── queries/
│   │   ├── handlers/
│   │   ├── ports/
│   ├── dto/
│   ├── services/
```

### CQRS Components

-   **commands/handlers/**: Classes handling write operations (create, update, delete).
-   **commands/ports/**: Ports (interfaces) for executing commands.
-   **queries/handlers/**: Classes handling read operations (queries).
-   **queries/ports/**: Ports for data retrieval.
-   **dto/**: Data Transfer Objects shared between commands and queries.
-   **services/**: Supporting logic for both command and query flows.

---

## Summary

The DDD + Hexagonal Architecture offers:

-   Rigorous modeling of complex domains via DDD patterns.
-   Clear separation of core logic from infrastructure and external systems through ports and adapters.
-   Adaptability for replacing or modifying external systems without impacting the domain.
-   Built-in support for CQRS patterns for scaling complex read/write operations independently.

This setup is perfect for projects aiming for long-term maintainability, complex business rules management, and technical flexibility.
