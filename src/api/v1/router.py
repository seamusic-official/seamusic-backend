from fastapi import APIRouter

from src.api.v1.routes.albums import albums
from src.api.v1.routes.auth import auth
from src.api.v1.routes.beatpacks import beatpacks
from src.api.v1.routes.beats import beats
from src.api.v1.routes.comments import comments
from src.api.v1.routes.licenses import licenses
from src.api.v1.routes.messages import messages
from src.api.v1.routes.soundkits import soundkits
from src.api.v1.routes.spotify import spotify
from src.api.v1.routes.squads import squads
from src.api.v1.routes.tags import tags
from src.api.v1.routes.tracks import tracks

router = APIRouter()

router.include_router(auth)
router.include_router(licenses)
router.include_router(beats)
router.include_router(beatpacks)
router.include_router(tracks)
router.include_router(albums)
router.include_router(soundkits)
router.include_router(messages)
router.include_router(spotify)
router.include_router(tags)
router.include_router(squads)
router.include_router(comments)
