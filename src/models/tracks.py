from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ProducerProfile
from src.models.base import Base
from src.models.tags import Tag

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
    producers: Mapped[list["ProducerProfile"]] = relationship(secondary=track_to_producer_association)
    tags: Mapped[list["Tag"]] = relationship(secondary=track_to_tag_association)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
