from dataclasses import dataclass
from datetime import date, datetime
from io import BytesIO

from pydantic import EmailStr

from src.dtos.database.auth import (
    ArtistResponseDTO,
    ArtistsResponseDTO,
    CreateUserRequestDTO,
    ProducerResponseDTO,
    ProducersResponseDTO,
    UserResponseDTO,
    UsersResponseDTO,
    UpdateArtistRequestDTO,
    UpdateProducerRequestDTO,
    UpdateUserRequestDTO, User, CreateArtistRequestDTO, CreateProducerRequestDTO,
)
from src.dtos.database.tags import AddTagsRequestDTO, Tag
from src.enums.auth import Role, AccessLevel
from src.exceptions.services import NotFoundException, ServerError, NoRightsException
from src.repositories import Repositories, DatabaseRepositories, BaseMediaRepository
from src.repositories.api.spotify.base import BaseSpotifyRepository
from src.repositories.database.auth.base import BaseUsersRepository, BaseProducersRepository, BaseArtistsRepository
from src.repositories.database.auth.postgres import (
    init_users_postgres_repository,
    init_artists_postgres_repository,
    init_producers_postgres_repository, )
from src.repositories.database.tags.base import BaseTagsRepository
from src.repositories.database.tags.postgres import init_postgres_repository as init_tags_postgres_repository
from src.repositories.media.s3 import S3Repository, init_s3_repository
from src.services.base import BaseService
from src.utils.auth import create_access_token, create_refresh_token, get_hashed_password, authenticate_user


@dataclass
class UsersDatabaseRepositories(DatabaseRepositories):
    users: BaseUsersRepository
    tags: BaseTagsRepository
    artists: BaseArtistsRepository
    producers: BaseProducersRepository


@dataclass
class ArtistsDatabaseRepositories(DatabaseRepositories):
    artists: BaseArtistsRepository


@dataclass
class ProducersDatabaseRepositories(DatabaseRepositories):
    producers: BaseProducersRepository


@dataclass
class AuthDatabaseRepositories(DatabaseRepositories):
    users: BaseUsersRepository


@dataclass
class BaseAuthRepositories(Repositories):
    database: UsersDatabaseRepositories | ArtistsDatabaseRepositories | ProducersDatabaseRepositories | AuthDatabaseRepositories
    media: BaseMediaRepository


class UsersRepositories(BaseAuthRepositories):
    database: UsersDatabaseRepositories
    media: S3Repository


class ArtistsRepositories(BaseAuthRepositories):
    database: ArtistsDatabaseRepositories
    media: S3Repository


class ProducersRepositories(BaseAuthRepositories):
    database: ProducersDatabaseRepositories
    media: S3Repository


class AuthRepositories(BaseAuthRepositories):
    database: AuthDatabaseRepositories
    media: S3Repository
    api: BaseSpotifyRepository


