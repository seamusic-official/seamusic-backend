from datetime import datetime, date

from sqlalchemy import ForeignKey, Column, Table, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.auth.users.models import user_to_producer_association
from src.app.music.beats.models import producer_to_beat_association
from src.app.music.squads.models import producer_to_squad_association
from src.infrastructure.postgres import Base

producer_to_beatpacks_association = Table(
    "producer_to_beatpacks_association",
    Base.metadata,
    Column("producer_profile_id", ForeignKey("producer_profiles.id")),
    Column("beatpack_id", ForeignKey("beatpacks.id"))
)

producer_to_soundkits_association = Table(
    "producer_to_soundkits_association",
    Base.metadata,
    Column("soundkit_id", Integer, ForeignKey("soundkits.id"), primary_key=True),
    Column("producer_id", Integer, ForeignKey("producer_profiles.id"), primary_key=True),
)

producer_to_tags_association = Table(
    'producer_to_tags_association',
    Base.metadata,
    Column("producer_id", ForeignKey('producer_profiles.id'), primary_key=True),
    Column("tag_id", ForeignKey('tags.id'), primary_key=True),
)


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    description: Mapped[str]
    picture_url: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    followers: Mapped[list["User"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=user_to_producer_association,
        back_populates="followed_producers"
    )
    beats: Mapped[list["Beat"]] = relationship(secondary=producer_to_beat_association, back_populates="producers")  # type: ignore[name-defined]  # noqa: F821
    squads: Mapped[list["Squad"]] = relationship(secondary=producer_to_squad_association, back_populates="producers")  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship(secondary=producer_to_tags_association)  # type: ignore[name-defined]  # noqa: F821
    beatpacks: Mapped[list["Beatpack"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        secondary=producer_to_beatpacks_association,
        back_populates="producers"
    )
    soundkits: Mapped[list["Soundkit"]] = relationship(secondary=producer_to_soundkits_association, back_populates="producers")  # type: ignore[name-defined]  # noqa: F821
