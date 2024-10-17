
from sqlalchemy import Column, Table, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


album_to_track_association = Table(
    "album_to_track_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("track_id", ForeignKey("tracks.id"), primary_key=True)
)

album_to_artist_association = Table(
    "album_to_artist_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("artist_id", ForeignKey("artist_profiles.id"), primary_key=True)
)

album_to_tag_association = Table(
    "album_to_tag_association",
    Base.metadata,
    Column("album_id", ForeignKey("albums.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)


class Album(Base):
    __tablename__ = "albums"

    name: Mapped[str] = mapped_column(String, nullable=False)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
