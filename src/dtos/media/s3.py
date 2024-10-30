from io import BytesIO

from src.dtos.media.base import BaseRequestDTO, BaseResponseDTO


class UploadFileRequestDTO(BaseRequestDTO):
    path: str
    filename: str
    file_stream: BytesIO


class UploadFileResponseDTO(BaseResponseDTO):
    url: str


class DeleteFileRequestDTO(BaseRequestDTO):
    path: str
    filename: str
