import ssl
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

from .config import get_settings

settings = get_settings()


def get_async_database_url() -> tuple[str, dict]:
    """
    Parse database URL and extract SSL settings for asyncpg.

    asyncpg doesn't accept many query parameters that psycopg2/libpq accept.
    We need to strip them and handle SSL via connect_args.

    Also converts postgresql:// to postgresql+asyncpg:// for async support.
    """
    url = settings.database_url
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    # Convert scheme to async driver
    scheme = parsed.scheme
    if scheme == "postgresql":
        scheme = "postgresql+asyncpg"
    elif scheme == "postgres":
        scheme = "postgresql+asyncpg"

    # Extract SSL mode before removing incompatible params
    ssl_mode = query_params.get("sslmode", [None])[0]

    # Remove all parameters that asyncpg doesn't support
    # asyncpg only supports: host, port, user, password, database, ssl, timeout, etc.
    unsupported_params = [
        "sslmode", "channel_binding", "sslcert", "sslkey", "sslrootcert",
        "sslcrl", "application_name", "options", "keepalives", "keepalives_idle",
        "keepalives_interval", "keepalives_count", "target_session_attrs",
    ]
    for param in unsupported_params:
        query_params.pop(param, None)

    # Rebuild URL without unsupported params and with async scheme
    new_query = urlencode(query_params, doseq=True)
    clean_url = urlunparse((
        scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        new_query,
        parsed.fragment,
    ))

    # Configure SSL for asyncpg
    connect_args = {}
    if ssl_mode in ("require", "verify-ca", "verify-full", "prefer"):
        # Create SSL context for secure connection
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        connect_args["ssl"] = ssl_context

    return clean_url, connect_args


database_url, connect_args = get_async_database_url()

# Create async engine
engine = create_async_engine(
    database_url,
    echo=False,
    future=True,
    connect_args=connect_args,
)

# Create async session factory
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_db() -> None:
    """Initialize database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get database session."""
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