@dataclass
class UsersService(BaseService):
    repositories: UsersRepositories

    async def create_new_user(
        self,
        username: str,
        password: str,
        email: EmailStr,
        roles: list[Role],
        birthday: date,
        tags: list[str],
    ) -> int:

        existing_user: UserResponseDTO | None = await self.repositories.database.users.get_user_by_email(email=email)
        if existing_user:
            raise NoRightsException

        superuser = await self.repositories.database.users.get_user_by_id(user_id=1)
        if not superuser:
            access_level = AccessLevel.superuser
        else:
            access_level = AccessLevel.user

        user = CreateUserRequestDTO(
            username=username,
            email=email,
            password=get_hashed_password(password),
            access_level=access_level,
            roles=roles,
            birthday=birthday,
            tags=tags,
        )
        user_id: int = await self.repositories.database.users.create_user(user=user)
        await self.repositories.database.tags.add_tags(tags=AddTagsRequestDTO(tags=list(map(lambda name: Tag(name=name), tags))))

        artist_profile_id: int = await self.repositories.database.artists.create_artist(CreateArtistRequestDTO(
            user_id=user_id,
            description="Hi, I'm an artist",
            is_available=False,
        ))
        await self.repositories.database.users.update_user(UpdateUserRequestDTO(artist_profile_id=artist_profile_id))
        producer_profile_id: int = await self.repositories.database.producers.create_producer(CreateProducerRequestDTO(
            user_id=user_id,
            description="Hi, I'm a producer",
            is_available=False,
        ))
        await self.repositories.database.users.update_user(UpdateUserRequestDTO(producer_profile_id=producer_profile_id))
        return user_id

    async def get_user_by_id(self, user_id: int) -> UserResponseDTO:
        user: UserResponseDTO | None = await self.repositories.database.users.get_user_by_id(user_id=user_id)

        if not user:
            raise NotFoundException()

        return user

    async def get_user_by_email(self, email: EmailStr) -> UserResponseDTO:
        user: UserResponseDTO | None = await self.repositories.database.users.get_user_by_email(email=email)

        if not user:
            raise NotFoundException()

        return user

    async def get_all_users(self) -> UsersResponseDTO:
        return await self.repositories.database.users.get_users()

    async def update_user_picture(
        self,
        file_stream: BytesIO,
        file_info: str,
        user_id: int
    ) -> None:

        user: UserResponseDTO | None = await self.repositories.database.users.get_user_by_id(user_id=user_id)

        if not user:
            raise NotFoundException()

        picture_url = await self.repositories.media.upload_file("PICTURES", file_info, file_stream)

        updated_user = UpdateUserRequestDTO(picture_url=picture_url)
        await self.repositories.database.users.update_user(user=updated_user)

    async def update_user(
        self,
        username: str | None,
        description: str | None,
        user_id: int
    ) -> int:
        user: UserResponseDTO | None = await self.repositories.database.users.get_user_by_id(user_id=user_id)

        if not user:
            raise NotFoundException()

        update_data = UpdateUserRequestDTO(
            username=username,
            description=description
        )

        return await self.repositories.database.users.update_user(user=update_data)

    async def delete_user(self, user_id: int) -> None:
        user: UserResponseDTO | None = await self.repositories.database.users.get_user_by_id(user_id=user_id)

        if not user:
            raise NotFoundException()

        await self.repositories.database.users.delete_user(user_id=user_id)


class ArtistsService(BaseService):
    repositories: ArtistsRepositories

    async def get_artist_id_by_user_id(self, user_id: int) -> int:
        artist_id: int | None = await self.repositories.database.artists.get_artist_id_by_user_id(user_id=user_id)

        if not artist_id:
            raise NotFoundException

        return artist_id

    async def get_artist_by_id(self, artist_id: int) -> ArtistResponseDTO:
        artist: ArtistResponseDTO | None = await self.repositories.database.artists.get_artist_by_id(artist_id=artist_id)

        if not artist:
            raise NotFoundException()

        return artist

    async def get_all_artists(self) -> ArtistsResponseDTO:
        return await self.repositories.database.artists.get_artists()

    async def update_artist(
        self,
        artist_id: int,
        description: str | None = None
    ) -> int:
        artist: ArtistResponseDTO | None = await self.repositories.database.artists.get_artist_by_id(artist_id=artist_id)

        if not artist:
            raise NotFoundException()

        updated_artist = UpdateArtistRequestDTO(
            id=artist_id,
            description=description,
        )
        return await self.repositories.database.artists.update_artist(artist=updated_artist)

    async def deactivate_artist(self, artist_id: int) -> None:
        artist: ArtistResponseDTO | None = await self.repositories.database.artists.get_artist_by_id(artist_id=artist_id)

        if not artist:
            raise NotFoundException()

        updated_artist = UpdateArtistRequestDTO(
            id=artist_id,
            description=None,
            is_available=False,
        )
        await self.repositories.database.artists.update_artist(artist=updated_artist)


