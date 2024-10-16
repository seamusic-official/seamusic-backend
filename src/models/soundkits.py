from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


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

    title: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
