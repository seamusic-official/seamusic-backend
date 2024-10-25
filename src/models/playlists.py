from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship

from src.models.auth import user_to_playlists_association
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
    Column("tag_name", ForeignKey("tags.name"), primary_key=True)
)

user_to_playlists_likes = Table(
    "user_to_playlists_likes",
    Base.metadata,
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)


class Playlist(Base):
    __tablename__ = 'playlists'

    views: Mapped[int]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    liked_users: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_playlists_likes
    )
    author: Mapped[list["User"]] = relationship(secondary=user_to_playlists_association)   # type: ignore[name-defined]  # noqa: F821
    beats: Mapped[list["Beat"]] = relationship(secondary=playlists_to_beat_association)   # type: ignore[name-defined]  # noqa: F821
    tracks: Mapped[list["Track"]] = relationship(secondary=playlists_to_track_association)   # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=playlists_to_tag_association)   # type: ignore[name-defined]  # noqa: F821
