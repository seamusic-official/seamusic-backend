from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ProducerProfile, Beat
from src.models.auth import producer_to_beatpacks_association_table
from src.models.base import Base
from src.models.tags import Tag

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
    producers: Mapped[list["ProducerProfile"]] = relationship(
        secondary=producer_to_beatpacks_association_table,
        back_populates="producers"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=beatpack_to_beat_association_table)
    tags: Mapped[list["Tag"]] = relationship(secondary=beatpack_to_tag_association)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
