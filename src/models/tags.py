from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


artist_profile_tags_association = Table(
    'artist_profile_tags_association',
    Base.metadata,
    Column("artist_id", ForeignKey('artist_profiles.id'), primary_key=True),
    Column("tag_name", ForeignKey('tags.name'), primary_key=True),
)


producer_profile_tags_association = Table(
    'producer_profile_tags_association',
    Base.metadata,
    Column("producer_id", ForeignKey('producer_profiles.id'), primary_key=True),
    Column("tag_names", ForeignKey('tags.name'), primary_key=True),
)


class Tag(Base):
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(nullable=False)
