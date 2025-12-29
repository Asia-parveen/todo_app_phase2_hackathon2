# Tasks: Phase 2 Full-Stack Todo Web Application

**Input**: Design documents from `/specs/002-fullstack-todo-web/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/openapi.yaml, research.md, quickstart.md
**Branch**: `002-fullstack-todo-web`
**Date**: 2025-12-29

**Tests**: Not explicitly requested in specification - tests are OPTIONAL and not included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/app/` for source, `backend/tests/` for tests
- **Frontend**: `frontend/app/` for pages, `frontend/components/` for components, `frontend/lib/` for utilities

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for both backend and frontend

### Backend Setup

- [x] T001 Create backend project structure with directories: app/, app/core/, app/models/, app/routers/, app/services/, tests/
- [x] T002 Create backend/requirements.txt with dependencies: fastapi, uvicorn, sqlmodel, asyncpg, python-jose, passlib[bcrypt], python-dotenv, alembic
- [x] T003 [P] Create backend/.env.example with DATABASE_URL, JWT_SECRET, JWT_ALGORITHM, CORS_ORIGINS placeholders
- [x] T004 [P] Create backend/.gitignore for Python projects (venv, __pycache__, .env, etc.)

### Frontend Setup

- [x] T005 Initialize Next.js 14+ project in frontend/ with App Router, TypeScript, Tailwind CSS
- [x] T006 [P] Create frontend/.env.example with NEXT_PUBLIC_API_URL, BETTER_AUTH_SECRET placeholders
- [x] T007 [P] Create frontend/.gitignore for Node.js/Next.js projects

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Backend Foundation

- [ ] T008 Create backend/app/core/__init__.py (empty init file)
- [ ] T009 Create backend/app/core/config.py with Settings class loading env vars (DATABASE_URL, JWT_SECRET, JWT_ALGORITHM, CORS_ORIGINS)
- [ ] T010 Create backend/app/core/database.py with async SQLModel engine and session dependency using asyncpg
- [ ] T011 Create backend/app/core/security.py with password hashing (bcrypt via passlib) and JWT token validation (python-jose)
- [ ] T012 Create backend/app/models/__init__.py (empty init file)
- [ ] T013 Create backend/app/models/user.py with User SQLModel (id, email, password_hash, created_at) and UserCreate, UserRead, UserLogin schemas
- [ ] T014 Create backend/app/services/__init__.py (empty init file)
- [ ] T015 Create backend/app/routers/__init__.py (empty init file)
- [ ] T016 Create backend/app/dependencies.py with get_current_user dependency extracting user from JWT
- [ ] T017 Create backend/app/main.py with FastAPI app, CORS middleware, and router includes
- [ ] T018 Create backend/alembic.ini and backend/alembic/ directory structure for migrations
- [ ] T019 Create initial Alembic migration for User table in backend/alembic/versions/

### Frontend Foundation

- [ ] T020 Create frontend/lib/types.ts with TypeScript interfaces for User, Task, AuthResponse, Error matching OpenAPI schemas
- [ ] T021 Create frontend/lib/api.ts with base API client including auth header injection and error handling
- [ ] T022 Create frontend/lib/auth.ts with Better Auth client setup for registration, login, logout, and token management
- [ ] T023 Create frontend/components/ui/Button.tsx - reusable button component with variants (primary, secondary, danger)
- [ ] T024 [P] Create frontend/components/ui/Input.tsx - reusable input component with label and error states
- [ ] T025 [P] Create frontend/components/ui/Card.tsx - reusable card container component
- [ ] T026 [P] Create frontend/components/ui/Loading.tsx - loading spinner component
- [ ] T027 Create frontend/app/globals.css with Tailwind imports and base styles
- [ ] T028 Create frontend/app/layout.tsx with root layout, auth provider wrapper, and metadata

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - User Registration and Login (Priority: P1) 🎯 MVP

**Goal**: Enable users to create accounts and authenticate to access the application

**Independent Test**: Register a new account, logout, login again - user should be authenticated and see their email

**Acceptance Criteria** (from spec.md):
- FR-001: Register with email/password
- FR-002: Authenticate existing users
- FR-003: Issue JWT on auth
- FR-004: Validate JWT on requests
- FR-005: Reject invalid JWT with 401
- FR-006: Logout (client-side)
- FR-007: Hash passwords

### Backend - User Story 1

