from typing import Callable, Any

import pydantic
from fastapi import Request, Depends, Response
from sqlalchemy.sql.functions import current_user

from src.api.app import app, auth_v1
from src.exceptions import services, api
from src.schemas.auth import User


@app.middleware('http')
async def v1_exceptions_middleware(  # type: ignore[no-untyped-def]
    request: Request,
    call_next: Callable[[Request], Any],
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


@auth_v1.middleware('http')
async def v1_auth_exceptions_middleware(  # type: ignore[no-untyped-def]
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
