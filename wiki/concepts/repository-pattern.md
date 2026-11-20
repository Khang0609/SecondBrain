---
type: concept
tags: [software-architecture, design-patterns, backend, data-access, crud]
sources: ["https://stackoverflow.com/questions/2570556/what-are-some-good-design-patterns-for-crud"]
updated: 2026-11-20
---

# Repository Pattern

The **Repository Pattern** is an architectural pattern that acts as a mediating boundary between the application domain/business logic and the data persistence layer. By abstracting data access behind a collection-like interface, it isolates the core system from database implementation details, query languages, and underlying storage technologies.

```mermaid
flowchart LR
    A["Domain / Application Service"] -->|"Method Call (e.g. getById)"| B["Repository Interface"]
    B -->|"Implements"| C["Repository Implementation"]
    C -->|"Queries / Mutations"| D["Database / ORM"]
```

## Core Mechanics in CRUD Operations

Instead of executing raw SQL queries or ORM commands directly within controllers or services, the application delegates persistence tasks to the repository:

- **Create**: Accepts a new domain entity and persists it to the storage layer.
- **Read**: Retrieves an entity by unique identifier, or queries a filtered collection matching domain criteria.
- **Update**: Receives an altered domain entity, synchronizes state changes, and writes updates to the store.
- **Delete**: Identifies an entity or key and removes the corresponding record from storage.

## Key Architectural Advantages

1. **Persistence Ignorance & Technology Swapping**:
   - The domain model remains completely unaware of whether data resides in PostgreSQL, MongoDB, an external REST API, or an in-memory cache.
   - Switching database engines requires updating only the repository implementation without altering business rules.
2. **Separation of Concerns & Clean Code**:
   - Business services focus exclusively on operational logic and domain invariants, eliminating complex query construction leaks.
3. **Testability & Mocking**:
   - Facilitates unit testing by allowing developers to substitute a fake or mock in-memory repository (e.g., an array or hash map) without requiring a live database connection or teardown scripts.

## References
- Source: [Stack Overflow: What are some good design patterns for CRUD?](https://stackoverflow.com/questions/2570556/what-are-some-good-design-patterns-for-crud)
