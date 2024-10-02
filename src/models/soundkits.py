
from sqlalchemy import Column, Table, ForeignKey, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import User
from src.models.base import Base



user_to_soundkits_association_table = Table(
    "user_to_soundkits_association_table",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
)


class Soundkit(Base):
    __tablename__ = "soundkits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    file_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)
