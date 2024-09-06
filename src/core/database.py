from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.core.config import settings


engine = create_async_engine(url=settings.db_url, echo=settings.echo)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
