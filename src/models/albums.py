from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.tags import album_tags_association

artist_profile_album_association = Table(
    "artist_profile_album_association",
    Base.metadata,
    Column("artist_id", Integer, ForeignKey(
        "artist_profiles.id"), primary_key=True),
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
)

album_track_association = Table(
    "album_track_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)


album_user_association = Table(
    "album_user_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)


class Album(Base):
    __tablename__ = "albums"

    title: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date] = mapped_column(nullable=False)
    tags: Mapped[list["Tag"]] = relationship(
        argument="Tag",
        secondary=album_tags_association
    )  # type: ignore[name-defined]  # noqa: F821
    artist_profiles: Mapped[list["ArtistProfile"]] = relationship(
        argument="ArtistProfile",
        secondary=artist_profile_album_association
    )  # type: ignore[name-defined]  # noqa: F821
