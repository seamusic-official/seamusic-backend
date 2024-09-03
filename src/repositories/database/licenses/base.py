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
    async def get_user_licenses(self, user_id: int, offset: int = 0, limit: int = 10) -> LicensesResponseDTO:
        ...

    @abstractmethod
    async def get_user_licenses_count(self, user_id: int) -> int:
        ...

    @abstractmethod
    async def get_all_licenses(self, offset: int = 0, limit: int = 10) -> LicensesResponseDTO:
        ...

    @abstractmethod
    async def get_licenses_count(self) -> int:
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
