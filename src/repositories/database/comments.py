from dataclasses import dataclass

from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class CommentsRepository(SQLAlchemyRepository):
    pass


def init_comments_repository() -> CommentsRepository:
    return CommentsRepository()
