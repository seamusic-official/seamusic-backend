from pydantic import BaseModel


class TelegramAccount(BaseModel):
    telegram_id: int | None = None
    subscribe: int | None = None


class OnlyTelegramSubscribeMonth(BaseModel):
    subscribe: bool | None = None
    telegram_account_id: int
    telegram_account: TelegramAccount


class OnlyTelegramSubscribeYear(BaseModel):
    subscribe: bool | None = None
    telegram_account_id: int | None = None
    telegram_account: TelegramAccount


class STelegramAccountResponse(BaseModel):
    telegram_id: int
    subscribe: bool | None = None
    only_telegram_subscribe_year: OnlyTelegramSubscribeYear | None = None
    only_telegram_subscribe_month: OnlyTelegramSubscribeMonth | None = None


class STelegramAccountsIDResponse(BaseModel):
    ids: list[int]
