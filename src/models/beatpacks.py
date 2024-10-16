from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


beatpacks_to_producer_association_table = Table(
    "user_to_beatpacks_association_table",
    Base.metadata,
    Column("producer_id", ForeignKey("producer_profiles.id")),
    Column("beatpack_id", ForeignKey("beatpacks.id"))
)

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

    name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
