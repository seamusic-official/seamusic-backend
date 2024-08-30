from src.core.database import Base
from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO


def model_to_response_dto(response_dto: type[BaseResponseDTO], model: Base | None = None):  # type: ignore[no-untyped-def, no-any-return]
    return response_dto(**model.__dict__) if model else None


def models_to_dto(models: list[Base], dto: type[BaseDTO]) -> list:
    return list(map(lambda model: dto(**model.__dict__), models))


def request_dto_to_model(request_dto: BaseRequestDTO, model: type[Base]):  # type: ignore[no-untyped-def, no-any-return]
    request_dto_dict = {key: item if item is not None else None for key, item in request_dto.model_dump()}  # type: ignore
    return model(**request_dto_dict)
