from sqlalchemy import ForeignKey, Integer, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


user_to_comments_association = Table(
    "user_to_comments_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("comment_id", Integer, ForeignKey("comments.id"), primary_key=True)
)


class Comment(Base):
    __tablename__ = "comments"

    text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))  # этот столбец нужен для o2o связи
    author: Mapped["User"] = relationship("User", back_populates="comments")    # type: ignore[name-defined]  # noqa: F821
