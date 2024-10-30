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

    comments: list["CommentDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    messages: list["MessageDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    licenses: list["LicenseDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    followed_artists: list["ArtistDTO"] = list()
    saved_playlists: list["PlaylistDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    followed_producers: list["ProducerDTO"] = list()
    followed_albums: list["AlbumDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
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

    created_at: date = date.today()
    updated_at: datetime = datetime.now()

    is_active: bool
    is_adult: bool
    is_verified: bool


class CreateUserResponseDTO(BaseResponseDTO):
    id: int


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

    updated_at: datetime = datetime.now()

    comments_ids: list[int] | None = None
    messages_ids: list[int] | None = None
    licenses_ids: list[int] | None = None
    followed_artists_ids: list[int] | None = None
    saved_playlists_ids: list[int] | None = None
    followed_producers_ids: list[int] | None = None
    followed_albums_ids: list[int] | None = None
    followed_tags: list[str] | None = None


class UpdateUserResponseDTO(BaseResponseDTO):
    id: int


class ArtistResponseDTO(BaseResponseDTO):
    id: int
    username: str
    followers: list["UserDTO"] = list()
    tracks: list["TrackDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    albums: list["AlbumDTO"] = list()  # type: ignore[name-defined]  # noqa: F821
    tags: list[str] = list()
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class ArtistItemResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str] = list()


class ArtistsResponseDTO(BaseResponseDTO):
    artists: list[ArtistItemResponseDTO]


class CreateArtistRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class CreateArtistResponseDTO(BaseResponseDTO):
    id: int


class UpdateArtistRequestDTO(BaseRequestDTO):
    id: int
    username: str | None = None
    followers_ids: list[int] | None = None
    tracks_ids: list[int] | None = None
    albums_ids: list[int] | None = None
    tags: list[str] | None = None
    user_id: int | None = None
    description: str | None = None
    picture_url: str | None = None


class UpdateArtistResponseDTO(BaseResponseDTO):
    id: int


class ProducerResponseDTO(BaseResponseDTO):
    id: int
    username: str
    followers: list["UserDTO"]
    beats: list["BeatDTO"]  # type: ignore[name-defined]  # noqa: F821
    sqauds: list["SquadDTO"]  # type: ignore[name-defined]  # noqa: F821
    tags: list[str]
    beatpacks: list["BeatpackDTO"]  # type: ignore[name-defined]  # noqa: F821
    soundkits: list["SoundkitDTO"]  # type: ignore[name-defined]  # noqa: F821
    user_id: int
    description: str | None = None
    picture_url: str | None = None


class ProducerItemResponseDTO(BaseResponseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class ProducersResponseDTO(BaseResponseDTO):
    producers: list[ProducerResponseDTO]


class CreateProducerRequestDTO(BaseRequestDTO):
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class CreateProducerResponseDTO(BaseResponseDTO):
    id: int


class UpdateProducerRequestDTO(BaseRequestDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int | None = None
    followers_ids: list[int] | None = None
    beats_ids: list[int] | None = None
    sqauds_ids: list[int] | None = None
    tags: list[str] | None = None
    beatpacks_ids: list[int] | None = None
    soundkits_ids: list[int] | None = None


class UpdateProducerResponseDTO(BaseResponseDTO):
    id: int


class UserDTO:
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

    followed_tags: list[str]


class ArtistDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]


class ProducerDTO(BaseDTO):
    id: int
    username: str
    description: str | None = None
    picture_url: str | None = None
    user_id: int
    tags: list[str]
