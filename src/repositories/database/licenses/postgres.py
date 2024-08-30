from dataclasses import dataclass

from sqlalchemy import select, delete

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, model_to_response_dto, models_to_dto
from src.dtos.database.licenses import (
    License as _License,
    LicensesResponseDTO,
    LicenseResponseDTO,
    CreateLicenseRequestDTO,
    UpdateLicenseRequestDTO
)
from src.models.licenses import License
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.licenses.base import BaseLicensesRepository


@dataclass
class LicensesRepository(SQLAlchemyRepository, BaseLicensesRepository):
    async def get_user_licenses(self, user_id: int) -> LicensesResponseDTO:
        query = select(License).filter_by(user_id=user_id)
        licenses = list(await self.scalars(query))
        return LicensesResponseDTO(licenses=models_to_dto(models=licenses, dto=_License))

    async def get_all_licenses(self) -> LicensesResponseDTO:
        query = select(License)
        licenses = list(await self.scalars(query))
        return LicensesResponseDTO(licenses=models_to_dto(models=licenses, dto=_License))

    async def get_license_by_id(self, license_id: int) -> LicenseResponseDTO | None:
        return model_to_response_dto(
            model=await self.get(License, license_id),
            response_dto=LicenseResponseDTO
        )

    async def add_license(self, license_: CreateLicenseRequestDTO) -> int:
        model = request_dto_to_model(model=License, request_dto=license_)
        await self.add(model)
        return model.id

    async def update_license(self, license_: UpdateLicenseRequestDTO) -> int:
        model = request_dto_to_model(model=License, request_dto=license_)
        await self.merge(model)
        return model.id

    async def delete_license(self, license_id: int, user_id: int) -> None:
        query = delete(License).filter_by(id=license_id, user_id=user_id)
        await self.execute(query)


def init_postgres_repository() -> LicensesRepository:
    return LicensesRepository()
