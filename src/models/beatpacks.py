
from sqlalchemy import Integer, String, Table, ForeignKey, Column, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import User
from src.models.base import Base
from src.models.beats import Beat

beats_to_beatpacks_association_table = Table(
    "beats_to_beatpacks_association_table",
    Base.metadata,
    Column("beat_id", Integer, ForeignKey("beats.id")),
    Column("beatpack_id", Integer, ForeignKey("beatpacks.id")),
)


class Beatpack(Base):
    __tablename__ = "beatpacks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    users: Mapped[list["User"]] = relationship("User", secondary=user_to_beatpacks_association_table)  # type: ignore[name-defined]
    beats: Mapped[list["Beat"]] = relationship("Beat", secondary=beats_to_beatpacks_association_table)  # type: ignore[name-defined]
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)
