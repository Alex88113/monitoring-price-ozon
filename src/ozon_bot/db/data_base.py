from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from src.ozon_bot.configs.config_db import settings

class Base(DeclarativeBase):
    pass

# Импортируем модели ПОСЛЕ определения Base, чтобы SQLAlchemy их увидел
from src.ozon_bot.models.db_models import User, Track

engine = create_async_engine(
    settings.database_url.replace("postgresql://", "postgresql+asyncpg://"),
    echo=True
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)