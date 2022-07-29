from sys import prefix
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..middleware.utils_db import get_session
from ..schemas import ProductSchema
from ..controllers import ProductController 

""""
    Responsible for managing product routes        
"""

router = APIRouter(tags=["product"], prefix='/product')

# GET method
@router.get("/", response_model=List[ProductSchema.Product])
async def get_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    """
    Get produts from database. The amount of product depends on the parameters.

    Parameters:
    -------
    **skip** (int): Skips the first products according the param value. *Default is 0*.\n
    **limit** (int): Indicates the number of products that will be returned.

    Returns:
    -------
    product list.
    """
    return await ProductController.get_products(db, skip=skip, limit=limit)