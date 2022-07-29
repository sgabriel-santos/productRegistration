from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..repository import ProductRepository
from ..schemas import ProductSchema

""""
    Responsible for managing the flow to do CRUD on product table and create the necessary logs.
"""

# READ operations
async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await ProductRepository.get_products(db, skip=skip, limit=limit)