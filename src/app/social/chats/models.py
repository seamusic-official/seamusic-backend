from sqlalchemy import Integer, Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.postgres import Base

user_to_chat_association = Table(
    "user_to_chat_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("chat_id", Integer, ForeignKey("chat.id"), primary_key=True)
)

message_to_chat_association = Table(
    "message_to_chat_association",
    Base.metadata,
    Column("message_id", Integer, ForeignKey("messages.id"), primary_key=True),
    Column("chat_id", Integer, ForeignKey("chat.id"), primary_key=True)
)


class Chat(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True)
    messages: Mapped[list["Message"]] = relationship(secondary=message_to_chat_association, back_populates="chat")  # type: ignore[name-defined]  # noqa: F821
    participants: Mapped[list["User"]] = relationship(secondary=user_to_chat_association)  # type: ignore[name-defined]  # noqa: F821
