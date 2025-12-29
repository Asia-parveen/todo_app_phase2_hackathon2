<!--
================================================================================
SYNC IMPACT REPORT
================================================================================
Version Change: 0.0.0 → 1.0.0 (MAJOR - initial Phase 2 constitution)

Modified Principles: N/A (first version of Phase 2)

Added Sections:
- Purpose & Phase Context
- Core Principles (3 principles)
- Repository & Folder Governance
- Technology Constraints
- Deployment Intent & Flexibility
- Authentication & Security Rules
- Data & Persistence Rules
- Feature Scope
- API Design Rules
- Quality & UX Standards
- Governance
- Completion Criteria

Removed Sections: N/A (new document)

Templates Requiring Updates:
- .specify/templates/plan-template.md: ⚠ Review for Phase 2 alignment
- .specify/templates/spec-template.md: ⚠ Review for Phase 2 alignment
- .specify/templates/tasks-template.md: ⚠ Review for Phase 2 alignment

Follow-up TODOs:
- Create Phase 2 specs folder structure when first feature is specified
- Verify Better Auth integration pattern during auth spec phase
================================================================================
-->

# Phase 2 Constitution

## Todo Full-Stack Web Application

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29

---

## Purpose

This constitution governs **Phase 2** of the Todo application.

- **Phase 1** (CLI In-Memory Todo App) is **complete, frozen, and MUST remain unchanged**.
- **Phase 2** evolves the project into a secure, multi-user, full-stack web application.

This document defines the non-negotiable rules, constraints, and governance for all Phase 2 development.

---

## Core Principles

### I. Spec-Driven Development is Mandatory (NON-NEGOTIABLE)

- All development MUST follow the Spec-Kit lifecycle:
  **Specify → Plan → Tasks → Implement**
- No code may be written without an approved specification and task.
- Manual coding is strictly prohibited.
- If output is incorrect, specifications MUST be refined — not code edited directly.

**Rationale**: Ensures traceability, architectural integrity, and consistent AI-assisted development.

### II. Phase Isolation (NON-NEGOTIABLE)

- Phase 1 implementation, constitution, and specifications are **frozen**.
- Phase 2 MUST NOT modify or invalidate any Phase 1 artifacts.
- New rules in this constitution apply **only** to Phase 2.
- Phase 1 location: `.specify/memory/constitution.md` (read-only reference)
- Phase 2 location: `.specify/memory/phase-2/constitution.md` (this document)

**Rationale**: Preserves hackathon deliverable integrity; enables independent evolution.

### III. Full-Stack Architecture (NON-NEGOTIABLE)

- The application MUST be split into:
  - **Frontend** (Next.js)
  - **Backend** (FastAPI)
- Frontend and backend MUST communicate **exclusively** via REST APIs.
- No shared code, no direct imports between frontend and backend.

**Rationale**: Clean separation of concerns; independent deployment; clear API contracts.

---

## Repository & Folder Governance (Critical)

### 1. Monorepo Structure

The repository MUST follow a strict folder-based separation:

```
project-root/
├── frontend/   → Next.js application
├── backend/    → FastAPI application
├── specs/      → Phase 2 specifications
└── .specify/   → Constitution and templates
```

### 2. Frontend Folder Rules

- All frontend code MUST reside inside `/frontend`.
- Only Next.js, UI logic, and API consumption are allowed.
- **FORBIDDEN** in frontend:
  - Backend logic
  - Direct database access
  - Authentication enforcement (validation only, not enforcement)
- Frontend MUST be deployable independently to **Vercel** without structural changes.

### 3. Backend Folder Rules

- All backend code MUST reside inside `/backend`.
- Backend MUST contain:
  - FastAPI application
  - Database logic (SQLModel + Neon PostgreSQL)
  - Authentication enforcement
  - Business rules
- Backend MUST NOT depend on frontend runtime or files.

### 4. No Cross-Folder Coupling

- No shared code between frontend and backend.
- No direct imports across folders.
- Communication is allowed **only** via HTTP APIs.
- Shared types/contracts MUST be duplicated or generated, never imported.

---

