from sqlalchemy import Column, ForeignKey, Integer, Table, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.albums import album_track_association
from src.models.base import Base
from .albums import Album
from .tags import Tag

artist_profile_track_association = Table(
    "artist_profile_track_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id")),
    Column("track_id", Integer, ForeignKey("tracks.id")),
)


class Track(Base):
    __tablename__ = "tracks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    picture_url: Mapped[str] = mapped_column(String, nullable=True)
    file_url: Mapped[str] = mapped_column(String, nullable=False)
    album: Mapped["Album"] = relationship(
        back_populates="tracks"
    )
    tags: Mapped["Tag"] = relationship(
        back_populates="tags"
    )