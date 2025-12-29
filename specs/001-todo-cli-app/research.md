# Research: Todo In-Memory CLI Application

**Feature**: 001-todo-cli-app
**Date**: 2025-12-28
**Status**: Complete

## Research Summary

This Phase I application has minimal research requirements due to:
- Python standard library only (no framework decisions)
- In-memory storage (no database decisions)
- CLI interface (no UI framework decisions)

All technical decisions are constrained by the constitution.

## Decision Log

### D-001: Python Version

**Decision**: Python 3.x (any version 3.6+)
**Rationale**:
- f-strings for readable output formatting
- dataclasses available (3.7+) but not required
- No version-specific features needed
**Alternatives Considered**:
- Python 2.x: Rejected (end of life)

### D-002: Data Structure for Tasks

**Decision**: Python list of dictionaries
**Rationale**:
- Simple, no external dependencies
- Easy iteration for view/search operations
- Mutable for updates
- Order preserved for consistent display
**Alternatives Considered**:
- Dictionary keyed by ID: Faster lookup but loses insertion order in older Python
- Custom class instances: More overhead for simple use case
- Named tuples: Immutable, harder to update

### D-003: ANSI Color Implementation

**Decision**: Raw ANSI escape codes as string constants
**Rationale**:
- Zero dependencies (colorama not allowed per constitution)
- Works on most modern terminals
- Simple string concatenation
**Alternatives Considered**:
- colorama library: Rejected (external dependency)
- No colors: Rejected (spec requires colors per FR-006)

### D-004: Input Validation Approach

**Decision**: Try/except with specific error messages
**Rationale**:
- Graceful handling per FR-013
- User-friendly messages per constitution IV
- Consistent with edge cases in spec
**Alternatives Considered**:
- Regex validation: Overkill for simple inputs
- Type hints with validation: Requires external libraries

### D-005: ID Generation Strategy

**Decision**: Instance counter in TaskManager class
**Rationale**:
- Centralized per FR-015
- Never reused per FR-003
- Survives task deletions
- Simple increment-only logic
**Alternatives Considered**:
- UUID: Overkill, not user-friendly for CLI
- Timestamp-based: Not sequential as required
- Global module variable: Violates encapsulation

## Technology Constraints (Constitutional)

| Constraint | Source | Impact |
|------------|--------|--------|
| No external packages | Constitution V | Use stdlib only |
| No file I/O | Constitution II | In-memory storage |
| No database | Constitution II | Python data structures |
| No GUI | Constitution III | print()/input() only |
| No networking | Constitution VI (Out of Scope) | Standalone app |

## Clarifications Resolved

| Item | Resolution |
|------|------------|
| Python version | Any 3.x (3.6+ for f-strings) |
| Color library | None - raw ANSI codes |
| Test framework | Manual testing only (no pytest) |
| Data persistence | None - explicitly forbidden |

## Research Complete

All NEEDS CLARIFICATION items have been resolved. Ready for Phase 1 design.
