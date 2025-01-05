from fastapi import FastAPI

from src.app.music.albums.api.routes import router as albums

app = FastAPI(
    title='SeaMusic',
    summary='Web app for music collaborations',
    version='0.1.0',
    root_path='/',
    redoc_url='/docs',
    docs_url='/swagger',
)
app.include_router(albums)
