# Implementation Plan: Todo In-Memory CLI Application

**Branch**: `001-todo-cli-app` | **Date**: 2025-12-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-cli-app/spec.md`

## Summary

Build a Python console application for in-memory task management with 6 core features (Add, View, Update, Delete, Mark Complete, Exit). The application uses ANSI colors for CLI output, maintains strict ID immutability rules, and separates business logic from presentation. No external dependencies - Python standard library only.

## Technical Context

**Language/Version**: Python 3.x (standard library only)
**Primary Dependencies**: None (Python standard library only per constitution)
**Storage**: In-memory only (Python list/dict) - NO persistence
**Testing**: Manual CLI testing (no pytest framework per stdlib-only constraint)
**Target Platform**: Any terminal supporting ANSI escape codes
**Project Type**: Single project (CLI application)
**Performance Goals**: Handle 100+ tasks without degradation (per SC-006)
**Constraints**: No databases, no file I/O, no external packages, no GUI
**Scale/Scope**: Single user, in-memory, session-based

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status |
|-----------|-------------|--------|
| I. Spec-Driven Development | All code generated from specs | PASS |
| II. In-Memory Storage Only | No databases, no file persistence | PASS |
| III. CLI-Only Interface | print()/input() only, no GUI | PASS |
| IV. Error Handling | Graceful handling, friendly messages | PASS |
| V. Python Standard Library Only | No pip dependencies | PASS |
| VI. Feature Scope | 6 features (Add, View, Update, Delete, Complete, Exit) | PASS* |

*Note: Constitution specifies 5 features, but user-provided spec includes Update. Proceeding with 6 features as explicitly requested.

**Gate Status: PASS** - All constitutional principles satisfied.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli-app/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py          # Package marker
├── main.py              # Application entry point
├── models/
│   ├── __init__.py
│   └── task.py          # Task entity and TaskManager
├── services/
│   ├── __init__.py
│   └── task_service.py  # Business logic layer
└── cli/
    ├── __init__.py
    ├── colors.py        # ANSI color constants
    ├── menu.py          # Menu display and navigation
    └── handlers.py      # Feature handlers (add, view, update, delete, toggle)
```

**Structure Decision**: Single project with clear separation of concerns:
- `models/` - Data structures and in-memory storage
- `services/` - Business logic (ID generation, CRUD operations)
- `cli/` - Presentation layer (colors, menus, user interaction)

## Architectural Decisions

### ADR-001: Separation of Concerns

**Decision**: Separate business logic from CLI handling (per FR-014)

**Structure**:
- `models/task.py` - Task dataclass and TaskManager (in-memory storage + ID generation)
- `services/task_service.py` - Business operations (add, update, delete, toggle)
- `cli/handlers.py` - User interaction and output formatting

**Rationale**: Constitution requires code that "maps clearly to specification" and separates concerns.

### ADR-002: Centralized ID Generation

**Decision**: ID counter lives in TaskManager class (per FR-015)

**Implementation**:
- Global counter starts at 1
- Increments on each task creation
- Never decremented or reused on deletion
- Counter state is instance variable, not module global

**Rationale**: FR-003 mandates "never reuse deleted task IDs" and FR-015 requires "centralized ID generation logic."

### ADR-003: ANSI Color System

**Decision**: Define color constants in dedicated module

**Colors** (per FR-006):
- GREEN: Success messages
- RED: Errors and invalid input
- YELLOW: Warnings and confirmations
- BLUE: Section headers and menus
- CYAN: User input prompts
- RESET: Return to default

**Rationale**: Consistent color usage per specification, easy to modify if needed.

## Complexity Tracking

> No constitution violations requiring justification.

| Aspect | Complexity Level | Justification |
|--------|-----------------|---------------|
| Data Model | Low | Single entity (Task) with 4 fields |
| Storage | Low | In-memory list only |
| UI | Low | Text menu with 6 options |
| Error Handling | Medium | Must handle all edge cases gracefully |

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| ANSI colors not supported | Colors enhance but don't break functionality |
| Large task lists | Python lists handle 100+ items easily |
| Invalid input crashes | Comprehensive try/except in all handlers |
