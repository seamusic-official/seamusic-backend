from datetime import date

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.models.base import Base

playlists_to_beat_association = Table(
    "playlists_to_beat_association",
    Base.metadata,
    Column("playlists_id", ForeignKey("playlists.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)

playlists_to_track_association = Table(
    "playlists_to_track_association",
    Base.metadata,
    Column("playlists_id", ForeignKey("playlists.id"), primary_key=True),
    Column("track_id", ForeignKey("tracks.id"), primary_key=True)
)

playlists_to_tag_association = Table(
    "playlists_to_tag_association",
    Base.metadata,
    Column("playlists_id", ForeignKey("playlists.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)


class Playlists(Base):
    __tablename__ = 'playlists'

    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    beats: Mapped[list['Beat']] = relationship(secondary=playlists_to_beat_association)  # type: ignore[name-defined]  # noqa: F821
    tracks: Mapped[list['Track']] = relationship(secondary=playlists_to_track_association)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list['Tag']] = relationship(secondary=playlists_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date] = mapped_column(nullable=False)
