# Research: Phase 2 Full-Stack Todo Web Application

**Feature**: 002-fullstack-todo-web
**Date**: 2025-12-29
**Purpose**: Resolve technical decisions and document best practices for implementation

---

## Research Areas

### 1. Better Auth Integration Pattern

**Context**: Constitution specifies Better Auth for JWT authentication, but Better Auth is a TypeScript/Node.js library. Backend is Python FastAPI.

**Decision**: Hybrid Authentication Architecture
- Better Auth runs on the **Next.js frontend** for user registration, login, and JWT issuance
- FastAPI backend **validates JWTs** issued by Better Auth (does not issue tokens)
- JWT verification in Python using `python-jose` or `PyJWT` library

**Rationale**:
- Better Auth is designed for Node.js/Next.js environments
- FastAPI excels at JWT validation but doesn't need to manage auth sessions
- This maintains clean separation: frontend handles auth UX, backend validates tokens

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| Better Auth on backend | Not compatible with Python |
| Pure FastAPI auth (no Better Auth) | Violates constitution requirement |
| Auth microservice | Over-engineering for Phase 2 scope |

**Implementation Pattern**:
```
Frontend (Next.js + Better Auth):
  - /auth/register → Better Auth handles registration
  - /auth/login → Better Auth issues JWT
  - Stores JWT in httpOnly cookie or localStorage

Backend (FastAPI):
  - Middleware validates JWT on protected routes
  - Extracts user_id from JWT claims
  - No auth session management
```

---

### 2. JWT Secret Sharing

**Context**: Better Auth issues JWTs on frontend, FastAPI validates on backend. Both need the same secret.

**Decision**: Shared JWT Secret via Environment Variables
- Same `JWT_SECRET` environment variable on both frontend and backend
- Use asymmetric keys (RS256) if security concerns arise in future

**Rationale**:
- Simplest approach for Phase 2
- Environment variables are secure and platform-agnostic
- RS256 adds complexity without Phase 2 benefit

**Configuration**:
```
Frontend (.env.local):
  BETTER_AUTH_SECRET=<shared-secret>

Backend (.env):
  JWT_SECRET=<same-shared-secret>
  JWT_ALGORITHM=HS256
```

---

### 3. Neon PostgreSQL Connection

**Context**: Constitution requires Neon Serverless PostgreSQL.

**Decision**: Direct Connection with Connection Pooling
- Use Neon's pooled connection string
- SQLModel/SQLAlchemy async driver (`asyncpg`)
- Connection string via environment variable

**Rationale**:
- Neon provides serverless-optimized connection pooling
- asyncpg is the standard async PostgreSQL driver for Python
- Matches FastAPI's async-first design

**Configuration**:
```
Backend (.env):
  DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>/<database>?sslmode=require
```

**Best Practices**:
- Use connection pooling (Neon provides this)
- Set reasonable pool size (5-10 for moderate load)
- Enable SSL (required by Neon)

---

### 4. Frontend-Backend Communication

**Context**: Constitution requires HTTP-only communication, no shared code.

**Decision**: REST API with JSON
- All communication via JSON over HTTPS
- Frontend uses native `fetch` or lightweight wrapper
- No shared TypeScript types (duplicate definitions)

**Rationale**:
- REST is simple and well-understood
- JSON is native to both TypeScript and Python
- Avoids complexity of GraphQL for simple CRUD

**API Base URL Configuration**:
```
Frontend (.env.local):
  NEXT_PUBLIC_API_URL=http://localhost:8000/api  # development
  NEXT_PUBLIC_API_URL=https://api.example.com/api  # production
```

---

### 5. CORS Configuration

**Context**: Frontend (Vercel) and Backend (separate host) are different origins.

**Decision**: Explicit CORS Allowlist
- Backend allows only known frontend origins
- Credentials (cookies/auth headers) enabled
- Preflight caching for performance

**Configuration**:
```python
# FastAPI CORS middleware
origins = [
    "http://localhost:3000",  # development
    "https://your-app.vercel.app",  # production
]
```

**Best Practices**:
- Never use `*` with credentials
- List specific origins only
- Set appropriate max_age for preflight cache

---

### 6. Password Hashing

**Context**: Constitution requires passwords to be hashed.

**Decision**: bcrypt via `passlib`
- Industry-standard password hashing
- Built-in salt generation
- Configurable work factor

