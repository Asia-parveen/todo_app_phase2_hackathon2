"""Task model and schemas."""

from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class TaskBase(SQLModel):
    """Base task schema with shared fields."""

    title: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)


class Task(TaskBase, table=True):
    """Task database model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TaskCreate(SQLModel):
    """Schema for creating a new task."""

    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)


class TaskUpdate(SQLModel):
    """Schema for updating a task."""

    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)


class TaskRead(TaskBase):
    """Schema for reading task data."""

    id: int
    user_id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
