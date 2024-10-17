from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


user_to_message_association = Table(
    "user_to_message_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("message_id", Integer, ForeignKey("messages.id"), primary_key=True)
)


class Message(Base):
    __tablename__ = "messages"

    text: Mapped[str] = mapped_column(nullable=False)
