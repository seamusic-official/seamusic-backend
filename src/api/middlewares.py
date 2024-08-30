import pydantic
from fastapi import Request, Depends, Response
from sqlalchemy.sql.functions import current_user

from src.exceptions import services, api
from src.schemas.auth import User


class V1ExceptionsMiddleware:
    async def __call__(  # type: ignore[no-untyped-def]
        self,
        request: Request,
        call_next,
        user: User | None = Depends(current_user)
    ) -> Response:

        if not user:
            raise api.UnauthorizedException("Unauthorized")

        try:
            response = await call_next(request)

        except services.InvalidRequestException as e:
            raise api.InvalidRequestException(detail=e.detail)
        except pydantic.ValidationError:
            raise api.InvalidRequestException()
        except services.NoRightsException as e:
            raise api.NoRightsException(detail=e.detail)
        except services.NotFoundException as e:
            raise api.NotFoundException(detail=e.detail)
        except services.ServerError as e:
            raise api.CustomException(status_code=500, detail=e.detail)

        return response


class V1AuthExceptionsMiddleware:
    async def __call__(  # type: ignore[no-untyped-def]
        self,
        request: Request,
        call_next
    ) -> Response:
        try:
            response = await call_next(request)
        except services.InvalidRequestException as e:
            raise api.InvalidRequestException(detail=e.detail)
        except pydantic.ValidationError:
            raise api.InvalidRequestException()
        except services.NoRightsException as e:
            raise api.NoRightsException(detail=e.detail)
        except services.NotFoundException as e:
            raise api.NotFoundException(detail=e.detail)
        except services.ServerError as e:
            raise api.CustomException(status_code=500, detail=e.detail)

        return response
