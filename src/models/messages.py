from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

user_to_message_association = Table(
    "user_to_message_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("message_id", Integer, ForeignKey("messages.id"), primary_key=True)
)


class Message(Base):
    __tablename__ = "messages"

    text: Mapped[str]
    author: Mapped["User"] = relationship("User", back_populates="messages")   # type: ignore[name-defined]  # noqa: F821
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
