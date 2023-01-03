from os import environ
import asyncpg
from sqlalchemy import create_engine, databases
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DB_USER = environ.get('DB_USER')
DB_PASSWORD = environ.get('DB_PASS')
DB_HOST = environ.get('DB_HOST')

TESTING = environ.get("TESTING")

if TESTING:
    # Use separate DB for tests
    DB_NAME = "my_db"
    TEST_SQLALCHEMY_DATABASE_URL = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
    database = create_async_engine(TEST_SQLALCHEMY_DATABASE_URL)
else:
    DB_NAME = "my_db"
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
    database = create_async_engine(SQLALCHEMY_DATABASE_URL)

