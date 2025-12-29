# Data Model: Phase 2 Full-Stack Todo Web Application

**Feature**: 002-fullstack-todo-web
**Date**: 2025-12-29
**Database**: Neon Serverless PostgreSQL
**ORM**: SQLModel

---

## Entity Overview

```
┌─────────────────┐         ┌─────────────────┐
│      User       │         │      Task       │
├─────────────────┤         ├─────────────────┤
│ id (PK)         │────────<│ id (PK)         │
│ email (unique)  │         │ user_id (FK)    │
│ password_hash   │         │ title           │
│ created_at      │         │ description     │
└─────────────────┘         │ completed       │
                            │ created_at      │
                            │ updated_at      │
                            └─────────────────┘

Relationship: User (1) ──── (0..*) Task
```

---

## Entity Definitions

### User

Represents an authenticated account holder in the system.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | PK, Auto-increment | Unique identifier |
| `email` | String(255) | Unique, Not Null, Indexed | User's email address (login identifier) |
| `password_hash` | String(255) | Not Null | bcrypt-hashed password |
| `created_at` | DateTime | Not Null, Default: now() | Account creation timestamp |

**Validation Rules**:
- Email must be valid format (RFC 5322 compliant)
- Email must be unique across all users
- Password hash is generated from password with minimum 8 characters

**Indexes**:
- Primary key on `id`
- Unique index on `email`

---

### Task

Represents a todo item owned by a specific user.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | PK, Auto-increment | Unique identifier |
| `user_id` | Integer | FK → User.id, Not Null, Indexed | Owner of the task |
| `title` | String(200) | Not Null | Task title (1-200 chars) |
| `description` | String(2000) | Nullable | Optional task description (0-2000 chars) |
| `completed` | Boolean | Not Null, Default: false | Completion status |
| `created_at` | DateTime | Not Null, Default: now() | Task creation timestamp |
| `updated_at` | DateTime | Not Null, Default: now(), On Update: now() | Last modification timestamp |

**Validation Rules**:
- Title must not be empty
- Title must not exceed 200 characters
- Description must not exceed 2000 characters (if provided)
- user_id must reference an existing User

**Indexes**:
- Primary key on `id`
- Index on `user_id` (for efficient user task queries)
- Composite index on `(user_id, completed)` (optional, for filtered queries)

**Cascade Behavior**:
- On User delete: CASCADE (delete all user's tasks)

---

## SQLModel Definitions

### Base Models (Shared Fields)

```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class UserBase(SQLModel):
    email: str = Field(max_length=255, index=True, unique=True)

class TaskBase(SQLModel):
    title: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)
```

### Database Models (table=True)

```python
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    tasks: list["Task"] = Relationship(back_populates="user")

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    user: Optional[User] = Relationship(back_populates="tasks")
```

### API Schemas (Request/Response)

```python
# User Schemas
class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserRead(UserBase):
    id: int
    created_at: datetime

class UserLogin(SQLModel):
    email: str
    password: str

# Task Schemas
class TaskCreate(TaskBase):
    pass  # title required, description optional

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)

class TaskRead(TaskBase):
    id: int
    user_id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
```

---

## State Transitions

### Task Completion State Machine

```
┌──────────┐                    ┌───────────┐
│ Pending  │ ───── toggle ────> │ Completed │
│ (false)  │ <──── toggle ───── │ (true)    │
└──────────┘                    └───────────┘
```

- Initial state: `Pending` (completed = false)
- Toggle action: Flips `completed` boolean
- No intermediate states
- Always updates `updated_at` timestamp

---

## Database Schema (SQL)

```sql
-- Users table
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_email ON "user"(email);

-- Tasks table
CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description VARCHAR(2000),
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_task_user_id ON task(user_id);
```

---

## Migration Strategy

### Initial Migration (v1)
1. Create `user` table
2. Create `task` table with foreign key

### Future Migrations (if needed)
- Use Alembic for version-controlled migrations
- All schema changes must be documented in specs first
- Backwards-compatible changes preferred

---

## Data Integrity Rules

### Constraints Enforced at Database Level
1. User email uniqueness
2. Task user_id foreign key
3. Not null constraints
4. Max length constraints

### Constraints Enforced at Application Level
1. Email format validation
2. Password minimum length
3. Empty title rejection
4. User ownership verification (security)

---

## Query Patterns

### Common Queries

| Operation | Query Pattern |
|-----------|---------------|
| Get user by email | `SELECT * FROM user WHERE email = ?` |
| Get user's tasks | `SELECT * FROM task WHERE user_id = ?` |
| Get single task (with ownership) | `SELECT * FROM task WHERE id = ? AND user_id = ?` |
| Create task | `INSERT INTO task (user_id, title, description) VALUES (?, ?, ?)` |
| Update task | `UPDATE task SET title=?, description=?, updated_at=now() WHERE id=? AND user_id=?` |
| Toggle completion | `UPDATE task SET completed = NOT completed, updated_at=now() WHERE id=? AND user_id=?` |
| Delete task | `DELETE FROM task WHERE id = ? AND user_id = ?` |

### Security Note
All task queries MUST include `user_id` filter to enforce ownership isolation.
