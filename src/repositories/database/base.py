from abc import ABC
from dataclasses import dataclass
from typing import Iterable, Any

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.sql import Executable

from src.core.config import settings
from src.models.base import Base


engine = create_async_engine(url=settings.db_url, echo=settings.echo)
sessionmaker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


@dataclass
class BaseDatabaseRepository(ABC): ...


@dataclass
class DatabaseRepositories(ABC): ...


@dataclass
class SQLAlchemyRepository(BaseDatabaseRepository):
    async def add(self, obj: Base) -> None:
        async with sessionmaker() as session:
            session.add(obj)
            await session.commit()
            await engine.dispose()

    async def merge(self, obj: Base) -> None:
        async with sessionmaker() as session:
            await session.merge(obj)

    async def execute(self, statement: Executable) -> None:
        async with sessionmaker() as session:
            await session.execute(statement)

    async def get(self, table: type[Base], primary_key: Any):  # type: ignore[no-untyped-def]
        async with sessionmaker() as session:
            model = await session.get(table, primary_key)
        return model

    async def scalar(self, statement: Executable) -> Any:
        async with sessionmaker() as session:
            item = await session.scalar(statement)
        return item

    async def scalars(self, statement: Executable) -> Iterable:
        async with sessionmaker() as session:
            items = await session.scalars(statement)
        return items