- [ ] T029 [US1] Create backend/app/services/auth.py with register_user (hash password, check duplicate email, create user) and login_user (verify password, issue JWT) functions
- [ ] T030 [US1] Create backend/app/routers/auth.py with POST /api/auth/register endpoint (201 on success, 400 on duplicate email)
- [ ] T031 [US1] Add POST /api/auth/login endpoint to backend/app/routers/auth.py (200 with JWT, 401 on invalid credentials)
- [ ] T032 [US1] Add POST /api/auth/logout endpoint to backend/app/routers/auth.py (200 success message)
- [ ] T033 [US1] Register auth router in backend/app/main.py with prefix /api/auth

### Frontend - User Story 1

- [ ] T034 [US1] Create frontend/components/auth/RegisterForm.tsx with email, password fields, validation, and API call
- [ ] T035 [US1] Create frontend/components/auth/LoginForm.tsx with email, password fields, validation, and API call
- [ ] T036 [US1] Create frontend/app/(auth)/register/page.tsx with RegisterForm and link to login
- [ ] T037 [US1] Create frontend/app/(auth)/login/page.tsx with LoginForm and link to register
- [ ] T038 [US1] Create frontend/app/(dashboard)/layout.tsx with auth check redirecting unauthenticated users to login
- [ ] T039 [US1] Create frontend/app/page.tsx as landing page redirecting to /login or /tasks based on auth state
- [ ] T040 [US1] Add logout button to dashboard layout with token clearing and redirect to login

**Checkpoint**: User Story 1 complete - users can register, login, logout, and protected routes redirect to login

---

## Phase 4: User Story 2 - View Personal Task List (Priority: P2)

**Goal**: Authenticated users can view all their tasks with completion status

**Independent Test**: Login as user with tasks, verify task list shows with title, description, completion status; verify empty state for new users

**Acceptance Criteria** (from spec.md):
- FR-009: View all own tasks
- FR-014: Tasks associated with user
- FR-015: Cannot view other users' tasks
- FR-016: User ID from JWT

**Dependencies**: Requires User Story 1 (authentication)

### Backend - User Story 2

- [ ] T041 [US2] Create backend/app/models/task.py with Task SQLModel (id, user_id, title, description, completed, created_at, updated_at) and TaskCreate, TaskUpdate, TaskRead schemas
- [ ] T042 [US2] Create Alembic migration for Task table in backend/alembic/versions/
- [ ] T043 [US2] Create backend/app/services/tasks.py with get_user_tasks(user_id) function returning all tasks for user
- [ ] T044 [US2] Create backend/app/routers/tasks.py with GET /api/tasks endpoint (requires auth, filters by user_id)
- [ ] T045 [US2] Add GET /api/tasks/{id} endpoint to backend/app/routers/tasks.py (returns 404 if not owned by user)
- [ ] T046 [US2] Register tasks router in backend/app/main.py with prefix /api/tasks

### Frontend - User Story 2

- [ ] T047 [US2] Create frontend/components/tasks/TaskItem.tsx displaying single task with title, description, completion checkbox
- [ ] T048 [US2] Create frontend/components/tasks/TaskList.tsx rendering list of TaskItem components
- [ ] T049 [US2] Create frontend/app/(dashboard)/tasks/page.tsx fetching and displaying task list with loading and empty states
- [ ] T050 [US2] Add empty state component to tasks page showing friendly message when no tasks exist

**Checkpoint**: User Story 2 complete - authenticated users see their task list (or empty state)

---

## Phase 5: User Story 3 - Add New Task (Priority: P3)

**Goal**: Authenticated users can create new tasks

**Independent Test**: Login, create task with title and optional description, verify task appears in list and persists on refresh

**Acceptance Criteria** (from spec.md):
- FR-008: Create tasks with title (required) and description (optional)
- FR-013: Persist task data
- FR-019: Validate title not empty, max 200 chars
- FR-020: Validate description max 2000 chars

**Dependencies**: Requires User Story 1 (authentication), User Story 2 (task list to view created tasks)

### Backend - User Story 3

- [ ] T051 [US3] Add create_task(user_id, task_data) function to backend/app/services/tasks.py
- [ ] T052 [US3] Add POST /api/tasks endpoint to backend/app/routers/tasks.py (201 on success, 400 on validation error)

### Frontend - User Story 3

- [ ] T053 [US3] Create frontend/components/tasks/TaskForm.tsx with title input, description textarea, validation, and submit
- [ ] T054 [US3] Integrate TaskForm into frontend/app/(dashboard)/tasks/page.tsx with optimistic UI update on success
- [ ] T055 [US3] Add validation error display to TaskForm for title required and max length