class ProducersService(BaseService):
    repositories: ProducersRepositories

    async def get_producer_id_by_user_id(self, user_id: int) -> int:
        producer_id: int | None = await self.repositories.database.producers.get_producer_id_by_user_id(user_id=user_id)

        if not producer_id:
            raise NotFoundException

        return producer_id

    async def get_producer_by_id(self, producer_id: int) -> ProducerResponseDTO:
        producer: ProducerResponseDTO | None = await self.repositories.database.producers.get_producer_by_id(producer_id=producer_id)

        if not producer:
            raise NotFoundException()

        return producer

    async def get_all_producers(self) -> ProducersResponseDTO:
        return await self.repositories.database.producers.get_producers()

    async def update_producer(
        self,
        producer_id: int,
        description: str | None = None
    ) -> int:
        producer: ProducerResponseDTO | None = await self.repositories.database.producers.get_producer_by_id(producer_id=producer_id)

        if not producer:
            raise NotFoundException()

        updated_producer = UpdateProducerRequestDTO(
            id=producer_id,
            description=description
        )
        return await self.repositories.database.producers.update_producer(producer=updated_producer)

    async def deactivate_one_producer(self, producer_id: int) -> None:
        producer: ProducerResponseDTO | None = await self.repositories.database.producers.get_producer_by_id(producer_id=producer_id)

        if not producer:
            raise NotFoundException()

        updated_producer = UpdateProducerRequestDTO(
            id=producer_id,
            description=None,
            is_available=False,
        )
        await self.repositories.database.producers.update_producer(producer=updated_producer)


class AuthService(BaseService):
    repositories: AuthRepositories

    @staticmethod
    async def login(email: EmailStr, password: str) -> tuple[str, str, User]:

        user = await authenticate_user(email=email, password=password)
        if not user:
            raise NotFoundException

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token_ = create_refresh_token({"sub": str(user.id)})

        return access_token, refresh_token_, user

    @staticmethod
    async def refresh_token(user_id: int) -> tuple[str, str]:

        access_token = create_access_token({"sub": str(user_id)})
        refresh_token_ = create_refresh_token({"sub": str(user_id)})

        return access_token, refresh_token_

    async def spotify_callback(self, code) -> tuple[str, str]:  # type: ignore[no-untyped-def]
        # old functional
        access_token = await self.repositories.api.login(code=code)

        if access_token:

            user_data = await self.repositories.api.get_me(access_token=access_token)

            user = await self.repositories.database.users.get_user_by_email(email=user_data.get("email"))  # type: ignore[arg-type]
            if not user:
                user = CreateUserRequestDTO(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=None,
                    roles=[Role.artist, Role.artist, Role.producer],
                    birthday=datetime.today(),
                    tags=[],
                    access_level=AccessLevel.user
                )  # type: ignore[assignment]
                user_id: int = await self.repositories.database.users.create_user(user=user)  # type: ignore[arg-type]
                access_token = create_access_token({"sub": str(user_id)})
                refresh_token_ = create_refresh_token({"sub": str(user_id)})

                return access_token, refresh_token_

            else:
                access_token = create_access_token({"sub": str(user.id)})
                refresh_token_ = create_refresh_token({"sub": str(user.id)})

                return access_token, refresh_token_

        else:
            raise ServerError("Failed to obtain access token")


def get_users_repositories() -> UsersRepositories:
    return UsersRepositories(
        database=UsersDatabaseRepositories(
            users=init_users_postgres_repository(),
            tags=init_tags_postgres_repository(),
            artists=init_artists_postgres_repository(),
            producers=init_producers_postgres_repository()
        ),
        media=init_s3_repository()
    )


def get_users_service() -> UsersService:
    return UsersService(repositories=get_users_repositories())


def get_artists_repositories() -> ArtistsRepositories:
    return ArtistsRepositories(
        database=ArtistsDatabaseRepositories(artists=init_artists_postgres_repository()),
        media=init_s3_repository()
    )


def get_artists_service() -> ArtistsService:
    return ArtistsService(repositories=get_artists_repositories())


def get_producers_repositories() -> ProducersRepositories:
    return ProducersRepositories(
        database=ProducersDatabaseRepositories(producers=init_producers_postgres_repository()),
        media=init_s3_repository()
    )


def get_producers_service() -> ProducersService:
    return ProducersService(repositories=get_producers_repositories())


def get_auth_repositories() -> AuthRepositories:
    return AuthRepositories(
        database=AuthDatabaseRepositories(users=init_users_postgres_repository()),
        media=init_s3_repository()
    )


def get_auth_service() -> AuthService:
    return AuthService(repositories=get_auth_repositories())
