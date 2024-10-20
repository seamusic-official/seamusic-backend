from src.dtos.database.base import BaseResponseDTO, BaseRequestDTO, BaseDTO


class Noftification(BaseDTO):
    title: str
    description: str | None = None


class CreateNoftificationDTO(BaseRequestDTO):
    title: str
    description: str | None = None


class UpdateNoftificationDTO(BaseRequestDTO):
    title: str
    description: str | None = None


class NoftificationResponseDTO(BaseResponseDTO):
    title: str
    description: str | None = None
