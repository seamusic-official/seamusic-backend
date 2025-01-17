from datetime import date, datetime

from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.app.auth.producers.models import producer_to_soundkits_association
from src.infrastructure.postgres import Base, Sequence

tag_to_soundkits_association = Table(
    "tag_to_soundkits_association",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id"), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True)
)

beat_to_soundkits_association = Table(
    "beat_to_soundkits_association",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id"), primary_key=True),
    Column("beat_id", ForeignKey('beats.id'), primary_key=True)

)


class Soundkit(Base):
    __tablename__ = "soundkits"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    picture_url: Mapped[str | None]
    file_url: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    viewers_ids: Sequence[int]
    likers_ids: Sequence[int]
    producers: Mapped[list["ProducerProfile"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_soundkits_association,
        back_populates="soundkits"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=beat_to_soundkits_association)  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=tag_to_soundkits_association)  # type: ignore[name-defined]  # noqa: F821
