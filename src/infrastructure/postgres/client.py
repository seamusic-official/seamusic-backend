from dataclasses import dataclass
from typing import Any, Literal

from sqlalchemy import Executable
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.infrastructure.config import settings
from src.infrastructure.postgres.orm import Base

engine = create_async_engine(url=settings.db_url, echo=settings.echo)
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


@dataclass
class PostgresSessionMixin(AsyncSession):
    table: type[Base]

    async def read(self, obj_id: int) -> Any | None:
        return await self.get(self.table, obj_id)

    async def write(self, obj) -> None:  # type: ignore[no-untyped-def]
        self.add(obj)

    async def update(self, obj: Base) -> None:
        await self.merge(obj)

    async def remove(self, obj_id: int) -> None:
        obj = await self.get(self.table, obj_id)
        await self.delete(obj)

    async def run(self, statement: Executable, action: Literal['scalars', 'scalar', 'execute']) -> Base | list[Base] | int | None:  # type: ignore[return]
        if action == 'scalars':
            return list(await self.scalars(statement))
        elif action == 'scalar':
            return await self.scalar(statement)
        elif action == 'execute':
            await self.execute(statement)
