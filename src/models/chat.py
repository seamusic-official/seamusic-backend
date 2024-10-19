from sqlalchemy import Integer, Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base

user_to_chat_association = Table(
    "user_to_chat_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("chat_id", Integer, ForeignKey("chat.id"), primary_key=True)
)


class Chat(Base):
    __tablename__ = "chat"

    text: Mapped[str]
    author: Mapped[list["User"]] = relationship(secondary=user_to_chat_association)  # type: ignore[name-defined]  # noqa: F821
