from abc import ABC
from dataclasses import dataclass
from typing import Iterable, Any

from sqlalchemy.sql import Executable

from src.models.base import Base
from src.repositories.database.db_connecter import DB


@dataclass
class BaseDatabaseRepository(ABC):
    ...


@dataclass
class DatabaseRepositories(ABC):
    ...


@dataclass
class SQLAlchemyRepository(BaseDatabaseRepository, DB):

    async def add(self, obj: Base) -> None:
        async with self.sessionmaker() as session:
            session.add(obj)
            await session.commit()
            await self.engine().dispose()

    async def merge(self, obj: Base) -> None:
        async with self.sessionmaker() as session:
            await session.merge(obj)

    async def execute(self, statement: Executable) -> None:
        async with self.sessionmaker() as session:
            await session.execute(statement)

    async def get(self, table: type[Base], primary_key: Any):  # type: ignore[no-untyped-def]
        async with self.sessionmaker() as session:
            model = await session.get(table, primary_key)
        return model

    async def scalar(self, statement: Executable) -> Any:
        async with self.sessionmaker() as session:
            item = await session.scalar(statement)
        return item

    async def scalars(self, statement: Executable) -> Iterable:
        async with self.sessionmaker() as session:
            items = await session.scalars(statement)
        return items
