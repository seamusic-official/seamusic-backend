from datetime import datetime

from src.dtos.database.base import BaseResponseDTO, BaseDTO, BaseRequestDTO
from src.dtos.database.auth import User


class License(BaseDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None
    price: str
    created_at: datetime
    updated_at: datetime


class LicenseResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None
    price: str
    user: User
    created_at: datetime
    updated_at: datetime


class LicensesResponseDTO(BaseResponseDTO):
    licenses: list[License]


class CreateLicenseRequestDTO(BaseRequestDTO):
    title: str
    price: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    user: User
    is_available: bool = True
    created_at: datetime
    updated_at: datetime


class UpdateLicenseRequestDTO(BaseRequestDTO):
    title: str | None = None
    description: str | None = None
    price: str | None = None
