from ..config.ConfigDB import async_session
from sqlalchemy.ext.asyncio import AsyncSession

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session