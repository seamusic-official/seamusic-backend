from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src_.core.config import settings

test_engine = create_async_engine(settings.db_url, echo=True)

sessionmaker_test = async_sessionmaker(test_engine)


async def test_connection_to_db() -> None:
    async with sessionmaker_test() as session:
        test_request = await session.execute(text("select 'Hello world!'"))
        assert test_request.all() is not None
