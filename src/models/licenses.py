from sqlalchemy import Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

user_to_licenses_association = Table(
    "user_to_licenses_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("license_id", Integer, ForeignKey("licenses.id")),
)


class License(Base):
    __tablename__ = "licenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["User"] = relationship("User", secondary=user_to_licenses_association)  # type: ignore[name-defined]  # noqa: F821