**Checkpoint**: User Story 3 complete - users can create tasks that persist

---

## Phase 6: User Story 4 - Mark Task as Complete (Priority: P4)

**Goal**: Authenticated users can toggle task completion status

**Independent Test**: Create task, toggle complete, verify checkbox state changes and persists on refresh

**Acceptance Criteria** (from spec.md):
- FR-012: Toggle task completion status

**Dependencies**: Requires User Story 2 (task list), User Story 3 (task creation)

### Backend - User Story 4

- [ ] T056 [US4] Add toggle_task_completion(user_id, task_id) function to backend/app/services/tasks.py
- [ ] T057 [US4] Add PATCH /api/tasks/{id}/complete endpoint to backend/app/routers/tasks.py (returns updated task, 404 if not owned)

### Frontend - User Story 4

- [ ] T058 [US4] Add toggle completion handler to frontend/components/tasks/TaskItem.tsx calling PATCH endpoint
- [ ] T059 [US4] Update task list state in frontend/app/(dashboard)/tasks/page.tsx when completion toggled

**Checkpoint**: User Story 4 complete - users can toggle task completion

---

## Phase 7: User Story 5 - Update Task (Priority: P5)

**Goal**: Authenticated users can edit task title and description

**Independent Test**: Create task, edit title/description, verify changes persist on refresh

**Acceptance Criteria** (from spec.md):
- FR-010: Update own tasks (title, description)
- FR-019: Validate title not empty, max 200 chars
- FR-020: Validate description max 2000 chars

**Dependencies**: Requires User Story 2 (task list), User Story 3 (task creation)

### Backend - User Story 5

- [ ] T060 [US5] Add update_task(user_id, task_id, task_data) function to backend/app/services/tasks.py
- [ ] T061 [US5] Add PUT /api/tasks/{id} endpoint to backend/app/routers/tasks.py (returns updated task, 400 on validation, 404 if not owned)

### Frontend - User Story 5

- [ ] T062 [US5] Add edit mode to frontend/components/tasks/TaskItem.tsx with inline editing or modal
- [ ] T063 [US5] Create edit form UI in TaskItem with save/cancel buttons and validation
- [ ] T064 [US5] Update task list state in frontend/app/(dashboard)/tasks/page.tsx when task updated

**Checkpoint**: User Story 5 complete - users can edit their tasks

---

## Phase 8: User Story 6 - Delete Task (Priority: P6)

**Goal**: Authenticated users can delete tasks with confirmation

**Independent Test**: Create task, delete it with confirmation, verify task removed from list and stays removed on refresh

**Acceptance Criteria** (from spec.md):
- FR-011: Delete own tasks

**Dependencies**: Requires User Story 2 (task list), User Story 3 (task creation)

### Backend - User Story 6

- [ ] T065 [US6] Add delete_task(user_id, task_id) function to backend/app/services/tasks.py
- [ ] T066 [US6] Add DELETE /api/tasks/{id} endpoint to backend/app/routers/tasks.py (returns success message, 404 if not owned)

### Frontend - User Story 6

- [ ] T067 [US6] Create frontend/components/tasks/TaskDeleteConfirm.tsx confirmation dialog component
- [ ] T068 [US6] Add delete button to frontend/components/tasks/TaskItem.tsx triggering confirmation dialog
- [ ] T069 [US6] Handle delete confirmation in frontend/app/(dashboard)/tasks/page.tsx removing task from list

**Checkpoint**: User Story 6 complete - users can delete tasks with confirmation

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

### Error Handling & UX

- [ ] T070 [P] Add global error boundary to frontend/app/layout.tsx for uncaught errors
- [ ] T071 [P] Add loading states to all API operations in task components (FR-021)
- [ ] T072 [P] Add user-friendly error messages to all forms and API calls (FR-022)
- [ ] T073 [P] Ensure responsive design works on 320px+ screens (FR-024) in all components

### Backend Hardening

- [ ] T074 [P] Add request validation error handling to return consistent JSON errors (FR-026)
- [ ] T075 [P] Ensure error messages don't expose sensitive info (FR-027)
- [ ] T076 [P] Verify CORS configuration allows only trusted origins

### Environment & Deployment Prep

- [ ] T077 [P] Create backend/README.md with setup and deployment instructions
- [ ] T078 [P] Create frontend/README.md with setup and deployment instructions
- [ ] T079 Verify backend runs with uvicorn and all endpoints work
- [ ] T080 Verify frontend builds with next build without errors
- [ ] T081 Run quickstart.md validation - verify both services start and communicate

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
    ↓
