from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ProducerProfile
from src.models.base import Base
from src.models.tags import Tag

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
    producers: Mapped[list["ProducerProfile"]] = relationship(
        secondary=producer_to_beat_association,
        back_populates="beats"
    )
    tags: Mapped[list["Tag"]] = relationship(secondary=tag_to_beat_association)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
