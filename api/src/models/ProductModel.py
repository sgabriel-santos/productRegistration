from sqlalchemy import Column, Float, Integer, String
from ..config.ConfigDB import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(64))
    category = Column(String(50))
    price = Column(Float)