from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import ProductSchema
from ..models import ProductModel
from sqlalchemy.future import select
from sqlalchemy import update, delete

""""
    Responsible for performing operations on database.
"""

# CREATE operations
async def create_product(db: AsyncSession, product: ProductSchema.ProductCreate):
    db_product = ProductModel.Product(description=product.description, category=product.category, price=product.price, date=product.date)
    db.add(db_product)
    return db_product


# READ operations
async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    response = await db.execute(select(ProductModel.Product).offset(skip).limit(limit))
    return response.scalars().all()

async def get_product_by_id(db: AsyncSession, product_id: int):
    response = await db.execute(select(ProductModel.Product).where(ProductModel.Product.id == product_id))
    return response.scalars().first()

async def get_product_by_description(db: AsyncSession, product_description: str):
    response = await db.execute(select(ProductModel.Product).where(ProductModel.Product.description == product_description))
    return response.scalars().first()


# UPDATE operations
async def update_product(db: AsyncSession, product: ProductSchema.ProductCreate, product_id: int):
    response = await db.execute(update(ProductModel.Product).where(ProductModel.Product.id == product_id).values(product.__dict__))
    return response


# DELETE operations
async def delete_product(db: AsyncSession, product_id: int):
    response = await db.execute(delete(ProductModel.Product).where(ProductModel.Product.id == product_id))
    return response
