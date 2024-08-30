from dataclasses import dataclass

from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.comments.base import BaseCommentsRepository


@dataclass
class CommentsRepository(SQLAlchemyRepository, BaseCommentsRepository):
    pass


def init_postgres_repository() -> CommentsRepository:
    return CommentsRepository()
