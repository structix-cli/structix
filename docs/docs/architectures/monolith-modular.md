# Monolith Modular Architecture

The **Monolith Modular Architecture** organizes the backend into independent modules while keeping everything inside a single application.

This approach allows for clear boundaries between different domains of the system without introducing the complexity of distributed systems like microservices.

## Root Structure

At the root level of the project, we have a `shared` directory, which contains components that are reusable across all modules:

```bash
shared/
├── value_objects/
├── types/
├── utils/
├── exceptions/
```

### Shared Components

-   **value_objects/**: Defines immutable and domain-driven value objects.
-   **types/**: Contains global type definitions or type aliases used throughout the application.
-   **utils/**: Helper functions and utility classes shared across modules.
-   **exceptions/**: Custom exception classes for handling application-specific errors.

---

## Module Structure

Each domain feature is grouped into its own **module**.  
Modules help maintain code separation and encapsulate domain logic clearly.

Each module has the following structure:

```bash
module-name/
├── controllers/
├── services/
├── repositories/
├── dto/
├── entities/
```

### Module Components

-   **controllers/**: Handle incoming HTTP requests, call services, and return responses.
-   **services/**: Contain the core business logic of the module.
-   **repositories/**: Abstract data access logic (e.g., database queries).
-   **dto/**: Data Transfer Objects to validate and shape data entering or leaving the system.
-   **entities/**: Domain entities representing the core business models.

---

## CQRS Mode (Optional)

If **CQRS mode** is enabled for a module (Command Query Responsibility Segregation), the module structure is slightly modified:

```bash
module-name/
├── commands/
│   ├── handlers/
│   ├── dto/
├── queries/
│   ├── handlers/
│   ├── dto/
├── repositories/
├── entities/
├── controllers/
```

### CQRS Components

-   **commands/handlers/**: Classes that handle "write" operations (creating, updating, deleting).
-   **commands/dto/**: Data Transfer Objects specifically for commands.
-   **queries/handlers/**: Classes that handle "read" operations (fetching data).
-   **queries/dto/**: DTOs related to query requests.
-   **repositories/**, **entities/**, **controllers/** remain similar.

---

## Summary

The Monolith Modular Architecture balances simplicity with scalability:

-   Modules create clear domain boundaries.
-   Shared utilities promote code reuse.
-   Optional CQRS enhances scalability when needed without overcomplicating the project structure.

This setup is ideal for projects that expect growth but want to maintain the deployment simplicity of a monolith.
