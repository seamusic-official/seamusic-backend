from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1 import v1


def create_app() -> FastAPI:
    _app = FastAPI(
        title="SeaMusic",
        description="High-perfomance musical application",
        version='0.1.0',
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
