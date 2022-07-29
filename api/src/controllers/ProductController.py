from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from ..repository import ProductRepository
from ..schemas import ProductSchema

""""
    Responsible for managing the flow to do CRUD on product table.
"""

# CREATE operations
async def create_product(db: AsyncSession, product: ProductSchema.ProductCreate):
    db_product = await ProductRepository.get_product_by_description(db, product_description=product.description)
    if db_product:
        raise HTTPException(status_code=409, detail="Description already registered")
    
    try:
        db_product = await ProductRepository.create_product(db, product=product)
        await db.commit()
        return db_product
    
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server Error")

# READ operations
async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await ProductRepository.get_products(db, skip=skip, limit=limit)

async def get_product_by_id(db: AsyncSession, product_id: int):
    db_product = await ProductRepository.get_product_by_id(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not Found")
    return db_product


# UPDATE operations
async def update_product(db: AsyncSession, product: ProductSchema.ProductCreate, product_id: int):
    db_product = await ProductRepository.get_product_by_id(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    
    try:
        await ProductRepository.update_product(db, product=product, product_id=product_id)
        await db.commit()
        return product
    except:
        await db.rollback()
        raise HTTPException(status_code=402, detail="Server Error")


# DELETE operations
async def delete_product(db: AsyncSession, product_id: int):
    db_product = await ProductRepository.get_product_by_id(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product Not Found")

    try:
        await ProductRepository.delete_product(db, product_id=product_id)
        await db.commit()
        return db_product
    except:
        await db.rollback()
        raise HTTPException(status_code=402, detail="Server Error")
