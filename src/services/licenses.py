from dataclasses import dataclass
from datetime import datetime

from src.dtos.database.auth import UserDTO
from src.dtos.database.licenses import (
    LicensesResponseDTO,
    CreateLicenseRequestDTO,
    UpdateLicenseRequestDTO,
    LicenseResponseDTO
)
from src.exceptions import NotFoundException, NoRightsException
from src.repositories import Repositories, DatabaseRepositories, BaseMediaRepository
from src.repositories.database.auth import init_users_repository, UsersRepository
from src.repositories.database.licenses import (
    init_licenses_repository as init_licenses_postgres_repository,
    LicensesRepository,
)
from src.repositories.media.s3 import init_s3_repository


@dataclass
class LicensesDatabaseRepositories(DatabaseRepositories):
    licenses: LicensesRepository
    users: UsersRepository


@dataclass
class LicensesRepositories(Repositories):
    database: LicensesDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class LicensesService:
    repositories: LicensesRepositories

    async def get_user_licenses(self, user_id: int, start: int = 1, size: int = 10) -> LicensesResponseDTO:
        return await self.repositories.database.licenses.get_user_licenses(user_id=user_id, offset=start - 1, limit=size)

    async def get_user_licenses_count(self, user_id: int) -> int:
        return await self.repositories.database.licenses.get_user_licenses_count(user_id=user_id)

    async def get_all_licenses(self, start: int = 1, size: int = 10) -> LicensesResponseDTO:
        return await self.repositories.database.licenses.get_all_licenses(offset=start - 1, limit=size)

    async def get_licenses_count(self) -> int:
        return await self.repositories.database.licenses.get_licenses_count()

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
            user=UserDTO(**user.model_dump()),
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


def get_licenses_repositories() -> LicensesRepositories:
    return LicensesRepositories(
        database=LicensesDatabaseRepositories(
            licenses=init_licenses_postgres_repository(),
            users=init_users_repository(),
        ),
        media=init_s3_repository()
    )


def get_licenses_service() -> LicensesService:
    return LicensesService(repositories=get_licenses_repositories())
