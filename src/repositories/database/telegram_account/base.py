from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.subscriptions import (
    TelegramAccountResponseDTO,
    CreateTelegramAccountRequestDTO, TelegramAccountsIDSResponseDTO
)


@dataclass
class BaseTelegramAccountRepository(ABC):
    @abstractmethod
    async def add_one(self, telegram_account: CreateTelegramAccountRequestDTO) -> int:
        ...

    @abstractmethod
    async def get_telegram_account_by_id(self, telegram_id: int) -> TelegramAccountResponseDTO | None:
        ...

    @abstractmethod
    async def get_telegram_accounts_ids(self) -> TelegramAccountsIDSResponseDTO:
        ...
