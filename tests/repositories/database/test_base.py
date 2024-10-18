# from typing import Iterable, Any
#
# from sqlalchemy.sql import Executable
#
# from src.models.base import Base
# from src.repositories.database.base import SQLAlchemyRepository
#
#
# class TestSQLAlchemyRepository:
#     repository = SQLAlchemyRepository()
#
#     async def test_add(self, obj: Base) -> None:
#         await self.repository.add(obj=obj)
#
#     async def test_merge(self, obj: Base) -> None:
#         await self.repository.merge(obj=obj)
#
#     async def test_execute(self, statement: Executable) -> None:
#         await self.repository.execute(statement=statement)
#
#     async def test_get(self, table: type[Base], primary_key: Any) -> None:
#         response = await self.repository.get(table=table, primary_key=primary_key)
#         assert isinstance(response, Base | None)
#
#     async def test_scalar(self, statement: Executable) -> None:
#         await self.repository.scalar(statement=statement)
#
#     async def test_scalars(self, statement: Executable) -> None:
#         response = await self.repository.scalars(statement=statement)
#         assert isinstance(response, Iterable)
