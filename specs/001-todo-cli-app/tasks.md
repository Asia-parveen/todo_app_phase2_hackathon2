# Tasks: Todo In-Memory CLI Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, quickstart.md

**Tests**: Manual CLI testing only (no pytest per constitution - Python stdlib only)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, at repository root
- Paths follow plan.md structure: `src/models/`, `src/services/`, `src/cli/`

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project structure and foundational files

- [ ] T001 Create project directory structure: `src/`, `src/models/`, `src/services/`, `src/cli/`
- [ ] T002 [P] Create package marker `src/__init__.py`
- [ ] T003 [P] Create package marker `src/models/__init__.py`
- [ ] T004 [P] Create package marker `src/services/__init__.py`
- [ ] T005 [P] Create package marker `src/cli/__init__.py`
- [ ] T006 Create ANSI color constants in `src/cli/colors.py` per FR-006

**Checkpoint**: Project structure ready, colors module available

---

## Phase 2: Foundational (Core Data Model)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Create Task entity class in `src/models/task.py` with fields: id, title, description, completed
- [ ] T008 Create TaskManager class in `src/models/task.py` with in-memory storage and ID generation
- [ ] T009 Implement centralized ID counter in TaskManager (starts at 1, never reused per FR-003, FR-015)
- [ ] T010 Create TaskService class in `src/services/task_service.py` with CRUD method stubs
- [ ] T011 Create main menu display function in `src/cli/menu.py` per FR-005
- [ ] T012 Create main application loop in `src/main.py` with menu integration

**Checkpoint**: Foundation ready - core model exists, menu displays, app runs (no features yet)

---

## Phase 3: User Story 1 - Add Task (Priority: P1)

**Goal**: Users can add new tasks with title and optional description

**Independent Test**: Run app → Select option 1 → Enter title → See green success message with ID

### Implementation for User Story 1

- [ ] T013 [US1] Implement `add_task(title, description)` method in `src/services/task_service.py`
- [ ] T014 [US1] Create add task handler in `src/cli/handlers.py` with title prompt and validation
- [ ] T015 [US1] Add description prompt (optional, can be empty) in add task handler
- [ ] T016 [US1] Implement empty title validation with red error message per FR-007
- [ ] T017 [US1] Display green success message with task ID on successful add
- [ ] T018 [US1] Integrate add task handler with main menu (option 1) in `src/main.py`

**Checkpoint**: User Story 1 complete - can add tasks with proper validation and feedback

---

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: Users can see all tasks with status indicators

**Independent Test**: Add tasks → Select option 2 → See list with IDs, titles, status markers

### Implementation for User Story 2

- [ ] T019 [US2] Implement `get_all_tasks()` method in `src/services/task_service.py`
- [ ] T020 [US2] Create view tasks handler in `src/cli/handlers.py`
- [ ] T021 [US2] Format task display with ID, status marker, title, description per FR-009
- [ ] T022 [US2] Implement green checkmark for completed tasks
- [ ] T023 [US2] Implement yellow X marker for incomplete tasks
- [ ] T024 [US2] Handle empty list with yellow warning message
- [ ] T025 [US2] Add task count summary (Total: X | Completed: Y)
- [ ] T026 [US2] Integrate view tasks handler with main menu (option 2) in `src/main.py`

**Checkpoint**: User Stories 1 AND 2 complete - can add and view tasks

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status

**Independent Test**: Add task → Mark complete → View (should show checkmark) → Toggle again → View (should show X)

### Implementation for User Story 3

- [ ] T027 [US3] Implement `toggle_complete(task_id)` method in `src/services/task_service.py`
- [ ] T028 [US3] Create toggle handler in `src/cli/handlers.py` with ID prompt
- [ ] T029 [US3] Implement ID validation (must be positive integer)
- [ ] T030 [US3] Handle task not found with red error message
- [ ] T031 [US3] Display confirmation message with new status (complete/incomplete)
- [ ] T032 [US3] Integrate toggle handler with main menu (option 5) in `src/main.py`

**Checkpoint**: User Stories 1, 2, 3 complete - can add, view, and toggle tasks

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Users can modify task title and/or description

**Independent Test**: Add task → Update title → View (should show new title, same ID)

### Implementation for User Story 4

- [ ] T033 [US4] Implement `update_task(task_id, title, description)` method in `src/services/task_service.py`
- [ ] T034 [US4] Create update handler in `src/cli/handlers.py` with ID prompt
- [ ] T035 [US4] Add prompts for new title (optional - keep old if empty)
- [ ] T036 [US4] Add prompts for new description (optional - keep old if empty)
- [ ] T037 [US4] Handle task not found with red error message
- [ ] T038 [US4] Display green success message on update
- [ ] T039 [US4] Ensure task ID never changes on update per FR-011
- [ ] T040 [US4] Integrate update handler with main menu (option 3) in `src/main.py`

