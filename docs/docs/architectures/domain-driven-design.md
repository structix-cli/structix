# Domain-Driven Design (DDD) Architecture

The **Domain-Driven Design (DDD) Architecture** organizes the backend following DDD tactical patterns, ensuring clear separation of concerns between domain logic, application services, and infrastructure.

This architecture is ideal for medium-to-large systems where domain complexity needs to be modeled cleanly.

---

## Root Structure

At the root level of the project, we maintain a `shared` folder that holds elements common across all modules:

```bash
shared/
├── value_objects/
├── types/
├── utils/
├── exceptions/
```

### Shared Components

-   **value_objects/**: Defines shared, immutable domain value objects.
-   **types/**: Global type aliases and data definitions.
-   **utils/**: Helper functions and reusable logic.
-   **exceptions/**: Application-wide custom exception classes.

---

## Module Structure

Each domain concept is organized as a module with a strict separation of layers:

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
├── infrastructure/
│   ├── repositories/
│   ├── services/
│   ├── mappers/
│   ├── external_services/
```

### Module Components

-   **domain/**:  
    Contains the heart of the business logic.

    -   **entities/**: Core domain entities with identity and lifecycle.
    -   **value_objects/**: Immutable domain-specific value types.
    -   **aggregates/**: Aggregate roots managing consistency boundaries.
    -   **repositories/**: Abstract interfaces for persistence operations.
    -   **services/**: Domain services encapsulating business logic that doesn't naturally fit inside an entity.
    -   **events/**: Domain events triggered by changes in the model.
    -   **exceptions/**: Domain-specific exception classes.

-   **application/**:  
    Coordinates interaction between the outside world and the domain.

    -   **use_cases/**: Application-specific tasks orchestrating domain operations.
    -   **dto/**: Data Transfer Objects for inbound and outbound communications.
    -   **services/**: Application services implementing use cases.
    -   **ports/**: Abstractions for communication with infrastructure or other systems.

-   **infrastructure/**:  
    Implements technical concerns and integrations.
    -   **repositories/**: Concrete implementations of domain repository interfaces.
    -   **services/**: Infrastructure-level services.
    -   **mappers/**: Utilities to map between domain models and database or external representations.
    -   **external_services/**: Integrations with external APIs, third-party services, etc.

---

## CQRS Mode (Optional)

When **CQRS (Command Query Responsibility Segregation)** is enabled, the `application/` layer is further divided:

```bash
moule-name/
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

-   **commands/handlers/**: Handle write operations (create, update, delete).
-   **commands/ports/**: Define command execution interfaces.
-   **queries/handlers/**: Handle read operations (data fetching).
-   **queries/ports/**: Define query interfaces for retrieval operations.

---

## Summary

The pure DDD architecture ensures:

-   Clear distinction between domain logic, application orchestration, and infrastructure concerns.
-   Strong domain modeling aligned with real-world business rules.
-   Optional CQRS support for scaling complex operations.
-   A flexible foundation for evolving business needs without tightly coupling technical concerns to the domain.

This structure is ideal for systems where maintaining domain integrity and complexity management is critical.
