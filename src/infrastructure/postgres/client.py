from dataclasses import dataclass
from enum import Enum
from typing import AsyncGenerator, Any

from sqlalchemy import Executable
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.domain.repositories import BaseStorageRepositoryMixinSession, BaseStorageRepositoryMixin
from src.infrastructure.config import settings
from src.infrastructure.postgres.orm import Base

engine = create_async_engine(url=settings.db_url, echo=settings.echo)
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


class ExecuteAction(Enum):
    scalars = 'scalars'
    scalar = 'scalar'
    execute = 'execute'


@dataclass
class Session(BaseStorageRepositoryMixinSession, AsyncSession):
    table: type[Base]

    async def read(self, obj_id: int) -> Any | None:
        return await self.get(self.table, obj_id)

    async def write(self, obj) -> None:  # type: ignore[no-untyped-def]
        self.add(obj)

    async def update(self, obj: Base) -> None:
        response = await self.get(obj.__class__, obj.id)
        if response:
            await self.merge(obj)

    async def remove(self, table: type[Base], obj_id: int) -> None:
        obj = await self.get(table, obj_id)
        await self.delete(obj)

    async def run(self, statement: Executable, action: ExecuteAction) -> Base | list[Base] | None:  # type: ignore[return]
        if action == action.scalars:
            return list(await self.scalars(statement))
        elif action == action.scalar:
            return await self.scalar(statement)
        elif action == action.execute:
            await self.execute(statement)


@dataclass
class SQLAlchemyRepository(BaseStorageRepositoryMixin):
    table: type[Base]

    async def start(self) -> AsyncGenerator[Session]:
        async with Session(table=self.table) as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
