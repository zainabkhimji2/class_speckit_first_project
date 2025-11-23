# Tasks: Basic Calculator

**Input**: Design documents from `/specs/001-basic-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The specification explicitly requests "full testing" and "TDD approach".

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create directory `src/calculator`
- [ ] T002 Create directory `tests/unit`
- [ ] T003 Create file `src/calculator/__init__.py`
- [ ] T004 Create file `tests/__init__.py`
- [ ] T005 Create file `tests/unit/__init__.py`
- [ ] T006 Configure `pyproject.toml` with `pytest` and `mypy` dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Verify `pytest` installation by creating and running a dummy test in `tests/unit/test_dummy.py`
- [ ] T008 Configure `mypy` for the project by creating a `mypy.ini` file or updating `pyproject.toml`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Two Numbers (Priority: P1) 🎯 MVP

**Goal**: Implement and test the addition operation.

**Independent Test**: The `add` function should correctly sum various numeric inputs (integers, floats, positive, negative, zero).

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [US1] Write RED tests for `add` function in `tests/unit/test_operations.py`

### Implementation for User Story 1

- [ ] T010 [P] [US1] Implement `add` function in `src/calculator/operations.py`
- [ ] T011 [US1] Refactor `add` function: add type hints, docstrings, and run tests (GREEN) in `src/calculator/operations.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Subtract Two Numbers (Priority: P1)

**Goal**: Implement and test the subtraction operation.

**Independent Test**: The `subtract` function should correctly find the difference between various numeric inputs (integers, floats, positive, negative, zero).

### Tests for User Story 2 ⚠️

- [ ] T012 [US2] Write RED tests for `subtract` function in `tests/unit/test_operations.py`

### Implementation for User Story 2

- [ ] T013 [P] [US2] Implement `subtract` function in `src/calculator/operations.py`
- [ ] T014 [US2] Refactor `subtract` function: add type hints, docstrings, and run tests (GREEN) in `src/calculator/operations.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Multiply Two Numbers (Priority: P1)

**Goal**: Implement and test the multiplication operation.

**Independent Test**: The `multiply` function should correctly find the product of various numeric inputs (integers, floats, positive, negative, zero).

### Tests for User Story 3 ⚠️

- [ ] T015 [US3] Write RED tests for `multiply` function in `tests/unit/test_operations.py`

### Implementation for User Story 3

- [ ] T016 [P] [US3] Implement `multiply` function in `src/calculator/operations.py`
- [ ] T017 [US3] Refactor `multiply` function: add type hints, docstrings, and run tests (GREEN) in `src/calculator/operations.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Divide Two Numbers (Priority: P1)

**Goal**: Implement and test the division operation, including handling division by zero.

**Independent Test**: The `divide` function should correctly find the quotient of various numeric inputs and raise `ZeroDivisionError` when the divisor is zero.

### Tests for User Story 4 ⚠️

- [ ] T018 [US4] Write RED tests for `divide` function (including zero division) in `tests/unit/test_operations.py`

### Implementation for User Story 4

- [ ] T019 [P] [US4] Implement `divide` function in `src/calculator/operations.py`
- [ ] T020 [US4] Refactor `divide` function: add type hints, docstrings, and run tests (GREEN) in `src/calculator/operations.py`

**Checkpoint**: All user stories should now be independently functional

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T021 Run `mypy` to verify type checking across the library
- [ ] T022 Generate code coverage report and ensure 100% test coverage
- [ ] T023 Run linters/formatters (e.g., `black`, `flake8`) on all code
- [ ] T024 Update `quickstart.md` with actual library name and installation instructions
- [ ] T025 Final review of all code against constitution rules

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
-   **User Stories (Phase 3-6)**: All depend on Foundational phase completion
    -   User stories can then proceed in parallel (if staffed)
    -   Or sequentially in priority order (P1 → P2 → P3 → P4)
-   **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

-   **User Story 1 (Add)**: Can start after Foundational (Phase 2) - No dependencies on other stories
-   **User Story 2 (Subtract)**: Can start after Foundational (Phase 2) - No dependencies on other stories
-   **User Story 3 (Multiply)**: Can start after Foundational (Phase 2) - No dependencies on other stories
-   **User Story 4 (Divide)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

-   Tests MUST be written and FAIL before implementation
-   Core implementation before refactoring
-   Story complete before moving to next priority

### Parallel Opportunities

-   All Setup tasks can run in sequence.
-   All Foundational tasks can run in sequence.
-   Once Foundational phase completes, User Stories 1, 2, 3, and 4 can theoretically start in parallel if different team members work on them.
-   Within each User Story, tasks for writing RED tests, implementing, and refactoring should be done sequentially.
-   Refactoring tasks (e.g., adding type hints, docstrings) can be done in parallel for different functions if a clear separation is maintained.

---

## Parallel Example: User Story 1, 2, 3, 4 (After Foundational Phase)

```bash
# Developer A: User Story 1 (Add)
# Developer B: User Story 2 (Subtract)
# Developer C: User Story 3 (Multiply)
# Developer D: User Story 4 (Divide)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1 (Add)
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 (Add) → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 (Subtract) → Test independently → Deploy/Demo
4.  Add User Story 3 (Multiply) → Test independently → Deploy/Demo
5.  Add User Story 4 (Divide) → Test independently → Deploy/Demo
6.  Complete Final Phase: Polish & Cross-Cutting Concerns

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1 (Add)
    -   Developer B: User Story 2 (Subtract)
    -   Developer C: User Story 3 (Multiply)
    -   Developer D: User Story 4 (Divide)
3.  Stories complete and integrate independently

---

## Notes

-   Tasks marked with [P] indicate potential for parallel execution (different files, minimal dependencies).
-   Each user story should be independently completable and testable.
-   Verify tests fail (RED) before implementing code.
-   Commit after each task or logical group of tasks.
-   Stop at any checkpoint to validate story independently.
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence.
