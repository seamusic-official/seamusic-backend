from sqlalchemy.orm import Mapped, relationship

from src.models.auth import user_to_licenses_association
from src.models.base import Base


class License(Base):
    __tablename__ = "licenses"

    title: Mapped[str]
    text: Mapped[str]
    description: Mapped[str]
    author: Mapped["User"] = relationship(  # type: ignore[name-defined]  # noqa: F821
        argument="User",
        secondary=user_to_licenses_association,
        back_populates="licenses"
    )
