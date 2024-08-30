from datetime import datetime, timedelta, UTC

from fastapi import Depends, Request
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.core.config import settings
from src.exceptions.api import UnauthorizedException
from src.schemas.auth import User
from src.dtos.database.auth import User as _User
from src.services.auth import UsersService

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 14  # 14 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.jwt_secret_key
JWT_REFRESH_SECRET_KEY = settings.jwt_refresh_secret_key


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, real_hashed_pass: str) -> bool:
    return password_context.verify(password, real_hashed_pass)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expires_delta = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires_delta})

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expires_delta = datetime.now(UTC) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires_delta})

    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def authenticate_user(
    email: EmailStr,
    password: str,
    service: UsersService = Depends(),
) -> _User | None:

    user = await service.get_user_by_email(email=email)

    if user and verify_password(password, user.password):
        return _User(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            picture_url=user.picture_url,
            birthday=user.birthday,
            roles=user.roles
        )
    return None


async def get_refresh_token(request: Request) -> str:
    token = request.cookies.get("refreshToken")
    if not token:
        raise UnauthorizedException()
    return token


async def get_current_user(
    token: str = Depends(get_refresh_token),
    service: UsersService = Depends(),
) -> User:
    try:
        payload = jwt.decode(token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise UnauthorizedException()

    expire: str = payload.get("exp")

    if (not expire) or (int(expire) < datetime.now(UTC).timestamp()):
        raise UnauthorizedException()
    user_id: str = payload.get("sub")
    if not user_id:
        raise UnauthorizedException()
    user = await service.get_user_by_id(user_id=int(user_id))
    if not user:
        raise UnauthorizedException()

    return User(
        id=user.id,
        username=user.username,
        email=user.email,
        password=user.password,
        picture_url=user.picture_url,
        birthday=user.birthday
    )
