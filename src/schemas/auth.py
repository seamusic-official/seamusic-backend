from datetime import date, datetime

from pydantic import BaseModel, EmailStr, Field

from src.enums.auth import Role
from src.schemas.base import DetailMixin


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str | None = None
    picture_url: str
    birthday: datetime


class SUserResponse(BaseModel):
    id: int
    username: str
    email: str
    picture_url: str
    birthday: datetime


class SMeResponse(BaseModel):
    id: int
    username: str
    email: str
    picture_url: str
    birthday: datetime


class SUsersResponse(BaseModel):
    users: list[User]


class SUpdateUserPictureResponse(BaseModel, DetailMixin):
    detail: str = "User picture updated."


class SUpdateUserRequest(BaseModel):
    name: str | None = None
    username: str | None = None
    description: str | None = None


class SUpdateUserResponse(BaseModel):
    id: int


class SDeleteUserResponse(BaseModel, DetailMixin):
    detail: str = "User deleted."


class Artist(BaseModel):
    id: int
    user: User
    description: str | None = None


class SArtistResponse(BaseModel):
    id: int
    user: User
    description: str | None = None


class SMeAsArtistResponse(BaseModel):
    id: int
    user: User
    description: str | None = None


class SArtistsResponse(BaseModel):
    artists: list[Artist]


class SUpdateArtistRequest(BaseModel):
    description: str | None = Field(max_length=255)


class SUpdateArtistResponse(BaseModel):
    id: int


class SDeleteArtistResponse(BaseModel, DetailMixin):
    detail: str = "Artist deleted"


class Producer(BaseModel):
    id: int
    user: User
    description: str | None = None


class SProducerResponse(BaseModel):
    id: int
    user: User
    description: str | None = None


class SMeAsProducerResponse(BaseModel):
    id: int
    user: User
    description: str | None = None


class SProducersResponse(BaseModel):
    producers: list[Producer]


class SUpdateProducerRequest(BaseModel):
    description: str | None = Field(max_length=255)


class SUpdateProducerResponse(BaseModel):
    id: int


class SDeleteProducerResponse(BaseModel, DetailMixin):
    detail: str = "Producer deleted"


class SRegisterUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=25)
    password: str = Field(min_length=5)
    email: EmailStr
    roles: list[Role]
    birthday: date
    tags: list[str] = list()


class SRegisterUserResponse(BaseModel, DetailMixin):
    id: int


class SLoginRequest(BaseModel):
    email: EmailStr
    password: str


class SLoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: User


class SRefreshTokenResponse(BaseModel):
    accessToken: str
    refreshToken: str


class SSpotifyCallbackResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: User
