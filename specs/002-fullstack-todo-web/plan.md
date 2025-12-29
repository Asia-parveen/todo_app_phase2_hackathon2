# Implementation Plan: Phase 2 Full-Stack Todo Web Application

**Branch**: `002-fullstack-todo-web` | **Date**: 2025-12-29 | **Spec**: [spec.md](./spec.md)
**Constitution**: [.specify/memory/phase-2/constitution.md](../../.specify/memory/phase-2/constitution.md)

---

## Summary

Transform the Phase 1 CLI-based in-memory Todo application into a secure, persistent, multi-user full-stack web application. The system consists of two independently deployable applications:

- **Frontend**: Next.js (App Router) + TypeScript + Tailwind CSS deployed to Vercel
- **Backend**: Python FastAPI + SQLModel + Neon PostgreSQL deployed to cloud platform

Key technical approach: Hybrid authentication with Better Auth on frontend issuing JWTs, FastAPI backend validating JWTs and enforcing user isolation at API and database levels.

---

## Technical Context

**Language/Version**:
- Frontend: TypeScript 5.x, Node.js 18+
- Backend: Python 3.11+

**Primary Dependencies**:
- Frontend: Next.js 14+, Better Auth, Tailwind CSS
- Backend: FastAPI, SQLModel, asyncpg, python-jose, passlib

**Storage**: Neon Serverless PostgreSQL (asyncpg driver)

**Testing**:
- Backend: pytest + httpx
- Frontend: Jest + React Testing Library

**Target Platform**:
- Frontend: Vercel (Edge-compatible)
- Backend: Any FastAPI-compatible platform (Railway, Render, Fly.io)

**Project Type**: Web (frontend + backend)

**Performance Goals**:
- Registration: < 30 seconds
- Login to task list: < 5 seconds
- Task operations: < 10 seconds

**Constraints**:
- Stateless backend
- Environment-variable driven configuration
- No platform-specific assumptions
- JWT-secured APIs

**Scale/Scope**: Moderate user base, standard web application load

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| Spec-Driven Development | ✅ PASS | Following Specify → Plan → Tasks → Implement lifecycle |
| Phase Isolation | ✅ PASS | Phase 1 artifacts unchanged, separate constitution |
| Full-Stack Architecture | ✅ PASS | Next.js frontend + FastAPI backend |
| Monorepo Structure | ✅ PASS | /frontend and /backend folders |
| Frontend Folder Rules | ✅ PASS | All frontend code in /frontend, Vercel-deployable |
| Backend Folder Rules | ✅ PASS | All backend code in /backend, no frontend dependencies |
| No Cross-Folder Coupling | ✅ PASS | HTTP API communication only |
| Technology Constraints | ✅ PASS | Using mandated stack exactly |
| Authentication Mandatory | ✅ PASS | Better Auth + JWT implemented |
| JWT Enforcement | ✅ PASS | All protected routes require Bearer token |
| User Isolation | ✅ PASS | Task ownership enforced at API and DB levels |
| Persistent Storage | ✅ PASS | Neon PostgreSQL, no in-memory storage |
| RESTful APIs | ✅ PASS | Standard REST conventions followed |
| Manual Coding Prohibited | ✅ PASS | All code via Claude Code + Spec-Kit |

**Gate Result**: ✅ ALL CHECKS PASS - Proceeding with implementation

---

## Project Structure

### Documentation (this feature)

