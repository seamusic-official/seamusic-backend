from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

user_to_beatpacks_association_table = Table(
    "user_to_beatpacks_association_table",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("beatpack_id", Integer, ForeignKey("beatpacks.id")),
)


beats_to_beatpacks_association_table = Table(
    "beats_to_beatpacks_association_table",
    Base.metadata,
    Column("beat_id", Integer, ForeignKey("beats.id")),
    Column("beatpack_id", Integer, ForeignKey("beatpacks.id")),
)


producer_profile_beatpack_association = Table(
    "producer_profile_beatpack_association",
    Base.metadata,
    Column("producer_profile_id", Integer, ForeignKey(
        "producer_profiles.id"), primary_key=True),
    Column("beatpack_id", Integer, ForeignKey(
        "beatpacks.id"), primary_key=True),
)


class Beatpack(Base):
    __tablename__ = "beatpacks"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    users: Mapped[list["User"]] = relationship("User", secondary=user_to_beatpacks_association_table)  # type: ignore[name-defined]  # noqa: F821
    beats: Mapped[list["Beat"]] = relationship("Beat", secondary=beats_to_beatpacks_association_table)  # type: ignore[name-defined]  # noqa: F821
    created_at: Mapped[date] = mapped_column(nullable=False)
