from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

artist_profile_track_association = Table(
    "artist_profile_track_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)


class Track(Base):
    __tablename__ = "tracks"
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    album: Mapped["Album"] = relationship(back_populates="tracks")  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(argument="Tag")  # type: ignore[name-defined]  # noqa: F821
