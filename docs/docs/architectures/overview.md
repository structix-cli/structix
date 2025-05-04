# Overview

Modern backend systems benefit greatly from adopting clear architectural patterns that guide the organization of code, separation of concerns, and scalability.

This section introduces several architectural approaches that help structure backend applications around maintainability, modularity, and business logic isolation.

## Why Architecture Matters

-   **Separation of concerns**: Isolating domain logic from infrastructure and interfaces.
-   **Testability**: Easier to write unit and integration tests due to clear boundaries.
-   **Scalability**: Modular design allows individual parts to grow or evolve independently.
-   **Maintainability**: Clear folder structures and responsibilities make onboarding and refactoring easier.

## Common Concepts

Each architecture defines:

-   A **root structure** for shared code (like types and utilities).
-   A **modular structure** where each feature or context is isolated.
-   Optional **patterns** such as CQRS (Command Query Responsibility Segregation) to separate read and write logic.

The following documents describe different architecture styles that can be applied in backend development, from monolithic modular setups to microservices and domain-driven designs.
