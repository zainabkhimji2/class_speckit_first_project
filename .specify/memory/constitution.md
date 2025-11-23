<!--
Sync Impact Report:
Version change: [CONSTITUTION_VERSION_OLD] -> 1.0.0
List of modified principles:
  - Added: I. Write tests first (TDD approach)
  - Added: II. Use Python 3.12+ with type hints everywhere
  - Added: III. Keep code clean and easy to read
  - Added: IV. Document important decisions with ADRs
  - Added: V. Follow essential OOP principles: SOLID, DRY, KISS
Added sections:
  - Technical Stack
  - Quality Requirements
Removed sections:
  - None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/commands/sp.adr.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.analyze.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.checklist.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.clarify.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.constitution.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.git.commit_pr.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.implement.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.phr.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.plan.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.specify.toml: ✅ updated (generic guidance)
  - .specify/commands/sp.tasks.toml: ✅ updated (generic guidance)
Follow-up TODOs:
  - None
-->
# CLI Calculator Project Constitution

## Core Principles

### I. Write tests first (TDD approach)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced.

### II. Use Python 3.12+ with type hints everywhere
All Python code must use version 3.12 or newer. Type hints are mandatory for all function signatures and variable declarations to ensure code clarity and maintainability.

### III. Keep code clean and easy to read
Code must adhere to established style guides (e.g., PEP 8) and prioritize readability, clarity, and simplicity. Avoid unnecessary complexity.

### IV. Document important decisions with ADRs
All significant architectural and design decisions must be documented using Architecture Decision Records (ADRs) to capture context, alternatives, and rationale.

### V. Follow essential OOP principles: SOLID, DRY, KISS
Object-Oriented Programming (OOP) principles such as SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid) must be applied where appropriate.

## Technical Stack
- Python 3.12+ with UV package manager
- pytest for testing
- Keep all project files in git

## Quality Requirements
- All tests must pass
- At least 80% code coverage
- Use dataclasses for data structures

## Governance
This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All Pull Requests (PRs) and code reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-11-23 | **Last Amended**: 2025-11-23