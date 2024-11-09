from dataclasses import dataclass


@dataclass
class InvalidRequestException(Exception):
    detail: str = "Invalid request"


@dataclass
class NoRightsException(Exception):
    detail: str = "No access rights"


@dataclass
class NotFoundException(Exception):
    detail: str = "Not found"


@dataclass
class ServerError(Exception):
    detail: str = "Internal server error"
