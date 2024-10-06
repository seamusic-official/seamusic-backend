from datetime import date

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

producer_profile_beat_association = Table(
    "producer_profile_beat_association",
    Base.metadata,
    Column("producer_profile_id", ForeignKey(
        "producer_profiles.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True),
)


playlist_beat_association = Table(
    "playlist_beat_association",
    Base.metadata,
    Column("playlist_id", ForeignKey(
        "playlists.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True),
)


class Beat(Base):
    __tablename__ = "beats"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)
