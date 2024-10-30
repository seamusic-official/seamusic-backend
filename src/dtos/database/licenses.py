from datetime import date, datetime

from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class LicenseResponseDTO(BaseResponseDTO):
    id: int
    title: str
    text: str
    description: str

    created_at: date
    updated_at: datetime

    author: "UserDTO"  # type: ignore[name-defined]  # noqa: F821


class LicenseItemResponseDTO(BaseResponseDTO):
    id: int
    title: str
    text: str
    description: str

    created_at: date
    updated_at: datetime

    author: "UserDTO"  # type: ignore[name-defined]  # noqa: F821


class LicensesResponseDTO(BaseResponseDTO):
    licenses: list[LicenseItemResponseDTO]


class MyLicensesResponseDTO(BaseResponseDTO):
    licenses: list[LicenseItemResponseDTO]


class CreateLicenseRequestDTO(BaseRequestDTO):
    title: str
    text: str
    description: str
    author_id: int

    created_at: date = date.today()
    updated_at: datetime = datetime.now()


class CreateLicenseResponseDTO(BaseResponseDTO):
    id: int


class UpdateLicenseRequestDTO(BaseRequestDTO):
    id: int
    title: str
    text: str
    description: str
    author_id: int

    updated_at: datetime = datetime.now()


class UpdateLicenseResponseDTO(BaseResponseDTO):
    id: int


class LicenseDTO(BaseDTO):
    id: int
    title: str
    text: str
    description: str

    created_at: date
    updated_at: datetime

    author: "UserDTO"  # type: ignore[name-defined]  # noqa: F821
