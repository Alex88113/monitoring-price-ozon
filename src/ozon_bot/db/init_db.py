import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from src.ozon_bot.db.data_base import Base
from src.ozon_bot.configs.config_db import settings

async def create_tables():
    db_url = settings.database_url.replace("postgresql://", "postgresql+asyncpg://")
    engine = create_async_engine(db_url, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("✅ Таблицы users и tracks созданы!")

if __name__ == "__main__":
    asyncio.run(create_tables())