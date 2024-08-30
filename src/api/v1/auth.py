from fastapi import (
    UploadFile,
    File,
    APIRouter,
    Depends,
    Response,
    status,
)

from src.schemas.auth import (
    SRefreshTokenResponse,
    SSpotifyCallbackResponse,
    SArtistResponse,
    SProducerResponse,
    SRegisterUserResponse,
    SRegisterUserRequest,
    SLoginRequest,
    User,
    SMeResponse,
    SUsersResponse,
    SUserResponse,
    SUpdateUserPictureResponse,
    SUpdateUserRequest,
    SUpdateUserResponse,
    SDeleteUserResponse,
    SMeAsArtistResponse,
    SArtistsResponse,
    SUpdateArtistRequest,
    SUpdateArtistResponse,
    SDeleteArtistResponse,
    SProducersResponse,
    Producer,
    SMeAsProducerResponse,
    SUpdateProducerRequest,
    SUpdateProducerResponse,
    SDeleteProducerResponse,
    SLoginResponse, Artist,
)
from src.services.auth import (
    AuthService,
    ArtistsService,
    ProducersService,
    UsersService,
    get_users_service,
    get_artists_service,
    get_producers_service,
    get_auth_service
)
from src.utils.auth import get_current_user
from src.utils.files import unique_filename, get_file_stream

auth_v1 = APIRouter(prefix='/v1/auth')  # included directly in main app to avoid using ExceptionMiddleware

users = APIRouter(prefix='/auth/users', tags=['Users'])
artists = APIRouter(prefix='/auth/artists', tags=['Artists'])
producers = APIRouter(prefix='/auth/producers', tags=['Producers'])


@users.get(
    path='/me',
    response_model=SMeResponse,
    summary='Get details of currently logged in user',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SMeResponse}},
)
async def get_me(user: User = Depends(get_current_user)) -> SMeResponse:
    return SMeResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        picture_url=user.picture_url,
        birthday=user.birthday
    )


@users.get(
    path='/',
    response_model=SUsersResponse,
    summary='Get all users',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SUsersResponse}},
)
async def get_users(service: UsersService = Depends(get_users_service)) -> SUsersResponse:
    response = await service.get_all_users()

    users_: list[User] = list(map(
        lambda user: User(
            id=user.id,
            username=user.username,
            email=user.email,
            picture_url=user.picture_url,
            birthday=user.birthday,
        ),
        response.users
    ))

    return SUsersResponse(users=users_)


@users.get(
    path='/{user_id}',
    response_model=SUserResponse,
    summary='Get a user by ID',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SUserResponse}},
)
async def get_one(
    user_id: int,
    service: UsersService = Depends(get_users_service)
) -> SUserResponse:

    user = await service.get_user_by_id(user_id=user_id)
    return SUserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        picture_url=user.picture_url,
        birthday=user.birthday
    )


@users.put(
    path='/{user_id}/picture',
    summary='Update image info by id',
    response_model=SUpdateUserPictureResponse,
    responses={status.HTTP_200_OK: {'model': SUpdateUserPictureResponse}},
)
async def update_user_picture(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    service: UsersService = Depends(get_users_service)
) -> SUpdateUserPictureResponse:

    await service.update_user_picture(
        user_id=user.id,
        file_info=unique_filename(file),
        file_stream=await get_file_stream(file)
    )

    return SUpdateUserPictureResponse()


@users.put(
    path='/{user_id}',
    summary='Update user info by id',
    response_model=SUpdateUserResponse,
    responses={status.HTTP_200_OK: {'model': SUpdateUserResponse}},
)
async def update_user(
    data: SUpdateUserRequest,
    user: User = Depends(get_current_user),
    service: UsersService = Depends(get_users_service)
) -> SUpdateUserResponse:

    user_id = await service.update_user(
        username=data.username,
        description=data.description,
        user_id=user.id,
    )
    return SUpdateUserResponse(id=user_id)


@users.delete(
    path='/{user_id}',
    summary='Delete user by id',
    response_model=SDeleteUserResponse,
    responses={status.HTTP_200_OK: {'model': SDeleteUserResponse}},
)
async def delete_users(
    user: User = Depends(get_current_user),
    service: UsersService = Depends(get_users_service)
) -> SDeleteUserResponse:

    await service.delete_user(user_id=user.id)

    return SDeleteUserResponse()


