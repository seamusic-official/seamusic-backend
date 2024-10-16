from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base


track_to_tag_association = Table(
    'track_to_tag_association',
    Base.metadata,
    Column("track_id", ForeignKey('tracks.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
)

track_to_producer_association = Table(
    'track_to_producer_association',
    Base.metadata,
    Column("producer_id", ForeignKey('producer_profiles.id'), primary_key=True),
    Column("track_id", ForeignKey('tracks.id'), primary_key=True),
)


class Track(Base):
    __tablename__ = "tracks"
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
