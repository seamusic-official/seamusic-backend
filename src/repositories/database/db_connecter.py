"""SqlAlchemy connector to session."""
from typing import Any

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from asyncio import current_task

from src.core.config import settings


class DB:
    """DB halper."""
    
    @staticmethod
    def engine() -> "AsyncEngine":
        """Create async engine."""
        return create_async_engine(
            url=settings.db_url, echo=settings.echo, pool_pre_ping=True
        )
    
    @staticmethod
    def _create_session(
            engine: "AsyncEngine",
    ) -> "async_sessionmaker[AsyncSession]":
        """Create db session."""
        return async_sessionmaker(
            bind=engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
            class_=AsyncSession,
        )
    
    @property
    def sessionmaker(self) -> async_scoped_session[AsyncSession | Any]:
        """Return current scope."""
        return async_scoped_session(
            session_factory=self._create_session(
                self.engine()
            ),
            scopefunc=current_task,
        )