**Checkpoint**: User Stories 1-4 complete - full CRUD except delete

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Users can permanently remove tasks with confirmation

**Independent Test**: Add tasks 1,2,3 → Delete task 2 → Add new task → New task gets ID 4 (not 2)

### Implementation for User Story 5

- [ ] T041 [US5] Implement `delete_task(task_id)` method in `src/services/task_service.py`
- [ ] T042 [US5] Create delete handler in `src/cli/handlers.py` with ID prompt
- [ ] T043 [US5] Implement Y/N confirmation prompt in yellow per FR-010
- [ ] T044 [US5] Handle "N" response - do not delete, return to menu
- [ ] T045 [US5] Handle task not found with red error message
- [ ] T046 [US5] Display green success message on deletion
- [ ] T047 [US5] Verify deleted ID is never reused (ID counter not decremented)
- [ ] T048 [US5] Integrate delete handler with main menu (option 4) in `src/main.py`

**Checkpoint**: User Stories 1-5 complete - full CRUD functionality

---

## Phase 8: User Story 6 - Exit Application (Priority: P3)

**Goal**: Clean application exit with farewell message

**Independent Test**: Select option 6 → See blue farewell message → Program terminates

### Implementation for User Story 6

- [ ] T049 [US6] Create exit handler in `src/cli/handlers.py`
- [ ] T050 [US6] Display blue farewell message per spec
- [ ] T051 [US6] Implement clean program termination
- [ ] T052 [US6] Integrate exit handler with main menu (option 6) in `src/main.py`

**Checkpoint**: All 6 user stories complete - full application functionality

---

## Phase 9: Polish & Error Handling

**Purpose**: Cross-cutting improvements and edge case handling

- [ ] T053 Implement global try/except in main loop for graceful error recovery per FR-013
- [ ] T054 Handle non-numeric menu input with red error message
- [ ] T055 Handle negative task IDs with red error message
- [ ] T056 Ensure all operations return to main menu after completion per FR-012
- [ ] T057 Add welcome banner with blue color on startup per FR-004
- [ ] T058 Verify color consistency across all messages per FR-006
- [ ] T059 Run quickstart.md verification checklist manually

**Checkpoint**: Application is demo-ready and judge-friendly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies - can start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Phase 2 completion
  - US1 (Add) → Can start after Phase 2
  - US2 (View) → Depends on US1 (needs tasks to view)
  - US3 (Toggle) → Depends on US1 (needs tasks to toggle)
  - US4 (Update) → Depends on US1 (needs tasks to update)
  - US5 (Delete) → Depends on US1 (needs tasks to delete)
  - US6 (Exit) → Can start after Phase 2 (independent)
- **Phase 9 (Polish)**: Depends on all user stories being complete

### Within Each User Story

- Service method before handler
- Handler before menu integration
- Validation before success path
- Error handling alongside main flow

### Parallel Opportunities

Phase 1 parallel tasks:
```
T002, T003, T004, T005 - All __init__.py files
```

After Phase 2, these user stories can proceed in parallel:
```
US1 (Add) - required first for data
US6 (Exit) - fully independent
```

After US1 is complete:
```
US2, US3, US4, US5 - can proceed in parallel (different handlers)
```

---

## Implementation Strategy

### MVP First (User Story 1 + 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: Add Task (US1)
4. Complete Phase 4: View Tasks (US2)
5. **STOP and VALIDATE**: Can add and view tasks
6. Demo if ready - this is a working MVP!

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US1 (Add Task) → Test independently
3. Add US2 (View Tasks) → Test independently → MVP Complete!
4. Add US3 (Toggle) → Test independently
5. Add US4 (Update) → Test independently
6. Add US5 (Delete) → Test independently
7. Add US6 (Exit) → Test independently
8. Polish phase → Demo ready

---

## Task Summary

| Phase | User Story | Task Count | Priority |
|-------|------------|------------|----------|
| 1 | Setup | 6 | - |
| 2 | Foundational | 6 | - |
| 3 | US1 - Add Task | 6 | P1 |
| 4 | US2 - View Tasks | 8 | P1 |
| 5 | US3 - Toggle Complete | 6 | P2 |
| 6 | US4 - Update Task | 8 | P2 |
| 7 | US5 - Delete Task | 8 | P2 |
| 8 | US6 - Exit | 4 | P3 |
| 9 | Polish | 7 | - |
| **Total** | | **59** | |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Manual CLI testing only (no pytest per constitution)
- Commit after each phase or logical group
- Stop at any checkpoint to validate story independently
