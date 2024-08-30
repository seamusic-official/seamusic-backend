from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base

user_to_licenses_association = Table(
    "user_to_licenses_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("license_id", Integer, ForeignKey("licenses.id")),
)


class License(Base):
    __tablename__ = "licenses"

    title: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", secondary=user_to_licenses_association)  # type: ignore[name-defined]