Phase 2 (Foundational) ← BLOCKS ALL USER STORIES
    ↓
Phase 3 (US1: Auth) ← MVP - Can deploy here!
    ↓
Phase 4 (US2: View Tasks)
    ↓
Phase 5 (US3: Add Task)
    ↓
Phase 6 (US4: Complete Task)
    ↓
Phase 7 (US5: Update Task)
    ↓
Phase 8 (US6: Delete Task)
    ↓
Phase 9 (Polish)
```

### User Story Dependencies

| Story | Depends On | Can Start After |
|-------|------------|-----------------|
| US1 (Auth) | Foundational | Phase 2 complete |
| US2 (View Tasks) | US1 | Phase 3 complete |
| US3 (Add Task) | US1, US2 | Phase 4 complete |
| US4 (Complete) | US2, US3 | Phase 5 complete |
| US5 (Update) | US2, US3 | Phase 5 complete |
| US6 (Delete) | US2, US3 | Phase 5 complete |

**Note**: US4, US5, US6 can run in parallel after US3 is complete (different endpoints/components)

### Within Each User Story

1. Backend models/migrations first
2. Backend services second
3. Backend routers third
4. Frontend components fourth
5. Frontend page integration last

### Parallel Opportunities

**Phase 1 Setup**:
- T003, T004 can run in parallel (different files)
- T006, T007 can run in parallel (different files)

**Phase 2 Foundational**:
- T024, T025, T026 can run in parallel (different UI components)

**Phase 9 Polish**:
- T070, T071, T072, T073 can run in parallel (different concerns)
- T074, T075, T076 can run in parallel (different backend files)
- T077, T078 can run in parallel (different READMEs)

**After US3 Complete**:
- US4, US5, US6 can all proceed in parallel (different endpoints)

---

## Parallel Example: User Story 4, 5, 6 Together

After User Story 3 (Add Task) is complete, these three stories can be worked on simultaneously:

```bash
# Developer A: User Story 4 (Complete Task)
T056 → T057 → T058 → T059

# Developer B: User Story 5 (Update Task)
T060 → T061 → T062 → T063 → T064

# Developer C: User Story 6 (Delete Task)
T065 → T066 → T067 → T068 → T069
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T007)
2. Complete Phase 2: Foundational (T008-T028)
3. Complete Phase 3: User Story 1 (T029-T040)
4. **STOP and VALIDATE**: Test registration, login, logout
5. Deploy if ready - you have auth working!

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US1 (Auth) → Test → Deploy (MVP!)
3. Add US2 (View) → Test → Deploy
4. Add US3 (Add) → Test → Deploy
5. Add US4 (Complete) → Test → Deploy
6. Add US5 (Update) → Test → Deploy
7. Add US6 (Delete) → Test → Deploy
8. Polish → Final Deploy

### Full Feature Delivery

Complete all phases sequentially for full Phase 2 functionality:
- 81 total tasks
- Approximately 9 phases
- Each phase builds on previous

---

## Task Summary

| Phase | Name | Task Count | Parallelizable |
|-------|------|------------|----------------|
| 1 | Setup | 7 | 4 |
| 2 | Foundational | 21 | 3 |
| 3 | US1: Auth (P1) | 12 | 0 |
| 4 | US2: View Tasks (P2) | 10 | 0 |
| 5 | US3: Add Task (P3) | 5 | 0 |
| 6 | US4: Complete (P4) | 4 | 0 |
| 7 | US5: Update (P5) | 5 | 0 |
| 8 | US6: Delete (P6) | 5 | 0 |
| 9 | Polish | 12 | 10 |
| **Total** | | **81** | **17** |

### Tasks per User Story

| User Story | Backend Tasks | Frontend Tasks | Total |
|------------|---------------|----------------|-------|
| US1 (Auth) | 5 | 7 | 12 |
| US2 (View) | 6 | 4 | 10 |
| US3 (Add) | 2 | 3 | 5 |
| US4 (Complete) | 2 | 2 | 4 |
| US5 (Update) | 2 | 3 | 5 |
| US6 (Delete) | 2 | 3 | 5 |

---

## Notes

- [P] tasks = different files, no dependencies - can run in parallel
- [USn] label maps task to specific user story for traceability
- Each user story should be independently testable after completion
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Constitution compliance: All tasks follow Spec-Driven Development, use mandated tech stack, maintain folder separation
