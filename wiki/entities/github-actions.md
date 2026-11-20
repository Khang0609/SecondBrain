---
type: entity
tags: [ci-cd, github-actions, devops, automation, workflows]
sources: ["GitHub Actions Documentation"]
updated: 2026-11-20
---

# GitHub Actions

**GitHub Actions** is a continuous integration and continuous delivery (CI/CD) platform integrated natively into GitHub repositories. It enables software teams to automate build, lint, type-check, test, and release pipelines directly triggered by repository lifecycle events (such as pull requests and branch pushes).

## Enterprise CI Pipeline Pattern for Node.js / pnpm

A robust, production-grade GitHub Actions CI workflow for TypeScript and JavaScript applications incorporating `pnpm`, caching, and concurrency control:

```yaml
name: CI

on:
  push:
    branches: [main, master, dev, develop]
  pull_request:
    branches: [main, master, dev, develop]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint-and-build:
    name: Lint, Check Types & Build
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install pnpm
        uses: pnpm/action-setup@v4
        with:
          run_install: false

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Format check
        run: pnpm exec prettier --check "**/*.{ts,tsx,md,json}"

      - name: Lint
        run: pnpm run lint

      - name: Type check
        run: pnpm run check-types

      - name: Build
        run: pnpm run build
```

## Key Workflow Optimizations

- **Concurrency Control**: `concurrency` with `cancel-in-progress: true` automatically cancels obsolete pipeline runs on rapid subsequent commits to save execution minutes.
- **Deterministic Installs**: Using `--frozen-lockfile` prevents unexpected dependency version drifts across test runners.
- **Multi-Level Caching**: Leveraging `actions/setup-node` with `cache: 'pnpm'` dramatically cuts installation time by caching pnpm's global virtual store across runner jobs.
- **Quality Gates**: Sequenced execution ensures that formatting and static typing errors halt builds early before costlier compilation steps run.

## Shift-Left Integration
While GitHub Actions acts as the remote gatekeeper, local verification is enforced via Git hooks before code is ever pushed. See [[frontend-dev-tooling]] for local hook setups using Husky and pnpm.

## References
- Related Tooling: [[frontend-dev-tooling]]
