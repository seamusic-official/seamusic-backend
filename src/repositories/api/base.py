from abc import ABC
from dataclasses import dataclass

import aiohttp
import requests


@dataclass
class BaseAPIRepository(ABC):
    pass


@dataclass
class RequestsRepository(BaseAPIRepository):
    @property
    def session(self) -> requests.Session:
        return requests.session()


@dataclass
class AiohttpRepositpry(BaseAPIRepository):
    @property
    async def session(self) -> aiohttp.ClientSession:
        async with aiohttp.ClientSession() as session_:
            return session_
