from fastapi import APIRouter

from src.api.v1.albums import albums
from src.api.v1.auth import users, artists, producers
from src.api.v1.beatpacks import beatpacks
from src.api.v1.beats import beats
from src.api.v1.comments import comments
from src.api.v1.licenses import licenses
from src.api.v1.messages import messages
from src.api.v1.soundkits import soundkits
from src.api.v1.spotify import spotify
from src.api.v1.squads import squads
from src.api.v1.subscriptions import subscription
from src.api.v1.tags import tags
from src.api.v1.tracks import tracks


router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(users)
router.include_router(artists)
router.include_router(producers)
router.include_router(licenses)
router.include_router(beats)
router.include_router(beatpacks)
router.include_router(tracks)
router.include_router(albums)
router.include_router(soundkits)
router.include_router(messages)
router.include_router(spotify)
router.include_router(subscription)
router.include_router(tags)
router.include_router(squads)
router.include_router(comments)
