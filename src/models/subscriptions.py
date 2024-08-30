from __future__ import annotations

from sqlalchemy import BigInteger, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class OnlyTelegramSubscribeMonth(Base):
    __tablename__ = "only_telegram_subscribe_month"

    subscribe: Mapped[bool] = mapped_column(nullable=False, default=False)

    telegram_account_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("telegram_accounts.id")
    )
    telegram_account: Mapped["TelegramAccount"] = relationship(  # type: ignore[name-defined]
        "TelegramAccount", back_populates="only_telegram_subscribe_month"
    )


class OnlyTelegramSubscribeYear(Base):
    __tablename__ = "only_telegram_subscribe_year"

    subscribe: Mapped[bool] = mapped_column(nullable=False, default=False)

    telegram_account_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("telegram_accounts.id")
    )
    telegram_account: Mapped["TelegramAccount"] = relationship(  # type: ignore[name-defined]
        "TelegramAccount", back_populates="only_telegram_subscribe_year"
    )


class TelegramAccount(Base):
    __tablename__ = "telegram_accounts"

    telegram_id: Mapped[int] = mapped_column(nullable=False, type_=BigInteger)
    subscribe: Mapped[bool] = mapped_column(nullable=False, default=False)
    only_telegram_subscribe_year: Mapped["OnlyTelegramSubscribeYear"] = relationship(  # type: ignore[name-defined]
        back_populates="telegram_account"
    )
    only_telegram_subscribe_month: Mapped["OnlyTelegramSubscribeMonth"] = relationship(  # type: ignore[name-defined]
        back_populates="telegram_account"
    )
