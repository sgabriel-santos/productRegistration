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

@router.get("/{product_id}", response_model=ProductSchema.Product)
async def get_product_by_id(product_id: int, db: AsyncSession = Depends(get_session)):
    """
    Get product from database by id.

    Parameters:
    -------
    **product_id** (int): id used to find the correct Product.

    Returns:
    -------
    the product if it exists.
    """
    return await ProductController.get_product_by_id(db, product_id=product_id)


# POST method
@router.post("/", response_model=ProductSchema.Product)
async def create_product(product: ProductSchema.ProductCreate, db: AsyncSession = Depends(get_session)):
    """
    Create new product on database.

    Parameters:
    -------
    **product** (ProductCreate): Pydantic model with all product information.\n

    Returns:
    -------
    The new product created.
    """
    print('----> Criando Produto')
    print(product)
    return await ProductController.create_product(db=db, product=product)


# PUT method
@router.put("/{product_id}", response_model=ProductSchema.ProductCreate)
async def update_product(product: ProductSchema.Product, product_id: int, db: AsyncSession = Depends(get_session)):
    """
    Update a product from database.

    Parameters:
    -------
    **product** (UserCreate): Product with new informations.\n
    **product_id** (int): Product id to be update.

    Returns:
    -------
    Product with the new information.
    """
    return await ProductController.update_product(db=db, product=product, product_id=product_id)


# DELETE method
@router.delete("/{product_id}", response_model=ProductSchema.Product)
async def delete_user(product_id: int, db: AsyncSession = Depends(get_session)):
    """
    Delete a product from database.

    Parameters:
    -------
    **product_id** (int): product id to be deleted.

    Returns:
    -------
    The product deleted from database.
    """
    return await ProductController.delete_product(db, product_id=product_id)