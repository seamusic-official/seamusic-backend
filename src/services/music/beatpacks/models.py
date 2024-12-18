from datetime import datetime, date

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship

from src.infrastructure.postgres.orm import Base
from src.services.auth.producers.models import producer_to_beatpacks_association
from src.services.social.views.models import user_to_beatpacks_views_association

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

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    viewers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_beatpacks_views_association
    )
    likers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_beatpacks_likes,
        overlaps="likers"
    )
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beatpacks_association,
        back_populates="beatpacks"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=beatpack_to_beat_association_table)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=beatpack_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
