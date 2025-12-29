"""Authentication service for user registration and login."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from ..core.security import hash_password, verify_password, create_access_token
from ..models.user import User, UserCreate, UserLogin


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    """Get a user by email address."""
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def register_user(session: AsyncSession, user_data: UserCreate) -> User:
    """
    Register a new user.

    Args:
        session: Database session
        user_data: User registration data

    Returns:
        Created user object

    Raises:
        ValueError: If email already exists
    """
    # Check if email already exists
    existing_user = await get_user_by_email(session, user_data.email)
    if existing_user:
        raise ValueError("Email already registered")

    # Hash password and create user
    password_hash = hash_password(user_data.password)
    user = User(
        email=user_data.email,
        password_hash=password_hash,
    )

    session.add(user)
    await session.flush()
    await session.refresh(user)

    return user


async def login_user(
    session: AsyncSession, login_data: UserLogin
) -> tuple[User, str]:
    """
    Authenticate a user and issue JWT token.

    Args:
        session: Database session
        login_data: Login credentials

    Returns:
        Tuple of (user, access_token)

    Raises:
        ValueError: If credentials are invalid
    """
    # Get user by email
    user = await get_user_by_email(session, login_data.email)
    if not user:
        raise ValueError("Invalid email or password")

    # Verify password
    if not verify_password(login_data.password, user.password_hash):
        raise ValueError("Invalid email or password")

    # Create access token - sub must be a string per JWT spec
    token_data = {
        "sub": str(user.id),
        "email": user.email,
    }
    access_token = create_access_token(token_data)

    return user, access_token
