from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import ProducerProfile, Beat
from src.models.auth import producer_to_soundkits_association
from src.models.base import Base
from src.models.tags import Tag

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
    description: Mapped[str] = mapped_column(nullable=True)
    producers: Mapped[list["ProducerProfile"]] = relationship(
        secondary=producer_to_soundkits_association,
        back_populates="soundkits"
    )
    beat: Mapped[list["Beat"]] = relationship(secondary=beat_to_soundkits_association)
    tags: Mapped[list["Tag"]] = relationship(secondary=tag_to_soundkits_association)
    title: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
