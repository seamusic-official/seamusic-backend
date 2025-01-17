from datetime import datetime, date

from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.app.auth.users.models import user_to_licenses_association
from src.infrastructure.postgres import Base


class License(Base):
    __tablename__ = "licenses"

    id: Mapped[int] = mapped_column(primary_key=True)
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
