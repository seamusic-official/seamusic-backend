import os
from dataclasses import dataclass
from io import BytesIO
from types import TracebackType
from typing import Self
from uuid import uuid4

from boto3 import Session as Boto3Session, client as _client

from src.infrastructure.config import settings


@dataclass
class Session:
    session: Boto3Session = Boto3Session(
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key
    )
    client: _client = session.client(service_name='s3', endpoint_url='https://storage.yandexcloud.net')
    bucket_name: str = settings.bucket_name

    async def read(self, path: str, filename: str) -> str:
        return os.path.join('https://storage.yandexcloud.net/', self.bucket_name, path, filename)

    async def write(self, path: str, filename: str, file_stream: BytesIO) -> str:
        key = os.path.join(path, filename)
        self.client.upload_fileobj(file_stream, self.bucket_name, key)
        file_url = os.path.join('https://storage.yandexcloud.net/', self.bucket_name, key)
        return file_url

    async def update(self, path: str, filename: str, file_stream: BytesIO) -> str:
        key = os.path.join(path, filename)
        self.client.upload_fileobj(file_stream, self.bucket_name, key)
        file_url = os.path.join('https://storage.yandexcloud.net/', self.bucket_name, key)
        return file_url

    async def remove(self, path: str, filename: str) -> None:
        key = f'{path}/{filename}'
        self.client.delete_object(Bucket=self.bucket_name, Key=key)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[Exception] | None = None,
        exc_val: Exception | None = None,
        exc_tb: TracebackType | None = None,
    ) -> None:
        pass


def unique_filename(filename: str) -> str:
    file_name, file_extension = os.path.splitext(filename)
    return f'{file_name.replace(' ', '-')}_{uuid4()}{file_extension}'


def get_file_stream(data: bytes) -> BytesIO:
    # await file.read()
    return BytesIO(data)
