from sqlalchemy import Column, ForeignKey, Table
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
    Column("tag_name", ForeignKey('tags.name'), primary_key=True),
)


album_tags_association = Table(
    'album_tags_association',
    Base.metadata,
    Column("album_id", ForeignKey('albums.id'), primary_key=True),
    Column("tag_name", ForeignKey('tags.name'), primary_key=True),
)


track_tags_association = Table(
    'track_tags_association',
    Base.metadata,
    Column("track_id", ForeignKey('tracks.id'), primary_key=True),
    Column("tag_name", ForeignKey('tags.name'), primary_key=True),
)


user_followed_tags_association = Table(
    'user_followed_tags_association',
    Base.metadata,
    Column("user_id", ForeignKey('users.id'), primary_key=True),
    Column("tag_name", ForeignKey('tags.name'), primary_key=True),
)


playlist_tags_association = Table(
    "playlist_tags_association",
    Base.metadata,
    Column("playlist_id", ForeignKey(
        "playlists.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class Tag(Base):
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
