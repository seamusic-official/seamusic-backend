from dataclasses import dataclass

from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.domain.repositories import BaseDatabaseRepository
from src.infrastructure.config import settings
from src.infrastructure.postgres.exceptions import NotFoundError
from src.infrastructure.postgres.orm import Base

engine = create_async_engine(url=settings.db_url, echo=settings.echo)
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


@dataclass
class SQLAlchemyRepository(BaseDatabaseRepository):
    @staticmethod
    async def read(obj_id: int, table: type[Base]) -> Base | None:
        async with sessionmaker() as session:
            try:
                response = await session.get_one(table, obj_id)
            except NoResultFound:
                response = None
        return response

    @staticmethod
    async def write(obj: Base) -> None:
        async with sessionmaker() as session:
            session.add(obj)
            await session.commit()

    @staticmethod
    async def update(obj: Base) -> None:
        async with sessionmaker() as session:
            try:
                await session.get_one(obj.__class__, obj.id)
            except NoResultFound:
                raise NotFoundError()
            await session.merge(obj)
            await session.commit()

    @staticmethod
    async def delete(obj_id: int, table: type[Base]) -> None:
        async with sessionmaker() as session:
            try:
                obj = await session.get_one(table, obj_id)
                await session.delete(obj)
                await session.commit()
            except NoResultFound:
                pass
