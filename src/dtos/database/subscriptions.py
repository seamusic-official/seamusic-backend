from src.dtos.database.base import BaseResponseDTO, BaseDTO, BaseRequestDTO


class TelegramAccount(BaseDTO):
    telegram_id: int | None = None
    subscribe: int | None = None


class OnlyTelegramSubscribeMonth(BaseDTO):
    subscribe: bool | None = None
    telegram_account_id: int
    telegram_account: TelegramAccount


class OnlyTelegramSubscribeYear(BaseDTO):
    subscribe: bool | None = None
    telegram_account_id: int | None = None
    telegram_account: TelegramAccount


class OnlyTelegramSubscribeMonthResponseDTO(BaseResponseDTO):
    subscribe: bool | None = None
    telegram_account_id: int
    telegram_account: TelegramAccount


class OnlyTelegramSubscribeYearResponseDTO(BaseResponseDTO):
    subscribe: bool | None = None
    telegram_account_id: int | None = None
    telegram_account: TelegramAccount


class TelegramAccountResponseDTO(BaseResponseDTO):
    telegram_id: int
    subscribe: bool | None = None
    only_telegram_subscribe_year: OnlyTelegramSubscribeYear | None = None
    only_telegram_subscribe_month: OnlyTelegramSubscribeMonth | None = None


class TelegramAccountsIDSResponseDTO(BaseResponseDTO):
    ids: list[int]


class CreateTelegramAccountRequestDTO(BaseRequestDTO):
    id: int
