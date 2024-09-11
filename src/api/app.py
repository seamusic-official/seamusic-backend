from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.middlewares import V1AuthExceptionsMiddleware, V1ExceptionsMiddleware
from src.api.v1 import v1
from src.api.v1.auth import auth_v1


def create_app() -> FastAPI:

    app_ = FastAPI(
        title="SeaMusic",
        description="High-perfomance musical application",
    )

    origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

    app_.include_router(v1)

    app_.add_middleware(
        CORSMiddleware,  # type: ignore[arg-type]
        allow_credentials=True,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app_.add_middleware(V1ExceptionsMiddleware)  # type: ignore[arg-type]

    auth_v1_app = FastAPI()
    auth_v1_app.include_router(auth_v1)
    auth_v1_app.add_middleware(V1AuthExceptionsMiddleware)  # type: ignore

    app_.mount(path='/', app=auth_v1_app)

    return app_


app = create_app()
