import asyncio

from asyncpg import DatabaseDroppedError, DuplicateDatabaseError, DuplicateTableError

from conn import create_conn

CREATE_BRAND_TABLE = """ CREATE TABLE brand (
            brand_id INTEGER PRIMARY KEY,
            brand_name VARCHAR(255) NOT NULL
        )"""

CREATE_PRODUCT_TABLE = """ CREATE TABLE product (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            FOREIGN KEY (brand_id)
            REFERENCES brand (brand_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )"""

SQL_STATEMENTS = [
    CREATE_BRAND_TABLE,
    CREATE_PRODUCT_TABLE,
]


async def create_db():
    conn = await create_conn()
    try:
        status = await conn.execute("CREATE DATABASE products")
        print(status)
    except DuplicateDatabaseError:
        print("db exists")
    finally:
        await conn.close()


async def create_db_tables():
    conn = await create_conn("products")
    print("Creating the product database...")
    try:
        await conn.execute(CREATE_BRAND_TABLE)
        await conn.execute(CREATE_PRODUCT_TABLE)

    except DuplicateTableError as e:
        print("Table already exists")
        print(e)

    print("Finished creating the product database!")
    await conn.close()


asyncio.run(create_db())
asyncio.run(create_db_tables())
