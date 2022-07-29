from pydantic import BaseModel, Field
from datetime import datetime

class ProductBase(BaseModel):
    description: str = Field(..., description="Product description", example="This is the product description")
    category: str = Field(..., description="Product category", example="Livro")


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int = Field(..., description="Product id", example="110")
    date: datetime = Field(..., description="Date and time the product was created")
    
    class Config:
        orm_mode = True