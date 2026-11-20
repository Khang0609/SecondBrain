---
type: concept
tags: [computer-science, data-structures, algorithms, oop, cpp, linked-list]
sources: ["My Note My Life/6 - Full Note/Data Structure & Algorithm.md", "My Note My Life/6 - Full Note/Linked List.md"]
updated: 2026-11-20
---

# Data Structures and Linked Lists

**Data Structures and Algorithms (DSA)** provides the core abstractions for organizing data and designing efficient computations independent of specific frameworks or languages.

## 1. Core Computing Concepts
- **Data vs. Information:** Raw values (e.g., `30`) are *data*; context and units (e.g., `30 m` vs. `30°`) turn data into *information*.
- **Discretization:** Computers store inherently continuous phenomena by sampling/quantizing them into discrete representations.
- **Topological Order (Topological Sorting):** Ordering the vertices of a directed acyclic graph (DAG) into a linear sequence that preserves all dependency/cause-and-effect edges (every prerequisite appears before its dependents).

## 2. OOP & C++ Memory Semantics
- **Abstract Classes:** A class containing at least one pure virtual method cannot be instantiated directly; it defines an interface/contract for derived classes.
- **Early vs. Late Binding:** Static (compile-time) dispatch vs. dynamic (runtime, virtual-table) dispatch in polymorphism.
- **Virtual Inheritance:** Resolves diamond-inheritance ambiguity by sharing a single base-class subobject across derived paths.
- **Unions:** Combine multiple members sharing the same memory location, often paired with structs to save space or reinterpret bit patterns.
- **References vs. `const` Pointers:** In C++, a reference (`T&`) behaves conceptually like an automatically dereferenced `const` pointer (`T* const`) bound at initialization.
- **`const` & Compiler Optimization:** Attempting to mutate a `const` variable (e.g., `const int a = 10`) via pointer casting (`*(&a)`) is undefined behavior in C++; in practice, direct reads of `a` may still evaluate to `10` (constant folding) while indirect reads through `*(&a)` observe `20`.
- **Encapsulation Principle:** *"Design algorithms to be used, not modified"* — avoid overusing `friend` declarations that break encapsulation boundaries.

## 3. Linked Lists
*(Note: `Linked List.md` in the source vault is currently a stub; linked-list node layouts, pointer traversal, and complexity comparisons will be expanded here as lecture notes are added.)*
