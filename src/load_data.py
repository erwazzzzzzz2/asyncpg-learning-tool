import asyncio
from conn import create_conn


async def run():
    conn = await create_conn("products")
    result = await conn.copy_to_table("brands", source="/datasets/brands.csv")
    print(result)


asyncio.get_event_loop().run_until_complete(run())
