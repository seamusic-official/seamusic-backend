from abc import ABC
from dataclasses import dataclass
from typing import Iterable, Any

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.sql import Executable

from src.core.config import settings
from src.models.base import Base


@dataclass
class BaseDatabaseRepository(ABC):
    ...


@dataclass
class DatabaseRepositories(ABC):
    ...


@dataclass
class SQLAlchemyRepository(BaseDatabaseRepository):

    engine = create_async_engine(url=settings.db_url, echo=settings.echo)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    async def add(self, obj: Base) -> None:
        async with self.sessionmaker() as session:
            session.add(obj)
            await session.commit()

    async def merge(self, obj: Base) -> None:
        async with self.sessionmaker() as session:
            await session.merge(obj)

    async def execute(self, statement: Executable) -> None:
        async with self.sessionmaker() as session:
            await session.execute(statement)

    async def get(self, table: type[Base], primary_key: Any) -> Base | None:
        async with self.sessionmaker() as session:
            return await session.get(table, primary_key)

    async def scalar(self, statement: Executable) -> Any:
        async with self.sessionmaker() as session:
            return await session.scalar(statement)

    async def scalars(self, statement: Executable) -> Iterable:
        async with self.sessionmaker() as session:
            return await session.scalars(statement)
