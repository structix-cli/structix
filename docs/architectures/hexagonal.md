# Hexagonal Architecture (Ports and Adapters)

The **Hexagonal Architecture**, also known as **Ports and Adapters**, organizes the backend around the idea of isolating the business logic from external concerns like databases, APIs, or user interfaces.

It creates a strong boundary between the core application and the outside world, making the system more maintainable, testable, and adaptable.

---

## Root Structure

At the root level, we maintain a `shared` directory containing common utilities and types:

```bash
shared/
├── value_objects/
├── types/
├── utils/
├── exceptions/
```

### Shared Components

-   **value_objects/**: Immutable shared types.
-   **types/**: Global type aliases and common data types.
-   **utils/**: Utility classes and helper functions.
-   **exceptions/**: Custom global exceptions.

---

## Module Structure

Each module isolates its internal logic and exposes its capabilities through defined ports.

The standard structure for a module is:

```bash
module-name/
├── domain/
│   ├── models/
│   ├── services/
│   ├── events/
│   ├── exceptions/
├── application/
│   ├── ports/
│   ├── services/
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
```

### Module Components

-   **domain/**:

    -   **models/**: Core business models.
    -   **services/**: Domain services encapsulating key business logic.
    -   **events/**: Domain events that the system emits when business actions occur.
    -   **exceptions/**: Business-specific exceptions.

-   **application/**:

    -   **ports/**: Interfaces (input and output ports) that define how the application interacts internally and externally.
    -   **services/**: Application services implementing use cases by connecting domain logic to ports.

-   **adapters/**:
    -   **inbound/**: Mechanisms that allow external systems (e.g., REST APIs, CLI, events) to call into the application.
    -   **outbound/**: Mechanisms for the application to interact with the outside world (databases, APIs, messaging systems).

---

## CQRS Mode (Optional)

When **CQRS (Command Query Responsibility Segregation)** is enabled, the `application/` layer is organized into explicit command and query responsibilities:

```bash
module-name/
├── application/
│   ├── commands/
│   │   ├── handlers/
│   │   ├── ports/
│   │   ├── services/
│   ├── queries/
│   │   ├── handlers/
│   │   ├── ports/
│   │   ├── services/
```

### CQRS Components

-   **commands/handlers/**: Handle all write operations like create, update, or delete actions.
-   **commands/ports/**: Define ports specifically for command operations.
-   **commands/services/**: Services related to executing commands.

-   **queries/handlers/**: Handle all read operations for data retrieval.
-   **queries/ports/**: Define ports for query operations.
-   **queries/services/**: Services related to executing queries.

---

## Summary

The Hexagonal Architecture offers:

-   Clear separation between the core business logic and external dependencies.
-   High flexibility to replace external systems without impacting the domain logic.
-   Simplified testing by mocking ports and adapters.
-   Support for scaling with CQRS when needed.
-   A clean structure for growing applications without coupling internal code to external technologies.

This architecture is ideal for systems that require long-term maintainability and adaptability to changes.
