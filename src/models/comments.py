from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import user_comments_association
from src.models.base import Base


class BaseComment(Base):
    __tablename__ = "comments"

    text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(
        argument="User",
        secondary=user_comments_association
    )  # type: ignore[name-defined]  # noqa: F821
