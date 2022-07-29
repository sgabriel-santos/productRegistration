from sqlalchemy.orm import sessionmaker
from ..src.middleware.utils_db import get_session
from ..src.api import app
from ..src.config.ConfigDB import Base
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

TEST_DATABASE_DIALECT = 'mysql+aiomysql'
TEST_DATABASE_USER = 'root'
TEST_DATABASE_PASSWORD = 'desafio123'
TEST_DATABASE_HOST = 'localhost:3307'
TEST_DATABASE = 'testappdatabase'

TEST_DATABASE_URL = \
    f'{TEST_DATABASE_DIALECT}://{TEST_DATABASE_USER}:{TEST_DATABASE_PASSWORD}@{TEST_DATABASE_HOST}/{TEST_DATABASE}'

engine_test = create_async_engine(TEST_DATABASE_URL, echo=True)
async_session_test  = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


async def override_get_session() -> AsyncSession:
    async with async_session_test() as session_test:
        yield session_test
    
app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)