## Technology Constraints (Non-Negotiable)

| Layer | Technology | Notes |
|-------|------------|-------|
| Frontend | Next.js (App Router) | TypeScript required |
| Frontend Styling | Tailwind CSS | Utility-first CSS |
| Backend | Python FastAPI | Async-first API framework |
| ORM | SQLModel | SQLAlchemy + Pydantic |
| Database | Neon Serverless PostgreSQL | Cloud-hosted PostgreSQL |
| Authentication | Better Auth | JWT-based authentication |
| Development | Claude Code + Spec-Kit Plus | AI-assisted, spec-driven |

**Strict Constraints**:
- Manual coding is **strictly prohibited**.
- All code MUST be generated via Claude Code following specifications.
- No technology substitutions without constitution amendment.

---

## Deployment Intent & Flexibility

### 1. Frontend Deployment

- Frontend is intended for deployment on **Vercel**.
- Code MUST follow Vercel-compatible best practices:
  - App Router patterns
  - Edge-compatible where applicable
  - Environment variables via Vercel dashboard

### 2. Backend Deployment

- Backend deployment platform is intentionally **not fixed** at this stage.
- Backend MUST be:
  - **Stateless** (no in-memory session state)
  - **Environment-variable driven** (all config via env vars)
  - **Compatible** with common FastAPI hosting platforms:
    - Railway
    - Render
    - Hugging Face Spaces
    - Fly.io
    - Any Docker-compatible platform
- **No platform-specific assumptions** are allowed in backend code.

---

## Authentication & Security Rules

### 1. Authentication is Mandatory

- All users MUST sign up and sign in via Better Auth.
- JWT tokens MUST be issued on successful authentication.
- Anonymous access to task operations is **forbidden**.

### 2. JWT Enforcement

- Every backend API request (except auth endpoints) MUST include:
  ```
  Authorization: Bearer <JWT>
  ```
- Requests without valid JWT MUST return `401 Unauthorized`.
- Expired tokens MUST return `401 Unauthorized`.
- Invalid tokens MUST return `401 Unauthorized`.

### 3. User Isolation

- Each task MUST belong to exactly one authenticated user.
- Users may **only** access their own tasks.
- Task ownership MUST be enforced at:
  - **API level**: Filter queries by user ID
  - **Database level**: Foreign key to user table
- Cross-user data access MUST be impossible by design.

### 4. Security Best Practices

- Passwords MUST be hashed (never stored in plaintext).
- JWT secrets MUST be stored in environment variables.
- CORS MUST be configured to allow only trusted origins.
- Unauthorized access MUST NOT leak data or existence information.

---

## Data & Persistence Rules

### 1. Persistent Storage

- In-memory storage is **forbidden** in Phase 2.
- All tasks MUST be stored in Neon PostgreSQL.
- All user data MUST be stored in Neon PostgreSQL.

### 2. Source of Truth

- The database is the **single source of truth**.
- Backend MUST be stateless (no caching of user data in memory).
- Frontend MUST fetch fresh data from API (no permanent local storage).

### 3. Schema Governance

- All database schema changes MUST be defined in specifications before implementation.
- Schema migrations MUST be documented.
- Breaking schema changes require constitution-level review.

### 4. Data Model Requirements

- **User**: id, email, password_hash, created_at
- **Task**: id, user_id (FK), title, description, completed, created_at, updated_at

---

## Feature Scope (Phase 2)

The following features MUST be implemented as a web application:

| Feature | Description |
|---------|-------------|
| **Add Task** | Create new todo item for authenticated user |
| **View Task List** | Display all tasks belonging to authenticated user |
| **Update Task** | Modify task title/description |
| **Delete Task** | Remove task from database |
| **Mark Task as Complete** | Toggle task completion status |
| **User Registration** | Sign up with email/password |
| **User Login** | Sign in and receive JWT |
| **User Logout** | Invalidate session |

**Feature Behavior Consistency**:
- Core task operations (Add, View, Update, Delete, Complete) MUST behave consistently with Phase 1.
- Phase 2 adds: authentication, persistence, and web UI.

