from dataclasses import dataclass
from datetime import datetime

from src.dtos.database.auth import User
from src.dtos.database.licenses import (
    LicensesResponseDTO,
    CreateLicenseRequestDTO,
    UpdateLicenseRequestDTO,
    LicenseResponseDTO
)
from src.exceptions.api import NoRightsException
from src.exceptions.services import NotFoundException
from src.repositories import Repositories, DatabaseRepositories, BaseMediaRepository
from src.repositories.database.auth.base import BaseUsersRepository
from src.repositories.database.auth.postgres import init_users_postgres_repository
from src.repositories.database.licenses.base import BaseLicensesRepository
from src.repositories.database.licenses.postgres import init_postgres_repository as init_licenses_postgres_repository
from src.repositories.media.s3 import init_s3_repository


@dataclass
class LicensesDatabaseRepositories(DatabaseRepositories):
    licenses: BaseLicensesRepository
    users: BaseUsersRepository


@dataclass
class LicensesRepositories(Repositories):
    database: LicensesDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class LicensesService:
    repositories: LicensesRepositories

    async def get_user_licenses(self, user_id: int) -> LicensesResponseDTO:
        return await self.repositories.database.licenses.get_user_licenses(user_id=user_id)

    async def get_all_licenses(self) -> LicensesResponseDTO:
        return await self.repositories.database.licenses.get_all_licenses()

    async def get_one(self, license_id: int) -> LicenseResponseDTO:
        license_: LicenseResponseDTO | None = await self.repositories.database.licenses.get_license_by_id(license_id=license_id)

        if not license_:
            raise NotFoundException

        return license_

    async def add_license(
        self,
        title: str,
        price: str,
        user_id: int,
        description: str | None = None,
    ) -> int:

        user = await self.repositories.database.users.get_user_by_id(user_id=user_id)

        if not user:
            raise NotFoundException("User not found")

        license_ = CreateLicenseRequestDTO(
            title=title,
            description=description,
            price=price,
            user_id=user_id,
            user=User(**user.model_dump()),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        return await self.repositories.database.licenses.add_license(license_=license_)

    async def update_license(
        self,
        license_id: int,
        user_id: int,
        title: str | None = None,
        description: str | None = None,
        price: str | None = None,
    ) -> int:

        license_ = await self.repositories.database.licenses.get_license_by_id(license_id=license_id)

        if not license_:
            raise NotFoundException("license not found")

        if license_.user_id != user_id:
            raise NoRightsException()

        updated_license = UpdateLicenseRequestDTO(
            title=title,
            description=description,
            price=price
        )

        return await self.repositories.database.licenses.update_license(license_=updated_license)

    async def delete_license(self, license_id: int, user_id: int) -> None:

        license_ = await self.repositories.database.licenses.get_license_by_id(license_id=license_id)

        if not license_:
            raise NotFoundException("license not found")

        if license_.user.id != user_id:
            raise NoRightsException()

        await self.repositories.database.licenses.delete_license(license_id=license_id, user_id=user_id)


def get_licenses_service() -> LicensesService:
    return LicensesService(repositories=LicensesRepositories(
        database=LicensesDatabaseRepositories(
            licenses=init_licenses_postgres_repository(),
            users=init_users_postgres_repository(),
        ),
        media=init_s3_repository()
    ))
