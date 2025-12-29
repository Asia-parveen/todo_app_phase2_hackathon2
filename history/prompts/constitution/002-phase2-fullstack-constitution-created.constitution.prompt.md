---
id: 002
title: Phase 2 Full-Stack Constitution Created
stage: constitution
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-todo-cli-app
user: developer
command: /sp.constitution
labels: [phase-2, constitution, full-stack, web-application]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/phase-2/constitution.md (created)
tests:
  - N/A (governance document)
---

## Prompt

```text
# Phase 2 Constitution
## Todo Full-Stack Web Application

### Purpose
This constitution governs Phase 2 of the Todo application.
Phase 1 (CLI In-Memory Todo App) is complete, frozen, and must remain unchanged.
Phase 2 evolves the project into a secure, multi-user, full-stack web application.

---

## Core Principles

1. **Spec-Driven Development is mandatory**
   - All development must follow the Spec-Kit lifecycle:
     Specify → Plan → Tasks → Implement
   - No code may be written without an approved specification and task.

2. **Phase Isolation**
   - Phase 1 implementation, constitution, and specifications are frozen.
   - Phase 2 must not modify or invalidate Phase 1 artifacts.
   - New rules apply only to Phase 2.

3. **Full-Stack Architecture**
   - The application must be split into:
     - Frontend (Next.js)
     - Backend (FastAPI)
   - Frontend and backend must communicate exclusively via REST APIs.

---

## Repository & Folder Governance (Critical)

1. **Monorepo Structure**
   - The repository must follow a strict folder-based separation:

     project-root/
     ├── frontend/   → Next.js application
     └── backend/    → FastAPI application

2. **Frontend Folder Rules**
   - All frontend code must reside inside `/frontend`.
   - Only Next.js, UI logic, and API consumption are allowed.
   - No backend logic, database access, or authentication enforcement
     may exist in the frontend.
   - Frontend must be deployable independently to **Vercel**
     without requiring structural changes.

3. **Backend Folder Rules**
   - All backend code must reside inside `/backend`.
   - Backend must contain:
     - FastAPI application
     - Database logic
     - Authentication enforcement
     - Business rules
   - Backend must not depend on frontend runtime or files.

4. **No Cross-Folder Coupling**
   - No shared code between frontend and backend.
   - No direct imports across folders.
   - Communication is allowed only via HTTP APIs.

---

## Technology Constraints (Non-Negotiable)

- Frontend: Next.js (App Router) + TypeScript + Tailwind CSS
- Backend: Python FastAPI
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth (JWT-based)
- Development Method: Claude Code + Spec-Kit Plus
- Manual coding is strictly prohibited.

---

## Deployment Intent & Flexibility

1. **Frontend Deployment**
   - Frontend is intended for deployment on **Vercel**.
   - Code must follow Vercel-compatible best practices.

2. **Backend Deployment**
   - Backend deployment platform is intentionally **not fixed** at this stage.
   - Backend must be:
     - Stateless
     - Environment-variable driven
     - Compatible with common FastAPI hosting platforms
       (e.g., Railway, Render, Hugging Face, etc.)
   - No platform-specific assumptions are allowed in backend code.

---

## Authentication & Security Rules

1. **Authentication is mandatory**
   - All users must sign up and sign in via Better Auth.
   - JWT tokens must be issued on authentication.

2. **JWT Enforcement**
   - Every backend API request must include:
     `Authorization: Bearer <JWT>`
   - Requests without valid JWT must return `401 Unauthorized`.

3. **User Isolation**
   - Each task must belong to exactly one authenticated user.
   - Users may only access their own tasks.
   - Task ownership must be enforced at both API and database levels.

---

## Data & Persistence Rules

1. **Persistent Storage**
   - In-memory storage is forbidden.
   - All tasks must be stored in Neon PostgreSQL.

2. **Source of Truth**
   - The database is the single source of truth.
   - Backend must be stateless.

3. **Schema Governance**
   - All database schema changes must be defined in specifications
     before implementation.

---

## Feature Scope (Phase 2)

The following features must be implemented as a web application:

- Add Task
- View Task List
- Update Task
- Delete Task
- Mark Task as Complete

Feature behavior must remain consistent with Phase 1,
with the addition of authentication and persistence.

---

## API Design Rules

1. **RESTful APIs**
   - All APIs must follow REST conventions.
   - All endpoints must be documented in API specifications.

2. **User Context**
   - All API operations must execute in the context of the authenticated user.

3. **Error Handling**
   - Errors must be explicit, consistent, and meaningful.
   - Unauthorized access must never leak data.

---

## Quality & UX Standards

- Responsive UI
- Clear loading and error states
- Clean separation of concerns
- Predictable and testable behavior

---

## Governance

Constitution → Specifications → Plans → Tasks → Implementation

If a conflict occurs, higher-level documents take precedence.
No assumptions are allowed; unclear requirements must be specified.

---

## Completion Criteria

Phase 2 is considered complete when:

- Frontend deploys successfully to Vercel
- Backend deploys independently on a suitable FastAPI platform
- Authentication works end-to-end
- Tasks persist in Neon PostgreSQL
- All APIs are secured with JWT
- Specs, plans, and tasks are complete and traceable
```

## Response snapshot

Created Phase 2 Constitution at `.specify/memory/phase-2/constitution.md` (Version 1.0.0).

Key decisions made:
- **Separate file location**: Created new constitution at `.specify/memory/phase-2/constitution.md` to preserve Phase 1 constitution (frozen at `.specify/memory/constitution.md`)
- **Reconstructed corrupted text**: Fixed merged/corrupted sections from user input
- **Added explicit data model**: User and Task schema requirements
- **Added API endpoint structure**: Full REST API contract
- **Added security best practices**: Password hashing, CORS, JWT secret handling
- **Added out-of-scope items**: Explicit exclusions for Phase 2

The constitution defines:
- 3 Core Principles (Spec-Driven, Phase Isolation, Full-Stack Architecture)
- Technology stack (Next.js, FastAPI, SQLModel, Neon PostgreSQL, Better Auth)
- Monorepo folder governance (frontend/, backend/)
- Authentication & JWT enforcement rules
- 8 features (5 task operations + 3 auth operations)
- 11 completion criteria checkboxes

## Outcome

- ✅ Impact: Established governance foundation for Phase 2 full-stack development
- 🧪 Tests: N/A (governance document)
- 📁 Files: 1 created (.specify/memory/phase-2/constitution.md)
- 🔁 Next prompts: Create Phase 2 feature specifications, Start with auth spec or backend setup
- 🧠 Reflection: Phase isolation preserved by creating separate constitution file; corrupted input was reconstructed from context

## Evaluation notes (flywheel)

- Failure modes observed: None - user confirmed Option A (separate file)
- Graders run and results (PASS/FAIL): Manual validation PASS - no unresolved placeholders, proper structure
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