**Rationale**:
- bcrypt is battle-tested and recommended
- passlib provides clean Python API
- Automatic salt handling prevents common mistakes

**Implementation**:
```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
hashed = pwd_context.hash(password)

# Verify password
pwd_context.verify(password, hashed)
```

---

### 7. SQLModel Best Practices

**Context**: Constitution requires SQLModel ORM.

**Decision**: Async SQLModel with Pydantic Integration
- Use SQLModel for both ORM models and API schemas
- Async session management with `async_sessionmaker`
- Alembic for migrations

**Rationale**:
- SQLModel unifies SQLAlchemy and Pydantic
- Reduces code duplication between models and schemas
- Alembic is the standard migration tool

**Model Pattern**:
```python
from sqlmodel import SQLModel, Field
from datetime import datetime

class TaskBase(SQLModel):
    title: str = Field(max_length=200)
    description: str | None = Field(default=None, max_length=2000)

class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

---

### 8. Next.js App Router Patterns

**Context**: Constitution requires Next.js App Router.

**Decision**: Server Components with Client Islands
- Default to Server Components for data fetching
- Client Components (`"use client"`) for interactivity
- Route handlers for BFF (Backend-for-Frontend) patterns if needed

**Rationale**:
- Server Components reduce client-side JavaScript
- Better Auth integration works with both patterns
- Follows Next.js 14+ best practices

**Structure**:
```
frontend/
├── app/
│   ├── layout.tsx        # Root layout
│   ├── page.tsx          # Home/landing
│   ├── (auth)/
│   │   ├── login/page.tsx
│   │   └── register/page.tsx
│   └── (dashboard)/
│       └── tasks/page.tsx
├── components/
│   ├── ui/               # Reusable UI components
│   └── tasks/            # Task-specific components
└── lib/
    ├── auth.ts           # Better Auth client
    └── api.ts            # API client functions
```

---

### 9. Error Handling Strategy

**Context**: Constitution requires consistent error responses.

**Decision**: Standardized Error Format
- All errors return JSON with `error` code and `message`
- HTTP status codes follow REST conventions
- Frontend displays user-friendly messages

**Backend Error Response**:
```python
from fastapi import HTTPException

class AppException(HTTPException):
    def __init__(self, status_code: int, error: str, message: str):
        super().__init__(
            status_code=status_code,
            detail={"error": error, "message": message}
        )

# Usage
raise AppException(404, "task_not_found", "Task does not exist")
```

**Frontend Error Handling**:
```typescript
try {
  const response = await fetch(...)
  if (!response.ok) {
    const error = await response.json()
    // Display error.message to user
  }
} catch (e) {
  // Network error - display connection message
}
```

---

### 10. Testing Strategy

**Context**: Constitution requires testable code.

**Decision**: Layered Testing Approach
- **Backend**: pytest with httpx for API testing
- **Frontend**: Jest + React Testing Library for components
- **E2E**: Optional Playwright for critical flows

**Rationale**:
- pytest is Python standard
- httpx provides async test client for FastAPI
- React Testing Library follows testing best practices

**Test Structure**:
```
backend/
└── tests/
    ├── conftest.py       # Fixtures
    ├── test_auth.py      # Auth endpoint tests
    └── test_tasks.py     # Task endpoint tests

frontend/
└── __tests__/
    ├── components/       # Component tests
    └── pages/            # Page tests
```

---

## Summary of Decisions

| Area | Decision | Key Technology |
|------|----------|----------------|
| Authentication | Hybrid (Better Auth frontend, JWT validation backend) | Better Auth, PyJWT |
| JWT | Shared secret via env vars, HS256 | python-jose |
| Database | Neon with asyncpg | SQLModel, asyncpg |
| API Communication | REST + JSON | fetch, FastAPI |
| CORS | Explicit allowlist | FastAPI CORSMiddleware |
| Passwords | bcrypt hashing | passlib |
| ORM | SQLModel async | SQLModel, Alembic |
| Frontend | App Router, Server Components | Next.js 14+ |
| Errors | Standardized JSON format | Custom exception classes |
| Testing | pytest + Jest | pytest, httpx, RTL |

---

## Unresolved Items

None - all technical decisions resolved based on constitution constraints.

---

## References

- [Better Auth Documentation](https://www.better-auth.com/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Neon Documentation](https://neon.tech/docs)
- [Next.js App Router](https://nextjs.org/docs/app)
