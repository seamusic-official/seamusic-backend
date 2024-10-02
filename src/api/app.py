from typing import Callable, Any

import pydantic
from fastapi import FastAPI, Request, Depends, Response
from fastapi.middleware.cors import CORSMiddleware

from src import exceptions as services
from src.api.v1 import v1, exceptions as api
from src.api.v1.utils.auth import get_current_user
from src.models.auth import User


def create_app() -> FastAPI:
    _app = FastAPI(
        title="SeaMusic",
        description="High-perfomance musical application",
        version='0.1.0',
        docs_url='/',
        redoc_url='/docs',
    )

    _app.include_router(v1)

    _app.add_middleware(
        CORSMiddleware,  # type: ignore[arg-type]
        allow_credentials=True,
        allow_origins=[
            "http://127.0.0.1:5173",
            "http://localhost:5173",
        ],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = create_app()


@app.middleware('http')
async def v1_exceptions_middleware(
    request: Request,
    call_next: Callable[[Request], Any],
    user: User | None = Depends(get_current_user)
) -> Response:
    if not user:
        raise api.UnauthorizedException(detail="Unauthorized")

    try:
        response = await call_next(request)
    except services.InvalidRequestException as e:
        raise api.InvalidRequestException(detail=e.detail)
    except pydantic.ValidationError as e:
        raise api.InvalidRequestException(detail=e.title)
    except services.NoRightsException as e:
        raise api.NoRightsException(detail=e.detail)
    except services.NotFoundException as e:
        raise api.NotFoundException(detail=e.detail)
    except services.ServerError as e:
        raise api.CustomException(status_code=500, detail=e.detail)

    return response
