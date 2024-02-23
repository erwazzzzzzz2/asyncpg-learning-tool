import asyncio

from asyncpg import DuplicateDatabaseError, DuplicateTableError

from conn import create_conn

CREATE_BRAND_TABLE = """ CREATE TABLE brand (
            brand_id SERIAL PRIMARY KEY,
            brand_name VARCHAR(255) NOT NULL
        )"""

CREATE_PRODUCT_TABLE = """ CREATE TABLE product (
            product_id SERIAL PRIMARY KEY,
            FOREIGN KEY (brand_id)
            REFERENCES brand (brand_id)
            ON UPDATE CASCADE ON DELETE CASCADE
            product_name VARCHAR(255) NOT NULL
        )"""

SQL_STATEMENTS = [
    CREATE_BRAND_TABLE,
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
    for statement in SQL_STATEMENTS:
        try:
            status = await conn.execute(statement)
            print(status)
        except DuplicateTableError:
            print(f"Table for command {statement} already exists")

    print("Finished creating the product database!")
    await conn.close()


async def async_main():
    await asyncio.gather(create_db(), create_db_tables())


asyncio.run(async_main())