@artists.get(
    path='/me',
    summary='Get my artist profile',
    status_code=status.HTTP_200_OK,
    response_model=SMeAsArtistResponse,
    responses={status.HTTP_200_OK: {'model': SMeAsArtistResponse}},
)
async def get_me_as_artist(
    user: User = Depends(get_current_user),
    service: ArtistsService = Depends(get_artists_service)
) -> SMeAsArtistResponse:

    artist_id: int = await service.get_artist_id_by_user_id(user_id=user.id)
    artist = await service.get_artist_by_id(artist_id=artist_id)

    return SMeAsArtistResponse(
        id=artist_id,
        description=artist.description,
        user=User(
            id=artist.user.id,
            username=artist.user.username,
            email=artist.user.email,
            picture_url=artist.user.picture_url,
            birthday=artist.user.birthday,
        )
    )


@artists.get(
    path='/',
    response_model=SArtistsResponse,
    summary='Get all artists',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SArtistsResponse}},
)
async def get_artists(service: ArtistsService = Depends(get_artists_service)) -> SArtistsResponse:

    response = await service.get_all_artists()

    artists_ = list(map(
        lambda artist: Artist(
            id=artist.id,
            user=User(
                id=artist.user.id,
                username=artist.user.username,
                email=artist.user.email,
                picture_url=artist.user.picture_url,
                birthday=artist.user.birthday,
            ),
            description=artist.description
        ),
        response.artists
    ))

    return SArtistsResponse(artists=artists_)


@artists.get(
    path='/{artist_id}',
    response_model=SArtistResponse,
    summary='Get one artists by id',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SArtistResponse}},
)
async def get_one_artist(
    artist_id: int,
    service: ArtistsService = Depends(get_artists_service)
) -> SArtistResponse:

    artist = await service.get_artist_by_id(artist_id=artist_id)
    return SArtistResponse(
        id=artist.id,
        description=artist.description,
        user=User(
            id=artist.user.id,
            username=artist.user.username,
            email=artist.user.email,
            picture_url=artist.user.picture_url,
            birthday=artist.user.birthday,
        ),
    )


@artists.put(
    path='/{artist_id}',
    response_model=SUpdateArtistResponse,
    summary='Update artist by id',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SUpdateArtistResponse}},
)
async def update_artist(
    data: SUpdateArtistRequest,
    user: User = Depends(get_current_user),
    service: ArtistsService = Depends(get_artists_service)
) -> SUpdateArtistResponse:

    artist_id = await service.update_artist(
        artist_id=await service.get_artist_id_by_user_id(user_id=user.id),
        description=data.description
    )

    return SUpdateArtistResponse(id=artist_id)


@artists.delete(
    path='/{artist_id}',
    summary='Deactivate artist profile by id',
    response_model=SDeleteArtistResponse,
    responses={status.HTTP_200_OK: {'model': SDeleteArtistResponse}},
)
async def deactivate_artists(
    user: User = Depends(get_current_user),
    service: ArtistsService = Depends(get_artists_service)
) -> SDeleteArtistResponse:

    artist_id = await service.get_artist_id_by_user_id(user_id=user.id)
    await service.deactivate_artist(artist_id=artist_id)
    return SDeleteArtistResponse()


@producers.get(
    path='/me',
    summary='Get my producer profile',
    status_code=status.HTTP_200_OK,
    response_model=SMeAsProducerResponse,
    responses={status.HTTP_200_OK: {'model': SMeAsProducerResponse}},
)
async def get_me_as_producer(
    user: User = Depends(get_current_user),
    service: ProducersService = Depends(get_producers_service)
) -> SMeAsProducerResponse:

    producer_id = await service.get_producer_id_by_user_id(user_id=user.id)
    producer = await service.get_producer_by_id(producer_id=producer_id)

    return SMeAsProducerResponse(
        id=producer.id,
        description=producer.description,
        user=User(
            id=producer.user.id,
            username=producer.user.username,
            email=producer.user.email,
            picture_url=producer.user.picture_url,
            birthday=producer.user.birthday,
        ),
    )


@producers.get(
    path='/',
    summary='Get all producers',
    status_code=status.HTTP_200_OK,
    response_model=SProducersResponse,
    responses={status.HTTP_200_OK: {'model': SProducersResponse}},
)
async def get_all_producers(service: ProducersService = Depends(get_producers_service)) -> SProducersResponse:

    response = await service.get_all_producers()

    producers_ = list(map(
        lambda producer: Producer(
            id=producer.id,
            description=producer.description,
            user=User(
                id=producer.user.id,
                username=producer.user.username,
                email=producer.user.email,
                picture_url=producer.user.picture_url,
                birthday=producer.user.birthday,
            ),
        ),
        response.producers
    ))

    return SProducersResponse(producers=producers_)


