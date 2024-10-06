from src.core.config import settings
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

test_engine = create_async_engine(settings.db_url, echo=True)

sessionmaker_test = async_sessionmaker(test_engine)


async def test_connection_to_db():
    async with sessionmaker_test() as sesion:
        print(settings.db_url)
        test_request = await sesion.execute(text("select 'Hello world!'"))
        assert test_request.all() is not None