**Out of Scope for Phase 2**:
- Task sharing between users
- Task categories or tags
- Due dates or reminders
- File attachments
- Third-party OAuth (Google, GitHub, etc.)

---

## API Design Rules

### 1. RESTful APIs

- All APIs MUST follow REST conventions.
- All endpoints MUST be documented in API specifications.
- Standard HTTP methods:
  - `GET` for retrieval
  - `POST` for creation
  - `PUT/PATCH` for updates
  - `DELETE` for deletion

### 2. API Endpoint Structure

```
POST   /api/auth/register    → User registration
POST   /api/auth/login       → User login
POST   /api/auth/logout      → User logout

GET    /api/tasks            → List user's tasks
POST   /api/tasks            → Create new task
GET    /api/tasks/{id}       → Get single task
PUT    /api/tasks/{id}       → Update task
DELETE /api/tasks/{id}       → Delete task
PATCH  /api/tasks/{id}/complete → Toggle completion
```

### 3. User Context

- All task API operations MUST execute in the context of the authenticated user.
- User ID MUST be extracted from JWT, never from request body.

### 4. Error Handling

- Errors MUST be explicit, consistent, and meaningful.
- Standard error response format:
  ```json
  {
    "error": "error_code",
    "message": "Human-readable message"
  }
  ```
- HTTP status codes:
  - `200` - Success
  - `201` - Created
  - `400` - Bad Request
  - `401` - Unauthorized
  - `403` - Forbidden
  - `404` - Not Found
  - `500` - Internal Server Error

---

## Quality & UX Standards

### Frontend Quality

- **Responsive UI**: MUST work on desktop and mobile viewports.
- **Loading States**: MUST show loading indicators during API calls.
- **Error States**: MUST display user-friendly error messages.
- **Empty States**: MUST handle zero-task state gracefully.

### Code Quality

- Clean separation of concerns.
- Predictable and testable behavior.
- Consistent naming conventions.
- No hardcoded values (use environment variables).

### Testing Requirements

- API endpoints MUST be testable.
- Critical paths MUST have specifications with acceptance criteria.

---

## Governance

### Hierarchy of Authority

```
Constitution → Specifications → Plans → Tasks → Implementation
```

- If a conflict occurs, higher-level documents take precedence.
- No assumptions are allowed; unclear requirements MUST be specified.
- Claude Code MUST follow this constitution without exception.

### Amendment Procedure

1. Propose change with rationale.
2. Document impact on existing specs/implementation.
3. Increment version (MAJOR.MINOR.PATCH).
4. Update dependent artifacts.
5. Record in prompt history.

### Version Policy

- **MAJOR**: Backward incompatible changes (principle removal/redefinition)
- **MINOR**: New principles or sections added
- **PATCH**: Clarifications, typos, non-semantic refinements

### Compliance Review

- All implementation work MUST verify compliance before proceeding.
- Violations MUST be reported and corrected via spec refinement.
- Phase 1 artifacts MUST NOT be modified under any circumstances.

---

## Completion Criteria

Phase 2 is considered complete when **ALL** of the following are true:

- [ ] Frontend deploys successfully to Vercel
- [ ] Backend deploys independently on a suitable FastAPI platform
- [ ] User registration and login work end-to-end
- [ ] Authentication works with JWT tokens
- [ ] All 5 task operations work (Add, View, Update, Delete, Complete)
- [ ] Tasks persist in Neon PostgreSQL
- [ ] All APIs are secured with JWT (401 for unauthorized)
- [ ] Users can only access their own tasks
- [ ] Specs, plans, and tasks are complete and traceable
- [ ] No manual code edits were made
- [ ] Phase 1 artifacts remain unchanged

---

## Quick Reference

| Aspect | Phase 1 (Frozen) | Phase 2 (This Constitution) |
|--------|------------------|----------------------------|
| Interface | CLI | Web (Next.js + FastAPI) |
| Storage | In-memory | Neon PostgreSQL |
| Users | Single, no auth | Multi-user with auth |
| Deployment | Local only | Vercel + Cloud backend |
| API | None | RESTful HTTP |

---

*This constitution is the supreme authority for Phase 2 development.*
