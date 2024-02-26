import asyncio

from conn import create_conn


async def get_products():
    connection = await create_conn("products")

    res = await connection.execute("SELECT * FROM brands")
    print(res)
    await connection.close()


asyncio.run(get_products())
