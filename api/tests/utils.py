from .configTestDB import Base, engine_test

async def drop_and_create_table():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)