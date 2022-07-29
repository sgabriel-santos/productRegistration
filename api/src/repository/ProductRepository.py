from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import ProductSchema
from ..models import ProductModel
from sqlalchemy.future import select
from sqlalchemy import update, delete

""""
    Responsible for performing operations on database.
"""

# READ operations
async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    response = await db.execute(select(ProductModel.Product).offset(skip).limit(limit))
    return response.scalars().all()