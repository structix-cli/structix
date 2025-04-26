# Microservices Architecture

Structix provides a flexible way to scaffold backend systems based on a **Microservices Architecture**.

In this model, the project is composed of independent services, each responsible for a specific bounded context or functionality.

Each microservice is self-contained, can be developed, deployed, and scaled independently, and communicates with other services typically over APIs or messaging systems.

---

## General Principles

-   Each microservice has its own isolated codebase.
-   Each microservice can evolve independently from others.
-   Structix adapts the internal structure of each microservice depending on the chosen project architecture.

---

## Microservice Structure by Architecture Type

Depending on the selected architecture (Monolith, DDD, Hexagonal, or DDD + Hexagonal), the internal organization of each microservice will vary:

### 1. Monolith Modular (Simple Modules)

If no domain-driven (DDD) or hexagonal architecture is selected, each microservice will follow a **simple modular structure**:

-   A microservice will be equivalent to a single **module**.
-   The structure inside the microservice will include typical layers like `controllers/`, `services/`, `repositories/`, `dto/`, and `entities/`.

```bash
microservice-name/
├── controllers/
├── services/
├── repositories/
├── dto/
├── entities/
```

### 2. Domain-Driven Design (DDD)

If DDD architecture is selected:

-   Each **bounded context** becomes a **separate microservice**.
-   The microservice will follow a DDD-oriented structure, including `domain/`, `application/`, and `infrastructure/` layers.

```bash
microservice-name/
├── domain/
├── application/
├── infrastructure/
```

### 3. Hexagonal Architecture

If Hexagonal Architecture is selected:

-   Each microservice will follow the **full hexagonal prototype**.
-   There are no internal modules; the service directly follows ports and adapters structure.

```bash
microservice-name/
├── domain/
├── application/
├── adapters/
```

### 4. DDD + Hexagonal

If DDD + Hexagonal Architecture is selected:

-   Each bounded context is modeled as a separate microservice.
-   The microservice combines DDD tactical patterns with Hexagonal structural separation.

```bash
microservice-name/
├── domain/
├── application/
├── adapters/
├── infrastructure/
```

---

## Summary

Structix ensures that:

-   Microservices remain consistent with the selected architectural style.
-   Teams can choose the best organization strategy per project.
-   Microservices are fully decoupled, making the system easier to scale, maintain, and evolve over time.

Whether you prefer simple modular structures or fully domain-driven bounded contexts, Structix scaffolds your microservices in a clean, professional way.
