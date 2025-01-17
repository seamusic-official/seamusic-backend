from datetime import date, datetime

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.infrastructure.postgres import Base, Sequence

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

author_to_playlists_association = Table(
    "user_to_playlists_author_association",
    Base.metadata,
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)


class Playlist(Base):
    __tablename__ = 'playlists'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    viewers_ids: Sequence[int]
    likers_ids: Sequence[int]
    authors: Mapped[list["User"]] = relationship(secondary=author_to_playlists_association)   # type: ignore[name-defined]  # noqa: F821
    beats: Mapped[list["Beat"]] = relationship(secondary=playlists_to_beat_association)   # type: ignore[name-defined]  # noqa: F821
    tracks: Mapped[list["Track"]] = relationship(secondary=playlists_to_track_association)   # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=playlists_to_tag_association)   # type: ignore[name-defined]  # noqa: F821
