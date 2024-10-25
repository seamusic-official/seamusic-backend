from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class AddTagRequestDTO(BaseRequestDTO):
    name: str


class TagResponseDTO(BaseResponseDTO):
    name: str


class TagsResponseDTO(BaseResponseDTO):
    tags: list[str]


class AddTagsRequestDTO(BaseRequestDTO):
    tags: list[str]


class UpdateTagRequestDTO(BaseRequestDTO):
    name: str


class Tag(BaseDTO):
    name: str
