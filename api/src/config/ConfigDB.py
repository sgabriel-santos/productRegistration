from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_DIALECT = 'mysql+aiomysql'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'desafio123'
DATABASE_HOST = 'localhost:3307'
DATABASE = 'appdatabase'

DATABASE_URL = \
    f'{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE}'

engine = create_async_engine(DATABASE_URL, echo=True)
async_session  = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

origins = [
    "http://localhost:4200" # Temporary. Just to Test the frontend
]


Base = declarative_base()