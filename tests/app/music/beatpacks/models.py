from datetime import datetime, date

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.app.auth.producers.models import producer_to_beatpacks_association
from src.infrastructure.postgres.orm import Base

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


class Beatpack(Base):
    __tablename__ = "beatpacks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    viewers_ids: Mapped[list[int]]
    likers_ids: Mapped[list[int]]
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beatpacks_association,
        back_populates="beatpacks"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=beatpack_to_beat_association_table)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=beatpack_to_tag_association)  # type: ignore[name-defined]  # noqa: F821
