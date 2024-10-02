from dataclasses import dataclass

from sqlalchemy import select, func

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, model_to_response_dto
from src.dtos.database.subscriptions import (
    TelegramAccountResponseDTO,
    TelegramAccountsIDSResponseDTO,
    CreateTelegramAccountRequestDTO
)
from src.models.subscriptions import TelegramAccount
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.telegram_account.base import BaseTelegramAccountRepository


@dataclass
class TelegramAccountRepository(SQLAlchemyRepository, BaseTelegramAccountRepository):
    async def add_one(self, telegram_account: CreateTelegramAccountRequestDTO) -> int:
        telegram_account_ = request_dto_to_model(request_dto=telegram_account, model=TelegramAccount)
        await self.add(telegram_account_)
        return telegram_account_.id

    async def get_telegram_account_by_id(self, telegram_id: int) -> TelegramAccountResponseDTO | None:
        query = select(TelegramAccount).filter_by(telegram_id=telegram_id)
        return model_to_response_dto(model=await self.scalar(query), response_dto=TelegramAccountResponseDTO)

    async def get_telegram_accounts_ids(self, offset: int = 0, limit: int = 10) -> TelegramAccountsIDSResponseDTO:
        query = select(TelegramAccount.telegram_id).offset(offset).limit(limit).order_by(TelegramAccount.updated_at.desc())
        ids = list(await self.scalars(query))
        return TelegramAccountsIDSResponseDTO(ids=ids)

    async def get_telegram_accounts_ids_count(self) -> int:
        query = select(func.count(TelegramAccount.id))
        return await self.scalar(query)


def init_postgres_repository() -> TelegramAccountRepository:
    return TelegramAccountRepository()
