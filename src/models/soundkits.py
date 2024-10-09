from datetime import date

from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

user_to_soundkits_association_table = Table(
    "user_to_soundkits_association_table",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)

producer_to_soundkits_association_table = Table(
    "producer_to_soundkits_association_table",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
)


class Soundkit(Base):
    __tablename__ = "soundkits"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)
