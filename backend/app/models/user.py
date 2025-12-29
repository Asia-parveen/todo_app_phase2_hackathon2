from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    """Base user schema with shared fields."""
    email: str = Field(max_length=255, index=True, unique=True)


class User(UserBase, table=True):
    """User database model."""
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(SQLModel):
    """Schema for creating a new user."""
    email: str = Field(max_length=255)
    password: str = Field(min_length=8)


class UserRead(UserBase):
    """Schema for reading user data (public)."""
    id: int
    created_at: datetime


class UserLogin(SQLModel):
    """Schema for user login."""
    email: str
    password: str
