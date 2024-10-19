from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base

tag_to_beat_association = Table(
    "tag_to_beat_association",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)

producer_to_beat_association = Table(
    "producer_to_beat_association",
    Base.metadata,
    Column("producer_id", ForeignKey("producer_profiles.id"), primary_key=True),
    Column("beat_id", ForeignKey("beats.id"), primary_key=True)
)


class Beat(Base):
    __tablename__ = "beats"

    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    file_url: Mapped[str]
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beat_association,
        back_populates="beats"
    )
    tags: Mapped[list["Tag"]] = relationship(secondary=tag_to_beat_association)  # type: ignore[name-defined]  # noqa: F821
