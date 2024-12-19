import os
import uuid
from io import BytesIO

from src.infrastructure.s3.exceptions import ServerError, InvalidRequestException


def unique_filename(filename: str | None = None) -> str:
    if not filename:
        raise InvalidRequestException()

    try:
        file_name, file_extension = os.path.splitext(filename)
        return f'track-{file_name.replace(" ", "-")}_{uuid.uuid4()}{file_extension}'

    except Exception as e:
        raise ServerError(f"Failed to process the file: {str(e)}")


async def get_file_stream(data: bytes) -> BytesIO:
    # await file.read()
    return BytesIO(data)
