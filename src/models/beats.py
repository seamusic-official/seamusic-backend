from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base
from src.models.views import user_to_beats_views_association

tag_to_beat_association = Table(
    "tag_to_beat_association",
    Base.metadata,
    Column("tag_name", ForeignKey("tags.name"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)

producer_to_beat_association = Table(
    "producer_to_beat_association",
    Base.metadata,
    Column("producer_id", ForeignKey("producer_profiles.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)

user_to_beats_likes = Table(
    "user_to_beatpacks_likes",
    Base.metadata,
    Column("beat_id", ForeignKey("beats.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)


class Beat(Base):
    __tablename__ = "beats"

    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    file_url: Mapped[str]

    views: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_beats_views_association
    )
    liked_users: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_beats_likes
    )
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beat_association,
        back_populates="beats"
    )
    tags: Mapped[list["Tag"]] = relationship(secondary=tag_to_beat_association)  # type: ignore[name-defined]  # noqa: F821
