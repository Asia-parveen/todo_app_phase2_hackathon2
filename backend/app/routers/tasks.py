"""Tasks router for CRUD operations."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_session
from ..dependencies import get_current_user
from ..models.task import Task, TaskCreate, TaskUpdate, TaskRead
from ..models.user import User
from ..services import tasks as task_service

router = APIRouter()


@router.get("", response_model=list[TaskRead])
async def get_tasks(
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Get all tasks for the current user."""
    tasks = await task_service.get_user_tasks(session, current_user.id)
    return tasks


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Get a single task by ID."""
    task = await task_service.get_task_by_id(session, task_id, current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "not_found", "message": "Task not found"},
        )
    return task


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskRead)
async def create_task(
    task_data: TaskCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Create a new task."""
    task = await task_service.create_task(session, current_user.id, task_data)
    return task


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Update a task."""
    task = await task_service.get_task_by_id(session, task_id, current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "not_found", "message": "Task not found"},
        )
    updated_task = await task_service.update_task(session, task, task_data)
    return updated_task


@router.patch("/{task_id}/complete", response_model=TaskRead)
async def toggle_task_completion(
    task_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Toggle task completion status."""
    task = await task_service.get_task_by_id(session, task_id, current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "not_found", "message": "Task not found"},
        )
    updated_task = await task_service.toggle_task_completion(session, task)
    return updated_task


@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Delete a task."""
    task = await task_service.get_task_by_id(session, task_id, current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "not_found", "message": "Task not found"},
        )
    await task_service.delete_task(session, task)
    return {"message": "Task deleted successfully"}