```text
specs/002-fullstack-todo-web/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0: Technical decisions
├── data-model.md        # Phase 1: Entity definitions
├── quickstart.md        # Phase 1: Setup guide
├── contracts/
│   └── openapi.yaml     # Phase 1: API contract
├── checklists/
│   └── requirements.md  # Spec validation checklist
└── tasks.md             # Phase 2: Implementation tasks (via /sp.tasks)
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Environment configuration
│   │   ├── security.py      # JWT validation, password hashing
│   │   └── database.py      # Async database session
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User SQLModel
│   │   └── task.py          # Task SQLModel
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py          # /api/auth/* routes
│   │   └── tasks.py         # /api/tasks/* routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py          # Auth business logic
│   │   └── tasks.py         # Task business logic
│   └── dependencies.py      # FastAPI dependencies (get_current_user)
├── tests/
│   ├── conftest.py          # Test fixtures
│   ├── test_auth.py         # Auth endpoint tests
│   └── test_tasks.py        # Task endpoint tests
├── alembic/                 # Database migrations
│   └── versions/
├── alembic.ini
├── requirements.txt
├── .env.example
└── .gitignore

frontend/
├── app/
│   ├── layout.tsx           # Root layout with auth provider
│   ├── page.tsx             # Landing/redirect page
│   ├── globals.css          # Tailwind imports
│   ├── (auth)/
│   │   ├── login/
│   │   │   └── page.tsx     # Login page
│   │   └── register/
│   │       └── page.tsx     # Registration page
│   └── (dashboard)/
│       ├── layout.tsx       # Protected layout with auth check
│       └── tasks/
│           └── page.tsx     # Main task list page
├── components/
│   ├── ui/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   └── Loading.tsx
│   ├── auth/
│   │   ├── LoginForm.tsx
│   │   └── RegisterForm.tsx
│   └── tasks/
│       ├── TaskList.tsx
│       ├── TaskItem.tsx
│       ├── TaskForm.tsx
│       └── TaskDeleteConfirm.tsx
├── lib/
│   ├── auth.ts              # Better Auth client setup
│   ├── api.ts               # API client with auth headers
│   └── types.ts             # TypeScript type definitions
├── __tests__/
│   ├── components/
│   └── pages/
├── public/
├── tailwind.config.ts
├── next.config.js
├── package.json
├── tsconfig.json
├── .env.example
└── .gitignore
```

**Structure Decision**: Web application (Option 2) - separate frontend and backend folders per constitution requirements. No shared code between folders; communication via HTTP APIs only.

---

## Implementation Phases

### Phase 1: Backend Foundation
1. Project setup (FastAPI, dependencies, configuration)
2. Database connection (Neon, SQLModel, async sessions)
3. User model and auth service (registration, login, JWT validation)
4. Auth routes (/api/auth/*)

### Phase 2: Backend Task API
1. Task model
2. Task service (CRUD with user isolation)
3. Task routes (/api/tasks/*)
4. Backend tests

### Phase 3: Frontend Foundation
1. Next.js project setup (App Router, Tailwind)
2. Better Auth integration
3. Auth pages (login, register)
4. API client setup

### Phase 4: Frontend Task UI
1. Protected layout and routing
2. Task list page and components
3. Task CRUD operations
4. Loading and error states

### Phase 5: Integration & Deployment
1. End-to-end testing
2. Environment configuration for production
3. Deploy backend
4. Deploy frontend
5. Verify completion criteria

---

## Complexity Tracking

> No constitution violations requiring justification. All implementation follows mandated patterns.

| Aspect | Complexity | Justification |
|--------|------------|---------------|
| Two deployable applications | Required | Constitution mandates frontend/backend separation |
| JWT authentication | Required | Constitution mandates Better Auth + JWT |
| PostgreSQL persistence | Required | Constitution forbids in-memory storage |

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Better Auth + FastAPI integration complexity | Medium | Hybrid approach documented in research.md |
| Neon connection issues (cold starts) | Low | Use pooled connections, document retry logic |
| CORS misconfiguration | Low | Explicit allowlist in config |
| JWT secret mismatch | Medium | Clear documentation, environment validation |

---

## Dependencies Between Artifacts

```
spec.md
    ↓
research.md (technical decisions)
    ↓
data-model.md (entities from spec + research)
    ↓
contracts/openapi.yaml (API from spec requirements)
    ↓
plan.md (this document - integrates all above)
    ↓
tasks.md (generated via /sp.tasks from plan)
    ↓
Implementation (code follows tasks)
```

---

## Next Steps

1. Run `/sp.tasks` to generate implementation task list
2. Tasks will be ordered: backend → frontend → integration
3. Each task will reference specific spec requirements and contract endpoints

---

## References

- [Specification](./spec.md)
- [Research Decisions](./research.md)
- [Data Model](./data-model.md)
- [API Contract](./contracts/openapi.yaml)
- [Quickstart Guide](./quickstart.md)
- [Phase 2 Constitution](../../.specify/memory/phase-2/constitution.md)