@producers.get(
    path='/{producer_id}',
    response_model=SProducerResponse,
    summary='Get one producer by id',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SProducerResponse}},
)
async def get_one_producer(
    producer_id: int,
    service: ProducersService = Depends(get_producers_service)
) -> SProducerResponse:

    producer = await service.get_producer_by_id(producer_id=producer_id)

    return SProducerResponse(
        id=producer.id,
        description=producer.description,
        user=User(
            id=producer.user.id,
            username=producer.user.username,
            email=producer.user.email,
            picture_url=producer.user.picture_url,
            birthday=producer.user.birthday,
        ),
    )


@producers.put(
    path='/{producer_id}',
    response_model=SUpdateProducerResponse,
    summary='Update producer by id',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SUpdateProducerResponse}},
)
async def update_one_producer(
    data: SUpdateProducerRequest,
    user: User = Depends(get_current_user),
    service: ProducersService = Depends(get_producers_service)
) -> SUpdateProducerResponse:

    producer_id = await service.update_producer(
        producer_id=await service.get_producer_id_by_user_id(user_id=user.id),
        description=data.description
    )

    return SUpdateProducerResponse(id=producer_id)


@producers.post(
    path='/{producer_id}',
    summary='Deactivate artist profile by id',
    response_model=SDeleteProducerResponse,
    responses={status.HTTP_200_OK: {'model': SDeleteProducerResponse}},
)
async def deactivate_one_producer(
    user: User = Depends(get_current_user),
    service: ProducersService = Depends(get_producers_service)
) -> SDeleteProducerResponse:

    producer_id = await service.get_producer_id_by_user_id(user_id=user.id)
    await service.deactivate_one_producer(producer_id=producer_id)

    return SDeleteProducerResponse()


@auth_v1.post(
    path='/register',
    summary='Create new user',
    response_model=SRegisterUserResponse,
    responses={status.HTTP_201_CREATED: {'model': SRegisterUserResponse}},
)
async def register(
    user: SRegisterUserRequest,
    service: UsersService = Depends(get_users_service)
) -> SRegisterUserResponse:

    user_id = await service.create_new_user(
        username=user.username,
        password=user.password,
        email=user.email,
        roles=user.roles,
        birthday=user.birthday,
        tags=user.tags
    )

    return SRegisterUserResponse(id=user_id)


@auth_v1.post(
    path='/login',
    summary='Signin',
    response_model=SLoginResponse,
    responses={status.HTTP_200_OK: {'model': SLoginResponse}},
)
async def login(
    data: SLoginRequest,
    response: Response,
    service: AuthService = Depends(get_auth_service)
) -> SLoginResponse:

    access_token, refresh_token_, user = await service.login(
        email=data.email,
        password=data.password,
    )

    response.set_cookie('accessToken', access_token)
    response.set_cookie('refreshToken', refresh_token_)

    return SLoginResponse(
        access_token=access_token,
        refresh_token=refresh_token_,
        user=User(
            id=user.id,
            username=user.username,
            email=user.email,
            picture_url=user.picture_url,
            birthday=user.birthday
        )
    )


@auth_v1.post(
    path='/refresh',
    response_model=SRefreshTokenResponse,
    summary='Refresh auth token',
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SRefreshTokenResponse}},
)
async def refresh_token(
    user: User = Depends(get_current_user),
    service: AuthService = Depends(get_auth_service)
) -> SRefreshTokenResponse:

    access_token, refresh_token_ = await service.refresh_token(user_id=user.id)
    return SRefreshTokenResponse(
        accessToken=access_token,
        refreshToken=refresh_token_
    )


@auth_v1.post(
    path='/callback',
    response_model=SSpotifyCallbackResponse,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {'model': SSpotifyCallbackResponse}},
)
async def spotify_callback(
    code: str,
    user: User = Depends(get_current_user),
    service: AuthService = Depends(get_auth_service)
) -> SSpotifyCallbackResponse:

    access_token, refresh_token_ = await service.spotify_callback(code=code)

    return SSpotifyCallbackResponse(
        access_token=access_token,
        refresh_token=access_token,
        user=user
    )
