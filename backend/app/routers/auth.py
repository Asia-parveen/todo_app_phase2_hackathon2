"""Authentication router for registration, login, and logout."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_session
from ..models.user import UserCreate, UserLogin, UserRead
from ..services.auth import register_user, login_user

router = APIRouter()


class AuthResponse:
    """Response model for authentication."""

    def __init__(self, access_token: str, token_type: str, user: UserRead):
        self.access_token = access_token
        self.token_type = token_type
        self.user = user


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Register a new user.

    Returns:
        201: User created successfully
        400: Email already exists or validation error
    """
    try:
        user = await register_user(session, user_data)
        return {
            "message": "User registered successfully",
            "user": UserRead.model_validate(user),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "registration_failed", "message": str(e)},
        )


@router.post("/login")
async def login(
    login_data: UserLogin,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Authenticate user and return JWT token.

    Returns:
        200: Login successful with access token
        401: Invalid credentials
    """
    try:
        user, access_token = await login_user(session, login_data)
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": UserRead.model_validate(user),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "unauthorized", "message": str(e)},
        )


@router.post("/logout")
async def logout():
    """
    Logout the current user.

    Note: Since we use JWT tokens, logout is primarily client-side.
    The server just acknowledges the request.

    Returns:
        200: Logout successful
    """
    return {"message": "Logged out successfully"}
