from sqlalchemy import select
from src.ozon_bot.db.data_base import async_session_maker
from src.ozon_bot.models.db_models import User, Track

async def get_or_create_user(telegram_id: int, username: str = None):
    async with async_session_maker() as session:
        result = await session.execute(select(User).where(User.id == telegram_id))
        user = result.scalar_one_or_none()
        if not user:
            user = User(id=telegram_id, username=username)
            session.add(user)
            await session.commit()
        return user

async def add_track(user_id: int, url: str, target_price: float, product_name: str = None) -> int:
    async with async_session_maker() as session:
        track = Track(
            user_id=user_id,
            product_url=url,
            target_price=target_price,
            product_name=product_name
        )
        session.add(track)
        await session.commit()
        await session.refresh(track)
        return track.id

async def get_user_tracks(user_id: int):
    async with async_session_maker() as session:
        result = await session.execute(
            select(Track).where(Track.user_id == user_id).order_by(Track.created_at.desc())
        )
        return result.scalars().all()