"""Task service for CRUD operations."""

from datetime import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from ..models.task import Task, TaskCreate, TaskUpdate


async def get_user_tasks(session: AsyncSession, user_id: int) -> list[Task]:
    """Get all tasks for a user."""
    result = await session.execute(
        select(Task).where(Task.user_id == user_id).order_by(Task.created_at.desc())
    )
    return list(result.scalars().all())


async def get_task_by_id(
    session: AsyncSession, task_id: int, user_id: int
) -> Task | None:
    """Get a single task by ID, ensuring it belongs to the user."""
    result = await session.execute(
        select(Task).where(Task.id == task_id, Task.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def create_task(
    session: AsyncSession, user_id: int, task_data: TaskCreate
) -> Task:
    """Create a new task for a user."""
    task = Task(
        user_id=user_id,
        title=task_data.title,
        description=task_data.description,
    )
    session.add(task)
    await session.flush()
    await session.refresh(task)
    return task


async def update_task(
    session: AsyncSession, task: Task, task_data: TaskUpdate
) -> Task:
    """Update an existing task."""
    update_data = task_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.utcnow()
    await session.flush()
    await session.refresh(task)
    return task


async def toggle_task_completion(session: AsyncSession, task: Task) -> Task:
    """Toggle the completion status of a task."""
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()
    await session.flush()
    await session.refresh(task)
    return task


async def delete_task(session: AsyncSession, task: Task) -> None:
    """Delete a task."""
    await session.delete(task)
    await session.flush()
