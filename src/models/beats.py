from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

tag_to_beat_association = Table(
    "tag_to_beat_association",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)

producer_to_beat_association = Table(
    "producer_to_beat_association",
    Base.metadata,
    Column("producer_id", ForeignKey("producer_profiles.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)


class Beat(Base):
    __tablename__ = "beats"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
