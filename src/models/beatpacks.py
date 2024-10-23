from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship

from src.models.auth import producer_to_beatpacks_association
from src.models.base import Base
from src.models.views import user_to_beatpacks_views_association

beatpack_to_beat_association_table = Table(
    "beatpack_to_beat_association_table",
    Base.metadata,
    Column("beat_id", ForeignKey("beats.id")),
    Column("beatpack_id", ForeignKey("beatpacks.id"))
)

beatpack_to_tag_association = Table(
    'beatpack_to_tag_association',
    Base.metadata,
    Column("beatpack_id", ForeignKey('beatpacks.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
)

user_to_beatpacks_likes = Table(
    "user_to_beatpacks_likes",
    Base.metadata,
    Column("beatpacks_id", ForeignKey("beatpacks.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    extend_existing=True
)


class Beatpack(Base):
    __tablename__ = "beatpacks"

    title: Mapped[str]
    description: Mapped[str | None]
    views: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_beatpacks_views_association
    )
    liked_users: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_beatpacks_likes
    )
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beatpacks_association,
        back_populates="producers"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=beatpack_to_beat_association_table)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=beatpack_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
