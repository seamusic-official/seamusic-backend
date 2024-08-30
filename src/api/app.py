from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView

from src.api.middlewares import V1AuthExceptionsMiddleware, V1ExceptionsMiddleware
from src.api.v1 import v1
from src.api.v1.auth import auth_v1
from src.core.database import engine
from src.models.auth import User, ProducerProfile, ArtistProfile
from src.models.beatpacks import Beatpack
from src.models.beats import Beat
from src.models.soundkits import Soundkit
from src.models.squads import Squad
from src.models.tags import Tag


class BeatsAdmin(ModelView, model=Beat):
    column_list = [Beat.id, Beat.title]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]


class SquadAdmin(ModelView, model=Squad):
    column_list = [Squad.id, Squad.name]


class TagAdmin(ModelView, model=Tag):
    column_list = [Tag.id, Tag.name]


class SoundkitAdmin(ModelView, model=Soundkit):
    column_list = [Tag.id, Soundkit.name]


class ProducerProfileAdmin(ModelView, model=ProducerProfile):
    column_list = [ProducerProfile.id, ProducerProfile.user]


class ArtistProfileAdmin(ModelView, model=ArtistProfile):
    column_list = [ArtistProfile.id, ArtistProfile.user]


class BeatpackAdmin(ModelView, model=Beatpack):
    column_list = [Beatpack.id, Beatpack.title]


def create_app() -> FastAPI:

    app_ = FastAPI(
        title="SeaMusic",
        description="High-perfomance musical application",
    )

    admin = Admin(app_, engine)

    admin.add_view(SoundkitAdmin)
    admin.add_view(TagAdmin)
    admin.add_view(SquadAdmin)
    admin.add_view(BeatsAdmin)
    admin.add_view(BeatpackAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ProducerProfileAdmin)
    admin.add_view(ArtistProfileAdmin)

    origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

    app_.include_router(v1)

    app_.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_credentials=True,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app_.add_middleware(V1ExceptionsMiddleware)  # type: ignore

    auth_v1_app = FastAPI()
    auth_v1_app.include_router(auth_v1)
    auth_v1_app.add_middleware(V1AuthExceptionsMiddleware)  # type: ignore

    app_.mount(path='/', app=auth_v1_app)

    return app_


if __name__ == '__main__':
    app = create_app()
