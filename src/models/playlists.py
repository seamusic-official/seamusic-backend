from datetime import date

from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.models.auth import user_to_playlists_association
from src.models.base import Base


class Playlists(Base):
    __tablename__ = 'playlists'

    author: Mapped['User'] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument='User',
        secondary=user_to_playlists_association,
    )
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    beats: Mapped[list['Beat']] = relationship(argument='Beat')  # type: ignore[name-defined]  # noqa: F821
    tracks: Mapped[list['Track']] = relationship(argument='Track')  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list['Tag']] = relationship(argument='Track')  # type: ignore[name-defined]  # noqa: F821
    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date] = mapped_column(nullable=False)
