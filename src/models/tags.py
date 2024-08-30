from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


producer_tags_association = Table(
    "producer_tags_association",
    Base.metadata,
    Column("producer_profile_id", Integer, ForeignKey("producer_profiles.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)

artist_tags_association = Table(
    "artist_tags_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)

listener_tags_association = Table(
    "listener_tags_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class Tag(Base):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(nullable=False)
    artist_profiles: Mapped[list["ArtistProfile"]] = relationship(  # type: ignore[name-defined]
        secondary=artist_tags_association, back_populates="tags"
    )
    producer_profiles: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]
        secondary=producer_tags_association, back_populates="tags"
    )
    listener_profiles: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]
        secondary=listener_tags_association, back_populates="tags"
    )
