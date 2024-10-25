from datetime import datetime, date

from pydantic import EmailStr

from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO
from src.enums.auth import AccessLevel, PremiumLevel


class UserResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str | None = None
    access_level: AccessLevel = AccessLevel.user
    telegram_id: int | None = None
    premium_level: PremiumLevel = PremiumLevel.none

    is_active: bool
    is_adult: bool
    is_verified: bool

    created_at: date
    updated_at: datetime

    comments: list["CommentDTO"] = list()
    messages: list["MessageDTO"] = list()
    licenses: list["LicenseDTO"] = list()
    followed_artists: list["ArtistDTO"] = list()
    saved_playlists: list["PlaylistDTO"] = list()
    followed_producers: list["ProducerDTO"] = list()
    followed_albums: list["AlbumDTO"] = list()
    followed_tags: list[str] = list()


class UserItemResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str | None = None
    access_level: AccessLevel = AccessLevel.user
    telegram_id: int | None = None
    premium_level: PremiumLevel = PremiumLevel.none

    is_active: bool
    is_adult: bool
    is_verified: bool

    created_at: date
    updated_at: datetime


class UsersResponseDTO(BaseResponseDTO):
    users: list[UserItemResponseDTO]


class CreateUserRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    email: EmailStr
    password: str
    picture_url: str | None = None
    access_level: AccessLevel = AccessLevel.user
    telegram_id: int | None = None
    premium_level: PremiumLevel = PremiumLevel.none

    is_active: bool
    is_adult: bool
    is_verified: bool


class UpdateUserRequestDTO(BaseRequestDTO):
    id: int
    username: str | None = None
    description: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    picture_url: str | None = None
    access_level: AccessLevel | None = None
    telegram_id: int | None = None
    premium_level: PremiumLevel | None = None

    is_active: bool | None = None
    is_adult: bool | None = None
    is_verified: bool | None = None

    created_at: date | None = None
    updated_at: datetime | None = None

    comments: list["CommentDTO"] | None = None
    messages: list["MessageDTO"] | None = None
    licenses: list["LicenseDTO"] | None = None
    followed_artists: list["ArtistDTO"] | None = None
    saved_playlists: list["PlaylistDTO"] | None = None
    followed_producers: list["ProducerDTO"] | None = None
    followed_albums: list["AlbumDTO"] | None = None
    followed_tags: list[str] | None = None


class ArtistResponseDTO(BaseResponseDTO):
    id: int
    username: str
    followers: list["UserDTO"] = list()
    tracks: list["TrackDTO"] = list()
    albums: list["AlbumDTO"] = list()
    tags: list[str] = list()
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class ArtistItemResponseDTO(BaseResponseDTO):
    id: int
    username: str
    user_id: int
    description: str | None = None
    picture_url: str | None = None
    tags: list[str] = list()


class ArtistsResponseDTO(BaseResponseDTO):
    artists: list[ArtistItemResponseDTO]


class CreateArtistRequestDTO(BaseRequestDTO):
    username: str
    followers: list["UserDTO"]
    tracks: list["TrackDTO"]
    albums: list["AlbumDTO"]
    tags: list[str]
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class UpdateArtistRequestDTO(BaseRequestDTO):
    id: int
    username: str | None = None
    followers: list["UserDTO"] | None = None
    tracks: list["TrackDTO"] | None = None
    albums: list["AlbumDTO"] | None = None
    tags: list[str] | None = None
    user_id: int | None = None
    description: str | None = None
    picture_url: str | None = None


class ProducerResponseDTO(BaseResponseDTO):
    id: int
    followers: list["UserDTO"]
    beats: list["BeatDTO"]
    sqauds: list["SquadDTO"]
    tags: list[str]
    beatpacks: list["BeatpackDTO"]
    soundkits: list["SoundkitDTO"]
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class ProducerItemResponseDTO(BaseResponseDTO):
    id: int
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class ProducersResponseDTO(BaseResponseDTO):
    producers: list[ProducerResponseDTO]


class CreateProducerRequestDTO(BaseRequestDTO):
    followers: list["UserDTO"] = list()
    beats: list["BeatDTO"] = list()
    sqauds: list["SquadDTO"] = list()
    tags: list[str] = list()
    beatpacks: list["BeatpackDTO"] = list()
    soundkits: list["SoundkitDTO"] = list()
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class UpdateProducerRequestDTO(BaseRequestDTO):
    id: int
    followers: list["UserDTO"] | None = None
    beats: list["BeatDTO"] | None = None
    sqauds: list["SquadDTO"] | None = None
    tags: list[str] | None = None
    beatpacks: list["BeatpackDTO"] | None = None
    soundkits: list["SoundkitDTO"] | None = None
    user_id: int | None = None
    description: str | None = None
    picture_url: str | None = None


class UserDTO:
    id: int
    username: str
    description: str | None
    email: EmailStr
    password: str
    picture_url: str | None
    access_level: AccessLevel
    telegram_id: int | None
    premium_level: PremiumLevel

    is_active: bool
    is_adult: bool
    is_verified: bool

    created_at: date
    updated_at: datetime

    followed_tags: list[str]


class ArtistDTO(BaseDTO):
    id: int
    user_id: int
    description: str | None = None
    picture_url: str | None = None
    tags: list[str]
