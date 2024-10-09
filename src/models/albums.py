from datetime import date

from sqlalchemy import Column, Table, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


artist_to_album_association = Table(
    "artist_to_album_association",
    Base.metadata,
    Column("artist_id", ForeignKey("artist_profiles.id"), primary_key=True),
    Column("album_id", ForeignKey("albums.id"), primary_key=True)
)

album_to_track_association = Table(
    "album_to_track_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("track_id", ForeignKey("tracks.id"), primary_key=True)
)

album_to_tag_association = Table(
    "album_to_tag_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

album_to_artist_association = Table(
    "album_to_artist_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("artist_id", ForeignKey("artist_profiles.id"), primary_key=True),
)


class Album(Base):
    __tablename__ = "albums"

    title: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date] = mapped_column(nullable=False)
    tags: Mapped[list["Tag"]] = relationship(secondary=album_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
    artist_profiles: Mapped[list["ArtistProfile"]] = relationship(secondary=album_to_artist_association)  # type: ignore[name-defined]  # noqa: F821
