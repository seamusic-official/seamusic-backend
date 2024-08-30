import os
import uuid
from io import BytesIO

from fastapi import UploadFile

from src.exceptions.services import ServerError, InvalidRequestException


def unique_filename(file: UploadFile | None = None) -> str:

    if not file or not file.filename:
        raise InvalidRequestException()

    try:
        file_name, file_extension = os.path.splitext(file.filename)
        return f'track-{file_name.replace(" ", "-")}_{uuid.uuid4()}{file_extension}'

    except Exception as e:
        raise ServerError(f"Failed to process the audio file: {str(e)}")


async def get_file_stream(file: UploadFile) -> BytesIO:
    file_data = await file.read()
    return BytesIO(file_data)
