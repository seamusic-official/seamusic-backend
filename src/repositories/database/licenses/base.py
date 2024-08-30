from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.licenses import (
    LicensesResponseDTO,
    LicenseResponseDTO,
    CreateLicenseRequestDTO,
    UpdateLicenseRequestDTO
)


@dataclass
class BaseLicensesRepository(ABC):
    @abstractmethod
    async def get_user_licenses(self, user_id: int) -> LicensesResponseDTO:
        ...

    @abstractmethod
    async def get_all_licenses(self) -> LicensesResponseDTO:
        ...

    @abstractmethod
    async def get_license_by_id(self, license_id: int) -> LicenseResponseDTO | None:
        ...

    @abstractmethod
    async def add_license(self, license_: CreateLicenseRequestDTO) -> int:
        ...

    @abstractmethod
    async def update_license(self, license_: UpdateLicenseRequestDTO) -> int:
        ...

    @abstractmethod
    async def delete_license(self, license_id: int, user_id: int) -> None:
        ...
