from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    description: str = Field(..., description="Product description", example="This is the product description")
    category: str = Field(..., description="Product category", example="Livro")
    date: str = Field(..., description="Product purchase date", example="30/07/2022")
    price: float = Field(..., description="Price of the product", example="26.99")


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int = Field(..., description="Product id", example="110")
    
    class Config:
        orm_mode = True