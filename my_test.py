from os import environ
import asyncpg
from sqlalchemy import create_engine, databases
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.models.users import users_table

DB_USER = environ.get('DB_USER')
DB_PASSWORD = environ.get('DB_PASS')
DB_HOST = environ.get('DB_HOST')

TESTING = environ.get("TESTING")


DB_NAME = "my_db"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
database = create_async_engine(SQLALCHEMY_DATABASE_URL)

async def async_main():
    query = users_table.insert().values(
        email='user@email.com',
        name='ExampleName',
        hashed_password=f"dsadsad324dsads")

    async with database.begin() as conn:
        l = await conn.execute(query)
        print(l.inserted_primary_key)

if __name__ == '__main__':
    asyncio.run(async_main())
# .begin() для insert
# .connect()для select
# update/delete проверить