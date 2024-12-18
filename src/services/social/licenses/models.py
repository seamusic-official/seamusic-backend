from datetime import datetime, date

from sqlalchemy.orm import Mapped, relationship

from src.infrastructure.postgres.orm import Base
from src.services.auth.users.models import user_to_licenses_association


class License(Base):
    __tablename__ = "licenses"

    title: Mapped[str]
    text: Mapped[str]
    description: Mapped[str]

    created_at: Mapped[date]
    updated_at: Mapped[datetime]

    author: Mapped["User"] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_licenses_association,
        back_populates="licenses"
    )
